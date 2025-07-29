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

Vi du 

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
