# Chương 1 Ma trận

## 1.1 Các khái niệm cơ bản

### Định nghĩa (Ma trận).

Ma trận cỡ m $\times$ n là một bảng số (thực hoặc phức) hình chữ nhật có m hàng và n cột.

$$ A = \begin{pmatrix} a_{11} & \ldots & a_{1j} & \ldots & a_{1n} \\ \ldots & \ldots & \ldots & \ldots & \ldots \\ a_{i1} & \ldots & a_{ij} & \ldots & a_{in} \\ \ldots & \ldots & \ldots & \ldots & \ldots \\ a_{m1} & \ldots & a_{mj} & \ldots & a_{mn} \end{pmatrix} $$

Vi du

$$ A = \begin{pmatrix} 3 & 4 & 1 \\ 2 & 0 & 5 \end{pmatrix}_{2 \times 3}, B = \begin{pmatrix} 1+i & 2 \\ 3-i & 4i \end{pmatrix}. $$

A là ma trận cỡ 2 $\times$ 3 có 2 hàng và 3 cột. Các phần tử của ma trận A:

$a_{11} =$ 3, $a_{12} =$ 4, $a_{13} =$ 1, $a_{21} =$ 2, $a_{22} =$ 0, $a_{32} =$ 5.

B là ma trận cỡ 2 $\times$ 2 có các phần tử trong phức.

### Ghi chú

• Ma trận A cỡ m $\times$ n thường được ký hiệu bởi A $= (a_{ij})_{m \times n}$.

• Tập tất cả các ma trận cỡ m $\times$ n trên trường số K được ký hiệu $M_{m \times n}(K)$.

### Ma trận không.

Ma trận không có tất cả các phần tử bằng 0, ký hiệu là 0

$$ 0_{2\times3} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}. $$

Có vô số ma trận 0 tùy theo cỡ.


### Phần tử cơ sở
Phần tử cơ sở của một hàng là phần tử khác 0 đầu tiên của hàng đó kể từ bên trái sang.

Hàng toàn số 0 thì không có phần tử cơ sở.

### Ma trận bậc thang

1. Hàng toàn số 0 (nếu có) thì nằm dưới.

2. Phần từ cơ sở hàng dưới nằm bên phải phần tử cơ sở hàng trên.

Vi dụ

$ A = \begin{pmatrix} \boxed{2} & 1 & 0 & -1 \\ 0 & 0 & \boxed{1} & 0 \\ 0 & \boxed{-1} & 0 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ không phải bậc thang. 
$B = \begin{pmatrix} \boxed{-2} & 1 & 0 & -1 \\ 0 & 0 & 0 & \boxed{2} \\ 0 & 0 & 0 & \boxed{-3} \end{pmatrix}$ không phải bậc thang.

$ C = \begin{pmatrix} \boxed{1} & 1 & 0 & 0 & 2 \\ 0 & 0 & \boxed{3} & 2 & 0 \\ 0 & 0 & 0 & 0 & \boxed{-3} \end{pmatrix}$ là ma trận bậc thang. 
$D = \begin{pmatrix} \boxed{1} & 2 & 0 & 1 \\ 0 & 0 & \boxed{-1} & 0 \\ 0 & 0 & 0 & \boxed{-4} \end{pmatrix}$ là ma trận bậc thang. 

### Ma trận chuyển vị

Chuyển vị của $A = (a_{ij})_{m \times n}$ là ma trận $A^T = (a_{ji})_{n \times m}$ thu được từ A bằng cách chuyển hàng thành cột.

Ví dụ 
$$ A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 0 & 3 \end{pmatrix} \longrightarrow A^{T} = \begin{pmatrix} 1 & 2 \\ 2 & 0 \\ 3 & 3 \end{pmatrix} $$

### Ma trận vuông 
Ma trận vuông có số hàng bằng số cột.

Tập tất cả các ma trận vuông trên trường số K được ký hiệu là $M_n[K]$.

### Đường chéo chính
Đường chéo chính của ma trận vuông A đi qua các phần tử

$a_{11}$, $a_{22}$, $\ldots$, $a_{nn}$

Vi dụ:

Ma trận vuông cấp 4 $\begin{pmatrix} \boxed{1} & 2 & 3 & 4 \\2 & \boxed{1} & -2 & 0 \\0 & 2 & \boxed{-3} & 2 \\ -1 & 1 & 2 & \boxed{0} \end{pmatrix} $ có các phần tử trên đường chéo chính là 1, 1, -3, 0.

### Ma trận tam giác

i) Ma trận vuông A $= (a_{ij})_n$ gọi là tam giác trên nếu $a_{ij} =$ 0, $\forall$ i $>$ j

Các phần tử phía dưới đường chéo chính bằng 0.

ii) Ma trận vuông A $= (a_{ij})_n$ gọi là tam giác dưới nếu $a_{ij} =$ 0, $\forall$ i $<$ j

Các phần tử phía trên đường chéo chính bằng 0.

### Ma trận chéo
Ma trận chéo có các phần tử nằm ngoài đường chéo chính bằng 0.

Hay nó vừa tam giác trên, vừa tam giác dưới.

Ma trận vuông, không cũng là ma trận chéo.

### Ma trận đơn vị
Ma trận đơn vị là ma trận chéo với các phần từ trên đường chéo bằng 1.

### Ma trận đối xứng
Ma trận đối xứng thỏa mãn $A^T = A$

### Ma trận đối xứng
Ma trận đối xứng thỏa $A^T = -A$

Vi dụ

Ma trận tam giác trên $A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 2 & 0 \\ 0 & 0 & -2 \end{pmatrix}$. Ma trận tam giác dưới $A = \begin{pmatrix} 1 & 0 & 0 \\ -3 & 0 & 0 \\ 3 & 2 & -2 \end{pmatrix}$

Ma trận chéo $D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 3 \end{pmatrix}$. Ma trận đơn vị cấp 3 là $I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$

Ma trận đối xứng $A = \begin{pmatrix} 0 & 1 & 2 \\ 1 & 2 & -3 \\ 2 & -3 & 4 \end{pmatrix}$. Ma trận phản đối xứng $A = \begin{pmatrix} 0 & -1 & 2 \\ 1 & 0 & -3 \\ -2 & 3 & 0 \end{pmatrix}$

## 1.2 Các phép biến đổi sơ cấp

Các phép biến đổi sơ cấp theo hàng

1) Nhân một hàng với 1 số khác 0: $h_i \rightarrow \alpha h_i; \alpha \neq$ 0.

2) Cộng vào một hàng một hàng khác đã được nhân với 1 số tùy ý:

$h_i \rightarrow h_i$ + $\beta h_j$, $\forall \beta$.

3) Đổi chỗ 2 hàng: $h_i \leftrightarrow h_j$.

Tương tự ta có 3 phép biến đổi theo cột.

Các phép biến đổi sơ cấp là các phép biến đổi cơ bản nhất đổi với ma trận.

### Định lý
Mọi ma trận đều có thể đưa về dạng bậc bằng các phép biến đổi sơ cấp.

Khi dùng phép biến đổi sơ cấp với ma trận, ta thu được nhiều ma trận bậc thang khác nhau.

Ví dụ: Dùng phép biến đổi sơ cấp đưa ma trận sau về dạng bậc thang
$ A = \begin{pmatrix} 1 & 1 & 1 & 2 & 1 \\ 2 & 3 & -1 & 4 & 5 \\ 3 & 2 & -3 & 7 & 4 \end{pmatrix} $

$A = \begin{pmatrix} \boxed{1} & 1 & -1 & 2 & 1 \\ 2 & 3 & -1 & 4 & 5 \\ 3 & 2 & -3 & 7 & 4 \\ -1 & 1 & 2 & -3 & 1 \end{pmatrix}$ 
$\xrightarrow[h_4 \to h_4 + h_1 ]{\substack{ h_2 \to h_2 - 2h_1 \\ h_3 \to h_2 - 3h_1}}$ $ \begin{pmatrix} \boxed{1} & 1 & -1 & 2 & 1 \\ 0 & \boxed{1} & 1 & 0 & 3 \\ 0 & -1 & 0 & 1 & 1 \\ 0 & 2 & 1 & -1 & 2 \end{pmatrix}$ 
$\xrightarrow[h_4 \to h_4 - 2h_2]{h_3 \to h_3 + h_2}$ 
$\begin{pmatrix} \boxed{1} & 1 & -1 & 2 & 1 \\ 0 & \boxed{1} & 1 & 0 & 3 \\ 0 & 0 & \boxed{1} & 1 & 4 \\ 0 & 0 & -1 & -1 & -4 \end{pmatrix}$ 

$\xrightarrow{h_4 \to h_4 + h_3}$ 
$\begin{pmatrix} \boxed{1} & 1 & -1 & 2 & 1 \\ 0 & \boxed{1} & 1 & 0 & 3 \\ 0 & 0 & \boxed{1} & 1 & 4 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}  \Rightarrow r(A) = 3. $

## 1.3 Các phép toán ma trân

Hai ma trận bằng nhau nếu chúng cùng cỡ và các phần tử tương ứng bằng nhau: $a_{ij} = b_{ij}$, $\forall$ i, j.

Cho 2 ma trận A, B cùng cỡ và số $\alpha$.

Tổng A + B: cộng các phần tử tương ứng.

Nhân $\alpha.A$: nhân $\alpha$ vào tất cả các phần tử của A.

Ví dụ 1.7 
$$ a) \begin{pmatrix} 1 & 2 & -1 \\ 2 & -1 & 0 \end{pmatrix} + \begin{pmatrix} 3 & -2 & 1 \\ 1 & 0 & 3 \end{pmatrix} = \begin{pmatrix} 4 & 0 & 0 \\ 3 & -1 & 3 \end{pmatrix}. $$

$$ b) \ 2. \begin{pmatrix} 1 & 2 & -1 \\ 2 & -1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 4 & -2 \\ 4 & -2 & 0 \end{pmatrix}. $$

$$ c) \ 2. \begin{pmatrix} 1 & 2 & -1 \\ 2 & -1 & 0 \end{pmatrix} - 3. \begin{pmatrix} 3 & -2 & 1 \\ 1 & 0 & 3 \end{pmatrix} = \begin{pmatrix} -7 & 10 & -5 \\ 1 & -2 & -9 \end{pmatrix}. $$

### Tính chất
i. $A + B = B + A$

ii. $(A+B)+C=A+(B+C)$

iii. $A + 0 = A$

iv. $\alpha(A + B) = \alpha A + \alpha B$

v. $\alpha(\beta A)=(\alpha\beta)A$

vi. $(\alpha + \beta)A = \alpha A + \beta A$

### Phép nhân ma trận
Cho A $= (a_{ij})_{m \times p}$, B $= (b_{ij})_{p \times m}$.

Tích $A.B = C = (c_{ij})_{m \times n}: c_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + \cdots + a_{ip}b_{pj}$

$$ AB = \begin{pmatrix} \dots & \dots & \dots & \dots \\ a_{i1} & a_{i2} & \dots & a_{ip} \\ \dots & \dots & \dots & \dots \end{pmatrix} \cdot \begin{pmatrix} \dots & b_{1j} & \dots \\ \dots & b_{2j} & \dots \\ \dots & \dots & \dots \end{pmatrix} = \begin{pmatrix} \dots & \dots & \dots \\ \dots & c_{ij} & \dots \\ \dots & \dots & \dots \end{pmatrix} $$

Điều kiện phép nhân AB: số cột của A bằng số hàng của B.

$c_{ij}$ là tích vô hướng hàng i của A và cột j của B.

Ví dụ: cho $ A = \begin{pmatrix} 2 & -1 & 4 \\ 4 & 1 & 0 \end{pmatrix}; B = \begin{pmatrix} 1 & -2 & 2 \\ 3 & 0 & 1 \\ 2 & 4 & 3 \end{pmatrix}. \ Tính \ AB. $

$ c_{11} = (2 \quad -1 \quad 4) \begin{pmatrix} 1 \\ 3 \\ 2 \end{pmatrix} = 2.1 + (-1).3 + 4.2 = 7$: tích vô hướng hàng 1 của A và cột 1 của B.

Tương tự, ta tính được $AB = \begin{pmatrix} 7 & 12 & 15 \\ 7 & -8 & 9 \end{pmatrix}. $

### Tính chất

i. $A(BC) = (AB)C$  

ii. $A(B + C) = AB + AC$ 

iii. $(B + C)A = BA + CA$ 

iv. $I_m A = AI_m = A$ 

v. $\alpha(AB) = (\alpha A)B = A(\alpha B)$

