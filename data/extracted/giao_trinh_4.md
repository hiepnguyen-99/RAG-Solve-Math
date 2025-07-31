# Chương 1

Nội dung

· Định nghĩa và ví dụ.

· Các phép biến đổi sơ cấp.

• Các phép toán đối với ma trận.

· Hạng của ma trận.

· Ma trận nghịch đảo.

Các khái niệm cơ bản

## 1.1 Các khái niệm cơ bản

### Dịnh nghĩa 1.1 (Ma trận).

Ma trận cỡ m $\times$ n là một bảng số (thực hoặc phức) hình chữ nhật có m hàng và n cột.

$ A = \begin{pmatrix} a_{11} & \ldots & a_{1j} & \ldots & a_{1n} \\ \ldots & \ldots & \ldots & \ldots & \ldots \\ a_{i1} & \ldots & a_{ij} & \ldots & a_{in} \\ \ldots & \ldots & \ldots & \ldots & \ldots \\ a_{m1} & \ldots & a_{mj} & \ldots & a_{mn} \end{pmatrix} $

Vi du 1.1

$ A = \begin{pmatrix} 3 & 4 & 1 \\ 2 & 0 & 5 \end{pmatrix}_{2 \times 2}, B = \begin{pmatrix} 1+i & 2 \\ 3-i & 4i \end{pmatrix}. $

A là ma trận cỡ 2 $\times$ 3 có 2 hàng và 3 cột. Các phần tử của ma trận A:

$a_{11} =$ 3, $a_{12} =$ 4, $a_{13} =$ 1, $a_{21} =$ 2, $a_{22} =$ 0, $a_{32} =$ 5.

B là ma trận cỡ 2 $\times$ 2 có các phần tử trong phức.

Ghi chú

• Ma trận A $\circ \tilde{\sigma}$ m $\times$ n thường được ký hiệu bởi A $= (a_{ij})_{m \times n}$.

• Tập tất cả các ma trận cỡ m $\times$ n trên trường số K được ký hiệu $M_{m \times n}(K)$.

Ma trận không.

Ma trận không có tất cả các phần tử bằng 0, ký hiệu là 0

$ 0_{2\times3} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}. $

Có vô số ma trận 0 tùy theo cỡ.



Phần tử cơ sở của một hàng là phần tử khác 0 đầu tiên

của hàng đó kể từ bên trái sang.

Hàng toàn số 0 thì không có phần tử cơ sở.

Ma trận bậc thang

1. Hàng toàn số 0 (nếu có) thì nằm dưới.

2. Phần từ cơ sở hàng dưới nằm bên phải phần tử cơ sở hàng trên.

Vi dụ 1.2

$ A = \begin{pmatrix} 2 & 1 & 0 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & -1 & 0 & 2 \end{pmatrix} không phải bậc thang. B = \begin{pmatrix} -2 & 1 & 0 & -1 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & -3 \end{pmatrix} không phải bậc thang. $

$ C = \begin{pmatrix} 2 & 1 & 0 & 0 & 2 \\ 0 & 0 & 3 & 2 & 0 \\ 0 & 0 & 0 & 0 & -3 \end{pmatrix} là ma trận bậc thang. D = \begin{pmatrix} \boxed{1} & 2 & 0 & 1 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -4 \end{pmatrix} là ma trận bậc thang. $

Ma trận chuyển vị

Chuyển vị của A $= (a_{ij})_{m \times n}$ là ma trận AT $= (a_{ji})_{n \times m}$ thu

được từ A bằng cách chuyển hàng thành cột.

$ Ví dụ 1.3 A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 0 & 3 \end{pmatrix} \longrightarrow A^{T} = \begin{pmatrix} 1 & 2 \\ 2 & 0 \\ 3 & 3 \end{pmatrix} $

Ma trận vuông có số hàng bằng số cột.

Tập tất cả các ma trận vuông trên trường số K được ký hiệu là $M_n[K]$.

Đường chéo chính của ma trận vuông A đi qua các phần tử

$a_{11}$, $a_{22}$, $\ldots$, $a_{nn}$

Vi dụ 1.4

$\overline{2}$

3 $\t$ 4

$ Ma trận vuông cấp 4 \begin{pmatrix} 2 & (1) & -2 & 0 \\ 0 & 2 & \boxed{-3} & 2 \end{pmatrix} $

có các phần tử trên đường chéo chính là 1, 1, -3, 0.

Ma trận tam giác

i) Ma trận vuông A $= (a_{ij})_n$ gọi là tam giác trên nếu $a_{ij} =$ 0, $\forall$ i $>$ j

Các phần tử phía dưới đường chéo chính bằng 0.

Ma trận vuông A $= (a_{ij})_n$ gọi là tam giác dưới nếu $a_{ij} =$ 0, $\forall$ i $<$ j

ii)

Các phần tử phía trên đường chéo chính bằng 0.



Ma trận chéo có các phần tử nằm ngoài đường chéo chính bằng 0.

Hay nó vừa tam giác trên, vừa tam giác dưới.

Ma trận vuông, không cũng là ma trận chéo.

Ma trận đơn vị là ma trận chéo với các phần từ trên đường chéo bằng 1.

Ma trận đối xứng thỏa $A^T =$ A

Ma trận phản đối xứng thỏa $A^T =$ -A

Vi du 1.5

$ Ma trận tam giác trên A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 2 & 0 \\ 0 & 0 & -2 \end{pmatrix}. Ma trận tam giác dưới A = \begin{pmatrix} 1 & 0 & 0 \\ -3 & 0 & 0 \\ 3 & 2 & -2 \end{pmatrix}. $

$ Ma trận chéo D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 3 \end{pmatrix}. Ma trận đơn vị cấp 3 là I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}. $

$ Ma trận đối xứng A = \begin{pmatrix} 0 & 1 & 2 \\ 1 & 2 & -3 \\ 2 & -3 & 4 \end{pmatrix}. Ma trận phản đối xứng A = \begin{pmatrix} 0 & -1 & 2 \\ 1 & 0 & -3 \\ -2 & 3 & 0 \end{pmatrix}. $

Các phép biến đổi sơ cấp

## 1.2\, Các phép biến đổi sơ cấp

Các phép biến đổi sơ cấp theo hàng

1) Nhân một hàng với 1 số khác 0: $h_i \rightarrow \alpha h_i; \alpha \neq$ 0.

2) Cộng vào một hàng một hàng khác đã được nhân với 1 số tùy ý:

$h_i \rightarrow h_i$ + $\beta h_j$, $\forall \beta$.

3) Đổi chỗ 2 hàng: $h_i \leftrightarrow h_j$.

Tương tự ta có 3 phép biến đổi theo cột.

Các phép biến đổi sơ cấp là các phép biến đổi cơ bản nhất đổi với ma trận.

### Dịnh lý Mọi ma trận đều có thể đưa về dạng bậc

bằng các phép biến đổi sơ cấp.

Khi dùng phép biến đổi sơ cấp với ma trận, ta thu được nhiều ma trận bậc thang khác nhau.

$ Ví dụ 1.6 Dùng phép biến đổi sơ cấp đưa ma trận sau về dạng bậc thang A = \begin{pmatrix} 1 & 1 & 1 & 2 & 1 \\ 2 & 3 & -1 & 4 & 5 \\ 3 & 2 & -3 & 7 & 4 \end{pmatrix} $

$ A = \begin{pmatrix} \boxed{1} & 1 & -1 & 2 & 1 \\ 2 & 3 & -1 & 4 & 5 \\ 3 & 2 & -3 & 7 & 4 \\ -1 & 1 & 2 & -3 & 1 \end{pmatrix} \xrightarrow[h_4 \rightarrow h_4 + h_1]{h_2 \rightarrow h_2 - 2h_1} \begin{pmatrix} \boxed{1} & 1 & -1 & 2 & 1 \\ 0 & \boxed{1} & 1 & 0 & 3 \\ 0 & -1 & 0 & 1 & 1 \\ 0 & 2 & 1 & -1 & 2 \end{pmatrix} \xrightarrow[h_4 \rightarrow h_4 - 2h_2]{h_3 \rightarrow h_3 + h_2} \begin{pmatrix $

$ \underbrace{h_4 \rightarrow h_4 + h_3}_{0} \underbrace{\begin{pmatrix} 1 & 1 & -1 & 2 & 1 \\ 0 & 1 & 1 & 0 & 3 \\ 0 & 0 & 1 & 1 & 4 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}} \Rightarrow r(A) = 3. $



Các phép toán ma trân

## 1.3 Các phép toán ma trân

Hai ma trận bằng nhau nếu chúng cùng cỡ và các phần

tử tương ứng bằng nhau: $a_{ij} = b_{ij}$, $\forall$ i, j.

Cho 2 ma trận A, B cùng cỡ và số $\alpha$.

Tổng A + B: cộng các phần tử tương ứng.

Nhân $\alpha.A:$ nhân $\alpha$ vào tất cả các phần tử của A.

$ Ví dụ 1.7 a) \begin{pmatrix} 1 & 2 & -1 \\ 2 & -1 & 0 \end{pmatrix} + \begin{pmatrix} 3 & -2 & 1 \\ 1 & 0 & 3 \end{pmatrix} = \begin{pmatrix} 4 & 0 & 0 \\ 3 & -1 & 3 \end{pmatrix}. $

$ b) 2. \begin{pmatrix} 1 & 2 & -1 \\ 2 & -1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 4 & -2 \\ 4 & -2 & 0 \end{pmatrix}. $

$ c) 2. \begin{pmatrix} 1 & 2 & -1 \\ 2 & -1 & 0 \end{pmatrix} - 3. \begin{pmatrix} 3 & -2 & 1 \\ 1 & 0 & 3 \end{pmatrix} = \begin{pmatrix} -7 & 10 & -5 \\ 1 & -2 & -9 \end{pmatrix}. $

Tính chất

i. A + B $=$ B + A. iv. $\alpha(A$ + B) $= \alpha$ A + $\alpha$ B.

ii. $(A+B)+C=A+(B+C)$. v. $\alpha(\beta A)=(\alpha\beta)A$.

iii. A + 0 $=$ A.

vi. $(\alpha$ + $\beta)A = \alpha$ A + $\beta$ A.

Phép nhân hai ma trận Cho A $= (a_{ij})_{m \times p}$, B $= (b_{ij})_{p \times m}$.

Tich A.B $=$ C $= (c_{ij})_{m \times n}: c_{ij} = a_{i1}b_{1j}$ + $a_{i2}b_{2j}$ + $\cdots$ + $a_{ip}b_{pj}$.

$ AB = \begin{pmatrix} \dots & \dots & \dots & \dots \\ a_{i1} & a_{i2} & \dots & a_{ip} \\ \dots & \dots & \dots & \dots \end{pmatrix} \cdot \begin{pmatrix} \dots & b_{1j} & \dots \\ \dots & b_{2j} & \dots \\ \dots & \dots & \dots \end{pmatrix} = \begin{pmatrix} \dots & \dots & \dots \\ \dots & c_{ij} & \dots \\ \dots & \dots & \dots \end{pmatrix} $

Điều kiện phép nhân AB: số cột của A bằng số hàng của B.

$c_{ij}$ là tích vô hướng hàng i của A và cột j của B.

$ Ví dụ 1.8 Cho A = \begin{pmatrix} 2 & -1 & 4 \\ 4 & 1 & 0 \end{pmatrix}; B = \begin{pmatrix} 1 & -2 & 2 \\ 3 & 0 & 1 \\ 2 & 4 & 3 \end{pmatrix}. Tính AB. $

$ c_{11} = (2 \quad -1 \quad 4) \begin{pmatrix} 1 \\ 3 \\ 2 \end{pmatrix} = 2.1 + (-1).3 + 4.2 = 7: tích vô hướng hàng 1 của A và cột 1 của B. $

$ Tương tự, ta tính được AB = \begin{pmatrix} 7 & 12 & 15 \\ 7 & -8 & 9 \end{pmatrix}. $

Tính chất

i. A(BC) $=$ (AB)C. iv. $I_m$ A $= AI_m =$ A. ii. A(B + C) $=$ AB + AC. iii. (B + C)A $=$ BA + CA. v. $\alpha(AB) = (\alpha$ A)B $= A(\alpha$ B).

Chú ý: Nhìn chung AB $\neq$ BA; AB $=$ AC $\Rightarrow$ B $=$ C, AB $=$ 0 $\Rightarrow$ A $=$ 0 $\vee$ B $=$ 0.



Nâng lũy thừa:

Quy ước: $A^0 =$ I $A^n =$ A.A...A.A(n $\text{$ n ma trận $}$ A).

$ Ví dụ 1.9 Cho A = \begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix} và f(x) = 2x^2 - 4x + 3. Tính f(A). $

Ta có

f(A) $= 2A^2$ - 4A + 3I.

$ f(A) = 2\begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}^2 - 4\begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix} + 3\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = 2\begin{pmatrix} 1 & -6 \\ 18 & 13 \end{pmatrix} - \begin{pmatrix} 8 & -4 \\ 12 & 16 \end{pmatrix} + \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} -3 & -8 \\ 24 & 13 \end{pmatrix} $

Ví dụ 1.10 Tính $A^{200}$, với

$ b) A = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix}. $

$ a) A = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}. $

$ c) A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}. $

Bài giải

$ a) A^2 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 6 \\ 0 & 1 \end{pmatrix}, \quad A^3 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 6 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 9 \\ 0 & 1 \end{pmatrix} \Rightarrow A^{200} = \begin{pmatrix} 1 & 200.3 \\ 0 & 1 \end{pmatrix}. $

$ b) A = 2\begin{pmatrix} 1 & \frac{3}{2} \\ 0 & 1 \end{pmatrix} \Longrightarrow A^{200} = 2^{200} \begin{pmatrix} 1 & 200 \cdot \frac{3}{2} \\ 0 & 1 \end{pmatrix} = 2^{200} \begin{pmatrix} 0 & 300 \\ 0 & 1 \end{pmatrix}. $

$ c) A^2 = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}. \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} = 2 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = 2A \Longrightarrow A^{200} = 2^{199}. A = \begin{pmatrix} 2^{199} & 2^{199} \\ 2^{199} & 2^{199} \end{pmatrix}. $

Tóm lai

$ \begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}^n = \begin{pmatrix} 1 & na \\ 0 & 1 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}^n = 2^{n-1} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}. $

Hạng của ma trận

## 1.4 Hạng của ma trận

Hạng ma trận A là số hàng khác 0 của ma trận bậc thang

của A, ký hiệu là: r(A).

$ Ví dụ 1.11 Tìm hạng của ma trận A = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 4 & 2 & 2 \\ 3 & 6 & 3 & 4 \end{pmatrix}. $

$ A = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 4 & 2 & 2 \\ 3 & 6 & 3 & 4 \end{pmatrix} \xrightarrow[h_3-3h_1]{h_2-2h_1} \begin{pmatrix} 1 & 2 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \xrightarrow[h_2 \leftrightarrow h_3]{h_2 \leftrightarrow h_3} \begin{pmatrix} 1 & 2 & 1 & 1 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} \implies r(A) = 2. $

Tính chất

i) r(A) $=$ 0 $\Longrightarrow$ A $=$ 0.ii) A $= (a_{ij})_{m \times n} \Longrightarrow$ r(A) $\le \min\{m$, $n\}$.

iii) Nếu A $\xrightarrow{\text{bién$ dối sớ $cáp}}$ B $\Longrightarrow$ r(A) $=$ r(B).



Ma trận nghịch đảo

## 1.5 Ma trận nghịch đảo

Ma trận nghịch đảo

Ma trận vuông $<math display="inline">Agọi$ là khả nghịch nếu tồn tại ma trận $<math display="inline">Bsao$ cho

AB $=$ I $=$ BA.

Khi đó, B gọi là nghịch đảo của A, ký hiệu là $A^{-1}$.

Ví dụ 1.12

$ a) Nghịch đảo của A = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix} là \begin{pmatrix} -3 & 2 \\ 2 & -1 \end{pmatrix}. Vì \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix} \begin{pmatrix} -3 & 2 \\ 2 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} -3 & 2 \\ 2 & -1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}. $

$ b) Cho A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}. Ta tìm ma trận nghịch đảo của A có dạng B = \begin{pmatrix} a & b \\ c & d \end{pmatrix}. $

$ Ta có AB = I \Longleftrightarrow \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \Longleftrightarrow \begin{pmatrix} 2a+c & 2b+d \\ 5a+c & 5b+d \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} $

$ \Leftrightarrow \begin{cases} 2a + c = 1 \\ 2b + d = 0 \\ 5a + c = 0 \\ 5b + d = 1 \end{cases} \Leftrightarrow \begin{cases} a = 3 \\ b = -1 \\ c = -5 \\ d = 2 \end{cases} \Rightarrow A^{-1} = B = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}. $

$ c) Hãy thử tìm ma trận nghịch đảo của A = \begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}. $

Chú ý: Không phải mt vuông nào cũng có nghịch đảo. Có rất nhiều mt vuông không có nghịch đảo.

Sự tôn tại ma trận khả nghịch

Cho ma trận vuông A. Các mệnh đề sau tương đương

i) A khả nghịch (tồn tại $A^{-1})$.

ii) r(A) $=$ n: ma trận không suy biến iii) AX $=$ 0 $\Longleftrightarrow$ X $=$ 0. iv) A $\xrightarrow{\text{Bdsc$ theo $hàng}}$ I.

Ma trận sơ cấp: Ma trận thu được từ I bằng đúng 1 phép

biến đổi sơ cấp gọi là ma trận sơ cấp.

Ví du 1.13

$ I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{h_3 \to 3h_3} E_1 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{pmatrix}, \qquad I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{h_2 \to h_2 + 2h_1} E_2 = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} $

$ A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \xrightarrow{h_3 \rightarrow 3h_3} \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 21 & 24 & 27 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} = E_1.A. $

$ A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \xrightarrow{h_2 \rightarrow h_2 + 2h_1} \begin{pmatrix} 1 & 2 & 3 \\ 6 & 9 & 12 \\ 7 & 8 & 9 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} = E_2.A. $

Tương tự:

$ I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{c_1 \leftrightarrow c_3} E_3 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix} \Longrightarrow A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} \xrightarrow{h_3 \leftrightarrow h_1} \begin{pmatrix} 3 & 2 & 1 \\ 6 & 5 & 4 \\ 9 & 8 & 7 \end{pmatrix} = A.E_3. $



Mỗi phép biến đổi sơ cấp tương ứng với phép nhân ma trận sơ cấp tương ứng.

Bầu theo hàng $\Rightarrow$ nhân bên trái. Bầu theo cột $\Rightarrow$ nhân bên phải.

Cách tìm ma trận nghịch đảo

[A|I] $\xrightarrow{\text{Bdsc$ theo $h\nàng}} [I|A^{-1}]$

$ Ví dụ 1.14 Tìm ma trận nghịch đảo A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 2 \end{pmatrix}. $

Bài giải

$ [A|I] = \left( \begin{array}{cccc} \boxed{1} & 1 & 1 & 1 & 0 & 0 \\ 1 & 2 & 2 & 0 & 1 & 0 \\ 1 & 2 & 3 & 0 & 0 & 1 \end{array} \right) \xrightarrow[h_3-h_1]{h_2-h_1} \left( \begin{array}{cccc} 1 & 1 & 1 & 0 & 0 \\ 0 & \boxed{1} & 1 & -1 & 1 & 0 \\ 0 & 1 & 2 & -1 & 0 & 1 \end{array} \right) \xrightarrow[h_1-h_2]{h_3-h_2} \left( \begin{array}{cccc} 1 & 0 & 0 & 2 & -1 & 0 \\ 0 & 1 & 1 $

$ \underbrace{h_2-h_3}_{\Omega} \left( \begin{array}{ccc|ccc} 1 & 0 & 0 & 2 & -1 & 0 \\ 0 & 1 & 0 & -1 & 2 & -1 \\ 0 & 0 & 1 & 0 & 1 & 1 \end{array} \right) \Longrightarrow A^{-1} = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}. $

Tính chất ma trận nghịch đảo

Cho hai ma $trận<math display="inline">A,Bkhả$ nghịch. Ta có

i) $(A^{-1})^{-1} =$ A ii) $(AB)^{-1} = B^{-1}A^{-1}$ iii) $(A^T)^{-1} = (A^{-1})^T$.

Bài tập

$ Bài 1. Cho A = \begin{pmatrix} 1 & 2 & 1 \\ -1 & 1 & -2 \end{pmatrix}, B = \begin{pmatrix} -1 & 2 \\ 0 & 2 \\ -1 & 1 \end{pmatrix}. Tính 3A - 2B^T $

$ Bài 2. Cho A = \begin{pmatrix} 1 & 2 & 1 \\ -1 & 1 & -2 \end{pmatrix}, B = \begin{pmatrix} -1 & 2 \\ 0 & 2 \\ -1 & 1 \end{pmatrix}, C = \begin{pmatrix} 2 & 1 & 0 \\ -1 & 1 & 1 \\ 0 & 2 & -1 \end{pmatrix}. Tính 2AC - (CB)^T $

$ Bài 3. Cho A = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix} và f(x) = x^2 - 4x - 1. Tính f(A) và A^{2013}. $

$ Bài 4. Cho A = \begin{pmatrix} 2 & -1 \\ 3 & 1 \end{pmatrix} và B = \begin{pmatrix} -2 \\ 3 \end{pmatrix}. Tìm ma trận X thỏa AX = B. $

$ Dáp số X = \begin{pmatrix} 1 & 1 \\ 5 & 12 \end{pmatrix}. $

Bài 5. Tìm hạng của ma trận

$ (a) A = \begin{pmatrix} 1 & 2 & 1 \\ -2 & 2 & -1 \\ 1 & 8 & 2 \end{pmatrix}.
(c) A = \begin{pmatrix} 1 & 1 & 2 & 1 & -1 \\ 2 & 1 & 3 & 4 & -2 \\ 3 & 1 & 4 & 7 & -3 \\ 5 & 3 & 8 & 9 & -5 \end{pmatrix} (e) A = \begin{pmatrix} m & 1 & 1 \\ 1 & m & 1 \\ 1 & 1 & m \end{pmatrix}. $

$ (b) A = \begin{pmatrix} 1 & 2 & 1 & 2 \\ 2 & 3 & -1 & 1 \\ 3 & 4 & -3 & 2 \\ 2 & 3 & -1 & 3 \end{pmatrix} (d) \begin{pmatrix} 1 & 1 & -1 \\ 2 & 3 & 1 \\ 3 & 5 & m \end{pmatrix}. $

$ (f) \begin{pmatrix} 1 & m & -1 & 2 \\ 2 & -1 & m & 5 \\ 1 & 10 & -6 & m \end{pmatrix}. $

$ Bài 6. Tìm ma trận nghịch đảo (nếu có) của A = \begin{pmatrix} 1 & 1 & -1 \\ 2 & 3 & 1 \\ 2 & 4 & 1 \end{pmatrix}, Dáp án \begin{pmatrix} -1 & -5 & 4 \\ 1 & 4 & -3 \\ 1 & 1 & 1 \end{pmatrix}. $



# Chương 2

Nội dung

· Định nghĩa định thức và ví dụ.

· Tính chất định thức.

· Dùng định thức để tìm ma trận nghịch đảo.

### Định nghĩa định thức và ví dụ

## 2.1 Định nghĩa định thức và ví dụ

Định thức ma trận vuông A $= (a_{ij})_n$ là một số, được ký

hiệu bởi

$\det(A) = |a^{ij}|_n =$ |A|.

Bù đại số của phần tử $a_{ij}$ là

$ A_{ij} = (-1)^{i+j} \begin{vmatrix} \text{dinh thức thu được từ } A \\ \text{bỏ đi hàng i, cột j} \end{vmatrix}_{n-1} $

### Định nghĩa định thức bằng qui nạp.

$ i) k = 1 : A = [a_{11}] \Rightarrow |A| = a_{11}.
ii) k = 2 : A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \Rightarrow |A| = a_{11}A_{11} + a_{12}A_{12} = a_{11}a_{22} - a_{12}a_{21}.
:
iii) k = n : A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & \ddots & \vdots \\ \vdots & \vdots & \ddots & \vdots \end{pmatrix} \Rightarrow |A| = a_{11} $

$ Ví dụ 2.1 Tính định thức của \begin{pmatrix} 1 & 2 & -3 \\ 2 & 3 & 0 \\ 3 & 2 & 4 \end{pmatrix}. $

Bài giải

$\det(A) = a_{11}A_{11}$ + $a_{12}A_{12}$ + $a_{13}A_{13} = 1A_{11}$ + $2A_{12}$ - $3A_{13}$.



$ A_{11} = (-1)^{1+1} \begin{vmatrix} 3 & 0 \\ 2 & 4 \end{vmatrix} = 12 (từ A, bỏ hàng 1 và cột 1).Tương tự: \det(A) = 1(-1)^{1+1} \begin{vmatrix} 3 & 0 \\ 3 & 4 \end{vmatrix} + 2(-1)^{1+2} \begin{vmatrix} 2 & 0 \\ 3 & 4 \end{vmatrix} - 3(-1)^{1+3} \begin{vmatrix} 2 & 3 \\ 3 & 2 \end{vmatrix} = 12 - 16 + 15 = 11. $

Tính chất định thức

## 2.2 Tính chất định thức

Có thể tính định thức bằng cách khai triển theo một

hàng hoặc 1 cột bất kỳ

$ |A| = \begin{vmatrix} \cdots & \cdots & \cdots & \cdots \\ a_{k1} & a_{k2} & \cdots & a_{kn} \\ \cdots & \cdots & \cdots & \cdots \end{vmatrix} = a_{k1}A_{k1} + a_{k2}A_{k2} + \cdots + a_{kn}A_{kn}. $

Ví dụ 2.2 Tính định thức

$ b) \begin{vmatrix} 2 & -3 & 3 & 2 \\ 3 & 0 & 1 & 4 \\ -2 & 0 & 3 & 2 \\ 4 & 0 & -1 & 5 \end{vmatrix} $

$ a) \begin{vmatrix} 1 & 2 & -1 \\ 2 & 1 & 3 \\ 0 & 0 & -3 \end{vmatrix}. $

$ a) Khai triển theo hàng 3: \begin{vmatrix} 1 & 2 & -1 \\ 2 & 1 & 3 \\ 0 & 0 & -3 \end{vmatrix} = -3(-1)^{3+3} \begin{vmatrix} 1 & 2 \\ 2 & 1 \end{vmatrix} = -3(-3) = 9. $

b) Khai triển theo cột 2

$ I = \begin{vmatrix} 2 & -3 & 3 & 2 \ 3 & 0 & 1 & 4 \ -2 & 0 & 3 & 2 \ 4 & 0 & -1 & 5 \ \end{vmatrix} = -3(-1)^{1+2} \begin{vmatrix} 3 & 1 & 4 \ -2 & 3 & 2 \ 4 & -1 & 5 \ \end{vmatrix} khai triển theo hàng 1,= 3(3(-1)^{1+1}) \begin{vmatrix} 3 & 2 \ -1 & 5 \ \end{vmatrix} + 1(-1)^{1+2} \begin{vmatrix} -2 & 2 \ 4 & 5 \ \end{vmatrix} + 4(-1)^{1+ $

Định thức của ma trận tam giác bằng tích các phần tử nằm

trên đường chéo chính.

Ví dụ 2.3 .

$ \begin{vmatrix} 1 & -2 & 2 & 3 \\ 0 & 4 & -2 & 0 \\ 0 & 0 & -3 & 2 \end{vmatrix} = 1.4.(-3).5 = -60. $

$\overline{5}$

$\overline{0}$

$|0\rangle$

$\overline{0}$

Dùng biến đổi sơ cấp để tính định thức

1. Nếu A $\xrightarrow{h_i \to \alpha h_j}$ B thì |B| $= \alpha$ |A|.

2. Nếu A $\xrightarrow{h_i$ + $\beta h_j}$ B thì |B| $=$ |A|.

3. Nếu A $\xrightarrow{h_i \leftrightarrow h_j}$ B thì |B| $=$ -|A|.



Nguyên tắc tính định thức sử dụng biến đối sơ cấp

1. Chọn 1 hàng (hoặc 1 cột tùy ý).

2. Chọn 1 phần tử khác 0 của hàng (cột) đó. Dùng biến

đối sơ cấp, khử tất cả các phần tử khác.

3. Khai triển theo hàng (hay cột) đã chọn.

Ví du 2.4.

$ (a) I = \begin{bmatrix} 1 & 1 & 2 & -1 \ 2 & 3 & 5 & 0 \ 3 & 2 & 6 & -2 \ -2 & 1 & 3 & 1 \end{bmatrix} \xrightarrow[h_4 + 2h_1]{h_2 - 2h_1} \begin{bmatrix} 1 & 1 & 2 & -1 \ 0 & 1 & 1 & 2 \ 0 & -1 & 0 & 1 \ 0 & 3 & 7 & -1 \end{bmatrix} \xrightarrow[\text{theo côt 1}]{\text{khai triën}} 1.(-1)^{1+1} \begin{bmatrix} 1 & 1 & 2 \ -1 & 0 & 1 \ 3 & 7 & -1 \end{bmatrix} $

$ \frac{h_3 - 3h_1}{-1} \begin{vmatrix} 1 & 1 & 2 \\ -1 & 0 & 1 \\ -4 & 0 & -15 \end{vmatrix} = 1.(-1)^{1+2} \begin{vmatrix} -1 & 1 \\ -4 & -15 \end{vmatrix} = -1(15+4) = -19. $

$ b) \begin{vmatrix} 3 & 2 & -1 & 1 \\ 2 & 3 & -2 & 0 \\ -3 & 1 & 4 & -2 \\ 4 & 1 & 3 & 1 \end{vmatrix} \xrightarrow{h_3+2h_1} \begin{vmatrix} 3 & 2 & -1 & 1 \\ 2 & 3 & -2 & 0 \\ 3 & 5 & 2 & 0 \\ 1 & -1 & 4 & 0 \end{vmatrix} \xrightarrow{\text{khai triën}} -1 \begin{vmatrix} 2 & 3 & -2 \\ 3 & 5 & 2 \\ 1 & -1 & 4 \end{vmatrix} = -\begin{vmatrix} 2 & 3 & -2 \\ 5 & 8 & 0 \\ 5 & 5 & 0 \ $

