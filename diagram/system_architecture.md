```mermaid
---
config:
  layout: dagre
  flowchart:
    curve: basis
---
flowchart TD
 subgraph subGraph0["Nguồn dữ liệu & Người dùng"]
    direction LR
        User["Người dùng / Web Client"]
        DataSources["Nguồn dữ liệu<br>(PDF)"]
  end
 subgraph subGraph1["Luồng nạp tri thức"]
        IngestionModule["Knowledge Ingestion Module<br>(Markdown hóa, Chunks, Embedding)"]
  end
 subgraph subGraph2["Luồng xử lý yêu cầu"]
        APIGateway["API Gateway Module"]
        RetrieverModule["Retriever Module<br>(Vector hóa câu hỏi,<br>tìm kiếm DB)"]
        GeneratorModule["Generator Module<br>(Xây dựng prompt,<br>gọi mô hình)"]
  end
 subgraph Monolith["Modular Monolith"]
    direction LR
        subGraph1
        subGraph2
  end
 subgraph subGraph4["Dịch vụ"]
        SharedDB[("ChromaDB<br>(Vector Database)")]
        FineTunedLLM["Mô hình LLM đã Fine-tune<br>Hoặc gọi API"]
  end
    User -- "B. Yêu cầu qua API" --> APIGateway
    APIGateway -- "8\. Phản hồi qua API" --> User
    DataSources -- "A. Nạp tài liệu" --> IngestionModule
    IngestionModule -- "1\. Lưu trữ<br>Vector Vmbeddings" --> SharedDB
    APIGateway -- "2\. Định tuyến yêu cầu" --> RetrieverModule
    RetrieverModule -- "4\. Trả về ngữ cảnh liên quan" --> GeneratorModule
    GeneratorModule -- "7\. Gửi câu trả lời cuối cùng" --> APIGateway
    RetrieverModule -- "3\. Đọc các vector liên quan" --> SharedDB
    GeneratorModule -- "5\. Gửi prompt" --> FineTunedLLM
    FineTunedLLM -- "6\. Trả về văn bản được tạo" --> GeneratorModule
    style SharedDB fill:#dae8fc,stroke:#6c8ebf,stroke-width:2px
    style FineTunedLLM fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style Monolith fill:#f0f6ff,stroke:#0b5394,stroke-width:2px
