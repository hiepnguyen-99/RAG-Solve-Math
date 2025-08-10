from flask import Flask, render_template, request, jsonify, session
import uuid
import time
from datetime import datetime
import os
import sys
import markdown
import re
import json
from dotenv import load_dotenv
import base64
from PIL import Image
import io
import google.generativeai as genai

# Load .env
load_dotenv()

# Import model manager
sys.path.append('./model')
from model.model_manager import model_manager

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Cấu hình
class Config:
    DEFAULT_MODEL = 'qwen-4b'
    DEFAULT_K_DOCUMENTS = 3
    DEFAULT_RERANK = False
    CHAT_HISTORY_FILE = 'chat_history.json'

# Utility functions for chat history
def load_chat_history():
    """Load chat history from JSON file"""
    if os.path.exists(Config.CHAT_HISTORY_FILE):
        try:
            with open(Config.CHAT_HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_chat_history(history):
    """Save chat history to JSON file"""
    try:
        with open(Config.CHAT_HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving chat history: {e}")

def get_chat_preview(messages):
    """Get a preview of the chat for display in sidebar"""
    if not messages:
        return "Cuộc trò chuyện trống"
    
    # Find first user message
    for msg in messages:
        if msg.get('type') == 'user':
            content = msg.get('content', '')
            return content[:50] + ('...' if len(content) > 50 else '')
    
    return "Cuộc trò chuyện mới"

# Khởi tạo session chat
def init_session():
    if 'chat_id' not in session:
        session['chat_id'] = str(uuid.uuid4())
        session['messages'] = []
        session['selected_model'] = Config.DEFAULT_MODEL
        session['k_documents'] = Config.DEFAULT_K_DOCUMENTS
        session['rerank_enabled'] = Config.DEFAULT_RERANK
        session['chat_title'] = None

@app.route('/')
def index():
    init_session()
    return render_template('index.html', 
                         models=model_manager.get_available_models(), 
                         current_model=session.get('selected_model', Config.DEFAULT_MODEL),
                         rerank_enabled=session.get('rerank_enabled', Config.DEFAULT_RERANK))

@app.route('/api/chat', methods=['POST'])
def chat():
    init_session()
    
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        k_documents = data.get('k_documents', session['k_documents'])
        selected_model = data.get('model', session['selected_model'])
        rerank_enabled = data.get('rerank', session.get('rerank_enabled', Config.DEFAULT_RERANK))
        
        if not user_message:
            return jsonify({'error': 'Tin nhắn không được để trống'}), 400
        
        # Cập nhật session
        session['k_documents'] = k_documents
        session['selected_model'] = selected_model
        session['rerank_enabled'] = rerank_enabled
        
        # Tạo message ID
        message_id = str(uuid.uuid4())
        
        # Lưu tin nhắn user
        user_msg = {
            'id': message_id + '_user',
            'type': 'user',
            'content': user_message,
            'timestamp': datetime.now().isoformat(),
            'model': selected_model,
            'k_documents': k_documents,
            'rerank_enabled': rerank_enabled
        }
        session['messages'].append(user_msg)
        
        # Xử lý với model đã chọn
        start_time = time.time()
        
        # Load model nếu chưa được load
        try:
            model_function = model_manager.get_model_function(selected_model)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
        # Gọi function với các tham số phù hợp
        try:
            print(f"DEBUG: Calling model function for {selected_model}")
            
            # Chuẩn bị conversation history (chỉ lấy các tin nhắn trước đó, không bao gồm user message mới nhất)
            conversation_history = session['messages'][:-1] if len(session['messages']) > 0 else []
            
            if selected_model == 'qwen-4b':
                # Qwen 4B có thể cần ngrok_url parameter
                ngrok_url = os.getenv("NGROK_URL", "")
                result = model_function(
                    question=user_message, 
                    k=k_documents, 
                    rerank=rerank_enabled,
                    ngrok_url=ngrok_url,
                    conversation_history=conversation_history
                )
                print(f"DEBUG: Model function returned {len(result)} values: {type(result)}")
                answer, source_docs, rewrite_queries = result
            elif selected_model == 'gemini-api':
                # Gemini có parameter rewrite và conversation_history
                result = model_function(
                    question=user_message,
                    k=k_documents,
                    rerank=rerank_enabled,
                    rewrite=True,  # Có thể được config từ UI
                    conversation_history=conversation_history
                )
                print(f"DEBUG: Model function returned {len(result)} values: {type(result)}")
                answer, source_docs, rewrite_queries = result
            else:
                # Các model khác - thêm conversation_history nếu function hỗ trợ
                try:
                    result = model_function(
                        question=user_message, 
                        k=k_documents, 
                        rerank=rerank_enabled,
                        rewrite=True,
                        conversation_history=conversation_history
                    )
                except TypeError:
                    # Fallback nếu function không hỗ trợ conversation_history
                    print(f"DEBUG: {selected_model} không hỗ trợ conversation_history, sử dụng mode cũ")
                    result = model_function(
                        question=user_message, 
                        k=k_documents, 
                        rerank=rerank_enabled,
                        rewrite=True
                    )
                print(f"DEBUG: Model function returned {len(result)} values: {type(result)}")
                answer, source_docs, rewrite_queries = result
        except Exception as e:
            print(f"DEBUG: Exception in model function call: {str(e)}")
            import traceback
            traceback.print_exc()
            return jsonify({'error': f'Lỗi khi xử lý với model {selected_model}: {str(e)}'}), 500
        
        processing_time = round(time.time() - start_time, 2)
        
        # Lưu tin nhắn bot
        bot_msg = {
            'id': message_id + '_bot',
            'type': 'bot',
            'content': answer,
            'timestamp': datetime.now().isoformat(),
            'source_documents': source_docs,
            'rewrite_queries': rewrite_queries if 'rewrite_queries' in locals() else [],
            'model': selected_model,
            'k_documents': k_documents,
            'processing_time': processing_time,
            'used_context': len(conversation_history) > 0  # Thêm thông tin này
        }
        session['messages'].append(bot_msg)
        
        # Auto-save chat after each message
        save_current_chat()
        
        return jsonify({
            'success': True,
            'message': bot_msg,
            'user_message': user_msg
        })
        
    except Exception as e:
        return jsonify({'error': f'Đã xảy ra lỗi: {str(e)}'}), 500

@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    """API endpoint để xử lý ảnh và trích xuất text toán học"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'Không tìm thấy file ảnh'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'Không có file được chọn'}), 400
        
        # Kiểm tra định dạng file
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
        if not ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in allowed_extensions):
            return jsonify({'error': 'Định dạng file không được hỗ trợ'}), 400
        
        # Đọc ảnh
        image_data = file.read()
        image = Image.open(io.BytesIO(image_data))
        
        # Chuyển đổi thành RGB nếu cần
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Sử dụng Gemini Vision để đọc text từ ảnh
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return jsonify({'error': 'GEMINI_API_KEY không được cấu hình'}), 500
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash-exp")
        
        # Prompt để trích xuất đề bài toán
        prompt = """
        Hãy đọc và trích xuất CHÍNH XÁC toàn bộ nội dung văn bản từ hình ảnh này, đặc biệt chú ý đến:
        1. Các công thức toán học
        2. Số liệu, phân số, căn thức
        3. Ký hiệu toán học đặc biệt
        4. Cấu trúc câu hỏi
        
        Yêu cầu:
        - Viết lại đề bài một cách rõ ràng, đầy đủ
        - Với công thức phức tạp, hãy mô tả bằng ký hiệu toán học chuẩn
        - Không thêm giải thích hay phân tích, chỉ trích xuất nội dung gốc
        - Nếu có nhiều câu hỏi, hãy tách riêng từng câu
        
        Nội dung đề bài:
        """
        
        # Gửi ảnh và prompt tới Gemini
        response = model.generate_content([prompt, image])
        extracted_text = response.text.strip()
        
        return jsonify({
            'success': True,
            'extracted_text': extracted_text,
            'message': 'Đã trích xuất thành công nội dung từ ảnh'
        })
        
    except Exception as e:
        return jsonify({'error': f'Lỗi khi xử lý ảnh: {str(e)}'}), 500

@app.route('/api/clear', methods=['POST'])
def clear_chat():
    session['messages'] = []
    return jsonify({'success': True})

@app.route('/api/history')
def get_history():
    init_session()
    return jsonify({'messages': session.get('messages', [])})

@app.route('/api/models')
def get_models():
    return jsonify({
        'models': model_manager.get_available_models(),
        'current': session.get('selected_model', Config.DEFAULT_MODEL),
        'loaded_models': model_manager.get_loaded_models()
    })

@app.route('/api/models/<model_id>/load', methods=['POST'])
def load_model(model_id):
    """Load một model cụ thể"""
    try:
        success = model_manager.load_model(model_id)
        if success:
            return jsonify({
                'success': True, 
                'message': f'Model {model_id} đã được load thành công',
                'loaded_models': model_manager.get_loaded_models()
            })
        else:
            return jsonify({
                'success': False, 
                'message': f'Không thể load model {model_id}, sử dụng fallback',
                'loaded_models': model_manager.get_loaded_models()
            })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/models/<model_id>/unload', methods=['POST'])
def unload_model(model_id):
    """Unload một model để giải phóng bộ nhớ"""
    try:
        success = model_manager.unload_model(model_id)
        if success:
            return jsonify({
                'success': True, 
                'message': f'Model {model_id} đã được unload',
                'loaded_models': model_manager.get_loaded_models()
            })
        else:
            return jsonify({
                'success': False, 
                'message': f'Model {model_id} không được load hoặc không tồn tại'
            })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/models/unload-all', methods=['POST'])
def unload_all_models():
    """Unload tất cả models"""
    try:
        model_manager.unload_all_models()
        return jsonify({
            'success': True, 
            'message': 'Đã unload tất cả models',
            'loaded_models': []
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/system-info')
def get_system_info():
    """Lấy thông tin hệ thống"""
    try:
        import torch
        import psutil
        
        system_info = {
            'cuda_available': torch.cuda.is_available(),
            'cuda_device_count': torch.cuda.device_count() if torch.cuda.is_available() else 0,
            'memory_total': round(psutil.virtual_memory().total / (1024**3), 2),  # GB
            'memory_available': round(psutil.virtual_memory().available / (1024**3), 2),  # GB
            'memory_percent': psutil.virtual_memory().percent
        }
        
        if torch.cuda.is_available():
            try:
                system_info['cuda_memory_total'] = round(torch.cuda.get_device_properties(0).total_memory / (1024**3), 2)  # GB
                system_info['cuda_memory_allocated'] = round(torch.cuda.memory_allocated(0) / (1024**3), 2)  # GB
                system_info['cuda_memory_reserved'] = round(torch.cuda.memory_reserved(0) / (1024**3), 2)  # GB
            except:
                system_info['cuda_memory_error'] = True
        
        return jsonify({
            'success': True,
            'system_info': system_info
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/documents')
def get_documents():
    """Lấy danh sách tài liệu từ folder data/extracted"""
    try:
        documents_folder = './data/extracted'
        documents = []
        
        if os.path.exists(documents_folder):
            for filename in os.listdir(documents_folder):
                if filename.endswith('.md'):
                    # Tạo tên hiển thị đẹp hơn
                    display_name = filename.replace('.md', '').replace('_', ' ').title()
                    display_name = re.sub(r'File \d+', '', display_name).strip()
                    
                    documents.append({
                        'name': filename,
                        'display_name': display_name,
                        'path': f'data/extracted/{filename}'
                    })
        
        return jsonify({
            'success': True,
            'documents': sorted(documents, key=lambda x: x['display_name'])
        })
    
    except Exception as e:
        return jsonify({'error': f'Lỗi khi tải danh sách tài liệu: {str(e)}'}), 500

@app.route('/api/document/<filename>')
def get_document(filename):
    """Lấy nội dung của một tài liệu"""
    try:
        file_path = os.path.join('./data/extracted', filename)
        
        if not os.path.exists(file_path) or not filename.endswith('.md'):
            return jsonify({'error': 'Tài liệu không tồn tại'}), 404
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert markdown to HTML
        html_content = markdown.markdown(content, extensions=['tables', 'fenced_code'])
        
        # Tạo tiêu đề từ filename
        title = filename.replace('.md', '').replace('_', ' ').title()
        title = re.sub(r'File \d+', '', title).strip()
        
        return jsonify({
            'success': True,
            'title': title,
            'content': html_content,
            'filename': filename
        })
    
    except Exception as e:
        return jsonify({'error': f'Lỗi khi tải tài liệu: {str(e)}'}), 500

@app.route('/api/settings', methods=['POST'])
def update_settings():
    """Cập nhật cài đặt người dùng"""
    init_session()
    
    try:
        data = request.get_json()
        
        if 'rerank_enabled' in data:
            session['rerank_enabled'] = data['rerank_enabled']
        
        if 'k_documents' in data:
            session['k_documents'] = data['k_documents']
        
        if 'selected_model' in data:
            session['selected_model'] = data['selected_model']
        
        return jsonify({'success': True, 'message': 'Cài đặt đã được cập nhật'})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/rerank-status')
def rerank_status():
    """Kiểm tra trạng thái tính năng reranking"""
    try:
        # Kiểm tra import FlagEmbedding trực tiếp
        import FlagEmbedding
        available = True
        message = 'Reranking khả dụng'
    except ImportError:
        available = False
        message = 'FlagEmbedding chưa được cài đặt'
    except Exception as e:
        available = False
        message = f'Lỗi kiểm tra reranking: {str(e)}'
    
    return jsonify({
        'available': available,
        'message': message
    })

@app.route('/api/chats', methods=['GET'])
def get_chats():
    """Lấy danh sách tất cả các cuộc trò chuyện"""
    history = load_chat_history()
    chats = []
    
    for chat_id, chat_data in history.items():
        chats.append({
            'id': chat_id,
            'title': chat_data.get('title') or get_chat_preview(chat_data.get('messages', [])),
            'created_at': chat_data.get('created_at'),
            'updated_at': chat_data.get('updated_at'),
            'message_count': len(chat_data.get('messages', []))
        })
    
    # Sort by updated_at descending
    chats.sort(key=lambda x: x.get('updated_at', ''), reverse=True)
    
    return jsonify({'chats': chats})

@app.route('/api/chats/<chat_id>', methods=['GET'])
def get_chat(chat_id):
    """Lấy một cuộc trò chuyện cụ thể"""
    history = load_chat_history()
    
    if chat_id not in history:
        return jsonify({'error': 'Chat không tồn tại'}), 404
    
    chat_data = history[chat_id]
    return jsonify({
        'chat_id': chat_id,
        'title': chat_data.get('title'),
        'messages': chat_data.get('messages', []),
        'created_at': chat_data.get('created_at'),
        'updated_at': chat_data.get('updated_at')
    })

@app.route('/api/chats/new', methods=['POST'])
def new_chat():
    """Tạo cuộc trò chuyện mới"""
    # Save current chat if it has messages
    if 'chat_id' in session and session.get('messages'):
        save_current_chat()
    
    # Create new chat
    new_chat_id = str(uuid.uuid4())
    session['chat_id'] = new_chat_id
    session['messages'] = []
    session['chat_title'] = None
    
    return jsonify({
        'success': True,
        'chat_id': new_chat_id,
        'message': 'Đã tạo cuộc trò chuyện mới'
    })

@app.route('/api/chats/<chat_id>/load', methods=['POST'])
def load_chat(chat_id):
    """Tải một cuộc trò chuyện"""
    # Save current chat if it has messages
    if 'chat_id' in session and session.get('messages'):
        save_current_chat()
    
    # Load requested chat
    history = load_chat_history()
    
    if chat_id not in history:
        return jsonify({'error': 'Chat không tồn tại'}), 404
    
    chat_data = history[chat_id]
    
    # Update session
    session['chat_id'] = chat_id
    session['messages'] = chat_data.get('messages', [])
    session['chat_title'] = chat_data.get('title')
    
    return jsonify({
        'success': True,
        'chat_id': chat_id,
        'messages': session['messages'],
        'title': session['chat_title']
    })

@app.route('/api/chats/<chat_id>', methods=['DELETE'])
def delete_chat(chat_id):
    """Xóa một cuộc trò chuyện"""
    history = load_chat_history()
    
    if chat_id not in history:
        return jsonify({'error': 'Chat không tồn tại'}), 404
    
    del history[chat_id]
    save_chat_history(history)
    
    # If deleting current chat, create new one
    if session.get('chat_id') == chat_id:
        session['chat_id'] = str(uuid.uuid4())
        session['messages'] = []
        session['chat_title'] = None
    
    return jsonify({'success': True, 'message': 'Đã xóa cuộc trò chuyện'})

def save_current_chat():
    """Lưu cuộc trò chuyện hiện tại"""
    if not session.get('chat_id') or not session.get('messages'):
        return
    
    history = load_chat_history()
    chat_id = session['chat_id']
    
    # Generate title if not exists
    title = session.get('chat_title')
    if not title:
        title = get_chat_preview(session['messages'])
    
    now = datetime.now().isoformat()
    
    history[chat_id] = {
        'title': title,
        'messages': session['messages'],
        'created_at': history.get(chat_id, {}).get('created_at', now),
        'updated_at': now
    }
    
    save_chat_history(history)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)