Tính chất định thức: Cho A $\in M_n$.

i) $\det(A^T) = \det(A)$. iii) $\det(AB) = \det(A) \cdot \det(B)$.

ii) $|\alpha$ A| $= \alpha^n$ |A|. iv) $|A^m| = |A|^m$.

v) A có 1 hàng (hoặc cột) bằng 0 thì |A| $=$ 0.

vi) A có 2 hàng (hoặc cột) tỷ lệ thì |A| $=$ 0.

Chú $\hat{\mathbf{y}}:$ nhìn chung det(A + B) $\neq \det(A)$ + $\det(B)$.

Ví dụ 2.5 Cho A, B $\in M_3$ thỏa |A| $=$ 2, |B| $=$ 3.

Ta có $|2A^3| = 2^3$. $|A|^3 = 8.2^3 =$ 64. $|3AB^T| = 3^3|A||B| =$ 27.2.3 $=$ 162.

Điều kiện khả nghịch

A khả nghịch khi và chỉ khi |A| $\neq$ 0.

$ Ví dụ 2.6 Tìm m để A.B khả nghịch. Biết A = \begin{pmatrix} 1 & 2 & 1 \\ 0 & -1 & 2 \\ 0 & -1 & 3 \end{pmatrix}, B = \begin{pmatrix} 2 & -1 & 3 \\ 0 & 1 & 1 \\ m & 2 & 1 \end{pmatrix}. $

Bài làm

AB khả nghịch khi và chỉ khi det(AB) $\neq$ 0

$\iff \det(A) \cdot \det(B) \neq$ 0 $\iff$ -1 $\cdot$ (-4m-1) $\neq$ 0 $\iff$ m $\neq -\frac{1}{4}$.



Tìm ma trận nghịch đảo bằng phương pháp định thức.

## 2.3 Tìm ma trận nghịch đảo bằng phương pháp định thức.

### Dịnh nghĩa 2.1 (Ma trận phụ hợp).

Ma trận phụ hợp của ma trận vuông A $\in M_n$ được định nghĩa là

$ P_A = \begin{pmatrix} A_{11} & A_{12} & \ldots & A_{1n} \\ A_{21} & A_{22} & \ldots & A_{2n} \\ \ldots & \ldots & \ldots & \ldots \\ A_{n1} & A_{n2} & \ldots & A_{nn} \end{pmatrix}. $

Công thức tính ma trận nghịch đảo $A^{-1} = \frac{1}{|A|} P_A$

$ Ví dụ 2.7 Tìm ma trận nghịch đảo A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & 1 \\ 3 & 4 & 0 \end{pmatrix}. $

Bài làm

$\det(A) =$ -2 $\neq$ 0 $\Longrightarrow$ A khả nghịch.

$ A_{11} = (-1)^{1+1} \begin{pmatrix} 3 & 1 \\ 4 & 0 \end{pmatrix} = -4, A_{12} = (-1)^{1+2} \begin{pmatrix} 2 & 1 \\ 3 & 0 \end{pmatrix} = 3, A_{13} = (-1)^{1+3} = \begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix} = -1.Tuong tự: A_{21} = 4, A_{22} = -3, A_{23} = -1, A_{31} = -2, A_{32} = 1, A_{33} = 1. $

$ Ma trận nghịch đảo A^{-1} = \frac{1}{|A|} P_A = \frac{1}{-2} \begin{pmatrix} -4 & 4 & -2 \\ 3 & -3 & 1 \\ -1 & -1 & 1 \end{pmatrix} (nhớ lấy chuyển vị). $

Tính chất

i) $|A^{-1}| = \frac{1}{|A|}ii) P_A = |A|^{n-1}$.

$ iii) r(P_A) = \begin{cases} n, & \text{nêu } r(A) = n \\ 1, & \text{nêu } r(A) = n - 1 \\ 0, & \text{nêu } r(A) < n - 1 \end{cases} $

Ví dụ 2.8 Cho A $\in M_3$ biết |A| $=$ -2. Tính $det(2P_A^2)$.

Bài làm

Ta có: $\det(2P_4^2) = 2^3 \cdot |P_A|^2 =$ 8 $\cdot (|A|^{3-1})^2 =$ 8 $\cdot (-2)^4 =$ 128.

$ Ví dụ 2.9 Cho A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 3 & -1 \\ 1 & 1 & m \end{pmatrix}. Tìm m để r(P_A) = 1. $

Bài làm

$ A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 3 & -1 \\ 1 & 1 & m \end{pmatrix} \xrightarrow{bdsc} \begin{pmatrix} 1 & 2 & 1 \\ 0 & -1 & -3 \\ 0 & 0 & m+2 \end{pmatrix}, r(P_A) = 1 \Longleftrightarrow r(A) = 3 - 1 = 2 \Longleftrightarrow m = -2 $

Bài tập

1. Tính định thức

$ (a) \begin{vmatrix} 2 & 1 & -1 & 3 \\ 3 & 2 & 1 & -2 \\ 4 & 1 & 0 & 1 \\ -3 & 3 & 2 & 2 \end{vmatrix}. DS: 59. (b) \begin{vmatrix} 4 & 1 & 1 & 0 \\ 3 & -2 & 4 & 1 \\ -2 & 1 & 3 & 1 \\ 5 & 1 & 2 & 3 \end{vmatrix}. DS: -161. $



$ (c) \begin{vmatrix} 1 & 0 & 1+i \\ 0 & 1 & i \\ 1-i & 2+i & 1 \end{vmatrix}, DS: -2i, (h) \begin{vmatrix} 3 & 2 & 2 & \dots & 2 \\ 2 & 3 & 2 & \dots & 2 \\ 2 & 2 & 3 & \dots & 2 \\ \vdots & \vdots & \vdots & \vdots & \vdots \\ 2 & 2 & 2 & \dots & 3 \end{vmatrix}, DS: 2n+1. $

$ (d) \begin{vmatrix} 1 & 2 & 2 & 2 & 2 \\ 2 & 1 & 2 & 2 & 2 \\ 2 & 2 & 1 & 2 & 2 \\ 2 & 2 & 2 & 1 & 2 \\ 2 & 2 & 2 & 2 & 1 \end{vmatrix}. DS: 9. $

$ (i) \begin{vmatrix} 2 & x & 2 & 3 \\ x & -2 & 3 & 4 \\ 0 & 0 & 7 & 6 \\ 0 & 0 & 5 & 3 \end{vmatrix}. DS: 9(x^2 + 4). $

$ (j) D_n = \begin{vmatrix} 7 & 5 & 0 & \dots & 0 \\ 2 & 7 & 5 & \dots & 0 \\ 0 & 2 & 7 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \dots & 7 \end{vmatrix}. $

$ (e) \begin{vmatrix} 1 & x & x^2 & x^3 \\ 1 & a & a^2 & a^3 \\ 1 & b & b^2 & b^3 \\ 1 & c & c^2 & c^3 \end{vmatrix}. $

DS: (c-x)(b-x)(a-x)(c-a)(c-b)(b-a)

HD: kt theo $h_1$, suy ra $D_n = 7D_{n-1}$ - $10D_{n-2}$.

$ (f) \begin{vmatrix} 1 & 1 & 1 & \dots & 1 \\ 1 & 1-x & 1 & \dots & 1 \\ 1 & 1 & 2-x & \dots & 1 \end{vmatrix} (k) D_n = \begin{vmatrix} 4 & 4 & 0 & \dots & 0 \\ 1 & 4 & 4 & \dots & 0 \\ 0 & 1 & 4 & \dots & 0 \end{vmatrix} $

$ \begin{vmatrix} \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \ $

$ \begin{bmatrix} 0 & 0 & 0 & \dots & 4 \end{bmatrix} $

HD: kt theo $h_1$, suy ra $D_n = 4D_{n-1}$ - $4D_{n-2}$.

DS:-x(1-x)(2-x)...(n-1-x).

$ (g) \begin{vmatrix} 1 & 2 & 3 & \dots & n \\ -1 & 0 & 3 & \dots & n \\ -1 & -2 & 0 & \dots & n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ -1 & -2 & -3 & \dots & 0 \end{vmatrix}. DS: n! $

HD: kt theo $h_1$, suy ra $D_n = 2D_{n-1}$ - $2D_{n-2}$.

2. Tìm ma trận nghịch đảo

$ (a) A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 3 & -1 \\ 3 & 5 & 2 \end{pmatrix} DS: A^{-1} = \frac{1}{2} \begin{pmatrix} -11 & -1 & 0 \\ 7 & 1 & -3 \\ -1 & -1 & 1 \end{pmatrix}. $

$ (b) A = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 2 & -1 & 0 & 0 \\ 5 & 4 & 1 & 0 \\ 1 & 0 & 3 & 0 \end{pmatrix} \qquad DS: A^{-1} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 2 & -1 & 0 & 0 \\ -13 & 4 & 1 & 0 \\ 17 & 5 & 3 & 1 \end{pmatrix}. $

3. Tìm m đế ma trận khả nghịch

$ (a) A = \begin{pmatrix} 1 & 1 & 2 & 1 \\ 2 & 1 & 5 & 3 \\ 5 & 0 & 7 & m \\ -1 & 2 & 3 & -3 \end{pmatrix}. DS: m \neq 9. (b) A = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 3 & m \\ 3 & 2 & -1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & 2 \\ 5 & 7 & 5 \end{pmatrix}. DS: \neq m. $

$ 4. Cho A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & 1 \\ 3 & 3 & 5 \end{pmatrix}. Tính |A^{-1}|, |(5A)^{-1}|, |2P_A|. DS: \frac{1}{2}, \frac{1}{250}, 32. $

DS: $-\frac{1}{384}$, 36.

5. Cho A, B $\in M_3[R]$ : |A| $=$ 2, |B| $=$ -3. Tính $|(4AB)^{-1}|$, $|P_{AB}|$.



# Chương 3

Dinh nghĩa 3.1 (hệ phương trình tuyên tính) Hệ phương trình tuyến tính gồm m phương trình, n ấn

có dạng

$ \left\{\n\begin{array}{ccccccc}\na_{11}x_1 & + & a_{12}x_2 & + & \dots & + & a_{1n}x_n & = & b_1 \\
a_{21}x_1 & + & a_{22}x_2 & + & \dots & + & a_{2n}x_n & = & b_2 \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
a_{m1}x_1 & + & a_{m2}x_2 & + & \dots & + & a_{mn}x_n & = & b_m\n\end{array}\n\right. $

$a_{11}$, $a_{12}$, $\ldots$, $a_{mn}$ được gọi là hệ số của hệ phương trình.

$b_1$, $b_2$, $\ldots$, $b_m$ được gọi là hệ số tự do của hệ phương trình.

Ta ký hiệu

$ A = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \dots & \dots & \dots & \dots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix}, \quad X = \begin{pmatrix} x_1 \\ x_2 \\ \dots \\ x_n \end{pmatrix}, b = \begin{pmatrix} b_1 \\ b_2 \\ \dots \\ b_m \end{pmatrix}, \quad (A|b) = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} & b_1 \\ a_{21} & a_{22} & \dots & a_{2n} & b_2 \\ \dots & \dots & \dots & \dots \\ a $

Hệ phương trình được viết lại

A.X $=$ b hoặc viết gọn (A|b).

Chú thích

• Một hệ phương trình tuyến tính có thể:

1) vô nghiệm 2) có nghiệm duy nhất 3) vô số nghiệm.

• Hai hệ phương trình gọi là tương đương nếu chúng cùng tập nghiệm.

• Để giải hệ phương trình, ta dùng phép biến đổi tương đương để đưa về

hệ đơn giản.



Phép biến đổi tương đương

Một phép biến đổi được gọi là tương đương nếu nó biến một hệ

phương trình bất kỳ thành một hệ phương trình tương đương.

Ta có 3 phép biến đổi tương đương thường gặp:

i) Nhân 2 về của một phương trình với 1 số khác 0.

Cộng vào một phương trình một phương trình khác đã được

$\overline{11}$

nhân với một số tùy ý.

iii) Đổi chổ hai phương trình.

Chú $\dot{y}:$

$\bullet$ Đây là 3 phép biến đổi quen thuộc ở phổ thông mà chúng ta đã biết.

• Nếu ta ký hiệu hệ phương trình ở dạng ma trận mở rộng (A|b). Các phép biến đổi sơ cấp đối với ma

trận tương ứng với các phép biến đổi tương đương đối với hệ phương trình.

Ân cơ sở của hệ phương trình ở dạng bậc thang

$\bullet$ Ân cơ sở là ẩn tương ứng với cột chứa phần tử cơ sở.

$\bullet$ Ân tự do là ẩn tương ứng với cột không có phần tử cơ sở.

$ Ví dụ 3.1 \begin{bmatrix} 1 & 1 & 1 & 2 & 1 \\ 2 & 2 & 3 & 5 & 6 \\ 3 & 3 & 4 & 1 & -1 \end{bmatrix} \xrightarrow{bi\hat{e}n} d\hat{\phi}i s\sigma c\hat{a}p \longrightarrow \begin{bmatrix} (1) & 1 & 1 & 2 & 1 \\ 0 & 0 & (1) & 1 & 4 \\ 0 & 0 & 0 & (-6) & -8 \end{bmatrix} $

$x_1$, $x_3$, $x_4$ là phần tử cơ sở. $x_2$ là phần tử tự do.

Các bước giải hệ phương trình

Bước 1: Đưa ma trận $\tilde{A} =$ [A|b] về dạng bậc thang bằng

biến đổi sơ cấp theo hàng.

Kiểm tra hệ có nghiệm hay không.

Bước 2: Giải hệ phương trình từ dưới lên.

Ví dụ 3.2 Giải hệ phương trình

$x_1$ + $x_2$ - $x_3$ + $2x_4 =$ 1

$ \begin{cases} 2x_1 + 3x_2 - 3x_3 + 3x_4 = 3 \\ 3x_1 + 2x_2 - 5x_3 + 7x_4 = 5. \end{cases} $

Bài làm

$ \tilde{A} = \left[\begin{array}{ccc|c} 1 & 1 & -1 & 2 & 1 \\ 2 & 3 & -3 & 3 & 3 \\ 3 & 2 & -5 & 7 & 5 \end{array}\right] \xrightarrow[h_3-3h_1]{h_2-2h_1} \left[\begin{array}{ccc|c} 1 & 1 & -1 & 2 & 1 \\ 0 & 1 & -1 & -1 & 1 \\ 0 & -1 & -2 & 1 & 2 \end{array}\right] \xrightarrow[h_3+h_2]{h_3+h_2} \left[\begin{array}{ccc|c} (1) & 1 & -1 & 2 & 1 \\ 0 & (1) & -1 & -1 & 1 \\ 0 & 0 & (-3 $

Dặt $x_4 = \alpha$. pt (3): $x_3 =$ -1. Từ pt (2): $x_2 =$ 1 + $x_3$ + $x_4 = \alpha$. Từ pt (1): $x_1 =$ 1 - $x_2$ + $x_3$ - $2x_4 = -3\alpha$.

Vậy nghiệm của hệ là $(x_1$, $x_2$, $x_3$, $x_4) = (-3\alpha$, $\alpha$, -1, $\alpha)$, $\alpha \in$ R.



Dinh lý Kronecker Capelli

Nếu r(A|b) $\neq$ r(A) thì hệ AX $=$ b vô nghiệm.

Nếu r(A|b) $=$ r(A) thì hệ AX $=$ b có nghiệm.

i) Nếu r(A|b) $=$ r(A) $= s\hat{o}$ ẩn thì hệ AX $=$ b có nghiệm duy nhất.

ii) Nếu r(A|b) $=$ r(A) $<số$ ẩn thì hệ AX $=$ b có vô số nghiệm.

Ví dụ 3.3 Tìm tất cả các giá trị của m để hệ sau vô số nghiệm

$ \begin{cases}\nx_1 + x_2 - 2x_3 = 1 \\
2x_1 + 3x_2 - 3x_3 = 5 \\
3x_1 + mx_2 - 7x_2 = 8\n\end{cases} $

Bài làm

$ [A|b]=\left[\begin{array}{ccc|c} 1 & 1 & -2 & 1 \\ 2 & 3 & -3 & 5 \\ 3 & m & -7 & 8 \end{array}\right]\longrightarrow \left[\begin{array}{ccc|c} 1 & 1 & -2 & 1 \\ 0 & 1 & 1 & 3 \\ 0 & m-3 & -1 & 5 \end{array}\right]\longrightarrow \left[\begin{array}{ccc|c} 1 & -2 & 1 & 1 \\ 0 & 1 & 1 & 3 \\ 0 & -1 & m-3 & 5 \end{array}\right]\longrightarrow \left[\begin{array}{ccc|c} 1 & -2 & 1 & 1 \\ 0 & 1 & 1 & 3 \\ 0 & 0 & m-2 & 8 \end{array}\right $

Hệ vô số nghiệm khi và chỉ khi r(A) $=$ r(A) $<$ 3. Vì r(A|b) $=$ 3 nên không tồn tại m để hệ vô số nghiệm.

Ví dụ 3.4 Tìm tất cả các giá trị m để hệ có nghiệm duy nhất

$ \begin{cases}\nx_1 + 2x_2 + x_3 - x_4 = 5 \\
2x_1 + mx_2 - x_3 = -1 \\
mx_1 + x_2 - 3x_4 = 6\n\end{cases} $

Vì hệ có 3 phương trình nên r(A) $\leq$ 3 $<$ 4 $= s\hat{\sigma}$ ẩn nên hệ không có nghiệm duy nhất.

Chú ý: Nếu hệ có số phương trình ít hơn số ẩn thì không thể có nghiệm duy nhất.

## 3.1 Chú ý: Nếu hệ có số phương trình ít hơn số ẩn thì không thể có nghiệm duy nhất.

Hê Cramer

Hệ Cramer

Hệ AX $=$ b gọi là hệ Cramer nếu A là ma trận vuông và $\det(A) \neq$ 0.

Hệ Cramer có nghiệm duy nhất

$x_i = \frac{|A_i|}{|A|}$, i $\in \overline{1,n}$

với $A_i$ là ma trận thu từ A bằng cách thay cột i bởi cột tự do b.

Ví dụ 3.5 Kiếm tra hệ sau là Cramer và giải hệ

$ \begin{cases}\nx_1 + 2x_2 - x_3 = 12 \\
2x_1 + 3x_2 - 3x_3 = 4 \\
3x_1 + 2x_2 + 5x_3 = -8\n\end{cases} $

Bài làm

$ A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 3 & -3 \\ 3 & 2 & 5 \end{pmatrix}, A_1 = \begin{pmatrix} 12 & 2 & -1 \\ 4 & 3 & -3 \\ -8 & 2 & 5 \end{pmatrix}, A_2 = \begin{pmatrix} 1 & 12 & -1 \\ 2 & 4 & -3 \\ 3 & -8 & 5 \end{pmatrix} A_3 = \begin{pmatrix} 1 & 2 & 12 \\ 2 & 3 & 4 \\ 3 & 2 & -8 \end{pmatrix} $

$<math display="inline">|A| =$ -12 $\neq$ 0nên hệ là Cramer.

$|A_1| =$ 228, $|A_2| =$ -204, $|A_3| =$ -36. Nghiệm của hệ là $\left(\frac{|A_1|}{||A|}$, $\frac{|A_2|}{||A|}$, $\frac{|A_3|}{||A|}\right) =$ (-19, 17, 3).



Hệ thuần nhất

## 3.2 Hệ thuần nhất

Hệ thuần nhất

• Hệ AX $=$ b gọi là thuần nhất nếu tất cả các hệ số tự do

$b_1 = b_2 = \cdots = b_m =$ 0.

$\bullet$ Hệ thuần nhất luôn có nghiệm tầm thường.

$x_1 = x_2 = \cdots = x_n =$ 0

• Hệ thuần nhất có nghiệm duy nhất khi và chỉ khi

r(A) $=$ n $= s\hat{\delta} \text{ an}$.

• Cho A là ma trận vuông. Hệ thuần nhất AX $=$ 0 có nghiệm

không tầm thường $nghi\hat{e}m$ khác $\theta)$ khi và chỉ khi

A| $\neq$ 0.

Ví dụ 3.6 Giải hệ phương trình

$ \begin{cases}\nx_1 + x_2 - x_3 + 2x_4 = 0 \\
2x_1 + 3x_2 - 3x_3 + 3x_4 = 0 \\
3x_1 + 5x_2 - 5x_3 + 4x_4 = 0.\n\end{cases} $

Bài làm

$ \begin{vmatrix} 1 & 1 & -1 & 2 & 0 \\ 2 & 3 & -3 & 3 & 0 \\ 3 & 5 & -5 & 4 & 0 \end{vmatrix} \longrightarrow \begin{vmatrix} 1 & 1 & -1 & 2 & 0 \\ 0 & 1 & -1 & -1 & 0 \\ 0 & 2 & -2 & -2 & 0 \end{vmatrix} \longrightarrow \begin{bmatrix} (1) & 1 & -1 & 2 & 0 \\ 0 & (1) & -1 & -1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} $

Dặt các ẩn tự do làm tham số $x_3 = \alpha$, $x_4 = \beta$.

Pt(2): $x_2 = x_3$ + $x_4 = \alpha$ + $\beta$. $Pt(1):x_1 = -x_2$ + $x_3$ - $2x_4 = -3\beta$.

Vậy nghiệm của hệ là $(x_1$, $x_2$, $x_3$, $x_4) = (-3\beta$, $\alpha$ + $\beta$, $\alpha$, $\beta)$.

Ví dụ 3.7 Tìm m để hệ có nghiệm không tầm thường

$ \begin{cases}\nmx_1 + x_2 + x_3 + x_4 = 0 \\
x_1 + mx_2 + x_3 + x_4 = 0 \\
x_1 + x_2 + mx_3 + x_4 = 0 \\
x_1 + x_2 + x_3 + mx_4 = 0.\n\end{cases} $

Bài làm

Hệ có nghiệm không tầm thường khi và chỉ khi r(A) $<$ n $\Longleftrightarrow$ |A| $=$ 0.

$ |A| = \begin{vmatrix} m & 1 & 1 & 1 \\ 1 & m & 1 & 1 \\ 1 & 1 & m & 1 \\ 1 & 1 & 1 & m \end{vmatrix} = (m+3) \begin{vmatrix} 1 & 1 & 1 & 1 \\ 1 & m & 1 & 1 \\ 1 & 1 & m & 1 \\ 1 & 1 & 1 & m \end{vmatrix} = (m+3) \begin{vmatrix} 1 & 1 & 1 & 1 \\ 0 & m-1 & 0 & 0 \\ 0 & 0 & m-1 & 0 \\ 0 & 0 & 0 & m-1 \end{vmatrix} = (m+3)(m-1)^3. $

Vậy m $=$ -3 $\vee$ m $=$ 1.



Ví dụ 3.8 Tìm m để hệ có vô số nghiệm

$ \begin{cases}\nx_1 + x_2 + 2x_3 - x_4 = 0 \\
x_1 + 3x_2 + mx_3 + 2x_4 = 0 \\
mx_1 - x_2 + 3x_3 - 2x_4 = 0\n\end{cases} $

Bài làm

Vì A là ma trận cở 3 $\times$ 4 nên r(A) $\leq$ 3 $<$ 4 $= \hat{\delta}$ ẩn. Vậy hệ luôn có vô số nghiệm.

Chú ý: Hệ thuần nhất có số phương trình ít hơn số ẩn thì vô số nghiệm.

Bài tập

Bài 1) Giải hệ phương trình

$ (a) \begin{cases} x_1 + 2x_2 + x_3 + 2x_4 = 0 \\ 2x_1 + 4x_2 + x_3 + 3x_4 = 0 \\ 3x_1 + 6x_2 + x_3 + 4x_4 = 0 \end{cases} (e) \begin{bmatrix} 0 & 1 & 1 & 3 \\ 3 & 5 & 9 & -2 \\ 1 & 2 & 3 & 3 \end{bmatrix}. $

DS (-5 - $\alpha$, 5 + $2\alpha$, $\alpha)$.

DS: $(-2\alpha$ - $\beta$, $\alpha$, $-\beta$, $\beta)$

DS: (-43, 11, 8)

$ (b) \begin{vmatrix} 1 & 5 & 2 \\ -1 & -4 & 1 \\ 1 & 3 & -3 \end{vmatrix} \begin{vmatrix} 1 \\ 6 \\ -9 \end{vmatrix}. $

$ (f) \begin{bmatrix} 0 & 3 & -6 & 6 & 4 & -5 \\ 3 & -7 & 8 & -5 & 8 & 9 \\ 3 & -9 & 12 & -9 & 6 & 15 \end{bmatrix} $

DS: (18, -5, 4)

DS: (-24 + $2\alpha$ - $3\beta$, -7 + $2\alpha$ - $2\beta$, $\alpha$, $\beta$, 4)

$ (c) \begin{bmatrix} 1 & 5 & 2 \\ 0 & 4 & -7 \\ 0 & 0 & 5 \end{bmatrix} \begin{bmatrix} -6 \\ 2 \\ 0 \end{bmatrix}. DS: $

$ (g) \begin{bmatrix} 1 & 1 & 1 & -1 & 2 \\ 2 & 1 & 3 & 0 & 1 \\ 3 & 4 & 2 & -2 & 5 \\ 2 & 3 & 1 & -1 & 3 \end{bmatrix}. \text{DS:}(\frac{1}{3} - 2\alpha, \frac{1}{3} + \alpha) $

$(\frac{-17}{2}$, $\frac{1}{2}$, 0)

$ (d) \begin{bmatrix} 1 & 1 & -1 & 0 \\ 0 & 1 & -2 & 5 \end{bmatrix}. $

$\alpha$, $\alpha$, $-\frac{4}{2})$.

Bài 2) Tìm tất cả các giá trị của m để hệ sau có nghiệm

$ (a) \begin{bmatrix} 1 & 1 & 1 \ 2 & 3 & 1 \ 3 & 4 & m \end{bmatrix} \begin{bmatrix} 1 \ 4 \ m \end{bmatrix}. DS m \neq 2.(b) \begin{bmatrix} m & 1 & 1 \ 1 & m & 1 \ 1 & 1 & m \end{bmatrix} \begin{bmatrix} 1 \ m \ m \end{bmatrix}. DS m \neq -2. $

Bài 3) Tìm m để hệ sau có nghiệm duy nhất

$ (a) \begin{bmatrix} 2 & 3 & 1 & 4 \ 1 & -1 & 0 & m \ -2 & m & 1 & 4 \end{bmatrix} \begin{bmatrix} 0 \ 2 \ m^2 \end{bmatrix}. DS: \nexists m. $

$ (b) \begin{bmatrix} 1 & 1 & 1 & 1 \\ 2 & 1 & 3 & -1 \\ 3 & 4 & 2 & 0 \\ -2 & -1 & 0 & m \end{bmatrix} \begin{bmatrix} 1 \\ 2 \\ 6 \\ m-1 \end{bmatrix}. \forall m \in R. $



# Chương 4

Nội dung

• Dịnh nghĩa và ví dụ

• Độc lập tuyến tính - phụ thuộc tuyến tính

$\bullet$ Hạng của họ véc tơ

· Cơ sở và số chiều

$\bullet$ Tọa độ véc tơ

• Không gian con

• Tổng giao 2 không gian con

### Dịnh nghĩa và ví dụ

## 4.1 Dịnh nghĩa và ví dụ

### Định nghĩa 4.1 (Không gian véc tơ) Cho V là tập hợp khác rỗng và 2 phép toán: cộng 2 véc tơ và nhân

