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

