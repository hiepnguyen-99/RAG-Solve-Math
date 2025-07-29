# Chương 4: Ma trận chuyển vị

Chuyển vị là một phép biến đổi quan trọng giúp hoán đổi hàng và cột của ma trận. Khái niệm này rất hữu ích trong giải tích, lập trình, và các bài toán đại số tuyến tính.

## 4.1 Định nghĩa

Cho ma trận A kích thước m x n, ma trận chuyển vị A^T (hoặc A') là ma trận n x m sao cho phần tử hàng i, cột j của A trở thành phần tử hàng j, cột i của A^T.

\[(A^T)_{ij} = A_{ji}\]

Ví dụ:
\[
A = \begin{bmatrix}1 & 2 & 3 \\ 4 & 5 & 6\end{bmatrix} \Rightarrow A^T = \begin{bmatrix}1 & 4 \\ 2 & 5 \\ 3 & 6\end{bmatrix}
\]

## 4.2 Tính chất của chuyển vị

- \((A^T)^T = A\)
- \((A + B)^T = A^T + B^T\)
- \((kA)^T = kA^T\)
- \((AB)^T = B^T A^T\)

Lưu ý: Phép chuyển vị của tích ma trận là tích của các chuyển vị theo thứ tự ngược lại.

## 4.3 Ứng dụng

- Kiểm tra tính đối xứng: A là ma trận đối xứng nếu A = A^T
- Trong giải hệ phương trình tuyến tính, đặc biệt khi làm việc với ma trận hệ số và ma trận nghịch đảo
- Trong lập trình, chuyển vị thường dùng để tối ưu hóa lưu trữ và truy xuất dữ liệu

## 4.4 Tổng kết

Ma trận chuyển vị là một phép toán đơn giản nhưng rất hữu ích. Việc thành thạo thao tác này giúp hỗ trợ các phép toán phức tạp hơn như tìm định thức, ma trận nghịch đảo, và phân tích ma trận.

