# Chương 8: Giải hệ phương trình tuyến tính bằng Ma trận

Giải hệ phương trình tuyến tính là một trong những ứng dụng quan trọng nhất của ma trận trong toán học và kỹ thuật.

## 8.1 Dạng ma trận của hệ phương trình

Một hệ phương trình tuyến tính có thể viết dưới dạng:
\[
\begin{cases}
a_1x + b_1y + c_1z = d_1 \\
a_2x + b_2y + c_2z = d_2 \\
a_3x + b_3y + c_3z = d_3
\end{cases}
\]
Dạng ma trận:
\[
AX = B
\]
Trong đó:
- A: ma trận hệ số
- X: vectơ ẩn số
- B: vectơ kết quả

## 8.2 Các phương pháp giải

### 1. Phương pháp ma trận nghịch đảo
Nếu A khả nghịch:
\[
X = A^{-1}B
\]

### 2. Phương pháp Cramer (áp dụng cho hệ n phương trình với n ẩn)
\[
x_i = \frac{|A_i|}{|A|}, \quad i = 1, 2, ..., n
\]
Trong đó A_i là ma trận A thay cột thứ i bằng vectơ B.

### 3. Phương pháp khử Gauss
- Dùng biến đổi sơ cấp để đưa ma trận mở rộng [A|B] về dạng bậc thang
- Giải ngược từ hàng dưới lên

### 4. Phương pháp khử Gauss-Jordan
- Tiếp tục biến đổi đến khi A trở thành ma trận đơn vị ⇒ vectơ kết quả là nghiệm

## 8.3 Số nghiệm của hệ phương trình

Dựa vào hạng:
- Nếu rank(A) = rank([A|B]) = số ẩn ⇒ nghiệm duy nhất
- Nếu rank(A) = rank([A|B]) < số ẩn ⇒ vô số nghiệm
- Nếu rank(A) < rank([A|B]) ⇒ vô nghiệm

## 8.4 Tổng kết

Ma trận là công cụ mạnh mẽ để biểu diễn và giải hệ phương trình tuyến tính. Các phương pháp như nghịch đảo, khử Gauss và định lý Cramer giúp xử lý hệ một cách hiệu quả trong cả lý thuyết và thực hành.

