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
        this.initializeModelStatus();
    }

    initElements() {
        // Core elements
        this.chatMessages = document.getElementById('chat-messages');
        this.userInput = document.getElementById('user-input');
        this.sendButton = document.getElementById('send-button');
        this.loadingIndicator = document.getElementById('loading-indicator');
        
        // Image upload elements
        this.imageInput = document.getElementById('image-input');
        this.imageButton = document.getElementById('image-button');
        
        // New input buttons
        this.docsToggle = document.getElementById('docs-toggle');
        
        // Controls
        this.modelSelect = document.getElementById('model-select');
        this.kSelect = document.getElementById('k-select');
        this.kValue = document.getElementById('k-value');
        this.rerankToggle = document.getElementById('rerank-toggle');
        this.themeToggle = document.getElementById('theme-toggle');
        this.clearChat = document.getElementById('clear-chat');
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
        this.userInput.addEventListener('paste', (e) => this.handlePaste(e));
        this.userInput.addEventListener('focus', () => this.handleInputFocus());
        this.userInput.addEventListener('blur', () => this.handleInputBlur());
        this.sendButton.addEventListener('click', () => this.handleSendMessage());
        
        // Image upload events
        this.imageButton.addEventListener('click', () => this.imageInput.click());
        this.imageInput.addEventListener('change', (e) => this.handleImageUpload(e));
        
        // New input button events
        if (this.docsToggle) {
            this.docsToggle.addEventListener('click', () => this.showDocumentsModal());
        }
        
        // Control events
        this.modelSelect.addEventListener('change', () => this.handleModelChange());
        this.kSelect.addEventListener('input', () => this.handleKChange());
        this.kSelect.addEventListener('change', () => this.handleKChange());
        this.rerankToggle.addEventListener('change', () => this.handleRerankToggle());
        
        // Initialize slider progress on load with wave effect
        setTimeout(() => {
            this.updateSliderProgress();
            this.kSelect.style.animation = 'waveRipple 1s ease-out';
        }, 500);
        
        // Dropdown list animation events
        this.modelSelect.addEventListener('mousedown', (e) => this.handleDropdownOpen(e));
        this.modelSelect.addEventListener('blur', (e) => this.handleDropdownClose(e));
        
        // Note: These will be handled through dropdown menu now
        // this.themeToggle.addEventListener('click', () => this.toggleTheme());
        // this.chatHistoryToggle.addEventListener('click', () => this.toggleChatHistory());
        
        // Add dropdown functionality
        const addDropdownBtn = document.getElementById('add-dropdown-btn');
        const addDropdownMenu = document.getElementById('add-dropdown-menu');
        const newChatBtn = document.getElementById('new-chat');
        
        if (addDropdownBtn && addDropdownMenu) {
            addDropdownBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.toggleAddDropdown();
            });
            
            // Close dropdown when clicking outside
            document.addEventListener('click', (e) => {
                if (!addDropdownBtn.contains(e.target) && !addDropdownMenu.contains(e.target)) {
                    this.closeAddDropdown();
                }
            });
        }
        
        if (newChatBtn) {
            newChatBtn.addEventListener('click', () => {
                this.handleNewChat();
                this.closeAddDropdown();
            });
        }
        
        // Menu dropdown functionality
        const menuDropdownBtn = document.getElementById('menu-dropdown-btn');
        const menuDropdownMenu = document.getElementById('menu-dropdown-menu');
        
        if (menuDropdownBtn && menuDropdownMenu) {
            menuDropdownBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.toggleMenuDropdown();
            });
            
            // Close dropdown when clicking outside
            document.addEventListener('click', (e) => {
                if (!menuDropdownBtn.contains(e.target) && !menuDropdownMenu.contains(e.target)) {
                    this.closeMenuDropdown();
                }
            });
            
            // Add event listeners for menu items
            const chatHistoryItem = menuDropdownMenu.querySelector('#chat-history-toggle');
            const themeToggleItem = menuDropdownMenu.querySelector('#theme-toggle');
            const settingsItem = menuDropdownMenu.querySelector('#model-management-toggle');
            
            if (chatHistoryItem) {
                chatHistoryItem.addEventListener('click', () => {
                    this.toggleChatHistory();
                    this.closeMenuDropdown();
                });
            }
            
            if (themeToggleItem) {
                themeToggleItem.addEventListener('click', () => {
                    this.toggleTheme();
                    this.closeMenuDropdown();
                });
            }
            
            if (settingsItem) {
                settingsItem.addEventListener('click', () => {
                    this.toggleModelManagement();
                    this.closeMenuDropdown();
                });
            }
        }
        
        // Additional buttons
        if (this.imageButton) {
            this.imageButton.addEventListener('click', () => this.imageInput.click());
        }
        
        // Deep research button
        const deepResearchBtn = document.getElementById('deep-research');
        if (deepResearchBtn) {
            deepResearchBtn.addEventListener('click', () => this.handleDeepResearch());
        }
        
        // Model management sidebar controls
        const modelManagementClose = document.getElementById('model-management-close');
        const unloadAllBtn = document.getElementById('unload-all-models');
        const refreshStatusBtn = document.getElementById('refresh-model-status');
        if (modelManagementClose) {
            modelManagementClose.addEventListener('click', () => this.closeModelManagement());
        }
        if (unloadAllBtn) {
            unloadAllBtn.addEventListener('click', () => this.unloadAllModels());
        }
        if (refreshStatusBtn) {
            refreshStatusBtn.addEventListener('click', () => this.refreshModelStatus());
        }
        
        // Sidebar events
        if (this.sidebarClose) {
            this.sidebarClose.addEventListener('click', () => this.closeSidebar());
        }
        if (this.chatHistoryClose) {
            this.chatHistoryClose.addEventListener('click', () => this.closeChatHistory());
        }
        if (this.docSearch) {
            this.docSearch.addEventListener('input', (e) => this.searchDocuments(e.target.value));
        }
        if (this.chatSearch) {
            this.chatSearch.addEventListener('input', (e) => this.filterChats(e.target.value));
        }
        
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

    async openDocumentChunk(content, filename) {
        try {
            const response = await fetch('/api/document-chunk', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    content: content,
                    filename: filename
                })
            });
            
            const data = await response.json();
            
            if (data.success) {
                this.modalTitle.textContent = data.title;
                
                // Add source info and navigation option
                const sourceInfo = `
                    <div class="chunk-info">
                        <div class="chunk-header">
                            <span class="material-icons">content_cut</span>
                            <span>Đoạn văn được tìm thấy từ chunking</span>
                        </div>
                        <div class="chunk-actions">
                            <button class="view-full-doc" data-filename="${this.escapeHtml(filename)}">
                                <span class="material-icons">library_books</span>
                                <span>Xem tài liệu đầy đủ</span>
                            </button>
                        </div>
                    </div>
                    <hr style="margin: 15px 0; border: 1px solid var(--border-color);">
                `;
                
                this.modalBody.innerHTML = sourceInfo + data.content;
                this.documentModal.classList.add('show');
                
                // Add event listener for "view full document" button
                const viewFullDocBtn = this.modalBody.querySelector('.view-full-doc');
                if (viewFullDocBtn) {
                    viewFullDocBtn.addEventListener('click', (e) => {
                        e.preventDefault();
                        const targetFilename = e.currentTarget.getAttribute('data-filename');
                        this.openDocument(targetFilename);
                    });
                }
                
                // Process LaTeX in modal
                this.processLaTeX(data.content, this.modalBody);
            } else {
                this.showToast('Không thể tải chi tiết chunk', 'error');
            }
        } catch (error) {
            console.error('Error opening chunk:', error);
            this.showToast('Đã xảy ra lỗi khi tải chi tiết chunk', 'error');
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

        // Tạo user message ngay lập tức để hiển thị
        const userMessage = {
            id: Date.now() + '_user',
            type: 'user',
            content: message,
            timestamp: new Date().toISOString(),
            model: selectedModel,
            k_documents: kDocuments,
            rerank_enabled: rerankEnabled
        };

        // Hiển thị user message ngay lập tức
        this.addMessage(userMessage);

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
                // Chỉ add bot response (user message đã được add rồi)
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
        
        // Add toggle functionality for bot messages (source docs and rewrite queries)
        if (message.type === 'bot' && (message.source_documents || message.rewrite_queries)) {
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
            
            const rewriteQueriesHTML = message.rewrite_queries && message.rewrite_queries.length > 0
                ? this.createRewriteQueriesHTML(message.rewrite_queries)
                : '';

            // Context indicator
            const contextIndicator = message.used_context ? 
                `<div class="context-indicator">
                    <span class="material-icons">memory</span>
                    <span>Sử dụng ngữ cảnh trò chuyện</span>
                </div>` : '';

            return `
                <div class="message-content">
                    ${this.escapeHtml(message.content)}
                    ${contextIndicator}
                    ${rewriteQueriesHTML}
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
                    ${message.used_context ? `<span>•</span><span class="context-badge">Context</span>` : ''}
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
                        <button class="document-link" 
                                data-filename="${fileName}" 
                                data-content="${this.escapeHtml(doc.page_content)}"
                                title="Xem chi tiết đoạn văn được tìm thấy">
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

    createRewriteQueriesHTML(rewriteQueries) {
        if (!rewriteQueries || rewriteQueries.length === 0) return '';

        const queriesHTML = rewriteQueries.map((query, index) => `
            <div class="rewrite-query-item">
                <span class="query-number">${index + 1}.</span>
                <span class="query-text">${this.escapeHtml(query)}</span>
            </div>
        `).join('');

        return `
            <div class="rewrite-queries collapsed">
                <div class="rewrite-header">
                    <span class="material-icons">expand_more</span>
                    <span>Câu hỏi được mở rộng (${rewriteQueries.length})</span>
                </div>
                <div class="rewrite-list">
                    ${queriesHTML}
                </div>
            </div>
        `;
    }

    initSourceToggle(messageElement) {
        // Handle source documents toggle
        const sourceHeader = messageElement.querySelector('.source-header');
        const sourceContainer = messageElement.querySelector('.source-documents');
        
        if (sourceHeader && sourceContainer) {
            sourceHeader.addEventListener('click', () => {
                sourceContainer.classList.toggle('collapsed');
            });
        }
        
        // Handle rewrite queries toggle
        const rewriteHeader = messageElement.querySelector('.rewrite-header');
        const rewriteContainer = messageElement.querySelector('.rewrite-queries');
        
        if (rewriteHeader && rewriteContainer) {
            rewriteHeader.addEventListener('click', () => {
                rewriteContainer.classList.toggle('collapsed');
            });
        }
        
        // Add click handlers for document links - now shows chunk detail
        const documentLinks = messageElement.querySelectorAll('.document-link');
        documentLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const filename = link.getAttribute('data-filename');
                const content = link.getAttribute('data-content');
                
                // Show chunk detail instead of full document
                if (content) {
                    this.openDocumentChunk(content, filename);
                } else {
                    // Fallback to full document if no chunk content
                    this.openDocument(filename);
                }
            });
        });
    }

    // ===== Control Handlers =====
    async handleModelChange() {
        const selectedModel = this.modelSelect.value;
        this.modelInfo.textContent = this.getModelDisplayName(selectedModel);
        
        this.showModelLoadingState(selectedModel);
        
        try {
            const response = await fetch(`/api/models/${selectedModel}/load`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            const result = await response.json();
            
            if (result.success) {
                this.showToast(`Model ${this.getModelDisplayName(selectedModel)} đã sẵn sàng`, 'success');
                this.updateModelStatus(selectedModel, 'loaded');
            } else {
                this.showToast(`Cảnh báo: ${result.message}`, 'warning');
                this.updateModelStatus(selectedModel, 'fallback');
            }
            
            this.updateLoadedModelsList(result.loaded_models || []);
            
        } catch (error) {
            this.showToast('Lỗi khi load model', 'error');
            this.updateModelStatus(selectedModel, 'error');
        }
    }
    
    showModelLoadingState(modelId) {
        const option = this.modelSelect.querySelector(`option[value="${modelId}"]`);
        if (option) {
            option.textContent = `🔄 ${this.getModelDisplayName(modelId)} (Đang load...)`;
        }
        
        this.modelSelect.disabled = true;
    }
    
    updateModelStatus(modelId, status) {
        const option = this.modelSelect.querySelector(`option[value="${modelId}"]`);
        if (option) {
            const baseName = this.getModelDisplayName(modelId);
            switch (status) {
                case 'loaded':
                    option.textContent = `✅ ${baseName}`;
                    break;
                case 'fallback':
                    option.textContent = `⚠️ ${baseName} (Fallback)`;
                    break;
                case 'error':
                    option.textContent = `❌ ${baseName} (Lỗi)`;
                    break;
                default:
                    option.textContent = baseName;
            }
        }
        
        // Re-enable model select
        this.modelSelect.disabled = false;
    }
    
    updateLoadedModelsList(loadedModels) {
        const loadedInfo = document.getElementById('loaded-models-info');
        if (loadedInfo) {
            if (loadedModels.length > 0) {
                loadedInfo.textContent = `Models đã load: ${loadedModels.length}`;
                loadedInfo.style.display = 'block';
            } else {
                loadedInfo.style.display = 'none';
            }
        }
    }

    handleKChange() {
        // Update slider value display
        if (this.kValue) {
            this.kValue.textContent = this.kSelect.value;
        }
        
        // Update progress bar width based on value
        this.updateSliderProgress();
        
        // Add visual feedback with wave effect
        this.kValue.style.transform = 'scale(1.1)';
        this.kSelect.style.animation = 'waveRipple 0.8s ease-out';
        
        setTimeout(() => {
            this.kValue.style.transform = 'scale(1)';
            this.kSelect.style.animation = '';
        }, 800);
    }

    updateSliderProgress() {
        if (!this.kSelect) return;
        
        const value = parseInt(this.kSelect.value);
        const min = parseInt(this.kSelect.min);
        const max = parseInt(this.kSelect.max);
        const percentage = ((value - min) / (max - min)) * 100;
        
        // Update the ::before pseudo-element width through CSS custom property
        this.kSelect.style.setProperty('--slider-progress', `${percentage}%`);
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
        this.showChatHistoryModal();
    }

    async showChatHistoryModal() {
        try {
            const response = await fetch('/api/chats');
            const data = await response.json();
            
            this.modalTitle.textContent = 'Lịch sử trò chuyện';
            this.modalBody.innerHTML = this.createChatHistoryHTML(data.chats || []);
            this.documentModal.classList.add('show');
            
            // Add event listeners for chat items
            this.initChatHistoryLinks();
        } catch (error) {
            console.error('Error loading chat history:', error);
            this.showToast('Lỗi khi tải lịch sử chat', 'error');
        }
    }

    createChatHistoryHTML(chats) {
        if (!chats || chats.length === 0) {
            return `
                <div class="no-chats">
                    <div class="empty-state">
                        <span class="material-icons">chat_bubble_outline</span>
                        <h3>Chưa có cuộc trò chuyện nào</h3>
                        <p>Hãy bắt đầu cuộc trò chuyện đầu tiên của bạn!</p>
                    </div>
                </div>
            `;
        }

        // Group chats by date
        const groupedChats = this.groupChatsByDate(chats);
        
        let html = '<div class="chat-history-modal-list">';
        
        Object.entries(groupedChats).forEach(([dateGroup, chatList]) => {
            html += `
                <div class="chat-date-group">
                    <h4 class="date-title">${dateGroup}</h4>
                    <div class="chat-items">
            `;
            
            chatList.forEach(chat => {
                const title = chat.title || 'Cuộc trò chuyện không có tiêu đề';
                const truncatedTitle = title.length > 50 ? title.substring(0, 50) + '...' : title;
                const timeStr = this.formatChatTime(chat.updated_at);
                const messageCount = chat.message_count || 0;
                
                html += `
                    <div class="chat-item" data-chat-id="${chat.id}">
                        <div class="chat-icon">
                            <span class="material-icons">chat</span>
                        </div>
                        <div class="chat-info">
                            <div class="chat-title">${this.escapeHtml(truncatedTitle)}</div>
                            <div class="chat-time">${messageCount} tin nhắn • ${timeStr}</div>
                        </div>
                        <div class="chat-actions">
                            <button class="chat-action-btn" data-action="load" data-chat-id="${chat.id}" title="Tải cuộc trò chuyện">
                                <span class="material-icons">restore</span>
                            </button>
                            <button class="chat-action-btn delete-btn" data-action="delete" data-chat-id="${chat.id}" title="Xóa cuộc trò chuyện">
                                <span class="material-icons">delete</span>
                            </button>
                        </div>
                    </div>
                `;
            });
            
            html += `
                    </div>
                </div>
            `;
        });
        
        html += '</div>';
        return html;
    }

    groupChatsByDate(chats) {
        const now = new Date();
        const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
        const yesterday = new Date(today.getTime() - 24 * 60 * 60 * 1000);
        const weekAgo = new Date(today.getTime() - 7 * 24 * 60 * 60 * 1000);

        const groups = {
            'Hôm nay': [],
            'Hôm qua': [],
            '7 ngày trước đó': [],
            'Cũ hơn': []
        };

        chats.forEach(chat => {
            const chatDate = new Date(chat.updated_at);
            const chatDay = new Date(chatDate.getFullYear(), chatDate.getMonth(), chatDate.getDate());

            if (chatDay.getTime() === today.getTime()) {
                groups['Hôm nay'].push(chat);
            } else if (chatDay.getTime() === yesterday.getTime()) {
                groups['Hôm qua'].push(chat);
            } else if (chatDay >= weekAgo) {
                groups['7 ngày trước đó'].push(chat);
            } else {
                groups['Cũ hơn'].push(chat);
            }
        });

        // Remove empty groups
        Object.keys(groups).forEach(key => {
            if (groups[key].length === 0) {
                delete groups[key];
            }
        });

        return groups;
    }

    formatChatTime(updated_at) {
        const date = new Date(updated_at);
        const now = new Date();
        const diffMs = now - date;
        const diffHours = Math.floor(diffMs / (1000 * 60 * 60));
        const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));

        if (diffHours < 1) {
            const diffMinutes = Math.floor(diffMs / (1000 * 60));
            return `${diffMinutes} phút trước`;
        } else if (diffHours < 24) {
            return `${diffHours} giờ trước`;
        } else if (diffDays < 7) {
            return `${diffDays} ngày trước`;
        } else {
            return date.toLocaleDateString('vi-VN');
        }
    }

    initChatHistoryLinks() {
        const chatActionBtns = this.modalBody.querySelectorAll('.chat-action-btn');
        chatActionBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const action = btn.dataset.action;
                const chatId = btn.dataset.chatId;
                
                if (action === 'load') {
                    this.loadChatConversation(chatId);
                    this.documentModal.classList.remove('show'); // Đóng modal sau khi load
                } else if (action === 'delete') {
                    this.deleteChatConversation(chatId);
                }
            });
        });
    }

    closeChatHistory() {
        this.chatHistorySidebar.classList.remove('open');
    }

    // ===== Model Management Methods =====
    toggleModelManagement() {
        // Khôi phục chức năng ban đầu - toggle sidebar
        const sidebar = document.getElementById('model-management-sidebar');
        if (sidebar) {
            const isOpen = sidebar.classList.contains('open');
            if (isOpen) {
                this.closeModelManagement();
            } else {
                sidebar.classList.add('open');
                this.loadModelStatus(); // Load status khi mở sidebar
            }
        }
    }

    // Method riêng để show modal (có thể dùng sau này)
    async showModelManagementModal() {
        this.modalTitle.textContent = 'Quản lý Models';
        this.modalBody.innerHTML = this.createModelManagementHTML();
        this.documentModal.classList.add('show');
        
        // Load model status and system info
        await this.loadModelStatusInModal();
        this.loadSystemInfoInModal();
        this.initModelManagementActions();
    }

    async loadSystemInfoInModal() {
        try {
            const response = await fetch('/api/system-info');
            const data = await response.json();
            
            const cudaStatus = document.getElementById('modal-cuda-status');
            const memoryStatus = document.getElementById('modal-memory-status');
            
            if (data.success && data.system_info) {
                const info = data.system_info;
                
                if (cudaStatus) {
                    const cudaText = info.cuda_available ? 
                        `Có (${info.cuda_device_count || 0} GPU)` : 'Không có';
                    cudaStatus.textContent = cudaText;
                    cudaStatus.className = `info-value ${info.cuda_available ? 'status-success' : 'status-error'}`;
                }
                
                if (memoryStatus) {
                    const memoryText = info.memory_info || 'N/A';
                    memoryStatus.textContent = memoryText;
                    memoryStatus.className = 'info-value status-info';
                }
            } else {
                if (cudaStatus) {
                    cudaStatus.textContent = 'Lỗi khi tải';
                    cudaStatus.className = 'info-value status-error';
                }
                if (memoryStatus) {
                    memoryStatus.textContent = 'Lỗi khi tải';
                    memoryStatus.className = 'info-value status-error';
                }
            }
        } catch (error) {
            console.error('Error loading system info for modal:', error);
            const cudaStatus = document.getElementById('modal-cuda-status');
            const memoryStatus = document.getElementById('modal-memory-status');
            
            if (cudaStatus) {
                cudaStatus.textContent = 'Lỗi kết nối';
                cudaStatus.className = 'info-value status-error';
            }
            if (memoryStatus) {
                memoryStatus.textContent = 'Lỗi kết nối';
                memoryStatus.className = 'info-value status-error';
            }
        }
    }

    createModelManagementHTML() {
        return `
            <div class="model-management-content">
                <div class="model-section">
                    <div class="section-header">
                        <h4 class="section-title">
                            <span class="material-icons">memory</span>
                            Trạng thái Models
                        </h4>
                    </div>
                    <div class="model-status-list" id="modal-model-status-list">
                        <div class="loading-message">
                            <span class="material-icons">hourglass_empty</span>
                            Đang tải trạng thái...
                        </div>
                    </div>
                </div>
                
                <div class="model-section">
                    <div class="section-header">
                        <h4 class="section-title">
                            <span class="material-icons">build</span>
                            Hành động
                        </h4>
                    </div>
                    <div class="action-buttons">
                        <button class="action-btn primary" id="modal-unload-all-models">
                            <span class="material-icons">clear_all</span>
                            <span>Unload All Models</span>
                        </button>
                        <button class="action-btn secondary" id="modal-refresh-model-status">
                            <span class="material-icons">refresh</span>
                            <span>Refresh Status</span>
                        </button>
                    </div>
                </div>
                
                <div class="model-section">
                    <div class="section-header">
                        <h4 class="section-title">
                            <span class="material-icons">info</span>
                            Thông tin hệ thống
                        </h4>
                    </div>
                    <div class="system-info-grid" id="modal-system-info">
                        <div class="info-card">
                            <div class="info-label">CUDA</div>
                            <div class="info-value" id="modal-cuda-status">Đang kiểm tra...</div>
                        </div>
                        <div class="info-card">
                            <div class="info-label">Memory</div>
                            <div class="info-value" id="modal-memory-status">Đang kiểm tra...</div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    async loadModelStatusInModal() {
        try {
            const response = await fetch('/api/models');
            const data = await response.json();
            
            const statusContainer = document.getElementById('modal-model-status-list');
            const cudaStatus = document.getElementById('modal-cuda-status');
            const memoryStatus = document.getElementById('modal-memory-status');
            
            if (statusContainer) {
                let statusHTML = '';
                
                if (data.models && Object.keys(data.models).length > 0) {
                    Object.entries(data.models).forEach(([modelId, modelInfo]) => {
                        const status = modelInfo.loaded ? 'loaded' : 'unloaded';
                        const statusClass = modelInfo.loaded ? 'status-loaded' : 'status-unloaded';
                        const statusText = modelInfo.loaded ? 'Đã tải' : 'Chưa tải';
                        
                        statusHTML += `
                            <div class="model-status-card">
                                <div class="model-info">
                                    <div class="model-name">${modelInfo.name}</div>
                                    <div class="status-badge ${statusClass}">${statusText}</div>
                                </div>
                                <div class="model-actions">
                                    ${modelInfo.loaded ? 
                                        `<button class="model-action-btn unload-btn" data-model-id="${modelId}" title="Unload model">
                                            <span class="material-icons">stop</span>
                                        </button>` : 
                                        `<span class="model-action-placeholder">—</span>`
                                    }
                                </div>
                            </div>
                        `;
                    });
                } else {
                    statusHTML = '<div class="no-models">Không có models nào được tìm thấy</div>';
                }
                
                statusContainer.innerHTML = statusHTML;
            }
            
            // Update system info
            if (cudaStatus) {
                cudaStatus.textContent = data.cuda_available ? 'Có sẵn' : 'Không có';
                cudaStatus.className = `info-value ${data.cuda_available ? 'status-success' : 'status-error'}`;
            }
            
            if (memoryStatus) {
                memoryStatus.textContent = data.memory_info || 'N/A';
            }
            
        } catch (error) {
            console.error('Error loading model status:', error);
            const statusContainer = document.getElementById('modal-model-status-list');
            if (statusContainer) {
                statusContainer.innerHTML = '<div class="error-message">Lỗi khi tải trạng thái</div>';
            }
        }
    }

    initModelManagementActions() {
        const unloadAllBtn = document.getElementById('modal-unload-all-models');
        const refreshBtn = document.getElementById('modal-refresh-model-status');
        
        if (unloadAllBtn) {
            unloadAllBtn.addEventListener('click', () => this.unloadAllModels());
        }
        
        if (refreshBtn) {
            refreshBtn.addEventListener('click', () => this.loadModelStatusInModal());
        }
        
        // Add event listeners for individual model unload buttons
        const unloadBtns = document.querySelectorAll('.unload-btn');
        unloadBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const modelId = btn.dataset.modelId;
                this.unloadSingleModel(modelId);
            });
        });
    }

    async unloadSingleModel(modelId) {
        if (!confirm(`Bạn có chắc chắn muốn unload model ${modelId}?`)) {
            return;
        }

        try {
            const response = await fetch(`/api/models/${modelId}/unload`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            const result = await response.json();
            
            if (result.success) {
                this.showToast(`Đã unload model ${modelId}`, 'success');
                
                // Refresh modal if it's open
                if (this.documentModal.classList.contains('show') && this.modalTitle.textContent === 'Quản lý Models') {
                    this.loadModelStatusInModal();
                } else {
                    this.loadModelStatus();
                }
                
                // Update model status in select
                this.updateModelStatus(modelId, 'unloaded');
            } else {
                this.showToast(result.message || 'Không thể unload model', 'error');
            }
        } catch (error) {
            console.error('Error unloading model:', error);
            this.showToast('Lỗi khi unload model', 'error');
        }
    }

    closeModelManagement() {
        const sidebar = document.getElementById('model-management-sidebar');
        sidebar.classList.remove('open');
    }

    async loadModelStatus() {
        try {
            const response = await fetch('/api/models');
            const data = await response.json();
            
            this.renderModelStatus(data.models, data.loaded_models || []);
            await this.loadSystemInfo(); // Load system info khi mở model management
        } catch (error) {
            console.error('Error loading model status:', error);
            this.showToast('Không thể tải trạng thái models', 'error');
        }
    }

    renderModelStatus(models, loadedModels) {
        const statusList = document.getElementById('model-status-list');
        if (!statusList) return;

        statusList.innerHTML = '';

        Object.entries(models).forEach(([modelId, modelInfo]) => {
            const isLoaded = loadedModels.includes(modelId);
            
            const modelItem = document.createElement('div');
            modelItem.className = `model-item ${isLoaded ? 'loaded' : 'unloaded'}`;
            
            modelItem.innerHTML = `
                <div class="model-info">
                    <div class="model-name">
                        <span class="status-indicator ${isLoaded ? 'loaded' : 'unloaded'}"></span>
                        ${modelInfo.name}
                    </div>
                    <div class="model-status">
                        ${isLoaded ? 'Đã load' : 'Chưa load'}
                    </div>
                </div>
                <div class="model-actions">
                    ${!isLoaded ? `
                        <button class="model-action-btn load" onclick="app.loadModel('${modelId}')" title="Load model">
                            <span class="material-icons">download</span>
                        </button>
                    ` : `
                        <button class="model-action-btn unload" onclick="app.unloadModel('${modelId}')" title="Unload model">
                            <span class="material-icons">delete</span>
                        </button>
                    `}
                </div>
            `;
            
            statusList.appendChild(modelItem);
        });
    }

    async loadModel(modelId) {
        try {
            const response = await fetch(`/api/models/${modelId}/load`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            const result = await response.json();
            
            if (result.success) {
                this.showToast(result.message, 'success');
                this.loadModelStatus(); // Refresh status
                this.updateLoadedModelsList(result.loaded_models || []);
            } else {
                this.showToast(result.message, 'warning');
            }
        } catch (error) {
            console.error('Error loading model:', error);
            this.showToast('Lỗi khi load model', 'error');
        }
    }

    async unloadModel(modelId) {
        if (!confirm(`Bạn có chắc chắn muốn unload model này?${modelId === this.modelSelect.value ? ' (Đây là model hiện tại)' : ''}`)) {
            return;
        }

        try {
            const response = await fetch(`/api/models/${modelId}/unload`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            const result = await response.json();
            
            if (result.success) {
                this.showToast(result.message, 'success');
                this.loadModelStatus(); // Refresh status
                this.updateLoadedModelsList(result.loaded_models || []);
                
                // Reset model select display if this was the current model
                if (modelId === this.modelSelect.value) {
                    this.updateModelStatus(modelId, 'unloaded');
                }
            } else {
                this.showToast(result.message, 'warning');
            }
        } catch (error) {
            console.error('Error unloading model:', error);
            this.showToast('Lỗi khi unload model', 'error');
        }
    }

    async unloadAllModels() {
        if (!confirm('Bạn có chắc chắn muốn unload tất cả models? Điều này sẽ giải phóng bộ nhớ nhưng các model sẽ cần được load lại khi sử dụng.')) {
            return;
        }

        try {
            const response = await fetch('/api/models/unload-all', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            const result = await response.json();
            
            if (result.success) {
                this.showToast(result.message, 'success');
                
                // Refresh modal if it's open
                if (this.documentModal.classList.contains('show') && this.modalTitle.textContent === 'Quản lý Models') {
                    this.loadModelStatusInModal();
                } else {
                    this.loadModelStatus(); // Refresh status for sidebar
                }
                
                this.updateLoadedModelsList([]);
                
                // Reset all model select options
                this.modelSelect.querySelectorAll('option').forEach(option => {
                    const modelId = option.value;
                    this.updateModelStatus(modelId, 'unloaded');
                });
            } else {
                this.showToast(result.message, 'error');
            }
        } catch (error) {
            console.error('Error unloading all models:', error);
            this.showToast('Lỗi khi unload models', 'error');
        }
    }

    async refreshModelStatus() {
        await this.loadModelStatus();
        this.showToast('Đã refresh trạng thái models', 'info');
    }

    async initializeModelStatus() {
        try {
            const response = await fetch('/api/models');
            const data = await response.json();
            
            this.updateLoadedModelsList(data.loaded_models || []);
            
            // Update model select options to show initial status
            Object.keys(data.models).forEach(modelId => {
                const isLoaded = (data.loaded_models || []).includes(modelId);
                this.updateModelStatus(modelId, isLoaded ? 'loaded' : 'unloaded');
            });
        } catch (error) {
            console.error('Error initializing model status:', error);
        }
    }

    async loadSystemInfo() {
        try {
            const response = await fetch('/api/system-info');
            const data = await response.json();
            
            if (data.success) {
                this.renderSystemInfo(data.system_info);
            }
        } catch (error) {
            console.error('Error loading system info:', error);
        }
    }

    renderSystemInfo(info) {
        const cudaStatus = document.getElementById('cuda-status');
        const memoryStatus = document.getElementById('memory-status');
        
        if (cudaStatus) {
            const cudaText = info.cuda_available ? 
                `Có (${info.cuda_device_count} GPU)` : 'Không có';
            cudaStatus.textContent = cudaText;
            cudaStatus.style.color = info.cuda_available ? 'var(--secondary-color)' : 'var(--text-secondary)';
        }
        
        if (memoryStatus) {
            const memoryText = `${info.memory_available}GB / ${info.memory_total}GB (${100-info.memory_percent}% free)`;
            memoryStatus.textContent = memoryText;
            
            // Add CUDA memory info if available
            if (info.cuda_available && !info.cuda_memory_error) {
                memoryStatus.title = `CUDA Memory: ${info.cuda_memory_allocated}GB / ${info.cuda_memory_total}GB used`;
            }
        }
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
                    // Refresh modal if it's open
                    if (this.documentModal.classList.contains('show') && this.modalTitle.textContent === 'Lịch sử trò chuyện') {
                        this.showChatHistoryModal();
                    } else {
                        this.loadChatHistorySidebar();
                    }
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
            'model-api': 'llama 7B (API)',
            'gemini-api': 'Gemini (API)',
            'Rag-2B': 'Qwen-2B',
        };
        return models[modelKey] || modelKey;
    }

    createWelcomeMessage() {
        return `
            <div class="welcome-message">
                <div class="welcome-icon">
                    <span class="material-icons">psychology</span>
                </div>
                <h2>Chào mừng đến với Gia sư Toán học!</h2>
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
            this.handleKChange(); // Update slider display and progress
        } else {
            // Initialize progress for default value
            this.updateSliderProgress();
        }
    }

    // ===== Input Focus Handlers =====
    handleInputFocus() {
        this.checkClipboardForImages();
    }

    handleInputBlur() {
        this.hidePasteIndicator();
    }

    async checkClipboardForImages() {
        try {
            // Kiểm tra xem có quyền truy cập clipboard không
            if (navigator.clipboard && navigator.clipboard.read) {
                const items = await navigator.clipboard.read();
                let hasImage = false;
                
                for (const item of items) {
                    if (item.types.some(type => type.startsWith('image/'))) {
                        hasImage = true;
                        break;
                    }
                }
                
                if (hasImage) {
                    this.showPasteIndicator();
                }
            }
        } catch (error) {
            // Không thể truy cập clipboard, bỏ qua
            console.log('Cannot access clipboard:', error);
        }
    }

    showPasteIndicator() {
        // Kiểm tra xem indicator đã tồn tại chưa
        if (document.getElementById('pasteIndicator')) return;
        
        const indicator = document.createElement('div');
        indicator.id = 'pasteIndicator';
        indicator.className = 'paste-indicator';
        indicator.innerHTML = '📋 Ctrl+V để dán ảnh từ clipboard';
        
        const inputWrapper = this.userInput.closest('.input-wrapper');
        inputWrapper.appendChild(indicator);
        inputWrapper.classList.add('paste-ready');
        
        // Auto hide after 3 seconds
        setTimeout(() => {
            this.hidePasteIndicator();
        }, 3000);
    }

    hidePasteIndicator() {
        const indicator = document.getElementById('pasteIndicator');
        const inputWrapper = this.userInput.closest('.input-wrapper');
        
        if (indicator) {
            indicator.remove();
        }
        
        if (inputWrapper) {
            inputWrapper.classList.remove('paste-ready');
        }
    }

    // ===== Paste Handler =====
    async handlePaste(event) {
        const items = event.clipboardData?.items;
        if (!items) return;

        // Tìm file ảnh trong clipboard
        for (let i = 0; i < items.length; i++) {
            const item = items[i];
            
            // Kiểm tra nếu là file ảnh
            if (item.type.startsWith('image/')) {
                event.preventDefault(); // Ngăn paste text mặc định
                
                // Ẩn paste indicator
                this.hidePasteIndicator();
                
                const file = item.getAsFile();
                if (file) {
                    // Hiển thị thông báo paste detected
                    this.showToast('📋 Đã phát hiện ảnh từ clipboard, đang xử lý...', 'info');
                    
                    // Xử lý file như upload bình thường
                    await this.processImageFile(file);
                }
                break;
            }
        }
    }

    // ===== Image Upload Handlers =====
    async handleImageUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        await this.processImageFile(file);
        
        // Reset input để có thể upload cùng file lần nữa
        this.imageInput.value = '';
    }

    async processImageFile(file) {
        // Kiểm tra kích thước file (max 10MB)
        if (file.size > 10 * 1024 * 1024) {
            this.showToast('File ảnh quá lớn. Vui lòng chọn file nhỏ hơn 10MB.', 'error');
            return;
        }
        
        // Hiển thị loading
        this.showImageProcessing();
        
        try {
            const formData = new FormData();
            formData.append('image', file);
            
            const response = await fetch('/api/upload-image', {
                method: 'POST',
                body: formData
            });
            
            const result = await response.json();
            
            if (result.success) {
                // Điền text đã trích xuất vào input
                this.userInput.value = result.extracted_text;
                this.handleInputChange();
                this.userInput.focus();
                
                // Hiển thị preview ảnh
                this.showImagePreview(file, result.extracted_text);
                
                this.showToast('Đã trích xuất nội dung từ ảnh thành công!', 'success');
            } else {
                throw new Error(result.error || 'Không thể xử lý ảnh');
            }
        } catch (error) {
            console.error('Error uploading image:', error);
            this.showToast(`Lỗi khi xử lý ảnh: ${error.message}`, 'error');
        } finally {
            this.hideImageProcessing();
        }
    }

    showImageProcessing() {
        const processingHtml = `
            <div id="imageProcessing" class="image-processing">
                <div class="spinner-border-sm" role="status"></div>
                <span>Đang xử lý ảnh và trích xuất nội dung...</span>
            </div>
        `;
        this.chatMessages.insertAdjacentHTML('beforeend', processingHtml);
        this.scrollToBottom();
    }

    hideImageProcessing() {
        const processing = document.getElementById('imageProcessing');
        if (processing) {
            processing.remove();
        }
    }

    showImagePreview(file, extractedText) {
        const reader = new FileReader();
        reader.onload = (e) => {
            const previewHtml = `
                <div class="message message-user" id="imagePreview">
                    <div class="message-content">
                        <div class="image-upload-preview">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                                <strong>📷 Ảnh đã tải lên:</strong>
                                <button type="button" style="background: #dc3545; color: white; border: none; border-radius: 4px; padding: 4px 8px; cursor: pointer;" onclick="window.app.removeImagePreview()">
                                    ✕ Xóa
                                </button>
                            </div>
                            <img src="${e.target.result}" alt="Uploaded image">
                            <div class="extracted-text">
                                <small style="color: var(--text-muted);">Nội dung đã trích xuất:</small>
                                <div style="margin-top: 8px;">${this.escapeHtml(extractedText).replace(/\n/g, '<br>')}</div>
                            </div>
                        </div>
                    </div>
                    <div class="message-meta">
                        <span class="material-icons">schedule</span>
                        <span>${new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' })}</span>
                    </div>
                </div>
            `;
            this.chatMessages.insertAdjacentHTML('beforeend', previewHtml);
            this.scrollToBottom();
        };
        reader.readAsDataURL(file);
    }

    removeImagePreview() {
        const preview = document.getElementById('imagePreview');
        if (preview) {
            preview.remove();
        }
        this.userInput.value = '';
        this.handleInputChange();
        this.userInput.focus();
    }

    // ===== Function Button Handlers =====
    handleDeepResearch() {
        // Chế độ nghiên cứu sâu - có thể thêm logic đặc biệt sau
        this.userInput.focus();
        this.userInput.placeholder = "Nhập câu hỏi cần nghiên cứu sâu...";
        this.addMessage('system', '🔍 Chế độ nghiên cứu sâu đã được kích hoạt. Tôi sẽ tìm kiếm và phân tích chi tiết cho câu hỏi của bạn.');
    }

    // ===== Dropdown Handlers =====
    toggleAddDropdown() {
        const dropdown = document.getElementById('add-dropdown-menu');
        if (dropdown) {
            dropdown.classList.toggle('show');
        }
    }

    closeAddDropdown() {
        const dropdown = document.getElementById('add-dropdown-menu');
        if (dropdown) {
            dropdown.classList.remove('show');
        }
    }

    toggleMenuDropdown() {
        const dropdown = document.getElementById('menu-dropdown-menu');
        if (dropdown) {
            dropdown.classList.toggle('show');
        }
    }

    closeMenuDropdown() {
        const dropdown = document.getElementById('menu-dropdown-menu');
        if (dropdown) {
            dropdown.classList.remove('show');
        }
    }

    // ===== Documents Modal =====
    async showDocumentsModal() {
        try {
            const response = await fetch('/api/documents');
            const data = await response.json();
            
            if (data.success) {
                this.modalTitle.textContent = 'Thư viện tài liệu';
                this.modalBody.innerHTML = this.createDocumentsListHTML(data.documents);
                this.documentModal.classList.add('show');
                
                // Add event listeners for document links
                this.initDocumentLinks();
            } else {
                this.showToast('Không thể tải danh sách tài liệu', 'error');
            }
        } catch (error) {
            console.error('Error loading documents:', error);
            this.showToast('Lỗi khi tải tài liệu', 'error');
        }
    }

    createDocumentsListHTML(documents) {
        if (!documents || documents.length === 0) {
            return '<p class="no-documents">Không có tài liệu nào.</p>';
        }

        // Group documents by category
        const categories = {
            'Cơ bản': [],
            'Phép toán': [],
            'Nâng cao': []
        };

        documents.forEach(doc => {
            if (doc.name.includes('basics') || doc.name.includes('types') || doc.name.includes('transpose')) {
                categories['Cơ bản'].push(doc);
            } else if (doc.name.includes('operations') || doc.name.includes('determinant') || doc.name.includes('inverse')) {
                categories['Phép toán'].push(doc);
            } else {
                categories['Nâng cao'].push(doc);
            }
        });

        let html = '<div class="documents-modal-list">';
        
        Object.entries(categories).forEach(([category, docs]) => {
            if (docs.length > 0) {
                html += `
                    <div class="document-category">
                        <h4 class="category-title">${category}</h4>
                        <div class="category-docs">
                `;
                
                docs.forEach(doc => {
                    const displayName = doc.name.replace('.md', '').replace(/_/g, ' ');
                    html += `
                        <div class="doc-item" data-filename="${doc.name}">
                            <span class="material-icons">description</span>
                            <span class="doc-name">${displayName}</span>
                            <span class="doc-size">${doc.size || 'N/A'}</span>
                        </div>
                    `;
                });
                
                html += `
                        </div>
                    </div>
                `;
            }
        });
        
        html += '</div>';
        return html;
    }

    initDocumentLinks() {
        const docItems = this.modalBody.querySelectorAll('.doc-item');
        docItems.forEach(item => {
            item.addEventListener('click', () => {
                const filename = item.dataset.filename;
                this.openDocument(filename);
            });
        });
    }

    // ===== Dropdown List Animation Methods =====
    handleDropdownOpen(e) {
        const select = e.target;
        
        // Trigger dropdown opening with size
        setTimeout(() => {
            if (select.size > 1 || select.multiple) {
                // Dropdown đã mở, trigger animation
                this.animateDropdownList(select);
            } else {
                // Force mở dropdown với size
                const optionCount = select.options.length;
                const maxSize = Math.min(optionCount, 6);
                select.size = maxSize;
                this.animateDropdownList(select);
                
                // Auto-close khi chọn
                const handleSelection = () => {
                    setTimeout(() => {
                        select.removeAttribute('size');
                    }, 150);
                    select.removeEventListener('change', handleSelection);
                };
                select.addEventListener('change', handleSelection);
            }
        }, 50);
    }

    handleDropdownClose(e) {
        const select = e.target;
        setTimeout(() => {
            select.removeAttribute('size');
        }, 100);
    }

    animateDropdownList(select) {
        // Reset animation
        select.style.animation = 'none';
        
        // Trigger reflow
        select.offsetHeight;
        
        // Start animation
        select.style.animation = 'dropdownSlideDown 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
        
        // Animate options với stagger effect
        const options = select.querySelectorAll('option');
        options.forEach((option, index) => {
            option.style.animation = 'none';
            option.offsetHeight; // Trigger reflow
            option.style.animation = `optionFadeIn 0.2s ease forwards`;
            option.style.animationDelay = `${index * 0.05}s`;
        });
    }
}

// ===== Application Initialization =====
document.addEventListener('DOMContentLoaded', () => {
    window.app = new ChatApp(); // Make app globally accessible
    
    // Load saved state
    window.app.loadSavedState();
    
    // Focus on input
    window.app.userInput.focus();
    
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