Chú ý: Nhìn chung $AB \neq BA$; $AB = AC \nRightarrow B = C, AB = 0 \nRightarrow A = 0 \vee B = 0.$

### Nâng lũy thừa
Quy ước: $A^0 = I \qquad A^n=A.A...A.A(n \text{ n ma trận } A)$

Ví dụ $ Cho A = \begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}$ và $f(x) = 2x^2 - 4x + 3$. Tính f(A).

Ta có

$f(A) = 2A^2 - 4A + 3I$

$$ f(A) = 2\begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}^2 - 4\begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix} + 3\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = 2\begin{pmatrix} 1 & -6 \\ 18 & 13 \end{pmatrix} - \begin{pmatrix} 8 & -4 \\ 12 & 16 \end{pmatrix} + \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} -3 & -8 \\ 24 & 13 \end{pmatrix} $$

Ví dụ 1.10 Tính $A^{200}$, với
$$ a) A = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}. \qquad  b) A = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix}. \qquad c) A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}. $$

Bài giải

$$ a) A^2 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 6 \\ 0 & 1 \end{pmatrix}, \quad A^3 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 6 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 9 \\ 0 & 1 \end{pmatrix} \Rightarrow A^{200} = \begin{pmatrix} 1 & 200.3 \\ 0 & 1 \end{pmatrix}. $$

$$ b) A = 2\begin{pmatrix} 1 & \frac{3}{2} \\ 0 & 1 \end{pmatrix} \Longrightarrow A^{200} = 2^{200} \begin{pmatrix} 1 & 200 \cdot \frac{3}{2} \\ 0 & 1 \end{pmatrix} = 2^{200} \begin{pmatrix} 0 & 300 \\ 0 & 1 \end{pmatrix}. $$

$$ c) A^2 = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}. \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} = 2 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = 2A \Longrightarrow A^{200} = 2^{199}. A = \begin{pmatrix} 2^{199} & 2^{199} \\ 2^{199} & 2^{199} \end{pmatrix}. $$

Tóm lai

$$ \begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}^n = \begin{pmatrix} 1 & na \\ 0 & 1 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}^n = 2^{n-1} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}. $$

## 1.4 Hạng của ma trận

### Hạng ma trận
Hạng ma trận A là số hàng khác 0 của ma trận bậc thang của A, ký hiệu là: r(A).

Ví dụ: Tìm hạng của ma trận $A = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 4 & 2 & 2 \\ 3 & 6 & 3 & 4 \end{pmatrix}$

$$ A = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 4 & 2 & 2 \\ 3 & 6 & 3 & 4 \end{pmatrix} \xrightarrow[h_3-3h_1]{h_2-2h_1} \begin{pmatrix} 1 & 2 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} 
\xrightarrow{h_2 \leftrightarrow h_3} \begin{pmatrix} 1 & 2 & 1 & 1 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} \implies r(A) = 2. $$

### Tính chất

i) $r(A) = 0 \Longrightarrow A = 0$

ii)$ A = (a_{ij})_{m \times n} \Longrightarrow r(A) \le \min\{m, n\}$

iii) Nếu $A \xrightarrow{\text{biến đổi sơ cấp}} B \Longrightarrow r(A) = r(B)$

## 1.5 Ma trận nghịch đảo

### Ma trận nghịch đảo
Ma trận vuông A là khả nghịch nếu tồn tại ma trận B cho

$$AB = I = BA$$

Khi đó, B gọi là nghịch đảo của A, ký hiệu là $A^{-1}$.

Ví dụ
a) Nghịch đảo của $A = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$ là $\begin{pmatrix} -3 & 2 \\ 2 & -1 \end{pmatrix}$. Vì $\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix} \begin{pmatrix} -3 & 2 \\ 2 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} -3 & 2 \\ 2 & -1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$

b) Cho $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$. Ta tìm ma trận nghịch đảo của A có dạng $B = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$

Ta có $AB = I \Longleftrightarrow \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \Longleftrightarrow \begin{pmatrix} 2a+c & 2b+d \\ 5a+c & 5b+d \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} $

$ \Leftrightarrow \begin{cases} 2a + c = 1 \\ 2b + d = 0 \\ 5a + c = 0 \\ 5b + d = 1 \end{cases} \Leftrightarrow \begin{cases} a = 3 \\ b = -1 \\ c = -5 \\ d = 2 \end{cases} \Rightarrow A^{-1} = B = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}. $

c) Hãy thử tìm ma trận nghịch đảo của $A = \begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}$

Chú ý: Không phải mt vuông nào cũng có nghịch đảo. Có rất nhiều mt vuông không có nghịch đảo.

### Sự tồn tại ma trận khả nghịch

Cho ma trận vuông A. Các mệnh đề sau tương đương

i) A khả nghịch (tồn tại $A^{-1}$).

ii) r(A) $=$ n: ma trận không suy biến 

iii) $AX = 0 \Longleftrightarrow X = 0$ 

iv) $ A \xrightarrow{\text{Biến đổi theo hàng}} I$

### Ma trận sơ cấp
Ma trận thu được từ I bằng đúng 1 phép biến đổi sơ cấp gọi là ma trận sơ cấp.

Ví dụ

$$ I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{h_3 \to 3h_3} E_1 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{pmatrix}, \qquad I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{h_2 \to h_2 + 2h_1} E_2 = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$

$$ A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \xrightarrow{h_3 \rightarrow 3h_3} \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 21 & 24 & 27 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} = E_1.A. $$

$$ A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \xrightarrow{h_2 \rightarrow h_2 + 2h_1} \begin{pmatrix} 1 & 2 & 3 \\ 6 & 9 & 12 \\ 7 & 8 & 9 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} = E_2.A. $$

Tương tự:

$$ I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{c_1 \leftrightarrow c_3} E_3 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix} \Longrightarrow A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \xrightarrow{h_3 \leftrightarrow h_1} \begin{pmatrix} 3 & 2 & 1 \\ 6 & 5 & 4 \\ 9 & 8 & 7 \end{pmatrix} = A.E_3. $$


Mỗi phép biến đổi sơ cấp tương ứng với phép nhân ma trận sơ cấp tương ứng.

Bđsc theo hàng $\Rightarrow$ nhân bên trái. Bđsc theo cột $\Rightarrow$ nhân bên phải.

Cách tìm ma trận nghịch đảo

$[A|I] \xrightarrow{\text{Bđsc theo hàng}} [I|A^{-1}]$

Ví dụ: Tìm ma trận nghịch đảo $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 2 \end{pmatrix} $

Bài giải

$
[A\mid I] =
\left(\begin{array}{ccc|ccc}
\boxed{1} & 1 & 1 & 1 & 0 & 0 \\
1 & 2 & 2 & 0 & 1 & 0 \\
1 & 2 & 3 & 0 & 0 & 1
\end{array}\right)
\xrightarrow[h_3 - h_1]{h_2 - h_1}
\left(\begin{array}{ccc|ccc}
1 & 1 & 1 & 1 & 0 & 0 \\
0 & \boxed{1} & 1 & -1 & 1 & 0 \\
0 & 1 & 2 & -1 & 0 & 1
\end{array}\right)
\xrightarrow[h_1 - h_2]{h_3 - h_2}
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 2 & -1 & 0 \\
0 & 1 & 1 & -1 & 1 & 0 \\
0 & 0 & \boxed{1} & 0 & -1 & 1
\end{array}\right)
\xrightarrow{h_2 - h_3}
\left(\begin{array}{ccc|ccc} 1 & 0 & 0 & 2 & -1 & 0 \\ 0 & 1 & 0 & -1 & 2 & -1 \\ 0 & 0 & 1 & 0 & 1 & 1 \end{array}\right) \Longrightarrow A^{-1} = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}$

### Tính chất ma trận nghịch đảo
Cho hai ma trận A, B khả nghịch. Ta có

i) $(A^{-1})^{-1} = A$

ii) $(AB)^{-1} = B^{-1}A^{-1}$ 

iii) $(A^T)^{-1} = (A^{-1})^T$.

# Chương 2 Đinh thức

## 2.1 Định nghĩa định thức và ví dụ

### Định nghĩa

Định thức ma trận vuông $ A = (a_{ij})_n $ được kí hiệu bởi

$$\det(A) = |a^{ij}|_n = |A|$$

### Bù đại số

Bù đại số của phần tử $a_{ij}$ là

$$ A_{ij} = (-1)^{i+j} \begin{vmatrix} \text{định thức thu được từ } A \\ \text{bỏ đi hàng i, cột j} \end{vmatrix}_{n-1} $$

### Định nghĩa định thức bằng qui nạp

$ i) \ k = 1 : A = [a_{11}] \Rightarrow |A| = a_{11}$

$ ii) \ k = 2 : A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \Rightarrow |A| = a_{11}A_{11} + a_{12}A_{12} = a_{11}a_{22} - a_{12}a_{21} $

$ iii) \ k = n : A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & \ddots & \vdots \\ \end{pmatrix} \Rightarrow |A| = a_{11}A_{11} + a_{12}A_{12} + \cdots + a_{1n}A_{1n} $

Ví dụ: Tính định thức của $\begin{pmatrix} 1 & 2 & -3 \\ 2 & 3 & 0 \\ 3 & 2 & 4 \end{pmatrix}$

Bài giải

$\det(A) = a_{11}A_{11}$ + $a_{12}A_{12}$ + $a_{13}A_{13} = 1A_{11}$ + $2A_{12}$ - $3A_{13}$.

$ A_{11} = (-1)^{1+1} \begin{vmatrix} 3 & 0 \\ 2 & 4 \end{vmatrix} = 12$ (từ A, bỏ hàng 1 và cột 1)

Tương tự: $\det(A) = 1(-1)^{1+1} \begin{vmatrix} 3 & 0 \\ 3 & 4 \end{vmatrix} + 2(-1)^{1+2} \begin{vmatrix} 2 & 0 \\ 3 & 4 \end{vmatrix} - 3(-1)^{1+3} \begin{vmatrix} 2 & 3 \\ 3 & 2 \end{vmatrix} = 12 - 16 + 15 = 11. $

## 2.2 Tính chất định thức

### Tính định thức bằng khai triển
Có thể tính định thức bằng cách khai triển theo một hàng hoặc 1 cột bất kỳ

$$ |A| = \begin{vmatrix} \cdots & \cdots & \cdots & \cdots \\ a_{k1} & a_{k2} & \cdots & a_{kn} \\ \cdots & \cdots & \cdots & \cdots \end{vmatrix} = a_{k1}A_{k1} + a_{k2}A_{k2} + \cdots + a_{kn}A_{kn} $$

Ví dụ 2.2 Tính định thức

$$a) \begin{vmatrix} 1 & 2 & -1 \\ 2 & 1 & 3 \\ 0 & 0 & -3 \end{vmatrix} \qquad b) \begin{vmatrix} 2 & -3 & 3 & 2 \\ 3 & 0 & 1 & 4 \\ -2 & 0 & 3 & 2 \\ 4 & 0 & -1 & 5 \end{vmatrix} $$

a) Khai triển theo hàng 3: $\begin{vmatrix} 1 & 2 & -1 \\ 2 & 1 & 3 \\ 0 & 0 & -3 \end{vmatrix} = -3(-1)^{3+3} \begin{vmatrix} 1 & 2 \\ 2 & 1 \end{vmatrix} = -3(-3) = 9. $

b) Khai triển theo cột 2
$ I = \begin{vmatrix} 2 & -3 & 3 & 2 \\ 3 & 0 & 1 & 4 \\ -2 & 0 & 3 & 2 \\ 4 & 0 & -1 & 5 \end{vmatrix} = -3(-1)^{1+2} \begin{vmatrix} 3 & 1 & 4 \\ -2 & 3 & 2 \\ 4 & -1 & 5 \end{vmatrix} \xrightarrow{\text{khai triển theo hàng 1}} = 3 \Big (3(-1)^{1+1} \begin{vmatrix} 3 & 2 \\ -1 & 5 \end{vmatrix} + 1(-1)^{1+2} \begin{vmatrix} -2 & 2 \\ 4 & 5 \end{vmatrix} + 4(-1)^{1+3} \begin{vmatrix} -2 & 3 \\ 4 & -1 \end{vmatrix}\Big ) = 3(51+18-40) = 87 $

### Tính định thức của ma trận tam giác
Định thức của ma trận tam giác bằng tích các phần tử nằm trên đường chéo chính

