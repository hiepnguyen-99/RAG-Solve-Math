# Phân tích giá trị kỳ dị (SVD)

## Định nghĩa
Phân tích giá trị kỳ dị (Singular Value Decomposition - SVD) là phép phân tích một ma trận \( A \) bất kỳ thành ba ma trận:
\[ A = U \Sigma V^T \]
Trong đó:
- \( U \) là ma trận trực giao \( m \times m \)
- \( \Sigma \) là ma trận đường chéo \( m \times n \) chứa các giá trị kỳ dị
- \( V^T \) là chuyển vị của ma trận trực giao \( n \times n \)

## Ý nghĩa hình học
SVD biểu diễn ma trận như một phép biến đổi gồm:
1. Xoay hệ trục đầu vào (\( V \))
2. Co giãn dọc các trục toạ độ (\( \Sigma \))
3. Xoay hệ trục đầu ra (\( U \))

## Ứng dụng
- Giảm nhiễu và nén ảnh
- Giải hệ phương trình không xác định
- Phân tích dữ liệu trong học máy

## Quan hệ với trị riêng
Giá trị kỳ dị là căn bậc hai của trị riêng của \( A^TA \) hoặc \( AA^T \)

## Tính chất
- Mọi ma trận đều có SVD
- Giá trị kỳ dị luôn không âm
- Số giá trị kỳ dị bằng hạng của ma trận

