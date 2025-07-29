# Chương 5: Định thức của Ma trận

Định thức là một giá trị vô hướng đặc biệt được tính từ các phần tử của một ma trận vuông. Nó cung cấp thông tin quan trọng về ma trận như khả năng nghịch đảo, tính tuyến tính độc lập và thể tích hình học.

## 5.1 Định nghĩa

Định thức chỉ xác định cho ma trận vuông. Ký hiệu: det(A) hoặc |A|

### Với ma trận 2x2:
\[
A = \begin{bmatrix}a & b \\ c & d\end{bmatrix} \Rightarrow |A| = ad - bc
\]

### Với ma trận 3x3:
\[
A = \begin{bmatrix}a & b & c \\ d & e & f \\ g & h & i\end{bmatrix}
\]
\[
|A| = a(ei - fh) - b(di - fg) + c(dh - eg)
\]

## 5.2 Tính chất của định thức

- |A^T| = |A|
- |AB| = |A||B|
- Nếu A có một hàng hoặc cột là tổ hợp tuyến tính của các hàng/cột khác ⇒ |A| = 0
- Nếu hoán vị hai hàng (hoặc hai cột) của A ⇒ đảo dấu định thức
- Nếu nhân một hàng/cột với k ⇒ định thức cũng nhân với k

## 5.3 Phương pháp tính định thức

- Phương pháp Laplace: triển khai theo hàng hoặc cột
- Biến đổi sơ cấp: đưa về ma trận tam giác rồi tính tích các phần tử đường chéo
- Dùng định nghĩa cho kích thước nhỏ (2x2, 3x3)

## 5.4 Ý nghĩa hình học

- |A| cho biết thể tích của hình hộp do các vectơ cột của A sinh ra
- |A| = 0 ⇔ các vectơ phụ thuộc tuyến tính (không tạo ra không gian đầy đủ)

## 5.5 Ứng dụng

- Kiểm tra tính khả nghịch của ma trận (|A| ≠ 0 ⇔ A khả nghịch)
- Giải hệ phương trình tuyến tính (Cramer)
- Tính toán trong vi phân, tích phân đa biến

## 5.6 Tổng kết

Định thức là công cụ mạnh mẽ để phân tích cấu trúc và hành vi của ma trận. Nó kết nối đại số tuyến tính với hình học và nhiều lĩnh vực ứng dụng khác.

