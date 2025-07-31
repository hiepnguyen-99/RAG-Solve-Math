// ===== Application State =====
class ChatApp {
    constructor() {
        this.isLoading = false;
        this.currentTheme = localStorage.getItem('theme') || 'light';
        this.messages = [];
        this.init();
    }

    init() {
        this.initElements();
        this.initEventListeners();
        this.initTheme();
        this.autoResizeTextarea();
        this.loadChatHistoryFromSession();
        this.loadDocuments();
        this.checkRerankStatus();
        this.loadChatHistorySidebar();
    }

    initElements() {
        // Core elements
        this.chatMessages = document.getElementById('chat-messages');
        this.userInput = document.getElementById('user-input');
        this.sendButton = document.getElementById('send-button');
        this.loadingIndicator = document.getElementById('loading-indicator');
        
        // Controls
        this.modelSelect = document.getElementById('model-select');
        this.kSelect = document.getElementById('k-select');
        this.rerankToggle = document.getElementById('rerank-toggle');
        this.themeToggle = document.getElementById('theme-toggle');
        this.clearChat = document.getElementById('clear-chat');
        this.docsToggle = document.getElementById('docs-toggle');
        this.newChat = document.getElementById('new-chat');
        this.chatHistoryToggle = document.getElementById('chat-history-toggle');
        
        // Sidebar elements
        this.documentSidebar = document.getElementById('document-sidebar');
        this.sidebarClose = document.getElementById('sidebar-close');
        this.docSearch = document.getElementById('doc-search');
        this.mainContent = document.querySelector('.main-content');
        
        // Chat history elements
        this.chatHistorySidebar = document.getElementById('chat-history-sidebar');
        this.chatHistoryClose = document.getElementById('chat-history-close');
        this.chatSearch = document.getElementById('chat-search');
        this.chatList = document.getElementById('chat-list');
        
        // Modal elements
        this.documentModal = document.getElementById('document-modal');
        this.modalClose = document.getElementById('modal-close');
        this.modalTitle = document.getElementById('modal-title');
        this.modalBody = document.getElementById('modal-body');
        
        // Info elements
        this.charCounter = document.getElementById('char-counter');
        this.modelInfo = document.getElementById('model-info');
        this.toastContainer = document.getElementById('toast-container');
        this.rerankStatus = document.getElementById('rerank-status');
    }

