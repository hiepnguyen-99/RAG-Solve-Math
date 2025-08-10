"""
Conversation Manager - Quản lý ngữ cảnh trò chuyện
Tạo context từ lịch sử chat để giúp AI hiểu ngữ cảnh
"""

from typing import List, Dict, Any
import json

class ConversationManager:
    def __init__(self, max_history_length=10, max_context_tokens=2000):
        """
        Args:
            max_history_length: Số lượng tin nhắn tối đa giữ lại
            max_context_tokens: Số tokens tối đa cho context (ước tính)
        """
        self.max_history_length = max_history_length
        self.max_context_tokens = max_context_tokens
    
    def build_conversation_context(self, messages: List[Dict], current_question: str) -> str:
        """
        Xây dựng ngữ cảnh trò chuyện từ lịch sử tin nhắn
        
        Args:
            messages: Danh sách tin nhắn từ session
            current_question: Câu hỏi hiện tại
            
        Returns:
            str: Context được format sẵn
        """
        if not messages:
            return ""
        
        # Lọc và giới hạn số lượng tin nhắn
        recent_messages = self._filter_recent_messages(messages)
        
        # Tạo context text
        context_parts = []
        
        # Thêm thông tin về cuộc trò chuyện
        context_parts.append("=== Ngữ cảnh cuộc trò chuyện trước đó ===")
        
        # Thêm các cặp Q&A gần đây
        for i in range(0, len(recent_messages) - 1, 2):
            if i + 1 < len(recent_messages):
                user_msg = recent_messages[i]
                bot_msg = recent_messages[i + 1]
                
                if user_msg.get('type') == 'user' and bot_msg.get('type') == 'bot':
                    # Rút gọn nội dung nếu quá dài
                    user_content = self._truncate_content(user_msg.get('content', ''), 200)
                    bot_content = self._truncate_content(bot_msg.get('content', ''), 300)
                    
                    context_parts.append(f"Câu hỏi trước: {user_content}")
                    context_parts.append(f"Trả lời trước: {bot_content}")
                    context_parts.append("---")
        
        # Thêm câu hỏi hiện tại
        context_parts.append(f"Câu hỏi hiện tại: {current_question}")
        context_parts.append("=== Kết thúc ngữ cảnh ===")
        
        context = "\n".join(context_parts)
        
        # Kiểm tra độ dài và cắt bớt nếu cần
        return self._ensure_context_length(context)
    
    def _filter_recent_messages(self, messages: List[Dict]) -> List[Dict]:
        """Lọc tin nhắn gần đây và quan trọng"""
        if not messages:
            return []
        
        # Lấy tin nhắn gần đây nhất
        recent = messages[-self.max_history_length:]
        
        # Đảm bảo bắt đầu từ tin nhắn của user
        if recent and recent[0].get('type') != 'user':
            recent = recent[1:]
        
        return recent
    
    def _truncate_content(self, content: str, max_length: int) -> str:
        """Rút gọn nội dung nếu quá dài"""
        if len(content) <= max_length:
            return content
        return content[:max_length] + "..."
    
    def _ensure_context_length(self, context: str) -> str:
        """Đảm bảo context không vượt quá giới hạn tokens"""
        # Ước tính 1 token ≈ 4 ký tự tiếng Việt
        estimated_tokens = len(context) // 4
        
        if estimated_tokens <= self.max_context_tokens:
            return context
        
        # Cắt bớt từ giữa nếu quá dài
        target_chars = self.max_context_tokens * 4
        if len(context) > target_chars:
            # Giữ phần đầu và phần cuối
            start_part = context[:target_chars//3]
            end_part = context[-target_chars//3:]
            return start_part + "\n...[Đã rút gọn]...\n" + end_part
        
        return context
    
    def extract_key_topics(self, messages: List[Dict]) -> List[str]:
        """
        Trích xuất các chủ đề chính từ cuộc trò chuyện
        Có thể dùng để cải thiện retrieval
        """
        topics = []
        
        for msg in messages:
            if msg.get('type') == 'user':
                content = msg.get('content', '').lower()
                
                # Tìm các từ khóa toán học phổ biến
                math_keywords = [
                    'ma trận', 'định thức', 'phương trình', 'hệ phương trình',
                    'đạo hàm', 'tích phân', 'giới hạn', 'hàm số',
                    'vector', 'không gian', 'hình học', 'đại số',
                    'xác suất', 'thống kê', 'logarit', 'mũ',
                    'tam giác', 'đường tròn', 'ellipse', 'parabol'
                ]
                
                for keyword in math_keywords:
                    if keyword in content and keyword not in topics:
                        topics.append(keyword)
        
        return topics[:5]  # Giới hạn 5 topic chính
    
    def should_use_context(self, current_question: str, messages: List[Dict]) -> bool:
        """
        Quyết định có nên sử dụng context hay không
        Dựa vào lịch sử có tồn tại hay không
        """
        if not messages:
            return False
        
        # Chỉ sử dụng context nếu có ít nhất 2 tin nhắn trước đó
        return len(messages) >= 2

# Singleton instance
conversation_manager = ConversationManager()
