# Không gian vector

## Định nghĩa
Một **không gian vector** (hay không gian tuyến tính) là một tập hợp các phần tử gọi là **vector**, cùng với hai phép toán:
- **Cộng vector**
- **Nhân vector với vô hướng**

Các phép toán này phải thỏa mãn 8 tiên đề cơ bản:
1. Tính kết hợp của phép cộng
2. Tính giao hoán của phép cộng
3. Tồn tại phần tử không (vector không)
4. Tồn tại phần tử đối
5. Tính kết hợp của phép nhân vô hướng
6. Tính phân phối của phép nhân vô hướng với phép cộng vector
7. Tính phân phối của phép nhân vô hướng với phép cộng vô hướng
8. Phần tử đơn vị nhân với vector không đổi

## Ví dụ về không gian vector
- \( \mathbb{R}^n \): Tập hợp tất cả các vector có n phần tử thực
- Tập các đa thức có bậc nhỏ hơn hoặc bằng n
- Tập các hàm liên tục trên một đoạn \( [a, b] \)

## Tập con sinh (Span)
**Tập con sinh** của một tập hợp các vector là tập tất cả các tổ hợp tuyến tính có thể có từ các vector trong tập hợp đó.

## Cơ sở và số chiều
- **Cơ sở** là một tập các vector vừa **sinh ra không gian vector**, vừa **độc lập tuyến tính**.
- **Số chiều** là số lượng vector trong một cơ sở bất kỳ của không gian đó.

## Không gian con
Một tập con \( W \subseteq V \) là một **không gian con** nếu:
- \( W \) chứa vector không
- \( W \) đóng dưới phép cộng và nhân vô hướng

## Độc lập tuyến tính
Một tập hợp các vector \( \{v_1, v_2, ..., v_n\} \) là **độc lập tuyến tính** nếu phương trình \( c_1v_1 + c_2v_2 + ... + c_nv_n = 0 \) chỉ có nghiệm duy nhất là \( c_1 = c_2 = ... = c_n = 0 \).


# Biến đổi tuyến tính

## Định nghĩa
Một **biến đổi tuyến tính** là một hàm ánh xạ \( T: V \rightarrow W \) giữa hai không gian vector sao cho:
- \( T(u + v) = T(u) + T(v) \)
- \( T(cu) = cT(u) \) với mọi vector \( u, v \in V \) và mọi vô hướng \( c \)

## Hạt nhân và ảnh
- **Hạt nhân** (kernel): \( \text{Ker}(T) = \{v \in V \mid T(v) = 0\} \)
- **Ảnh** (image): \( \text{Im}(T) = \{T(v) \mid v \in V\} \)

## Định lý hạng-nullity
Cho ánh xạ tuyến tính \( T: V \to W \), ta có:
\[ \dim(V) = \text{rank}(T) + \text{nullity}(T) \]

## Biểu diễn ma trận
Mỗi biến đổi tuyến tính giữa các không gian hữu hạn chiều có thể biểu diễn bởi một ma trận. Cột của ma trận là ảnh của các vector cơ sở.

## Thành phần của biến đổi tuyến tính
- **Hạng (Rank)**: Số chiều của ảnh
- **Nullity**: Số chiều của hạt nhân


# Ma trận

## Khái niệm
**Ma trận** là một bảng hình chữ nhật gồm các số, sắp xếp theo hàng và cột. Ma trận kích thước \( m \times n \) có \( m \) hàng và \( n \) cột.

## Các phép toán với ma trận
- **Cộng trừ ma trận**: Thực hiện theo phần tử tương ứng
- **Nhân ma trận với vô hướng**
- **Nhân hai ma trận**: Ma trận \( A_{m \times n} \) nhân với \( B_{n \times p} \) cho kết quả là ma trận \( C_{m \times p} \)

## Ma trận đặc biệt
- **Ma trận đơn vị (I)**: Ma trận vuông có đường chéo chính là 1, còn lại là 0
- **Ma trận đường chéo**
- **Ma trận khả nghịch**: Ma trận có tồn tại ma trận nghịch đảo \( A^{-1} \) sao cho \( AA^{-1} = I \)

## Định thức
Chỉ áp dụng cho ma trận vuông. Định thức có tính chất:
- \( \text{det}(AB) = \text{det}(A) \cdot \text{det}(B) \)
- Ma trận khả nghịch khi và chỉ khi \( \text{det}(A) \neq 0 \)

# Trị riêng và vector riêng

## Định nghĩa
Cho ma trận vuông \( A \), một số \( \lambda \) là **trị riêng** nếu tồn tại vector \( v \neq 0 \) sao cho:
\[ Av = \lambda v \]

Vector \( v \) được gọi là **vector riêng** tương ứng với trị riêng \( \lambda \).

## Đa thức đặc trưng
Để tìm trị riêng, giải phương trình:
\[ \text{det}(A - \lambda I) = 0 \]
Đây là **đa thức đặc trưng** của ma trận \( A \).

## Đường chéo hóa
Ma trận \( A \) gọi là **đường chéo hóa được** nếu tồn tại ma trận khả nghịch \( P \) sao cho:
\[ P^{-1}AP = D \]
Trong đó \( D \) là ma trận đường chéo với các trị riêng nằm trên đường chéo.

## Ứng dụng
- Giải hệ phương trình vi phân
- Phân tích PCA trong học máy
- Nâng lũy thừa ma trận


# Không gian tích vô hướng

## Định nghĩa
Một **không gian tích vô hướng** là không gian vector có thêm một phép toán:
\[ \langle u, v \rangle \]
thoả mãn:
1. Tuyến tính theo thành phần đầu
2. Đối xứng: \( \langle u, v \rangle = \langle v, u \rangle \)
3. Tích vô hướng dương: \( \langle v, v \rangle \ge 0 \), và bằng 0 khi \( v = 0 \)

## Chuẩn và khoảng cách
- **Chuẩn (norm)** của vector \( v \): \( \|v\| = \sqrt{\langle v, v \rangle} \)
- **Khoảng cách** giữa \( u \) và \( v \): \( d(u, v) = \|u - v\| \)

## Trực giao và cơ sở trực chuẩn
- Hai vector \( u, v \) là **trực giao** nếu \( \langle u, v \rangle = 0 \)
- Tập vector là **trực chuẩn** nếu tất cả các vector đều có độ dài 1 và trực giao với nhau

## Quá trình Gram-Schmidt
Là một thuật toán dùng để tạo cơ sở trực chuẩn từ một tập vector bất kỳ, đảm bảo độc lập tuyến tính và trực giao hóa.

## Ứng dụng
- Biến đổi Fourier
- Giải hệ phương trình tuyến tính bằng phương pháp chiếu
- Nén dữ liệu bằng phân tích thành phần chính (PCA)