    initEventListeners() {
        // Input events
        this.userInput.addEventListener('input', () => this.handleInputChange());
        this.userInput.addEventListener('keydown', (e) => this.handleKeyDown(e));
        this.sendButton.addEventListener('click', () => this.handleSendMessage());
        
        // Control events
        this.modelSelect.addEventListener('change', () => this.handleModelChange());
        this.kSelect.addEventListener('change', () => this.handleKChange());
        this.rerankToggle.addEventListener('change', () => this.handleRerankToggle());
        this.themeToggle.addEventListener('click', () => this.toggleTheme());
        this.clearChat.addEventListener('click', () => this.handleClearChat());
        this.newChat.addEventListener('click', () => this.handleNewChat());
        this.chatHistoryToggle.addEventListener('click', () => this.toggleChatHistory());
        
        // Sidebar events
        this.docsToggle.addEventListener('click', () => this.toggleSidebar());
        this.sidebarClose.addEventListener('click', () => this.closeSidebar());
        this.chatHistoryClose.addEventListener('click', () => this.closeChatHistory());
        this.docSearch.addEventListener('input', (e) => this.searchDocuments(e.target.value));
        this.chatSearch.addEventListener('input', (e) => this.filterChats(e.target.value));
        
        // Modal events
        this.modalClose.addEventListener('click', () => this.closeModal());
        this.documentModal.addEventListener('click', (e) => {
            if (e.target === this.documentModal) this.closeModal();
        });
        
        // Window events
        window.addEventListener('beforeunload', () => this.saveState());
        window.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                if (this.documentModal.classList.contains('show')) {
                    this.closeModal();
                } else if (this.documentSidebar.classList.contains('open')) {
                    this.closeSidebar();
                }
            }
        });
    }

    initTheme() {
        document.documentElement.setAttribute('data-theme', this.currentTheme);
        this.updateThemeIcon();
    }

    // ===== Input Handling =====
    handleInputChange() {
        const text = this.userInput.value;
        const length = text.length;
        
        // Update character counter
        this.charCounter.textContent = `${length}/2000`;
        
        // Update send button state
        this.sendButton.disabled = length === 0 || this.isLoading;
        
        // Auto-resize textarea
        this.autoResizeTextarea();
    }

    handleKeyDown(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            if (!this.sendButton.disabled) {
                this.handleSendMessage();
            }
        }
    }

    autoResizeTextarea() {
        this.userInput.style.height = 'auto';
        this.userInput.style.height = Math.min(this.userInput.scrollHeight, 120) + 'px';
    }

    // ===== LaTeX and Markdown Processing =====
    processLaTeX(content, container = null) {
        // Render LaTeX math expressions
        if (window.MathJax) {
            setTimeout(() => {
                const targetElement = container || this.chatMessages;
                MathJax.typesetPromise([targetElement]).catch((err) => {
                    console.log('MathJax error:', err);
                });
            }, 100);
        }
        return content;
    }

    // ===== Sidebar Management =====
    toggleSidebar() {
        this.documentSidebar.classList.toggle('open');
        this.mainContent.classList.toggle('sidebar-open');
        
        // Add visual feedback
        this.docsToggle.style.transform = 'scale(0.9)';
        setTimeout(() => {
            this.docsToggle.style.transform = '';
        }, 150);
    }

    closeSidebar() {
        this.documentSidebar.classList.remove('open');
        this.mainContent.classList.remove('sidebar-open');
    }

    // ===== Document Management =====
    async loadDocuments() {
        try {
            const response = await fetch('/api/documents');
            const data = await response.json();
            
            if (data.success) {
                this.populateDocumentList(data.documents);
            }
        } catch (error) {
            console.error('Error loading documents:', error);
        }
    }

    populateDocumentList(documents) {
        const basicDocs = document.getElementById('basic-docs');
        const operationDocs = document.getElementById('operation-docs');
        const advancedDocs = document.getElementById('advanced-docs');

        // Clear existing content
        basicDocs.innerHTML = '';
        operationDocs.innerHTML = '';
        advancedDocs.innerHTML = '';

        // Categorize documents
        documents.forEach(doc => {
            const docElement = this.createDocumentElement(doc);
            
            if (doc.name.includes('basics') || doc.name.includes('types') || doc.name.includes('transpose')) {
                basicDocs.appendChild(docElement);
            } else if (doc.name.includes('operations') || doc.name.includes('determinant') || doc.name.includes('inverse')) {
                operationDocs.appendChild(docElement);
            } else {
                advancedDocs.appendChild(docElement);
            }
        });
    }

    createDocumentElement(doc) {
        const element = document.createElement('a');
        element.className = 'doc-item';
        element.href = '#';
        element.innerHTML = `
            <span class="material-icons">description</span>
            ${doc.display_name}
        `;
        
        element.addEventListener('click', (e) => {
            e.preventDefault();
            this.openDocument(doc.name);
        });
        
        return element;
    }

    async openDocument(filename) {
        try {
            const response = await fetch(`/api/document/${filename}`);
            const data = await response.json();
            
            if (data.success) {
                this.modalTitle.textContent = data.title;
                this.modalBody.innerHTML = data.content;
                this.documentModal.classList.add('show');
                
                // Process LaTeX in modal
                this.processLaTeX(data.content, this.modalBody);
            } else {
                this.showToast('Không thể tải tài liệu', 'error');
            }
        } catch (error) {
            console.error('Error opening document:', error);
            this.showToast('Đã xảy ra lỗi khi tải tài liệu', 'error');
        }
    }

    closeModal() {
        this.documentModal.classList.remove('show');
    }

    searchDocuments(query) {
        const docItems = document.querySelectorAll('.doc-item');
        const lowerQuery = query.toLowerCase();
        
        docItems.forEach(item => {
            const text = item.textContent.toLowerCase();
            if (text.includes(lowerQuery)) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }

    // ===== Message Handling ===== (Updated)
    async handleSendMessage() {
        const message = this.userInput.value.trim();
        if (!message || this.isLoading) return;

        const selectedModel = this.modelSelect.value;
        const kDocuments = parseInt(this.kSelect.value);
        const rerankEnabled = this.rerankToggle.checked;

        // Clear input and disable controls
        this.userInput.value = '';
        this.handleInputChange();
        this.setLoading(true);

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    model: selectedModel,
                    k_documents: kDocuments,
                    rerank: rerankEnabled
                })
            });

            const data = await response.json();

            if (data.success) {
                // Add user message
                this.addMessage(data.user_message);
                // Add bot response
                this.addMessage(data.message);
            } else {
                this.showToast(data.error || 'Đã xảy ra lỗi', 'error');
            }
        } catch (error) {
            console.error('Error sending message:', error);
            this.showToast('Không thể kết nối đến server', 'error');
        } finally {
            this.setLoading(false);
        }
    }

    addMessage(message, autoScroll = true) {
        const messageElement = document.createElement('div');
        messageElement.className = `message message-${message.type}`;
        messageElement.innerHTML = this.createMessageHTML(message);
        
        // Remove welcome message if it exists
        const welcomeMessage = this.chatMessages.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }
        
        this.chatMessages.appendChild(messageElement);
        
        // Add source documents toggle functionality for bot messages
        if (message.type === 'bot' && message.source_documents) {
            this.initSourceToggle(messageElement);
        }
        
        // Process LaTeX for math expressions
        this.processLaTeX(message.content);
        
        this.messages.push(message);
        
        // Auto-scroll only if requested
        if (autoScroll) {
            this.scrollToBottom();
        }
    }

    createMessageHTML(message) {
        const timestamp = new Date(message.timestamp).toLocaleTimeString('vi-VN', {
            hour: '2-digit',
            minute: '2-digit'
        });

        if (message.type === 'user') {
            return `
                <div class="message-content">
                    ${this.escapeHtml(message.content)}
                </div>
                <div class="message-meta">
                    <span class="material-icons">schedule</span>
                    <span>${timestamp}</span>
                </div>
            `;
        } else {
            const sourceDocsHTML = message.source_documents && message.source_documents.length > 0
                ? this.createSourceDocumentsHTML(message.source_documents)
                : '';

            return `
                <div class="message-content">
                    ${this.escapeHtml(message.content)}
                    ${sourceDocsHTML}
                </div>
                <div class="message-meta">
                    <span class="material-icons">smart_toy</span>
                    <span>${timestamp}</span>
                    <span>•</span>
                    <span>${this.getModelDisplayName(message.model)}</span>
                    <span>•</span>
                    <span>${message.k_documents} tài liệu</span>
                    ${message.processing_time ? `<span>•</span><span>${message.processing_time}s</span>` : ''}
                </div>
            `;
        }
    }

    createSourceDocumentsHTML(sourceDocs) {
        if (!sourceDocs || sourceDocs.length === 0) return '';

        const docsHTML = sourceDocs.map((doc, index) => {
            // Trích xuất tên file từ metadata nếu có
            const fileName = doc.metadata && doc.metadata.source ? 
                doc.metadata.source.split('/').pop() : 
                `document_${index + 1}.md`;
            
            // Tạo display name đẹp
            const displayName = fileName.replace('.md', '').replace(/_/g, ' ').replace(/file \d+/gi, '').trim();
            const capitalizedName = displayName.charAt(0).toUpperCase() + displayName.slice(1);
            
            return `
                <div class="source-item">
                    <div class="source-header-item">
                        <strong>Tài liệu ${index + 1}:</strong>
                        <button class="document-link" data-filename="${fileName}" title="Xem tài liệu đầy đủ">
                            <span class="material-icons">description</span>
                            <span>${capitalizedName}</span>
                        </button>
                    </div>
                    <div class="source-content">
                        ${this.escapeHtml(doc.page_content.substring(0, 200))}${doc.page_content.length > 200 ? '...' : ''}
                    </div>
                </div>
            `;
        }).join('');

        return `
            <div class="source-documents collapsed">
                <div class="source-header">
                    <span class="material-icons">expand_more</span>
                    <span>Tài liệu tham khảo (${sourceDocs.length})</span>
                </div>
                <div class="source-list">
                    ${docsHTML}
                </div>
            </div>
        `;
    }

    initSourceToggle(messageElement) {
        const sourceHeader = messageElement.querySelector('.source-header');
        const sourceContainer = messageElement.querySelector('.source-documents');
        
        if (sourceHeader && sourceContainer) {
            sourceHeader.addEventListener('click', () => {
                sourceContainer.classList.toggle('collapsed');
            });
        }
        
        // Add click handlers for document links
        const documentLinks = messageElement.querySelectorAll('.document-link');
        documentLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const filename = link.getAttribute('data-filename');
                this.openDocument(filename);
            });
        });
    }

    // ===== Control Handlers =====
    handleModelChange() {
        const selectedModel = this.modelSelect.value;
        this.modelInfo.textContent = this.getModelDisplayName(selectedModel);
    }

    handleKChange() {
        // Just update the UI, no immediate action needed
    }

    handleRerankToggle() {
        const isEnabled = this.rerankToggle.checked;
        const statusText = isEnabled ? 'bật' : 'tắt';
        this.showToast(`Đã ${statusText} reranking`, 'info');
    }

    async handleClearChat() {
        if (this.messages.length === 0) return;

        if (confirm('Bạn có chắc chắn muốn xóa toàn bộ cuộc trò chuyện?')) {
            try {
                const response = await fetch('/api/clear', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                });

                if (response.ok) {
                    this.messages = [];
                    this.chatMessages.innerHTML = this.createWelcomeMessage();
                    this.showToast('Đã xóa cuộc trò chuyện', 'success');
                } else {
                    this.showToast('Không thể xóa cuộc trò chuyện', 'error');
                }
            } catch (error) {
                console.error('Error clearing chat:', error);
                this.showToast('Đã xảy ra lỗi khi xóa cuộc trò chuyện', 'error');
            }
        }
    }

    // ===== Theme Management =====
    toggleTheme() {
        this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', this.currentTheme);
        localStorage.setItem('theme', this.currentTheme);
        this.updateThemeIcon();
        
        // Add visual feedback
        this.themeToggle.style.transform = 'scale(0.9)';
        setTimeout(() => {
            this.themeToggle.style.transform = '';
        }, 150);
    }

    updateThemeIcon() {
        const icon = this.themeToggle.querySelector('.material-icons');
        icon.textContent = this.currentTheme === 'light' ? 'light_mode' : 'dark_mode';
        this.themeToggle.title = this.currentTheme === 'light' ? 'Chuyển sang chế độ tối' : 'Chuyển sang chế độ sáng';
    }

    // ===== Chat History Functions =====
    async handleNewChat() {
        if (confirm('Bạn có muốn tạo cuộc trò chuyện mới? Cuộc trò chuyện hiện tại sẽ được lưu.')) {
            try {
                const response = await fetch('/api/chats/new', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' }
                });
                
                const data = await response.json();
                
                if (data.success) {
                    this.messages = [];
                    this.chatMessages.innerHTML = this.createWelcomeMessage();
                    this.showToast('Đã tạo cuộc trò chuyện mới', 'success');
                    this.loadChatHistorySidebar();
                } else {
                    this.showToast('Không thể tạo cuộc trò chuyện mới', 'error');
                }
            } catch (error) {
                console.error('Error creating new chat:', error);
                this.showToast('Đã xảy ra lỗi', 'error');
            }
        }
    }

    toggleChatHistory() {
        this.chatHistorySidebar.classList.toggle('open');
        if (this.chatHistorySidebar.classList.contains('open')) {
            this.loadChatHistorySidebar();
        }
    }

    closeChatHistory() {
        this.chatHistorySidebar.classList.remove('open');
    }

    async loadChatHistorySidebar() {
        try {
            const response = await fetch('/api/chats');
            const data = await response.json();
            
            this.renderChatHistory(data.chats);
        } catch (error) {
            console.error('Error loading chat history:', error);
            this.chatList.innerHTML = '<div class="empty-chats"><span class="material-icons">error</span><span>Không thể tải lịch sử</span></div>';
        }
    }

    renderChatHistory(chats) {
        if (chats.length === 0) {
            this.chatList.innerHTML = `
                <div class="empty-chats">
                    <span class="material-icons">chat_bubble_outline</span>
                    <span>Chưa có cuộc trò chuyện nào</span>
                </div>
            `;
            return;
        }

        this.chatList.innerHTML = chats.map(chat => `
            <div class="chat-item" data-chat-id="${chat.id}">
                <div class="chat-title">${this.escapeHtml(chat.title)}</div>
                <div class="chat-meta">
                    <span>${chat.message_count} tin nhắn</span>
                    <span>${this.formatDate(chat.updated_at)}</span>
                </div>
                <div class="chat-actions">
                    <button class="chat-delete" data-chat-id="${chat.id}" title="Xóa cuộc trò chuyện">
                        <span class="material-icons">delete</span>
                    </button>
                </div>
            </div>
        `).join('');

        // Add event listeners
        this.chatList.querySelectorAll('.chat-item').forEach(item => {
            item.addEventListener('click', (e) => {
                if (!e.target.closest('.chat-delete')) {
                    this.loadChatConversation(item.dataset.chatId);
                }
            });
        });

        this.chatList.querySelectorAll('.chat-delete').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.deleteChatConversation(btn.dataset.chatId);
            });
        });
    }

    async loadChatConversation(chatId) {
        try {
            const response = await fetch(`/api/chats/${chatId}/load`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' }
            });
            
            const data = await response.json();
            
            if (data.success) {
                this.messages = data.messages;
                this.renderMessages();
                this.closeChatHistory();
                this.showToast('Đã tải cuộc trò chuyện', 'success');
            } else {
                this.showToast(data.error || 'Không thể tải cuộc trò chuyện', 'error');
            }
        } catch (error) {
            console.error('Error loading chat:', error);
            this.showToast('Đã xảy ra lỗi', 'error');
        }
    }

    async deleteChatConversation(chatId) {
        if (confirm('Bạn có chắc chắn muốn xóa cuộc trò chuyện này?')) {
            try {
                const response = await fetch(`/api/chats/${chatId}`, {
                    method: 'DELETE'
                });
                
                const data = await response.json();
                
                if (data.success) {
                    this.showToast('Đã xóa cuộc trò chuyện', 'success');
                    this.loadChatHistorySidebar();
                } else {
                    this.showToast(data.error || 'Không thể xóa cuộc trò chuyện', 'error');
                }
            } catch (error) {
                console.error('Error deleting chat:', error);
                this.showToast('Đã xảy ra lỗi', 'error');
            }
        }
    }

    filterChats(query) {
        const chatItems = this.chatList.querySelectorAll('.chat-item');
        chatItems.forEach(item => {
            const title = item.querySelector('.chat-title').textContent.toLowerCase();
            const visible = title.includes(query.toLowerCase());
            item.style.display = visible ? 'block' : 'none';
        });
    }

    renderMessages() {
        this.chatMessages.innerHTML = '';
        if (this.messages.length === 0) {
            this.chatMessages.innerHTML = this.createWelcomeMessage();
        } else {
            this.messages.forEach(message => {
                this.addMessage(message, false); // false = don't auto-scroll
            });
            this.scrollToBottom();
        }
    }

    formatDate(dateString) {
        if (!dateString) return '';
        const date = new Date(dateString);
        const now = new Date();
        const diffTime = Math.abs(now - date);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        
        if (diffDays === 1) return 'Hôm qua';
        if (diffDays < 7) return `${diffDays} ngày trước`;
        return date.toLocaleDateString('vi-VN');
    }

    // ===== Utility Functions =====
    setLoading(loading) {
        this.isLoading = loading;
        this.sendButton.disabled = loading || this.userInput.value.trim().length === 0;
        
        if (loading) {
            this.loadingIndicator.classList.add('show');
            this.scrollToBottom();
        } else {
            this.loadingIndicator.classList.remove('show');
        }
    }

    scrollToBottom() {
        setTimeout(() => {
            this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
        }, 100);
    }

    showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        
        const icon = type === 'error' ? 'error' : type === 'success' ? 'check_circle' : 'info';
        
        toast.innerHTML = `
            <span class="material-icons">${icon}</span>
            <span>${this.escapeHtml(message)}</span>
        `;
        
        this.toastContainer.appendChild(toast);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            if (toast.parentNode) {
                toast.style.animation = 'slideInRight 0.3s ease-out reverse';
                setTimeout(() => {
                    if (toast.parentNode) {
                        toast.remove();
                    }
                }, 300);
            }
        }, 3000);
    }

    async checkRerankStatus() {
        try {
            const response = await fetch('/api/rerank-status');
            const data = await response.json();
            
            if (this.rerankStatus) {
                this.rerankStatus.textContent = data.message;
                this.rerankStatus.className = `rerank-status ${data.available ? 'available' : 'unavailable'}`;
                
                if (!data.available && this.rerankToggle) {
                    this.rerankToggle.disabled = true;
                    this.rerankToggle.checked = false;
                }
            }
        } catch (error) {
            console.error('Error checking rerank status:', error);
            if (this.rerankStatus) {
                this.rerankStatus.textContent = 'Không thể kiểm tra';
                this.rerankStatus.className = 'rerank-status unavailable';
            }
        }
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML.replace(/\\n/g, '<br>');
    }

    getModelDisplayName(modelKey) {
        const models = {
            'qwen-1.5b': 'Qwen 1.5B',
            'qwen-4b': 'Qwen 4B',
            'model-api': 'Meta-llama 70B (API)'
        };
        return models[modelKey] || modelKey;
    }

    createWelcomeMessage() {
        return `
            <div class="welcome-message">
                <div class="welcome-icon">
                    <span class="material-icons">psychology</span>
                </div>
                <h2>Chào mừng đến với Trợ lý Toán học!</h2>
                <p>Tôi có thể giúp bạn giải quyết các bài toán 1 cách nhanh chóng và chính xác. Hãy đặt câu hỏi về toán học!</p>
                <div class="feature-highlights">
                    <div class="feature">
                        <span class="material-icons">auto_awesome</span>
                        <span>AI thông minh</span>
                    </div>
                    <div class="feature">
                        <span class="material-icons">library_books</span>
                        <span>Tài liệu phong phú</span>
                    </div>
                    <div class="feature">
                        <span class="material-icons">speed</span>
                        <span>Trả lời nhanh</span>
                    </div>
                </div>
            </div>
        `;
    }

    // ===== Data Persistence =====
    async loadChatHistoryFromSession() {
        try {
            const response = await fetch('/api/history');
            const data = await response.json();
            
            if (data.messages && data.messages.length > 0) {
                // Remove welcome message
                const welcomeMessage = this.chatMessages.querySelector('.welcome-message');
                if (welcomeMessage) {
                    welcomeMessage.remove();
                }
                
                // Add all messages
                data.messages.forEach(message => {
                    this.addMessage(message);
                });
                
                this.scrollToBottom();
            }
        } catch (error) {
            console.error('Error loading chat history:', error);
        }
    }

    saveState() {
        // Save current selections to localStorage
        localStorage.setItem('selectedModel', this.modelSelect.value);
        localStorage.setItem('selectedK', this.kSelect.value);
    }

    // ===== Initialization =====
    loadSavedState() {
        // Restore saved selections
        const savedModel = localStorage.getItem('selectedModel');
        const savedK = localStorage.getItem('selectedK');
        
        if (savedModel) {
            this.modelSelect.value = savedModel;
            this.handleModelChange();
        }
        
        if (savedK) {
            this.kSelect.value = savedK;
        }
    }
}

// ===== Application Initialization =====
document.addEventListener('DOMContentLoaded', () => {
    const app = new ChatApp();
    
    // Load saved state
    app.loadSavedState();
    
    // Focus on input
    app.userInput.focus();
    
    // Add some visual polish
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});

// ===== Service Worker Registration (Optional) =====
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/static/js/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}
