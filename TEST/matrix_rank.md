# Chương 6: Hạng của Ma trận

Hạng của ma trận là một khái niệm quan trọng trong đại số tuyến tính, phản ánh mức độ độc lập tuyến tính của các hàng hoặc cột trong ma trận.

## 6.1 Định nghĩa

Hạng của ma trận A, ký hiệu là rank(A), là số lượng lớn nhất của các hàng (hoặc cột) độc lập tuyến tính trong A.

Nó cũng bằng cấp của ma trận con vuông có định thức khác 0 lớn nhất có thể tìm được trong A.

## 6.2 Cách xác định hạng

### Phương pháp 1: Dựa vào định thức
- Tìm tất cả ma trận con vuông có định thức khác 0
- Bậc lớn nhất của các ma trận con đó chính là hạng

### Phương pháp 2: Biến đổi sơ cấp
- Đưa ma trận về dạng bậc thang (row echelon form)
- Đếm số hàng khác 0
- Số hàng khác 0 chính là hạng của ma trận

## 6.3 Tính chất của hạng

- rank(A) ≤ min(m, n) với ma trận m x n
- rank(A) = rank(A^T)
- rank(AB) ≤ min(rank(A), rank(B))
- rank(A) không thay đổi khi thực hiện các phép biến đổi sơ cấp trên hàng hoặc cột

## 6.4 Ý nghĩa hình học

- Hạng = số chiều của không gian con được tạo bởi các vectơ hàng hoặc cột
- Nếu hạng bằng số chiều không gian ⇒ các vectơ sinh đầy đủ không gian (cơ sở)

## 6.5 Ứng dụng

- Kiểm tra nghiệm của hệ phương trình tuyến tính
- Tìm nghiệm duy nhất, vô nghiệm, hay vô số nghiệm
- Phân tích cấu trúc ma trận trong các mô hình toán học, máy học, v.v.

## 6.6 Tổng kết

Hạng ma trận cung cấp thông tin về cấu trúc tuyến tính của hệ thống vectơ. Nó đóng vai trò trung tâm trong việc giải hệ phương trình và phân tích dữ liệu trong khoa học máy tính và trí tuệ nhân tạo.

