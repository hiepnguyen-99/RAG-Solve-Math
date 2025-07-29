# Chương 7: Ma trận nghịch đảo

Ma trận nghịch đảo là một khái niệm quan trọng dùng để giải hệ phương trình tuyến tính, biến đổi tọa độ và nhiều ứng dụng trong toán học và kỹ thuật.

## 7.1 Định nghĩa

Cho ma trận vuông A kích thước n x n, nếu tồn tại một ma trận B sao cho:
\[ AB = BA = I \]
trong đó I là ma trận đơn vị cùng kích thước, thì B gọi là ma trận nghịch đảo của A và ký hiệu là A^{-1}.

## 7.2 Điều kiện tồn tại

- A phải là ma trận vuông
- |A| ≠ 0 (tức là định thức khác 0)

Nếu |A| = 0 ⇒ A không khả nghịch (không tồn tại ma trận nghịch đảo).

## 7.3 Cách tính ma trận nghịch đảo

### Phương pháp 1: Dùng công thức (chỉ áp dụng với 2x2)
\[
A = \begin{bmatrix}a & b \\ c & d\end{bmatrix} \Rightarrow A^{-1} = \frac{1}{ad - bc} \begin{bmatrix}d & -b \\ -c & a\end{bmatrix}
\]

### Phương pháp 2: Dùng ma trận phụ hợp, chuyển vị và định thức (cho mọi kích thước)
\[
A^{-1} = \frac{1}{|A|} \cdot adj(A)
\]
Trong đó adj(A) là ma trận phụ hợp (chuyển vị của ma trận các phần tử phụ đại số).

### Phương pháp 3: Dùng biến đổi sơ cấp (Gauss-Jordan)
- Gắn A với ma trận đơn vị I thành [A|I]
- Dùng biến đổi sơ cấp đưa A về I ⇒ phần bên phải sẽ trở thành A^{-1}

## 7.4 Tính chất

- \((A^{-1})^{-1} = A\)
- \((AB)^{-1} = B^{-1}A^{-1}\)
- \((A^T)^{-1} = (A^{-1})^T\)
- \((kA)^{-1} = \frac{1}{k}A^{-1}\), với k ≠ 0

## 7.5 Ứng dụng

- Giải hệ phương trình tuyến tính: \(AX = B \Rightarrow X = A^{-1}B\)
- Tính toán trong đồ họa máy tính, biến đổi affine
- Mô hình hóa trong học máy và thống kê

## 7.6 Tổng kết

Ma trận nghịch đảo giúp đơn giản hóa việc giải các hệ tuyến tính và nhiều ứng dụng tính toán phức tạp. Tuy nhiên, không phải mọi ma trận đều có nghịch đảo, nên cần kiểm tra điều kiện trước khi áp dụng.

