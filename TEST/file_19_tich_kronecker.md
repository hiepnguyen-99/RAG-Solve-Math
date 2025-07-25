# Tích Kronecker

## Định nghĩa
Tích Kronecker của hai ma trận \( A \in \mathbb{R}^{m \times n} \) và \( B \in \mathbb{R}^{p \times q} \):
\[ A \otimes B = \begin{bmatrix} a_{11}B & a_{12}B & \dots & a_{1n}B \\ a_{21}B & a_{22}B & \dots & a_{2n}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \dots & a_{mn}B \end{bmatrix} \]

## Kích thước
\( (m \cdot p) \times (n \cdot q) \)

## Tính chất
- Không giao hoán
- \( (A \otimes B)(C \otimes D) = (AC \otimes BD) \)
- \( (A \otimes B)^T = A^T \otimes B^T \)

## Ứng dụng
- Xử lý ảnh và tín hiệu
- Biểu diễn hệ thống động lực học lớn
- Trong học sâu: mô hình hóa tương tác đa chiều