véc tơ với một số thỏa mãn 8 tiên đề sau

v) $\alpha$, $\beta \in$ K : $(\alpha$ + $\beta)x = \alpha$ x + $\beta$ x

i) $x+y=y+x$

ii) (x + y) + z $=$ x + (y + z)

vi) $\alpha \in$ K : $\alpha(x+y) = \alpha$ x + $\alpha$ y

iii) $\exists$ 0 $\in$ V : x + 0 $=$ x

vii) $(\alpha \beta)x = \alpha(\beta$ x)

iv) $\forall$ x $\in$ V, $\exists$ (-x) $\in$ V : x + (-x) $=$ 0

viii) 1.x $=$ x

Khi đó, ta nói V là một không gian véc tơ.

Chi $\circ:$

Đây là khái niệm được mở rộng từ khái niệm véc tơ ở phổ thông.

Tập các véc tơ trong mặt phẳng (hoặc không gian) có gốc O là một không gian véc tơ.

Tính chất

i) Véc tơ không là duy nhất. $<br/>ii)$ Véc tơ đối $<math display="inline">(-x) của<math display="inline">x$ là duy nhất.

iii) $0.\vec{x} = \vec{0}$, $\forall$ x $\in$ V iv) $\alpha.\vec{0} = \vec{0}$, $\forall \alpha \in$ K v) -x $=$ -1.x, $\forall$ inV

Vi du 4.1



1. Tập $V_1 = \{(x_1$, $x_2$, $x_3)|x_i \in$ R; i $=$ 1, 2, $3\}$ với phép toán cộng 2 véc tơ và nhân véc tơ với số thực thông

thường là một không gian véc tơ trên R. Ký hiệu là $R^3$.

Tương tự, ta có không gian $R^2$, $R^3$, $R^4$, $\ldots$, $R^n$, $\ldots$

2. Tập $V_2 = \{ax^2$ + bx + c | a, b, c $\in R\}$ với phép toán thông thường đối với đa thức là một không gian véc

tơ. Ký hiệu là $P_2[x]$.

Tương tự, ta có không gian $P_3[x]$, $P_4[x]$, $\ldots$, $P_n[x]$, $\ldots$

$ 3. Tập V_3 = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} | a, b, c, d \in R \right\} với phép toán thông thường đối với ma trận là một không gian véc $

tơ. Ký hiệu là $M_2[R]$.

Tương tự, ta có các không gian $M_{m \times n}[R]$, $M_{m \times n}[R]$ các ma trận cỡ m $\times$ n trong thực và phức.

4. Tập $V_4 = \{(x_1$, $x_2$, $x_3)|x_i \in$ R $\wedge x_1$ + $2x_2$ - $3x_3 = 0\}$ với phép toán đối với véc tơ thông thường là một

không gian véc tơ.

Chú ý: Có nhiều cách định nghĩa phép toán để cho các tập hợp trên là một không gian véc tơ, miễn

là thỏa 8 tiên đề của không gian trên.

Độc lập tuyến tính - phụ thuộc tuyến tính

## 4.2 Độc lập tuyến tính - phụ thuộc tuyến tính

### Dịnh nghĩa 4.2 Trong không gian véc tơ V, cho tập hợp con gồm m véc tơ M = \{x_1, x_2, \ldots, x_m\}

• Véc tơ x gọi là tổ hợp tuyến tính của M nếu $\exists \alpha_1$, $\alpha_2$, $\ldots$, $\alpha_m \in$ K thỏa

x $= \alpha_1 x_1$ + $\alpha_2 x_2$ + $\cdots$ + $\alpha_m x_m$

$\bullet \exists \alpha_1$, $\alpha_2$, $\ldots$, $\alpha_m$ không đồng thời bằng 0 thỏa

$\alpha_1 x_1$ + $\alpha_2 x_2$ + $\cdots$ + $\alpha_m x_m =$ 0 $\Longrightarrow$ M phy thuộc tuyến tính.

$\bullet$ M gọi là độc lập tuyến tính nếu nó không PTTT. Tức là

$\alpha_1 x_1$ + $\alpha_2 x_2$ + $\cdots$ + $\alpha_m x_m =$ 0 $\longrightarrow \alpha_1 = \alpha_2 = \cdots = \alpha_m =$ 0.

Nói cách khác:

M PTTT nếu có một THTT không tầm thường bằng không.

M ĐƯT nếu nó chỉ có duy nhất một THTT bằng không là tổ hợp tầm thường $(\alpha_k =$ 0, $\forall$ k).

Ví dụ 4.2 Trong $R^3$, cho họ véc tơ M $= \{(1$, 1, 1), (2, 1, 3), (1, 2, $0)\}$.

a) Véc tơ x $=$ (2, -1, 3) có là tổ hợp tuyến tính của M hay không?

b) M DLTT hay PTTT?

Bài làm

a) Xét x $= \alpha(1;$ 1; 1) + $\beta(2;$ 1; 3) + $\gamma(1;$ 2; 0) $\Longleftrightarrow$ (2; -1; 3) $= (\alpha$ + $2\beta$ + $\gamma; \alpha$ + $\beta$ + $2\gamma; \alpha$ + $3\beta)$

$ \Leftrightarrow \begin{cases} \alpha + 2\beta + \gamma = 2 \\ \alpha + \beta + 2\gamma = -1 \\ \alpha + 3\beta = 3 \end{cases}, (A|b) = \begin{bmatrix} 1 & 2 & 1 \\ 1 & 1 & 2 \\ 1 & 3 & 0 \end{bmatrix} \begin{bmatrix} 2 \\ -1 \\ 3 \end{bmatrix} \Longrightarrow r(A) = 2 < r(A|b) = 3. $

Hệ vô nghiệm, tức là không tồn tại $\alpha\beta$, $\gamma$. Vậy x không là THTT của M.



b) Xét tổ hợp bằng 0

$\alpha(1;1;1)$ + $\beta(2;1;3)$ + $\gamma(1;2;0) =$ 0 $\Longleftrightarrow (\alpha$ + $2\beta$ + $\gamma; \alpha$ + $\beta$ + $2\gamma; \alpha$ + $3\beta) =$ 0

$ \iff \begin{cases} \alpha+2\beta+\gamma=0\\ \alpha+\beta+2\gamma=0\\ \alpha+3\beta=0 \end{cases}, A=\begin{pmatrix} 1 & 2 & 1\\ 1 & 1 & 2\\ 1 & 3 & 0 \end{pmatrix} \Longrightarrow |A|=0 $

Hệ vô số nghiệm nên tồn tại nghiệm không tầm thường, do đó M PTTT.

Cho tập M $= \{x_1$, $x_2$, $\ldots$, $x_m\}$ và véc tơ x

$\alpha_1 x_1$ + $\alpha_2 x_2$ + $\cdots$ + $\alpha_m x_m =$ 0 $\Longleftrightarrow$ AX $=$ 0

Hệ có nghiệm duy nhất X $=$ 0 $\implies$ M DLTT.

Hệ có nghiệm khác không $\Rightarrow$ M PTTT.

$\alpha_1 x_1$ + $\alpha_2 x_2$ + $\cdots$ + $\alpha_m x_m =$ x $\Longleftrightarrow$ AX $=$ b

Hệ có nghiệm $\Rightarrow$ x là THTT của M.

Hệ vô nghiệm $\Rightarrow$ x không là THTT của M.

Ví dụ 4.3 Trong không gian véc tơ V, cho họ M $= \{x$, y, 2x + 3y, $z\}$.

a) Véc tơ 2x + 3y có là THTT của x, y, z hay không?

b) M DLTT hay PTTT?

Bài làm

a) Chọn $\alpha =$ 2, $\beta =$ 3, $\gamma =$ 0: 2x + 3y $=$ 2.x + 3.y + 0.z $\implies$ 2x + 3y là THTT của x, y, z.

b) Chọn $\alpha_1 =$ 2, $\alpha_2 =$ 3 $\alpha_3 =$ -1, $\alpha_4 =$ 0: 2 $\cdot$ x + 3 $\cdot$ y - 1. (2x + 3y) + 0 $\cdot$ z $=$ 0 $\implies$ M PTTT.

Ví dụ 4.4 Trong không gian véc tơ V, cho $\{x$, y, $z\}$ DLTT.

Hãy chứng tỏ M $= \{x$ + y + 2z, 2x + 3y + z, 3x + 4y + $z\}$ DLTT.

Bài làm

Xét một tổ hợp bằng không của M:

$\alpha(x+y+2z)+\beta(2x+3y+z)+\gamma(3x+4y+z)=0 \Longleftrightarrow (\alpha+2\beta+3\gamma)x+(\alpha+3\beta+4\gamma)y+(2\alpha+\beta+1\gamma)z=0$.

$ Vì x, y, z DLTT nên \begin{cases} \alpha + 2\beta + 3\gamma = 0 \\ \alpha + 3\beta + 4\gamma = 0 \\ 2\alpha + \beta + 1\gamma = 0 \end{cases} \Longleftrightarrow \begin{cases} \alpha = 0 \\ \beta = 0 \\ \gamma = 0 \end{cases}. Vậy M ĐLTT. $

Ví dụ 4.5 Trong không gian V, cho $\{x$, $y\}$ DLTT. Các tập hợp sau DLTT hay PTTT?

a) $M_1 = \{2x$, $3y\}.b) M_2 = \{x$ + y, 2x + $3y\}.c) M_3 = \{x$ + y, x - y, 2x + $3y\}$.

$\Deltaane$ (b) DLTT. (b) DLTT. (c) PTTT.

Ví dụ 4.6 Trong không gian V, cho $\{x$, $y\}$ DLTT và z không là THTT của $\{x$, $y\}$. Chứng tổ $\{x$, y, $z\}$

DLTT.

Bài làm

Xét $\alpha$ x + $\beta$ y + $\gamma$ z $=$ 0. Nếu $\gamma \neq$ 0 thì z $= -\frac{\alpha}{\beta}x$ - $\frac{\beta}{\gamma}y$, mâu thuẫn với giả thiết, suy ra $\gamma =$ 0.

Khi đó $\alpha$ x + $\beta$ y $=$ 0 $\xrightarrow{x,y \text{ DLTT}} \alpha = \beta =$ 0. Vậy $\{x$, y, $z\}$ ĐLTT.



Dấu hiệu ĐLTT-PTTT

• Nếu họ M chứa véc tơ không thì PTTT.

• Trong họ M, có một véc tơ là THTT của các véc tơ còn lại thì M PTTT.

• Thêm một số véc tơ vào họ PTTT, ta thu được 1 họ PTTT.

$\bullet$ Bốt đi một số véc tơ của họ DLTT, ta thu được 1 họ DLTT.

Bố đề cơ bản

Cho họ véc tơ gồm m véc tơ M $= \{x_1$, $x_2$, $\ldots$, $x_m\}$.

Cho họ véc tơ gồm n véc tơ N $= \{y_1$, $y_2$, $\ldots$, $y_n\}$.

Nếu mỗi véc tơ $y_k$ của N là THTT của M và n $>$ m thì N PTTT.

Ví dụ 4.7 Trong không gian véc tơ V, tập N $= \{2x$ + y, x + y, 3x - $2y\}$ DLTT hay PTTT?

Các véc tơ của N là THTT của M $= \{x$, $y\}$ và số véc tơ của N lớn hơn số véc tơ của M nên N PTTT.

Ví dụ 4.8 Trong KGVT V, cho M $= \{x$, y, $z\}$, N $= \{x$ + y + z, 2x + 3y - z, 3x + 4y + $z\}$. Chứng minh rằng

a) Nếu M DLTT thì N DLTT.

b) $N\acute{e}u$ N DLTT thì M DLTT.

Bài làm

a) Xét tổ hợp bằng 0 của N:

$\alpha(x+y+z)+\beta(2x+3y-z)+\gamma(3x+4y+z)=0 \Longleftrightarrow (\alpha+2\beta+3\gamma)x+(\alpha+3\beta+4\gamma)y+(\alpha-\beta+\gamma)z=0$

$ \xrightarrow{M \text{ DLTT}} \begin{cases} \alpha + 2\beta + 3\gamma = 0 \\ \alpha + 3\beta + 4\gamma = 0 \\ \alpha - \beta + \gamma = 0 \end{cases} \Longleftrightarrow \begin{cases} \alpha = 0 \\ \beta = 0 \\ \gamma = 0 \end{cases}. Vậy N ĐLTT. $

b) Dùng phản chứng, giả sử M PTTT. Khi đó có 1 véc tơ là THTT của các véc tơ còn lại.

Không mất tính tổng quát, ta giả sử z là THTT của x, y.

Ta có các véc tơ của N là THTT của M và cũng là THTT của $\{x$, $y\}$.

Số véc tơ của N lớn hơn số véc tơ của $\{x$, $y\}$. Theo bổ đề cơ bản, N PTTT, mâu thuẫn với giả thiết.

Hạng của họ véc tơ

## 4.3 Hạng của họ véc tơ

Dinh nghĩa 4.3 Cho họ véc tơ M $= \{x_1$, $x_2$, $\ldots$, $x_m$, $\ldots\} \subset$ V.

Ta nói hạng của M là $k_0$ nếu tồn tại $k_0$ véc tơ DLTT của

M và mọi tập con hơn $k_0$ véc tơ của M luôn PTTT.

Hạng của họ M là số tối đại các vécto độc lập tuyến tính của M.

Ví dụ 4.9 Trong KGVT V, cho M $= \{x$, $y\}$ DLTT. Tìm hạng của các họ véc tơ sau:

a) $M_1 = \{2x$, $3y\}$

b) $M_2 = \{x$, y, 2x + $3y\}$ c) $M_3 = \{x$, y, 2x + 3y, $0\}$.

Bài làm

a) Kiếm tra $\{2x$, $3y\}$ DLTT. Do đó $r(M_1) =$ 2.

b) 2x + 3y $=$ 2 $\cdot$ x + 3 $\cdot$ y $\Longrightarrow M_2$ PTTT và $\{x$, $y\}$ DLTT $\Longrightarrow r(M_2) =$ 2.



c) $M_3$ chứa véc tơ 0 nên PTTT. Dễ thấy 4 họ con gồm 3 véc tơ của $M_3$ đều PTTT.

Có 1 họ 2 véc tơ ĐLTT là $\{x$, $y\}$. Vậy $r(M_3) =$ 2.

Tính chất hạng của họ véc tơ

Hạng của họ véctơ M không đổi nếu ta nhân một véctơ

$\ket{1}$

của M với một số khác không.

Cộng vào một véctơ của họ M, một véctơ khác đã được

$\overline{11})$

nhân với một số thì hạng không thay đổi.

iii) Thêm vào họ M vécto x là tổ hợp tuyến tính của M thì

hạng không thay đổi.

iv) Bốt đi 1 véc tơ của M là THTT của các véc tơ khác thì

hạng không thay đổi.

Ví dụ 4.10 Cho họ véc tơ M $= \{(1;$ 1; 1; 0), (1; 2; 1; 1), (2; 3; 2; 1), (1; 3; 1; $2)\}$.

Bài làm

Ta có (2; 3; 2; 1) $=$ (1; 1; 1; 0) + (1; 2; 1; 1), (1; 3; 1; 2) $=$ -(1; 1; 1; 0) + 2(1; 2; 1; 1) $\implies$ r(M) $= r\{(1;$ 1; 1; 0), (1; 2; 1; $1)\}$.

Hơn nữa, vì $\{(1;1;1;0),(1;2;1;1)\}\text{ DLTT}$ nên $r(M)=2$.

### Dịnh lý về hạng Cho A là ma trận cỡ m \times n trên K.

• r(A) bằng với hạng của họ véc tơ hàng.

• r(A) bằng với hạng của họ véc tơ cột.

Ví dụ 4.11 Tìm hạng của hai họ véc tơ

a) M $= \{(1;$ 2; 1), (2; -1; 7), (1; 3; 0), (1; 2; $1)\}\$ và N $= \{(1;$ 2; 1; 1;), (2; -1; 3; 2), (1; 7; $01)\}\$.

b) P $= \{(1;$ 1; 1; 0), (1; 1; -1; 1), (2; 3; 1; 1), (3; 4; 0; $2)\}$.

Bài làm

$ a) Xét A = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & -1 & 3 & 2 \\ 1 & 2 & 0 & 1 \end{pmatrix} có họ véc tơ cột là M và họ véc tơ hàng là N. Do đó r(M) = r(N) = r(A) = 2. $

b) Hạng của P bằng hạng của ma trận

$ B = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 1 \\ 2 & 3 & 1 & 1 \\ 3 & 4 & 0 & 2 \end{pmatrix}. Vì r(B) = 2 nên r(P) = 2. $

Tính chất cho họ véc tơ M và véc tơ x

• Hạng M bằng số véc tơ thì M DLTT.

• Hạng M bé hơn số véc tơ thì M PTTT.

r(M, x) $=$ r(M) thì x là THTT của M.

Ví du 4.12 Xét sự DLTT của họ véc tơ sau



a) M $= \{(1;$ 1; 1), (2; 1; 3), (1; 2; $0)\}$.

b) N $= \{x^2$ + x + 1, $2x^2$ + 3x + 2, 2x + $1\}$.

$ c)\ P=\left\{\begin{pmatrix}1&1\\1&0\end{pmatrix},\begin{pmatrix}2&1\\1&-1\end{pmatrix},\begin{pmatrix}3&4\\0&1\end{pmatrix},\begin{pmatrix}1&3\\-1&2\end{pmatrix}\right\}. $

d) Q $= \{(1$, 1, 0), (1, 2, 1), (m, 0, $1)\}$.

Bài làm

$ a) r(M) = r\begin{pmatrix} 1 & 1 & 1 \\ 2 & 1 & 3 \\ 1 & 2 & 0 \end{pmatrix} = 2 \Longrightarrow M PTTT (vì hạng bé hơn số véc tơ). $

$ b) r(N) = r\begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & 2 \\ 0 & 2 & 1 \end{pmatrix} = 3 \Longrightarrow N DLTT (vì hạng bằng số véc tơ). $

$ c) r(P) = r \begin{pmatrix} 1 & 1 & 1 & 0 \\ 2 & 1 & 1 & -1 \\ 3 & 4 & 0 & 1 \end{pmatrix} = 4 \Longrightarrow P DLTT. $

$ \begin{pmatrix} 1 & 3 & -1 & 2 \end{pmatrix} $

$ d) r(Q) = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 2 & 1 \\ m & 0 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & -m & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & m+1 \end{pmatrix} $

Nếu m $=$ -1 $\Longleftrightarrow$ r(Q) $=$ 2 thì Q PTTT.

Nếu m $\neq$ -1 $\Longleftrightarrow$ r(Q) $=$ 3 thì Q DLTT.

Cơ sở và số chiều

## 4.4 Cơ sở và số chiều

Tập sinh Cho M $= \{x_1$, $x_2$, $\ldots$, $x_m$, $\ldots\} \subset$ V.

M gọi là tập sinh của V nếu mọi véc tơ x của V đều

là THTT của M. Ta viết

V $=$ M $\geq -< x_1$, $x_2$, $\ldots$, $x_m >$

Ta còn nói M sinh ra V hay V được sinh bởi M.

Ví dụ 4.13 Xét xem các tập sau có là tập sinh trong $R^3$ hay không?

a) M $= \{(1;$ 1; 1), (1; 2; 1), (2; 3; $1)\}$.

b) M $= \{(1$, 1, 1), (1, 2, 3), (3, 2, $1)\}\$

Bài làm

a) $\forall$ x $= (x_1$, $x_2$, $x_3) \in R^3$. Giả sử x $= \alpha(1$, 1, 1) + $\beta(1$, 2, 1) + $\gamma(2$, 3, 1)

$ \Longleftrightarrow \begin{cases} \alpha + \beta + 2\gamma = x_1 \\ \alpha + 2\beta + 3\gamma = x_2 \\ \alpha + \beta + \gamma = x_3 \end{cases}, |A| = \begin{vmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 1 & 1 & 1 \end{vmatrix} = -1 \neq 0. $

Hệ Cramer nên có nghiệm $\forall$ x $\in R^3$. Do đó x là THTT của M.

Vậy M là tập sinh của $R^3$.



b) $\forall$ x $= (x_1; x_2; x_3) \in R^3$. Giả sử x $= \alpha(1;$ 1; 1) + $\beta(1;$ 2; 3) + $\gamma(3;$ 2; 1)

$ \iff \begin{cases} \alpha+\beta+3\gamma=x_1\\ \alpha+2\beta+2\gamma=x_2\\ \alpha+3\beta+\gamma=x_3 \end{cases} \iff \begin{bmatrix} 1 & 1 & 3 & | & x_1 \\ 1 & 2 & 2 & | & x_2 \\ 1 & 3 & 1 & | & x_3 \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 1 & 3 & | & x_1 \\ 0 & 1 & -1 & | & x_2-x_1 \\ 0 & 0 & 0 & | & x_3+x_1-2x_1 \end{bmatrix} $

Với $x_3$ + $x_1$ - $2x_2 \neq$ 0 thì hệ vô nghiệm, nghĩa là tồn tại x (ví dụ như (1,0,0)) không là THTT của M.

Vậy M không là tập sinh của $R^3$.

Ví dụ 4.14 Tập M $= \{x^2$ + x + 1, $2x^2$ + 3x + 1, $x^2$ + $2x\}$ có là tập sinh của $P_2[x]$ hay không?

Bài làm

$\forall$ p(x) $= ax^2$ + bx + c $\in P_2[x]$ : p(x) $= \alpha(x^2$ + x + 1) + $\beta(2x^2$ + 3x + 1) + $\gamma(x^2$ + 2x)

$ \iff \begin{cases} \alpha+2\beta+\gamma = a \\ \alpha+3\beta+2\gamma = b \\ \alpha+\beta = c \end{cases} \iff \begin{bmatrix} 1 & 2 & 1 & a \\ 1 & 3 & 2 & b \\ 1 & 1 & 0 & c \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 2 & 1 & a \\ 0 & 1 & 1 & b-a \\ 0 & 0 & 0 & b+c-2a \end{bmatrix}. $

Với b + c - 2a $\neq$ 0 thì hệ vô nghiệm. Vậy M không là tập sinh của $P_2[x]$.

Ví dụ 4.15 Cho M $= \{x$, y, $z\}$ là tập sinh của KGVTV. Tập nào sau đây là tập sinh của V?

b) $M_2 = \{x$, x+y, $x-y\}$.

a) $M_1 = \{2x$, x+y, $z\}$.

Bài làm

a) $Vì<math display="inline">Mlà$ tập sinh của $<math display="inline">Vnên <math display="inline">\forall$ v $\in$ V: v $= \alpha$ x + $\beta$ y + $\gamma$ z

$\iff$ v $= \frac{\alpha$ - $\beta}{2}$. 2x + $\beta$. (x + y) + $\gamma$. z. Vì v là THTT của $M_1$ nên $M_1$ là tập sinh của V.

b) Nếu z là THTT của x, y. Khi đó ta chứng minh $M_2$ là tập sinh của V. (??)

Nếu z không là THTT của x, y. Khi đó z ta chứng minh được z không là THTT của $M_2$. (??)

Do đó $M_2$ không là THTT của V.

Cơ sở và số chiều: Cho M $= \{x_1$, $x_2$, $\ldots$, $x_m$, $\ldots\} \subset$ V

M sinh ra V | + | M - DLTT | $\Longrightarrow$ | M - là cơ sở |

Cơ sở có n véc tơ $\Rightarrow$ Số chiều của V là n: dim(V) $=$ n

$<math display="inline">V$ không có tập sinh hữu hạn thì $<math display="inline">Vgọi$ là KGVT vô hạn chiều.

Ví dụ 4.16 Cho M $= \{x$, y, $z\}$ là cơ sở của V. Xét xem tập nào sau đây là tập sinh, cơ sở?

a) $M_1 = \{2x$ + y + z, x + 2y + z, x + y + $z\}$. b) $M_2 = \{2x$, 3y, z, x + y + $z\}$.

Bài làm

a) 1) Chứng tỏ $M_1$ là tập sinh của V. 2) Chứng tỏ $M_1$ DLTT.(?)

Suy ra $M_1$ là cơ sở của V.

b) Chứng tỏ $M_2$ là tập sinh của V.(??).

Dễ thấy $M_2$ PTTT. Do đó $M_2$ là tập sinh nhưng không là cơ sở của V.

Dinh lý cơ sở Cho V là KGVT hữu hạn chiều

$\bullet$ V có vô số cơ sở.

• Số véc tơ trong mỗi cơ sở đều bằng nhau.



Cơ sở chính tắc

i) $dim(R^n) =$ n và cơ sở chính tắc (cơ sở đơn giản nhất) là

E $= \{(1;$ 0; $\ldots;$ 0), (0; 1; $\ldots;$ 0), $\ldots$, (0; 0; $\ldots; 1)\}$.

ii) $dim(P_n[x]) =$ n + 1 và cơ sở chính tắc là

E $= \{x^n$, $x^{n-1}$, $\ldots$, x, $1\}$.

iii) $dim(M_n[R]) = n^2$ và cơ sở chính tắc là

$ E = \left\{ \begin{pmatrix} 1 & 0 & \ldots & 0 \\ 0 & 0 & \ldots & 0 \\ \end{pmatrix} ~~, \begin{pmatrix} 0 & 1 & \ldots & 0 \\ 0 & 0 & \ldots & 0 \\ \ldots & \ldots & \ldots & \ldots \end{pmatrix} ~~, \ldots \right\} $

Tính chất Cho dim(V) $=$ n

• Mọi tập con nhiều hơn n véc tơ thì PTTT.

• Mọi tập con ít hơn n véc tơ không sinh ra V.

• Mọi tập con DLTT có đúng n véc tơ là cơ sở.

• Mọi tập sinh có đúng n véc tơ là cơ sở.

• Mọi tập có hạng bằng n là tập sinh.

Ví dụ 4.17 Kiểm tra tập sinh - cơ sở trong $R^3$.

a) M $= \{(1;$ 1; 1), (2; 3; 1), (3; 1; $0)\}$.

b) N $= \{(1;$ 1; 1), (2; 0; 1), (1; 1; 0), (1; -2; $1)\}$.

Bài làm

a) M có 3 véc tơ bằng số chiều của $R^3$.

$ r(M) = r\begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & 1 \\ 3 & 1 & 0 \end{pmatrix} = 3 \Longrightarrow M là cơ sở của R^3. $

b) N có 4 véc tơ trong không gian 3 chiều nên PTTT.

$ r(N) = r \begin{pmatrix} 1 & 1 & 1 \\ 2 & 0 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix} = 3 \Longrightarrow N là tập sinh của R^3. $

Ví dụ 4.18 Kiểm tra tập M $= \{x^2$ + x + 1, $2x^2$ + x + 1, $x^2$ + 2x + $2\}$ có là cơ sở của $P_2[x]?$

Bài làm

M có 3 véc tơ, bằng số chiều của $P_2[x]$. M là cơ sở khi và chỉ khi r(M) $=$ 3.

$ r(M) = r\begin{pmatrix} 1 & 1 & 1 \\ 2 & 1 & 1 \\ 1 & 2 & 2 \end{pmatrix} = 2. \Longrightarrow M không là cơ sở của P_2[x]. $



Tọa độ véc tơ

## 4.5 Tọa độ véc tơ

Dinh nghĩa 4.4 Cho E $= \{e_1$, $e_2$, $\ldots$, $e_n\}$ là cơ sở sắp thứ tự của K-KGVT V.

Bộ số $(x_1$, $x_2$, $\ldots$, $x_n)$ gọi là tọa độ véc tơ x trong cơ sở E. Ký hiệu

$ [x]_E = \begin{pmatrix} x_1 \\ x_2 \\ \dots \\ x_n \end{pmatrix} \Longleftrightarrow x = x = x_1e_1 + x_2e_2 + \dots + x_ne_n. $

Ví dụ 4.19 Cho E $= \{x^2$ + x + 1, $x^2$ + 2x + 1, $x^2$ + x + $2\}$ là cơ sở của $P_2[x]$.

b) Cho q(x) $= x^2$. Tim $[q(x)]_E$.

$ a) Tìm p(x) biết [p(x)]_E = \begin{pmatrix} 3 \\ -2 \\ 5 \end{pmatrix}. $

Bài giải

$ a) [p(x)]_E = \begin{pmatrix} 3 \\ -2 \\ 5 \end{pmatrix} \Longleftrightarrow p(x) = 3(x^2 + x + 1) - 2(x^2 + 2x + 1) + 5(x^2 + x + 2) \Longleftrightarrow p(x) = -5x + 2. $

$ b) Giả sử [q(x)]_E = \begin{pmatrix} \alpha \\ \beta \\ \gamma \end{pmatrix} $