Ví dụ:
$ \begin{vmatrix} 1 & -2 & 2 & 3 \\ 0 & 4 & -2 & 0 \\ 0 & 0 & -3 & 2 \\ 0 & 0 & 0 & 5 \end{vmatrix} = 1.4.(-3).5 = -60 $

### Tính định thức dùng biến đổi đổi sơ cấp
Dùng biến đổi sơ cấp để tính định thức

1. Nếu A $\xrightarrow{h_i \to \alpha h_j}$ B thì |B| $= \alpha$ |A|

2. Nếu A $\xrightarrow{h_i + \beta h_j}$ B thì |B| $=$ |A|.

3. Nếu A $\xrightarrow{h_i \leftrightarrow h_j}$ B thì |B| $=$ -|A|.


### Nguyên tắc tính định thức sử dụng biến đối sơ cấp

1. Chọn 1 hàng (hoặc 1 cột tùy ý).

2. Chọn 1 phần tử khác 0 của hàng (cột) đó. Dùng biến

đối sơ cấp, khử tất cả các phần tử khác.

3. Khai triển theo hàng (hay cột) đã chọn.

Ví du 2.4.

$ (a) I = \begin{vmatrix} 1 & 1 & 2 & -1 \\ 2 & 3 & 5 & 0 \\ 3 & 2 & 6 & -2 \\ -2 & 1 & 3 & 1 \end{vmatrix} \xrightarrow[h_4 + 2h_1]{\substack{h_2 - 2h_1 \\ h_3 - 3h_1}} \begin{vmatrix} 1 & 1 & 2 & -1 \\ 0 & 1 & 1 & 2 \\ 0 & -1 & 0 & 1 \\ 0 & 3 & 7 & -1 \end{vmatrix} \xrightarrow[\text{theo cột 1}]{\text{khai triển}} 1.(-1)^{1+1} \begin{vmatrix} 1 & 1 & 2 \\ -1 & 0 & 1 \\ 3 & 7 & -1 \end{vmatrix} \frac{h_3 - 3h_1}{-1} \begin{vmatrix} 1 & 1 & 2 \\ -1 & 0 & 1 \\ -4 & 0 & -15 \end{vmatrix} = 1.(-1)^{1+2} \begin{vmatrix} -1 & 1 \\ -4 & -15 \end{vmatrix} = -1(15+4) = -19. $

$ b) \begin{vmatrix} 3 & 2 & -1 & 1 \\ 2 & 3 & -2 & 0 \\ -3 & 1 & 4 & -2 \\ 4 & 1 & 3 & 1 \end{vmatrix} \xrightarrow[h_4-h_1]{h_3+2h_1} \begin{vmatrix} 3 & 2 & -1 & 1 \\ 2 & 3 & -2 & 0 \\ 3 & 5 & 2 & 0 \\ 1 & -1 & 4 & 0 \end{vmatrix} \xrightarrow[\text{theo cột 4}]{\text{khai triển}} -1 \begin{vmatrix} 2 & 3 & -2 \\ 3 & 5 &2 \\ 1 & -1 & 4 \end{vmatrix} = -\begin{vmatrix} 2 & 3 & -2 \\ 5 & 8 & 0 \\ 5 & 5 & 0 \end{vmatrix} = 2\begin{vmatrix} 5 & 8 \\ 5 & 5 \end{vmatrix} = -30 $

### Tính chất định thức
Cho $A \in M_n$.

i) $\det(A^T) = \det(A)$ 

ii) $|\alpha A| = \alpha^n |A| $

iii) $\det(AB) = \det(A) \cdot \det(B)$

iv) $|A^m| = |A|^m$

v) A có 1 hàng (hoặc cột) bằng 0 thì $|A| = 0$

vi) A có 2 hàng (hoặc cột) tỷ lệ thì $|A| = 0$

Chú ý: nhìn chung $det(A + B) \neq \det(A) + \det(B)$.

Ví dụ: Cho $A, B \in M_3$ thỏa $|A| = 2, |B| = 3$

Ta có $|2A^3| = 2^3. |A|^3 = 8.2^3 = 64 \qquad  |3AB^T| = 3^3|A||B| = 27.2.3 = 162$

### Điều kiện khả nghịch

A khả nghịch khi và chỉ khi |A| $\neq$ 0.

**Ví dụ**: Tìm m để A.B khả nghịch. Biết $ A = \begin{pmatrix} 1 & 2 & 1 \\ 0 & -1 & 2 \\ 0 & -1 & 3 \end{pmatrix}, B = \begin{pmatrix} 2 & -1 & 3 \\ 0 & 1 & 1 \\ m & 2 & 1 \end{pmatrix}. $

**Bài làm**

AB khả nghịch khi và chỉ khi $det(AB) \neq 0$

$\iff \det(A) \cdot \det(B) \neq 0 \iff -1 \cdot (-4m-1) \neq 0 \iff m \neq -\frac{1}{4}$


## 2.3 Tìm ma trận nghịch đảo bằng phương pháp định thức

### Định nghĩa (Ma trận phụ hợp)

Ma trận phụ hợp của ma trận vuông $A \in M_n$ được định nghĩa là

$ P_A = \begin{pmatrix} A_{11} & A_{12} & \ldots & A_{1n} \\ A_{21} & A_{22} & \ldots & A_{2n} \\ \ldots & \ldots & \ldots & \ldots \\ A_{n1} & A_{n2} & \ldots & A_{nn} \end{pmatrix}. $

Công thức tính ma trận nghịch đảo $A^{-1} = \frac{1}{|A|} .P_A$

**Ví dụ** Tìm ma trận nghịch đảo $A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & 1 \\ 3 & 4 & 0 \end{pmatrix} $

**Bài làm**

$\det(A) = -2 \neq 0 \Longrightarrow$ A khả nghịch.

$ A_{11} = (-1)^{1+1} \begin{pmatrix} 3 & 1 \\ 4 & 0 \end{pmatrix} = -4, A_{12} = (-1)^{1+2} \begin{pmatrix} 2 & 1 \\ 3 & 0 \end{pmatrix} = 3, A_{13} = (-1)^{1+3} = \begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix} = -1$

Tương tự: $A_{21} = 4, A_{22} = -3, A_{23} = -1, A_{31} = -2, A_{32} = 1, A_{33} = 1. $

Ma trận nghịch đảo $A^{-1} = \frac{1}{|A|} P_A = \frac{1}{-2} \begin{pmatrix} -4 & 4 & -2 \\ 3 & -3 & 1 \\ -1 & -1 & 1 \end{pmatrix} (\text{nhớ lấy chuyển vị}). $

### Tính chất

$ i)\ |A^{-1}| = \frac{1}{|A|} $

$ ii)\ P_A = |A|^{n-1}$

$ iii)\ r(P_A) = \begin{cases} n, & \text{nếu } r(A) = n \\ 1, & \text{nếu } r(A) = n - 1 \\ 0, & \text{nếu } r(A) < n - 1 \end{cases} $

**Ví dụ**: Cho $A \in M_3$ biết $|A| = -2$. Tính $det(2P_A^2)$.

**Bài làm**

Ta có: $\det(2P_4^2) = 2^3 \cdot |P_A|^2 = 8 \cdot (|A|^{3-1})^2 = 8 \cdot (-2)^4 = 128$

**Ví dụ**: Cho $A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 3 & -1 \\ 1 & 1 & m \end{pmatrix}$. Tìm m để $r(P_A) = 1$

**Bài làm**

$ A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 3 & -1 \\ 1 & 1 & m \end{pmatrix} \xrightarrow{bdsc} \begin{pmatrix} 1 & 2 & 1 \\ 0 & -1 & -3 \\ 0 & 0 & m+2 \end{pmatrix}, r(P_A) = 1 \Longleftrightarrow r(A) = 3 - 1 = 2 \Longleftrightarrow m = -2 $

# Chương 3

### Định nghĩa (hệ phương trình tuyên tính) 
Hệ phương trình tuyến tính gồm m phương trình, n ấn có dạng

$ \left \{
\begin{array}{ccccccccc}
  a_{11}x_1 & + & a_{12}x_2 & + & \dots & + & a_{1n}x_n & = & b_1 \\
  a_{21}x_1 & + & a_{22}x_2 & + & \dots & + & a_{2n}x_n & = & b_2 \\
  \vdots    &     & \vdots    &     & \ddots &     & \vdots    &     & \vdots \\
  a_{m1}x_1 & + & a_{m2}x_2 & + & \dots & + & a_{mn}x_n & = & b_m
\end{array}
\right. $

$a_{11}, a_{12}, \ldots, a_{mn}$ được gọi là hệ số của hệ phương trình.

$b_1, b_2, \ldots, b_m$ được gọi là hệ số tự do của hệ phương trình.

Ta ký hiệu

$ A = \begin{pmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{pmatrix}, \quad
X = \begin{pmatrix}
x_1 \\ x_2 \\ \vdots \\ x_n
\end{pmatrix}, \quad
b = \begin{pmatrix}
b_1 \\ b_2 \\ \vdots \\ b_m
\end{pmatrix}, \quad
(A\mid b) = \left(
\begin{array}{cccc|c}
a_{11} & a_{12} & \dots & a_{1n} & b_1 \\
a_{21} & a_{22} & \dots & a_{2n} & b_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn} & b_m
\end{array}
\right) $

Hệ phương trình được viết lại

A.X $=$ b hoặc viết gọn (A|b).

**Chú thích**

• Một hệ phương trình tuyến tính có thể:

$$\text{1) vô nghiệm \qquad 2) có nghiệm duy nhất \qquad 3) vô số nghiệm.}$$

• Hai hệ phương trình gọi là tương đương nếu chúng cùng tập nghiệm.

• Để giải hệ phương trình, ta dùng phép biến đổi tương đương để đưa về hệ đơn giản.


### Phép biến đổi tương đương

Một phép biến đổi được gọi là tương đương nếu nó biến một hệ phương trình bất kỳ thành một hệ phương trình tương đương.

Ta có 3 phép biến đổi tương đương thường gặp:

i) Nhân 2 về của một phương trình với 1 số khác 0.

ii) Cộng vào một phương trình một phương trình khác đã được nhân với một số tùy ý.

iii) Đổi chổ hai phương trình.

**Chú ý**:

• Đây là 3 phép biến đổi quen thuộc ở phổ thông mà chúng ta đã biết.

• Nếu ta ký hiệu hệ phương trình ở dạng ma trận mở rộng (A|b). Các phép biến đổi sơ cấp đối với ma trận tương ứng với các phép biến đổi tương đương đối với hệ phương trình.

### Ẩn cơ sở
Ẩn cơ sở của hệ phương trình ở dạng bậc thang

$\bullet$ Ẩn cơ sở là ẩn tương ứng với cột chứa phần tử cơ sở.

$\bullet$ Ẩn tự do là ẩn tương ứng với cột không có phần tử cơ sở.

Ví dụ:
$
\left[
\begin{array}{cccc|c}
1 & 1 & 1 & 2 & 1 \\
2 & 2 & 3 & 5 & 6 \\
3 & 3 & 4 & 1 & -1
\end{array}
\right]
\xrightarrow{\text{Biến đổi sơ cấp}}
\left[
\begin{array}{cccc|c}
(1) & 1 & 1 & 2 & 1 \\ 
0 & 0 & (1) & 1 & 4 \\ 
0 & 0 & 0 & (-6) & -8 
\end{array}
\right] $

$x_1$, $x_3$, $x_4$ là phần tử cơ sở. $x_2$ là phần tử tự do.

### Các bước giải hệ phương trình

Bước 1: Đưa ma trận $\tilde{A} = [A|b]$ về dạng bậc thang bằng biến đổi sơ cấp theo hàng.

Kiểm tra hệ có nghiệm hay không.

Bước 2: Giải hệ phương trình từ dưới lên.

**Ví dụ** Giải hệ phương trình

$ \begin{cases} x_1 + x_2 - x_3 + 2x_4 = 1 \\ 2x_1 + 3x_2 - 3x_3 + 3x_4 = 3 \\ 3x_1 + 2x_2 - 5x_3 + 7x_4 = 5 \end{cases} $

**Bài làm**

$ \tilde{A} = \left[\begin{array}{cccc|c} 1 & 1 & -1 & 2 & 1 \\ 2 & 3 & -3 & 3 & 3 \\ 3 & 2 & -5 & 7 & 5 \end{array}\right] \xrightarrow[h_3-3h_1]{h_2-2h_1} \left[\begin{array}{cccc|c} 1 & 1 & -1 & 2 & 1 \\ 0 & 1 & -1 & -1 & 1 \\ 0 & -1 & -2 & 1 & 2 \end{array}\right] \xrightarrow{h_3+h_2} \left[ \begin{array}{cccc|c} \boxed{1} & 1 & -1 & 2 & 1 \\ 0 & \boxed{1} & -1 & -1 & 1 \\ 0 & 0 & \boxed{-3} & 0 & 3 \end{array} \right]$

