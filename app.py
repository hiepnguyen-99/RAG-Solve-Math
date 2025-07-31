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

# Load .env
load_dotenv()
# Import các model RAG
sys.path.append('./model')
try:
    from rag_4b import solve_question_4b  
    from rag_15b import solve_question_15b
    from rag_api import solve_question_api
    models_available = True
except ImportError as e:
    print(f"Warning: Could not import RAG models: {e}")
    models_available = False
    # Fallback functions for testing
    def solve_question_4b(question, k=3, ngrok_url="", rerank=False):
        return f"Fallback response (4B) for: {question}", []
    def solve_question_15b(question, k=3, rerank=False):
        return f"Fallback response (1.5B) for: {question}", []
    def solve_question_api(question, k=3, rerank=False):
        return f"Fallback response (API) for: {question}", []

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Cấu hình
class Config:
    MODELS = {
        'qwen-4b': {'name': 'Qwen 4B', 'function': solve_question_4b},
        'qwen-1.5b': {'name': 'Qwen 1.5B', 'function': solve_question_15b},
        'model-api': {'name': 'Meta-llama 70B (API) ', 'function': solve_question_api}
    }
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
                         models=Config.MODELS, 
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
        model_config = Config.MODELS.get(selected_model)
        
        if not model_config:
            return jsonify({'error': 'Model không hợp lệ'}), 400
        
        # Gọi function tương ứng
        if selected_model == 'qwen-4b':
            answer, source_docs = model_config['function'](
                question=user_message, 
                k=k_documents, 
                rerank=rerank_enabled
            )
        elif selected_model == 'qwen-1.5b':
            answer, source_docs = model_config['function'](
                question=user_message, 
                k=k_documents, 
                rerank=rerank_enabled
            )
        else:
            answer, source_docs = model_config['function'](
                question=user_message, 
                k=k_documents, 
                rerank=rerank_enabled
            )
        
        processing_time = round(time.time() - start_time, 2)
        
        # Lưu tin nhắn bot
        bot_msg = {
            'id': message_id + '_bot',
            'type': 'bot',
            'content': answer,
            'timestamp': datetime.now().isoformat(),
            'source_documents': source_docs,
            'model': selected_model,
            'k_documents': k_documents,
            'processing_time': processing_time
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
        'models': Config.MODELS,
        'current': session.get('selected_model', Config.DEFAULT_MODEL)
    })

@app.route('/api/documents')
def get_documents():
    """Lấy danh sách tài liệu từ folder TEST"""
    try:
        test_folder = './TEST'
        documents = []
        
        if os.path.exists(test_folder):
            for filename in os.listdir(test_folder):
                if filename.endswith('.md'):
                    # Tạo tên hiển thị đẹp hơn
                    display_name = filename.replace('.md', '').replace('_', ' ').title()
                    display_name = re.sub(r'File \d+', '', display_name).strip()
                    
                    documents.append({
                        'name': filename,
                        'display_name': display_name,
                        'path': f'TEST/{filename}'
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
        file_path = os.path.join('./TEST', filename)
        
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
    app.run(debug=True, host='0.0.0.0', port=5000)