$\iff$ q(x) $= \alpha(x^2$ + x + 1) + $\beta(x^2$ + 2x + 1) + $\gamma(x^2$ + x + 2) $\iff x^2 = (\alpha$ + $\beta$ + $\gamma)x^2$ + $(\alpha$ + $2\beta$ + $\gamma)x$ + $(\alpha$ + $\beta$ + $2\gamma)$

$ \Leftrightarrow \begin{cases} \alpha+\beta+\gamma=1\\ \alpha+2\beta+\gamma=0\\ \alpha+\beta+2\gamma=0 \end{cases} \Leftrightarrow \begin{cases} \alpha=3\\ \beta=-1\\ \gamma=-1 \end{cases}. Vậy [q(x)]_E = \begin{pmatrix} 3\\ -1\\ -1 \end{pmatrix}. $

Tính chất tọa độ

$ Cho E là cơ sở của KGVT V: [x]_E = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} [y]_E = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix} $

$ i) x = y \Longleftrightarrow \begin{cases} x_1 = y_1 \\ x_2 = y_2 \\ \dots \\ x_n = y \end{cases} ii) [x + y]_E = \begin{pmatrix} x_1 + y_1 \\ x_2 + y_2 \\ \vdots \\ x_n + y_n \end{pmatrix} iii) [\alpha x]_E = \begin{pmatrix} \alpha x_1 \\ \alpha x_2 \\ \vdots \\ \alpha x_n \end{pmatrix} $

Ví dụ 4.20 Cho E $= \{(1$, 1, 1), (1, 1, 0), (1, 0, $1)\}\là$ cơ sở của $R^3$.

b) Cho x $=$ (3; 1; -2). Tim $[x]_E$.

$ a) Tim x, biết [x]_E = \begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix}. $

Bài làm

$ a) [x]_E = \begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix} \Longleftrightarrow x = -1(1; 1; 1) + 2(1; 1; 0) + 1(1; 0; 1) = (2; 1; 0) $

Ghi chú:

$ E.[x]_E = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} \xrightarrow{\text{viét lai}} x = (2; 1; 0). $



$ b) Giả sử [x]_E = \begin{pmatrix} \alpha \\ \beta \\ \gamma \end{pmatrix} \Longleftrightarrow x = \alpha(1; 1; 1) + \beta(1; 1; 0) + \gamma(1; 0; 1) $

$ \iff \begin{cases} \alpha+\beta+\gamma=3\\ \alpha+\beta=1\\ \alpha+\gamma=-2 \end{cases} \iff [x]_E=\begin{pmatrix} -4\\ 5\\ 2 \end{pmatrix} $

Ghi chú:

$ E.[x]_E = x^T \Longleftrightarrow [x]_E = E^{-1}x^T = \begin{pmatrix} -4 \\ 5 \\ 2 \end{pmatrix}. $

Dùng máy tính casio cho bài toán tọa độ

$ Co sở E = \{e_1, e_2, \dots, e_3\} \xrightarrow{\text{MT côt}} E = \begin{pmatrix} e_1 & e_2 & \dots & e_3 \end{pmatrix} $

$\boxed{x^T = E.[x]_E} \qquad \Longleftrightarrow \qquad \boxed{[x]_E = E^{-1}x^T}$

Ý nghĩa của tọa độ Cho E $= \{e_1$, $e_2$, $\ldots$, $e_n\}$ là cơ sở của KGVT V.

Mọi véc tơ của V đều biểu diễn qua E dưới dạng tọa độ.

Các phép toán tọa độ giống như các phép toán trong $R_n$.

$\implies$ tất cả các không gian n chiều đều coi là $R_n$.

Ví dụ 4.21 Tìm tọa độ của p(x) $= 3x^2$ + 4x - 1 trong cơ sở E $= \{x^2$ + x + 1, x + 1, 2x + $1\}$ trong $P_2[x]$.

Bài làm

$ Lập ma trận E = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix}. $

$ Tọa độ [p(x)]_E = E^{-1}[p(x)] = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix}^{-1} \cdot \begin{pmatrix} 3 \\ 4 \\ -1 \end{pmatrix} = \begin{pmatrix} 3 \\ -9 \\ 5 \end{pmatrix}. $

Ma trận chuyển cơ sở

## 4.6 Ma trận chuyển cơ sở

Dinh nghĩa 4.5 Cho 2 cơ sở của KGVT V: E $= \{e_1$, $e_2$, ..., $e_n\}$, E' $= \{e'_1$, $e'_2$, ..., $e'_n\}$. $\forall$ x $\in$ V : x $= x_1e_1$ + $x_2e_2$ + ... + $x_ne_n = x'_1e'_1$ + $x'_2e'_2$ + ... + $x'_ne'_n$. (1)

$\forall$ x $\in$ V: x $= x_1e_1$ + $x_2e_2$ + $\cdots$ + $x_ne_n = x'_1e'_1$ + $x'_2e'_2$ + $\cdots$ + $x'_ne'_n$.

$e'_1 = a_{11}e_1$ + $a_{21}e_2$ + $\cdots$ + $a_{n1}e_n$

$e'_2 = a_{12}e_1$ + $a_{22}e_2$ + $\cdots$ + $a_{n2}e_n$

$e'_n = a_{1n}e_1$ + $a_{2n}e_2$ + $\cdots$ + $a_{nn}e_n$

x $= x'_1(a_{11}e_1$ + $a_{21}e_2$ + $\cdots$ + $a_{n1}e_n)$ + $x'_2(a_{12}e_1$ + $a_{22}e_2$ + $\cdots$ + $a_{n2}e_n)$ + $\cdots$ + $x'_n(a_{12}e_1$ + $a_{22}e_2$ + $\cdots$ + $a_{n2}e_n)$.

$ Từ (1), ta suy ra \begin{pmatrix} x_1 \\ x_2 \\ \cdots \\ x_n \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \cdots & \cdots & \cdots & \cdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix} \begin{pmatrix} x'_1 \\ x'_2 \\ \cdots \\ x'_n \end{pmatrix}. $

$ Ma trận A = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \vdots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{pmatrix}gọi là ma trận chuyển cơ sở từ E sang E'. $



Ma trận chuyển cơ sở từ E sang E'

$ P = \begin{pmatrix} [e'_n]_E & [e'_n]_E & \cdots & [e'_n]_E \\ || & || & || & || \end{pmatrix} = E^{-1}E' \text{ (viét dang côt).} $

Có tính chất

$[x]_E = P[x]_{E}$.

Tính chất

$\bullet$ Ma trận chuyển cơ sở P khả nghịch.

• P chuyển cơ sở từ E sang E' thì $P^{-1}$ là ma trận chuyển cơ

sở từ E' sang E.

• Pchuyển cơ sở từ E sang E' và Q chuyển cơ sở từ E' sang

E'' thì PQ là ma trận chuyển cơ sở từ E sang E''.

Ví dụ 4.22 Trong $R^3$, cho 2 cơ sở E $= \{(1,1,1)$, (1,0,1), $(1,1,0)\}$ và E' $= \{(1,1,2)$, (1,2,1), $(1,1,1)\}$.

a) Tìm ma trận chuyển cơ sở từ E sang E' và ma trận chuyển cơ sở từ E' sang E.

b) Cho x $=$ (2, 1, 3). Tim $|x|_{E'}$ và $|x|_E$.

Bài làm

$ a) E = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}, E' = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 1 \\ 2 & 1 & 1 \end{pmatrix}. $

$ Ma trận chuyển cơ sở từ E sang E': P = E^{-1}E' = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 1 \\ 2 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 2 & 1 \\ 0 & -1 & 0 \\ -1 & 0 & 0 \end{pmatrix} $

$ Ma trận chuyển cơ sở từ <math display="inline">E' sang <math display="inline">E\colon Q = E'^{-1}E = P^{-1} = \begin{pmatrix} 0 & 0 & -1 \\ 0 & -1 & 0 \end{pmatrix}. $

$ b) Ta có [x]_{E'} = E'^{-1}x^T = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 1 \\ 2 & 1 & 1 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}. $

$ [x]_E = E^{-1}x^T = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}. $

$ Cách khác: [x]_E = P[x]_{E'} = \begin{pmatrix} 2 & 2 & 1 \\ 0 & -1 & 0 \\ -1 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}. $

Không gian con

## 4.7 Không gian con

### Dịnh nghĩa 4.6 Trong KGVT V, nếu tập con F với các phép toán trong V lập thành một KGVT thì ta

nói F là không gian con của V.

Dinh lý không gian con

Tập con khác rỗng F của KGVT V là một không gian con của V khi và

chỉ khi hai điều kiện sau thỏa

i) $\forall$ x, y $\in$ F : x + y $\in$ F. ii) $\forall$ x $\in$ F, $\alpha \in$ K : $\alpha$ x $\in$ F.



Ví dụ 4.23 Cho F $= \{(x_1; x_2; x_3) \in R^3$ | $x_1$ + $2x_2$ - $x_3 =$ 0 $\}$.

a) Chứng tỏ F là KG con của $R^3$.

b) Tìm cơ sở và số chiều của F.

Bài làm

a) Sinh viên tự kiểm tra 2 điều kiện trong định lý.

b) $\forall$ x $= (x_1; x_2; x_3) \in$ F $\Longleftrightarrow x_1$ + $2x_2$ - $x_3 =$ 0 $\Longleftrightarrow x_3 = x_1$ + $2x_2$.

x $= (x_1; x_2; x_3) =$ x $= (x_1; x_2; x_1$ + $2x_2) = x_1(1;$ 0; 1) + $x_2(0;$ 1; 2).

Suy ra E $= \{(1,0,1)$, $(0,1,2)\}\là$ tập sinh của F.

Kiếm tra E ĐLTT. Vậy E là cơ sở của F và $\dim(F) =$ 2.

Ví dụ 4.24 Cho F $= \{p(x) \in P_2[x]$ | p(1) $=$ 0 $\land$ p(2) $= 0\}$.

b) Tìm cơ sở và số chiều của F.

a) Chứng tỏ F là KG con của $R^3$.

a) Sinh viên tự kiểm tra 2 điều kiện trong định lý.

b) $\forall$ p(x) $= ax^2$ + bx + c $\in$ F $\Longleftrightarrow$ p(1) $=$ 0 $\land$ p(2) $=$ 0

$ \iff \begin{cases} a+b+c=0 \\ 4a+2b+c=0 \end{cases} \iff \begin{cases} a=\alpha \\ b=-3\alpha \\ c=2\alpha \end{cases} $

p(x) $= \alpha x^2$ - $3\alpha$ x + $2\alpha = \alpha(x^2$ - 3x + 2).

Suy ra E $= \{x^2$ - 3x + $2\}$ là tập sinh của F.

Hiến nhiên E DLTT. Vậy E là cơ sở của F và $\dim(F) =$ 1.

$ Ví dụ 4.25 Cho F = \left\{ A \in M_2[R] | A \begin{pmatrix} 1 & -1 \\ 2 & -2 \end{pmatrix} = 0 \right\}. $

a) Chứng tỏ F là KG con của $R^3$.

b) Tìm cơ sở và số chiều của F.

Bài làm

a) Sinh viên tự kiểm tra 2 điều kiện trong định lý.

$ b) \forall A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in F \Longleftrightarrow \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 2 & -2 \end{pmatrix} = 0 \Longleftrightarrow \begin{pmatrix} a+2b & -a-2b \\ c+2d & -c-2d \end{pmatrix} = 0 $

$ \iff \begin{cases} a+2b=0 \\ c+2d=0 \end{cases} \iff \begin{cases} a=-2b \\ c=-2d \end{cases} $

$ A = \begin{pmatrix} -2b & b \\ -2d & d \end{pmatrix} = b \begin{pmatrix} -2 & 1 \\ 0 & 0 \end{pmatrix} + d \begin{pmatrix} 0 & 0 \\ -2 & 1 \end{pmatrix}. $

$ Suy ra E = \left\{ \begin{pmatrix} -2 & 1 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ -2 & 1 \end{pmatrix} \right\} là tập sinh của F. $

Dễ thấy E ĐLTT. Vậy E là cơ sở của F và $\dim(F) =$ 2.

Dinh lý Cho M $= \{v_1$, $v_2$, $\ldots$, $v_p\} \subset$ V

Ký hiệu H $:=$ Span(M) $= {\alpha_1v_1$ + $\alpha_2v_2$ + $\cdots$ + $\alpha_pv_p} \forall \alpha_i \in R}$.

• H là một KGVT được sinh bởi S: H $= <$ M $>$.

$\bullet$ dim(H) $=$ r(M).

• x $\in$ H $\Longleftrightarrow$ x là THTT của M $\Longleftrightarrow$ r(S, x) $=$ r(M)



Ví dụ 4.26 Tìm cơ sở và số chiều của các không gian con sau

a) F $= \langle$ (1;1;1), (2;1;1), (3;1;1) $\rangle$.

b) F $= \langle x^2$ + x + 1, $2x^2$ + 3x - 1, $x^2$ + 2x - 2 $\rangle$.

$ c) F = \left\langle \begin{pmatrix} 1 & 1 \\ 2 & 1 \end{pmatrix}, \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}, \begin{pmatrix} 3 & 1 \\ -2 & 1 \end{pmatrix}, \begin{pmatrix} 1 & 0 \\ -2 & 0 \end{pmatrix} \right\rangle $

d) F $= \{(x_1; x_2; x_3; x_4) \in R^3$ | $x_1$ + $x_2$ + $x_3 =$ 0 $\land x_1$ - $x_2$ + $x_4 =$ 0 $\}$

Bài làm

$ a) A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 1 & 1 \\ 2 & 1 & 1 \end{pmatrix} \xrightarrow{b dsc} \begin{pmatrix} 1 & 1 & 1 \\ 0 & -1 & -1 \\ 0 & 0 & 0 \end{pmatrix} \Longrightarrow \dim(F) = r(A) = 2 và cơ sở của F là \{(1; 1; 1), (0; -1; -1)\}. $

$ b) A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & -1 \\ 1 & 2 & -2 \end{pmatrix} \xrightarrow{bdsc} \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & -3 \\ 0 & 0 & 0 \end{pmatrix} \implies \dim(F) = r(A) = 2 và cơ sở của F là \{x^2 + x + 1, x - 3\}. $

$ c) A = \begin{pmatrix} 1 & 1 & 2 & 1 \\ 2 & 1 & 0 & 1 \\ 3 & 1 & -2 & 1 \\ 1 & 0 & 0 & 0 \end{pmatrix} \xrightarrow{b dsc} \begin{pmatrix} 1 & 1 & 2 & 1 \\ 0 & -1 & -4 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \implies \dim(F) = 2 \text{ và cơ sở của } F \text{ là } \left\{ \begin{pmatrix} 1 & 1 \\ 2 & 1 \end{pmatrix}, \begin{pmatrix} 0 & -1 \\ -4 & -1 \end{pmatrix} \right\}. $

$ d) Giải hệ \begin{cases} x_1 + x_2 + x_3 = 0 \\ x_1 - x_2 + x_4 = 0 \end{cases} \Longleftrightarrow \begin{bmatrix} 1 & 1 & 1 & 0 \\ 1 & -1 & 0 & 1 \end{bmatrix} \begin{bmatrix} 0 \\ 0 \end{bmatrix} \Longrightarrow \begin{bmatrix} (1) & 1 & 1 & 0 \\ 0 & (-2) & -1 & 1 \end{bmatrix} \begin{bmatrix} 0 \\ 0 \end{bmatrix} $

Dăt $x_3 = 2\alpha$, $x_4 = 2\beta$, $\quad$ pt(2): $x_2 = \frac{1}{2}(-x_3$ + $x_4) = -\alpha$ + $\beta$, $\quad$ pt(1): $x_1 = -x_2$ - $x_3 = -\alpha$ - $\beta$

$\forall$ x $\in$ F $\Longleftrightarrow$ x $= (-\alpha$ - $\beta; -\alpha$ + $\beta; 2\alpha; 2\beta) = \alpha(-1;$ -1; 2; 0) + $\beta(-1;$ 1; 0; 2)

Suy ra E $= \{(-1$, -1, 2, 0), $\beta(-1$, 1, 0, $2)\}\là$ tập sinh của F.

Dễ thấy E ĐLTT. Vậy E là cơ sở của F và dim F $=$ 2.

Tìm cơ sở và số chiều không gian con

Trong $R^n$, cho không gian con F

TH 1) Cho tập sinh F $= \langle v_1$, $v_2$, $\ldots$, $v_m \rangle:$

$ Lập ma trận hàng A = \begin{pmatrix} v_1 \\ v_2 - \\ \cdots \end{pmatrix} \stackrel{b d s c}{\longrightarrow} bậc thang $

$\dim(F) =$ r(A) và cơ sở gồm các hàng khác 0 của ma trận bậc thang.

TH 2) Cho tập nghiệm của hệ thuần nhất AX $=$ 0

Giải hệ: $\left|\dim$ V + r(A) $= n\right|$ và cơ sở được suy ra từ nghiệm của hệ.



Ví dụ 4.27 Trong $R^3$, cho tập M $= \{(1$, 1, 1), (2 : 3 : 1), (1, 0, $2)\}$.

a) x $=$ (1, -2, 3) thuộc không gian con span(M) hay không?

b) Tim m $d\acute{e}$ x $=$ (1,0;m) $\in$ span(M).

Bài làm

a) x thuộc Kg con span(M) khi và chỉ khi x là THTT của M. Ta lập ma trận cột

$ [M|x] = \begin{vmatrix} 1 & 2 & 1 & 1 \\ 1 & 3 & 0 & -2 \\ 1 & 1 & 2 & 3 \end{vmatrix} \xrightarrow{bdsc} \begin{vmatrix} 1 & 2 & 3 & 1 \\ 0 & 1 & -1 & -3 \\ 0 & 0 & 0 & -1 \end{vmatrix} $

r(M) $=$ 2 $<$ r(M|x) $\Longrightarrow$ x $\notin$ span(M).

$ b) [M|x] = \begin{vmatrix} 1 & 2 & 1 & 1 \\ 1 & 3 & 0 & 0 \\ 1 & 1 & 2 & m \end{vmatrix} \xrightarrow{bdsc} \begin{vmatrix} 1 & 2 & 3 & 1 \\ 0 & 1 & -1 & -1 \\ 0 & 0 & 0 & m-2 \end{vmatrix} $

x $\in \notin$ span(M) $\Longleftrightarrow$ r(M) $=$ r(M|x) $\Longleftrightarrow$ m $=$ 2.

Tông giao hai không gian con

## 4.8 Tông giao hai không gian con

Dinh nghĩa 4.7 (Tổng giao 2 không gian con) Cho hai không gian con F và G của KGVTV.

Giao 2 không gian con

F $\cap$ G $= \{x \in$ V | x $\in$ F $\text{$ via $}$ x $\in G\}$.

Tổng 2 không gian con

F + G $= \{f$ + g | f $\in$ F $\text{$ via $}$ g $\in G\}$.

Tính chất

F $\cap$ G $\subset$ F, G $\subset$ F + G $\subset$ V.

Dinh lý F $\cap$ G và F + G là 2 không gian con của V và

$\dim(F \cap$ G) + $\dim(F$ + G) $= \dim$ F + $\dim$ G.

### Định nghĩa 4.8 (Tổng trực tiếp) Không gian con W gọi là tổng trực tiếp của 2 không gian con F và G,

ký hiệu F $\oplus$ G, nếu

ii) F $\cap$ G $= \{0\}$.

i) W $=$ F + G.

Dinh lý Cho W $=$ F $\oplus$ G. Khi đó mọi véc tơ x $\in$ W

được biểu diễn duy nhất dưới dạng

x $=$ f + g | f $\in$ F, g $\in$ G.

Tích chất tổng 2 không gian con

F $= \langle f_1$, $f_2$, $\ldots$, $f_n \rangle$ G $= \langle g_1$, $g_2$, $\ldots$, $g_m \rangle$

$\Rightarrow$ F + G $= \leq f_1$, $f_2$, $\dots$, $f_n$, $q_1$, $q_2$, $\dots$, $q_m >$



Ví dụ 4.28 Trong $R^3$, cho 2 không gian con

F $= \{(x_1$, $x_2$, $x_3) \in R^3$ | $x_1$ + $x_2$ - $2x_3 = 0\}$, $\quad$ G $= \{(x_1$, $x_2$, $x_3) \in R^3$ | $x_1$ - $x_2$ + $x_3 = 0\}$.

Tìm cơ sở và số chiều của F $\cap$ G và F + G.

Bài làm

a) Tìm cơ sở và số chiều của F $\cap$ G.

$\forall$ x $\in$ F $\cap$ G $\longleftrightarrow$ x $\in$ F $\land$ x $\in$ G

$ \Leftrightarrow \begin{cases} x_1 + x_2 - 2x_3 = 0 \\ x_1 - x_2 + x_3 = 0 \end{cases} \Leftrightarrow \begin{cases} x_1 = \alpha \\ x_2 = 3\alpha \\ x_3 = 2\alpha \end{cases} \Leftrightarrow x = (\alpha, 3\alpha, 2\alpha) = \alpha(1, 3, 2). $

Suy ra E $= \{(1,3,2)\}\là$ tập sinh của F $\cap$ G.

Hiến nhiên E DLTT do đó E là cơ sở của F $\cap$ G và $\dim(F \cap$ G) $=$ 1.

b) Tìm tập sinh của F và G.

F $= \langle$ (-1,1,0), (2,0,1) $\rangle$, G $= \langle$ (1,1,0), (-1,0,1) $\rangle \Longrightarrow$ F + G $= \langle$ (-1,1,0), (2,0,1), (1,1,0), (-1,0,1) $\rangle$

$ A = \begin{pmatrix} -1 & 1 & 0 \ 2 & 0 & 1 \ 1 & 1 & 0 \ -1 & 0 & 1 \end{pmatrix} \xrightarrow{bdsc} \begin{pmatrix} -1 & 1 & 0 \ 0 & 2 & 1 \ 0 & 0 & -1 \ 0 & 0 & 0 \end{pmatrix}. $

$\implies$ dim(F + G) $=$ r(A) $=$ 3 và co sở E $= {(-1;$ 1; 0), (0; 2; 1), (0; 0; $-1)}$.

Cách khác: ta có

$\dim(F \cap$ G) + $\dim(F+G) = \dim$ F + $\dim$ G $\Longrightarrow \dim(F+G) = \dim$ F + $\dim$ G - $\dim(F \cap$ G) $=$ 2+2-1 $=$ 3

$\Rightarrow$ F + G $\equiv R^3$, do đó có cơ sở là $\{(1;0;0)$, (0;1;0), $(0;0;1)\}$.

Ví dụ 4.29 Trong $R^3$, cho 2 không gian con F $= \{(x_1$, $x_2$, $x_3) \in R^3$ | $x_1$ + $x_2$ + $x_3 = 0\}$, G $= \langle$ (1, 0, 1), (2, 3, 1) $\rangle$.

Tìm cơ sở và số chiều của F $\cap$ G và F + G.

Bài làm

F + G tương tự như ví dụ trên. Ta tìm cơ sở và số chiều của F $\cap$ G.

$\forall$ x $\in$ F $\cap$ G $\Longleftrightarrow$ x $\in$ F $\land$ x $\in$ G.

x $\in$ G $\Longleftrightarrow$ x $= \alpha(1;$ 0; 1) + $\beta(2;$ 3; 1) $= (\alpha$ + $2\beta; 3\beta; \alpha$ + $\beta)$.

x $\in$ F $\Longleftrightarrow$ x thỏa điều kiện của F: $\alpha$ + $2\beta$ + $3\beta$ + $\alpha$ + $\beta =$ 0 $\Longleftrightarrow \alpha = -3\beta$.

x $= (\alpha$ + $2\beta; 3\beta; \alpha$ + $\beta) = (-\beta; 3\beta; -2\beta) = \beta(-1;$ 3; -2).

Dễ dàng suy ra E $= \{(-1$, 3, $-2)\}\là$ cơ sở của F $\cap$ G và dim(F $\cap$ G) $=$ 1.

Ví dụ 4.30 Trong $R^3$, cho 2 không gian con

F $= \langle f_1 =$ (1,0,1), $f_2 =$ (1,1,1) $\rangle$, G $= \langle g_1 =$ (1,1,0), $g_2 =$ (2,1,1) $\rangle$.

Tìm cơ sở và số chiều của F+G và $F\cap$ G.

Bài làm F + G làm tương tự ví dụ trên. Ta tìm cơ sở và số chiều của F $\cap$ G.

x $\in$ F $\cap$ G khi và chỉ khi x đồng thời là THTT của $f_1$, $f_2$ và $g_1$, $g_2:$

x $= x_1 f_1$ + $x_2 f_2 = x_3 g_1$ + $x_4 g_2 \Leftrightarrow x_1 f_1$ + $x_2 f_2$ - $x_3 g_1$ - $x_4 g_2 =$ 0.

$ Viết lại ở dạng ma trận \begin{bmatrix} 1 & 1 & -1 & -2 & 0 \\ 0 & 1 & -1 & -1 & 0 \\ 1 & 1 & 0 & -1 & 0 \end{bmatrix} \xrightarrow{bdsc} \begin{bmatrix} 1 & 1 & -1 & -2 & 0 \\ 0 & 1 & -1 & -1 & 0 \\ 0 & 0 & 1 & 1 & 0 \end{bmatrix}. $

Dặt $x_4 = \alpha \Longrightarrow x_3 = -x_4 = -\alpha$.

x $= x_3q_1$ + $x_4q_2 = -\alpha(1;$ 1; 0) + $\alpha(2;$ 1; 1) $= \alpha(1;$ 0; 1).

Dễ dang suy ra cơ sở của F $\cap$ G là $\{(1,0,1)\}\và \dim(F \cap$ G) $=$ 1.



Bài tập

Câu 1) Trong $R^4$, cho U $= \langle$ (1,2,1,1); (2,1,0,-2) $\rangle$ và V $= \langle$ (1,5,3,5); (3,0,-1,m) $\rangle$. Tìm m để U $\equiv$ V.

Câu 2) Trong $R^4$, cho V là tập nghiệm của hệ phương trình

$ \begin{cases}\nx_1 + x_2 - x_3 = 0 \\
2x_1 + 2x_2 + x_3 + x_4 = 0 \\
x_1 + x_2 + 2x_3 + mx_4 = 0\n\end{cases} $

(a) Tìm m để dim(V) lớn nhất.

(b) Tìm cơ sở và số chiều của V với m ở câu a.

Câu 3) Trong $R^4$, cho U $= \langle$ (1,2,1,0); (2,-1,1,1) $\rangle$ V $= \langle$ (1,1,-2,1); (2,0,4,m) $\rangle$

(a) Tìm m để dim(U $\cup$ V) lớn nhất.

(b) Tìm cơ sở và số chiều của U + V và U $\cup$ V.

Câu 4) Trong $R^4$, cho 2 không gian dưới dạng tập nghiệm của hệ phương trình

$ U : \left[ \begin{array}{ccc|ccc} 1 & 1 & 2 & 0 & 0 \\ -1 & 1 & -1 & 2 & 0 \end{array} \right], \qquad V : \left[ \begin{array}{ccc|ccc} 1 & 2 & 2 & 2 & 0 \\ -1 & 0 & -1 & m & 0 \end{array} \right] $

(a) Tìm m để dim(U + V) bé nhất.

(b) Tìm cơ sở và số chiều của U + V và U $\cup$ V.

Câu 5) Trong $R^4$, cho U $= \{(x_1$, $x_2$, $x_3$, $x_4) \in R^4$ : $x_1$ + $x_2$ - $x_3$ + $x_4 = 0\}$ Và V $= \langle$ (1, 2, 1, 2), (2, 1, 0, m) $\rangle$

(a) Tìm m để dim(U $\cup$ V) lớn nhất.

(b) Tìm cơ sở và số chiều của U + V và U $\cup$ V.



# Chương 5

Nội dung

Tích vô hướng của 2 véc tơ.

2) Bù vuông góc của không gian con.

3) Quá trình trực giao hóa Gram-Schmidt.

4) Hình chiếu vuông góc xuống không gian con.

Tích vô hướng của 2 véc tơ

## 5.1 Tích vô hướng của 2 véc tơ

### Dịnh nghĩa 5.1 (Tích vô hướng) Tích vô hướng trong R-kgvt V là một hàm thực sao cho mỗi cặp véctơ

u và v thuộc V, tương ứng với một số thực ký hiệu (u, v) thỏa 4 tiên đề sau:

iii) $(\forall \alpha \in$ K, $\forall$ u, v $\in$ V) : $(\alpha$ u, v) $= \alpha(u$, v).

i) $(\forall$ u, v $\in$ V) : (u, v) $=$ (v, u).

ii) $(\forall$ u, v, w $\in$ V) : (u + v, w) $=$ (u, w) + (v, w). $\forall$ u $\in$ V) : (u, u) $\geq$ 0; (u, u) $=$ 0 $\Longleftrightarrow$ u $=$ 0.

Không gian hữu hạn hạn chiều cùng với tính vô hướng trên gọi là không gian euclide.