Dặt $x_4 = \alpha$. pt (3): $x_3 = -1$. Từ pt (2): $x_2 = 1 + x_3 + x_4 = \alpha$. Từ pt (1): $x_1 = 1 - x_2 + x_3 - 2x_4 = -3\alpha$.

Vậy nghiệm của hệ là $(x_1, x_2, x_3, x_4) = (-3\alpha, \alpha, -1, \alpha), \alpha \in R$



### Định lý Kronecker Capelli

Nếu $r(A|b) \neq r(A)$ thì hệ $AX = b$ vô nghiệm.

Nếu $r(A|b) = r(A)$ thì hệ $AX = b$ có nghiệm.

i) Nếu $r(A|b) = r(A) =$ số ẩn thì hệ $AX $=$ b$ có nghiệm duy nhất.

ii) Nếu $r(A|b) = r(A)$ < số ẩn thì hệ $AX = b$ có vô số nghiệm.

**Ví dụ** Tìm tất cả các giá trị của m để hệ sau vô số nghiệm

$ \begin{cases}x_1 + x_2 - 2x_3 = 1 \\
2x_1 + 3x_2 - 3x_3 = 5 \\
3x_1 + mx_2 - 7x_3 = 8\end{cases} $

**Bài làm**

$ [A|b]=\left[\begin{array}{ccc|c} 1 & 1 & -2 & 1 \\ 2 & 3 & -3 & 5 \\ 3 & m & -7 & 8 \end{array}\right]\longrightarrow \left[\begin{array}{ccc|c} 1 & 1 & -2 & 1 \\ 0 & 1 & 1 & 3 \\ 0 & m-3 & -1 & 5 \end{array}\right]\longrightarrow \left[\begin{array}{ccc|c} 1 & -2 & 1 & 1 \\ 0 & 1 & 1 & 3 \\ 0 & -1 & m-3 & 5 \end{array}\right]\longrightarrow \left[\begin{array}{ccc|c} 1 & -2 & 1 & 1 \\ 0 & 1 & 1 & 3 \\ 0 & 0 & m-2 & 8 \end{array}\right] $

Hệ vô số nghiệm khi và chỉ khi r(A) = r(A) < 3. Vì r(A|b) $=$ 3 nên không tồn tại m để hệ vô số nghiệm.

**Ví dụ** Tìm tất cả các giá trị m để hệ có nghiệm duy nhất

$ \begin{cases}x_1 + 2x_2 + x_3 - x_4 = 5 \\
2x_1 + mx_2 - x_3 = -1 \\
mx_1 + x_2 - 3x_4 = 6\end{cases} $

Vì hệ có 3 phương trình nên r(A) $\leq$ 3 $<$ 4 = số ẩn nên hệ không có nghiệm duy nhất.

Chú ý: Nếu hệ có số phương trình ít hơn số ẩn thì không thể có nghiệm duy nhất.

## 3.1 Hệ Cramer

Hệ AX $=$ b gọi là hệ Cramer nếu A là ma trận vuông và $\det(A) \neq$ 0.

Hệ Cramer có nghiệm duy nhất

$x_i = \frac{|A_i|}{|A|}, i \in \overline{1,n}$

với $A_i$ là ma trận thu từ A bằng cách thay cột i bởi cột tự do b.

**Ví dụ** Kiểm tra hệ sau là Cramer và giải hệ

$ \begin{cases}x_1 + 2x_2 - x_3 = 12 \\
2x_1 + 3x_2 - 3x_3 = 4 \\
3x_1 + 2x_2 + 5x_3 = -8\end{cases} $

**Bài làm**

$ A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 3 & -3 \\ 3 & 2 & 5 \end{pmatrix}, A_1 = \begin{pmatrix} 12 & 2 & -1 \\ 4 & 3 & -3 \\ -8 & 2 & 5 \end{pmatrix}, A_2 = \begin{pmatrix} 1 & 12 & -1 \\ 2 & 4 & -3 \\ 3 & -8 & 5 \end{pmatrix} A_3 = \begin{pmatrix} 1 & 2 & 12 \\ 2 & 3 & 4 \\ 3 & 2 & -8 \end{pmatrix} $

$|A| = -12 \neq 0$ nên hệ là Cramer.

$|A_1| = 228, |A_2| = -204, |A_3| = -36$. Nghiệm của hệ là $\left(\frac{|A_1|}{|A|}, \frac{|A_2|}{|A|}, \frac{|A_3|}{|A|}\right) = (-19, 17, 3)$

## 3.2 Hệ thuần nhất

### Hệ thuần nhất

• Hệ $AX = b$ gọi là thuần nhất nếu tất cả các hệ số tự do

$$b_1 = b_2 = \cdots = b_m = 0$$

• Hệ thuần nhất luôn có nghiệm tầm thường.

$$x_1 = x_2 = \cdots = x_n = 0$$

• Hệ thuần nhất có nghiệm duy nhất khi và chỉ khi

$$r(A) = n = \text{số ẩn}$$

• Cho A là ma trận vuông. Hệ thuần nhất $AX = 0$ có nghiệm không tầm thường (nghiệm khác 0) khi và chỉ khi

$$|A| \neq 0 $$

**Ví dụ** Giải hệ phương trình

$ \begin{cases}x_1 + x_2 - x_3 + 2x_4 = 0 \\
2x_1 + 3x_2 - 3x_3 + 3x_4 = 0 \\
3x_1 + 5x_2 - 5x_3 + 4x_4 = 0.\end{cases} $

**Bài làm**

$ \left[ \begin{array}{cccc|c} 1 & 1 & -1 & 2 & 0 \\ 2 & 3 & -3 & 3 & 0 \\ 3 & 5 & -5 & 4 & 0 \end{array} \right]
\longrightarrow \left[ \begin{array}{cccc|c}  1 & 1 & -1 & 2 & 0 \\ 0 & 1 & -1 & -1 & 0 \\ 0 & 2 & -2 & -2 & 0 \end{array} \right] \longrightarrow \left[ \begin{array}{cccc|c} \boxed{1} & 1 & -1 & 2 & 0 \\ 0 & \boxed{1} & -1 & -1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right] $

Đặt các ẩn tự do làm tham số $x_3 = \alpha, x_4 = \beta$.

Pt(2): $x_2 = x_3 + x_4 = \alpha+ \beta \qquad$ Pt(1):$ x_1 = -x_2 + x_3 - 2x_4 = -3\beta$

Vậy nghiệm của hệ là $(x_1, x_2, x_3, x_4) = (-3\beta, \alpha + \beta, \alpha, \beta)$

**Ví dụ** Tìm m để hệ có nghiệm không tầm thường

$ \begin{cases}mx_1 + x_2 + x_3 + x_4 = 0 \\
x_1 + mx_2 + x_3 + x_4 = 0 \\
x_1 + x_2 + mx_3 + x_4 = 0 \\
x_1 + x_2 + x_3 + mx_4 = 0\end{cases} $

**Bài làm**

Hệ có nghiệm không tầm thường khi và chỉ khi $r(A) < n \Longleftrightarrow  |A| = 0$

$ |A| = \begin{vmatrix} m & 1 & 1 & 1 \\ 1 & m & 1 & 1 \\ 1 & 1 & m & 1 \\ 1 & 1 & 1 & m \end{vmatrix} = (m+3) \begin{vmatrix} 1 & 1 & 1 & 1 \\ 1 & m & 1 & 1 \\ 1 & 1 & m & 1 \\ 1 & 1 & 1 & m \end{vmatrix} = (m+3) \begin{vmatrix} 1 & 1 & 1 & 1 \\ 0 & m-1 & 0 & 0 \\ 0 & 0 & m-1 & 0 \\ 0 & 0 & 0 & m-1 \end{vmatrix} = (m+3)(m-1)^3 $

Vậy $m = -3 \vee m = 1$



**Ví dụ** Tìm m để hệ có vô số nghiệm

$ \begin{cases}x_1 + x_2 + 2x_3 - x_4 = 0 \\
x_1 + 3x_2 + mx_3 + 2x_4 = 0 \\
mx_1 - x_2 + 3x_3 - 2x_4 = 0\end{cases} $

**Bài làm**

Vì A là ma trận cở 3 $\times$ 4 nên $r(A) \leq 3 < 4$ = số ẩn. Vậy hệ luôn có vô số nghiệm.

Chú ý: Hệ thuần nhất có số phương trình ít hơn số ẩn thì vô số nghiệm.

# Chương 4 Không gian véc tơ

## 4.1 Định nghĩa và ví dụ

### Định nghĩa (Không gian véc tơ): 
Cho V là tập hợp khác rỗng và 2 phép toán: cộng 2 véc tơ và nhân véc tơ với một số thỏa mãn 8 tiên đề sau

i) $x+y=y+x$

ii) $(x + y) + z = x + (y + z)$

iii) $\exists 0 \in V : x + 0 = x$

iv) $\forall x \in V, \exists (-x) \in V : x + (-x) = 0 $

v) $\alpha, \beta \in K : (\alpha + \beta)x = \alpha x + \beta x$

vi) $\alpha \in K : \alpha(x+y) = \alpha x + \alpha y$

vii) $(\alpha \beta)x = \alpha(\beta x)$

viii) $1.x = x$

Khi đó, ta nói V là một không gian véc tơ.

**Chú ý**:

Đây là khái niệm được mở rộng từ khái niệm véc tơ ở phổ thông.

Tập các véc tơ trong mặt phẳng (hoặc không gian) có gốc O là một không gian véc tơ.

### Tính chất

i) Véc tơ không là duy nhất. 

ii) Véc tơ đối $(-x)$ của $x$ là duy nhất.

iii) $0.\vec{x} = \vec{0}, \forall x \in V $

iv) $\alpha.\vec{0} = \vec{0}, \forall \alpha \in K $

v) $-x = -1.x, \forall x \in V$

**Ví dụ**

1. Tập $V_1 = \{(x_1, x_2, x_3)|x_i \in R; i = 1, 2, 3\}$ với phép toán cộng 2 véc tơ và nhân véc tơ với số thực thông thường là một không gian véc tơ trên R. Ký hiệu là $R^3$.

Tương tự, ta có không gian $R^2$, $R^3$, $R^4$, $\ldots$, $R^n$, $\ldots$

2. Tập $V_2 = \{ax^2 + bx + c | a, b, c \in R\}$ với phép toán thông thường đối với đa thức là một không gian véc tơ. Ký hiệu là $P_2[x]$.

Tương tự, ta có không gian $P_3[x]$, $P_4[x]$, $\ldots$, $P_n[x]$, $\ldots$

3. Tập $V_3 = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} | a, b, c, d \in R \right\}$ với phép toán thông thường đối với ma trận là một không gian véc tơ. Ký hiệu là $M_2[R]$.

Tương tự, ta có các không gian $M_{m \times n}[R]$, $M_{m \times n}[R]$ các ma trận cỡ m $\times$ n trong thực và phức.

4. Tập $V_4 = \{(x_1$, $x_2$, $x_3)|x_i \in$ R $\wedge x_1$ + $2x_2$ - $3x_3 = 0\}$ với phép toán đối với véc tơ thông thường là một không gian véc tơ.

Chú ý: Có nhiều cách định nghĩa phép toán để cho các tập hợp trên là một không gian véc tơ, miễn là thỏa 8 tiên đề của không gian trên.


## 4.2 Độc lập tuyến tính - phụ thuộc tuyến tính

### Định nghĩa 
Trong không gian véc tơ V, cho tập hợp con gồm m véc tơ $M = \{x_1, x_2, \ldots, x_m\}$

$\bullet$ Véc tơ $x$ gọi là tổ hợp tuyến tính của $M$ nếu $\exists \alpha_1, \alpha_2, \ldots, \alpha_m \in K$ thỏa

$x = \alpha_1 x_1 + \alpha_2 x_2 + \cdots +\alpha_m x_m$

$\bullet \exists \alpha_1$, $\alpha_2$, $\ldots$, $\alpha_m$ không đồng thời bằng 0 thỏa

$\alpha_1 x_1$ + $\alpha_2 x_2$ + $\cdots$ + $\alpha_m x_m =$ 0 $\Longrightarrow$ M phụ thuộc tuyến tính.

$\bullet$ M gọi là độc lập tuyến tính nếu nó không PTTT. Tức là

