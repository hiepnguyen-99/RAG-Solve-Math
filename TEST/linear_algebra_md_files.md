# Hệ phương trình tuyến tính

## Định nghĩa
Một **hệ phương trình tuyến tính** là tập hợp các phương trình có dạng:
\[ a_1x_1 + a_2x_2 + \dots + a_nx_n = b \]

## Phương pháp giải
- **Khử Gauss (Gaussian elimination)**
- **Nghịch đảo ma trận**
- **Phân tích LU**

## Ma trận hệ số và vector hằng số
Một hệ phương trình có thể viết lại dưới dạng ma trận:
\[ AX = B \]
Trong đó:
- \( A \): Ma trận hệ số
- \( X \): Vector ẩn
- \( B \): Vector kết quả

## Số nghiệm
- **Không có nghiệm**: hệ vô nghiệm
- **Một nghiệm duy nhất**: hệ xác định
- **Vô số nghiệm**: hệ suy biến

# Các loại ma trận đặc biệt

## Ma trận đường chéo (Diagonal Matrix)
Tất cả phần tử ngoài đường chéo chính đều bằng 0.

## Ma trận tam giác
- **Tam giác trên**: tất cả phần tử dưới đường chéo bằng 0
- **Tam giác dưới**: ngược lại

## Ma trận trực giao
Ma trận \( Q \) được gọi là **trực giao** nếu:
\[ Q^TQ = QQ^T = I \]

## Ma trận đối xứng
Ma trận \( A \) đối xứng nếu \( A = A^T \)

## Ma trận khả nghịch (Invertible Matrix)
Tồn tại ma trận \( A^{-1} \) sao cho:
\[ AA^{-1} = A^{-1}A = I \]


# Không gian đối ngẫu (Dual space)

## Định nghĩa
Không gian đối ngẫu \( V^* \) của không gian vector \( V \) là tập tất cả các ánh xạ tuyến tính từ \( V \) vào \( \mathbb{R} \).

## Phần tử của \( V^* \)
Gọi là **hàm tuyến tính** hay **hàm đối ngẫu**.

## Cơ sở đối ngẫu
Nếu \( \{v_1, v_2, ..., v_n\} \) là cơ sở của \( V \), thì tồn tại cơ sở đối ngẫu \( \{f_1, ..., f_n\} \) sao cho:
\[ f_i(v_j) = \delta_{ij} \]

# Ứng dụng của đại số tuyến tính trong học máy

## Biến đổi PCA (Principal Component Analysis)
- Giảm chiều dữ liệu bằng cách chiếu lên không gian con
- Sử dụng trị riêng và vector riêng

## Học sâu (Deep learning)
- Ma trận trọng số trong mạng neuron
- Tích vô hướng, chuẩn hóa, đạo hàm ma trận

## Hồi quy tuyến tính
- Dự đoán đầu ra bằng tổ hợp tuyến tính các đầu vào
- Tối ưu nghiệm bằng đạo hàm và phương pháp ma trận

# Phân kỳ và cơ hội dòng trong đại số tuyến tính

## Giá trị kỳ vọng của ma trận lặp
Nghiên cứu các ma trận lặp khi số lần nhân tiến tới vô hạn.

## Lý thuyết Markov
- Ma trận chuyển trạng thái
- Vector trạng thái ổn định

## Ứng dụng trong kinh tế
- Phân tích đầu vào - đầu ra Leontief
- Dòng chảy tài nguyên, sản xuất