Tích vô hướng chính tắc trên $R^n$

x $= (x_1; x_2; \ldots; x_n)$, y $= (y_1; y_2; \ldots; y_n)$

(x,y) $= x_1y_1$ + $x_2y_2$ + $\cdots$ + $x_ny_n$.

Tích vô hướng chính tắc tương tự như phổ thông.

Ví dụ 5.1 Trong $R^2$, cho phép toán

x $= (x_1$, $x_2)$, y $= (y_1$, $y_2)$ : (x, y) $= x_1y_1$ + $2x_1y_2$ + $2x_2y_1$ + $10x_2y_2$.

a) Chứng tỏ (x, y) là 1 tích vô hướng trên $R^2$.

b) Tính tích vô hướng của 2 véc tơ u $=$ (1, 2), v $=$ (2, -1).

Bài làm

a) Sinh viên tự kiểm tra 4 điều kiện của tích vô hướng.

b) (u, v) $=$ 1.2 + 2.1(-1) + 2.2.2 + 10.2(-1) $=$ -12.



Ví dụ 5.2 Trong $P_2[x]$, cho tích vô hướng (p,q) $= \int_{0}^{1}$ p(x) $\cdot$ q(x) dx; p(x), q(x) $\in P_2[x]$.

a) Chứng tỏ (p,q) là 1 tích vô hướng trên $P_2[x]$.

b) Tính tích vô hướng của 2 véc tơ p(x) $= 2x^2$ - 3x + 1, q(x) $=$ x + 1.

Bài làm

a) Sinh viên tự kiểm tra 4 điều kiện của tích vô hướng.

b) (p,q) $= \int_{0}^{1}$ p(x)q(x)dx $= \int_{0}^{1} (2x^2$ - 3x + 1)(x+1)dx $= \frac{1}{6}$.

$\overline{D}ộ$ dài véc tơ u được định nghĩa bởi

||u|| $= \sqrt{u$, $u}$

Khoảng cách giữa 2 véc tơ u và v được định nghĩa bởi

d(u, v) $=$ ||u - v||

Góc $\alpha$ giữa 2 véc tơ u và v được xác định bởi

(u,v)

$\cos \alpha =$

• Véc tơ có độ dài bằng 1 gọi là véc tơ đơn vị.

• Chia 1 véc tơ khác 0 cho độ dài của nó ta được véc tơ đơn vị.

• Quá trình tạo ra véc tơ đơn vị gọi là chuẩn hóa.

Bất đẳng thức Cauchy-Schwatz

|| (u, v) | $\le$ ||u||.||v|| $||\forall$ u, v $\in$ V.

$\hat{\text{Di}}ang$ thức xảy ra khi và chỉ khi u, v cùng phương (hay PTTT).

Bất đẳng thức tam giác

||u + v|| $\le$ ||u|| + ||v|| $\le ||\forall$ u, v $\in$ V.

$\tilde{\text{Di}}ng$ thức xảy ra khi và chỉ khi u, v cùng hướng.

Ví dụ 5.3 Trong $R^3:$ x $= (x_1; x_2; x_3)$, y $= (y_1; y_2; y_3)$. cho tích vô hướng

(x, y) $= 5x_1y_1$ + $2x_1y_2$ + $2x_2y_1$ + $3x_2y_2$ + $x_3y_3$

a) Chứng tỏ (x, y) là tích vô hướng.

b) Tìm tích vô hướng của 2 véc tơ u $=$ (2, 1, 0), v $=$ (3, -2, 4).

c) Tim dộ dài véc tơ u $=$ (3, 2, 1).

d) Tìm khoảng cách giữa 2 véc tơ u $=$ (1, 2, 1) và v $=$ (3, 0, 2).

e) Tim góc giữa 2 véc tơ u $=$ (1,0,1) và v $=$ (2,1,0).

Bài làm



a) Sinh viên tự kiếm tra 4 điều kiện của tích vô hướng.

b) (u, v) $=$ ((2, 1, 0), (3, -2, 4)) $=$ 5.2.3 + 2.2.(-2) + 2.1.3 + 3.1.(-2) + 0.4 $=$ 2.

c) ||u|| $= \sqrt{(u$, $u)} = \sqrt{((3$, 2, 1), (3, 2, $1))} = \sqrt{5.3.3$ + 2.3.2 + 2.2.3 + 3.2.2 + $1.1} = \sqrt{82}$

d) d(u, v) $=$ ||u - v|| $= \sqrt{(u$ - v, u - $v)} = \sqrt{((-2$, 2, -1), (-2, 2, $-1))}$

$= \sqrt{5.(-2).(-2)+2.(-2).2+2(2).(-2)+3.2.2+(-1).(-1)} = \sqrt{17}$.

e) $\cos \alpha = \frac{(u$, $v)}{||u||$, $||v||} = \frac{12}{\sqrt{6} \sqrt{31}} = \frac{12}{\sqrt{168}} \implies \alpha = \arccos \frac{12}{\sqrt{168}}$.

Nhận xét: Độ dài, khoảng cách, góc đối với tích vô hướng trên có giá trị khác với tích vô hướng ở phố

thông.

Ví dụ 5.4 Trong $P_2[x]$, cho tích vô hướng (p,q) $= \int_{-1}^{1}$ p(x)q(x)dx; $\forall$ p(x), q(x) $\in P_2[x]$.

a) Chứng tỏ (p,q) là một tích vô hướng trên $P_2[x]$.

b) Tính tích vô hướng của 2 véc tơ p(x) $= 2x^2$ - 3x + 1, q(x) $=$ x - 3.

c) Tim độ dài của véc tơ p(x) $=$ 2x + 3.

d) Tính khoảng cách giữa 2 véc tơ p(x) $= x^2$ + x + 2, q(x) $= x^2$ - 2x + 3.

e) Tính góc giữa 2 véc tơ p(x) $= x^2$ + x, q(x) $=$ 2x + 3.

Bài làm

a) Sinh viên tự kiểm tra 4 điều kiện của tích vô hướng.

b) (p,q) $= \int_{-1}^{1}$ p(x)q(x)dx $= \int_{-1}^{1} (2x^2$ - 3x + 1)(x - 3)dx $=$ -12.

c) ||p|| $= \sqrt{(p,p)} = \sqrt{\int_{-1}^{1} p(x)p(x)dx} \sqrt{\int_{-1}^{1} (2x+3)^2 dx} = \sqrt{\frac{62}{3}}$.

d) d(p,q) $=$ ||p-q|| $= \sqrt{(p-q,p-q)} = \sqrt{(3x-1,3x-1)} = \sqrt{\int_{-1}^{1} (3x-1)^2 dx} = 2\sqrt{2}$.

e) $\cos \alpha = \frac{(p,q)}{||p||.||q||} \frac{\int_{-1}^{1} (x^2+x)(2x+3) dx}{\sqrt{\int_{-1}^{1} (x^2+x)^2 dx} \cdot \sqrt{\int_{-1}^{1} (2x+3)^2 dx}} = \frac{5\sqrt{310}}{124}$.

Hai véc tơ vuông góc

u $\bot$ v $\Longleftrightarrow$ (u, v) $=$ 0.

Véc tơ vuông góc với tâp hợp

u $\perp$ M $\Longleftrightarrow$ (u, y) $=$ 0, $\forall$ y $\in$ M.

Họ trực giao: họ véc tơ M gọi là trực giao nếu

$\forall$ x, y $\in$ M : x $\bot$ y.

Họ trực chuẩn: họ véc tơ M gọi là trực chuẩn nếu M trực giao và

$\forall$ x $\in$ M : ||x|| $=$ 1.



Mệnh đềCho không gian con F $= \langle f_1$, $f_2$, $\ldots$, $f_m \rangle$

x $\perp$ F $\iff$ x $\perp f_k$, $\forall$ k $=$ 1, 2, $\ldots$, m.

Ví dụ 5.5 Trong $R^3$ với tích vô hướng chính tắc, cho không gian con

F $= \{(x_1; x_2; x_3) \in R^3 \mid \frac{x_1$ + $x_2$ - $x_3 = 0}{2x_1$ + $3x_2$ + $x_3 = 0} \}$

Tim m $d\acute{e}$ x $=$ (2; 3; m) $\perp$ F.

Bài làm

Tập sinh của F là $\{u =$ (4, -3, $1)\}$.

x $\perp$ F $\iff$ x $\perp$ u $\iff$ (x, u) $=$ 0 $\iff$ 2.4 + 3.(-3) + m.1 $=$ 0 $\iff$ m $=$ 1.

Bù vuông góc của không gian con

## 5.2 Bù vuông góc của không gian con

Dinh nghĩa 5.2 Trong không gian Euclide V, cho không gian con F. Tập hợp

$F^{\perp} = \{x \in$ V | x $\perp F\}$

gọi là bù vuông góc của không gian con F.

Dinh lý

Cho F là KG con của KG Euclide V. Khi đó:

• $F^{\perp}$ là không gian con của V và V $=$ F $\oplus F^{\perp}$.

$\bullet$ dim F + $\dim F^{\perp} = \dim$ V.

Ví dụ 5.6 Trong $R^3$, cho không gian con F $= \langle f_1 =$ (1,1,1), $f_2 =$ (2,1,0), $f_3 =$ (1,0,-1) $\rangle$.

Tìm cơ sở và số chiều của $F^{\perp}$.

Bài làm

x $= (x_1$, $x_2$, $x_3) \in F^{\perp} \Longleftrightarrow$ x $\perp$ F $\Longleftrightarrow$ x $\perp f_k$, k $=$ 1, 2, 3.

$ \iff\n\begin{cases}\n(x, f_1) = 0 \\
(x, f_2) = 0 \\
(x, f_3) = 0\n\end{cases}\n\iff\n\begin{cases}\nx_1 + x_2 + x_3 = 0 \\
2x_1 + x_2 + 0x_3 = 0 \\
x_1 + 0x_2 - x_3 = 0\n\end{cases}\n\iff\n\begin{bmatrix}\n1 & 1 & 1 & 0 \\
2 & 1 & 0 & 0 \\
1 & 0 & -1 & 0\n\end{bmatrix}\n\begin{cases}\n\text{nhân xét các hàng của ma trận}\n\end{cases} $

Giải hệ suy $ra<math display="inline">x = \alpha(1;$ -2; 1). Cơ sở của $<math display="inline">F^{\perp}$ là $<math display="inline">\{(1;$ -2; $1)\}$ và $<math display="inline">\dim F^{\perp} =$ 1.

Ví du 5.7 Trong $R^3$, cho không gian con

F $= \{(x_1; x_2; x_3) \in R^3 \mid \frac{x_1$ + $x_2$ + $x_3 = 0}{2x_1$ + $x_2$ - $x_3 = 0} \}$

Tìm cơ sở và số chiều của $F^{\perp}$.

Bài làm

Giải hệ suy ra tập sinh của F: F $= \langle$ u $=$ (2, -1, 3) $\rangle$.

x $= (x_1; x_2; x_3) \in F^{\perp} \Longleftrightarrow$ x $\perp$ u $\Longleftrightarrow 2x_1$ - $x_2$ + $x_3 =$ 0.

$\implies F^{\perp} = \langle$ (1;2;0), (2;0;-1) $\rangle$.

Cơ sở của $F^{\perp}$ là $\{(1;$ 2; 0), (2; 0; $-1)\}\và$ dim $F^{\perp} =$ 2.

Ghi chú:



• Cho F $= \langle h_1$, $h_2$, $\ldots$, $h_m \rangle$. x $\in F^{\perp}$ khi và chỉ khi

$ \begin{cases} (h_1, x) = 0 \\ (h_2, x) = 0 \\ \cdots \\ (h_m, x) = 0 \end{cases} \Longleftrightarrow \begin{bmatrix} h_1 - \\ h_2 - \\ \cdots \\ h_m - \end{bmatrix} .x = 0 \text{(ma train hàng của } F) $

Do đó $F^{\perp}$ là tập nghiệm của hệ phương trình

$ \left|\begin{array}{c} h_1 - \ h_2 - \ 0 \\ \dots \\ h \end{array}\right| $

• Cho F $= \{x \in R^n$ | Ax $= 0\}$.

$ Ax = 0 viết lại theo véc tơ hàng\begin{bmatrix} h_1 - \\ h_2 - \\ \cdots \\ h_m - \end{bmatrix}. x = 0 \Longleftrightarrow \begin{cases} (h_1, x) = 0 \\ (h_2, x) = 0 \\ \cdots \\ (h_m, x) = 0 \end{cases} $

Diễu này chứng tỏ $\forall$ x $\in$ F : x $\perp f_k$, k $=$ 1, m.

Điều này chứng tỏ $F^{\perp}$ được sinh bởi các véc tơ hàng của ma trận A.

$F^{\perp} = \langle h_1$, $h_2$, $\ldots$, $h_m \rangle$, với $h_k$ là các hàng của ma trận A

Ví dụ 5.8 Hãy tìm cơ sở và số chiều của $F^{\perp}$ trong $R^{4}$, trong đó

a) F $= \{(x_1$, $x_2$, $x_3; x_4) \in R^4 \mid \frac{x_1$ + $x_3$ + $x_4 = 0}{2x_1$ - $x_2$ + $3x_3$ + $x_4 = 0} \}$

b) F $= \langle$ 1; -1; 2; 1 $\rangle$, (2; 1; 1; 0) $\rangle$

Bài làm

a) Ta có $F^{\perp} = \langle$ (1,0,1,1), (2,-1,3,1) $\rangle$ (lấy từ các hàng của hệ phương trình).

Suy ra cơ sở của $F^{\perp}$ là $\{(1;0;1;1),(2;-1;3;1)\}\;và$ dim $F^{\perp}=2$.

b) Vì F $= \langle$ (1, -1, 2, 1), (2, 1, 1, 0) $\rangle$ nên $F^{\perp}$ là tập nghiệm của hệ phương trình

$ \begin{bmatrix} 1 & -1 & 2 & 1 & 0 \end{bmatrix} $

$ \begin{vmatrix} 2 & 1 & 1 & 0 \end{vmatrix} $

Giải hệ suy ra tập nghiệm $F^{\perp} = <(-1;$ 1; 1; 0), (-1; 2; 0; 3) $>$.

Suy ra cơ sở của $F^{\perp}$ là $\{(-1;$ 1; 1; 0), (-1; 2; 0; $3)\}\và$ dim $F^{\perp} =$ 2.

Dinh lý

$\bullet$ Mọi tập trực giao, không chứa véc tơ không thì DLTT.

• Cho E $= \{e_1$, $e_2$, $\ldots$, $e_n\}$ là cơ sở trực chuẩn của KG Euclide V.

$\forall$ x $\in$ V luôn được biễu diễn duy nhất ở dạng

x $= x_1e_1$ + $x_2e_2$ + $\cdots$ + $x_ne_n$, với $x_k =$ (x, $e_k)$.



Ví dụ 5.9 Trong không gian Euclide V, cho cơ sở trực chuẩn

E $= \left\{ \left( \frac{1}{\sqrt{6}}; \frac{-1}{\sqrt{6}}; \frac{-2}{\sqrt{6}} \right)$, $\left( \frac{1}{\sqrt{2}}; \frac{1}{\sqrt{2}};$ 0 $\right)$, $\left( \frac{1}{\sqrt{3}}; \frac{-1}{\sqrt{3}}; \frac{1}{\sqrt{3}} \right) \right\}$

Tìm tọa độ của véc tơ x $=$ (3, -2, 1) trong cơ sở E.

Bài làm

Ta viết x $= x_1e_1$ + $x_2e_2$ + $x_3e_3$, trong đó $x_1 =$ (x, $e_1) = \frac{3}{\sqrt{6}}$, $x_2 =$ (x, $e_2) = \frac{1}{\sqrt{2}}$, $x_3 =$ (x, $e_3) = \frac{6}{\sqrt{3}}$.

$ Vậy tọa độ của x trong cơ sở E là [x]_E = \begin{pmatrix} \frac{3}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} \\ \frac{6}{\sqrt{6}} \end{pmatrix} $

Quá trình Gram-Schmidt

## 5.3 Quá trình Gram-Schmidt

Dinh lý 5.3 (Gram-Schmidt) Cho E $= \{e_1$, $e_2$, $\ldots$, $e_m\}$ là họ ĐLTT của KGVT V. Khi đó tồn tại một

họ trực giao

F $= \{f_1$, $f_2$, $\ldots$, $f_m\}$ thỏa $\langle e_1$, $e_2$, $\ldots$, $e_m \rangle = \langle f_1$, $f_2$, $\ldots$, $f_m \rangle$.

Thuật toán Gram-Schmidt

• $f_1 = e_1$.

• $f_2 = e_2$ - $\frac{(e_2$, $f_1)}{(f_1$, $f_1)} f_1$.

• $f_3 = e_3$ - $\frac{(e_3$, $f_1)}{(f_1$, $f_1)} f_1$ - $\frac{(e_3$, $f_2)}{(f_2$, $f_2)} f_2$.

• $f_k = e_k$ - $\frac{(e_k$, $f_1)}{(f_1$, $f_1)} f_1$ - $\frac{(e_k$, $f_2)}{(f_2$, $f_2)} f_2 \cdots$ - $\frac{(e_k$, $f_{k-1})}{(f_{k-1}$, $f_{k-1})} f_{k-1}$.

Ví du 5.10 Trực chuẩn họ véc tơ E $= \{(1;0;1;1),(0;1;1;1),(1;1;1;1)\}\$

Bài làm

Chon $f_1 = e_1 =$ (1; 0; 1; 1).

$f_2 = e_2$ - $\frac{(e_2$, $f_1)}{(f_1$ - $f_1)} f_1 =$ (0; 1; 1; 1) - $\frac{2}{3}$ (1; 0; 1; 1) $= \left(\frac{-2}{3};$ 1; $\frac{1}{3}; \frac{1}{3}\right)$. Chọn $f_2 =$ (-2; 3; 1; 1).

$f_3 = e_3$ - $\frac{(e_3$, $f_1)}{(f_1$, $f_1)} f_1$ - $\frac{(e_3$, $f_2)}{(f_2$, $f_2)} f_2 = \left(\frac{2}{5}$, $\frac{2}{5}$, $\frac{-1}{5}$, $\frac{-1}{5}\right)$. Chọn $f_3 =$ (2; 2; -1; -1).

Họ trục giao cần tìm là F $= \{f_1$, $f_2$, $f_3\}$.

Chia mỗi véc tơ cho độ dài của nó, ta được cơ sở trực chuẩn là

$\left\{ \left( \frac{1}{\sqrt{3}};$ 0; $\frac{1}{\sqrt{3}}; \frac{1}{\sqrt{3}} \right)$, $\left( \frac{-2}{\sqrt{15}}; \frac{3}{\sqrt{15}}; \frac{1}{\sqrt{15}}; \frac{1}{\sqrt{15}} \right) \left( \frac{2}{\sqrt{10}}; \frac{2}{\sqrt{10}}; \frac{-1}{\sqrt{10}}; \frac{-1}{\sqrt{10}} \right) \right\}$.

Ví dụ 5.11 Trong $R^4$ với tích vô hướng chính tắc, cho không gian con

F $= \{(x_1; x_2; x_3; x_4) \in R^4 \mid \frac{x_1$ + $x_2$ - $x_3$ + $x_4 = 0}{2x_1$ + $3x_2$ - $x_3$ + $3x_4 = 0} \}$

Tìm một cơ sở trực chuẩn của F.

Bài làm Giải hệ, tìm một cơ sở tùy ý của F là $\{(2;-1;1;0),(0;-1;0;1)\}$.

Dùng Gram-Schmidt: $f_1 = e_1 =$ (2, -1, 1, 0).

$f_2 = e_2$ - $\frac{(e_2$, $f_1)}{(f_1$, $f_1)} f_1 =$ (0; -1; 0; 1) - $\frac{1}{6}(2;$ -1; 1; 0) $= (\frac{-1}{3}; \frac{-5}{6}; \frac{-1}{6};$ 1). Chọn $f_2 =$ (2; 5; 1; -6).

Cơ sở trực giao là F $= \{f_1$, $f_2\}$. Cơ sở trực chuẩn là $\left\{ \left( \frac{2}{\sqrt{6}}; \frac{-1}{\sqrt{6}}; \frac{1}{\sqrt{6}};$ 0 $\right)$, $\left( \frac{2}{\sqrt{66}}; \frac{5}{\sqrt{66}}; \frac{1}{\sqrt{66}}; \frac{-6}{\sqrt{66}}; \right) \right\}$.



Hình chiếu vuông góc

## 5.4 Hình chiếu vuông góc

### Định nghĩa 5.4 (Hình chiếu vuông góc) Trong KG Euclide V, cho không gian con F và véc tơ v.

Véc tơ được biểu diễn duy nhất dưới dạng

v $=$ f + q; f $\in$ F, q $\in F^{\perp}$.

Véc tơ f được gọi là hình chiếu vuông góc của v xuống f, ký hiệu: f $= Pr_F$ v.

Khoảng cách từ v xuống F được định nghĩa là d(v, F) $=$ ||g|| $=$ ||v - $Pr_F$ v.

Ví dụ 5.12 Trong $R^4$ với tích vô hướng chính tắc, cho không gian con

F $= \{(x_1$, $x_2$, $x_3$, $x_4) \in R^4 \mid \frac{x_1$ + $x_2$ - $x_3$ + $x_4 = 0}{2x_1$ + $x_2$ - $3x_3$ + $3x_4 = 0} \}$

và véc tơ x $=$ (1; 1; 0; 1)

a) Tìm hình chiếu của x xuống F.

b) Tìm khoảng cách từ x đến F.

Bài làm

a) Chọn 1 cơ sở F $= \langle f_1 =$ (2, -1, 1, 0), $f_2 =$ (-2, 1, 0, 1) $\rangle$.

Viết x $=$ f + q $= x_1 f_1$ + $x_2 f_2$ + q, q $\in F^{\perp}$.

Nhân lần lượt $f_1$, $f_2$ vào phương trình theo nghĩa tích vô hướng, ta được

$ \begin{cases} x_1(f_1, f_1) + x_2(f_1, f_2) = (x, f_1) \\ x_2(f_2, f_1) + x_2(f_2, f_2) = (x, f_2) \end{cases} \Longleftrightarrow \begin{cases} 6x_1 - 5x_2 = 1 \\ -5x_1 + 6x_2 = -1 \end{cases} \Longleftrightarrow \begin{cases} x_1 = \frac{1}{11} \\ x_2 = \frac{-1}{11} \end{cases} $

$Pr_F$ x $=$ f $= x_1 f_1$ + $x_2 f_2 = \frac{1}{11}(2;$ -1; 1; 0) + $\frac{-1}{11} f_2 =$ (-2; 1; 0; 1) $= \left(\frac{4}{11}; \frac{-2}{11}; \frac{1}{11}; \frac{-1}{11}\right)$

b) d(x, F) $=$ ||g|| $=$ ||x - $Pr_F$ x|| $= ||(\frac{7}{11}; \frac{13}{11}; \frac{-1}{11}; \frac{12}{11})|| = \sqrt{3}$.

Bài tập

Câu 1) Trong $R_2:$ x $= (x_1$, $x_2)$, y $= (y_1$, $y_2)$, cho tích vô hướng

(x,y) $= x_1y_1$ - $2x_1y_2$ - $2x_2y_1$ + $5x_2y_2$

(a) Tinh (x, y), ||x||, ||y||.

(b) Tinh ||x + y||, d(x, y).

(c) Tính (x, y).

(d) Tim véc to u sao cho u $\perp$ x.

Câu 2) Trong $R_4$, cho KG con U $= \langle$ (1,1,0,0); (2,1,1,0), (2,1,0,1) $\rangle$ và véc tơ z $=$ (7,3,0,0).

(a) Tìm cơ sở và số chiều của $U^{\perp}$.

(b) Tim $Pr_U(z)$, $Pr_{U^{\perp}}(z)$, d(z, U), d(z, $U^{\perp})$.

Tìm một cơ sở trực chuẩn của U.

(c)

(d) Tìm lại $Pr_U(z)$ theo cơ sở trực chuẩn.



Câu 3) Trong $R_4$, cho không gian nghiệm của hệ thuần nhất

$ U: \begin{cases} x_1 + x_2 - x_3 + x_4 = 0, \\ 2x_1 - x_2 + x_3 + 2x_4 = 0. \end{cases} V: \begin{cases} x_1 + 2x_2 - x_3 = 0, \\ 2x_1 + 3x_2 - x_4 = 0. \end{cases} $

(a) Tìm cơ sở và số chiều $của<math display="inline">W=(U\cap V)^{\perp}$.

(b) Tìm cơ sở trực chuẩn E của W.

(c) Tìm véc tơ e sao cho $\{E$, $e\}$ là một cơ sở trực chuẩn của $R_4$.



# Chương 6

Nội dung

1) Định nghĩa và ví dụ.

2) Nhân và ảnh của ánh xạ tuyến tính.

3) Ma trận của ánh xạ tuyến tính trong một cặp cơ

$S\ddot{\mathbf{O}}$.

4) Ma trận chuyển cơ sở và đồng dạng.

### Dịnh nghĩa và ví dụ

## 6.1 Dịnh nghĩa và ví dụ

### Định nghĩa 6.1 (Ánh xạ) Cho 2 tập hợp khác rỗng X, Y. Ánh xạ f từ X đến Y là một quy tắc sao cho

$m\tilde{\delta}i$ x thuộc X, tồn tại duy nhất y thuộc Y. Ta viết

f: X $\longrightarrow$ Yx $\longmapsto$ y $=$ f(x).

Ánh xạ f gọi là đơn ánh nếu: $x_1 \neq x_2 \Longrightarrow f(x_1) \neq f(x_2)$

Ánh xạ f gọi là toàn ánh nếu: $\forall$ y $\in$ Y, $\exists$ x $\in$ X : y $=$ f(x)

Ánh xạ f gọi là song ánh nếu đơn ánh và toàn ánh.

Hàm số ở phổ thông là ví dụ về ánh xạ.

Cho ánh xạ tức là chỉ ra quy luật, dựa vào đó viết ảnh của mọi phần tử thuộc X.

Có nhiều cách cho ánh xạ: bằng đồ thị, bằng biểu đồ, bằng biểu thức đại số, bằng cách liệt kê,...

### Dịnh nghĩa 6.2 (Ánh xạ tuyến tính) Cho V, W là hai không gian trên cùng trường số K.

Ánh xạ f: V $\longrightarrow$ W gọi là ánh xạ tuyến tính nếu thỏa:

i) $f(v_1$ + $v_2) = f(v_1)$ + $f(v_2)$, $\forall v_1$, $v_2 \in$ V.

ii) $f(\alpha$ v) $= \alpha$ f(v), $\forall$ v $\in$ V, $\alpha \in$ K.

Ví dụ 6.1

a) $f(x_1; x_2; x_3) = (2x_1$ + $x_2$ - $3x_3; x_1$ - $4x_2)$ là một ánh xạ tuyến tính từ $R^3$ đến $R^2$. (??).



b) Phép quay trong không gian Oxyz quanh trục 0z một góc $30<sup>o</sup>$ ngược chiều kim đồng hồ nhìn từ hướng

dương của trục 0z là một ánh xạ tuyến tính từ $R^3$ đến $R^3$.

c) Tương tự phép đối xứng, phép chiếu,... qua các đường thắng và mặt phẳng qua gốc tọa độ là những ánh

xa tuyến tính từ $R^3$ đến $R^3$.

Cho E $= \{e_1$, $e_2$, $\ldots$, $e_n\}$ là tập sinh của KGVT V và axtif: V $\longrightarrow$ W.

Giả sử ta biết $f(e_1)$, $f(e_2)$, $\ldots$, $f(e_n)$.

$\forall$ x $\in$ V : x $= x_1e_1$ + $x_2e_2$ + $\cdots$ + $x_ne_n \Longrightarrow$ f(x) $= f(x_1e_1$ + $x_2e_2$ + $\cdots$ + $x_ne_n)$

f(x) $= f(x_1e_1)$ + $f(x_2e_2)$ + $\cdots$ + $f(x_ne_n) = x_1f(e_1)$ + $x_2f(e_2)$ + $\cdots$ + $x_nf(e_n)$.

Ánh xạ tuyến tính được xác định hoàn toàn nếu biết được ảnh của một tập sinh của V.

Ví du 6.2 Cho ánh xạ tuyến tính f: $R^3 \longrightarrow R^2$, biết

f(1;1;0) $=$ (2;-1), $\quad$ f(1;1;1) $=$ (1;2), $\quad$ f(1;0;1) $=$ (-1;1)

a) Tim f(3;1;5).

b) Tim f(x).

Bài làm

a) Viết (3; 1; 5) $= \alpha(1;$ 1; 0) + $\beta(1;$ 1; 1) + $\gamma(1;$ 0; 1)