$\alpha_1 x_1 + \alpha_2 x_2 + \cdots + \alpha_m x_m = 0 \longrightarrow \alpha_1 = \alpha_2 = \cdots = \alpha_m = 0$

Nói cách khác:

M PTTT nếu có một THTT không tầm thường bằng không.

M ĐLTT nếu nó chỉ có duy nhất một THTT bằng không là tổ hợp tầm thường $(\alpha_k = 0, \forall k)$

**Ví dụ** Trong $R^3$, cho họ véc tơ $M = \{(1, 1, 1), (2, 1, 3), (1, 2, 0)\}$

a) Véc tơ $x = (2, -1, 3)$ có là tổ hợp tuyến tính của M hay không?

b) M DLTT hay PTTT?

**Bài làm**

a) Xét $x = \alpha(1; 1; 1) + \beta(2; 1; 3) + \gamma(1; 2; 0) \Longleftrightarrow (2; -1; 3) = (\alpha + 2\beta + \gamma; \alpha + \beta + 2\gamma; \alpha + 3\beta)$

$ \Leftrightarrow \begin{cases} \alpha + 2\beta + \gamma = 2 \\ \alpha + \beta + 2\gamma = -1 \\ \alpha + 3\beta = 3 \end{cases}, (A|b) = \left[\begin{array}{ccc|c} 1 & 2 & 1 & 2\\ 1 & 1 & 2 & -1\\ 1 & 3 & 0 & 3\end{array} \right] \Longrightarrow r(A) = 2 < r(A|b) = 3 $

Hệ vô nghiệm, tức là không tồn tại $\alpha\beta$, $\gamma$. Vậy $x$ không là THTT của M.



b) Xét tổ hợp bằng 0

$\alpha(1;1;1) + \beta(2;1;3) + \gamma(1;2;0) = 0 \Longleftrightarrow (\alpha + 2\beta + \gamma; \alpha + \beta + 2\gamma; \alpha + 3\beta) = 0$

$ \iff \begin{cases} \alpha+2\beta+\gamma=0\\ \alpha+\beta+2\gamma=0\\ \alpha+3\beta=0 \end{cases}, A=\begin{pmatrix} 1 & 2 & 1\\ 1 & 1 & 2\\ 1 & 3 & 0 \end{pmatrix} \Longrightarrow |A|=0 $

Hệ vô số nghiệm nên tồn tại nghiệm không tầm thường, do đó $M$ PTTT.

### Các trường hợp

Cho tập $M = \{x_1, x_2, \ldots, x_m\}$ và véc tơ x

$\alpha_1 x_1 + \alpha_2 x_2 + \cdots + \alpha_m x_m = 0 \Longleftrightarrow AX = 0$

Hệ có nghiệm duy nhất $X = 0 \implies M$ ĐLTT.

Hệ có nghiệm khác không $\Rightarrow M$  PTTT.

$\alpha_1 x_1 + \alpha_2 x_2 + \cdots + \alpha_m x_m = x \Longleftrightarrow AX = b$

Hệ có nghiệm $\Rightarrow$ x là THTT của M.

Hệ vô nghiệm $\Rightarrow$ x không là THTT của M.

**Ví dụ** Trong không gian véc tơ V, cho họ $M = \{x, y, 2x + 3y,z\}$.

a) Véc tơ $2x + 3y$ có là THTT của $x, y, z$ hay không?

b) M ĐLTT hay PTTT?

**Bài làm**

a) Chọn $\alpha = 2, \beta = 3, \gamma = 0: 2x + 3y = 2.x + 3.y + 0.z \implies 2x + 3y$ là THTT của x, y, z.

b) Chọn $\alpha_1 = 2, \alpha_2 = 3 \alpha_3 = -1, \alpha_4 = 0: 2 \cdot x + 3 \cdot y - 1. (2x + 3y) + 0 \cdot z = 0 \implies$ M PTTT.

### Dấu hiệu ĐLTT-PTTT

$\bullet$ Nếu họ M chứa véc tơ không thì PTTT.

$\bullet$ Trong họ M, có một véc tơ là THTT của các véc tơ còn lại thì M PTTT.

$\bullet$ Thêm một số véc tơ vào họ PTTT, ta thu được 1 họ PTTT.

$\bullet$ Bốt đi một số véc tơ của họ DLTT, ta thu được 1 họ DLTT.

### Bổ đề cơ bản
Cho họ véc tơ gồm $m$ véc tơ $M = {x_1, x_2, \ldots, x_m}$.

Cho họ véc tơ gồm $n$ véc tơ $N = {y_1, y_2, \ldots, y_n}$.

Nếu mỗi véc tơ $y_k$ của $N$ là THTT của $M$ và $n > m$ thì $N$ PTTT.

**Ví dụ** 4.7
Trong không gian véc tơ $V$, tập $N =\{2x + y,\ x + y,\ 3x - 2y\}$ ĐLTT hay PTTT?

Các véc tơ của $N$ là THTT của $M = \{x,\ y\}$ và số véc tơ của $N$ lớn hơn số véc tơ của $M$ nên $N$ PTTT.

**Ví dụ** 4.8
Trong không gian véc tơ $V$, cho:

$M = \{x,\ y,\ z\}$

$N = \{x + y + z,\ 2x + 3y - z,\ 3x + 4y + z\}$

Chứng minh rằng:

a) Nếu $M$ ĐLTT thì $N$ ĐLTT.

b) Nếu $N$ ĐLTT thì $M$ ĐLTT.

**Bài làm**

a) Xét tổ hợp tuyến tính bằng 0 của $N$:

$
\alpha(x + y + z) + \beta(2x + 3y - z) + \gamma(3x + 4y + z) = 0
\Leftrightarrow (\alpha + 2\beta + 3\gamma)x + (\alpha + 3\beta + 4\gamma)y + (\alpha - \beta + \gamma)z = 0
\xrightarrow{M \ \text{ĐLTT}} 
\begin{cases}
\alpha + 2\beta + 3\gamma = 0 \\
\alpha + 3\beta + 4\gamma = 0 \\
\alpha - \beta + \gamma = 0
\end{cases}
\Rightarrow
\begin{cases}
\alpha = 0 \\
\beta = 0 \\
\gamma = 0
\end{cases}
\Rightarrow N \text{ ĐLTT}.
$

b) Dùng phản chứng: giả sử $M$ PTTT. Khi đó có một véc tơ là THTT của các véc tơ còn lại.

Không mất tính tổng quát, giả sử $z$ là THTT của $x,\ y$.

Ta có các véc tơ của $N$ là THTT của $M$ và cũng là THTT của $\{x,\ y\}$.

Số véc tơ của $N$ lớn hơn số véc tơ của $\{x,\ y\}$. Theo bổ đề cơ bản, $N$ PTTT — mâu thuẫn với giả thiết.

## 4.3 Hạng của họ véc tơ
### Định nghĩa 4.3
Cho họ véc tơ $M = {x_1, x_2, \ldots, x_m, \ldots} \subset V$.

Ta nói hạng của $M$ là $k_0$ nếu tồn tại $k_0$ véc tơ độc lập tuyến tính của $M$ và mọi tập con gồm hơn $k_0$ véc tơ của $M$ luôn phụ thuộc tuyến tính.

Hạng của họ $M$ là số tối đại các véc tơ độc lập tuyến tính của $M$.

**Ví dụ** 4.9
Trong không gian véc tơ $V$, cho $M = \{x, y\}$ độc lập tuyến tính. Tìm hạng của các họ véc tơ sau:

a) $M_1 = \{2x, 3y\}$

b) $M_2 = \{x, y, 2x + 3y\}$

c) $M_3 = \{x, y, 2x + 3y, 0\}$

**Bài làm**

a) Kiểm tra $\{2x, 3y\}$ độc lập tuyến tính. Do đó $r(M_1) = 2$.

b) $2x + 3y = 2 \cdot x + 3 \cdot y \Rightarrow M_2$ phụ thuộc tuyến tính và $\{x, y\}$ độc lập tuyến tính $\Rightarrow r(M_2) = 2$.

c) $M_3$ chứa véc tơ $0$ nên phụ thuộc tuyến tính. Dễ thấy 4 họ con gồm 3 véc tơ của $M_3$ đều phụ thuộc tuyến tính. Có 1 họ 2 véc tơ độc lập tuyến tính là $\{x, y\}$. Vậy $r(M_3) = 2$.

### Tính chất hạng của họ véc tơ

i) Hạng của họ véc tơ $M$ không đổi nếu ta nhân một véc tơ của $M$ với một số khác không.

ii) Cộng vào một véc tơ của họ $M$ một véc tơ khác đã được nhân với một số thì hạng không thay đổi.

iii) Thêm vào họ $M$ véc tơ $x$ là tổ hợp tuyến tính của $M$ thì hạng không thay đổi.

iv) Bớt đi một véc tơ của $M$ là tổ hợp tuyến tính của các véc tơ khác thì hạng không thay đổi.

**Ví dụ** 4.10
Cho họ véc tơ $M = \{(1; 1; 1; 0), (1; 2; 1; 1), (2; 3; 2; 1), (1; 3; 1; 2)\}$.

**Bài làm**

Ta có:
$(2; 3; 2; 1) = (1; 1; 1; 0) + (1; 2; 1; 1)$
$(1; 3; 1; 2) = -(1; 1; 1; 0) + 2(1; 2; 1; 1)$

$\Rightarrow r(M) = \{(1; 1; 1; 0), (1; 2; 1; 1)\}$

Hơn nữa, vì $\{(1; 1; 1; 0), (1; 2; 1; 1)\}$ độc lập tuyến tính nên $r(M) = 2$.

### Định lý về hạng
Cho $A$ là ma trận cỡ $m \times n$ trên $K$:
• $r(A)$ bằng với hạng của họ véc tơ hàng.
• $r(A)$ bằng với hạng của họ véc tơ cột.

**Ví dụ 4.11**
Tìm hạng của hai họ véc tơ:

a) $M = \{(1; 2; 1), (2; -1; 7), (1; 3; 0), (1; 2; 1)\}$ và $N = \{(1; 2; 1), (2; -1; 3), (1; 7; 0)\}$

b) $P = \{(1; 1; 1; 0), (1; 1; -1; 1), (2; 3; 1; 1), (3; 4; 0; 2)\}$

**Bài làm**

a) Xét $A = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & -1 & 3 & 2 \\ 1 & 2 & 0 & 1 \end{pmatrix}$ có họ véc tơ cột là $M$ và họ véc tơ hàng là $N$.
Do đó $r(M) = r(N) = r(A) = 2$.

b) Hạng của $P$ bằng hạng của ma trận
$B = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 1 \\ 2 & 3 & 1 & 1 \\ 3 & 4 & 0 & 2 \end{pmatrix}$.
Vì $r(B) = 2$ nên $r(P) = 2$.

### Tính chất cho họ véc tơ $M$ và véc tơ $x$:

• Hạng $M$ bằng số véc tơ thì $M$ độc lập tuyến tính.

• Hạng $M$ bé hơn số véc tơ thì $M$ phụ thuộc tuyến tính.

• $r(M, x) = r(M)$ thì $x$ là tổ hợp tuyến tính của $M$.

**Ví dụ 4.12**
Xét sự độc lập tuyến tính của các họ véc tơ sau:

a) $M = \{(1; 1; 1), (2; 1; 3), (1; 2; 0)\}$

b) $N =\{x^2 + x + 1, 2x^2 + 3x + 2, 2x + 1\}$

c) $P = \left\{ \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}, \begin{pmatrix} 3 & 4 \\ 0 & 1 \end{pmatrix}, \begin{pmatrix} 1 & 3 \\ -1 & 2 \end{pmatrix} \right\} $

d) $Q = {(1, 1, 0), (1, 2, 1), (m, 0, 1)}$

**Bài làm**

a) $r(M) = r\begin{pmatrix} 1 & 1 & 1 \\ 2 & 1 & 3 \\ 1 & 2 & 0 \end{pmatrix} = 2 \Rightarrow M$ phụ thuộc tuyến tính.

b) $r(N) = r\begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & 2 \\ 0 & 2 & 1 \end{pmatrix} = 3 \Rightarrow N$ độc lập tuyến tính.

c) $r(P) = r\begin{pmatrix} 1 & 1 & 1 & 0 \\ 2 & 1 & 1 & -1 \\ 3 & 4 & 0 & 1 \end{pmatrix} = 4 \Rightarrow P$ độc lập tuyến tính.

