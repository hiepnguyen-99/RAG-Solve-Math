# Phân tích QR

## Định nghĩa
Phân tích QR là việc phân tích một ma trận \( A \) thành tích của hai ma trận:
\[ A = QR \]
Trong đó:
- \( Q \) là ma trận trực giao (\( Q^TQ = I \))
- \( R \) là ma trận tam giác trên

## Ứng dụng
- Giải hệ phương trình tuyến tính
- Tìm nghiệm gần đúng của hệ phương trình quá xác định (least squares)
- Cơ sở trong các thuật toán phân tích phổ trị riêng

## Phương pháp Gram-Schmidt
Dùng để xây dựng ma trận \( Q \) từ các vector cơ sở ban đầu.

## Tính chất
- Ma trận \( Q \) có các vector trực chuẩn làm cột
- Phân tích QR tồn tại nếu \( A \) có hạng đầy đủ

## Biến thể
- **QR có trọng số**: ứng dụng trong thống kê
- **Phân tích QR mỏng**: chỉ lấy phần cần thiết để tiết kiệm bộ nhớ