$ \iff \begin{cases} \alpha+\beta+\gamma=3 \\ \alpha+\beta=1 \\ \alpha + \gamma=5 \end{cases} \iff \begin{cases} \alpha=-2 \\ \beta=3 \\ \gamma=2 \end{cases} $

f(x) $= f(\alpha(1;$ 1; 0) + $\beta(1;$ 1; 1) + $\gamma(1;$ 0; 1)) $= \alpha$ f(1; 1; 0) + $\beta$ f(1; 1; 1) + $\gamma$ f(1; 0; 1).

$\implies$ f(3; 1; 5) $=$ -2(2; -1) + 3(1; 2) + 2(-1; 1) $=$ (-3; 10).

b) Làm tương tự như trên cho trường hợp tổng quát $f(x_1; x_2; x_3)$.

Ta có thể làm cách khác bằng cách dùng phép biến đổi đại số như sau:

f(0;0;1) $=$ f(1;1;1) - f(1;1;0) $=$ (1;2) - (2;-1) $=$ (-1;3).

f(0;1;0) $=$ f(1;1;1) - f(1;0;1) $=$ (1;2) - (-1;1) $=$ (2;1).

f(1;0;0) $=$ f(1;1;0) - f(0;1;0) $=$ (2;-1) - (2;1) $=$ (0;-2)

$f(x_1; x_2; x_3) = x_1$ f(1; 0; 0) + $x_2$ f(0; 1; 0) + $x_3$ f(0; 0; 1) $= x_1(0;$ -2) + $x_2(2;$ 1) + $x_3(-1;$ 3)

f(x) $= (2x_2$ - $x_3; -2x_1$ + $x_2$ + $3x_3)$

Ghi chú: Ta có thể dùng các phép biến đổi cho ánh xạ tuyến tính để tìm ảnh của 3 véc tơ đơn vị.

Tuy nhiên ta sẽ gặp khó khăn tìm ra phép biến đổi trong trường hợp tổng quát.

Ta có thể viết ánh xạ tuyến tính dưới dạng ma trận để tìm ảnh của 3 véc tơ đơn vị như sau:

$ (theo hàng) \begin{bmatrix} e_1 \\ e_2 \\ e_3 \end{bmatrix} \begin{bmatrix} f(e_1) \\ f(e_2) \\ f(e_3) \end{bmatrix} \Longrightarrow \begin{bmatrix} 1 & 1 & 0 & 2 & -1 \\ 1 & 1 & 1 & 1 & 2 \\ 1 & 0 & 1 & -1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 & 0 & -2 \\ 0 & 1 & 0 & 2 & 1 \\ 0 & 0 & 1 & -1 & 3 \end{bmatrix} $

Kết hợp với ý nghĩa phép nhân ma trận, ta có thuật toán sau

Tìm axtt cho ảnh của cơ sở

Cho cơ sở E $= \{e_1$, $e_2$, $\ldots$, $e_n\}$ và ánh xạ tuyến tính thỏa

$f(e_k) = f_k$

Theo hàng $\left[$ E $\mid$ F $\right] \frac{\text{bdsc$ theo hàng, tương $ứng}}{\text{nhân$ bên trái với $} E^{-1}} \left[$ I $\mid E^{-1}F \right]$

Ví dụ 6.3 Cho f là phép đối xứng qua mặt phẳng 2x - y + 3z $=$ 0 là ánh xạ tuyến tính trong không gian

Oxyz. Hãy tìm $f(x_1; x_2; x_3)$.



Bài làm

f biến cặp véc tơ chỉ phương thành chính nó và véc tơ pháp tuyến thành véc tơ đối

$a_1 =$ (1; 2; 0) : f(1; 2; 0) $=$ (1; 2; 0)

$a_2 =$ (0; 3; 1) : f(0; 3; 1) $=$ (0; 3; 1)

n $=$ (2, -1, 3) : f(2, -1, 3) $=$ (-2, 1, -3).

Viết dạng ma trận

$ \begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c $

f(x) $= x_1(\frac{3}{7}; \frac{2}{7}; \frac{-6}{7})$ + $x_2(\frac{2}{7}; \frac{6}{7}; \frac{3}{7})$ + $x_3(\frac{-6}{7}; \frac{3}{7}; \frac{-2}{7}) = \frac{1}{7}(3x_1$ + $2x_2$ - $6x_3; 2x_1$ + $6x_2$ + $3x_3; -6x_1$ + $3x_2$ - $2x_3)$

Nhân và ảnh của ánh xạ tuyến tính

## 6.2 Nhân và ảnh của ánh xạ tuyến tính

Cho ánh xạ tuyến tính f: V $\longrightarrow$ W

Nhân của f được định nghĩa là

$\ker$ f $= \{x \in$ V : f(x) $= 0\}$

Anh được định nghĩa là

Im f $= \{f(x) \in$ W | x $\in V\}$

### Dịnh lý Cho ánh xạ tuyến tính f: V \longrightarrow W

• ker f là KG con của V. • Im f là KG con của W.

$\dim(\ker$ f) + $\dim(Im$ f) $= \dim$ V

Ví dụ 6.4 Cho axtt f: $\mathbb{R}^3 \longrightarrow \mathbb{R}^2$ thỏa $f(x_1; x_2; x_3) = (x_1$ - $x_2; x_1$ + $2x_2$ - $x_3)$.

Tìm cơ sở và số chiều của Imf và ker f.

Bài làm

$ a) x \in Ker f \implies f(x) = 0 \iff (x_1 - x_2; x_1 + 2x_2 - x_3) = 0 \iff \begin{cases} x_1 - x_2 = 0 \\ x_1 + 2x_2 - x_3 = 0 \end{cases} \iff \begin{cases} x_1 = x_2 \\ x_3 = 3x_2 \end{cases}\implies x = (x_2; x_2; 3x_2) = x_2(1; 1; 3) \implies \ker f = \langle (1; 1; 3) \rangle. $

Cơ sở của ker f là $\{(1;1;3)\}\và$ dim(ker f) $=$ 1.

b) Imf gồm tất cả các f(x):

$f(x_1; x_2; x_3) = (x_1$ - $x_2; x_1$ + $2x_2$ - $x_3) = x_1(1;$ 1) + $x_2(-1;$ 2) + $x_3(0;$ -1) $\implies$ Imf $= \langle$ (1; 1), (-1; 2), (0; -1) $\rangle$.

Cơ sở của Imf là $\{(1;1),(0;3)\}\;và$ dim(Im f) $=$ 2.

Cách khác

$\dim(Imf) = \dim(R^3)$ - $\dim(\ker$ f) $=$ 3 - 1 $=$ 2 $\Longrightarrow$ Imf $\equiv R^2$.

Cơ sở của Imf là $\{(1,0)$, $(0,1)\}$.

Dinh lý Cho axternal f: V $\longrightarrow$ W

Ảnh của tập sinh là tập sinh của ảnh:

V $= \langle e_1$, $e_2$, $\ldots$, $e_n \rangle \Longrightarrow$ Im f $= \langle f(e_1)$, $f(e_2)$, $\ldots$, $f(e_n) \rangle$



Ví dụ 6.5 Cho axtt f: $R^3 \longrightarrow R^3$ biết ảnh của một tập sinh

f(1; 1; 1) $=$ (1; 2; 1), f(1; 1; 2) $=$ (2; 1; -1), f(1; 2; 1) $=$ (5; 4; -1).

Tìm cơ sở và số chiều của Imf và ker f

a) Theo dinh lý: Im f $= \langle$ (1; 2; 1), (2; 1; -1), (5; 4; -1) $\rangle$.

Cơ sở của Imf là $\{(1;2;1),(0;1;1)\}\;và \dim(Imf)=2$.

b) E $= \{(1$, 1, 1), (1, 1, 2), (1, 2, $1)\}\là$ tập sinh của $R^3$.

Viết x $= x_1e_1$ + $x_2e_2$ + $x_3e_3 \implies$ f(x) $= x_1f(e_1)$ + $x_2f(e_2)$ + $x_3f(e_3)$

f(x) $= x_1(1;$ 2; 1) + $x_2(2;$ 1; -1) + $x_3(5;$ 4; -1) $= (x_1$ + $2x_2$ + $5x_3; 2x_1$ + $x_2$ + $4x_3; x_1$ - $x_2$ - $x_3)$

$ x \in \ker f \Longleftrightarrow f(x) = 0 \Longleftrightarrow \begin{cases} x_1 + 2x_2 + 5x_3 = 0 \\ 2x_1 + x_2 + 4x_3 = 0 \\ x_1 - x_2 - x_3 = 0 \end{cases} \Longleftrightarrow \begin{cases} x_1 = -\alpha \\ x_2 = -2\alpha \\ x_3 = \alpha \end{cases}. $

$\Rightarrow$ x $= -\alpha(1;$ 1; ) - $2\alpha(1;$ 1; 2) + $\alpha(1;$ 2; 1) $= \alpha(2;$ 1; 4).

Vậy cơ sở của ker f là $\{(2,1,4)\}\và$ dim(ker f) $=$ 1.

Ma trận của ánh xạ tuyến tính

## 6.3 Ma trận của ánh xạ tuyến tính

Ma trận của ánh xạ tuyến tính cho axte f: V $\longrightarrow$ W.

E $= \{e_1$, $e_2$, $\ldots$, $e_n\}$ là cơ sở của V. F $= \{f_1$, $f_2$, $\ldots$, $f_m\}$ là cơ sở của W.

Ma trận

$ A_{E,F} = \begin{pmatrix} [f(e_1)]_F & [f(e_2)]_F & \dots & [f(e_n)]_F \ | & || & || \end{pmatrix} $

gọi là ma trận của ánh xạ tuyến tính f trong cặp cơ sở E, F.

Chú ý: $[f(e_i)]_F = F^{-1}f(e_i)$. Do đó

$ A_{E,F} = \begin{pmatrix} F^{-1}f(e_1) & F^{-1}f(e_2) & \dots & F^{-1}f(e_n) \end{pmatrix} = F^{-1}f(E). $

Ví dụ 6.6 Cho axtt f: $\mathbb{R}^3 \longrightarrow \mathbb{R}^2$ biết $f(x_1; x_2; x_3) = (x_1$ + $2x_2$ - $3x_3; 2x_1$ + $x_3)$.

Tìm ma trận của f trong cặp cơ sở E $= \{(1;1;1)$, (1;0;1), $(1;1;0)\}$, F $= \{(1;3)$, $(2;5)\}$.

Bài làm

$ f(1;1;1) = (0;3) \Longrightarrow [f(1;1;1)]_F = \begin{pmatrix} 6 \\ -3 \end{pmatrix}. $

f(1;0;1) $=$ (-2;3) $\Longrightarrow [f(1;0;1)]_F = {16 \choose -9}$.

$ f(1;1;0) = (3;2) \Longrightarrow [f(1;1;0)]_F = \begin{pmatrix} -11 \\ 7 \end{pmatrix}. $

$ Ma trận cần tìm là A_{E,F} = \begin{pmatrix} 6 & 16 & -11 \\ -3 & -9 & 7 \end{pmatrix}. $

Cách khác

$ A_{E,F} = F^{-1}f(E) = \begin{pmatrix} 1 & 2 \\ 3 & 5 \end{pmatrix}^{-1} \begin{pmatrix} 0 & -2 & 3 \\ 3 & 3 & 2 \end{pmatrix} \xrightarrow{\text{dùng casio}} \begin{pmatrix} 6 & 16 & -11 \\ -3 & -9 & 7 \end{pmatrix}. $



Dinh lý

i) Cho axtt f: V $\longrightarrow$ W. Khi đó tồn tại duy nhất ma trận $A_{E,F}$

$c\tilde{\sigma}$ m $\times$ n sao cho

$[f(x)]_F = A_{E,F}[x]_E$,

với E, F là 2 cơ sở của V và W tương ứng.

ii) 2. Cho ma trận A $= (a_{ij})_{m \times n}$ trên trường số K. Khi đó tồn

tại duy nhất một ánh xạ tuyến tính f: $K^n \longrightarrow K^m$ thỏa

$[f(x)]_F = A_{E,F}[x]_E$.

Chú $\dot{y}:$

• Mỗi một ánh xạ tuyến tính từ khgian hữu hạn chiều vào KG hữu hạn chiều tương ứng duy nhất một

ma trận và ngược lại.

• Ta coi ánh xạ tuyến tính là ma trận. Thông thường không phân biệt hai khái niệm này.

Ví dụ 6.7 Cho axtt f: $\mathbb{R}^3 \longrightarrow \mathbb{R}^2$ biết ma trận của f trong cặp cơ sở

$ E = \{(1; 1; 1), (1; 0; 1), (1; 1; 0)\}, F = \{(1; 1), (2; 1)\}\là A_{E,F} = \begin{pmatrix} 2 & 1 & -3 \\ 0 & 3 & 4 \end{pmatrix}. $

a) Tim f(3;1;5).

b) Tim f(x).

Bài làm

$ a) [(3;1;5)]_E = E^{-1} \begin{pmatrix} 3 \\ 1 \\ 5 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} 3 \\ 1 \\ 5 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \\ -2 \end{pmatrix}. $

Dùng công thức $[f(x)]_F = A_{E,F}[x]_E$

$ [f(3;1;5)]_F = \begin{pmatrix} 2 & 1 & -3 \\ 0 & 3 & 4 \end{pmatrix} \begin{pmatrix} 3 \\ 2 \\ -2 \end{pmatrix} = \begin{pmatrix} 14 \\ -2 \end{pmatrix} $

$\implies$ f(3; 1; 5) $=$ 14(1; 1) - 2(2; 1) $=$ (10; 12).

$ b) [(x_1; x_2; x_3)]_E = E^{-1} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} -x_1 + x_2 + x_3 \\ x_1 - x_2 \\ x_1 - x_3 \end{pmatrix}. $

Dùng công thức $[f(x)]_F = A_{E,F}[x]_E$

$ [f(x_1; x_2; x_3)]_F = \begin{pmatrix} 2 & 1 & -3 \\ 0 & 3 & 4 \end{pmatrix} \begin{pmatrix} -x_1 + x_2 + x_3 \\ x_1 - x_2 \\ x_1 - x_2 \end{pmatrix} = \begin{pmatrix} -4x_1 + x_2 + 5x_3 \\ 7x_1 - 3x_2 - 4x_3 \end{pmatrix} $

$\implies f(x_1; x_2; x_3) = (-4x_1$ + $x_2$ + $5x_3)(1;$ 1) - $(7x_1$ - $3x_2$ - $4x_3)(2;$ 1) $= (10x_1$ - $5x_2$ - $3x_3; 3x_1$ - $2x_2$ + $x_3)$

Ma trận trong 1 cơ sở cho axte f: V $\longrightarrow$ V.

E $= \{e_1$, $e_2$, $\dots$, $e_n\}$ là cơ sở của V.

Ma trận ánh xạ của f trong cặp cơ sở E, E là

$A_E = E^{-1}$ f(E).



Ví dụ 6.8 Cho axtt f: $\mathbb{R}^3 \longrightarrow \mathbb{R}^3$ có ma trận trong cơ sở E $= \{(1$, 1, 1), (1, 0, 1), (1, 1, $0)\}\là$

$ A_E = \begin{pmatrix} 1 & 1 & -1 \ 2 & 3 & 3 \ 1 & 2 & 4 \end{pmatrix}. $

a) Tim f(2;3;-1).

b) Tìm cơ sở và số chiều của ker f.

c) Tìm cơ sở và số chiều của Imf.

Bài làm

a) Tương tự ví dụ trên: f(2; 3; -1) $=$ (12; 6; 2).

$ b) Giả sử x = x_1e_1 + x_2e_2 + x_3e_3 \iff [x]_E = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}. $

$ x \in \ker f \iff f(x) = 0 \iff [f(x)]_F = A_E[x]_E = 0 \iff \begin{pmatrix} 1 & 1 & -1 \\ 2 & 3 & 3 \\ 1 & 2 & 4 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = 0 \iff \begin{cases} x_1 = 6\alpha \\ x_2 = -5\alpha \\ x_3 = \alpha \end{cases} $

x $= 6\alpha(1;$ 1; 1) - $5\alpha(1;$ 0; 1) + $\alpha(1;$ 1; 0) $= \alpha(2;$ 7; 1)

$\Rightarrow$ ker f $= \langle$ 2, 7, 1 $\rangle$. Co sở của ker f là $\{(2$, 7, $1)\}$ và dim(ker f) $=$ 1.

$ c) [f(1;1;1)]_E = \begin{pmatrix} 1 & 1 & -1 \\ 2 & 3 & 3 \\ 1 & 2 & 4 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} \implies f(1;1;1) = (1;1;1) + (1;0;1) - (1;1;0) = (4;2;3). $

$ Tương tự [f(1;0;1)]_E = \begin{pmatrix} 1 \\ 3 \\ 2 \end{pmatrix} \Longrightarrow f(1;1;1) = (1;1;1) + 3(1;0;1) + 2(1;1;0) = (6;3;4). $

$ [f(1;1;0)]_E = \begin{pmatrix} -1 \\ 3 \\ 4 \end{pmatrix} \Longrightarrow f(1;1;1) = -(1;1;1) + 3(1;0;1) + 4(1;1;0) = (6;3;2). $

Im f $= \langle$ f(1;1;1), f(1;0;1), f(1;1;0) $\rangle$. Cơ sở của Im f là $\{(4;2;3)$, $(0;0;1)\}$.

Tính Chất 6.3 (Mối liên hệ giữa 2 ma trận trong cơ sở khác nhau)

Cho axte f: V $\longrightarrow$ W.

Cho 2 co sở của V là: E $= \{e_1$, $e_2$, $\ldots$, $e_n\}$, E' $= \{e'_1$, $e'_2$, $\ldots$, $e'_n\}$.

Cho 2 cơ sở của W là: F $= \{F_1$, $f_2$, $\ldots$, $f_n\}$, F' $= \{f'_1$, $f'_2$, $\ldots$, $f'_n\}$.

P là ma trận chuyển cơ sở từ E vào E': $[x]_E = P[x]_{E'}$

Q là ma trận chuyển cơ sở từ F vào $F'[y]_F = Q[y]_{F'}$

Ta có

$[f(x)]_F = A_{E,F}[x]_E \Longleftrightarrow Q[f(x)]_{F'} = A_{E,F}P[x]_{E'} \Longrightarrow [f(x)]_{F'} = Q^{-1}A_{E,F}P[x]_{E'}$

Khi đó, $Q^{-1}A_{E,F}P$ là ma trận của f trong cặp cơ sở E', F'.

Ta tóm tắc bằng sơ đồ sau

$ \begin{array}{ccc}\nE & \xrightarrow{\quad A\quad & F} \\
P \downarrow & & \downarrow Q \\
E' & \xrightarrow{Q^{-1}AP\quad & F'\n\end{array} $

Trong trường hợp đặc biệt: V $\equiv$ W, E $\equiv$ F, E' $\equiv$ F', ta có kết quả tương tự

$ \begin{array}{ccc}\nE & \xrightarrow{A} & E \\
P \downarrow & & \downarrow P \\
E' & \xrightarrow{P^{-1}AP} & E'\n\end{array} $



Ví dụ 6.9 Cho axtt f: $\mathbb{R}^3 \longrightarrow \mathbb{R}^3$ cho bởi $f(x_1; x_2; x_3) = (x_1$ + $2x_2$ - $3x_3; 2x_1$ + $x_2$ + $x_3; 3x_1$ - $x_2$ + $2x_3)$.

Tìm ma trận của f trong cơ sở E $= \{(1;1;1),(1;1;0),(1;0;1)\}$.

Bài làm

$ Ma trận của f trong cơ sở chính tắc E_0 là A = E_0^{-1} f(E_0) = f(E_0) = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 1 \\ 3 & -1 & 2 \end{pmatrix} $

$ Ma trận chuyển cơ sở từ E_0 sang E là P = E_0^{-1} E = E = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}. $

So $d\delta$

$ ctắc \begin{array}{ccc}\n & A & \rightarrow & \text{ctắc} \\
P \downarrow & & & \downarrow P \\
E' & \xrightarrow{P^{-1}AP} & E'\n\end{array} $

$ Ma trận cần tìm P^{-1}AP = E^{-1}AE = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}^{-1} \begin{pmatrix} 1 & 2 & -3 \\ 2 & 1 & 1 \\ 3 & -1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -4 & -7 \\ 2 & 8 & 10 \\ 0 & -4 & -5 \end{pmatrix}. $

Ví dụ 6.10 Cho axtt f: $R^3 \longrightarrow R^3$ có ma trận trong cơ sở E $= \{(1$, 2, 1), (1, 1, 2), (1, 1, $1)\}\là$

$ A = \begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 4 \\ 1 & 1 & 2 \end{pmatrix}. $

Tìm ma trận của f trong cơ sở E' $= \{(1,2,3)$, (2,3,5), $(5,8,4)\}$.

Bài làm

Sơ đồ

$ \begin{array}{ccc}\nE & \xrightarrow{A} & E \\
P \downarrow & & \downarrow P \\
E' & \xrightarrow{P^{-1}AP} & E'\n\end{array} $

Ma trận chuyển cơ sở từ E sang E' là P $= E^{-1}E'$.

Ma trận của f trong cơ sở E' là

$ P^{-1}AP = E'^{-1}EAE^{-1}E' = \frac{1}{9}\begin{pmatrix} 59 & 40 & -221 \\ -53 & -37 & 206 \\ -5 & -4 & 23 \end{pmatrix}. $

Ví dụ 6.11 Cho axtt f: $R^3 \longrightarrow R^3$ có ma trận trong cơ sở E $= \{(1$, 2, 1), (1, 1, 2), (1, 1, $1)\}\là$

$ A = \begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 4 \end{pmatrix}. $

$ \begin{pmatrix} 1 & 1 & 3 \end{pmatrix} $

Tìm ma trận của f trong cơ sở chính tắc F $= \{(1,0,0)$, (0,1,0), $(0,0,1)\}$. Từ đó suy ra f(x).

Bài làm

Sơ đồ

$ \begin{array}{ccc}\n {\rm ct \acute{a}c} & \xrightarrow{\quad A} & \mbox{ct \acute{a}c} \\
 P \downarrow & & \downarrow P \\
 E' & \xrightarrow{\quad P^{-1}AP} & E'\n \end{array} $

Ma trận chuyển có sở từ E sang F là P $= E^{-1} \cdot$ F $= E^{-1}$.

Ma trận của f trong cơ sở chính tắc là

$ B = P^{-1}AP = EAE^{-1} = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 4 \\ 1 & 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \\ 2 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix}^{-1} \xrightarrow{\text{duing case}} \begin{pmatrix} 18 & -4 & -6 \\ 20 & -4 & -7 \\ 27 & -6 & -9 \end{pmatrix} $



$\Rightarrow$ f(x) $= (18x_1$ - $4x_2$ - $6x_3; 20x_1$ - $4x_2$ - $7x_3; 27x_1$ - $6x_2$ - $9x_3)$. (??)

### Định nghĩa 6.4 (Hai ma trận đồng dạng).

Hai ma trận vuông A, B gọi là đồng dạng nếu tồn tại ma trận khả nghịch P thỏa

$P^{-1}AP =$ B.

Mệnh đề cho $axt<br/>t<math display="inline">f:$ V $\longrightarrow$ V.

$<math display="inline">Alà$ ma trận $của<math display="inline">f$ trong cơ $sở<math display="inline">E$.

$<math display="inline">Blà$ ma trận $của<math display="inline">f$ trong cơ sở $<math display="inline">F$.

Khi đó A và B đồng dạng.



# Chương 7

Nội dung

1) Trị riêng - véc tơ riêng ma trận

2) Chéo hóa ma trận

3) Chéo hóa ma trận đối xứng thực

4) Trị riêng - véc tơ riêng ánh xạ tuyến

tính

5) Chéo hóa ánh xạ tuyến tính

Trị riêng - véc tơ riêng

## 7.1 Trị riêng - véc tơ riêng

Trị riêng - véc tơ riêng của ma trận vuông A.

Số $\lambda$ gọi là trị riêng của ma trận A nếu tồn tại véc tơ x khác không

thỏa

Ax $= \lambda$ x

Khi đó, x gọi là véc tơ riêng ứng với trị riêng $\lambda$ của ma trận A.

x $\neq$ 0 là VTR của A nếu Ax cùng phương với x.

$ Ví dụ 7.1 Cho A = \begin{pmatrix} 1 & 6 \\ 5 & 2 \end{pmatrix} và u = \begin{pmatrix} 6 \\ -5 \end{pmatrix}, v = \begin{pmatrix} 3 \\ -2 \end{pmatrix}. $

$ Ta có: Au = \begin{pmatrix} 1 & 6 \\ 5 & 2 \end{pmatrix} \begin{pmatrix} 6 \\ -5 \end{pmatrix} = \begin{pmatrix} -24 \\ 20 \end{pmatrix} = -4 \begin{pmatrix} 6 \\ -5 \end{pmatrix} = -4u: u là VTR ứng với TR \lambda = -4. $

$ Av = \begin{pmatrix} 1 & 6 \\ 5 & 2 \end{pmatrix} \begin{pmatrix} 3 \\ -2 \end{pmatrix} = \begin{pmatrix} -9 \\ 11 \end{pmatrix}: không cùng phương với x, dó đó x không là VTR của A. $

$ Ví dụ 7.2 Cho A = \begin{pmatrix} 3 & 4 \\ 6 & 5 \end{pmatrix}, \lambda_1 = -1, \lambda_2 = 3. Số nào là TR của A? $

Bài làm



a) Xét hệ phương trình Ax $= \lambda_1$ x

$ \Leftrightarrow \begin{pmatrix} 3 & 4 \\ 6 & 5 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = -1 \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \Longleftrightarrow \begin{cases} 3x_1 + 4x_2 = -x_1 \\ 6x_1 + 5x_2 = -x_2 \end{cases} \Longleftrightarrow \begin{cases} 4x_1 + 4x_2 = 0 \\ 6x_1 + 6x_2 = 0 \end{cases} \begin{cases} x_1 = \alpha \\ x_2 = -\alpha \end{cases}. $

$ Như vậy x = \begin{pmatrix} \alpha \\ -\alpha \end{pmatrix}, \alpha \neq 0 là các VTR ứng với TR \lambda = -1 của A. $

b) Xét hệ phương trình Ax $= \lambda_2$ x

$ \Leftrightarrow \begin{pmatrix} 3 & 4 \\ 6 & 5 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 3 \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \Longleftrightarrow \begin{cases} 3x_1 + 4x_2 = 3x_1 \\ 6x_1 + 5x_2 = 3x_2 \end{cases} \Longleftrightarrow \begin{cases} 4x_2 = 0 \\ 6x_1 + 2x_2 = 0 \end{cases} \begin{cases} x_1 = 0 \\ x_2 = 0 \end{cases}. $

Vì hệ có nghiệm duy nhất x $=$ 0 nên $\lambda_2 =$ 3 không phải TR của ma trận A.

### Dịnh nghĩa 7.1 (Các khái niệm cơ bản)

Giả sử $\lambda_0$ là Tr của ma trận vuông A $\iff \exists x_0 \neq$ 0 : $Ax_0 = \lambda x_0 \iff Ax_0$ - $\lambda_0$ x $=$ 0 $\iff$ (A - $\lambda$ I)x $=$ 0.

Vì hệ thuần nhất có nghiệm khác không nên

$\det(A$ - $\lambda$ I) $=$ 0: gọi là phương trình đặc trưng của A.

Da thức $P_A(\lambda) = \det(A$ - $\lambda$ I) gọi là đa thức đặc trưng của A.

Tìm TR-VTR của ma trận vuông

Bước 1) Lập phương trình đặc trưng $\det(A$ - $\lambda$ I) $=$ 0.

Bước 2) Giải phương trình đặc trưng tìm trị riêng.

Bước 3) Với mỗi TR $\lambda_i$, giải hệ (A - $\lambda_i$ I)x $=$ 0:

Tìm VTR ứng với TR $\lambda_i$.

### Dịnh nghĩa 7.2.

i) Bội đại số của trị riêng $\lambda_i$ là bội nghiệm của $\lambda_i$ trong phương trình đặc trưng.

ii) Không gian con riêng của trị riêng $\lambda_i$ là không gian nghiệm của hệ (A - $\lambda_i)x =$ 0, kí hiệu là $E_{\lambda_i}$.

iii) Bội hình học của $\lambda_i$ là số chiều của $E_{\lambda_i}:$ BHH $= \dim(E_{\lambda_i})$.

Dinh lý 7.3 Cho A là ma trận vuông.

i) Cơ sở của các KG con riêng lập thành một hệ độc lập tuyến tuyến tính.

ii) 1 $\leq$ BHH $\leq B\mathbb{C}S$ cho tất cả các trị riêng $\lambda_i$.

Chứng minh: Theo dõi bài giảng trên lớp.

$ Ví dụ 7.3 Cho A = \begin{pmatrix} 1 & 4 \\ 2 & 3 \end{pmatrix}. Tìm tất cả các TR, cơ sở và chiều của KG con riêng tương ứng. $