d)
$r(Q) = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 2 & 1 \\ m & 0 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & -m & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & m + 1 \end{pmatrix}$

• Nếu $m = -1 \Rightarrow r(Q) = 2$ thì $Q$ phụ thuộc tuyến tính.

• Nếu $m \neq -1 \Rightarrow r(Q) = 3$ thì $Q$ độc lập tuyến tính.

## 4.4 Cơ sở và số chiều

### Tập sinh
Cho $M = \{x_1, x_2, \ldots, x_m, \ldots\} \subset V$.

$M$ gọi là tập sinh của $V$ nếu mọi véc tơ $x \in V$ đều là tổ hợp tuyến tính của $M$. Ta viết

$$V = \langle x_1, x_2, \ldots, x_m \rangle$$

Ta còn nói $M$ sinh ra $V$ hay $V$ được sinh bởi $M$.

**Ví dụ (4.13)**
Xét xem các tập sau có là tập sinh trong $\mathbb{R}^3$ hay không?

a) $M = \{(1;1;1),(1;2;1),(2;3;1)\}$.

**Bài làm**

Với mọi $x = (x_1,x_2,x_3)\in \mathbb{R}^3$, giả sử
$x = \alpha(1;1;1) + \beta(1;2;1) + \gamma(2;3;1)$
$\iff \begin{cases}  \alpha + \beta + 2\gamma = x_1  \\  \alpha + 2\beta + 3\gamma = x_2  \\  \alpha + \beta + \gamma = x_3  \end{cases},\; \det A = \det \begin{pmatrix}1&1&2\\1&2&3\\1&1&1\end{pmatrix} = -1 \neq 0.$
Do đó hệ Cramer có nghiệm với mọi $x\in\mathbb{R}^3$. Vậy $M$ là tập sinh của $\mathbb{R}^3$.

b) $M = \{(1;1;1),(1;2;3),(3;2;1)\}$.

**Bài làm**

Với mọi $x=(x_1,x_2,x_3)\in \mathbb{R}^3$, giả sử
$x=\alpha(1;1;1)+\beta(1;2;3)+\gamma(3;2;1)$
$\iff \begin{cases}  \alpha+\beta+3\gamma=x_1  \\  \alpha+2\beta+2\gamma=x_2  \\  \alpha+3\beta+\gamma=x_3  \end{cases}  \iff \left[\begin{array}{ccc|c}1&1&3&x_1\\1&2&2&x_2\\1&3&1&x_3\end{array}\right]\to\left[\begin{array}{ccc|c}1&1&3&x_1\\0&1&-1&x_2-x_1\\0&0&0&x_3+x_1-2x_2\end{array}\right].$

Nếu $x_3+x_1-2x_2\neq0$ thì hệ vô nghiệm, tức tồn tại $x$ không biểu diễn được. Vậy $M$ không là tập sinh của $\mathbb{R}^3$.

**Ví dụ (4.14)**
Tập $M=\{x^2+x+1;2x^2+3x+1;x^2+2x\}$ có là tập sinh của $P_2[x]$ hay không?

**Bài làm**
Với mọi $p(x)=ax^2+bx+c\in P_2[x]$, giả sử
$p(x)=\alpha(x^2+x+1)+\beta(2x^2+3x+1)+\gamma(x^2+2x)$
$\iff \begin{cases}  \alpha+2\beta+\gamma = a  \\  \alpha+3\beta+2\gamma = b  \\  \alpha+\beta = c  \end{cases}  \iff \left[\begin{array}{ccc|c}1&2&1&a\\1&3&2&b\\1&1&0&c\end{array}\right]\to\left[\begin{array}{ccc|c}1&2&1&a\\0&1&1&b-a\\0&0&0&b+c-2a\end{array}\right].$

Nếu $b+c-2a\neq0$ thì hệ vô nghiệm. Vậy $M$ không là tập sinh của $P_2[x]$.

**Ví dụ (4.15)**
Cho $M=\{x,y,z\}$ là tập sinh của không gian véc tơ $V$. Xét các tập sau:

a) $M_1=\{2x;x+y;z\}$.

**Bài làm**

Mỗi $v\in V$ viết được dưới dạng $v=\alpha x+\beta y+\gamma z$.
Ta có
$v=\tfrac{\alpha-\beta}{2}\cdot2x+\beta\cdot(x+y)+\gamma\cdot z,$
thể hiện $v$ là tổ hợp tuyến tính của $M_1$. Vậy $M_1$ là tập sinh của $V$.

b) $M_2=\{x;x+y;x-y\}$.

**Bài làm**

Nếu $z$ là tổ hợp tuyến tính của $x,y$ thì mọi véc tơ trong $V$ biểu diễn qua $x,y$ sẽ biểu diễn qua $M_2$, nên $M_2$ sinh $V$.

Nếu $z$ không là tổ hợp tuyến tính của $x,y$ thì $z$ không thể biểu diễn bởi $M_2$, nên $M_2$ không sinh $V$.

### Tính chất của cơ sở và số chiều

Cho $\dim(V)=n$.

• Mọi tập con có nhiều hơn $n$ véc tơ thì phụ thuộc tuyến tính.

• Mọi tập con có ít hơn $n$ véc tơ không sinh ra $V$.

• Mọi tập con độc lập tuyến tính gồm đúng $n$ véc tơ là cơ sở của $V$.

• Mọi tập sinh gồm đúng $n$ véc tơ là cơ sở của $V$.

• Mọi tập có hạng bằng $n$ là tập sinh của $V$.

### Cơ sở và số chiều
(M sinh ra V) + (M - ĐLTT) ⇒ (M - là cơ sở)

(Cơ sở có n véc tơ) ⇒ (Số chiều của V là n: dim(V) = n)

V không có tập sinh hữu hạn thì V gọi là KGVT vô hạn chiều.

**Ví dụ (4.16)**
Cho $M=\{x,y,z\}$ là cơ sở của $V$. Xét:

**a)** $M_1=\{2x+y+z;x+2y+z;x+y+z\}$.

**Bài làm**

Ta chứng minh $M_1$ là tập sinh và độc lập tuyến tính, nên $M_1$ là cơ sở của $V$.

**b)** $M_2=\{2x;3y;z;x+y+z\}$.

**Bài làm**

Rõ ràng $M_2$ sinh $V$ nhưng phụ thuộc tuyến tính (hơn $3$ véc tơ trong không gian 3 chiều). Do đó $M_2$ không phải cơ sở.

**Ví dụ (4.17)**
Kiểm tra tập sinh và cơ sở trong $\mathbb{R}^3$:

**a)** $M={(1;1;1),(2;3;1),(3;1;0)}$.

**Bài làm**

$M$ có 3 véc tơ và
$r(M)=r\begin{pmatrix}1&1&1\\2&3&1\\3&1&0\end{pmatrix}=3\;\Longrightarrow\;M\text{ là cơ sở của }\mathbb{R}^3.$

**b)** $N={(1;1;1),(2;0;1),(1;1;0),(1;-2;1)}$.

**Bài làm**

$N$ có 4 véc tơ trong không gian 3 chiều nên phụ thuộc.
$r(N)=r\begin{pmatrix}1&1&1\\2&0&1\\1&1&0\\1&0&1\end{pmatrix}=3\;\Longrightarrow\;N\text{ là tập sinh của }\mathbb{R}^3.$

**Ví dụ (4.18)**
Kiểm tra $M=\{x^2+x+1,2x^2+x+1,x^2+2x+2\}$ có là cơ sở của $P_2[x]$ không?

**Bài làm**

$M$ có 3 véc tơ bằng số chiều của $P_2[x]$.
$r(M)=r\begin{pmatrix}1&1&1\\2&1&1\\1&2&2\end{pmatrix}=2\;\Longrightarrow\;M\text{ không là cơ sở của }P_2[x].$

## 4.5 Tọa độ véc tơ

### Định nghĩa
Cho $E = \{e_1, e_2, \ldots, e_n\}$ là một cơ sở sắp thứ tự của K-KGVT V.

Với mỗi véc tơ $x \in V$, tồn tại duy nhất một bộ số $(x_1, x_2, \ldots, x_n)$ sao cho $x = x_1e_1 + x_2e_2 + \dots + x_ne_n$. Bộ số này gọi là **tọa độ** của véc tơ $x$ trong cơ sở $E$. Ký hiệu:

$ [x]_E = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} \Longleftrightarrow x = x_1e_1 + x_2e_2 + \dots + x_ne_n. $

**Ví dụ (4.19)**
Cho $E = \{x^2 + x + 1, x^2 + 2x + 1, x^2 + x + 2\}$ là một cơ sở của $P_2[x]$.

a) Tìm $p(x)$ biết $[p(x)]_E = \begin{pmatrix} 3 \\ -2 \\ 5 \end{pmatrix}$.

b) Cho $q(x) = x^2$. Tìm $[q(x)]_E$.

**Bài làm**

a) $[p(x)]_E = \begin{pmatrix} 3 \\ -2 \\ 5 \end{pmatrix} \Longleftrightarrow p(x) = 3(x^2 + x + 1) - 2(x^2 + 2x + 1) + 5(x^2 + x + 2) \Longleftrightarrow p(x) = (3 - 2 + 5)x^2 + (3 - 4 + 5)x + (3 - 2 + 10) \Longleftrightarrow p(x) = 6x^2 + 4x + 11$.

b) Giả sử $[q(x)]_E = \begin{pmatrix} \alpha \\ \beta \\ \gamma \end{pmatrix}$

$\iff q(x) = \alpha(x^2 + x + 1) + \beta(x^2 + 2x + 1) + \gamma(x^2 + x + 2)$

$\iff x^2 = (\alpha + \beta + \gamma)x^2 + (\alpha + 2\beta + \gamma)x + (\alpha + \beta + 2\gamma)$

$ \Leftrightarrow \begin{cases} \alpha+\beta+\gamma=1 \\ \alpha+2\beta+\gamma=0 \\ \alpha+\beta+2\gamma=0 \end{cases} \Leftrightarrow \begin{cases} \alpha=3 \\ \beta=-1 \\ \gamma=-1 \end{cases}. $
Vậy $[q(x)]_E = \begin{pmatrix} 3 \\ -1 \\ -1 \end{pmatrix}. $

### Tính chất tọa độ

Cho $E$ là cơ sở của KGVT $V$. Với $[x]_E = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}, [y]_E = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix}$

i) $ x = y \Longleftrightarrow [x]_E = [y]_E \Longleftrightarrow \begin{cases} x_1 = y_1 \\ x_2 = y_2 \\ \dots \\ x_n = y_n \end{cases} $

ii) $ [x + y]_E = [x]_E + [y]_E = \begin{pmatrix} x_1 + y_1 \\ x_2 + y_2 \\ \vdots \\ x_n + y_n \end{pmatrix} $

iii) $ [\alpha x]_E = \alpha [x]_E = \begin{pmatrix} \alpha x_1 \\ \alpha x_2 \\ \vdots \\ \alpha x_n \end{pmatrix} $

**Ví dụ**
Cho $E = \{(1, 1, 1), (1, 1, 0), (1, 0, 1)\}$ là cơ sở của $\mathbb{R}^3$.

a) Tìm $x$, biết $[x]_E = \begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix}$.

b) Cho $x = (3; 1; -2)$. Tìm $[x]_E$.

**Bài làm**

a) $[x]_E = \begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix} \Longleftrightarrow x = -1(1; 1; 1) + 2(1; 1; 0) + 1(1; 0; 1) = (2; 1; 0)$.

*Ghi chú:*

$ E \cdot [x]_E = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} \xrightarrow{\text{viết lại}} x = (2; 1; 0). $

b) Giả sử $[x]_E = \begin{pmatrix} \alpha \\ \beta \\ \gamma \end{pmatrix} \Longleftrightarrow x = \alpha(1; 1; 1) + \beta(1; 1; 0) + \gamma(1; 0; 1)$

$ \iff (3; 1; -2) = (\alpha+\beta+\gamma; \alpha+\beta; \alpha+\gamma) \iff \begin{cases} \alpha+\beta+\gamma=3 \\ \alpha+\beta=1 \\ \alpha+\gamma=-2 \end{cases} \iff [x]_E=\begin{pmatrix} -4 \\ 5 \\ 2 \end{pmatrix}. $

*Ghi chú:*

$ E \cdot [x]_E = x^T \Longleftrightarrow [x]_E = E^{-1}x^T = \begin{pmatrix} -4 \\ 5 \\ 2 \end{pmatrix}. $

### Dùng máy tính casio cho bài toán tọa độ

