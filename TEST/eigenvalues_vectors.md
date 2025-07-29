# Chương 9: Giá trị riêng và Vectơ riêng

Giá trị riêng (eigenvalue) và vectơ riêng (eigenvector) là những khái niệm cốt lõi trong đại số tuyến tính, với nhiều ứng dụng trong vật lý, học máy, xử lý tín hiệu và nhiều lĩnh vực khác.

## 9.1 Định nghĩa

Cho ma trận vuông A ∈ ℝ^{n×n}, nếu tồn tại vectơ không rỗng \(v \ne 0\) và số \(\lambda\) sao cho:
\[
Av = \lambda v
\]
thì \(\lambda\) gọi là giá trị riêng (eigenvalue), và \(v\) là vectơ riêng (eigenvector) tương ứng.

## 9.2 Cách tìm giá trị riêng và vectơ riêng

### Bước 1: Giải phương trình đặc trưng
\[
\det(A - \lambda I) = 0
\]
Phương trình trên cho ra các nghiệm \(\lambda\), là các giá trị riêng.

### Bước 2: Với mỗi \(\lambda\), giải phương trình:
\[
(A - \lambda I)v = 0
\]
để tìm vectơ riêng tương ứng.

## 9.3 Ví dụ đơn giản

Cho A = \[\begin{bmatrix}2 & 1 \\ 1 & 2\end{bmatrix}\]

\[
\det(A - \lambda I) = \begin{vmatrix}2-\lambda & 1 \\ 1 & 2-\lambda\end{vmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0
\]
⇒ \(\lambda_1 = 1, \lambda_2 = 3\)

Từ đó tìm vectơ riêng cho từng giá trị riêng.

## 9.4 Tính chất

- Một ma trận n×n có nhiều nhất n giá trị riêng (kể cả lặp)
- Các vectơ riêng tương ứng với các giá trị riêng khác nhau là tuyến tính độc lập
- Ma trận khả nghịch ⇔ không có giá trị riêng bằng 0

## 9.5 Ứng dụng

- Phân tích chính tắc (PCA) trong học máy
- Mô phỏng dao động trong vật lý
- Giải hệ phương trình vi phân
- Phân tích mạng và đồ thị

## 9.6 Tổng kết

Giá trị và vectơ riêng là công cụ mạnh để trích xuất các đặc trưng ẩn trong ma trận, mở đường cho nhiều ứng dụng thực tiễn từ dữ liệu lớn đến mô hình toán học phức tạp.

