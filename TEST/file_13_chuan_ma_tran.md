# Chuẩn ma trận

## Định nghĩa
**Chuẩn ma trận** là một hàm ánh xạ ma trận về một số thực không âm thỏa mãn:
1. \( \|A\| \geq 0 \), và \( \|A\| = 0 \iff A = 0 \)
2. \( \|cA\| = |c|\|A\| \)
3. \( \|A + B\| \leq \|A\| + \|B\| \)

## Các loại chuẩn thông dụng
- **Chuẩn 1**: Tổng lớn nhất của các giá trị tuyệt đối theo cột
- **Chuẩn vô cùng**: Tổng lớn nhất theo hàng
- **Chuẩn Frobenius**: \( \|A\|_F = \sqrt{\sum_{i,j} |a_{ij}|^2} \)
- **Chuẩn phổ (Spectral norm)**: Giá trị kỳ dị lớn nhất của \( A \)

## Ứng dụng
- Ước lượng sai số
- Đo độ lớn của ma trận
- Phân tích hội tụ trong thuật toán số

## Tính chất
- \( \|AB\| \leq \|A\| \cdot \|B\| \)
- Dễ tính toán hơn trị riêng hoặc SVD trong một số bài toán

