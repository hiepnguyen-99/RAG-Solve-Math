"""
Model manager để lazy loading các RAG models
Chỉ load model khi được yêu cầu
"""
import os
import sys
import torch
from typing import Dict, Optional, Callable

class ModelManager:
    def __init__(self):
        self._models = {}
        self._model_configs = {
            'qwen-4b': {
                'name': 'Qwen 4B',
                'module': 'model.rag_4b',
                'function': 'solve_question_4b',
                'loaded': False
            },
            'qwen-1.5b': {
                'name': 'Qwen 1.5B', 
                'module': 'model.rag_15b',
                'function': 'solve_question_15b',
                'loaded': False
            },
            'model-api': {
                'name': 'llama 7B (API)',
                'module': 'model.rag_7b_api', 
                'function': 'solve_question_api_groq',
                'loaded': False
            },
            'gemini-api': {
                'name': 'Gemini (API)',
                'module': 'model.rag_gemini_api',
                'function': 'solve_question_api_gemini',
                'loaded': False
            },
            'Rag-2b': {
                'name': 'Qwen-2b',
                'module': 'model.rag_2b',
                'function': 'solve_2b',
                'loaded': False
            }
        }
        
    def get_available_models(self) -> Dict:
        """Trả về danh sách các model có sẵn"""
        return {
            model_id: {
                'name': config['name'],
                'loaded': config['loaded']
            }
            for model_id, config in self._model_configs.items()
        }
    
    def load_model(self, model_id: str) -> bool:
        """Load một model cụ thể"""
        if model_id not in self._model_configs:
            raise ValueError(f"Model {model_id} không tồn tại")
            
        config = self._model_configs[model_id]
        
        if config['loaded']:
            return True
            
        try:
            module = __import__(config['module'], fromlist=[config['function']])
            function = getattr(module, config['function'])
            
            self._models[model_id] = function
            config['loaded'] = True
            
            return True
            
        except Exception as e:
            self._models[model_id] = self._create_fallback_function(model_id)
            config['loaded'] = True
            return False
    
    def _create_fallback_function(self, model_id: str) -> Callable:
        """Tạo fallback function khi model không load được"""
        def fallback_function(question, k=3, rerank=False, **kwargs):
            return f"Fallback response ({model_id}) for: {question}", []
        return fallback_function
    
    def get_model_function(self, model_id: str) -> Callable:
        """Lấy function của model, load nếu chưa có"""
        if model_id not in self._model_configs:
            raise ValueError(f"Model {model_id} không tồn tại")
            
        if not self._model_configs[model_id]['loaded']:
            self.load_model(model_id)
            
        return self._models[model_id]
    
    def unload_model(self, model_id: str) -> bool:
        """Unload một model để giải phóng bộ nhớ"""
        if model_id not in self._model_configs:
            return False
            
        if model_id in self._models:
            del self._models[model_id]
            self._model_configs[model_id]['loaded'] = False
            
            module_name = self._model_configs[model_id]['module']
            if module_name in sys.modules:
                del sys.modules[module_name]
                
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                
            return True
            
        return False
    
    def get_loaded_models(self) -> list:
        """Trả về danh sách các model đã được load"""
        return [
            model_id for model_id, config in self._model_configs.items() 
            if config['loaded']
        ]
    
    def unload_all_models(self):
        """Unload tất cả models"""
        for model_id in list(self._models.keys()):
            self.unload_model(model_id)

# Singleton instance
model_manager = ModelManager()
