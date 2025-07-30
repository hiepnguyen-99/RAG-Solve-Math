from flask import Flask, render_template, request, jsonify, session
import uuid
import time
from datetime import datetime
import os
import sys
import markdown
import re

# Import các model RAG
sys.path.append('./model')
try:
    from rag_4b import solve_question_4b  
    from rag_15b import solve_question_15b
    models_available = True
except ImportError as e:
    print(f"Warning: Could not import RAG models: {e}")
    models_available = False
    # Fallback functions for testing
    def solve_question_4b(question, k=3):
        return f"Fallback response (4B) for: {question}", []
    def solve_question_15b(question, k=3):
        return f"Fallback response (15B) for: {question}", []

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Cấu hình
class Config:
    MODELS = {
        'qwen-4b': {'name': 'Qwen 4B (Ngrok)', 'function': solve_question_4b},
        'qwen-15b': {'name': 'Qwen 15B (Local)', 'function': solve_question_15b}
    }
    DEFAULT_MODEL = 'qwen-4b'
    DEFAULT_K_DOCUMENTS = 3

# Khởi tạo session chat
def init_session():
    if 'chat_id' not in session:
        session['chat_id'] = str(uuid.uuid4())
        session['messages'] = []
        session['selected_model'] = Config.DEFAULT_MODEL
        session['k_documents'] = Config.DEFAULT_K_DOCUMENTS

@app.route('/')
def index():
    init_session()
    return render_template('index.html', 
                         models=Config.MODELS, 
                         current_model=session.get('selected_model', Config.DEFAULT_MODEL))

@app.route('/api/chat', methods=['POST'])
def chat():
    init_session()
    
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        k_documents = data.get('k_documents', session['k_documents'])
        selected_model = data.get('model', session['selected_model'])
        
        if not user_message:
            return jsonify({'error': 'Tin nhắn không được để trống'}), 400
        
        # Cập nhật session
        session['k_documents'] = k_documents
        session['selected_model'] = selected_model
        
        # Tạo message ID
        message_id = str(uuid.uuid4())
        
        # Lưu tin nhắn user
        user_msg = {
            'id': message_id + '_user',
            'type': 'user',
            'content': user_message,
            'timestamp': datetime.now().isoformat(),
            'model': selected_model,
            'k_documents': k_documents
        }
        session['messages'].append(user_msg)
        
        # Xử lý với model đã chọn
        start_time = time.time()
        model_config = Config.MODELS.get(selected_model)
        
        if not model_config:
            return jsonify({'error': 'Model không hợp lệ'}), 400
        
        # Gọi function tương ứng
        if selected_model == 'qwen-4b':
            answer, source_docs = model_config['function'](user_message, k_documents)
        else:
            answer, source_docs = model_config['function'](user_message, k_documents)
        
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
