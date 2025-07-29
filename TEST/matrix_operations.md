# Chương 2: Các phép toán cơ bản với Ma trận

Trong chương này, chúng ta sẽ tìm hiểu các phép toán cơ bản có thể thực hiện trên ma trận. Đây là nền tảng quan trọng để học các khái niệm nâng cao hơn sau này.

## 2.1 Phép cộng và trừ ma trận

Hai ma trận có thể cộng hoặc trừ nếu và chỉ nếu chúng có cùng kích thước (số hàng và số cột).

Cho hai ma trận A = \[a_{ij}\] và B = \[b_{ij}\] cùng kích thước m x n:
- A + B = \[a_{ij} + b_{ij}\]
- A - B = \[a_{ij} - b_{ij}\]

Ví dụ:
\[
A = \begin{bmatrix}1 & 2 \\ 3 & 4\end{bmatrix},\quad B = \begin{bmatrix}5 & 6 \\ 7 & 8\end{bmatrix}
\]
\[
A + B = \begin{bmatrix}6 & 8 \\ 10 & 12\end{bmatrix}
\]

## 2.2 Phép nhân ma trận với một số vô hướng

Cho ma trận A = \[a_{ij}\] và số thực k:
- kA = \[k \cdot a_{ij}\]

Ví dụ:
\[
k = 2,\quad A = \begin{bmatrix}1 & 2 \\ 3 & 4\end{bmatrix} \Rightarrow 2A = \begin{bmatrix}2 & 4 \\ 6 & 8\end{bmatrix}
\]

## 2.3 Phép nhân hai ma trận

Phép nhân hai ma trận A (m x n) và B (n x p) chỉ xác định khi số cột của A bằng số hàng của B.

Phép nhân được định nghĩa như sau:
\[(AB)_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}\]

Ví dụ:
\[
A = \begin{bmatrix}1 & 2 \\ 3 & 4\end{bmatrix},\quad B = \begin{bmatrix}2 & 0 \\ 1 & 2\end{bmatrix}
\]
\[
AB = \begin{bmatrix}(1\cdot2 + 2\cdot1) & (1\cdot0 + 2\cdot2) \\ (3\cdot2 + 4\cdot1) & (3\cdot0 + 4\cdot2)\end{bmatrix} = \begin{bmatrix}4 & 4 \\ 10 & 8\end{bmatrix}
\]

## 2.4 Tính chất các phép toán

- Giao hoán: A + B = B + A
- Kết hợp: (A + B) + C = A + (B + C)
- Phân phối: k(A + B) = kA + kB
- Không giao hoán với phép nhân: AB ≠ BA (trong hầu hết các trường hợp)

## 2.5 Tổng kết

Các phép toán cơ bản trên ma trận giúp xây dựng nền tảng cho việc giải phương trình tuyến tính, tìm định thức, và phân tích ma trận trong các ứng dụng kỹ thuật và khoa học.