Cơ sở $E = \{e_1, e_2, \ldots, e_n\} \xrightarrow{\text{MT cột}} E = \begin{pmatrix} e_1 & e_2 & \ldots & e_n \end{pmatrix}$

$ \boxed{x^T = E \cdot [x]_E} \qquad \Longleftrightarrow \qquad \boxed{[x]_E = E^{-1} \cdot x^T} $

### Ý nghĩa của tọa độ
Cho $E = \{e_1, e_2, \ldots, e_n\}$ là cơ sở của KGVT $V$.

Mọi véc tơ của $V$ đều biểu diễn qua $E$ dưới dạng tọa độ.

Các phép toán tọa độ giống như các phép toán trong $\mathbb{R}^n$.

$\implies$ Tất cả các không gian véc tơ $n$ chiều đều coi là tương đương với $\mathbb{R}^n$.

**Ví dụ**
Tìm tọa độ của $p(x) = 3x^2 + 4x - 1$ trong cơ sở $E = \{x^2 + x + 1, x + 1, 2x + 1\}$ trong $P_2[x]$.

**Bài làm**

Trong cơ sở chính tắc $S = \{x^2, x, 1\}$, véc tơ $p(x)$ có tọa độ là $\begin{pmatrix} 3 \\ 4 \\ -1 \end{pmatrix}$.

Lập ma trận $E$ với các cột là tọa độ của các véc tơ trong cơ sở $E$ đối với cơ sở chính tắc $S$:
$ e_1 = x^2+x+1 \to \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}; \quad e_2 = x+1 \to \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}; \quad e_3 = 2x+1 \to \begin{pmatrix} 0 \\ 2 \\ 1 \end{pmatrix} $.

Vậy ma trận $E = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix}$.

Tọa độ $[p(x)]_E$ được tính bằng:
$ [p(x)]_E = E^{-1} \cdot [p(x)]_S = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix}^{-1} \cdot \begin{pmatrix} 3 \\ 4 \\ -1 \end{pmatrix} = \begin{pmatrix} 3 \\ -9 \\ 5 \end{pmatrix}. $


## 4.6 Ma trận chuyển cơ sở

### Định nghĩa 4.6
Cho hai cơ sở của KGVT V: $E = \{e_1, e_2, \dots, e_n\}$ và $E' = \{e'_1, e'_2, \dots, e'_n\}$.

Với mọi véc tơ $x \in V$, ta có thể biểu diễn $x$ qua hai cơ sở:

$x = x_1e_1 + x_2e_2 + \dots + x_ne_n = x'_1e'_1 + x'_2e'_2 + \dots + x'_ne'_n$. (1)

Mỗi véc tơ của cơ sở mới $E'$ có thể được biểu diễn dưới dạng tổ hợp tuyến tính các véc tơ của cơ sở cũ $E$:

$e'_1 = a_{11}e_1 + a_{21}e_2 + \dots + a_{n1}e_n$

$e'_2 = a_{12}e_1 + a_{22}e_2 + \dots + a_{n2}e_n$

$...$

$e'_n = a_{1n}e_1 + a_{2n}e_2 + \dots + a_{nn}e_n$

Thay các biểu thức này vào (1), ta có:
$x = x'_1(a_{11}e_1 + a_{21}e_2 + \dots + a_{n1}e_n) + x'_2(a_{12}e_1 + a_{22}e_2 + \dots + a_{n2}e_n) + \dots + x'_n(a_{1n}e_1 + a_{2n}e_2 + \dots + a_{nn}e_n)$.

Bằng cách đồng nhất hệ số của các véc tơ $e_i$ ở hai vế, ta suy ra:
$ \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix} \begin{pmatrix} x'_1 \\ x'_2 \\ \vdots \\ x'_n \end{pmatrix}. $


Ma trận $P = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{pmatrix}$ gọi là **ma trận chuyển cơ sở** từ $E$ sang $E'$.

### Ma trận chuyển cơ sở
Cột thứ $j$ của ma trận $P$ chính là véc tơ tọa độ của $e'_j$ trong cơ sở $E$, tức là $[e'_j]_E$.
$ P_{E \to E'} = \begin{pmatrix} | & | & & | \\ [e'_1]_E & [e'_2]_E & \cdots & [e'_n]_E \\ | & | & & | \end{pmatrix} $

Trong $\mathbb{R}^n$, nếu ta xem $E$ và $E'$ là các ma trận có các cột là các véc tơ cơ sở tương ứng, công thức tính ma trận chuyển cơ sở là:
$ P_{E \to E'} = E^{-1}E' $.

Công thức liên hệ giữa các tọa độ là:
$ [x]_E = P_{E \to E'} \cdot [x]_{E'} $.

### Tính chất

*   Ma trận chuyển cơ sở $P$ luôn khả nghịch.
*   Nếu $P$ là ma trận chuyển cơ sở từ $E$ sang $E'$ thì $P^{-1}$ là ma trận chuyển cơ sở từ $E'$ sang $E$.
*   Nếu $P$ là ma trận chuyển cơ sở từ $E$ sang $E'$ và $Q$ là ma trận chuyển cơ sở từ $E'$ sang $E''$ thì $PQ$ là ma trận chuyển cơ sở từ $E$ sang $E''$.

**Ví dụ**
Trong $\mathbb{R}^3$, cho hai cơ sở $E = \{(1,1,1), (1,0,1), (1,1,0)\}$ và $E' = \{(1,1,2), (1,2,1), (1,1,1)\}$.

a) Tìm ma trận chuyển cơ sở từ $E$ sang $E'$ và ma trận chuyển cơ sở từ $E'$ sang $E$.

b) Cho $x = (2, 1, 3)$. Tìm $[x]_E$ và $[x]_{E'}$.

**Bài làm**

a) Lập các ma trận cơ sở:
$ E = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}, E' = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 1 \\ 2 & 1 & 1 \end{pmatrix}. $

Ma trận chuyển cơ sở từ $E$ sang $E'$:
$ P = E^{-1}E' = \begin{pmatrix} -1 & 1 & 1 \\ 1 & -1 & 0 \\ 1 & 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 1 \\ 2 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 2 & 1 \\ 0 & -1 & 0 \\ -1 & 0 & 0 \end{pmatrix}. $

Ma trận chuyển cơ sở từ $E'$ sang $E$:
$ Q = P^{-1} = \begin{pmatrix} 0 & 0 & -1 \\ 0 & -1 & 0 \\ 1 & 2 & 2 \end{pmatrix}. $

b) Tọa độ của $x$ trong cơ sở $E'$:
$ [x]_{E'} = (E')^{-1}x^T = \begin{pmatrix} -1 & 0 & 1 \\ -1 & 1 & 0 \\ 3 & -1 & -1 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}. $

Tọa độ của $x$ trong cơ sở $E$:
$ [x]_E = E^{-1}x^T = \begin{pmatrix} -1 & 1 & 1 \\ 1 & -1 & 0 \\ 1 & 0 & -1 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}. $

*Cách khác:* Dùng ma trận chuyển cơ sở:
$ [x]_E = P \cdot [x]_{E'} = \begin{pmatrix} 2 & 2 & 1 \\ 0 & -1 & 0 \\ -1 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}. $

## 4.7 Không gian con

### Định nghĩa 4.6
Trong không gian vector V, nếu tập con F với các phép toán trong V lập thành một không gian vector thì ta nói F là không gian con của V.

### Định lý không gian con
Tập con khác rỗng F của không gian vector V là một không gian con của V khi và chỉ khi hai điều kiện sau thỏa:

i) $\forall x, y \in F : x + y \in F$.

ii) $\forall x \in F, \alpha \in K : \alpha x \in F$.

**Ví dụ 4.23** Cho $F = \{(x_1; x_2; x_3) \in R^3 | x_1 + 2x_2 - x_3 = 0 \}$.

a) Chứng tỏ F là không gian con của $R^3$.

b) Tìm cơ sở và số chiều của F.

**Bài làm**

a) Sinh viên tự kiểm tra 2 điều kiện trong định lý.

b) $\forall x = (x_1; x_2; x_3) \in F \Longleftrightarrow x_1 + 2x_2 - x_3 = 0 \Longleftrightarrow x_3 = x_1 + 2x_2$.

$x = (x_1; x_2; x_3) = (x_1; x_2; x_1 + 2x_2) = x_1(1; 0; 1) + x_2(0; 1; 2)$.

Suy ra $E = \{(1,0,1), (0,1,2)\}$ là tập sinh của F.

Kiểm tra E độc lập tuyến tính. Vậy E là cơ sở của F và $\dim(F) = 2$.

**Ví dụ 4.24** Cho $F = \{p(x) \in P_2[x] | p(1) = 0 \land p(2) = 0\}$.

a) Chứng tỏ F là không gian con của $P_2[x]$.

b) Tìm cơ sở và số chiều của F.

**Bài làm**

a) Sinh viên tự kiểm tra 2 điều kiện trong định lý.

b) $\forall p(x) = ax^2 + bx + c \in F \Longleftrightarrow p(1) = 0 \land p(2) = 0$

$ \iff \begin{cases} a+b+c=0 \\ 4a+2b+c=0 \end{cases} \iff \begin{cases} a=\alpha \\ b=-3\alpha \\ c=2\alpha \end{cases} $

$p(x) = \alpha x^2 - 3\alpha x + 2\alpha = \alpha(x^2 - 3x + 2)$.

Suy ra $E = \{x^2 - 3x + 2\}$ là tập sinh của F.

Hiển nhiên E độc lập tuyến tính. Vậy E là cơ sở của F và $\dim(F) = 1$.

**Ví dụ 4.25** Cho $F = \left\{ A \in M_2[R] | A \begin{pmatrix} 1 & -1 \\ 2 & -2 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} \right\}.$

a) Chứng tỏ F là không gian con của $M_2[R]$.

b) Tìm cơ sở và số chiều của F.

**Bài làm**

a) Sinh viên tự kiểm tra 2 điều kiện trong định lý.

b) $\forall A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in F \Longleftrightarrow \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 2 & -2 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} \Longleftrightarrow \begin{pmatrix} a+2b & -a-2b \\ c+2d & -c-2d \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$

$ \iff \begin{cases} a+2b=0 \\ c+2d=0 \end{cases} \iff \begin{cases} a=-2b \\ c=-2d \end{cases} $

$ A = \begin{pmatrix} -2b & b \\ -2d & d \end{pmatrix} = b \begin{pmatrix} -2 & 1 \\ 0 & 0 \end{pmatrix} + d \begin{pmatrix} 0 & 0 \\ -2 & 1 \end{pmatrix}. $

Suy ra $E = \left\{ \begin{pmatrix} -2 & 1 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ -2 & 1 \end{pmatrix} \right\}$ là tập sinh của F.

Dễ thấy E độc lập tuyến tính. Vậy E là cơ sở của F và $\dim(F) = 2$.

### Định lý
Cho $M = \{v_1, v_2, \ldots, v_p\} \subset V$.

Ký hiệu $H := \text{Span}(M) = \{\alpha_1v_1 + \alpha_2v_2 + \cdots + \alpha_pv_p | \forall \alpha_i \in R\}$.

• H là một không gian con được sinh bởi M: $H = \langle M \rangle$.

• $\dim(H) = \text{r}(M)$.

• $x \in H \Longleftrightarrow x$ là tổ hợp tuyến tính của $M \Longleftrightarrow \text{r}(M, x) = \text{r}(M)$.

**Ví dụ 4.26** Tìm cơ sở và số chiều của các không gian con sau

a) $F = \langle (1;1;1), (2;1;1), (3;1;1) \rangle$.

b) $F = \langle x^2 + x + 1, 2x^2 + 3x - 1, x^2 + 2x - 2 \rangle$.

c) $F = \left\langle \begin{pmatrix} 1 & 1 \\ 2 & 1 \end{pmatrix}, \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}, \begin{pmatrix} 3 & 1 \\ -2 & 1 \end{pmatrix}, \begin{pmatrix} 1 & 0 \\ -2 & 0 \end{pmatrix} \right\rangle$

d) $F = \{(x_1; x_2; x_3; x_4) \in R^4 | x_1 + x_2 + x_3 = 0 \land x_1 - x_2 + x_4 = 0 \}$

**Bài làm**

a) $A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 1 & 1 \\ 3 & 1 & 1 \end{pmatrix} \xrightarrow{bdsc} \begin{pmatrix} 1 & 1 & 1 \\ 0 & -1 & -1 \\ 0 & 0 & 0 \end{pmatrix} \Longrightarrow \dim(F) = r(A) = 2$ và cơ sở của F là $\{(1; 1; 1), (0; -1; -1)\}$.