Bài làm

$ Phương trình đặc trưng \det(A - \lambda I) = 0 \Longleftrightarrow \begin{vmatrix} 1 - \lambda & 4 \\ 2 & 3 - \lambda \end{vmatrix} = 0 \Longleftrightarrow (1 - \lambda)(3 - \lambda) - 2.4 = 0 $

$ \iff \lambda^2 - 4\lambda - 5 = 0 \iff \begin{cases} \lambda_1 = -1 \text{ nghięm } \text{don: BDS=1} \\ \lambda_2 = 5 \text{ nghięm } \text{don: BDS=1} \end{cases}. $

$\lambda_1 =$ -1, giải hệ (A - $\lambda_1$ I)x $=$ 0

$ \iff \begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c $



$ \iff x = \begin{pmatrix} -2\alpha \\ \alpha \end{pmatrix} = \alpha \begin{pmatrix} -2 \\ 1 \end{pmatrix}. Cơ sở của E_{-1} là \left\{ \begin{pmatrix} -2 \\ 1 \end{pmatrix} \right\} và BHH = \dim(E_{-1}) = 1. $

$ \lambda_2 = 5, giải hệ (A - \lambda_2 I)x = 0 \Longleftrightarrow \begin{bmatrix} 2 & 4 & 0 \\ 2 & 4 & 0 \end{bmatrix} \Longleftrightarrow x = \begin{pmatrix} \alpha \\ \alpha \end{pmatrix} = \alpha \begin{pmatrix} 1 \\ 1 \end{pmatrix}. $

$ Cơ sở của E_5 là \left\{ \begin{pmatrix} 1 \\ 1 \end{pmatrix} \right\} và BHH = \dim(E_5) = 1. $

$ Ví dụ 7.4 Cho A = \begin{pmatrix} 3 & 1 & 1 \\ 2 & 4 & 2 \\ 1 & 1 & 3 \end{pmatrix}. Tìm tất cả các TR, cơ sở và chiều của KG con riêng tương ứng. $

Bài làm.

Phương trình đặc trưng: $\det(A$ - $\lambda$ I) $=$ 0

$ \Longleftrightarrow \begin{vmatrix} 3-\lambda & 1 & 1 \\ 2 & 4-\lambda & 2 \\ 1 & 1 & 3-\lambda \end{vmatrix} = 0 \Longleftrightarrow (3-\lambda)\begin{vmatrix} 4-\lambda & 2 \\ 1 & 3-\lambda \end{vmatrix} + 1\begin{vmatrix} 2 & 2 \\ 1 & 3-\lambda \end{vmatrix} + 1\begin{vmatrix} 2 & 4-\lambda \\ 1 & 1 \end{vmatrix} = 0 $

$ \iff (3 - \lambda)(\lambda^2 - 7\lambda + 10) + (-2\lambda + 4) + (\lambda - 2) = 0 \iff -\lambda^3 + 10\lambda^2 - 28\lambda + 24 = 0
\left[\begin{array}{ccc}\lambda_1 = 2 \text{ nothing to } 200 \\
\end{array}\right] $

$ \iff \begin{cases} \lambda_1 = 2 \text{ nghiệpi kép: BDS=2,} \\ \lambda_2 = 6 \text{ nghiệm đơn: BDS=1. $

$\lambda_1 =$ 2, giải hệ

$ (A - \lambda_1 I)x = 0 \Longleftrightarrow \begin{pmatrix} 3-2 & 1 & 1 \\ 2 & 4-2 & 2 \\ 1 & 1 & 3-2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = 0 \Longleftrightarrow \begin{bmatrix} 1 & 1 & 1 & 0 \\ 2 & 2 & 2 & 0 \\ 1 & 1 & 1 & 0 \end{bmatrix} $

$ \Leftrightarrow x = \alpha \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}. Cơ sở E_2 là \left\{ \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} \right\} và BHH = \dim(E_2) = 2. $

$\lambda_1 =$ 6, giải hệ

$ (A - \lambda_2 I)x = 0 \Longleftrightarrow \begin{vmatrix} -3 & 1 & 1 & 0 \\ 2 & -2 & 2 & 0 \\ 1 & 1 & -3 & 0 \end{vmatrix} $

$ Cơ sở của E_6 là \left\{ \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \right\} và BHH = \dim(E_6) = 1. $

Tính chất cho A là ma trận vuông trên C.

i) Mọi ma trận cấp n có đúng n trị riêng tính cả bội.

ii) Tổng các TR bằng tr(A): tổng các phần tử trên đường chéo

chính.

iii) Tích các Tr bằng det(A).

iv) Nếu $\lambda_0$ là TR của A thì $\lambda^m$ là TR của $A^m$, $\forall$ m $\in \mathbb{Z}^+$.

v) Nếu $\lambda_0 \neq$ 0 thì $\frac{1}{\lambda_0}$ là TR của $A^{-1}$.

Ví dụ 7.5 Tìm tất cả các trị riêng của ma trận cấp n

$ A = \begin{pmatrix} 1 & 1 & \dots & 1 \\ 1 & 1 & \dots & 1 \\ \vdots & \vdots & \vdots & \vdots \\ 1 & 1 & \dots & 1 \end{pmatrix}. $



Bài làm

Dễ thấy $\det(A) =$ 0 nên A có TR $\lambda =$ 0.

r(A - 0I) $=$ r(A) $=$ 1 $\Longrightarrow$ BHH $=$ n - 1 $\Longrightarrow$ B $\times$ S $\geq$ n - 1.

gọi n TR của A là $\lambda_1 = \lambda_2 = \cdots = \lambda_{n-1} =$ 0, $\lambda_n$.

Vì $\lambda_1$ + $\lambda_2$ + $\cdots$ + $\lambda_{n-1}$ + $\lambda_n =$ tr(A) $=$ n $\Longrightarrow \lambda_n =$ n.

Như vậy A có n-1 TR 0 và 1 TR bằng n.

Da thức đặc trưng ma trận cấp 3

$P_A(\lambda) = -\lambda^3$ + tr(A) - $(A_{11}$ + $A_{22}$ + $A_{33})\lambda$ + $\det(A)$.

Tính đa thức đặc trưng của ma trận cấp 3 dễ sai. Công thức trên cho ta tính đa thức đặc trưng ma trận

cấp 3 đơn gian hơn.

$ Ví dụ 7.6 Tìm tất cả cá TR, cơ sở KG con riêng của A = \begin{pmatrix} 15 & -10 & -10 \\ 9 & -12 & -8 \\ 4 & -4 & -6 \end{pmatrix} $

Bài làm

tr(A) $=$ 15 - 12 - 6 $=$ -3, det(A) $=$ 12

$ A_{11} + A_{22} + A_{33} = \begin{vmatrix} -12 & -8 \\ -4 & -6 \end{vmatrix} + \begin{vmatrix} 15 & -16 \\ 4 & -6 \end{vmatrix} + \begin{vmatrix} 15 & -18 \\ 9 & -12 \end{vmatrix} = 40 - 26 - 18 = -4. $

Da thức đặc trưng: $P(\lambda) = -\lambda^3$ - $3\lambda^2$ + $4\lambda$ + 12.

Suy ra TR: $\lambda_1 =$ -3, $\lambda_2 =$ -2, $\lambda_3 =$ 2.

$ \lambda_1 = -3, giải hệ \begin{bmatrix} 18 & -18 & -16 & 0 \\ 9 & -9 & -8 & 0 \\ 4 & -4 & -3 & 0 \end{bmatrix}. Cơ sở E_{-3} là \left\{ \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} \right\}. $

$ \lambda_1 = -2, giải hệ \begin{bmatrix} 17 & -18 & -16 \ 9 & -10 & -8 \ 4 & -4 & -4 \end{bmatrix} \begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix}. Cơ sở E_{-2} là \left\{ \begin{bmatrix} 2 \ 1 \ 1 \end{bmatrix} \right\}. $

$ \lambda_1 = 2, giải hệ \begin{pmatrix} 13 & -18 & -16 \\ 9 & -14 & -8 \\ 4 & -4 & -8 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}. Cơ sở E_2 là \left\{ \begin{pmatrix} 4 \\ 2 \\ 1 \end{pmatrix} \right\}. $

Chéo hóa ma trận

## 7.2 Chéo hóa ma trận

$\text{Dinh}$ lý 7.4.

Hai ma trận đồng dạng thì cùng đa thức đặc trưng.

Chi $\circ:$

$\bullet$ 2 ma trận đồng dạng cùng tập trị riêng nhưng không cùng véc tơ riêng.

$\bullet$ 2 ma trận cùng đa thức đặc trưng thì chưa chắc dồng dạng:

$ Xem 2 ma trận A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} và I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} cùng đa thức đặc trưng nhưng không đồng dạng. $

### Dịnh nghĩa 7.5 (Ma trận chéo hóa được).

Ma trận A gọi là chéo hóa được nếu A đồng dạng với ma trận chéo.

Tức là tồn tại ma trận P khả nghịch sao cho $P^{-1}AP =$ D là ma trận chéo.

Chi $\circ:$



$ • Không phải ma trận nào cũng chéo hóa được, ví dụ như A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}. $

• Chéo hóa ma trận A là cần tìm ma trận P và ma trận chéo D thỏa $P^{-1}AP =$ D.

- Ta tìm cấu trúc ma $trận<math display="inline">Pvà <math display="inline">Dnhư$ sau:

Giả sử A được chéo hóa bởi ma trận P và D:

$ P = \begin{pmatrix} P_1 & P_2 & \dots & P_n \\ \|\ & \|\ & \|\ & \|\end{pmatrix}, D = \begin{pmatrix} \lambda_1 & 0 & \dots & 0 \\ 0 & \lambda_2 & \dots & \\ \dots & \dots & \dots & \dots \\ 0 & 0 & \dots & \lambda_n \end{pmatrix} $

Ta có $P^{-1}AP =$ D $\Longleftrightarrow$ AP $=$ PD.

$ Lấy cột thứ k: A.P_k = \begin{pmatrix} P_1 & P_2 & \dots & P_n \\ \parallel & \parallel & & \end{pmatrix} \begin{pmatrix} 0 \\ \dots \\ \lambda_k \\ \dots \\ 0 \end{pmatrix} = \lambda_k.P_k, \forall k = \overline{1,n}. $

Diều này chứng tỏ các cột $P_k$ của ma trận P là các VTR ứng với TR $\lambda_k$ của ma trận A.

Các phần tử chéo của D là các TR của A.

### Định lý 7.6 Ma trận vuông A chéo hóa được khi và chỉ khi tồn tại n VTR độc lập tuyến tính.

Hệ quả

$\bullet$ A có n TR phân biệt thì chéo hóa được.

$\bullet$ A chéo hóa được khi và chỉ khi $BHH=BDS$ cho tất cả

các TR.

$D\hat{\mathrm{e}}$ chéo hóa ma trận A, ta cần tìm tất cả các TR và cơ sở KG con riêng

$ Ví dụ 7.7 Chéo hóa ma trận A = \begin{pmatrix} 1 & 3 & 3 \\ -3 & -5 & -3 \\ 3 & 3 & 1 \end{pmatrix}. $

Bài làm

$ Da thức đặc trưng P(\lambda) = -\lambda^3 - 3\lambda^2 + 4. Tri riêng \begin{bmatrix} \lambda_1 = 1 & (BDS=1) \\ \lambda_2 = -2 & (BDS=2) \end{bmatrix}.
λ<sub>1</sub> = 1, giải hệ (A − 1I)x = 0 \iff \begin{bmatrix} 0 & 3 & 3 & 0 \\ -3 & -6 & -3 & 0 \\ 3 & 3 & 0 & 0 \end{bmatrix}. Cơ sở E_1 là u_1 = \begin{pmatrix} 1 \\ -1 \\ 1 $

$\lambda_2 =$ -2, giải hệ (A + 2I)x $=$ 0

$ \Leftrightarrow \begin{vmatrix} 3 & 3 & 3 \\ -3 & -3 & -3 \\ 3 & 3 & 3 \end{vmatrix} \begin{vmatrix} 0 \\ 0 \\ 0 \end{vmatrix}. Cơ sở E_{-2} là u_2 = \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}, u_3 = \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix} BHH=2=BDS. $

Vậy A chéo hóa được:

$ P = \begin{pmatrix} 1 & -1 & -1 \\ -1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{pmatrix} $

$ Ví dụ 7.8 Chéo hóa ma trận A = \begin{pmatrix} 2 & 4 & 3 \\ -4 & -6 & -3 \\ 3 & 3 & 1 \end{pmatrix}. $



Bài làm

$ Da thức đặc trưng: P(\lambda) = -\lambda^3 - 3\lambda^2 + 4. Trị riêng \begin{vmatrix} \lambda_1 = 1 & (BDS=1) \\ \lambda_2 = -2 & (BDS=2) \end{vmatrix}. $

$ \lambda_2 = -2, giải hệ \begin{bmatrix} 4 & 4 & 3 & 0 \\ -4 & -4 & -3 & 0 \\ 3 & 3 & 3 & 0 \end{bmatrix}. r = 2 \Longrightarrow BHH = \dim = 3 - 2 = 1 < BDS. $

Vậy A không chéo hóa được.

$ Ví dụ 7.9 Chéo hóa A = \begin{pmatrix} 0 & -8 & 6 \\ -1 & -8 & 7 \\ 1 & -14 & 11 \end{pmatrix} và tính A^{2013}. $

Bài làm

Sinh viên tự tính TR và VTR. Suy ra

$ P = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 1 & 3 & 5 \end{pmatrix}, \quad D = \begin{pmatrix} -2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} $

$ Ta có P^{-1}AP = D \Longleftrightarrow A = PDP^{-1} \Longrightarrow A^2 = PDP^{-1}.PDP^{-1} = PD^2P^{-1}.Suy ra A^{2013} = PD^{2013}P^{-1} = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 1 & 3 & 5 \end{pmatrix} \begin{pmatrix} -2^{2013} & 0 & 0 \\ 0 & 2^{2013} & 0 \\ 0 & 0 & 3^{2013} \end{pmatrix} \begin{pmatrix} 1 & 1 & -1 \\ -2 & 3 & -1 \\ 1 & -2 & 1 \end{pmatrix}. $

$ Ví dụ 7.10 Chéo hóa A = \begin{pmatrix} 5 & 0 & 0 & 0 \\ 0 & 5 & 0 & 0 \\ 1 & 4 & -3 & 0 \\ -1 & -2 & 0 & -3 \end{pmatrix} và tính A^m. $

Sinh viên làm tương tự ví dụ trên.

$ Ví dụ 7.11 Tìm ma trận vuông có TR là 2, -3, 1 và có VTR tương ứng là v_1 = \begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}, v_2 = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}, v_3 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} $

Bài làm

A được chéo hóa bởi ma trận P và D như sau

$ P = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 1 \end{pmatrix}, D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 1 \end{pmatrix} $

Suy ra ma trận A cần tìm A $= PDP^{-1}$.

Chéo hóa ma trận đối xứng thực bởi ma trận trực giao

## 7.3 Chéo hóa ma trận đối xứng thực bởi ma trận trực giao

Dinh nghĩa

i) Ma trận vuông thực A gọi là đối xứng thực nếu AT $=$ A.

ii) Ma trận vuông P gọi là trực giao nếu $P^{-1} = P^{T}$.

iii) Ma trận A gọi là chéo hóa trực giao được nếu tồn tại ma trận

trực giao P và ma trận chéo D thỏa

A $= P^{-1}DP = P^TDP$.

Câu trúc ma trận trực giao



$<math display="inline">\mathbf{H}ệ$ quả Ma trận vuông $<math display="inline">A$ là trực giao nếu các cột của

A tạo thành 1 cơ sở trực chuẩn.

Dinh lý. cho A là ma trận đối xứng thực. Khi đó

Trị riêng A là những số thực.

$\mathbf{1}$

Các VTR ứng với các TR khác nhau thì vuông góc.

A luôn chéo hóa trực giao được.

111)

Mọi ma trận chéo hóa trực giao được là ma trận đối xứng.

Các bước chéo hóa trực giao ma trận đối xứng thực

Bước 1 Lập phương trình đặc trưng. Giải tìm trị riêng.

Bước 2 Tìm cơ sở TRỰC CHUẨN của các KG con riêng.

Bước 3 Thành lập ma trận P và D.

Chú $\dot{y}:$

• Ma trận đối xứng thực luôn chéo hóa được nên không cần xác định BHH và BĐS.

• Để tìm cơ sở trực chuẩn của một không gian con riêng nào đó ta chọn một cơ sở tùy ý rồi dùng quá

trình Gram – Schmidt (nếu cần).

$ Ví dụ 7.12 Chéo hóa trực giao ma trận A = \begin{pmatrix} 3 & -2 & 4 \\ -2 & 6 & 2 \\ 4 & 2 & 3 \end{pmatrix}. $

Bài làm

Da thức đặc trưng $P(\lambda) = -\lambda^3$ + $12\lambda^2$ - $21\lambda$ - 98. Trị riêng: $\lambda_1 =$ -2, $\lambda_2 =$ 7.

$ \lambda_1 = -2. Cơ sở E_{-2} là v_1 = \begin{pmatrix} 2 \\ 1 \\ -2 \end{pmatrix}. Cơ sở trực chuẩn f_1 = \begin{pmatrix} \frac{2}{3} \\ \frac{1}{3} \\ -\frac{2}{3} \end{pmatrix}. $

$ \lambda_2 = 7. Cơ sở E_7 là v_2 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, v_3 = \begin{pmatrix} -1 \\ 2 \\ 0 \end{pmatrix}. Tìm cơ sở trực chuẩn bằng Gram-Schmidt: $

$ e_2 = v_2 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \qquad \Longrightarrow f_2 = \begin{pmatrix} \overline{\sqrt{2}} \\ 0 \\ \frac{1}{\sqrt{2}} \end{pmatrix}. $

$ e_3 = v_3 - \frac{(v_3, e_2)}{(e_2, e_2)} e_2 = \begin{pmatrix} -1 \\ 2 \\ 0 \end{pmatrix} - \frac{-1}{2} \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} -1 \\ 4 \\ 1 \end{pmatrix} \Longrightarrow f_3 = \begin{pmatrix} \frac{1}{\sqrt{18}} \\ \frac{4}{\sqrt{18}} \\ 1 \end{pmatrix} $

Cơ sở trực chuẩn của $E_7$ là $\{f_2$, $f_3\}$.

Vậy ma trận trực giao P và ma trận chéo D là

$ P = \begin{pmatrix} \frac{2}{3} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{18}} \\ \frac{1}{3} & 0 & \frac{4}{\sqrt{18}} \\ \frac{-2}{3} & \frac{1}{\sqrt{18}} & \frac{1}{\sqrt{18}} \end{pmatrix}, \qquad D = \begin{pmatrix} -2 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 7 \end{pmatrix} $

$ Ví dụ 7.13 Hãy chéo hóa ma trận đối xứng thực A = \begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix} $



Sinh viên làm tương tự. Kết quả

$ P = \begin{pmatrix} \frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & 0 & \frac{2}{\sqrt{6}} \end{pmatrix}, \qquad D = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix} $

Ví dụ 7.14 Tìm ma trận đối xứng thực có 3 trị riêng lần lượt là 2, -2, 1

Hướng dẫn

$ Thành lập ma trận D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 1 \end{pmatrix}. $

Thành lập ma trận P bằng cách chọn cơ sở (khác chéo) tùy ý, ví dụ như E $= \{(1,0,1)$, (1,1,1), $(1,0,0)\}$.

Trực chuẩn E bằng Gram-Schmidt. Lập P từ các véc tơ cơ sở trực chuẩn.

Khi đó, ma trận A cần tìm là A $= PDP^T$.

Trị riêng - véc tơ riêng của ánh xạ tuyến tính

## 7.4 Trị riêng - véc tơ riêng của ánh xạ tuyến tính

### Dịnh nghĩa 7.7 Cho KGVT V trên trường số K và axtf: V \longrightarrow V.

$S\acute{o} \lambda$ gọi là TR của f nếu tồn tại véc tơ x $\neq$ 0 thỏa

f(x) $= \lambda$ x.

Khi đó, x gọi là VTR ứng với $TR\lambda$ của ma trận A.

Chú ý: x $\neq$ 0 là VTR của f nếu x và f(x) cùng phương.

Trong chương trước, xem ánh xạ tuyến tính như một ma trận: TR và VTR của axtt giống như TR và VTR

ma trận.

Ví dụ 7.15 Cho axtt f là phép chiếu vuông góc xuống mặt phẳng x - y + 2z $=$ 0. Tìm TR và VTR của f.

Bài làm

$ Véc tơ pháp tuyến n = (1; -1; 2) \Longrightarrow f(n) = 0.n: n là VTR ứng với TR \lambda_1 = 0.Cặp véc tơ chỉ phương a_1 = (1; 1; 0), a_2 = (2; 0; -1) \Longrightarrow \begin{cases} f(a_1) = 1.a_1 \\ f(a_2) = 1.a_2 \end{cases}. $

Vậy $a_1$, $a_2$ là 2 VTR ứng với TR $\lambda_2 =$ 1.

Vì f: $R^3 \longrightarrow R^3$ nên không còn véc tơ riêng nào khác.

Cho E là cơ sở của KGVT V trên K. Axtt f: V $\longrightarrow$ V.

Gọi A là ma trận của f trên trong cơ sở E.

giả sử $\lambda_0$ là TR của f: $\exists x_0 \neq$ 0 và $f(x_0) = \lambda x_0$.

$\Longleftrightarrow [f(x_0)]_E = \lambda_0[x_0]_E \Longleftrightarrow A[x_0]_E = \lambda_0[x_0]_E$.

Suy ra $[x_0]_E$ là VTR ứng với TR $\lambda_0$ của ma trận A.

Trị riêng - véc tơ riêng của ánh xạ tuyến tính

Cho A là ma trận của $axt<br/>t<math display="inline">f:$ V $\longrightarrow$ V trong cơ sở E.

i) Trị riêng A cũng là TR của f và ngược lại.

$<math display="inline">x_0là$ VTR của $<math display="inline">Aứng$ với $TR<math display="inline">\lambda_0thì$ véc $tơ<math display="inline">xsao cho<math display="inline">[x]_E = x_0là$

$\overline{11})$

VTR của f ứng với TR $\lambda_0:$

$x=E.x_0$



Chú $\t{y}:$

• TR của axt và ma trận giống nhau.

VTR của axtt và ma trận nhìn chung khác nhau.

$<math display="inline">\bullet$

• Nếu E là cơ sở chính tắc thì VTR của ma trận và axt giống nhau.

Ví dụ 7.16 Cho ánh xạ tuyến tính f : $\mathbb{R}_3 \to \mathbb{R}_3$, biết

f(x) $= f(x_1$, $x_2$, $x_3) = (5x_1$ - $10x_2$ - $5x_3$, $2x_1$ + $14x_2$ + $2x_3$, $-4x_1$ - $8x_2$ + $6x_3)$.

Tìm trị riêng, véc-tơ riêng của ánh xạ tuyến tính f.

Bài làm

$ Chọn E là cơ sở chính tắc. Ma trận của f trong E là A = \begin{pmatrix} 5 & -10 & -3 \\ 2 & 14 & 2 \\ 4 & 8 & 6 \end{pmatrix}. $

Tìm TR của A: $\lambda_1 =$ 5, $\lambda_2 =$ 10.

$ \lambda_1 = 5. Véc tơ riêng v_1 = \begin{pmatrix} 5 \\ -2 \\ 4 \end{pmatrix} \alpha, \alpha \neq 0. $

$ \lambda_2 = 10. Véc tơ riêng v_2 = \begin{pmatrix} -2\alpha - \beta \\ \alpha \\ \beta \end{pmatrix}, \alpha^2 + \beta^2 > 0. $

Vì E là cơ sở chính tắc nên TR-VTR của A cũng là TR-VTR của f.

Ví dụ 7.17 Cho ánh xạ tuyến tính f : $\mathbb{R}_3 \to \mathbb{R}_3$, biết

f(1; 1; 1) $=$ (2; 1; 3), f(1; 0; 1) $=$ (6; 3; 5), f(1; 1; 0) $=$ (-2; -1; -3).

$T\imath$ m TR-VTR của axti f.

Bài làm

Chọn cơ sở E $= \{(1$, 1, 1), (1, 0, 1), (1, 1, $0)\}\$. Ma trận của f trong cơ sở E là

$ A = E^{-1}f(E) = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 & -2 \\ 1 & 3 & -1 \\ 3 & 5 & 3 \end{pmatrix} = \begin{pmatrix} 2 & 2 & -2 \\ 1 & 3 & -1 \\ 1 & 1 & 1 \end{pmatrix}. $

Tìm TR của A: $\lambda_1 =$ 0, $\lambda_2 =$ 2, $\lambda_3 =$ 4. Đây cũng là TR của $axt<br/>t<math display="inline">f$.

$ \lambda_1 = 0 \Longrightarrow \text{VTR} của A là x = \begin{pmatrix} \alpha \\ 0 \\ \alpha \end{pmatrix}, \alpha \neq 0. $

Véc tơ riêng của f ứng với TR $\lambda_1$ là

$ v_1 = Ex = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} \alpha \\ 0 \\ \alpha \end{pmatrix} = \begin{pmatrix} 2\alpha \\ 2\alpha \\ \alpha \end{pmatrix}, \alpha \neq 0. $

Tương tự cho trị riêng $\lambda_2$ và $\lambda_3:$

$ v_2 = \begin{pmatrix} 2\alpha \\ \alpha \\ \alpha \end{pmatrix}, v_3 = \begin{pmatrix} 2\alpha \\ \alpha \\ 2\alpha \end{pmatrix}, \alpha \neq 0. $

Ví dụ 7.18 Cho axtt f: $R^3 \longrightarrow R^3$ có ma trận trong cơ sở E $= \{(1,1,1)$, (1,1,2), $(1,2,1)\}\là$

$ A = \begin{pmatrix} 2 & -2 & 1 \\ -2 & -1 & -2 \\ 14 & 25 & 14 \end{pmatrix} $

$T\hat{\imath}m$ TR-VTR của f.



Bài làm

TR của A là $\lambda_1 =$ 3, $\lambda_2 =$ 6. Đây cũng là TR của f.

$ \lambda_1 = 3 \Longrightarrow \text{VTR} của A là u_1 = \begin{pmatrix} \alpha \\ -\alpha \\ \alpha \end{pmatrix}, \alpha \neq 0. $

VTR của f ứng với TR $\lambda_1$ là

$ v_1 = E.u_1 = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 2 \\ 1 & 2 & 1 \end{pmatrix} \begin{pmatrix} \alpha \\ -\alpha \\ \alpha \end{pmatrix} = \begin{pmatrix} \alpha \\ 2\alpha \\ \alpha \end{pmatrix}, \alpha \neq 0. $

$ Tương tự cho trị riêng \lambda_2 : v_2 = \begin{pmatrix} 5\alpha \\ 13\alpha \\ 3\alpha \end{pmatrix}, \alpha \neq 0. $

Ví dụ 7.19 Cho axtt f: $R^3 \longrightarrow R^3$ biết f có 3 TR là 2, 1, 0 và 3 VTR tương ứng là (1; 1; 1), (1; 2; 1), (1; 1; 2).

$T\hat{i}m$ f(x).

Bài giải

Theo giả thiết ta có:

f(1; 1; 1) $=$ 2(1; 1; 1) $=$ (2; 2; 2), f(1; 2; 1) $=$ 1.(1; 2; 1), f(1; 1; 2) $=$ 0.(1; 1; 2) $=$ 0.

Từ đây suy ra f(x).

Chéo hóa ánh xạ tuyến tính

## 7.5 Chéo hóa ánh xạ tuyến tính

### Dịnh nghĩa 7.8 Axtt f: V \longrightarrow V gọi là chéo hóa được nếu tồn tại cơ sở B sao cho ma trận của f trong

cơ sở này là ma trận chéo.

Chéo

### Dịnh lý 7.9 Axtt f: V \longrightarrow V chéo hóa được khi và chỉ khi f có n véc tơ riêng độc lập tuyến tính.

Khi đó cơ sở B gồm các véc tơ riêng.

Các bước chéo hóa ánh xạ tuyến tính:

Bước 1) Chọn 1 cơ sở E của KGVT V. Tìm ma trận A của f trong cơ sở E.

Bước 2) Chéo hóa ma trận A (nếu được).

Bước 3) Kết luận:

i) Nếu A chéo hóa được thì f chéo hóa được và ngược lại

ii) Kết luận: Giả sử A chéo hóa được bởi ma trận P và ma trận chéo D:

Cơ sở B gồm các VTR của f và ma trận chéo cần tìm là D

