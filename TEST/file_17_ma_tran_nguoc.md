# Ma trận nghịch đảo

## Định nghĩa
Ma trận \( A \) khả nghịch nếu tồn tại ma trận \( A^{-1} \) sao cho:
\[ AA^{-1} = A^{-1}A = I \]

## Điều kiện tồn tại
- Ma trận vuông
- \( \text{det}(A) \neq 0 \)

## Cách tính
- Dùng công thức định thức và ma trận phụ hợp
- Khử Gauss-Jordan: ghép \( A \) với \( I \), đưa về \( [I | A^{-1}] \)

## Tính chất
- \( (A^{-1})^{-1} = A \)
- \( (AB)^{-1} = B^{-1}A^{-1} \)
- \( (A^T)^{-1} = (A^{-1})^T \)

## Ứng dụng
- Giải hệ phương trình \( AX = B \)
- Tính giá trị kỳ dị, trị riêng
- Ứng dụng trong học máy và điều khiển