b) $A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & -1 \\ 1 & 2 & -2 \end{pmatrix} \xrightarrow{bdsc} \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & -3 \\ 0 & 0 & 0 \end{pmatrix} \implies \dim(F) = r(A) = 2$ và cơ sở của F là $\{x^2 + x + 1, x - 3\}$.

c) $A = \begin{pmatrix} 1 & 1 & 2 & 1 \\ 2 & 1 & 0 & 1 \\ 3 & 1 & -2 & 1 \\ 1 & 0 & -2 & 0 \end{pmatrix} \xrightarrow{bdsc} \begin{pmatrix} 1 & 1 & 2 & 1 \\ 0 & -1 & -4 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \implies \dim(F) = 2 \text{ và cơ sở của } F \text{ là } \left\{ \begin{pmatrix} 1 & 1 \\ 2 & 1 \end{pmatrix}, \begin{pmatrix} 0 & -1 \\ -4 & -1 \end{pmatrix} \right\}.$

d) Giải hệ $\begin{cases} x_1 + x_2 + x_3 = 0 \\ x_1 - x_2 + x_4 = 0 \end{cases} \Longleftrightarrow \begin{bmatrix} 1 & 1 & 1 & 0 \\ 1 & -1 & 0 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \xrightarrow{bdsc} \begin{bmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

Đặt $x_3 = 2\alpha$, $x_4 = 2\beta$.

Từ pt(2): $-2x_2 -x_3 + x_4 = 0 \implies x_2 = \frac{1}{2}(-x_3 + x_4) = -\alpha + \beta$.

Từ pt(1): $x_1 = -x_2 - x_3 = -(-\alpha + \beta) - 2\alpha = -\alpha - \beta$.

$\forall x \in F \Longleftrightarrow x = (-\alpha - \beta; -\alpha + \beta; 2\alpha; 2\beta) = \alpha(-1; -1; 2; 0) + \beta(-1; 1; 0; 2)$.

Suy ra $E = \{(-1, -1, 2, 0), (-1, 1, 0, 2)\}$ là tập sinh của F.

Dễ thấy E độc lập tuyến tính. Vậy E là cơ sở của F và $\dim(F) = 2$.

### Tìm cơ sở và số chiều không gian con
Trong $R^n$, cho không gian con F:

**TH 1)** Cho F được cho bởi tập sinh $F = \langle v_1, v_2, \ldots, v_m \rangle:$

Lập ma trận có các vector $v_i$ là hàng $A = \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_m \end{pmatrix} \xrightarrow{bdsc} \text{ ma trận bậc thang}$

$\dim(F) = r(A)$ và cơ sở gồm các hàng khác không của ma trận bậc thang.

**TH 2)** Cho F là tập nghiệm của hệ phương trình tuyến tính thuần nhất $AX = 0$:

Giải hệ. Số chiều của không gian nghiệm là $\dim(F) = n - r(A)$ (với n là số ẩn) và cơ sở được suy ra từ nghiệm tổng quát của hệ.

**Ví dụ 4.27** Trong $R^3$, cho tập $M = \{(1, 1, 1), (2, 3, 1), (1, 0, 2)\}$.

a) $x = (1, -2, 3)$ thuộc không gian con span(M) hay không?

b) Tìm m để $x = (1, 0, m) \in \text{span}(M)$.

**Bài làm**

a) x thuộc không gian con span(M) khi và chỉ khi x là tổ hợp tuyến tính của các vector trong M. Ta lập ma trận cột:

$ [M|x] = \left[ \begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 1 & 3 & 0 & -2 \\ 1 & 1 & 2 & 3 \end{array} \right] \xrightarrow{bdsc} \left[ \begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 0 & 1 & -1 & -3 \\ 0 & 0 & 0 & -1 \end{array} \right] $

$r(M) = 2 < r([M|x]) = 3 \Longrightarrow x \notin \text{span}(M)$.

b) $ [M|x] = \left[ \begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 1 & 3 & 0 & 0 \\ 1 & 1 & 2 & m \end{array} \right] \xrightarrow{bdsc} \left[ \begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 0 & 1 & -1 & -1 \\ 0 & 0 & 0 & m-2 \end{array} \right] $

$x \in \text{span}(M) \Longleftrightarrow r(M) = r([M|x]) \Longleftrightarrow m-2 = 0 \Longleftrightarrow m = 2$.

## 4.8 Tổng và giao hai không gian con

### Định nghĩa 4.7 (Tổng và giao 2 không gian con)
Cho hai không gian con F và G của không gian vector V.

**Giao 2 không gian con**

$F \cap G = \{x \in V | x \in F \text{ và } x \in G\}$.

**Tổng 2 không gian con**

$F + G = \{f + g | f \in F \text{ và } g \in G\}$.

### Tính chất

$F \cap G \subset F, G \subset F + G \subset V$.

### Định lý
$F \cap G$ và $F + G$ là 2 không gian con của V và

$\dim(F \cap G) + \dim(F + G) = \dim(F) + \dim(G)$.

### Định nghĩa 4.8 (Tổng trực tiếp)
Không gian con W gọi là tổng trực tiếp của 2 không gian con F và G, ký hiệu $W = F \oplus G$, nếu:

i) $W = F + G$.

ii) $F \cap G = \{0\}$.

### Định lý
Cho $W = F \oplus G$. Khi đó mọi vector $x \in W$ được biểu diễn duy nhất dưới dạng $x = f + g$ với $f \in F, g \in G$.

### Tính chất tổng 2 không gian con
Nếu $F = \langle f_1, f_2, \ldots, f_n \rangle$ và $G = \langle g_1, g_2, \ldots, g_m \rangle$

$\implies F + G = \langle f_1, f_2, \ldots, f_n, g_1, g_2, \ldots, g_m \rangle$.

**Ví dụ 4.28** Trong $R^3$, cho 2 không gian con

$F = \{(x_1, x_2, x_3) \in R^3 | x_1 + x_2 - 2x_3 = 0\}$, $\quad G = \{(x_1, x_2, x_3) \in R^3 | x_1 - x_2 + x_3 = 0\}$.

Tìm cơ sở và số chiều của $F \cap G$ và $F + G$.

**Bài làm**

a) Tìm cơ sở và số chiều của $F \cap G$.

$\forall x \in F \cap G \longleftrightarrow x \in F \land x \in G$

$ \Leftrightarrow \begin{cases} x_1 + x_2 - 2x_3 = 0 \\ x_1 - x_2 + x_3 = 0 \end{cases} \Leftrightarrow \begin{cases} x_1 = \frac{1}{2}x_3 \\ x_2 = \frac{3}{2}x_3 \end{cases} $. Chọn $x_3=2\alpha \Rightarrow x_1=\alpha, x_2=3\alpha$.

$\Leftrightarrow x = (\alpha, 3\alpha, 2\alpha) = \alpha(1, 3, 2). $

Suy ra $E = \{(1,3,2)\}$ là tập sinh của $F \cap G$.

Hiển nhiên E độc lập tuyến tính do đó E là cơ sở của $F \cap G$ và $\dim(F \cap G) = 1$.

b) Tìm cơ sở và số chiều của $F+G$.

Tìm tập sinh của F và G:
*   Với F: $x_1 = -x_2 + 2x_3$, $x = (-x_2+2x_3, x_2, x_3) = x_2(-1,1,0) + x_3(2,0,1)$. Vậy $F = \langle (-1,1,0), (2,0,1) \rangle$, $\dim(F)=2$.
*   Với G: $x_1 = x_2 - x_3$, $x = (x_2-x_3, x_2, x_3) = x_2(1,1,0) + x_3(-1,0,1)$. Vậy $G = \langle (1,1,0), (-1,0,1) \rangle$, $\dim(G)=2$.

$F + G = \langle (-1,1,0), (2,0,1), (1,1,0), (-1,0,1) \rangle$.

$ A = \begin{pmatrix} -1 & 1 & 0 \\ 2 & 0 & 1 \\ 1 & 1 & 0 \\ -1 & 0 & 1 \end{pmatrix} \xrightarrow{bdsc} \begin{pmatrix} -1 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & -1 \\ 0 & 0 & 0 \end{pmatrix}. $

$\implies \dim(F + G) = r(A) = 3$ và cơ sở là $E' = \{(-1, 1, 0), (0, 2, 1), (0, 0, -1)\}$.

**Cách khác:** ta có
$\dim(F + G) = \dim(F) + \dim(G) - \dim(F \cap G) = 2+2-1 = 3$.

Vì $F+G$ là không gian con 3 chiều của $R^3$ nên $F + G = R^3$. Do đó, có thể chọn cơ sở là cơ sở chính tắc của $R^3$: $\{(1,0,0), (0,1,0), (0,0,1)\}$.

**Ví dụ 4.29** Trong $R^3$, cho 2 không gian con $F = \{(x_1, x_2, x_3) \in R^3 | x_1 + x_2 + x_3 = 0\}$, $G = \langle (1, 0, 1), (2, 3, 1) \rangle$.

Tìm cơ sở và số chiều của $F \cap G$ và $F + G$.

**Bài làm**

Việc tìm F+G tương tự như ví dụ trên. Ta tìm cơ sở và số chiều của $F \cap G$.

$\forall x \in F \cap G \Longleftrightarrow x \in F \land x \in G$.

$x \in G \Longleftrightarrow x = \alpha(1, 0, 1) + \beta(2, 3, 1) = (\alpha + 2\beta, 3\beta, \alpha + \beta)$.

$x \in F \Longleftrightarrow x$ thỏa điều kiện của F: $(\alpha + 2\beta) + (3\beta) + (\alpha + \beta) = 0 \Longleftrightarrow 2\alpha + 6\beta = 0 \Longleftrightarrow \alpha = -3\beta$.

Thay vào biểu thức của x:
$x = (-3\beta + 2\beta, 3\beta, -3\beta + \beta) = (-\beta, 3\beta, -2\beta) = \beta(-1, 3, -2)$.

Dễ dàng suy ra $E = \{(-1, 3, -2)\}$ là cơ sở của $F \cap G$ và $\dim(F \cap G) = 1$.

**Ví dụ 4.30** Trong $R^3$, cho 2 không gian con

$F = \langle f_1 = (1,0,1), f_2 = (1,1,1) \rangle$, $G = \langle g_1 = (1,1,0), g_2 = (2,1,1) \rangle$.

Tìm cơ sở và số chiều của $F+G$ và $F\cap G$.

**Bài làm**
Việc tìm F+G làm tương tự ví dụ trên. Ta tìm cơ sở và số chiều của $F \cap G$.

$x \in F \cap G$ khi và chỉ khi x đồng thời là tổ hợp tuyến tính của $\{f_1, f_2\}$ và $\{g_1, g_2\}$:
$x = x_1 f_1 + x_2 f_2 = x_3 g_1 + x_4 g_2 \Leftrightarrow x_1 f_1 + x_2 f_2 - x_3 g_1 - x_4 g_2 = 0$.

Viết lại ở dạng hệ phương trình theo tọa độ:
$x_1\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} + x_2\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} - x_3\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} - x_4\begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$

$ \Leftrightarrow \begin{cases} x_1+x_2-x_3-2x_4=0 \\ x_2-x_3-x_4=0 \\ x_1+x_2-x_4=0 \end{cases} $

Viết lại ở dạng ma trận và giải:
$ \left[ \begin{array}{cccc|c} 1 & 1 & -1 & -2 & 0 \\ 0 & 1 & -1 & -1 & 0 \\ 1 & 1 & 0 & -1 & 0 \end{array} \right] \xrightarrow{bdsc} \left[ \begin{array}{cccc|c} 1 & 1 & -1 & -2 & 0 \\ 0 & 1 & -1 & -1 & 0 \\ 0 & 0 & 1 & 1 & 0 \end{array} \right]. $

Đặt $x_4 = \alpha \Rightarrow x_3 = -x_4 = -\alpha$.
$x_2 = x_3 + x_4 = -\alpha + \alpha = 0$.
$x_1 = -x_2 + x_3 + 2x_4 = 0 - \alpha + 2\alpha = \alpha$.
Nghiệm là $(\alpha, 0, -\alpha, \alpha)$.

Ta tìm vector x:
$x = x_3g_1 + x_4g_2 = -\alpha(1, 1, 0) + \alpha(2, 1, 1) = \alpha(1, 0, 1)$.

Dễ dàng suy ra cơ sở của $F \cap G$ là $\{(1,0,1)\}$ và $\dim(F \cap G) = 1$.