Ví dụ 7.20 Cho axtt f: $\mathbb{R}^3 \longrightarrow \mathbb{R}^3$ biết f(x) $= (2x_1$ - $2x_2$ - $x_3; -2x_1$ - $1x_2$ - $2x_3; 14x_1$ + $25x_2$ + $14x_3)$.

Chéo hóa f (nếu được).

Bài làm

$ Ma trận của f trong cơ sở chính tắc A = \begin{pmatrix} 2 & -2 & -1 \\ -2 & -1 & -2 \\ 14 & 25 & 14 \end{pmatrix}. $

$ TR của A là \lambda_1 = 3, \lambda_2 = 6(B \times S = 2).
\lambda_2 = 6 \Longrightarrow \text{VTR} của A là v_2 = \begin{pmatrix} -1 \\ -2 \\ 8 \end{pmatrix} \alpha : BHH = 1 < B \times S. $

A không chéo hóa được do đó f cũng không chéo hóa được.



Ví du 7.21 Cho axte f : $\mathbb{R}_3 \to \mathbb{R}_3$, biết

f(1; 1; 1) $=$ (1; -7; 9), f(1; 0; 1) $=$ (-7; 4; -15), f(1; 1; 0) $=$ (-7; 1; -12).

Chéo hóa f (nếu được).

Bài làm

Ma trận của f trong cơ sở E $= \{(1;1;1)$, (1;0;1), $(1;1;0)\}\là$

$ A = E^{-1}f(E) = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}^{-1} \begin{pmatrix} 1 & -7 & -7 \\ -7 & 4 & 1 \\ 9 & -15 & -12 \end{pmatrix} = \begin{pmatrix} 1 & -4 & -4 \\ 8 & -11 & -8 \\ -8 & 8 & 5 \end{pmatrix} $

$ Phương trình đặc trưng -\lambda^3 - 5\lambda^2 - 3\lambda + 9 = 0 \Leftrightarrow -(\lambda - 1)(\lambda + 3)^2 = 0 Với \lambda_1 = 1 \Longrightarrow u_1 = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} \alpha, \alpha \neq 0. $

Cơ sở $E_1$ của f ứng với TR $\lambda_1$ là

$ v_1 = E u_1 = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ -2 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} $

$ \lambda_2 = -3. Cơ sở E_{-3} của A là \left\{ u_2 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, u_3 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \right\}. $

Cơ sở $E_{-3}$ của f ứng với TR $\lambda_2$ là

$ \left\{ v_{2}=Eu_{2}=\begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix}, v_{3}=Eu_{3}=\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix} \right\}. $

Vậy cơ sở cần tìm là B $= \{(1$, -1, 3), (2, 1, 2), (2, 2, $1)\}$ và ma trận của axtt f trong cơ sở B là

$ D = \left( \begin{array}{ccc} 1 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & -3 \end{array} \right). $

Bài tập

Câu 1) Chéo hóa các ma trận sau (nếu được):

$ a) A = \begin{pmatrix} -1 & 4 & -2 \\ -3 & 4 & 0 \\ -3 & 1 & 3 \end{pmatrix}, c) A = \begin{pmatrix} 2 & 2 & -1 \\ 1 & 3 & -1 \\ 1 & -1 & 0 \end{pmatrix}, e) A = \begin{pmatrix} 7 & 4 & 16 \\ 2 & 5 & 8 \\ -2 & -2 & -5 \end{pmatrix},TR: 1, 2, 3. TR: 0, 1, 4. TR: 3, 1 $

$ b) A = \begin{pmatrix} 4 & 2 & 2 \\ 2 & 4 & 2 \\ 2 & 2 & 4 \end{pmatrix}, d) A = \begin{pmatrix} 4 & 0 & -2 \\ 2 & 5 & 4 \\ 0 & 0 & 5 \end{pmatrix}, f) A = \begin{pmatrix} 0 & -4 & -6 \\ -1 & 0 & -3 \\ 1 & 2 & 5 \end{pmatrix}, $

TR: 5, 4.

TR: 2, 8.

TR: 2, 1

Câu 2) Chứng minh rằng nếu A chéo hóa và khả nghịch thì A-1 cũng chéo hóa và khả nghịch.

Câu 3) Chứng tỏ nếu ma trận vuông A cấp n có n VTR độc lập tuyến tính thì ma trận AT cũng có n VTR

độc lập tuyến tính.

Câu 4) Chứng tỏ nếu B đồng dạng với A và A chéo hóa được thì B cũng chéo hóa được.

Câu 5) Cho ánh xạ tuyến tính f: $\mathbb{R}^2 \to \mathbb{R}^2$. $f(x_1; x_2) = (x_1$ + $2x_2; 2x_1$ + $4x_2)$.



(a) Tìm cơ sở và số chiều của imf và ker f.

(b) Tìm tất cả các TR và VTR của f.

(c) Chéo hóa f (nếu được).

(d) Tinh $A_E^{20}$.

Câu 6) Cho axt f: $R^3 \to R^3$. E $= \{e_1 =$ (1, 1, 0); $e_2 =$ (2, 1, 1); $e_3 =$ (1, 0, $2)\}\là$ cơ sở của $R^3$. $f(e_1) =$

(0; 0; 4), $f(e_2) =$ (1; 3; 8), $f(e_3) =$ (3; 5; 6).

(a) Tìm f(x), cơ sở và số chiều của nhân và ảnh.

(b) Tìm tất cả các TR và véc tơ riêng của f.

(c) Tìm ma trận B sao cho $B^3 = A_{E_0}$.

(d) Chéo hóa f (nếu được).



# Chương 8

Nội dung

· Định nghĩa dạng toàn phương

• Dưa dạng toàn phương về dạng chính tắc

• Phân loại dạng toàn phương

Dinh nghĩa

## 8.1 Dinh nghĩa

Dinh nghĩa 8.1 Dạng toàn phương trong $\mathbb{R}^n$ là một hàm thực f : $\mathbb{R}^n \to \mathbb{R}$,

$\forall$ x $= (x_1$, $x_2$, $\dots$, $x_n)^T \in \mathbb{R}^n$ : f(x) $= x^T.A.x$,

trong đó A là ma trận đối xứng thực và được gọi là ma trận của dạng toàn phương (trong cơ sở chính tắc).

Ví dụ 8.1

$ Cho x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}, A = \begin{pmatrix} 2 & -3 \\ -3 & 4 \end{pmatrix}. Ma trận của dạng toàn phương trong R^2 là $

$ x^T Ax = (x_1 \ x_2) \begin{pmatrix} 2 & -3 \\ -3 & 4 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 2x_1^2 - 6x_1x_2 + 4x_2^2. $

Dạng toàn phương trong $\mathbb{R}^3$ thường được ghi ở dạng

f(x) $= f(x_1$, $x_2$, $x_3) = Ax_1^2$ + $Bx_2^2$ + $Cx_3^2$ + $2Dx_1x_2$ + $2Ex_1x_3$ + $2Fx_2x_3$.

Ma trận của dạng toàn phương lúc này là ma trận đối xứng

$ M = \left( \begin{array}{ccc} A & D & E \ D & B & F \ E & F & C \end{array} \right). $

Ví dụ 8.2 Cho dạng toàn phương trong $R^3:$ f(x) $= 2x_1^2$ - $3x_2^2$ + $4x_3^2$ - $2x_1x_2$ + $6x_1x_3$.

$ Ma trận của dạng toàn phương là A = \begin{pmatrix} 2 & -1 & 3 \\ -1 & -3 & 0 \\ 3 & 0 & 4 \end{pmatrix}. Dễ dang kiểm tra f(x) = x^T A x. $



Dưa dạng toàn phương về dạng chính tắc

## 8.2 Dưa dạng toàn phương về dạng chính tắc

Cho dạng toàn phương f(x) $= x^T$ A x, x $\in R_n$.

A là ma trận đối xứng thực nên chéo hóa được bởi ma trận trực giao P và ma trận chéo D: A $=$ PDPT.

Khi đó f(x) $= x^T$ A x $= x^T$ P D $P^T$ x $= (P^T x)^T$ D $(P^T$ x).

Dặt y $= P^T$ x $\Longleftrightarrow$ x $=$ Py, ta được

f $= y^T$ D y $= \lambda_n y_n^2$ + $\lambda_n y_n^2$ + $\cdots$ + $\lambda_n y_n^2$

Dạng toàn phương $y^T$ D y gọi là dạng chính tắc của

dạng toàn phương $x^T$ A x.

Dạng toàn phương $<math display="inline">f(x) = x^T$ A xluôn đưa được về dạng chính tắc

$<math display="inline">f = y^T$ D y bằng cách chéo hóa trực giao ma trận A.

Phép biến đổi x $=$ Py như trên gọi là phép biến đổi trực giao.

Thuật toán phép biến đổi trực giao:

Bước 1: Viết ma trận A của dạng toàn phương (trong cơ sở chính tắc).

Bước 2: Chéo hóa A bởi ma trận trực giao P và ma trận chéo D.

Bước 3: Kết luận: dạng chính tắc cần tìm là f $= y^T$ D y.

Phép biến đổi cần tìm x $=$ Py.

Ví dụ 8.3 Dưa dạng toàn phương

$f(x_1$, $x_2$, $x_3) = -4x_1x_2$ - $4x_1x_3$ + $3x_2^2$ - $2x_2x_3$ + $3x_3^2$

về dạng chính tắc bằng phép biến đổi trực giao. Nêu rõ phép biến đổi.

Bài làm

$ Ma trận của dạng toàn phương A = \begin{pmatrix} 0 & -2 & -2 \\ -2 & 3 & -1 \\ -2 & -1 & 2 \end{pmatrix} $

$ p(\lambda) = -\lambda^3 + 6\lambda^2 - 32 \Longrightarrow TR : \lambda_1 = -2, \lambda_2 = \lambda_3 = 4.Với \lambda_1 = -2, ta có P_{*1} = \begin{pmatrix} \frac{2}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \end{pmatrix}. $

$ \left( \begin{array}{cccc} 1 & \lambda & \lambda & \lambda \\ 1 & 1 & \lambda & \lambda \\ 0 & 0 & 0 & \lambda \end{array} \right) $

$ Với \lambda_2 = \lambda_3 = 4, ta có P_{*2} = \begin{pmatrix} -\frac{1}{\sqrt{5}} \\ \frac{2}{\sqrt{5}} \\ 0 \end{pmatrix}, P_{*3} = \begin{pmatrix} -\frac{2}{\sqrt{30}} \\ -\frac{1}{\sqrt{30}} \\ \frac{5}{\sqrt{30}} \end{pmatrix}. $

$ Do đó ma trận trực giao P = \begin{pmatrix} \frac{2}{\sqrt{6}} & -\frac{1}{\sqrt{5}} & -\frac{2}{\sqrt{30}} \\ \frac{1}{\sqrt{6}} & \frac{2}{\sqrt{5}} & -\frac{1}{\sqrt{30}} \\ \frac{1}{\sqrt{6}} & 0 & \frac{5}{\sqrt{6}} \end{pmatrix}. $

Dạng chính tắc f $= -2y_1^2$ + $4y_2^2$ + $4y_3^2$ và phép biến đổi tương ứng x $=$ py.

### Dịnh nghĩa 8.2 Phép biến đổi x = Py gọi là phép biến đổi không suy biến nếu P là ma trận không suy

$bi\hat{e}n$.



Thuật toán Lagrange

Bước 1) Chọn 1 số hạng $x_k^2$ có hệ số khác không.

Lập thành 2 nhóm: 1 nhóm gồm tất cả các số hạng chứa $x_k$,

nhóm còn lại không chứa $x_k$.

Bước 2) Trong nhóm đầu tiên: lập thành tổng bình phương.

Như vậy, ta sẽ được 1 tổng bình phương và 1 dạng toàn phương

không chứa $x_k$.

Bước 3) Sử dụng bước 1, 2 cho dạng toàn phương không chứa $x_k$.

Chú ý: Nếu trong dạng toàn phương không có số hạng $x_k^2$, thì ta chọn số hạng $x_i.x_j$ có hệ số khác 0. Đổi

biến

$ \begin{cases} x_i = y_i + y_j \\ x_j = y_i - y_j \\ x_k = y_k, \qquad k \neq i, j. \end{cases} $

Ví dụ 8.4 Dưa dạng toàn phương $f(x_1$, $x_2$, $x_3) = x_1^2$ + $2x_2^2$ - $7x_3^2$ - $4x_1x_2$ + $8x_1x_3$ về dạng chính tắc bằng

phương pháp Lagrange.

f(x) $= [x_1^2$ - $4x_1(x_2$ - $2x_3)]$ + $[2x_2^2$ - $7x_3^2]$

$= [x_1^2$ - $4x_1(x_2$ - $2x_3)$ + $4(x_2$ - $2x_3)^2]$ - $4(x_2$ - $2x_3)^2$ + $2x_2^2$ - $7x_3^2 = (x_1$ - $2x_2$ + $4x_3)^2$ - $2x_2^2$ + $16x_2x_3$ - $23x_3^2$

Làm tương tự cho phần không chứa $x_1:$

$-2x_2^2$ + $16x_2x_3$ - $23x_3^2 = -2(x_2^2$ - $8x_2x_3$ + $16x_3^2)$ + $9x_3^2 = -2(x_2$ - $4x_3)^2$ + $9x_3^2$.

$\implies$ f(x) $= (x_1$ - $2x_2$ + $4x_3)^2$ - $2(x_2$ - $4x_3)^2$ + $9x_3^2$.

$ \begin{cases}\ny_1 = x_1 - 2x_2 + 4x_3 \\
y_2 = x_2 - 4x_3 \\
y_3 = x_3\n\end{cases} \rightarrow \begin{cases}\nx_1 = y_1 + 2y_2 + 4y_3 \\
x_2 = y_2 + 4y_3 \\
x_3 = y_3\n\end{cases} $

Dạng chính tắc cần tìm là f(x) $=$ g(y) $= y_1^2$ - $2y_2^2$ + $9y_3^2$.

Ví dụ 8.5 Dưa dạng toàn phương f(x) $= x_1^2$ + $4x_1x_2$ + $4x_1x_3$ + $4x_2^2$ + $16x_2x_3$ + $4x_3^2$ về dạng chính tắc bằng

thuật toán Lagrange.

Bài làm

f(x) $= [x_1^2$ + $4x_1(x_2$ + $x_3)]$ + $4x_2^2$ + $16x_2x_3$ + $4x_3^2$

$=(x_1+2x_2+2x_3)^2-4(x_2+x_3)^2+4x_2^2+16x_2x_3+4x_3^2=(x_1+2x_2+2x_3)^2+8x_2x_3$. Phần còn lại không

$\int x_1$ + $2x_2$ + $2x_3 = y_1 \int x_1 = y_1$ + $4y_2$

$ có số hạng bình phương, ta đặt \begin{cases} x_2 = y_2 + y_3 \\ x_3 = y_2 - y_3 \end{cases} \begin{cases} x_2 = y_2 + y_3 \\ x_3 = y_2 - y_3 \end{cases}. $

Dạng chính tắc cần tìm $là<math display="inline">f=y_1^2+8y_2^2-8y_3^2$



Phân loại dạng toàn phương

## 8.3 Phân loại dạng toàn phương

Phân loại dạng toàn phương. Dạng toàn phương f(x) $= x^T$ A x được

gọi là

• xác định dương, nếu $\forall$ x $\neq$ 0 : f(x) $>$ 0.

• xác định âm, nếu $\forall$ x $\neq$ 0 : f(x) $<$ 0.

• nửa xác định dương, nếu $\forall$ x : f(x) $\geq$ 0, $\exists x_0 \neq$ 0 : $f(x_0) =$ 0.

• nửa xác định âm, nếu $\forall$ x : f(x) $\leq$ 0, $\exists x_0 \neq$ 0 : $f(x_0) =$ 0.

• không xác định dấu, nếu $\exists x_1$, $x_2$ : $f(x_1) <$ 0, $f(x_2) >$ 0.

Ví dụ 8.6 Phân loại dạng toàn phương f(x) $= x_1^2$ + $5x_2^2$ + $4x_3^2$ - $4x_1x_2$ - $2x_2x_3$.

Dùng thuật toán Lagrange: f(x) $= (x_1$ - $2x_2)^2$ + $(x_2$ - $x_3)^2$ + $3x_3^2 \ge$ 0

$ f(x) = 0 \Longleftrightarrow \begin{cases} x_1 - 2x_2 = 0 \\ x_2 - x_3 = 0 \Leftrightarrow x = 0. \\ x_3 = 0 \end{cases} $

Vậy f(x) là dạng toàn phương xác định dương.

Tính chất Cho dạng toàn phương ở dạng chính tắc

f $= \lambda_1 y_1^2$ + $\lambda_2 y_2^2$ + $\ldots$ + $\lambda_n y_n^2$

• Nếu $\lambda_k >$ 0, $\forall$ k thì f xác định dương.

• Nếu $\lambda_k <$ 0, $\forall$ k thì f xác định âm.

• Nếu $\lambda_k \geq$ 0, $\forall$ k, $\exists \lambda_i =$ 0 thì f nửa xác định dương.

• Nếu $\lambda_k \leq$ 0, $\forall$ k, $\exists \lambda_i =$ 0 thì f nửa xác định âm.

• Nếu $\exists \lambda_i >$ 0, $\lambda_j <$ 0, i $\neq$ j thì f không xác định dấu.

Dinh nghĩa 8.3 Giả sử dạng toàn phương đưa về chính tắc được:

f $= \lambda_1 y_1^2$ + $\lambda_2 y_2^2$ + $\cdots$ + $\lambda_n y_n^2$.

Số các hệ số dương được gọi là chỉ số dương quán tính.

Số các hệ số âm được gọi là chỉ số âm quán tính.

Luật quán tính Chỉ số dương quán tính, chỉ số âm quán tính của

dạng toàn phương là những đại lượng bất biến không phụ thuộc

vào cách đưa dạng toàn phương về dạng chính tắc.

### Dịnh nghĩa 8.4 (Định thức con chính) .Cho ma trận vuông A.

Tất cả các định thức con tạo nên dọc theo đường chéo chính được gọi là định thức con chính cấp 1, 2, ..., n.

$ A = \left( \begin{array}{cccc} a_{11} & a_{12} & a_{13} & \ldots & a_{1n} \ a_{21} & a_{22} & a_{23} & \ldots & a_{2n} \ a_{31} & a_{32} & a_{33} & \ldots & a_{3n} \ \ldots & \ldots & \ldots & \ldots & \ldots \ a_{n1} & a_{n2} & a_{n3} & \ldots & a_{nn} \end{array} \right) $

$ Các định thức con chính \Delta_1 = |a_{11}|, \Delta_2 = \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix}, \Delta_3 = \begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{21} & a_{22} & a_{23} \end{vmatrix}, ..., \Delta_n = \det(A). $



Tiêu chuẩn Sylvester Cho dạng toàn phương f(x) $= x^T$ A x

i) f(x) xác định dương khi và chỉ khi $\Delta_i >$ 0, $\forall$ i $=$ 1, 2, ..., n.

ii) f(x) xác định âm khi và chỉ khi $(-1)^i \Delta_i >$ 0, $\forall$ i $=$ 1, 2, ..., n.

Ví dụ 8.7 Phân loại dạng toàn phương f(x) $= 5x_1^2$ + $x_2^2$ + $5x_3^2$ + $4x_1x_2$ - $8x_1x_3$ - $4x_2x_3$.

Bài làm

$ Ta có ma trận của dạng toàn phương f là A = \begin{pmatrix} 5 & 2 & -4 \\ 2 & 1 & -2 \\ -4 & -2 & 5 \end{pmatrix} $

$ Vì \Delta_1 = 5 > 0, \Delta_2 = \begin{vmatrix} 5 & 2 \\ 2 & 1 \end{vmatrix} = 1 > 0, \Delta_3 = \begin{vmatrix} 5 & 2 & -4 \\ 2 & 1 & -2 \\ -4 & -2 & 5 \end{vmatrix} = 1 > 0. $

Vậy f xác định dương theo tiêu chuẩn Sylvester.

Ví dụ 8.8 Cho dạng toàn phương f(x) $= -5x_1^2$ - $x_2^2$ - $mx_3^2$ - $4x_1x_2$ + $2x_1x_3$ + $2x_2x_3$.

Với giá trị nào của m thì dạng toàn phương f xác định âm.

Bài làm

$ Ma trận của dạng toàn phương f là A = \begin{pmatrix} -5 & -2 & 1 \\ -2 & -1 & 1 \\ 1 & 1 & -m \end{pmatrix}. $

$ \Delta_1 = -5 < 0, \, \Delta_2 = \begin{vmatrix} -5 & -2 \\ -2 & -1 \end{vmatrix} = 1 > 0, \, \Delta_3 = \begin{vmatrix} -5 & -2 & 1 \\ -2 & -1 & 1 \\ 1 & 1 & -m \end{vmatrix} = -m + 2. $

$<math display="inline">fxác$ định âm khi và chỉ khi

$ \begin{cases} \Delta_1 < 0, \\ \Delta_2 > 0, \quad \Longleftrightarrow -m+2 < 0 \Longleftrightarrow m > 2. \end{cases} $

Ví dụ 8.9 Tìm m để dạng toàn phương sau không xác định dấu

f(x) $= x_1^2$ + $5x_2^2$ + $mx_3^2$ - $4x_1x_2$ + $6x_1x_3$ + $2x_2x_3$.

Bài làm

f(x) $= (x_1^2$ - $4x_1x_2$ + $6x_1x_3)$ + $5x_2^2$ + $mx_3^2$ + $2x_2x_3$

$= (x_1$ - $2x_2$ + $3x_3)^2$ + $x_2^2$ + $14x_2x_3$ + $(m-9)x_3^2 = (x_1$ - $2x_2$ + $3x_3)^2$ + $(x_2$ + $7x_3)^2$ + $(m-58)x_3^2$.

f(x) không xác định dấu khi và chỉ khi có ít nhất một hệ số âm và một hệ số dương $\Longleftrightarrow$ m $<$ 58.



$D\hat{e}$ on tap - 1

$ Câu 1) Cho hai ma trận A = \begin{pmatrix} 2 & 2 & 1 \\ 2 & 5 & 3 \\ 2 & 3 & 5 \end{pmatrix} và B = \begin{pmatrix} 3 & 1 & 2 \\ -1 & 2 & 4 \\ 2 & 6 & 3 \end{pmatrix}. Tìm ma trận X thỏa AX - X = B^T $

Câu 2) Trong $\mathbb{R}_4$ cho không gian con U $= \langle$ (1,1,2,2), (2,-1,1,0) $\rangle$, z $=$ (1,2,3,1).

(a) Tìm cơ sở và số chiều $U^{\perp}$.

Tìm hình chiếu của z xuống $U^{\perp}$.

(b)

Câu 3) Trong $\mathbb{R}_4$ cho 2 không gian con

U $= <(1$, 1, -2, 1), (1, 2, 1, 0)

$ V: \begin{cases} x_1 + 2x_2 + 3x_3 - 5x_4 = 0 \\ 2x_1 - x_2 + 2x_3 + x_4 = 0 \end{cases} $

Tìm cơ sở và số chiều của U $\cap$ V.

(a)

Tìm cơ sở và số chiều của U + V.

(b)

Câu 4) Trong $\mathbb{R}_2:$ x $= (x_1$, $x_2)$, y $= (y_1$, $y_2)$. Xét tích vô hướng (x, y) $= 2x_1y_1$ + $2x_1y_2$ + $2x_2y_1$ + $3x_2y_2$.

Tính khoảng cách giữa 2 vécto u, v với u $=$ (2, -1), v $=$ (1, 3).

Câu 5) Cho ánh xạ f : $\mathbb{R}^3 \to \mathbb{R}^3$, biết ma trận của f trong cơ sở E $= \{(1,1,0)$, (1,0,1), $(1,1,1)\}$ là

$ A = \left( \begin{array}{ccc} 1 & -2 & 1 \\ 3 & 2 & 0 \\ -1 & 3 & 4 \end{array} \right). Tìm f(4,3,6) $

Câu 6) Cho ma trận cấp 3

$ A = \left( \begin{array}{rrr} 0 & 2 & - \\ -1 & -3 & -2 \\ 1 & 5 & 4 \end{array} \right) $

Tìm một ma trận B $\in M_3(\mathbb{R})$ sao cho $B^3 =$ A.

$D\hat{e}$ ôn số 2

$ Câu 1) Cho A = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & 1 \\ 2 & 2 & 1 \end{pmatrix}, B = \begin{pmatrix} -2 & 3 & -0 \\ 1 & -2 & 5 \\ 3 & 0 & 7 \end{pmatrix}. Tìm ma trận X thỏa 3I + AX = B^T. $

Câu 2) Tìm tất cả các nghiệm của hệ phương trình

$ \begin{cases} 2x_1 + 3x_2 + 2x_3 + x_4 = -1 \\ x_1 + 2x_2 + x_4 = 0 \\ x_1 + x_2 + x_3 + x_4 = 3 \end{cases} $

vuông góc với véc tơ u $=$ (1, 1, 1, 0).

Câu 3) Trong $R^4$, cho 2 không gian con F $= \langle$ 1; 2; 1; 1 $\rangle;$ (2; 3; -1; 2) $>$, G $= \langle$ -3; 1; 2; 1 $\rangle$, (-5; 10; 7; 7) $>$.

Tìm cơ sở và số chiều của F $\cap$ G.

Câu 4) Trong $R^3$, cho tích vô hướng

(x, y) $= 3x_1y_1$ + $2x_1y_2$ + $2x_2y_1$ + $5x_2y_2$ + $x_3y_3$, x $= (x_1$, $x_2$, $x_3)$, y $= (y_1$, $y_2$, $y_3)$

và không gian con F $= \langle$ 1, -1, 2 $\rangle$. Tìm hình chiếu của véc tơ x $=$ (2, 0, 1) xuống F.



Câu 5) Cho ánh xạ tuyến tính f: $R^3 \longrightarrow R^3$ thỏa

f(1;2;1) $=$ (2;-1;3), f(2;3;0) $=$ (-3;2;5), f(1;3;2) $=$ (5;-3;-2).

Tìm cơ sở và số chiều của ker f và $\Im$ f.

(a)

(b) Tìm ma trận của f trong cơ sở E $= \{(1$, 2, 1), (2, 3, 0), (1, 3, $2)\}$.

$ Câu 6) Cho ma trận A = \begin{pmatrix} 3 & -2 & 3 \\ -1 & a & -3 \\ 2 & -4 & b \end{pmatrix} và x = \begin{pmatrix} 1 \\ -1 \\ -1 \end{pmatrix}. Tìm a, b để x là véc riêng của A. Chéo hóa A $

với a, b vừa tìm được.

Đáp số

$\underline{\mathbf{D}}\hat{\mathbf{e}}$ 1

$ 1. X = \begin{pmatrix} 20 & -9 & -10 \\ -6 & 2 & 5 \\ 5 & 4 & 2 \end{pmatrix} $

2. (a) Cơ sở của $U^{\perp}$ là $\{(-1;-1;1;0)$, $(-2;-4;0;3)\}$.

(b) $Pr_{U\perp}(z) = \frac{7}{17}(0;$ 2; 2; -3).

(a) Co so U + V là $\{(1;$ 1; -2; 1), (0; 1; 3; -1), (0; 0; -9; $5)\}\$

3.

(b) Cơ sở U $\bigcap$ V là $\{(2;3;-1;1)\}$.

4. d(u, v) $= \sqrt{34}$.

5. f(4;3;6) $=$ (22;26;21)

$ 6. B = \begin{pmatrix} 0 & 1 & 1 \\ -1 & -1 & -1 \\ 1 & 1 & 2 \end{pmatrix} \cdot \begin{pmatrix} -1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & \frac{3}{2} \end{pmatrix} \cdot \begin{pmatrix} 0 & 1 & 1 \\ -1 & -1 & -1 \\ 1 & 1 & 2 \end{pmatrix}. $

$<u>Đề 2:</u>$

$ 1. X = \begin{pmatrix} -16 & -5 & 11 \\ -11 & -6 & 8 \\ 0 & 2 & -5 \end{pmatrix}. $

2. x $=$ (-1, 0, 1, $2)\alpha$, $\forall \alpha \in$ R.

3. Co sở F $\cap$ G là $\{(4$, 7, 1, $4)\}$.

4. Hình chiếu là $\frac{4}{8}(1;-1;2)$.

(a) Cơ sở của $\Im$ f là $\{(2;-1;3),(0,1,19)\}$. Cơ sở của ker f là $\{(48;76;9)\}$.

5.

$ (b) Ma trận của f trong cơ sở E là \begin{pmatrix} 25 & -11 & 36 \\ -6 & 0 & -6 \\ -11 & 8 & -19 \end{pmatrix}. $

$ 6. a = 0, b = 4. D = \begin{pmatrix} -2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 7 \end{pmatrix}, P = \begin{pmatrix} 2 & 3 & -1 \\ 1 & 0 & 1 \\ 0 & -1 & -2 \end{pmatrix}. $



