# Chương 1

Không gian vector

Bài tập 1.1. Xét xem các tập hợp sau đây có lập thành F-không gian vector hay không đối với

các phép toán thông thường (được định nghĩa theo từng thành phần):

(a) Tập hợp tất cả các dãy $(x_1$, $\ldots$, $x_n) \in \mathbb{F}_n$ thỏa mãn điều kiện $x_1$ + $\cdots$ + $x_n =$ 0.

(b) Tập hợp tất cả các dãy $(x_1$, $\ldots$, $x_n) \in \mathbb{F}_n$ thỏa mãn điều kiện $x_1$ + $\cdots$ + $x_n =$ 1.

Tập hợp tất cả các dãy $(x_1$, $\ldots$, $x_n) \in \mathbb{F}_n$ thỏa mãn điều kiện $x_1 = x_n =$ -1.

(c)

Tập hợp tất cả các dãy $(x_1$, $\ldots$, $x_n) \in \mathbb{F}_n$ thỏa mãn điều kiện $x_1 = x_3 = x_5 = \cdots$, $x_2 = x_4 =$

(d)

$x_6=\cdots$.

Tập hợp các ma trận vuông $(a_{ij})_{n\times n}$ đối xứng cỡ n, nghĩa là các ma trận thỏa mãn $a_{ij} = a_{ji}$,

(e)

với 1 $\leq$ i, j $\leq$ n.

(a) Đây đúng là một không gian vector với các phép toán thông thường.

Chúng minh.

Dây không phải một không gian vector với các phép toán thông thường vì phép cộng không

(b)

dóng.

Đây không phải một không gian vector với các phép toán thông thường vì phép cộng không

( $\rm$ c )

dóng.

Dây đúng là một không gian vector với các phép toán thông thường.

(d)

(e) Đây đúng là một không gian vector với các phép toán thông thường.

Bài tập 1.2. Tập hợp tất cả các dãy $(x_1$, $\ldots$, $x_n) \in \mathbb{R}_n$ với tất cả các thành phần $x_1$, $\ldots$, $x_n$ đều

nguyên có lập thành một R-không gian vector hay không?

Chứng minh. Không. Bởi phép nhân vector với vô hướng không đóng trong tập này.



  
Bài tập 1.3. Với các phép toán thông thường, Q có là một R-không gian vector hay không? R

có là một C-không gian vector hay không?

Chứng minh. Q không phải là một R-không gian vector vì phép nhân một số hữu tỷ với một số

thực có thể là một số vô tỷ. Ví dụ: $\sqrt{2} \cdot$ 1 $= \sqrt{2} \notin \mathbb{Q}$.

R không phải là một C-không gian vector vì phép nhân một số thực với một số phức có thể là

một số phức mà không phải số thực. Ví dụ $\iota \cdot$ 1 $= \iota \notin \mathbb{R}$.

Bài tập 1.4. Chứng minh rằng nhóm Z không đẳng cấu với nhóm cộng của bất kỳ một không

gian vector trên bất kỳ trường nào.

Chứng minh. Giả sử phản chứng, tồn tại một không gian vector V trên trường $\mathbb$ F đẳng cấu với $\mathbb$ Z.

Khi đó, tồn tại một đồng cấu $\varphi$ : $\mathbb{Z} \to$ V sao cho:

$\varphi(x)$ + $\varphi(y) = \varphi(x+y) \quad \forall$ x, y $\in \mathbb{Z}$

và đồng cấu này là đẳng cấu nhóm.

Một đồng cấu nhóm biến phần tử trung lập của nhóm này thành phần tử trung lập của nhóm

kia, do đó $\varphi(0)$ là vector-không trên V. $\varphi(1) \neq \varphi(0) =$ 0 vì $\varphi$ là đẳng cấu.

$\varphi$ là đẳng cấu nên

V $= \{\cdots$, $\varphi(-2)$, $\varphi(-1)$, $\varphi(0)$, $\varphi(1)$, $\varphi(2)$, $\cdots\}$

Nếu F là một trường chỉ gồm một phần tử, với các phép toán được định nghĩa như sau:

0 + 0 $=$ 0

0 $\cdot$ 0 $=$ 0

Mọi vector trên trường một phần tử đều là vector-không. Điều này mâu thuẫn với giả sử vì Z

vô hạn đếm được, trong khi V chỉ có đúng một phần tử.

Do vậy, trường $\mathbb$ F phải có nhiều hơn một phần tử.

Giả sử $char(\mathbb{F}) =$ p với p là một số nguyên tố thì

$\varphi(p) = \underbrace{\varphi(1)$ + $\cdots$ + $\varphi(1)} = \underbrace{1_{\mathbb{F}}\varphi(1)$ + $\cdots$ + $1_{\mathbb{F}}\varphi(1)} = \underbrace{(1_{\mathbb{F}}$ + $\cdots$ + $1_{\mathbb{F}})} \varphi(1) =$ 0

mâu thuẫn với việc $\varphi$ là song ánh. Do đó $char(\mathbb{F}) =$ 0.

Với mọi số nguyên dương n, chúng ta có

$\varphi(n) = \underbrace{(1_{\mathbb{F}}$ + $\cdots$ + $1_{\mathbb{F}})} \varphi(1)$



$<u>UITUUNU$ I. IMIUNU UIAN $TEUTUU</u>$

do đó

$\varphi(-n) = \underbrace{((-1_{\mathbb{F}})$ + $\cdots$ + $(-1_{\mathbb{F}}))}_{\sim} \varphi(1)$.

$\mathbb$ F là một trường với đặc số khác không nên $1_{\mathbb F}+1_{\mathbb F}$ khác không và có nghịch đảo, kí hiệu

là k. Mặt khác, nghịch đảo này không có dạng $\underbrace{(1_\mathbb{F}+\cdots+1_\mathbb{F})}hay \underbrace{((-1_\mathbb{F})+\cdots+(-1_\mathbb{F}))}nên$

$k\varphi(1) \notin {\varphi(n) \mid$ n $\in \mathbb{Z}}$. Vậy giả sử phản chứng là sai.

Do đó ta kết luận Z không đẳng cấu với bất cứ không gian vector nào, trên bất cứ trường

nào.

Bài tập 1.5. Chứng minh rằng nhóm abel A đối với phép cộng + có thể trở thành một không

gian vector trên trường $\mathbb{F}_p$ nếu và chỉ nếu

px $=$ x + x + $\cdots$ + x $=$ 0, $\quad \forall$ x $\in$ A.

Chứng minh. Một nhóm abel A với phép cộng đã thỏa mãn 4 tiên đề đầu tiên của không gian

vector.

$(\Rightarrow)$ A là một không gian vector trên trường $\mathbb{F}_p$.

$\underbrace{x$ + x + $\cdots$ + $x}_{p} = \underbrace{1x$ + 1x + $\cdots$ + $1x}_{p} = \underbrace{(1$ + 1 + $\cdots$ + $1)}_{p}$ x $=$ 0x $=$ 0

$(\Leftarrow) \underbrace{x$ + x + $\cdots$ + $x} =$ 0

Ta định nghĩa kí hiệunxvới x $\in$ A, n $\in \mathbb{Z}như$ sau:

$ nx = \begin{cases} \underbrace{x + x + \dots + x}_{n}, & n > 0 \\ 0, & n = 0 \\ \underbrace{(-x) + (-x) + \dots + (-x)}_{n}, & n < 0 \end{cases} $

Cùng với điều kiện x + $\cdots$ + x $=$ 0, ta suy ra nx $=$ (n $\mod$ p)x

Ta kiểm tra 4 tiên đề còn lại:

(V5) (a + b)x Nếu a $>$ 0, b $>$ 0:

(a + b)x $=$ x + x + $\cdots$ + x $=$ x + $\cdots$ + x + x + $\cdots$ + x $=$ ax + bx



$<u>UITUUNU$ I. IMIUNU UIAN $VEULUIU</u>$

Nếu a $<$ 0, b $<$ 0:

(a + b)x $=$ (-x) + $\cdots$ + (-x) $=$ (-x) + $\cdots$ + (-x) + (-x) + $\cdots$ + (-x) $=$ ax + bx

Nếu a $=$ 0 hoặc b $=$ 0

(a+b)x $=$ ax + bx

Nếu a $>$ 0, b $<$ 0 và a + b $>$ 0

(a + b)x $=$ x + $\dots$ + x $=$ x + $\dots$ + x + (-x) + $\dots$ + (-x) $=$ ax + bx

Nếu a $>$ 0, b $<$ 0 và a + b $<$ 0

(a + b)x $=\underbrace{(-x)$ + $\cdots$ + $(-x)}_{-a-b} = \underbrace{x$ + $\cdots$ + $x}_{a}$ + $\underbrace{(-x)$ + $\cdots$ + $(-x)}_{b} =$ ax + bx

-a-b

Nếu a $>$ 0, b $<$ 0 và a + b $=$ 0

(a + b)x $=$ 0 $=$ (x + $\dots$ + x) + (-x) + $\dots$ + (-x) $=$ ax + bx

Trường hợp a $<$ 0, b $>$ 0 được chứng minh tương tự.

(V6) a(x + y)

Nếu $a=0:$

a(x + y) $=$ 0 $=$ 0 + 0 $=$ 0x + 0y $=$ ax + ay

Nếu a $>$ 0:

a(x + y) $=$ (x + y) + $\cdots$ + (x + y) $=$ x + $\cdots$ + x + y + $\cdots$ + y $=$ ax + ay

Nếu a $<$ 0:

a(x + y) $=$ (-x - y) + $\dots$ + (-x - y) $=$ (-x) + $\dots$ + (-x) + (-y) + $\dots$ + (-y) $=$ ax + ay

(V7) (ab)x



$<u>UITUUNU$ I. IMIUNU UIAN $VEULUIU</u>$

Nếu a $=$ 0 hoặc b $=$ 0:

(ab)x $=$ 0 $=$ a(bx)

Nếu a $>$ 0, b $>$ 0:

(ab)x $=$ x + $\dots$ + x $=$ (x + $\dots$ + x) + $\dots$ + (x + $\dots$ + x) $=$ a(bx)

Các trường hợp còn lại được quy về a $\geq$ 0, b $\geq$ 0 vì nx $=$ (n $\mod$ p)x.

(V8) 1x $=$ x

Do đó A là một không gian vector trên trường $\mathbb{F}_p$.

Bài tập 1.6. Xét xem các vector sau đây độc lập hay phụ thuộc tuyến tính trong $\mathbb{R}_4:$

(a) $e_1 =$ (-1, -2, 1, 2), $e_2 =$ (0, -1, 2, 3), $e_3 =$ (1, 4, 1, 2), $e_4 =$ (-1, 0, 1, 3).

(b) $\alpha_1 =$ (-1, 1, 0, 1), $\alpha_2 =$ (1, 0, 1, 1), $\alpha_3 =$ (-3, 1, -2, -1).

(a) Xét ràng buộc tuyến tính $x_1e_1$ + $x_2e_2$ + $x_3e_3$ + $x_4e_4 =$ (0,0,0,0). Đế tìm

Chúng minh.

$x_1$, $x_2$, $x_3$, $x_4$, ta giải hệ phương trình thuần nhất sau:

$ \begin{cases}\n(-1)x_1 + 0x_2 + 1x_3 + (-1)x_4 = 0 \\
(-2)x_1 + (-1)x_2 + 4x_3 + 0x_4 = 0 \\
1x_1 + 2x_2 + 1x_3 + 1x_4 = 0 \\
2x_1 + 3x_2 + 2x_3 + 3x_4 = 0\n\end{cases} $

$ \begin{cases}\n2x_1 + 3x_2 + 2x_3 + 3x_4 &= 0 \\
0x_1 + 3x_2 + 4x_3 + 1x_4 &= 0 \\
0x_1 + 2x_2 + 6x_3 + 3x_4 &= 0 \\
0x_1 + x_2 + 0x_3 + (-1)x_4 &= 0 \\
2x_1 + 3x_2 + 2x_3 + 3x_4 &= 0\n\end{cases} $

$ \begin{cases}\n0x_1 + 0x_2 + 6x_3 + 5x_4 &= 0 \\
0x_1 + x_2 + 0x_3 + (-1)x_4 &= 0 \\
2x_1 + 3x_2 + 2x_3 + 3x_4 &= 0\n\end{cases} $



$<u>UITUUNU$ I. IMIUINU UIAIN $VEUTUU</u>$

$ \begin{cases}\n0x_1 + 0x_2 + 12x_3 + 3x_4 = 0 \\
0x_1 + 0x_2 + 12x_3 + 10x_4 = 0 \\
0x_1 + x_2 + 0x_3 + (-1)x_4 = 0 \\
2x_1 + 3x_2 + 2x_3 + 3x_4 = 0\n\end{cases}
\begin{cases}\n0x_1 + 0x_2 + 0x_3 + (-7)x_4 = 0 \\
0x_1 + 0x_2 + 12x_3 + 10x_4 = 0 \\
0x_1 + x_2 + 0x_3 + (-1)x_4 = 0 \\
2x_1 + 3x_2 + 2x_3 + $

Hệ phương trình này chỉ có nghiệm tầm thường $(x_1$, $x_2$, $x_3$, $x_4) =$ (0, 0, 0, 0), kéo theo ràng

buộc tuyến tính tầm thường. Do đó hệ độc lập tuyến tính.

Xét ràng buộc tuyến tính $x_1\alpha_1$ + $x_2\alpha_2$ + $x_3\alpha_3 =$ (0,0,0). Để tìm $x_1$, $x_2$, $x_3$, ta giải hệ phương

(b)

trình thuần nhất sau:

$ \begin{cases}\n(-1)x_1 + 1x_2 + (-3)x_3 = 0 \\
1x_1 + 0x_2 + 1x_3 = 0 \\
0x_1 + 1x_2 + (-2)x_3 = 0 \\
1x_1 + 1x_2 + (-1)x_3 = 0\n\end{cases}

\Leftrightarrow \begin{cases}\n0x_1 + 2x_2 + (-4)x_3 = 0 \\
0x_1 + (-1)x_2 + 2x_3 = 0 \\
0x_1 + 1x_2 + (-2)x_3 = 0 \\
1x_1 + 1x_2 + (-1)x_3 = 0\n\end{cases}

\Leftrightarrow \begin{cases}\n0x_1 + 1x_2 + $

Hệ phương trình này có nghiệm không tầm thường $(x_1$, $x_2$, $x_3) =$ (0, 2, 1). Do đó hệ phụ

thuộc tuyến tính.

Bài tập 1.7. Chứng minh rằng hai hệ vector sau đây là các cơ sở của $\mathbb{C}_3$. Tìm ma trận chuyển

từ cơ sở thứ nhất sang cơ sở thứ hai:

$e_1 =$ (1, 2, 1), $e_2 =$ (2, 3, 3), $e_3 =$ (3, 7, 1);

$e'_1 =$ (3, 1, 4), $e'_2 =$ (5, 2, 1), $e'_3 =$ (1, 1, -6).



$<u>UITUUNU$ I. IMIUNU UIAN $TEULUI</u>$

Chứng minh. Xét ràng buộc tuyến tính $x_1e_1$ + $x_2e_2$ + $x_3e_3 =$ (0,0,0).

$ \begin{cases}\n1x_1 + 2x_2 + 3x_3 = 0 \\
2x_1 + 3x_2 + 7x_3 = 0 \\
1x_1 + 3x_2 + 1x_3 = 0\n\end{cases}
\begin{cases}\n1x_1 + 2x_2 + 3x_3 = 0 \\
0x_1 + (-1)x_2 + 1x_3 = 0 \\
0x_1 + 1x_2 + (-2)x_3 = 0\n\end{cases}
\begin{cases}\n1x_1 + 2x_2 + 3x_3 = 0 \\
0x_1 + (-1)x_2 + 1x_3 = 0 \\
0x_1 + 0x_2 + (-1)x_3 = 0\n\end{cases} $

Hệ phương trình trên chỉ có nghiệm tầm thường $(x_1$, $x_2$, $x_3) =$ (0, 0, 0) do đó hệ $e_1$, $e_2$, $e_3$ độc

lập tuyến tính và cực đại (vì dim $\mathbb{C}_3 =$ 3) nên hệ này cũng là một cơ sở của $\mathbb{C}_3$.

Xét ràng buộc tuyến tính $x_1e'_1$ + $x_2e'_2$ + $x_3e'_3 =$ (0,0,0).

$ \left\{ \begin{aligned} 3x_1 + 5x_2 + 1x_3 &= 0 \\ 1x_1 + 2x_2 + 1x_3 &= 0 \\ 4x_1 + 1x_2 + (-6)x_3 &= 0 \\ 3x_1 + 5x_2 + 1x_3 &= 0 \\ 0x_1 + 1x_2 + 2x_3 &= 0 \\ 0x_1 + (-6)x_2 + (-8)x_3 &= 0 \\ \Longleftrightarrow \left\{ \begin{aligned} 3x_1 + 5x_2 + 1x_3 &= 0 \\ 0x_1 + 1x_2 + 2x_3 &= 0 \\ 0x_1 + 0x_2 + 4x_3 &= 0 \end{aligned} \right. \end{ $

Hệ phương trình trên chỉ có nghiệm tầm thường $(x_1$, $x_2$, $x_3) =$ (0, 0, 0) do đó hệ $e_1$, $e_2$, $e_3$ độc

lập tuyến tính và cực đại (vì dim $\mathbb{C}_3 =$ 3) nên hệ này cũng là một cơ sở của $\mathbb{C}_3$.

$(e_1$, $e_2$, $e_3)$ là một cơ sở của $\mathbb{C}_3$ nên vector $(a_1$, $a_2$, $a_3)$ biểu thị tuyến tính được duy nhất theo

cơ sở này.



$<u>UITUUNU$ I. IMIUNU UIAN $TEUTUU</u>$

Bằng việc giải hệ phương trình sau:

$ \begin{cases}\n1x_1 + 2x_2 + 3x_3 = a_1 \\
2x_1 + 3x_2 + 7x_3 = a_2 \\
1x_1 + 3x_2 + 1x_3 = a_3\n\end{cases} $

ta thu được nghiệm:

$(x_1$, $x_2$, $x_3) = (-18a_1$ + $7a_2$ + $5a_3$, $5a_1$ - $2a_2$ - $a_3$, $3a_1$ - $a_2$ - $a_3)$

Thay số, ta biểu diễn được $(e'_1$, $e'_2$, $e'_3)$ qua $(e_1$, $e_2$, $e_3)$ như sau:

$e'_1 = (-27)e_1$ + $9e_2$ + $4e_3 e'_2 = (-71)e_1$ + $20e_2$ + $12e_3 e'_3 = (-41)e_1$ + $9e_2$ + $8e_3$

Như vậy, ma trận chuyển cơ sở $(e_1$, $e_2$, $e_3) \rightarrow (e'_1$, $e'_2$, $e'_3)$ là:

$ \begin{pmatrix} -27 & 9 & 4 \\ -71 & 20 & 12 \\ -41 & 9 & 8 \end{pmatrix} $

Bài tập 1.8. Chứng minh rằng hai hệ vector sau đây là các cơ sở của $\mathbb{C}_4$. Tìm mối liên hệ giữa

tọa độ của cùng một vector trong hai cơ sở đó:

$e_1 =$ (1, 1, 1, 1), $e_2 =$ (1, 2, 1, 1), $e_3 =$ (1, 1, 2, 1), $e_4 =$ (1, 3, 2, 3);

$e'_1 =$ (1, 0, 3, 3), $e'_2 =$ (2, 3, 5, 4), $e'_3 =$ (2, 2, 5, 4), $e'_4 =$ (2, 3, 4, 4).

Chứng minh. Xét ràng buộc tuyến tính $x_1e_1$ + $x_2e_2$ + $x_3e_3$ + $x_4e_4 =$ (0,0,0,0).

$ \begin{cases}\n1x_1 + 1x_2 + 1x_3 + 1x_4 = 0 \\
1x_1 + 2x_2 + 1x_3 + 3x_4 = 0\n\end{cases} $

$ \begin{cases} 1x_1 + 1x_2 + 2x_3 + 2x_4 = 0 \\ 1x_1 + 1x_2 + 1x_3 + 3x_4 = 0 \end{cases} $



VIIUVINU I. IMIUINU UIAIN VEUTUIU

$ \begin{cases}\n1x_1 + 1x_2 + 1x_3 + 1x_4 = 0 \\
0x_1 + 1x_2 + 0x_3 + 2x_4 = 0 \\
0x_1 + 0x_2 + 1x_3 + 1x_4 = 0 \\
0x_1 + 0x_2 + 0x_3 + 2x_4 = 0\n\end{cases} $

Hệ phương trình trên chỉ có nghiệm tầm thường $(x_1$, $x_2$, $x_3$, $x_4) =$ (0, 0, 0, 0).

Do đó hệ vector $e_1$, $e_2$, $e_3$, $e_4$ độc lập tuyến tính.

Số chiều của không gian vector $\mathbb{C}_4$ bằng 4 nên hệ vector $e_1$, $e_2$, $e_3$, $e_4$ độc lập tuyến tính cực đại,

nên cũng là cơ sở của $\mathbb{C}_4$.

Xét ràng buộc tuyến tính $x_1e'_1$ + $x_2e'_2$ + $x_3e'_3$ + $x_4e'_4 =$ (0,0,0,0).

$ \begin{cases}\n1x_1 + 2x_2 + 2x_3 + 2x_4 = 0 \\
0x_1 + 3x_2 + 2x_3 + 3x_4 = 0 \\
3x_1 + 5x_2 + 5x_3 + 4x_4 = 0 \\
3x_1 + 4x_2 + 4x_3 + 4x_4 = 0\n\end{cases} $

$3x_1$ + $4x_2$ + $4x_3$ + $4x_4 =$ 0 $\bigoplus_{x_1$ + $3x_2$ + $2x_3$ + $2x_4 = 0} 6x_1$ + $3x_2$ + $2x_3$ + $3x_4 =$ 0 $0x_1$ + $(-1)x_2$ + $(-1)x_3$ + $(-2)x_4 =$ 0 $0x_1$ + $(-2)x_2$ + $(-2)x_3$ + $(-2)x_4 =$ 0 $\bigoplus_{x_1$ + $3x_2$ + $2x_3$ + $3x_4 = 0} 0x_1$ + $3x_2$ + $2x_3$ + $3x_4 =$ 0 $0x_1$ + 0

Hệ phương trình trên chỉ có nghiệm tầm thường $(x_1$, $x_2$, $x_3$, $x_4) =$ (0, 0, 0, 0).

Do đó hệ $vectore_1^\prime$, $e_2^\prime$, $e_3^\prime$, $e_4^\primeđộc$ lập tuyến tính.

Số chiều của không gian vector $\mathbb{C}_4$ bằng 4 nên hệ vector $e'_1$, $e'_2$, $e'_3$, $e'_4$ độc lập tuyến tính cực đại,

nên cũng là cơ sở của $\mathbb{C}_4$.



VIIUVINU I. IMIUINU UIAIN VEUTUIU

Từ việc giải các hệ phương trình tuyến tính, ta được:

$e'_1 = 1e_1$ + $(-3)e_2$ + $1e_3$ + $1e_4 e'_2 = 0e_1$ + $(-1)e_2$ + $2e_3$ + $1e_4 e'_3 = 1e_1$ + $(-2)e_2$ + $2e_3$ + $1e_4 e'_4 = 1e_1$ + $(-1)e_2$ + $1e_3$ + $1e_4$

$ \left\{ \begin{aligned} e_1&=(-1)e'_1+(-2)e'_2+2e'_3+1e'_4\\ e_2&=(-1)e'_1+0e'_2+0e'_3+1e'_4\\ e_3&=1e'_1+(-1)e'_2+2e'_3+0e'_4\\ e_4&=1e'_1+2e'_2+(-3)e'_3+1e'_4\\ \end{aligned} \right. $

Với một vector bất kỳ $\alpha = (a_1$, $a_2$, $a_3$, $a_4):$

$\alpha = (a_1$ - $a_2$ - $a_3$ + $a_4)e_1$ + $(a_2$ - $a_4)e_2$ + $(\frac{1}{2}a_1$ + $a_3$ - $\frac{1}{2}a_4)e_3$ + $(\frac{1}{2}a_4$ - $\frac{1}{2}a_1)e_4$

$\alpha = (-2a_1$ + $a_4)e'_1$ + $\left(\frac{-9}{2}a_1$ + $a_2$ + $a_3$ + $\frac{1}{2}a_4\right)e_2$ + $\left(\frac{9}{2}a_1$ - $a_2$ - $\frac{3}{2}a_4\right)e'_3$ + $\left(\frac{3}{2}a_1$ - $a_3$ + $\frac{1}{2}a_4\right)e'_4$.

Bài tập 1.9. Xét xem các tập hợp hàm số thực sau đây có lập thành không gian vector đối với

các phép toán thông thường hay không? Nếu có, hãy tìm số chiều của các không gian đó.

(a) Tập $\mathbb{R}[X]$ các đa thức của một ẩn X.

(b) Tập $C^{\infty}(\mathbb{R})$ các hàm thực khả vi vô hạn trên $\mathbb{R}$.

Tập $C^0(\mathbb{R})$ các hàm thực liên tục trên $\mathbb{R}$.

(c)

Tập các hàm thực bị chặn trên R.

(d)

(e) Tập các hàm f : $\mathbb{R} \to \mathbb{R}$ sao cho $sup<sub>x \in \mathbb{R}</sub>$ |f(x)| $\leq$ 1.

Tập các hàm f : $\mathbb{R} \to \mathbb{R}$ thỏa mãn điều kiện f(0) $=$ 0.

(f)

Tập các hàm f : $\mathbb{R} \to \mathbb{R}$ thỏa mãn điều kiện f(0) $=$ -1.

(g)

Tập các hàm thực đơn điệu trên R.

(h)

Chúng minh. (a) $\mathbb{R}[X]$ là một không gian vector trên $\mathbb{R}$.

Xét hệ vector (1, X, $X^2$, $\ldots$, $X^n)$

Hệ này là độc lập tuyến tính $vì\sum^{n} a_k X^k =$ 0khi và chỉ $khia_k =$ 0, $\forall$ k $\in \{0$, 1, ..., $n\}$



$<u>UITUUNU$ I. IMIUNU UIAN $TEUTUU</u>$

Với n tự nhiên, bất kỳ thì hệ (1, X, $X^2$, $\ldots$, $X^n)$ độc lập tuyến tính.

Giả sử $\mathbb{R}[X]$ hữu hạn sinh, dim $\mathbb{R}[X] =$ m, m $\in \mathbb{N}$.

Mà hệ vector (1, X, $X^2$, $\ldots$, $X^m)$ độc lập tuyến tính, gồm m + 1 phần tử. Điều này mâu

thuẫn.

Do đó dim $\mathbb{R}[X] = \infty$.

(b) $C^{\infty}(\mathbb{R})$ là một không gian vector trên $\mathbb{R}$.

$C^{\infty}(\mathbb{R}) \supset \mathbb{R}[X]$ nên dim $C^{\infty}(\mathbb{R}) = \infty$.

(c) $C^0(\mathbb{R})$ là một không gian vector trên $\mathbb{R}$.

$C^0(\mathbb{R}) \supset \mathbb{R}[X]$ nên dim $C^0(\mathbb{R}) = \infty$.

(d) Tập các hàm thực bị chặn trên $\mathbb$ R là một không gian vector.

Xét dãy hàm $f_n(x) = \cos(nx)$. Từng hàm này đều bị chặn. Cụ thể là $|f_n(x)| \leq$ 1.

Bằng quy nạp theo n, ta chứng minh được hệ $(f_0$, $f_1$, $\ldots$, $f_n)$ độc lập tuyến tính.

Như vậy không gian vector các hàm thực bị chặn trên $\mathbb$ R có số chiều là $\infty$.

Tập các hàm này không lập thành không gian vector. Lấy ví dụ:

(e)

f(x) $= \cos$ x, 2f(x) $= 2\cos$ x. Mà $\sup_{x \in \mathbb{R}} |2\cos$ x| $=$ 2. Tức là phép nhân vector với số thực

không đóng trên tập này.

Tập các hàm f : $\mathbb{R} \to \mathbb{R}$ thỏa mãn điều kiện f(0) $=$ 0 tạo thành một không gian vector trên

(f)

$\mathbb{R}$.

Hệ (X, $X^2$, $\ldots$, $X^n)$ độc lập tuyến tính với mọi n $\in \mathbb{N}$

Do đó không gian vector này có số chiều là $\infty$.

Tập các hàm f : $\mathbb{R} \to \mathbb{R}$ thỏa mãn điều kiện f(0) $=$ -1 không tạo thành không gian vector

(g)

trên $\mathbb$ R vì không có phần tử trung lập với phép cộng.

Tập các hàm thực đơn điệu trên R không tạo thành một không gian vector trên R.

(h)

Ví dụ, f(x) $= x^3$, g(x) $=$ -3x, hàm f(x) + g(x) $= x^3$ - 3x không phải hàm đơn điệu trên R.

Bài tập 1.10. Định nghĩa hai phép toán cộng và nhân với vô hướng trên tập hợp

V $= \{(x$, y) $\in \mathbb{R} \times \mathbb{R} \mid$ y $> 0\}$

như sau:

(x, y) + (u, v) $=$ (x + u, yv)

a(x, y) $=$ (ax, $y^a)$



  
Xét xem V có là một không gian vector thực đối với hai phép toán đó không. Nếu có, hãy tìm

một cơ sở của không gian ấy.

Chứng minh. Đầu tiên, V đóng với hai phép toán đã được định nghĩa. Bây giờ ta kiểm tra 8 tiên

đề không gian vector

(V1)

$((x_1$, $y_1)$ + $(x_2$, $y_2))$ + $(x_3$, $y_3) = (x_1$ + $x_2$, $y_1y_2)$ + $(x_3$, $y_3)$

$= ((x_1$ + $x_2)$ + $x_3$, $(y_1y_2)y_3)$

$=(x_1+(x_2+x_3),y_1(y_1y_3))$

$=(x_1,y_1)+(x_2+x_3,y_2y_3)$

$=(x_1,y_1)+((x_2,y_2)+(x_3,y_3))$

(V2) Phần tử trung lập là (0, 1).

(x, y) + (0, 1) $=$ (x + 0, y) $=$ (x, y)

(0,1) + (x,y) $=$ (0+x,y) $=$ (x,y)

(V3)

(x,y) + (-x, $y^{-1}) =$ (x + (-x), $yy^{-1}) =$ (0,1)

(-x, $y^{-1})$ + (x, y) $=$ (-x + x, $y^{-1}y) =$ (0, 1)

(V4)

$(x_1$, $y_1)$ + $(x_2$, $y_2) = (x_1$ + $x_2$, $y_1y_2)$

$=(x_2+x_1,y_2y_1)$

$=(x_2,y_2)+(x_1,y_1)$

(V5)

(a + b)(x, y) $=$ ((a + b)x, $y^{a+b})$

$=(ax+bx$, $y^ay^b)$

$=(ax$, $y^a)$ + (bx, $y^b)$

$=$ a(x, y) + b(x, y)



  
(V6)

$a((x_1,y_1)$ + $(x_2,y_2)) = a(x_1$ + $x_2$, $y_1y_2)$

$= (a(x_1$ + $x_2)$, $y_1^a y_2^a)$

$= (ax_1$ + $ax_2$, $y_1^a y_2^a)$

$=(ax_1,y_1^a)+(ax_2,y_2^a)$

$= a(x_1$, $y_1)$ + $a(x_2$, $y_2)$

(V7)

a(b(x, y)) $=$ a(bx, $y^{b})$

$=(a(bx),(y^b)^a)$

$=$ ((ab)x, $y^{ab})$

$=$ ab(x, y)

(V8)

1(x,y) $=$ (1x, y1) $=$ (x, y)

Như vậy, V là một không gian vector thực.

(x, y) $=$ (x, 1) + (0, y)

$=(x,1^x)+(0,e^{\ln y})$

$=$ x(1,1) + $\ln$ y(0,e)

Xét hệ vector ((1, 1), (0, e)) và ràng buộc tuyến tính a(1, 1) + b(0, e) $=$ (0, 1)

a(1,1) + b(0, e) $=$ (0, 1) $\Longleftrightarrow$ (a, 1) + (0, $e^b) =$ (0, 1)

$\iff$ (a, $e^b) =$ (0, 1)

$\iff \int$ a $=$ 0

$\int e^b=1$

$\iff$ a $=$ b $=$ 0

Như vậy, ((1,1),(0,e)) là một hệ sinh độc lập tuyến tính của V, và là một cơ sở của V.

$\overline{\phantom{a}}$

Bài tập 1.11. Ma trận chuyển từ một cơ sở sang một cơ sở khác thay đổi thế nào nếu:



$<u>UITUUNU$ I. IMIUNU UIAN $TEUTUU</u>$

Dổi chỗ hai vector trong cơ sở thứ nhất?

(a)

(b) Đổi chỗ hai vector trong cơ sở thứ hai?

(c) Đổi các vector trong mỗi cơ sở theo thứ tự ngược lại?

Chứng minh. Lấy hai cơ sở $(\alpha_1$, $\ldots$, $\alpha_n)$, $(\beta_1$, $\ldots$, $\beta_n)$.

Ta xét ma trận chuyển cơ sở $(c_{ij})_{n\times n}$ chuyển từ cơ sở thứ nhất sang cơ sở thứ hai.

$\beta_j = \sum_{i=1}^n c_{ij} \alpha_i$

Đổi chỗ hai vector $\alpha_i$ và $\alpha_j$ thì hai hàng thứ i và j trong ma trận chuyển cơ sở đổi chỗ.

(a)

(b) Đổi chỗ hai vector $\beta_i$ và $\beta_j$ thì hai cột thứ i và j trong ma trận chuyển cơ sở đổi chỗ.

Phép đảo thứ tự vector là hợp thành của nhiều phép đổi chỗ hai vector. Như vậy, khi đảo

(c)

các vector $\alpha_i$ theo thứ tự ngược lại thì thứ tự các vector hàng ngược lại. Sau khi đảo tiếp

các vector $\beta_i$ theo thứ tự ngược lại thì thứ tự các vector cột ngược lại.

Cu thể hơn, $(c_{ii})_{n\times n} \mapsto (d_{ii})_{n\times n}$ thì $d_{ij} = c_{(n+1-i)(n+1-j)}$.

Bài tập 1.12. Chứng minh rằng hai hệ vector (1, X, $X^2$, ..., $X^n)$ và (1, (X - a), (X - $a)^2$, ..., (X - $a)^n)$

$(a)^n$, trong đó a là một số thực, là các cơ sở của không gian $\mathbb{R}[X]_n$ các đa thức hệ số thực với bậc

không vượt quá n. Tìm ma trận chuyển từ cơ sở thứ nhất sang cơ sở thứ hai.

Chúng minh. Lấy một đa thức có bậc không quá n:

P(X) $= a_0$ + $a_1$ X + $a_2 X^2$ + $\cdots$ + $a_n X^n$

P(X) biểu thị tuyến tính được theo hệ vector (1, X, $X^2$, $\ldots$, $X^n)$.

Giả sử P(X) $= b_0$ + $b_1$ X + $b_2 X^2$ + $\cdots$ + $b_n X^n$.

Đồng nhất hai đa thức, ta được $a_i = b_i$, $\forall$ i $\in \{0$, 1, ..., $n\}$. Như vậy P(X) biểu thị tuyến

tính được theo hệ vector (1, X, $X^2$, $\ldots$, $X^n)$ theo cách duy nhất. Do đó hệ này là một cơ sở và

$\dim_{\mathbb{R}} \mathbb{R}[X]_n =$ n+1.

Nếu a $=$ 0 thì hệ vector (1, (X - a), (X - $a)^2$, ..., (X - $a)^n)$ trở thành hệ (1, X, $X^2$, ..., $X^n)$,

đây là một cơ sở.

Do đó ta chỉ xem xét trường hợp a $\neq$ 0.

Ta xét ràng buộc tuyến tính $\sum_{k=0}^{n} x_k$ (X - $a)^k =$ 0



$<u>UITUUNU$ I. IMIUNU UIAN $TEUTUU</u>$

Khai triển ràng buộc trên bằng khai triển Newton, hệ số của hạng tử $X^k$ bằng:

$\sum x_i \binom{i}{i-k} (-a)^{i-k}$

Từ ràng buộc tuyến tính và khai triển trên, ta đồng nhất hệ số và thu được hệ phương trình

tuyến tính thuần nhất (theo thứ tự, đồng nhất các hệ số của $X^n$, $X^{n-1}$, $\ldots$, X, 1):

$ \begin{cases}\n x_n \binom{n}{0} = 0 \\
 x_n \binom{n}{1} (-a)^1 + x_{n-1} \binom{n-1}{0} (-a)^0 = 0 \\
 x_n \binom{n}{2} (-a)^2 + x_{n-1} \binom{n-1}{1} (-a)^1 + x_{n-2} \binom{n-2}{0} (-a)^0 = 0 \\
 \vdots \\
 x_n \binom{n}{k} (-a)^k + x_{n-1} \binom{n-1}{k-1} (-a)^{k-1} + \dots + x_{n-k} \binom{n-k}{0} (-a)^0 = 0\n \end{cases} $

$ \begin{cases} \frac{1}{n} \\ x_n \binom{n}{n} (-a)^n + x_{n-1} \binom{n-1}{n-1} (-a)^{n-1} + \cdots + x_0 \binom{0}{0} (-a)^0 = 0 \end{cases} $

Giải phương trình trên, thay vào phương trình dưới, ta thu được nghiệm duy nhất của hệ là

$(x_n$, $x_{n-1}$, $\ldots$, $x_0) =$ (0, 0, $\ldots$, 0).

Như vậy $x_n = x_{n-1} = \cdots = x_1 = x_0 =$ 0 nên hệ vector (1, (X - a), (X - $a)^2$, $\ldots$, (X - $a)^n)$ độc

lập tuyến tính.

Không gian vector $\mathbb{R}[X]_n$ hữu hạn sinh nên (1, (X - a), (X - $a)^2$, $\ldots$, (X - $a)^n)$ cũng là một

cơ sở của $\mathbb{R}[X]_n$.

Bằng khai triển Newton, ta thu được ma trận chuyển cơ sở từ (1, X, $X^2$, $\dots$, $X^n)$ sang (1, (X -

a), (X - $a)^2$, $\ldots$, (X - $a)^n$ là:

$ \begin{pmatrix} 1 & \binom{1}{1}(-a) & \binom{2}{2}(-a)^2 & \cdots & \binom{n}{n}(-a)^n \\ 0 & 1 & \binom{2}{1}(-a)^1 & \cdots & \binom{n}{n-1}(-a)^{n-1} \\ 0 & 0 & 1 & \cdots & \binom{n}{n-2}(-a)^{n-2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 \end{pmatrix} $

Các yếu tố của ma trận $(c_{ij})_{(n+1)\times(n+1)}$, trong đó, 0 $\le$ i, j $\le$ n này có thể được xác định nhanh



$<u>UITUUNU$ I. IMIUNU UIAN $VEULUIU</u>$

chóng như sau:

$ \left\{ \begin{aligned} c_{ij} &= \binom{j}{i} (-a)^{j-i} \quad , \quad \text{if } i \leq j \\ c_{ij} &= 0 \end{aligned} \right. , if i > j $

Bài tập 1.13. Tìm các tọa độ của đa thức f(X) $= a_0$ + $a_1X$ + $\cdots$ + $a_nX^n$ đối với hai cơ sở nói

trên.

Chứng minh. Tọa độ của f(X) đối với cơ sở (1, X, $\ldots$, $X^n)$ là:

$(a_0,a_1,\ldots,a_n)$

Theo bài toán trên, (1, (X - a), (X - $a)^2$, $\ldots$, (X - $a)^n)$ cũng là một cơ sở của không gian

vector $\mathbb{R}[X]_n$.

Từng vector trong cơ sở thứ nhất có thể biểu thị tuyến tính duy nhất theo cơ sở thứ hai.

$ \begin{cases}\n1 & = 1 \\
X & = a + (X - a) \\
X^2 & = a^2 + 2a(X - a) + (X - a)^2 \\
X^3 & = a^3 + 3a^2(X - a) + 3a(X - a)^2 + (X - a)^3 \\
\vdots \\
X^n & = a^n + \binom{n}{1}a^{n-1}(X - a) + \binom{n}{2}a^{n-2}(X - a)^2 + \dots + \binom{n}{n-1}(X - a)^{n-1} + (X - a)^n\n\end{cases} $

Nhân hai về của phương trình thứ k với $a_k$, rồi cộng về theo về, ta thu được

f(X) $= \sum_{k=0}^{n} b_k$ (X - $a)^k$

trong đó:

$b_k = \sum_{i=0}^{k} a_i \binom{k+i}{k} a^i$

Bài tập 1.14. Cho không gian vector con L của không gian $\mathbb{R}[X]$ các đa thức hệ số thực. Chứng

minh rằng nếu L chứa ít nhất một đa thức bậc k với mọi k $=$ 0, 1, ..., n, nhưng không chứa đa

thức nào với bậc lớn hơn n thì L chính là không gian con $\mathbb{R}[X]_n$ tất cả các đa thức bậc không vượt

quá n.



$<u>UITUUNU$ I. IMIUNU UIAN $TEUTUU</u>$

Chứng minh. Đặt các đa thức bậc 0, 1, 2, ..., n trong L lần lượt là:

$ \begin{cases}\nf_0(X) = a_{00} \\
f_1(X) = a_{10} + a_{11}X \\
f_2(X) = a_{20} + a_{21}X + a_{22}X^2 \\
\vdots \\
f_k(X) = a_{k0} + a_{k1}X + a_{k2}X^2 + \dots + a_{k(k-1)}X^{k-1} + a_{kk}X^k \\
\vdots \\
f_n(X) = a_{n0} + a_{n1}X + a_{n2}X^2 + \dots + a_{n(n-1)}X^{n-1} + a_{nn}X^n\n\end{cases} $

trong đó, $a_{ii} \neq$ 0, $\forall$ i $\in \{0$, 1, 2, ..., $n\}$

Ta sẽ chứng minh $X^k$ có thể biểu thị tuyến tính được theo hệ vector $(f_0(X)$, $f_1(X)$, $\ldots$, $f_n(X))$,

với mọi k $\in \{0$, 1, ..., $n\}$. Cụ thể hơn, ta chứng minh điều này bằng quy nạp.

$X^0 =$ 1 $= a_{00}^{-1} a_{00} = a_{00}^{-1} f_0(X)$

Giả sử điều trên đúng từ 0 đến k-1, với k-1 $<$ n.

$f_k(X) = a_{k0}$ + $a_{k1}X$ + $a_{k2}X^2$ + $\cdots$ + $a_{k(k-1)}X^{k-1}$ + $a_{kk}X^k$

$\Rightarrow X^{k} = a_{kk}^{-1}(f_{k}(X)$ - $a_{k0}$ - $a_{k1}X$ - $a_{k2}X^{2}$ - $\cdots a_{k(k-1)}X^{k-1})$

Theo giả thiết quy nạp, các đa thức 1, X, ..., $X^{k-1}$ biểu thị tuyến tính được theo $f_0(X)$, $f_1(X)$,

..., $f_n(X)$ nên đẳng thức trên cho thấy giả thiết vẫn đúng với k.

Như vậy, hệ (1, X, ..., $X^n)$ biểu thị tuyến tính được theo $(f_0(X)$, $f_1(X)$, ..., $f_n(X))$.

Xét một đa thức bất kỳ với bậc không quá n:

f(X) $= a_0$ + $a_1X$ + $a_2X^2$ + $\cdots$ + $a_nX^n$

Hiển nhiên f(X) biểu thị tuyến tính được theo (1, X, $\ldots$, $X^n)$. Quan hệ biểu thị tuyến tính có

tính bắc cầu nên f(X) cũng biểu thị tuyến tính được theo $(f_0(X)$, $f_1(X)$, $\ldots$, $f_n(X))$.

Do đó $span(\{f_0(X)$, $f_1(X)$, $\ldots$, $f_n(X)\}) = \mathbb{R}[X]_n$.

L không chứa đa thức nào có bậc lớn hơn n, cùng với điều trên, ta kết luận L $= \mathbb{R}[X]_n$. $\square$

Bài tập 1.15. Chứng minh rằng tập hợp các vector $(x_1$, $x_2$, $\ldots$, $x_n) \in \mathbb{R}_n$ thỏa mãn hệ thức

$x_1$ + $2x_2$ + $\cdots$ + $nx_n =$ 0 là một không gian vector con của $\mathbb{R}_n$. Tìm số chiều và một cơ sở của

không gian vector con đó.

Chứng minh. Ta chứng minh bài toán tổng quát hơn: tập hợp U các vector $(x_1$, $x_2$, $\ldots$, $x_n) \in \mathbb{R}_n$



$<u>UITUUNU$ I. IMIUNU UIAN $TEULUI</u>$

thỏa mãn hệ thức $\sum a_i x_i =$ 0 là một không gian vector con của $\mathbb{R}_n$.

$\mathbf{x} = (x_1$, $x_2$, $\ldots$, $x_n)$, $\mathbf{y} = (y_1$, $y_2$, $\ldots$, $y_n)$.

$\mathbf{x}$ + $\mathbf{y} = (x_1$ + $y_1$, $x_2$ + $y_2$, $\dots$, $x_n$ + $y_n)$. $\sum_{i=0}^{n} a_i (x_i$ + $y_i) = \sum_{i=0}^{n} a_i x_i$ + $\sum_{i=0}^{n} a_i y_i =$ 0 + 0 $=$ 0.

$\sum a_i(ax_i) =$ a $\sum a_i x_i =$ a $\cdot$ 0 $=$ 0.

$i=0$

Do đó U là một không gian vector con của $\mathbb{R}_n$.

Xét không gian con W $= \text{span}(\{(a_1$, $\ldots$, $a_n)\})$. dim W $=$ 1.

$\mathbf{x} = (x_1$, $\ldots$, $x_n) \in \mathbb{R}_n$.

$\underbrace{(x_1,\ldots,x_n)}_{\smile} = \left(x_1$ - $\frac{a_1 \sum_{i=1}^n a_i x_i}{\sum_{i=1}^n a_i^2},\ldots,x_n$ - $\frac{a_n \sum_{i=1}^n a_i x_i}{\sum_{i=1}^n a_i^2}\right)$ + $\frac{\sum_{i=1}^n a_i x_i}{\sum_{i=1}^n a_i^2}(a_1,\ldots,a_n)$

$\in\!$ U

$\in \!\!$ W

Do đó $\mathbb{R}_n =$ U + W. Mà U $\cap$ W $= \{(0$, $\ldots$, $0)\}\$ nên $\mathbb{R}_n =$ U $\oplus$ W.

Vì dim $\mathbb{R}_n = \dim$ U + $\dim$ W nên dim U $=$ n - $\dim$ W.

Nếu $(a_1$, ..., $a_n) =$ (0, ..., 0) thì dim W $=$ 0 nên dim U $=$ n.

Lúc này một cơ sở của $\mathbb{R}_n$ là cơ sở của U.

Còn nếu $(a_1$, $\ldots$, $a_n) \neq$ (0, $\ldots$, 0) thì dim W $=$ 1, kéo theo dim U $=$ n - 1.

Không mất tính tổng quát, giả sử $a_1 \neq$ 0, xét hệ vector sau:

$ \left\{\n\begin{aligned}\n(-a_2, a_1, 0, \ldots, 0) \\
(-a_3, 0, a_1, \ldots, 0) \\
\ldots \\
(-a_n, 0, 0, \ldots, a_1)\n\end{aligned}\n\right\} $

Xét biểu thị tuyến tính:

$b_2(-a_2$, $a_1$, 0, $\ldots$, 0) + $b_3(-a_3$, 0, $a_1$, $\ldots$, 0) + $\cdots$ + $b_n(-a_n$, 0, 0, $\ldots$, $a_1) =$ (0, 0, 0, $\ldots$, 0)

Đồng nhất các yếu tố, ta suy ra $b_2a_1 = b_3a_1 = \cdots = b_na_1 =$ 0 nên $b_2 = b_3 = \cdots = b_n$ nên hệ

vector trên độc lập tuyến tính. Số vector trong hệ này bằng n-1, bằng số chiều của U nên đây

là một cơ sở của U.

Bài tập 1.16. Tìm tất cả các $\mathbb{F}_2-không$ gian vector con một và hai chiều của $\mathbb{F}_2^3$. Giải bài toán

tương tự đối với không gian $\mathbb{F}_p^3$, trong đó p là một số nguyên tố.



UITUUITU

THUING CITIN VEUTUL

Chứng minh. Các không gian vector con một chiều của $\mathbb{F}_2^3$ là:

$ \left\{\begin{pmatrix}0\\0\\0\end{pmatrix},\begin{pmatrix}0\\0\\1\end{pmatrix}\right\},\left\{\begin{pmatrix}0\\0\\0\end{pmatrix},\begin{pmatrix}0\\1\\0\end{pmatrix}\right\},\left\{\begin{pmatrix}0\\0\\0\end{pmatrix},\begin{pmatrix}1\\0\\0\end{pmatrix}\right\},\right\} $

$ \left\{\left(\begin{matrix}0\\0\\0\end{matrix}\right),\left(\begin{matrix}0\\1\\1\end{matrix}\right)\right\},\left\{\left(\begin{matrix}0\\0\\0\end{matrix}\right),\left(\begin{matrix}1\\1\\0\end{matrix}\right)\right\},\left\{\left(\begin{matrix}0\\0\\0\end{matrix}\right),\left(\begin{matrix}1\\0\\1\end{matrix}\right)\right\},\left\{\left(\begin{matrix}0\\0\\0\end{matrix}\right),\left(\begin{matrix}1\\1\\1\end{matrix}\right)\right\} $

Các không gian vector con hai chiều của $\mathbb{F}_2^3$ là:

$ \left\{\begin{pmatrix}0\\0\\0\end{pmatrix},\begin{pmatrix}0\\0\\1\end{pmatrix},\begin{pmatrix}0\\1\\0\end{pmatrix},\begin{pmatrix}0\\1\\1\end{pmatrix}\right\},\left\{\begin{pmatrix}0\\0\\0\end{pmatrix},\begin{pmatrix}0\\0\\1\end{pmatrix},\begin{pmatrix}1\\0\\0\end{pmatrix},\begin{pmatrix}1\\0\\1\end{pmatrix},\begin{pmatrix}0\\1\\0\end{pmatrix},\begin{pmatrix}1\\0\\0\end{pmatrix},\begin{pmatrix}1\\1\\0\end{pmatrix}\right\},\right. $

$ \left\{\begin{pmatrix}0\\0\\0\end{pmatrix},\begin{pmatrix}0\\0\\1\end{pmatrix},\begin{pmatrix}1\\1\\0\end{pmatrix},\begin{pmatrix}1\\1\\1\end{pmatrix}\right\},\left\{\begin{pmatrix}0\\0\\0\end{pmatrix},\begin{pmatrix}0\\1\\0\end{pmatrix},\begin{pmatrix}1\\0\\1\end{pmatrix}\right\},\begin{pmatrix}0\\0\\0\end{pmatrix},\begin{pmatrix}1\\0\\0\end{pmatrix},\begin{pmatrix}0\\1\\1\end{pmatrix},\begin{pmatrix}1\\1\\1\end{pmatrix}\right\}, $

$ \left\{ \left\{ \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}, \left\{ \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}, \left\{ \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \left\{ \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \right\} \right\} \right\} $

Chưa xác định được các không gian con một và hai chiều trong trường hợp tổng quát.

$ \begin{array}{c} \hline \end{array} $

Bài tập 1.17. Chứng minh rằng các ma trận vuông đối xứng cỡ n với các yếu tố trong trường

$\mathbb$ F lập thành một không gian vector con của M(n $\times$ n, $\mathbb$ F). Tìm số chiều và một cơ sở của $\mathbb$ F-không

gian vector con dó.

Chứng minh. P $= (p_{ij})_{n \times n}$, Q $= (q_{ij})_{n \times n}$ là hai ma trận đối xứng.

P + Q $= (p_{ij}$ + $q_{ij})_{n \times n}$.

Vì $p_{ij} = p_{ji}$, $q_{ij} = q_{ji}$ nên $p_{ij}$ + $q_{ij} = p_{ji}$ + $q_{ji}$, do đó P + Q cũng là ma trận đối xứng.

aP $= (ap_{ij})_{n \times n}$.

Vì $p_{ij} = p_{ji}$ nên $ap_{ij} = ap_{ji}$, do đó aP cũng là ma trận đối xứng.

Như vậy tập hợp các ma trận đối xứng cỡ n với các yếu tố trong trường $\mathbb$ F là một không gian

vector con của M(n $\times$ n, $\mathbb{F})$.

Dặt $S_{ij}$ là ma trận vuông cỡ n sao cho yếu tố hàng i, cột j và yếu tố hàng j, cột i bằng 1, các

yếu tố còn lại bằng 0.

P $= \sum_{1 \leq$ i $\leq$ j $\leq n} p_{ij} S_{ij}$



$<u>UITUUNU$ I. IMIUNU UIAN $VEULUIU</u>$

Xét biểu thị tuyến tính 0 $= \sum s_{ij} S_{ij}$.

$1\leq i\leq j\leq$ n

$ \Rightarrow \begin{pmatrix} 0 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 \end{pmatrix} = \begin{pmatrix} s_{11} & s_{12} & \cdots & s_{1n} \\ s_{12} & s_{22} & \cdots & s_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ s_{1n} & s_{2n} & \cdots & s_{nn} \end{pmatrix} $

Đồng nhất các yếu tố, ta suy ra $s_{ij} =$ 0, $\forall$ i, j, tức là hệ $\{S_{ij}\}_{1 \le$ i $\le$ j $\le n}$ độc lập tuyến tính.

P luôn biểu thị tuyến tính được theo hệ độc lập tuyến tính $\{S_{ij}\}_{1\leq i\leq j\leq n}$ nên đây chính là một

cơ sở.

Số chiều của không gian vector các ma trận vuông đối xứng cỡ n là $\frac{n(n+1)}{2} = \binom{n+1}{2}$. $\Box$

Bài tập 1.18. Chứng minh rằng các ma trận vuông phản đối xứng cỡ n lập thành một không

gian vector con của M(n $\times$ n, $\mathbb{F})$. Tìm số chiều và một cơ sở của $\mathbb{F}-không$ gian vector con đó.

Chứng minh. P $= (p_{ij})_{n \times n}$ và Q $= (q_{ij})_{n \times n}$ là hai ma trận phản đối xứng.

P + Q $= (p_{ij}$ + $q_{ij})_{n \times n}$.

Vì $p_{ij}$ + $p_{ji} =$ 0, $q_{ij}$ + $q_{ji} =$ 0 nên $(p_{ij}$ + $q_{ij})$ + $(p_{ji}$ + $q_{ji}) =$ 0. Do đó P + Q cũng là ma trận

phản đối xứng.

aP $= (ap_{ii})_{n \times n}$.

Vì $p_{ij}$ + $p_{ji} =$ 0 nên $ap_{ij}$ + $ap_{ji} =$ 0. Do đó aP cũng là ma trận phản đối xứng.

Vậy các ma trận phản đối xứng lập thành một không gian vector con của M(n $\times$ n, $\mathbb{F})$.

Để tìm số chiều và cơ sở của không gian vector con này, chúng ta xét hai trường hợp sau đây

Trường hợp 1. $Char(\mathbb{F}) \neq$ 2

P là ma trận phản đối xứng nên $p_{ii}$ + $p_{ii} =$ 0. Mà đặc số của F khác 2 nên $p_{ii} =$ 0.

Đặt $A_{ij}$ là ma trận vuông cỡ n mà yếu tố hàng i, cột j bằng 1, yếu tố hàng j, cột i bằng

-1, các yếu tố còn lại bằng 0.

P $= \sum p_{ij} A_{ij}$

1 $\leq$ i $<$ j $\leq$ n

Xét biểu thị tuyến tính 0 $= \sum a_{ij} A_{ij}$

$1\leq$ i $<$ j $\leq$ n

$ \begin{pmatrix} 0 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 \end{pmatrix} = \begin{pmatrix} 0 & a_{12} & \cdots & a_{1n} \\ -a_{12} & 0 & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ -a_{1n} & -a_{2n} & \cdots & 0 \end{pmatrix} $



$<u>UITUUNU$ I. IMIUNU UIAN $TEUTUU</u>$

Đồng nhất hệ số, ta được $a_{ij} =$ 0. Do đó hệ vector $\{A_{ij}\}_{1 \leq$ i $<$ j $\leq n}$ độc lập tuyến tính.

Mọi ma trận phản đối xứng P biểu thị tuyến tính được qua hệ độc lập tuyến tính $\{A_{ij}\}_{1\leq$ i $<$ j $\leq n}$

nên $\{A_{ij}\}_{1 \leq$ i $\leq$ j $\leq n}$ là một cơ sở.

Vậy số chiều của không gian vector các ma trận phản đối xứng $là\frac{n(n-1)}{2} = \binom{n}{2}$, cơ sở là

hệ các vector $\{A_{ij}\}_{1 \leq$ i $\leq$ j $\leq n}$.

Trường hợp 2. $Char(\mathbb{F}) =$ 2

Dặc số của F bằng 2 nên $p_{ii}$ + $p_{ii} =$ 0, $\forall p_{ii}$.

Đặt $A_{ij}(1 \leq$ i $<$ j $\leq$ n) là ma trận vuông cỡ n mà yếu tố hàng i, cột j bằng 1, yếu tố hàng

j, cột i bằng -1, các yếu tố còn lại bằng 0. $A_{ii}$ là ma trận vuông cỡ n, yếu tố hàng i, cột i

bằng 1, các yếu tố còn lại bằng 0.

P $= \sum_{i=1}^{n} p_{ii} A_{ii}$ + $\sum_{1 \leq$ i $\leq$ j $\leq n} p_{ij} A_{ij}$

Xét biểu thị tuyến tính 0 $= \sum_{i=1}^n a_{ii} A_{ii}$ + $\sum_{1 \leq$ i $\leq$ j $\leq n} a_{ij} A_{ij}$

$ \begin{pmatrix} 0 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ -a_{12} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ -a_{1n} & -a_{2n} & \cdots & a_{nn} \end{pmatrix} $

Đồng nhất hệ số, ta được $a_{ij} =$ 0, $\forall$ 1 $\leq$ i $\leq$ j $\leq$ n. Do đó hệ vector $\{A_{ij}\}_{1 \leq$ i $\leq$ j $\leq n}$ độc lập

tuyến tính.

Mọi ma trận phản đối xứng P đều biểu thị tuyến tính được qua hệ độc lập tuyến tính

${A_{ij}}_{1\leq i\leq j\leq n}$ nên ${A_{ij}}_{1\leq i\leq j\leq n}$ là một cơ sở.

Vậy số chiều của không gian vector các ma trận phản đối xứng là $\frac{n(n+1)}{2} = \binom{n+1}{2}$.

Bài tập 1.19. Giả sử $V_1 \subset V_2$ là các không gian vector con của V. Chứng minh rằng dim $V_1 \leq$

dim $V_2$, đẳng thức xảy ra khi và chỉ khi $V_1 = V_2$. Khẳng định "đẳng thức xảy ra khi và chỉ khi

$V_1 = V_2"$ có còn đúng không nếu $V_1$ và $V_2$ là các không gian vector con bất kì của V?

Chứng minh. $V<sub>1</sub> \subset V_2$ thì mọi hệ độc lập tuyến tính trong $V<sub>1</sub>$ cũng độc lập tuyến tính trong $V<sub>2</sub>$.

Như vậy, cơ sở của $V_1$ cũng độc lập tuyến tính trong $V_2$.



  
Nếu cơ sở của $V_1$ là độc lập tuyến tính cực đại trong $V_2$ thì $V_1$ và $V_2$ có cùng cơ sở, do đó

$V_1 = V_2$ và dim $V_1 = \dim V_2$.

Nếu cơ sở của $V_1$ chưa phải độc lập tuyến tính cực đại trong $V_2$ thì dim $V_1 <$ dim $V_2$.

Lập luận trên cho thấy dim $V_1 \leq \dim V_2$, đẳng thức xảy ra khi và chỉ khi $V_1 = V_2$.

Khẳng định "đẳng thức xảy ra khi và chỉ khi $V_1 = V_2"$ nói chung không đúng. Ví dụ:

Trên trường số thực, hai không gian vector con của $\mathbb{R}_2$ là $span(\{(1,0)\})$ và $span(\{(0,1)\})$ đều

có số chiều bằng 1 nhưng hai không gian này lại không bằng nhau.

Bài tập 1.20. Giả sử $V_1$, $V_2$ là các không gian vector con của V. Chứng minh rằng nếu dim $V_1$ +

dim $V_2 >$ dim V thì $V_1 \cap V_2$ chứa ít nhất một vector khác không.

Chúng minh. Theo công thức Grassmann, $\dim(V_1 \cap V_2) = \dim V_1$ + $\dim V_2$ - $\dim(V_1$ + $V_2)$

$\dim$ V - $\dim(V_1$ + $V_2) \geq$ 0.

Do đó $V_1 \cap V_2$ không phải không gian vector không, và chứa ít nhất một vector khác không.

$\Box$

Bài tập 1.21. Với giả thiết như bài tập trước, chứng minh rằng nếu $dim(V_1$ + $V_2) = \dim(V_1 \cap V_2)$ + 1

thì $V_1$ + $V_2$ trùng với một trong hai không gian con đã cho, còn $V_1 \cap V_2$ trùng với không gian con

còn lại.

Chúng minh. $V_1 \cap V_2$ là không gian con của $V_1$, $V_2$ nên dim $V_1 \geq \dim(V_1 \cap V_2)$ và dim $V_2 \geq \dim(V_1 \cap V_2)$

$V_2)$.

Mà dim $V_1$ + $\dim V_2 = \dim(V_1$ + $V_2)$ + $\dim(V_1 \cap V_2) =$ 1 + $2\dim(V_1 \cap V_2)$.

Vì dim $V_1$, dim $V_2$, $dim(V_1 \cap V_2)$ là các số nguyên không âm nên đúng một trong hai điều sau

xảy ra

• dim $V_1 = \dim(V_1 \cap V_2)$, dim $V_2 =$ 1 + $\dim(V_1 \cap V_2) = \dim(V_1$ + $V_2)$. Do đó $V_1 = V_1 \cap V_2$ (vì

$V_1 \cap V_2$ là không gian con của $V_1)$ và $V_2 = V_1$ + $V_2$ (vì $V_2$ là không gian con của $V_1$ + $V_2)$.

• dim $V_1 =$ 1 + $\dim(V_1 \cap V_2) = \dim(V_1$ + $V_2)$, dim $V_2 = \dim(V_1 \cap V_2)$. Do đó $V_1 = V_1$ + $V_2$ (vi

$V_1$ là không gian con của $V_1$ + $V_2)$ và $V_2 = V_1 \cap V_2$ (vì $V_1 \cap V_2$ là không gian con của $V_2)$.

Tìm hạng của các hệ vector sau đây:

Bài tập 1.22. $\alpha_1 =$ (1, 2, 0, 1), $\alpha_2 =$ (1, 1, 1, 0), $\alpha_3 =$ (1, 0, 1, 0), $\alpha_4 =$ (1, 3, 0, 1).



$<u>UITUUNU$ I. IMIUNU UIAN $TEUTUU</u>$

$L\delta$ i giải.

$ \begin{bmatrix} \alpha_1 \\ \alpha_2 \\ \alpha_3 \\ \alpha_4 \end{bmatrix} = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 1 & 1 & 1 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 3 & 0 & 1 \end{pmatrix} \Longrightarrow \begin{bmatrix} \alpha_1 \\ \alpha_2 - \alpha_1 \\ \alpha_3 - \alpha_1 \\ \alpha_4 - \alpha_1 \end{bmatrix} = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & -1 & 1 & -1 \\ 0 & -2 & 1 & -1 \\ 0 & 1 & 0 & 0 \end{pmatrix} $

$ \Rightarrow \begin{bmatrix} \alpha_1 \\ \alpha_2 - \alpha_1 \\ \alpha_3 - 2\alpha_2 + \alpha_1 \\ \alpha_4 + \alpha_2 - 2\alpha_2 \end{bmatrix} = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & -1 & 1 & -1 \\ 0 & 0 & -1 & 1 \\ 0 & 0 & 1 & -1 \end{pmatrix} \Rightarrow \begin{bmatrix} \alpha_1 \\ \alpha_2 - \alpha_1 \\ \alpha_3 - 2\alpha_2 + \alpha_1 \\ \alpha_4 + \alpha_2 - \alpha_2 - \alpha_1 \\ \alpha_5 + \alpha_6 - \alpha_7 - \alpha_7 \end{bmatrix} = \begin{pmatrix} 1 & 2 & $

Như vậy, $\text{rank}(\alpha_1$, $\alpha_2$, $\alpha_3$, $\alpha_4) =$ 3.

Bài tập 1.23. $\alpha_1 =$ (1, 1, 1, 1), $\alpha_2 =$ (1, 3, 1, 3), $\alpha_3 =$ (1, 2, 0, 2), $\alpha_4 =$ (1, 2, 1, 2), $\alpha_5 =$ (3, 1, 3, 1).

Lời giải.

$ \begin{bmatrix} \alpha_1 \\ \alpha_2 \\ \alpha_3 \\ \alpha_4 \\ \alpha_5 \end{bmatrix} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 3 & 1 & 3 \\ 1 & 2 & 0 & 2 \\ 1 & 2 & 1 & 2 \\ 3 & 1 & 3 & 1 \end{pmatrix} \Longrightarrow \begin{bmatrix} \alpha_1 \\ \alpha_2 - \alpha_1 \\ \alpha_3 - \alpha_1 \\ \alpha_4 - \alpha_3 \\ \alpha_5 - 3\alpha_1 + \alpha_4 - \alpha_2 \end{bmatrix} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 2 & 0 & 2 \\ 0 & 1 & -1 & 1 $

$ \implies \begin{bmatrix} \alpha_1 \\ \alpha_2 - \alpha_1 \\ \alpha_3 - \frac{1}{2} \alpha_2 + \frac{1}{2} \alpha_1 \\ \alpha_4 - \alpha_3 \\ \alpha_5 - 3 \alpha_1 + \alpha_4 - \alpha_2 \end{bmatrix} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 2 & 0 & 2 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \implies \begin{bmatrix} \alpha_1 \\ \alpha_2 - \alpha_1 \\ \alpha_3 - \frac{1}{2} \alpha_2 + \frac{1}{2} \alpha_1 \\ \alpha_4 - $

Như vậy, $\text{rank}(\alpha_1$, $\alpha_2$, $\alpha_3$, $\alpha_4$, $\alpha_5) =$ 3.

Tìm một cơ sở của tổng và một cơ sở của giao của các không gian vector con sinh bởi các hệ

vector $\alpha_1$, $\ldots$, $\alpha_k$ và $\beta_1$, $\ldots$, $\beta_\ell$ sau đây:

Bài tập 1.24. $\alpha_1 =$ (1, 2, 1), $\alpha_2 =$ (1, 1, -1), $\alpha_3 =$ (1, 3, 3),

$\beta_1 =$ (2, 3, -1), $\beta_2 =$ (1, 2, 2), $\beta_3 =$ (1, 1, -3).

Lời giải. A $= \text{span}(\alpha_1$, $\alpha_2$, $\alpha_3)$, B $= \text{span}(\beta_1$, $\beta_2$, $\beta_3)$.

$ \begin{bmatrix} \alpha_1 \\ \alpha_2 \\ \alpha_3 \end{bmatrix} = \begin{pmatrix} 1 & 2 & 1 \\ 1 & 1 & -1 \\ 1 & 3 & 3 \end{pmatrix} \Longrightarrow \begin{bmatrix} \alpha_1 \\ \alpha_2 - \alpha_1 \\ \alpha_3 + \alpha_2 - 2\alpha_1 \end{bmatrix} = \begin{pmatrix} 1 & 2 & 1 \\ 0 & -1 & -2 \\ 0 & 0 & 0 \end{pmatrix} $



  
$ \begin{bmatrix} \beta_1 \\ \beta_2 \\ \beta_3 \end{bmatrix} = \begin{pmatrix} 2 & 3 & -1 \\ 1 & 2 & 2 \\ 1 & 1 & -3 \end{pmatrix} \Longrightarrow \begin{bmatrix} \beta_1 \\ 2\beta_2 - \beta_1 \\ \beta_3 + \beta_2 - \beta_1 \end{bmatrix} = \begin{pmatrix} 2 & 3 & -1 \\ 0 & 1 & 5 \\ 0 & 0 & 0 \end{pmatrix} $

Suy ra $rank(\alpha_1$, $\alpha_2$, $\alpha_3) = rank(\beta_1$, $\beta_2$, $\beta_3) =$ 2.

Một cơ sở của $span(\alpha_1$, $\alpha_2$, $\alpha_3)$ là (1, 2, 1), (0, -1, -2).

Một cơ sở của $\text{span}(\beta_1$, $\beta_2$, $\beta_3)$ là (2, 3, -1), (0, 1, 5).

Tương tự phương pháp tính hạng của hệ vector, ta tính được

$rank((2,3,-1),(1,2,1),(0,1,5),(0,-1,-2))=3$.

Vậy dim(A + B) $=$ 3 $= \dim \mathbb{C}_3$ nên một cơ sở của A + B là (1,0,0), (0,1,0), (0,0,1).

Ta tìm A $\cap$ B. Một vector thuộc A $\cap$ B biểu thị tuyến tính được theo $\alpha_1$, $\alpha_2$, $\alpha_3$ và $\beta_1$, $\beta_2$, $\beta_3$.

Xét ràng buộc sau

$a_1(1,2,1)$ + $a_2(0,-1,-2) = b_1(2,3,-1)$ + $b_2(0,1,5)$

Giải ra ta được

$a_1 = 3a_2 b_1 = \frac{1}{2}a_1 = \frac{3}{2}a_2 b_2 = \frac{1}{2}a_1$ - $a_2 = \frac{1}{2}a_2$

Vậy A $\cap$ B $= \text{span}(3(1,2,1)$ + (0,-1,-2)) $= \text{span}(3,5,1)$. Cơ sở của A $\cap$ B là (3,5,1).

$\Box$

Bài tập 1.25. $\alpha_1 =$ (1, 2, 1, -2), $\alpha_2 =$ (2, 3, 1, 0), $\alpha_3 =$ (1, 2, 2, -3),

$\beta_1 =$ (1, 1, 1, 1), $\beta_2 =$ (1, 0, 1, -1), $\beta_3 =$ (1, 3, 0, -4).

Lời giải. A $= \text{span}(\alpha_1$, $\alpha_2$, $\alpha_3)$, B $= \text{span}(\beta_1$, $\beta_2$, $\beta_3)$.

$ \begin{bmatrix} \alpha_1 \\ \alpha_2 \\ \vdots \end{bmatrix} = \begin{pmatrix} 1 & 2 & 1 & -2 \\ 2 & 3 & 1 & 0 \\ 1 & 2 & 2 & -2 \\ 1 & 2 & 2 & -2 \\ 2 & 2 & 1 & -2 \\ 2 & 2 & 2 & -2 \\ 2 & 2 & 2 & -2 \\ 2 & 2 & 2 & -2 \\ 2 & 2 & 2 & -2 \\ 2 & 2 & 2 & -2 \\ 2 & 2 & 2 & -2 \\ 2 & 2 & 2 & -2 \\ 2 & 2 & 2 & -2 \\ 2 & 2 & 2 & -2 \\ 2 & 2 & 2 & -2 \\ 2 & 2 & 2 $

Do đó $rank(\alpha_1$, $\alpha_2$, $\alpha_3) =$ 3.

$ \begin{bmatrix} \beta_1 & 1 & 1 & 1 \end{bmatrix} \beta_1 \begin{bmatrix} 1 & 1 & 1 \end{bmatrix} $

$ \begin{vmatrix} \beta_2 \\ \beta_3 \end{vmatrix} = \begin{pmatrix} 1 & 0 & 1 & -1 \\ 1 & 3 & 0 & -4 \end{pmatrix} \implies \begin{vmatrix} \beta_2 - \beta_1 \\ \beta_3 + 2\beta_2 - 3\beta_1 \end{vmatrix} = \begin{pmatrix} 0 & -1 & 0 & -2 \\ 0 & 0 & -1 & -9 \end{pmatrix} $

Do đó $rank(\beta_1$, $\beta_2$, $\beta_3) =$ 3.



$<u>UITUUNU$ I. IMIUNU UIAN $TEUTUU</u>$

$(\alpha_1$, $\alpha_2$, $\alpha_3)$ là một cơ sở của A. $(\beta_1$, $\beta_2$, $\beta_3)$ là một cơ sở của B.

$ \begin{bmatrix} \alpha_1 \\ \beta_1 \\ \alpha_2 \\ \beta_2 \\ \alpha_3 \\ \beta_3 \end{bmatrix} = \begin{pmatrix} 1 & 2 & 1 & -2 \\ 1 & 1 & 1 & 1 \\ 2 & 3 & 1 & 0 \\ 1 & 0 & 1 & -1 \\ 1 & 2 & 2 & -3 \\ 1 & 3 & 0 & -4 \end{pmatrix} \Longrightarrow \begin{bmatrix} \alpha_1 \\ \beta_1 \\ \alpha_2 - 2\alpha_1 \\ \beta_2 - \beta_1 \\ \alpha_3 - \alpha_1 \\ \beta_3 + 2\beta_2 - 3\beta_1 \end{bmatrix} = \begin{pmatrix} 1 & 2 & 1 & -2 \\ 1 $

$ \begin{bmatrix}\n\alpha_1 \\
\beta_1 - \alpha_1 \\
\alpha_2 - 2\alpha_1 \\
\beta_2 - \beta_1 - \alpha_2 + 2\alpha_1 \\
\alpha_3 - \alpha_1 \\
3 + 2\beta_2 - 3\beta_1 - \alpha_3 + \alpha_1\n\end{bmatrix} = \begin{pmatrix}\n1 & 2 & 1 & -2 \\
0 & -1 & 0 & 3 \\
0 & -1 & -1 & 4 \\
0 & 0 & 1 & -6 \\
0 & 0 & 1 & -1 \\
0 & 0 & 0 & -10\n\end{pmatrix} $

$\left[\beta_3+2\beta_2-3\beta_1-\alpha_3+\alpha_1\right]$

$ \begin{pmatrix} 1 & 2 & 1 \end{pmatrix} $

-2

$\alpha_1$

0 -1 0

$\beta_1-\alpha_1$

$\overline{\phantom{a}3}$

$ \begin{bmatrix} 0 & 0 & -1 & 1 \end{bmatrix} $

$ \begin{array}{c|c}\n\alpha_2 - \beta_1 - \alpha_1 \\
\beta_2 - \beta_1 - \alpha_2 + 2\alpha_1\n\end{array} = \begin{array}{|c|c|c|}\n0 & 0 & -1 & 1 \\
0 & 0 & 1 & -6\n\end{array} $

$\alpha_2$ - $\beta_1$ - $\alpha_1$

$ \begin{bmatrix} 0 & 0 & 0 \end{bmatrix} $

$\alpha_3+\alpha_2-3\alpha_1+\beta_1-\beta_2$

$5\overline{)}$

$\left[\beta_3+2\beta_2-3\beta_1-\alpha_3+\alpha_1\right]$

$\overline{0}$

$ \begin{pmatrix} 0 & 0 \end{pmatrix} $

-10

2 1 $-2<sup>-2</sup>$

$\alpha_1$

$ \begin{bmatrix} 0 & -1 & 0 & 3 \end{bmatrix} $

$\beta_1-\alpha_1$

$ \begin{array}{c|cc}\n\alpha_2 - \beta_1 - \alpha_1 \\
\beta_2 - 2\beta_1 + \alpha_1\n\end{array} = \begin{array}{|c|ccccc|} 0 & 0 & -1 & 1 \\
0 & 0 & 0 & -5 \end{array} $

$ \begin{bmatrix} 0 & 0 & -1 & 1 \end{bmatrix} $

$ \begin{array}{ccccccccc}\n & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & $

$\vert \alpha_3+\alpha_2-3\alpha_1+\beta_1-\beta_2\vert$

$ \begin{pmatrix} 0 & 0 \end{pmatrix} $

$\overline{0}$

$\left[\beta_3-\beta_1+\alpha_3+\alpha_1+2\alpha_2\right]$

$\overline{0}$

2 1 $-2<sup>\</sup>$

$\alpha_1$

$ \begin{bmatrix} 0 & -1 & 0 & 3 \end{bmatrix} $

$\beta_1-\alpha_1$

$ \begin{bmatrix} 0 & 0 & -1 & 1 \end{bmatrix} $

$ \begin{array}{c} \hline \end{array} $

$\alpha_2-\beta_1-\alpha_1$

$ \begin{bmatrix} 0 & 0 & 0 & -5 \end{bmatrix} $

$\beta_2-2\beta_1+\alpha_1$

$\overline{0}$

$\alpha_3+\alpha_2-2\alpha_1-\beta_1$

$ \begin{array}{c} \begin{array}{c} \end{array} $

$\overline{0}$

$\overline{0}$

$ \begin{vmatrix} \beta_3 - \beta_1 + \alpha_3 + \alpha_1 + 2\alpha_2 \end{vmatrix} (0 0 0 0) $

Do đó $rank(\alpha_1$, $\alpha_2$, $\alpha_3$, $\beta_1$, $\beta_2$, $\beta_3) =$ 4.

Vậy số chiều của A + B là 4 và một cơ sở của A + B là:

(1, 2, 1, -2), (0, -1, 0, 3), (0, 0, -1, 1), (0, 0, 0, -5)



  
Ta tìm A $\cap$ B. Một vector thuộc A $\cap$ B biểu thị tuyến tính được theo $\alpha_1$, $\alpha_2$, $\alpha_3$ và $\beta_1$, $\beta_2$, $\beta_3$.

Xét ràng buộc sau

$a_1\underbrace{(1,2,1,-2)}_{\alpha'_1}+a_2\underbrace{(0,-1,-1,4)}_{\alpha'_2}+a_3\underbrace{(0,0,1,-1)}_{\alpha'_3}=b_1\underbrace{(1,1,1,1)}_{\beta'_1}+b_2\underbrace{(0,-1,0,-2)}_{\beta'_2}+b_3\underbrace{(0,0,-1,-9)}_{\beta'_3}$

Giải ra ta được

$ \left\{ \begin{aligned} &a_1 = b_1 \\ &2a_1 - a_2 = b_1 - b_2 \\ &a_1 - a_2 + a_3 = b_1 - b_3 \\ &-2a_1 + 4a_2 - a_3 = b_1 - 2b_2 - 9b_3 \\ &\Longleftrightarrow \begin{cases} &a_1 = b_1 \\ &a_2 = b_1 + b_2 \\ &a_3 = b_1 + 6b_2 + 9b_3 \\ &a_3 = b_1 + 6b_2 + 9b_3 \end{cases} \end{aligned} \right. \Longleftrightarrow \left\{ \begin{aligned} &a_1 = b_1 \\ &a_2 = b_1 + b_2 \\ &a_3 = b_1 + b_ $

Như vậy,

$b_1\beta'_1$ + $b_2\beta'_2$ + $b_3\beta'_3 = b_1\beta'_1$ - $3b_3\beta'_2$ + $b_3\beta'_3$

$= b_1 \beta'_1$ + $b_3(-3\beta'_2$ + $\beta'_3)$

Một cơ sở của A $\cap$ B là $\beta'_1 =$ (1, 1, 1, 1), $-3\beta'_2$ + $\beta'_3 =$ (0, 3, -1, -3).

Bài tập 1.26. $\alpha_1 =$ (1, 1, 0, 0), $\alpha_2 =$ (0, 1, 1, 0), $\alpha_3 =$ (0, 0, 1, 1),

$\beta_1 =$ (1, 0, 1, 0), $\beta_2 =$ (0, 2, 1, 1), $\beta_3 =$ (1, 2, 1, 2).

Lời giải. A $= \text{span}(\alpha_1$, $\alpha_2$, $\alpha_3)$, B $= \text{span}(\beta_1$, $\beta_2$, $\beta_3)$.

Hệ $\alpha_1$, $\alpha_2$, $\alpha_3$ độc lập tuyến tính nên $rank(\alpha_1$, $\alpha_2$, $\alpha_3) =$ 3.

$ \begin{bmatrix} \beta_1 \\ \beta_2 \\ \beta_3 \end{bmatrix} = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 2 & 1 & 1 \\ 1 & 2 & 1 & 2 \end{pmatrix} \Longleftarrow \begin{bmatrix} \beta_1 \\ \beta_2 \\ \beta_3 - \beta_1 - \beta_2 \end{bmatrix} = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 2 & 1 & 1 \\ 0 & 0 & -1 & 1 \end{pmatrix} $



$<u>UITUUNU$ I. IMIUNU UIAN $VEULUIU</u>$

Như vậy, hệ $\beta_1$, $\beta_2$, $\beta_3$ độc lập tuyến tính nên $rank(\beta_1$, $\beta_2$, $\beta_3) =$ 3.

$ \begin{array}{c|c}\n\alpha_1 & \beta_1 \\
\beta_1 & \beta_2 \\
\beta_2 & \beta_3 \\
\alpha_3 & \beta_4 - \beta_2\n\end{array} $

$\alpha_1$

$ \begin{array}{|cccc|} \hline 1&0&1&0\\ 0&1&1&0\\ 0&2&1&1\\ \hline \end{array} $

$\beta_1$

$\alpha_2$

$\equiv$

0 $\quad$ 2 $\quad$ 1 $\quad$ 1

$\beta_1$

$ \begin{matrix} 0 & 0 & 1 & 1 \end{matrix} $

$0\quad 0\quad 1\quad$ 1

$\alpha_3$

2 $\quad$ 1 $\quad$ 2)

$|\beta_3-\beta_1-\beta_2|$

$\overline{0}$

$\lfloor\beta_3\rfloor$

$\overline{0}$

$ \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & -1 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 2 \end{pmatrix} \Longrightarrow \begin{pmatrix} \alpha_1 \\ \beta_1 - \alpha_1 \\ \alpha_2 - \alpha_1 + \beta_1 \\ \beta_2 - 2\alpha_2 \\ \alpha_3 + \beta_2 - 2\alpha_2 \\ \beta_3 + \alpha_3 - \beta_1 - \beta_2 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & 2 & 0 \\ 0 $

$\alpha_1$

$\beta_1-\alpha_1$

$\alpha_2$

$\beta_2-2\alpha_2$

$\alpha_3$

$\left[\,\beta_3+\alpha_3-\beta_1-\beta_2\,\right]$

1 $\quad$ 0 $\quad$ 0

$\overline{0}$

$\alpha_1$

$\alpha_1$

$ \implies \begin{bmatrix} \beta_1 - \alpha_1 \\ \alpha_2 - \alpha_1 + \beta_1 \\ 2\beta_2 - 3\alpha_2 - \alpha_1 + \beta_1 \\ \alpha_3 + \beta_2 - 2\alpha_2 \\ \beta_3 + \alpha_3 - \beta_1 - \beta_2 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 1 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & 2 \end{bmatrix} \implies \begin{bmatrix} \beta_1 - \alpha_1 \\ \alpha_2 - \alpha_1 + \beta_1 \\ 2 $

Một cơ sở của A + B là (1, 1, 0, 0), (0, -1, 1, 0), (0, 0, 2, 0), (0, 0, 0, 2).

Một vector của A $\cap$ B biểu thị tuyến tính được theo $\alpha_1$, $\alpha_2$, $\alpha_3$ và $\beta_1$, $\beta_2$, $\beta_3$. Xét ràng buộc

tuyến tính sau

$a_1(1,1,0,0)$ + $a_2(0,1,1,0)$ + $a_3(0,0,1,1) = b_1(1,0,1,0)$ + $b_2(0,2,1,1)$ + $b_3(0,0,-1,1)$

Giải ra ta được

$ \begin{cases}\na_1 = b_1 \\
a_1 + a_2 = 2b_2 \\
a_2 + a_3 = b_1 + b_2 - b_3\n\end{cases}\n\implies\n\begin{cases}\na_1 = b_1 \\
a_2 = 2b_2 - b_1 \\
a_3 = b_2 + b_3\n\end{cases}\n\implies\nb_1 - b_2 - b_3 = 0 $

$a_3 = b_2$ + $b_3$

$a_3 = 2b_1$ - $b_2$ - $b_3$

$\Rightarrow b_1(1,0,1,0)$ + $b_2(0,2,1,1)$ + $b_3(0,0,-1,1) = b_2(1,2,2,1)$ + $b_3(1,0,0,1)$

Một cơ sở của A $\cap$ B là (1, 2, 2, 1), (1, 0, 0, 1).

Bài tập 1.27. Chứng minh rằng với mọi không gian vector con $V_1$ của V, tồn tại một không gian



$<u>UITUUNU$ I. IMIUNU UIAN $TEUTUU</u>$

vector con $V_2$ của V sao cho V $= V_1 \oplus V_2$. Không gian $V_2$ có xác định duy nhất không?

Chứng minh. Giả sử $\alpha_1$, $\ldots$, $\alpha_n$ là một cơ sở của $V_1$.

Nếu $V_1 =$ V thì ta chọn $V_2 = \{0\}$. Như vậy, V $=$ V $\oplus V_2 = V_1 \oplus V_2$.

Nếu $V_1 \subsetneq$ V, ta có thể bổ sung vào hệ vector trên đến khi hệ độc lập tuyến tính cực đại.

Các vector được bổ sung vào hệ là $\beta_1$, $\ldots$, $\beta_m$.

Chọn $V_2 = \text{span}(\beta_1$, $\ldots$, $\beta_m)$ thì V $= V_1 \oplus V_2$.

Trong trường hợp $V_1 =$ V hoặc $V_1 = \{0\}$ thì $V_2$ là duy nhất.

Còn nếu $V_1 \subsetneq$ V thì $V_2$ không duy nhất. Chẳng hạn ta chọn:

$V_2 = \text{span}(\beta_1$, ..., $\beta_m) V_2 = \text{span}(\beta_1$ + $\alpha_1$, $\beta_2$, ..., $\beta_m)$

Bài tập 1.28. Chứng minh rằng không gian $\mathbb{C}_n$ là tổng trực tiếp của không gian vector con U

xác định bởi phương trình $x_1$ + $\cdots$ + $x_n =$ 0 và không gian vector con V xác định bởi phương trình

$x_1 = \cdots = x_n$. Tìm hình chiếu của các vector có cơ sở chính tắc của $\mathbb{C}_n$ lên U theo phương V và

lên V theo phương U.

Chúng minh. $(z_1$, $\ldots$, $z_n)$ là một vector của $\mathbb{C}_n$.

$(z_1$, ..., $z_n) = \left(z_1$ - $\frac{1}{n}\sum_{k=1}^n z_k$, ..., $z_n$ - $\frac{1}{n}\sum_{k=1}^n z_k\right)$ + $\frac{1}{n}\sum_{k=1}^n z_k$ (1, ..., 1)

$\in$ U

Mà U $\cap$ V $= \{(0$, $\ldots$, $0)\}\nên \mathbb{C}_n =$ U $\oplus$ V.

$\text{pr}_U((z_1,\ldots,z_n)) = \left(z_1$ - $\frac{1}{n}\sum_{k=1}^n z_k,\ldots,z_n$ - $\frac{1}{n}\sum_{k=1}^n z_k\right)$.

$pr_V((z_1,...,z_n)) = \left(\frac{1}{n}\sum_{i=1}^n z_k,...,\frac{1}{n}\sum_{i=1}^n z_k\right)$.

Bài tập 1.29. Cho F là một trường có đặc số khác 2. Chứng minh rằng không gian M(n $\times$ n, F)

các ma trận vuông cỡ n là tổng trực tiếp của không gian S(n) gồm các ma trận đối xứng và không

gian A(n) gồm các ma trận phản đối xứng. Tìm hình chiếu của ma trận C $\in$ M(n $\times$ n, $\mathbb{F})$ lên S(n)

theo phương A(n) và lên A(n) theo phương S(n).



$<u>UITUUNU$ I. IMIUNU UIAN $VEULUIU</u>$

Chứng minh. Theo bài tập 1.17 và 1.18, dim S(n) $= \frac{n(n+1)}{2}$, dim A(n) $= \frac{n(n-1)}{2}$.

$\dim$ S(n) + $\dim$ A(n) $= n^2 = \dim$ M(n $\times$ n, $\mathbb{F})$

Xét ma trận D $= (d_{ij})_{n \times n} \in$ S(n) $\cap$ A(n).

Vì D đối xứng và phản đối xứng nên

$ \left\{ \begin{aligned} d_{ii} &= 0 \ d_{ij} &= d_{ji} \ d_{ij} &= -d_{ii} \end{aligned} \right. \implies \left\{ \begin{aligned} d_{ii} &= 0 \ d_{ij} &= 0 \end{aligned} \right. $

Do đó, S(n) $\cap$ A(n) $= \{(0)_{n \times n}\}\$. Như vậy, M(n $\times$ n, $\mathbb{F}) =$ S(n) $\oplus$ A(n).

Xét ma trận vuông n hàng n cột P $= (p_{ij})_{n \times n}$.

$ \begin{pmatrix} p_{11} & p_{12} & \cdots & p_{1n} \ p_{21} & p_{22} & \cdots & p_{2n} \ \vdots & \vdots & \ddots & \vdots \ p_{n1} & p_{n2} & \cdots & p_{nn} \end{pmatrix} $

$ =\begin{pmatrix}\np_{11} & \frac{1}{2}(p_{12}+p_{21}) & \cdots & \frac{1}{2}(p_{1n}+p_{n1}) \\
\frac{1}{2}(p_{21}+p_{12}) & p_{22} & \cdots & \frac{1}{2}(p_{2n}+p_{n2}) \\
\vdots & \vdots & \ddots & \vdots \\
\frac{1}{2}(p_{n1}+p_{1n}) & \frac{1}{2}(p_{n2}+p_{2n}) & \cdots & p_{nn}\n\end{pmatrix} + \begin{pmatrix}\n0 & \frac{1}{2}(p_{12}-p_{21}) & \cdots & \frac{1}{2}(p_{1n}-p_{n1}) $

$\mathrm{pr}_{A(n)}$

$pr_{S(n)}$

Bài tập 1.30. Gọi $\mathbb{F}[X]_n$ là $\mathbb{F}-không$ gian vector các đa thức với hệ số $\mathbb{F}$ có bậc $\leq$ n. Tìm không

gian thương $\mathbb{F}[X]_n/\mathbb{F}[X]_m$ và số chiều của nó khi m $<$ n.

Chứng minh. 1, X, ..., $X^n$ là một cơ sở của $\mathbb{F}[X]_n$. Do đó, dim $\mathbb{F}[X]_n =$ n + 1.

1, X, $\ldots$, $X^m$ là một cơ sở của $\mathbb{F}[X]_m$.

f(X) $\sim$ g(X) $\Longleftrightarrow$ f(X) - g(X) $\in \mathbb{F}[X]_m$

Do đó, không gian thương $\mathbb{F}[X]_n/\mathbb{F}[X]_m$ là

$\{[a_{m+1}X^{m+1}+\cdots+a_{n}X^{n}]_{\sim}\mid a_{m+2},\ldots,a_{n}\in\mathbb{F}\}\$

$\dim \mathbb{F}[X]_n/\mathbb{F}[X]_m =$ (n+1) - (m+1) $=$ n-m.



# Chương 2

Ma trận và ánh xạ tuyến tính

Bài tập 2.1. Tính tích của hai ma trận sau đây:

$ \begin{pmatrix} 0 & 4 & 7 & 1 \\ 2 & 1 & 7 & 6 \\ 1 & 0 & 8 & 3 \\ 0 & 1 & 9 & 6 \end{pmatrix} \begin{pmatrix} -2 & 8 & -5 & 4 \\ 7 & 8 & 5 & 5 \\ 0 & 3 & 8 & 4 \\ -8 & 9 & -8 & 9 \end{pmatrix} $

Lời giải.

$ \begin{pmatrix} 20 & 62 & -68 & 57 \\ -45 & 99 & 3 & 95 \\ -26 & 59 & 35 & 63 \\ -41 & 89 & 29 & 95 \end{pmatrix}. $

$\Box$

Tính các lũy thừa sau đây

Bài tập 2.2.

$ \begin{pmatrix} \cos \varphi & -\sin \varphi \\ \sin \varphi & \cos \varphi \end{pmatrix}^n, \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}^n. $

Lời giải.

$ A = \begin{pmatrix} \cos \varphi & -\sin \varphi \\ \sin \varphi & \cos \varphi \end{pmatrix} $

Ta sẽ chứng minh bằng quy nạp rằng:

$ A^n = \begin{pmatrix} \cos(n\varphi) & -\sin(n\varphi) \\ \sin(n\varphi) & \cos(n\varphi) \end{pmatrix} $

$(\ast)$



VIIUVINU 2. INA TIUAIN VA AINII AA TUTEN TIINII

$<sup>(*)</sup>$ đúng với n $=$ 1, giả sử (*) cũng đúng với n $=$ k.

$ A^{k+1} = \begin{pmatrix} \cos(k\varphi) & -\sin(k\varphi) \\ \sin(k\varphi) & \cos(k\varphi) \end{pmatrix} \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix} $

$ = \begin{pmatrix} \cos(k\varphi)\cos\varphi - \sin(k\varphi)\sin\varphi & -\sin(k\varphi)\cos\varphi - \cos(k\varphi)\sin\varphi \\ \sin(k\varphi)\cos\varphi + \cos(k\varphi)\sin\varphi & \cos(k\varphi)\cos\varphi - \sin(k\varphi)\sin\varphi \end{pmatrix} $

$ = \begin{pmatrix} \cos((k+1)\varphi) & -\sin((k+1)\varphi) \\ \sin((k+1)\varphi) & \cos((k+1)\varphi) \end{pmatrix} $

Vậy (*) vẫn đúng với n $=$ k + 1. Theo nguyên lý quy nạp toán học, (*) đúng với mọi n $\in \mathbb{N}$.

$ B = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix} $

Ta sẽ chứng minh bằng quy nạp rằng:

$ B^n = \left(\begin{matrix} \lambda^n & n\lambda^{n-1} \\ 0 & \lambda^n \end{matrix}\right). $

(**)

$<sup>(**)</sup>$ đúng với n $=$ 1, giả sử (**) cũng đúng với n $=$ k.

$ A^{k+1} = \begin{pmatrix} \lambda^k & k\lambda^{k-1} \\ 0 & \lambda^k \end{pmatrix} \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix} = \begin{pmatrix} \lambda^{k+1} & (k+1)\lambda^k \\ 0 & \lambda^{k+1} \end{pmatrix}. $

Vậy (**) vẫn đúng với n $=$ k + 1. Theo nguyên lý quy nạp, (**) đúng với mọi n $\in \mathbb{N}$.

$\Box$

Bài tập 2.3.

$ \begin{pmatrix} a_1 & 0 & \cdots & 0 \\ 0 & a_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & a_n \end{pmatrix}^n $

Lời giải. Từ định nghĩa tích ma trận, ta có đẳng thức sau:

$ \begin{pmatrix} x_1 & 0 & \cdots & 0 \\ 0 & x_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & x_n \end{pmatrix} \begin{pmatrix} y_1 & 0 & \cdots & 0 \\ 0 & y_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & y_n \end{pmatrix} = \begin{pmatrix} x_1y_1 & 0 & \cdots & 0 \\ 0 & x_2y_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & x_ny_n \end{pmatrix} $



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Ap dụng vào bài toán, ta được:

$ \begin{pmatrix} a_1 & 0 & \cdots & 0 \\ 0 & a_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & a_n \end{pmatrix}^k = \begin{pmatrix} a_1^k & 0 & \cdots & 0 \\ 0 & a_2^k & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & a_n^k \end{pmatrix} $

Bài tập 2.4. Ma trận sau đây có n hàng, n cột.

$ \begin{pmatrix} 1 & 1 & 0 & 0 & \cdots & 0 & 0 \\ 0 & 1 & 1 & 0 & \cdots & 0 & 0 \\ 0 & 0 & 1 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & 1 & 1 \end{pmatrix}^{n-1} $

$ \begin{pmatrix} 0 & 0 & 0 & \cdots & 0 & 1 \end{pmatrix} $

Lời giải.

$ A = \begin{pmatrix} 1 & 1 & 0 & 0 & \cdots & 0 & 0 \\ 0 & 1 & 1 & 0 & \cdots & 0 & 0 \\ 0 & 0 & 1 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & 1 & 1 \\ 0 & 0 & 0 & 0 & \cdots & 0 & 1 \end{pmatrix} $

Ma trận A được viết lại như sau:

$ A = \left( \begin{matrix} \binom{1}{0} & \binom{1}{1} & 0 & 0 & \cdots & 0 & 0 \\ 0 & \binom{1}{0} & \binom{1}{1} & 0 & \cdots & 0 & 0 \\ 0 & 0 & \binom{1}{0} & \binom{1}{1} & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & \ddots & \binom{1}{0} & \binom{1}{1} \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & \bin $

$ \begin{pmatrix} 0 & 0 & 0 & 0 & \cdots & 0 & \binom{1}{0} \end{pmatrix} $



UHUURU 2. MA HUAR VA ARII AA TUTER HINII

Sử dụng quy tắc nhân ma trận và đẳng thức Pascal, ta được:

$ A^2 = \begin{pmatrix} \begin{pmatrix} 2 \\ 0 \end{pmatrix} & \begin{pmatrix} 2 \\ 1 \end{pmatrix} & \begin{pmatrix} 2 \\ 2 \end{pmatrix} & 0 & \cdots & 0 & 0 \\ 0 & \begin{pmatrix} 2 \\ 0 \end{pmatrix} & \begin{pmatrix} 2 \\ 1 \end{pmatrix} & \begin{pmatrix} 2 \\ 2 \end{pmatrix} & \cdots & 0 & 0 \\ 0 & 0 & \begin{pmatrix} 2 \\ 0 \end{pmatrix} & \begin{pmatrix} 2 \\ 1 \end{pmatrix} & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ $

Nhân liên tiếp với A, đến cuối cùng ta được:

$ A^{n-1}=\begin{pmatrix} \begin{pmatrix}n-1\\0\end{pmatrix}&\begin{pmatrix}n-1\\1\end{pmatrix}&\begin{pmatrix}n-1\\2\end{pmatrix}&\begin{pmatrix}n-1\\3\end{pmatrix}&\cdots&\begin{pmatrix}n-1\\n-2\end{pmatrix}&\begin{pmatrix}n-1\\n-1\end{pmatrix}\\ 0&\begin{pmatrix}n-1\\0\end{pmatrix}&\begin{pmatrix}n-1\\1\end{pmatrix}&\begin{pmatrix}n-1\\2\end{pmatrix}&\cdots&\begin{pmatrix}n-1\\n-3\end{pmatrix}&\begin{pmatrix}n-1\\n-2\end{pmatrix}\\ 0 $

Bài tập 2.5. Cho hai ma trận A và B với các yếu tố trong F. Chứng minh rằng nếu các tích AB

và BA đều có nghĩa và AB $=$ BA, thì A và B là các ma trận vuông cùng cõ.

Chứng minh. Tích AB và BA có nghĩa, tức là số cột của A bằng số hàng của B và số cột của B

$b\tilde{a}ng$ số hàng của A.

Vậy nếu A $\in$ M(m $\times$ n, $\mathbb{F})$ thì B $\in$ M(n $\times$ m, $\mathbb{F})$.

Suy ra AB $\in$ M(m $\times$ m, $\mathbb{F})$, BA $\in$ M(n $\times$ n, $\mathbb{F})$.

Mà AB $=$ BA nên m $=$ n.

Do đó A và B là hai ma trận vuông cùng cõ.

Bài tập 2.6. Ma trận tích AB sẽ thay đổi thế nào nếu ta

(a) đổi chỗ các hàng thứ i và thứ j của ma trận A?

(b) cộng vào hàng thứ i của A tích của vô hướng c với hàng thứ j của A?

(c) đổi chỗ các cột thứ i và thứ j của ma trận B.

(d) cộng vào cột thứ i của B tích của vô hướng c với cột thứ j của B?

(a) Hàng thứ i và thứ j của ma trận tích đổi chỗ.

$L\delta$ i giải.

(b) Hàng thứ i của AB được cộng thêm tích của vô hướng c với hàng thứ j của AB.



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Cột thứ i và thứ j của ma trận tích đổi chỗ.

(c)

(d) Cột thứ i của AB được cộng thêm tích của vô hướng c với cột thứ j của AB.

$\Box$

Bài tập 2.7. Vết của một ma trận vuông là tổng của tất cả các yếu tố nằm trên đường chéo

chính của ma trận đó. Chứng minh rằng vết của AB bằng vết của BA.

Chứng minh. Tích AB và BA có nghĩa, vậy là số cột của A bằng số hàng của B, số cột của B

$b\tilde{a}ng$ số hàng của A.

Giả sử A $\in$ M(m $\times$ n, $\mathbb{F})$. Khi đó, B $\in$ M(n $\times$ m, $\mathbb{F})$. Ta đặt

$ A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix} \quad B = \begin{pmatrix} b_{11} & b_{12} & \cdots & b_{1m} \\ b_{21} & b_{22} & \cdots & b_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ b_{n1} & b_{n2} & \cdots & b_{nm} \end{pmatrix} $

Kí hiệu $(AB)_{ij}$ là yếu tố hàng i, cột j của AB. Kí hiệu tr(X) là vết của ma trận X.

tr(AB) $= \sum_{i=1}^{m} (AB)_{ii} = \sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij}b_{ji}$.

tr(BA) $= \sum_{i=1}^{n} (BA)_{ii} = \sum_{i=1}^{n} \sum_{j=1}^{m} b_{ij} a_{ji}$.

Đổi thứ tự lấy tổng, ta được:

$\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} b_{ji} = \sum_{i=1}^{n} \sum_{j=1}^{m} b_{ij} a_{ji}$.

$i=1 i=1 \overline{i=1} \overline{i=1}$

Do đó, tr(AB) $=$ tr(BA).

Bài tập 2.8. Chứng minh rằng nếu A và B là các ma trận vuông cùng cấp, với AB $\neq$ BA, thì

(a) (A + $B)^2 \neq A^2$ + 2AB + $B^2$,

(b) (A + B)(A - B) $\neq A^2$ - $B^2$.



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Chúng minh.

(a)

(A + $B)^2 =$ (A + B)(A + B)

$= A^{2}$ + AB + BA + $B^{2}$

$\neq A^2$ + AB + AB + $B^2$

$= A^2$ + 2AB + $B^2$

(b)

(A + B)(A - B) $= A^{2}$ - AB + BA - $B^{2}$

$= A^{2}$ - $B^{2}$ + (BA - AB)

$\neq A^2$ - $B^2$

Bài tập 2.9. Chứng minh rằng nếu A và B là các ma trận vuông với AB $=$ BA thì

(A + $B)^n = A^n$ + $nA^{n-1}B$ + $\frac{n(n-1)}{2}A^{n-2}B^2$ + $\cdots$ + $B^n$.

$(\ast)$

Chứng minh. Ta chứng minh bằng quy nạp theo n.

(*) đúng với n $=$ 1. Giả sử (*) đúng với n $=$ k.

$(A+B)^k = \sum_{j=0}^k {k \choose j} A^{k-j} B^j$

$\implies$ (A + $B)^{k+1} = \sum_{i=0}^{k} {k \choose i} A^{k+1-j} B^j$ + $\sum_{i=0}^{k} {k \choose i} A^{k-j} B^{j+1}$

Sử dụng đẳng thức Pascal $\binom{n}{k} = \binom{n-1}{k}$ + $\binom{n-1}{k-1}$, ta suy ra

(A + $B)^{k+1} = A^{k+1}$ + $\sum_{i=1}^{k+1} {k+1 \choose j} A^{k+1-j} B^j = \sum_{i=0}^{k+1} {k+1 \choose j} A^{k+1-j} B^j$.

Vậy (*) đúng với n $=$ k + 1. Do đó (*) đúng với mọi số tự nhiên n.

Bài tập 2.10. Hai ma trận vuông A và B được gọi là giao hoán với nhau nếu AB $=$ BA. Chứng

minh rằng A giao hoán với mọi ma trận vuông cùng cỡ với nó nếu và chỉ nếu nó là một ma trận

vô hướng, tức là A $=$ cE trong đó c $\in \mathbb{F}$ và E là ma trận đơn vị cùng cỡ với A.



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Chứng minh. Vì ma trận đơn vị giao hoán với mọi ma trận vuông cùng cỡ nên mỗi ma trận vô

hướng cũng giao hoán với mọi ma trận vuông cùng cỡ.

Ta sẽ chứng minh điều ngược lại: Nếu một ma trận vuông giao hoán với mọi ma trận vuông

cùng cỡ thì đó là một ma trận vô hướng.

Giả sử A $= (a_{ij})_{n \times n}$ là một ma trận giao hoán với mọi ma trận vuông cùng cõ. Xét các ma

trận vuông $E_{k,\ell}$ cỡ n sao cho k $\neq \ell$ và các yếu tố trên đường chéo chính bằng 1, yếu tố thuộc hàng

k cột $\ell$ bằng 1, các yếu tố còn lại bằng 0. Thực hiện phép nhân $AE_{k,\ell}$, $E_{k,\ell}A$, ta thu được hai ma

trận với đặc điểm sau (hãy dùng một ma trận cụ thể để dễ hình dung)

• Cột $\ell$ của $AE_{k,\ell}$ là tổng của cột k và cột $\ell$ của ma trận A.

• Hàng k của $E_{k,\ell}A$ là tổng của hàng k và hàng $\ell$ của ma trận A.

Vì A giao hoán với $E_{k,\ell}$ nên hai ma trận trên bằng nhau. Đồng nhất các yếu tố ở hàng $k,\ell$ và

cột k, $\ell$ ở hai ma trận, ta thu được $a_{k,\ell} = a_{\ell,k} =$ 0 và $a_{k,k} = a_{\ell,\ell}$.

Do đó A là một ma trận vô hướng.

Bài tập 2.11. Ma trận vuông A được gọi là ma trận chéo nếu các yếu tố nằm ngoài đường chéo

chính của nó đều bằng không. Chứng minh rằng ma trận vuông A giao hoán với mọi ma trận chéo

cùng cỡ với nó nếu và chỉ nếu chính A là một ma trận chéo.

Chúng minh. $(\Rightarrow)$ A và B là các ma trận chéo.

$ \begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ 0 & a_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \vdots & a_{nn} \end{pmatrix} \begin{pmatrix} b_{11} & 0 & \cdots & 0 \\ 0 & b_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & b_{nn} \end{pmatrix} = \begin{pmatrix} a_{11}b_{11} & 0 & \cdots & 0 \\ 0 & a_{22}b_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \ $

$ \begin{pmatrix} b_{11} & 0 & \cdots & 0 \\ 0 & b_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \vdots & b_{nn} \end{pmatrix} \begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ 0 & a_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & a_{nn} \end{pmatrix} = \begin{pmatrix} a_{11}b_{11} & 0 & \cdots & 0 \\ 0 & a_{22}b_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \ $

Như vậy, A giao hoán với mọi ma trận chéo cùng cỡ.

$(\Leftarrow)$ A giao hoán với mọi ma trận chéo cùng cỡ.

A $= (a_{ij})_{n \times n}$. $E_i$ là ma trận vuông cỡ n với yếu tố hàng i cột i bằng đơn vị và các yếu tố còn



UHUURU 2. MA HIGIN VA AINII AA TUTEN TIINII

lại bằng không. $E_i$ là ma trận chéo.

$ AE_i = \begin{pmatrix} 0 & \cdots & a_{1i} & \cdots & 0 \\ \vdots & \ddots & \vdots & \ddots & \vdots \\ 0 & \cdots & a_{ii} & \cdots & 0 \\ \vdots & \ddots & \vdots & \ddots & \vdots \\ 0 & \cdots & a_{ni} & \cdots & 0 \end{pmatrix} $

$ E_i A = \left( \begin{array}{cccccc} 0 & \cdots & 0 & \cdots & 0 \ \vdots & \ddots & \vdots & \ddots & \vdots \ a_{i1} & \cdots & a_{ii} & \cdots & a_{in} \ \vdots & \ddots & \vdots & \ddots & \vdots \ 0 & \cdots & 0 & \cdots & 0 \end{array} \right) $

Do $AE_i = E_i$ A nên $a_{ij} = a_{ji} =$ 0, $\forall$ j $\neq$ i.

Như vậy, A là một ma trận chéo.

Bài tập 2.12. Chứng minh rằng nếu A là một ma trận chéo với các yếu tố trên đường chéo chính

đôi một khác nhau, thì mọi ma trận giao hoán với A cũng là một ma trận chéo.

Chúng minh.

$ A = \begin{pmatrix} a_1 & 0 & \cdots & 0 \\ 0 & a_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \vdots & \ddots \end{pmatrix} $

trong đó, $a_i \neq a_j$, $\forall$ i $\neq$ j. B $= (b_{ij})_{n \times n}$.

$ AB = \begin{pmatrix} a_1b_{11} & a_1b_{12} & \cdots & a_1b_{1n} \\ a_2b_{21} & a_2b_{22} & \cdots & a_2b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_nb_{n1} & a_nb_{n2} & \cdots & a_nb_{nn} \end{pmatrix} \qquad BA = \begin{pmatrix} a_1b_{11} & a_2b_{12} & \cdots & a_nb_{1n} \\ a_1b_{21} & a_2b_{22} & \cdots & a_nb_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_1b_{n1} & a_2b_{n2} & \cd $

AB $=$ BA thì $a_i b_{ij} = a_j b_{ij}$, $\forall$ i $\neq$ j. Vì $a_i \neq a_j$ nên $b_{ij} =$ 0, $\forall$ i $\neq$ j.

Vậy B là một ma trận chéo. Tức là mọi ma trận giao hoán với A cũng là ma trận chéo.

Bài tập 2.13. Gọi D $= diag(a_1$, $a_2$, $\ldots$, $a_n)$ là ma trận chéo với các yếu tố trên đường chéo chính

lần lượt bằng $a_1$, $a_2$, $\ldots$, $a_n$. Chứng minh rằng nhân D với A từ bên trái có nghĩa là nhân các hàng

của A theo thứ tự với $a_1$, $a_2$, $\ldots$, $a_n;$ còn nhân D với A từ bên phải có nghĩa là nhân với các cột

của A theo thứ tự với $a_1$, $a_2$, $\ldots$, $a_n$.



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Chứng minh. $A=(a_{ij})_{n\times n}$.

$ DA = \begin{pmatrix} a_1 & 0 & \cdots & 0 \\ 0 & a_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & a_n \end{pmatrix} \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix} = \begin{pmatrix} a_1a_{11} & a_1a_{12} & \cdots & a_1a_{1n} \\ a_2a_{21} & a_2a_{22} & \cd $

$ AD = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix} \begin{pmatrix} a_1 & 0 & \cdots & 0 \\ 0 & a_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & a_n \end{pmatrix} = \begin{pmatrix} a_1a_{11} & a_2a_{12} & \cdots & a_na_{1n} \\ a_1a_{21} & a_2a_{22} & \cdots & $

Bài tập 2.14. Tìm tất cả các ma trận giao hoán với ma trận sau đây:

$ \begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{pmatrix} $

Lời giải. Đặt ma trận cần tìm là A $= (a_{ij})_{n \times n}$.

$ \begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{pmatrix} \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} = \begin{pmatrix} 3a_{11} + a_{21} & 3a_{12} + a_{22} & 3a_{13} + a_{23} \\ 3a_{21} + a_{31} & 3a_{22} + a_{32} & 3a_{23} + a_{33} \\ 3a_{31} & 3a_{32} & 3a_{33} \end{ $

$ \begin{pmatrix} a_{11} & a_{12} & a_{13} \ a_{21} & a_{22} & a_{23} \ a_{31} & a_{32} & a_{33} \end{pmatrix} \begin{pmatrix} 3 & 1 & 0 \ 0 & 3 & 1 \ 0 & 0 & 3 \end{pmatrix} = \begin{pmatrix} 3a_{11} & a_{11} + 3a_{12} & a_{12} + 3a_{13} \ 3a_{21} & a_{21} + 3a_{22} & a_{22} + 3a_{23} \ 3a_{31} & a_{31} + 3a_{32} & a_{32} + 3a_{33} \end{ $



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Đồng nhất hệ số hai ma trận tích:

$ \left\{\n\begin{aligned}\n3a_{11} + a_{21} &= 3a_{11} \Leftrightarrow a_{21} = 0 \\
3a_{12} + a_{22} &= a_{11} + 3a_{12} \Leftrightarrow a_{11} = a_{22} \\
3a_{13} + a_{23} &= a_{12} + 3a_{13} \Leftrightarrow a_{12} = a_{23} \\
3a_{21} + a_{31} &= 3a_{21} \Leftrightarrow a_{31} = 0 \\
3a_{22} + a_{32} &= a_{21} + 3a_{22} \Leftrightarrow a_{21} = a_{32} \\
3a_{23} + a_{33} $

$ Vậy các ma trận giao hoán với ma trận\begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{pmatrix} có dạng $

$ \begin{pmatrix} a & b & c \ 0 & a & b \ 0 & 0 & a \end{pmatrix}. $

$ Bài tập 2.15. Chứng minh rằng ma trận A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} thỏa mãn phương trình $

$X^2$ - (a+d)X + (ad-bc) $=$ 0

Chúng minh.

$ A^{2} = \begin{pmatrix} a^{2} + bc & b(a+d) \\ c(a+d) & d^{2} + bc \end{pmatrix} $

$ A^{2} - (a+d)A + (ad - bc) = \begin{pmatrix} a^{2} + bc & b(a+d) \\ c(a+d) & d^{2} + bc \end{pmatrix} - (a+d) \begin{pmatrix} a & b \\ c & d \end{pmatrix} + (ad - bc) \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} $

$ =\begin{pmatrix} a^2 + bc - a(a + d) + (ad - bc) & b(a + d) - b(a + d) \\ c(a + d) - c(a + d) & d^2 + bc - d(a + d) + (ad - bc) \end{pmatrix} $

$ =\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = 0. $



VIIUVINU 2. INA TIUAIN VA AINII AA TUTEN TIINII

Bài tập 2.16. Chứng minh rằng đối với mỗi ma trận vuông A, tồn tại một đa thức khác không

f(X) sao cho f(A) $=$ 0. Hơn nữa, mọi đa thức có tính chất đó đều là bội của một đa thức $f_0(X)$

như thế.

Chúng minh. Giả sử A $\in$ M(n $\times$ n, $\mathbb{F})$.

M(n $\times$ n, $\mathbb{F})$ là một không gian vector với số chiều là $n^2$.

Do đó hệ $(E_n$, A, $A^2$, $\ldots$, $A^{n^2})$ phụ thuộc tuyến tính, tức là tồn tại các yếu tố $a_0$, $a_1$, $a_2$, $\ldots$, $a_{n^2}$

trong trường $\mathbb{F}$, không đồng thời bằng không sao cho:

$a_0$ + $a_1$ A + $a_2 A^2$ + $\cdots$ + $a_{n2} A^{n^2} =$ 0

Diều đó có nghĩa là đa thức f(X) $= a_0$ + $a_1X$ + $a_2X^2$ + $\cdots$ + $a_nX^{n^2}$ khác không và thỏa mãn

f(A) $=$ 0.

Như vậy tập hợp các đa thức khác không nhận A làm nghiệm là tập khác rồng. Theo nguyên

lý sắp thứ tự tốt, tập hợp này chứa đa thức có bậc nhỏ nhất. Đặt đa thức như vậy là $f_0(X)$.

Giả sử đa thức p(X) thỏa mãn p(A) $=$ 0. Ta thực hiện phép chia cho đa thức $f_0(X)$.

p(X) $= f_0(X)q(X)$ + r(X)

trong đó deg r(X) $<$ deg $f_0(X)$. p(A) $=$ 0 $\Rightarrow f_0(A)q(A)$ + r(A) $=$ 0 $\Rightarrow$ r(A) $=$ 0. Da thức r(X)

có bậc bé hơn $f_0(X)$, do đó r(X) $=$ 0. Vậy p(X) là bội của $f_0(X)$.

Bài tập 2.17. Giả sử n không chia hết cho đặc số p của trường $\mathbb{F}$. Chứng minh rằng không tồn

tại các ma trận A, B $\in$ M(n $\times$ n, $\mathbb{F})$ sao cho AB - BA $= E_n$.

Chứng minh. Ánh xạ vết tr : M(n $\times$ n, $\mathbb{F}) \to \mathbb{F}$ là một ánh xạ tuyến tính.

Theo Bài 2.7, tr(AB - BA) $=$ tr(AB) - tr(BA) $=$ 0.

Mà $tr(E_n) =$ n và n không là bội của đặc số của trường $\mathbb$ F nên n $\neq$ 0. Do đó tr(AB - BA) $\neq$ 0

$tr(E_n)$.

Diều đó cũng có nghĩa là AB - BA $\neq E_n$.

Bài tập 2.18. Giả sử A là một ma trận vuông cỡ 2 và k là một số nguyên $\geq$ 2. Chứng minh rằng

$A^k=0$ nếu và chỉ nếu $A^2=0$.

Chứng minh. Trong chứng minh này, chúng ta dùng kết quả sau: v là vector trong không gian

vector V trên trường $\mathbb$ F và a $\in \mathbb$ F thì av $=$ 0 $\iff$ a $=$ 0 $\lor$ v $=$ 0 (áp dụng cho không gian vector

$M(2\times 2,\mathbb{F}))$.

$ Dặt A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}. $



VIIUVINU 2. INA TIUAIN VA AINII AA TUTEN TIINII

$(\Rightarrow) A^2 =$ 0 thì $A^k =$ 0 với mọi k $\geq$ 2.

$(\Leftarrow) A^k =$ 0 với k là số nguyên nào đó $\geq$ 2.

Nếu k $=$ 2, ta có ngay điều phải chứng minh.

Nếu k $>$ 2. Theo Bài 2.15

$A^2$ - (a+d)A + (ad-bc) $=$ 0

$(\text{*})$

Xét hai trường hợp sau.

Trường hợp 1. ad - bc $=$ 0

thì $A^2$ - (a + d)A $=$ 0. Nhân hai vế của (*) với $A^{k-2}$, cùng với việc $A^k =$ 0, ta thu được

$(a+d)A^{k-1}=0$.

Nếu a + d $\neq$ 0 thì $A^{k-1} =$ 0. Bằng lập luận tương tự, chúng ta chứng minh được mệnh đề

$A^{\ell} =$ 0 $\implies A^{\ell-1} =$ 0 với mọi $\ell \geq$ 2. Kết hợp với $A^{k} =$ 0 (k $>$ 2), ta được $A^{2} =$ 0.

Nếu a + d $=$ 0, thay vào đẳng thức (*), ta có ngay $A^2 =$ 0.

Trường hợp 2. ad - bc $\neq$ 0

$A^k =$ 0 thì $A^{k+1} =$ 0. Nhân hai vế của (*) với $A^{k-1}$, ta suy ra $(ad-bc)A^{k-1} =$ 0. Vì ad-bc $\neq$ 0

nên $A^{k-1} =$ 0.

Bằng lập luận tương tự, chúng ta chứng minh được mệnh đề $A^{\ell} =$ 0 $\implies A^{\ell-1} =$ 0. Mà

$A^k =$ 0 nên ta thu được $A^2 =$ A $=$ 0. Thay vào (*), chúng ta thu được ad - bc $=$ 0, mâu

thuẫn. Vậy trường hợp này không xảy ra.

Tóm lại, trong tất cả các trường hợp, ta đều có $A^2 =$ 0.

Bài tập 2.19. Tìm tất cả các ma trận vuông A cỡ 2 sao cho $A^2 =$ 0.

$ Lời giải. A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies A^2 = \begin{pmatrix} a^2 + bc & b(a+d) \\ c(a+d) & d^2 + bc \end{pmatrix}. $

$ A^2 = 0 \implies \begin{cases} a^2 + bc = 0 \\ d^2 + bc = 0 \\ b(a + d) = 0 \end{cases} $

b(a + d) $=$ 0c(a + d) $=$ 0

Trường hợp 1: a + d $\neq$ 0.

b(a+d) $=$ c(a+d) $=$ 0 và a+d $\neq$ 0 nên $b=c=0$.

$a^{2}$ + bc $= d^{2}$ + bc $=$ b $=$ c $=$ 0 nên a $=$ b $=$ c $=$ d $=$ 0.



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Trường hợp 2: a + d $=$ 0.

$ Nếu a = d = 0 thì bc = 0. A = \begin{pmatrix} 0 & t \\ 0 & 0 \end{pmatrix} hoặc A = \begin{pmatrix} 0 & 0 \\ t & 0 \end{pmatrix}. $

$ Nếu a, d \neq 0 thì A = \begin{pmatrix} t & u \\ \frac{-t^2}{u} & -t \end{pmatrix} trong đó t \neq 0. $

Như vậy A thuộc một trong các dạng sau:

$ \begin{pmatrix} 0 & t \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 0 \\ t & 0 \end{pmatrix} \begin{pmatrix} t & u \\ \frac{-t^2}{\cdot} & -t \end{pmatrix} $

$\Box$

Bài tập 2.20. Tìm tất cả các ma trận vuông A cỡ 2 sao cho $A^2 = E_2$.

$ Lời giải. A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies A^2 = \begin{pmatrix} a^2 + bc & b(a+d) \\ c(a+d) & d^2 + bc \end{pmatrix}. $

Trường hợp 1: a + d $\neq$ 0.

Suy ra b $=$ c $=$ 0, $a^2 = d^2 =$ 1.

(a, d) $\in \{(1$, 1), (-1, -1), (1, -1), (-1, $1)\}$.

Trường hợp 2: a + d $=$ 0.

a $=$ t, d $=$ -t, suy ra bc $=$ 1 - $t^2$.

Nếu $t^2 =$ 1 thì bc $=$ 0.

Nếu $t^2 \neq$ 1 thì b $=$ u, c $= \frac{1-t^2}{u}$.

Như vậy A thuộc một trong các dạng sau:

$ \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ t & -1 \end{pmatrix} \begin{pmatrix} 1 & t \\ 0 & -1 \end{pmatrix} \begin{pmatrix} -1 & 0 \\ t & 1 \end{pmatrix} \begin{pmatrix} -1 & t \\ 0 & 1 \end{pmatrix} $

$ \begin{pmatrix} t & u \\ \frac{1-t^2}{u} & -t \end{pmatrix} (t \neq \pm 1) $

Bài tập 2.21. Giải phương trình AX $=$ 0, trong đó A là ma trận vuông cỡ 2 đã cho còn X là ma

trận vuông cỡ 2 cần tìm.



UIIUUIVU 2. INIA TIUAIV VA AIVII AA TUTEN TIIVII

$ Lời giải. A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}; X = \begin{pmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{pmatrix}. $

$ AX = \begin{pmatrix} ax_{11} + bx_{21} & ax_{12} + bx_{22} \\ cx_{11} + dx_{21} & cx_{12} + dx_{22} \end{pmatrix} $

Trường hợp 1: a $=$ b $=$ c $=$ d $=$ 0.

Mọi ma trận vuông cỡ 2 đều thỏa mãn.

Trường hợp 2: a $=$ b $=$ c $=$ 0, d $\neq$ 0.

$x_{21} = x_{22} =$ 0.

Trường hợp 3: a $=$ b $=$ d $=$ 0, c $\neq$ 0.

$x_{11} = x_{12} =$ 0.

Trường hợp 4: a $=$ c $=$ d $=$ 0, b $\neq$ 0.

$x_{21} = x_{22} =$ 0.

Trường hợp 5: b $=$ c $=$ d $=$ 0, a $\neq$ 0.

$x_{11} = x_{12} =$ 0.

Trường hợp 6: a $=$ b $=$ 0; c, d $\neq$ 0.

$x_{11} =$ dp, $x_{21} =$ -cp, $x_{12} =$ dq, $x_{22} =$ -cq.

Trường hợp 7: a, b $\neq$ 0; c $=$ d $=$ 0.

$x_{11} =$ bp, $x_{21} =$ -ap, $x_{12} =$ bq, $x_{22} =$ -aq.

Trường hợp 8: a $=$ c $=$ 0; b, d $\neq$ 0.

$x_{21} = x_{22} =$ 0.

Trường hợp 9: a, c $\neq$ 0; b $=$ d $=$ 0.

$x_{11} = x_{12} =$ 0.

Trường hợp 10: a $=$ d $=$ 0; b, c $\neq$ 0.

$x_{21} = x_{22} = x_{11} = x_{12} =$ 0.

Trường hợp 11: a, d $\neq$ 0; b $=$ c $=$ 0.

$x_{11} = x_{12} = x_{21} = x_{22} =$ 0.



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Trường hợp 12: a $=$ 0 $\vee$ b $=$ 0 $\vee$ c $=$ 0 $\vee$ d $=$ 0.

$x_{11} = x_{12} = x_{21} = x_{22} =$ 0.

Trường hợp 13: a, b, c, d $\neq$ 0.

Nếu ad - bc $=$ 0 thì $x_{11} =$ bp, $x_{21} =$ -ap, $x_{12} =$ bq, $x_{22} =$ -aq.

Nếu ad - bc $\neq$ 0 thì $x_{11} = x_{12} = x_{21} = x_{22} =$ 0.

Bài tập 2.22. Tìm ma trận nghịch đảo (nếu có) của ma trận

$ A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} $

Chúng minh. Theo Bài 2.15:

$A^2$ - (a+d)A + (ad-bc) $=$ 0

Trường hợp 1: ad - bc $=$ 0.

Giả sử A khả nghịch.

$A^{-1}(A^{2}$ - (a+d)A) $=$ 0 $\Rightarrow$ A $=$ (a+d)E

Đồng nhất hệ số của A và (a+d)E, ta suy ra a $=$ b $=$ c $=$ d $=$ 0. Ma trận này không khả

nghịch.

Vậy khi ad - bc $=$ 0 thì A không khả nghịch.

Trường hợp 2: ad - bc $\neq$ 0

$ Chọn B = \frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}, ta được AB = BA = E_2. $

Như vậy, khi ad - bc $=$ 0, ma trận A không khả nghịch. Khi ad - bc $\neq$ 0, A khả nghịch và

$ A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} $

Bài tập 2.23. Giả sử V $= V_1 \oplus V_2$, trong đó $V_1$ có cơ sở $(\alpha_1$, $\ldots$, $\alpha_k)$, $V_2$ có cơ sở $(\alpha_{k+1}$, $\ldots$, $\alpha_n)$.

Tìm ma trận của phép chiếu lên $V_1$ theo phương $V_2$ đối với cơ sở $(\alpha_1$, $\ldots$, $\alpha_n)$.



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Lời giải. $\text{pr}_{V_1}$ là phép chiếu lên $V_1$ theo phương $V_2$.

$ pr_{V_1}(\alpha_i) = \begin{cases} \alpha_i (i = \overline{1,k}) \\ 0 (i = \overline{k+1,n}) \end{cases} $

Vậy ma trận của $pr<sub>V<sub>1</sub></sub>$ đối với cơ sở $(\alpha_1$, $\ldots$, $\alpha_n)$ của V và cơ sở $(\alpha_1$, $\ldots$, $\alpha_k)$ của $V<sub>1</sub>$ là:

$ \begin{pmatrix} 1 & 0 & \cdots & 0 & \cdots & 0 \ 0 & 1 & \cdots & 0 & \cdots & 0 \ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \ 0 & 0 & \cdots & 1 & \cdots & 0 \ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \ 0 & 0 & \cdots & 0 & \cdots & 0 \end{pmatrix}. $

Bài tập 2.24. Chứng minh rằng nếu V $= V_1 \oplus V_2$, thì V đẳng cấu với tích trực tiếp $V_1 \times V_2$.

Chúng minh. v, $\alpha$, $\beta \in$ V. Giả sử

v $= v_1$ + $v_2 \overline{c_1} \overline{c_2} \overline{c_3} \overline{c_4} \overline{c_5} \overline{c_6} \overline{c_7} \overline{c_8} \overline{c_7} \overline{c_8} \overline{c_7} \overline{c_8} \overline{c_9}$

Ta xét ánh xạ:

$\varphi: V_1 \oplus V_2 \rightarrow V_1 \times V_2$

v $= v_1$ + $v_2 \mapsto (v_1$, $v_2)$

Anh xạ này là một đồng cấu tuyến tính vì:

$\varphi(\alpha+\beta)=(\alpha_1+\beta_1,\alpha_2+\beta_2)=(\alpha_1,\alpha_2)+(\beta_1,\beta_2)=\varphi(\alpha)+\varphi(\beta)$

$\varphi(a\alpha) = (a\alpha_1$, $a\alpha_2) = a(\alpha_1$, $\alpha_2) = a\varphi(\alpha)$

Anh xạ này là đơn cấu vì nếu $\varphi(\alpha) = \varphi(\beta)$ khi và chỉ khi $\alpha_1 = \beta_1$, $\alpha_2 = \beta_2$, tức là $\alpha = \beta$ (theo

dịnh nghĩa tổng trực tiếp).

Ánh xạ này là toàn cấu vì $\forall (v_1$, $v_2) \in V_1 \times V_2$ thì $\varphi(v_1$ + $v_2) = (v_1$, $v_2)$.

Do đó $\varphi$ là đẳng cấu. Như vậy, V $= V_1 \oplus V_2 \cong V_1 \times V_2$.

Bài tập 2.25. Chứng minh rằng tồn tại duy nhất tự đồng cấu $\mathbb{R}_3 \to \mathbb{R}_3$ chuyển các vector

$\alpha_1 =$ (2, 3, 5), $\alpha_2 =$ (0, 1, 2), $\alpha_3 =$ (1, 0, 0) tương ứng thành các vector $\beta_1 =$ (1, 1, 1), $\beta_2 =$ (1, 1, -1),

$\beta_3=(2,1,2)$. Tìm ma trận của fđối với cơ sở chính tắc của không gian.



VIIUVINU 2. INIA TIUAIN VA AINII AA TUTEIN TIINII

Chứng minh. Xét ràng buộc tuyến tính sau:

$a_1\alpha_1$ + $a_2\alpha_2$ + $a_3\alpha_3 =$ (0,0,0)

$\Leftrightarrow (2a_1$ + $a_3$, $3a_1$ + $a_2$, $5a_1$ + $2a_3) =$ (0, 0, 0)

$\Longleftrightarrow (2a_1$ + $a_3$, $3a_1$ + $a_2$, $5a_1$ + $2a_3$ - $2a_1$ - $a_3$ - $3a_1$ - $a_2) =$ (0, 0, 0)

$\Leftrightarrow (2a_1$ + $a_3$, $3a_1$ + $a_2$, $a_3$ - $a_2) =$ (0, 0, 0)

$\iff (2a_1$ + $a_3$, $a_1$ + $a_2$ - $a_3$, $a_3$ - $a_2) =$ (0, 0, 0)

$\Leftrightarrow (2a_1$ + $a_3$, $a_1$, $a_3$ - $a_2) =$ (0, 0, 0)

$\Longleftrightarrow (a_1$, $a_2$, $a_3) =$ (0, 0, 0)

Vậy hệ $(\alpha_1$, $\alpha_2$, $\alpha_3)$ độc lập tuyến tính.

Không gian vector $\mathbb{R}_3$ có số chiều là 3, do đó $(\alpha_1$, $\alpha_2$, $\alpha_3)$ là một cơ sở của $\mathbb{R}_3$.

Một ánh xạ tuyến tính được xác định duy nhất bởi tác động của nó lên một cơ sở, do đó tồn

tại duy nhất tự đồng cấu f : $\mathbb{R}_3 \to \mathbb{R}_3$ chuyển $\alpha_1 \mapsto \beta_1$, $\alpha_2 \mapsto \beta_2$, $\alpha_3 \mapsto \beta_3$.

$\beta_1 = 1\alpha_1$ + $(-2)\alpha_2$ + $(-1)\alpha_3 \beta_2 = 3\alpha_1$ + $(-8)\alpha_2$ + $(-5)\alpha_3 \beta_3 = 0\alpha_1$ + $1\alpha_2$ + $2\alpha_3$

Như vậy ma trận của tự đồng cấu f đối với cơ sở $(\alpha_1$, $\alpha_2$, $\alpha_3)$ là:

$ A = \begin{pmatrix} 1 & 3 & 0 \\ -2 & -8 & 1 \\ -1 & -5 & 2 \end{pmatrix} $

Ma trận chuyển từ cơ sở $(\alpha_1$, $\alpha_2$, $\alpha_3)$ sang cơ sở chính tắc là:

$ C = \begin{pmatrix} 0 & 2 & -1 \\ 0 & -5 & 3 \\ 1 & -4 & 2 \end{pmatrix} $

$f(e_1) = f(\alpha_3) = \beta_3 =$ (2, 1, 2) $f(e_2) = f(2\alpha_1$ - $5\alpha_2$ - $4\alpha_3) = 2\beta_1$ - $5\beta_2$ - $4\beta_3 =$ (-11, -7, -1) $f(e_3) = f(-\alpha_1$ + $3\alpha_2$ + $2\alpha_3) = -\beta_1$ + $3\beta_2$ + $2\beta_3 =$ (6, 4, 0)



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Vậy ma trận của f đối với cơ sở chính tắc là:

$ \begin{pmatrix} 2 & -11 & 6 \\ 1 & -7 & 4 \\ 2 & -1 & 0 \end{pmatrix} $

Bài tập 2.26. Tự đồng cấu f của không gian vector $\mathbb{F}^n$ chuyển các vector độc lập tuyến tính

$(\alpha_1,\ldots,\alpha_n)$ tương ứng thành các vector $\beta_1,\ldots,\beta_n$. Chứng minh rằng ma trận M(f) của f đối với

một cơ sở nào đó $(e_1$, $\ldots$, $e_n)$ thỏa mãn hệ thức M(f) $= BA^{-1}$, trong đó các cột của ma trận A và

ma trận B là tọa độ tương ứng của các vector $\alpha_1$, $\ldots$, $\alpha_n$ và $\beta_1$, $\ldots$, $\beta_n$ đối với cơ sở $(e_1$, $\ldots$, $e_n)$.

Chúng minh. Theo định nghĩa của M(f):

$(f(e_1) \dots f(e_n)) = (e_1 \dots e_n)$ M(f)

$(\alpha_1,\ldots,\alpha_n)$ độc lập tuyến tính trong không gian vector $\mathbb{F}^n$ nên $(\alpha_1,\ldots,\alpha_n)$ là một cơ sở.

A là ma trận mà các cột lần lượt là tọa độ của các vector $\alpha_1$, $\ldots$, $\alpha_n$ đối với cơ sở $(e_1$, $\ldots$, $e_n)$.

B là ma trận mà các cột lần lượt là tọa độ của các vector $\beta_1$, $\ldots$, $\beta_n$ đối với cơ sở $(e_1$, $\ldots$, $e_n)$.

$(\alpha_1 \ldots \alpha_n) = (e_1 \ldots e_n)A$

$(\beta_1 \ldots \beta_n) = (e_1 \ldots e_n)B$

$(f(\alpha_1) \dots f(\alpha_n)) = (f(e_1) \dots f(e_n))A$

$=(e_1 \ldots e_n)M(f)A$

Bên cạnh đó:

$(f(\alpha_1)\dots f(\alpha_n))=(\beta_1\dots\beta_n)$

$=(e_1 \ldots e_n)B$

Suy ra B $=$ M(f)A. Mà A là ma trận chuyển từ cơ sở $(e_1$, $\ldots$, $e_n)$ sang $(\alpha_1$, $\ldots$, $\alpha_n)$ nên A khả

nghịch. Do vậy M(f) $= M(f)AA^{-1} = BA^{-1}$.

$ Bài tập 2.27. Chứng minh rằng phép nhân với ma trận \begin{pmatrix} a & b \\ c & d \end{pmatrix} $

từ bên trái,

(a)

(b) từ bên phải



VIIUVINU 2. INIA TIUAIN VA AINII AA TUTEIN TIINII

là các tự đồng cấu của không gian các ma trận vuông cỡ 2. Hãy tìm ma trận của tự đồng cấu

đó đối với cơ sở gồm các ma trận sau đây:

$ \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}. $

Chứng minh. Phép nhân ma trận có tính phân phối với phép cộng ma trận nên:

$ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \left( \begin{pmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{pmatrix} + \begin{pmatrix} y_{11} & y_{12} \\ y_{21} & y_{22} \end{pmatrix} \right) = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{pmatrix} + \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} y_{11} & y_{12} \\ y_{21} & y_{22} \end{pmatrix} $

Bên cạnh đó, mọi ma trận đều giao hoán với ma trận vô hướng nên:

$ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} tx_{11} & tx_{12} \\ tx_{21} & tx_{22} \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} t & 0 \\ 0 & t \end{pmatrix} \begin{pmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{pmatrix} $

$ \begin{pmatrix} t & 0 \\ 0 & t \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{pmatrix} $

$ = t \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{pmatrix} $

Như vậy, phép nhân với một ma trận vuông cỡ 2 cho trước từ bên trái là một tự đồng cấu của

không gian M(2 $\times$ 2, $\mathbb{F})$.

Diều tương tự cũng đúng với phép nhân với một ma trận vuông cỡ 2 cho trước từ bên phải.

(a)

$ \left\{ \begin{pmatrix} a & b \\ c & d \\ c & d \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} a & 0 \\ c & 0 \\ 0 & c \end{pmatrix} \right\}
\left\{ \begin{pmatrix} a & b \\ c & d \\ c & d \end{pmatrix} \right\} \begin{pmatrix} 0 & 1 \\ 0 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & a \\ 0 & c \\ d & 0 \end{pmatrix} $

$ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & b \\ 0 & d \end{pmatrix} $



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Vậy ma trận của tự đồng cấu này đối với cơ sở chính tắc của M(2 $\times$ 2, $\mathbb{F})$ là:

$ \begin{pmatrix} a & 0 & b & 0 \\ 0 & a & 0 & b \\ c & 0 & d & 0 \\ 0 & c & 0 & d \end{pmatrix} $

(b)

$ \left\{ \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} a & b \\ 0 & 0 \end{pmatrix} \right\}
\left\{ \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} c & d \\ 0 & 0 \end{pmatrix} \right\}
\left\{ \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pm $

$ \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ c & d \end{pmatrix} $

Vậy ma trận của tự đồng cấu này đối với cơ sở chính tắc của M(2 $\times$ 2, $\mathbb{F})$ là:

$ \begin{pmatrix} a & c & 0 & 0 \\ b & d & 0 & 0 \\ 0 & 0 & a & c \\ 0 & 0 & b & d \end{pmatrix} $

$\Box$

Bài tập 2.28. Chứng minh rằng đạo hàm là một tự đồng cấu của không gian vector các đa thức

hệ số thực có bậc không vượt quá n. Tìm ma trận của tự đồng cấu đó với các cơ sở sau đây:

(a) (1, X, $\ldots$, $X^n)$.

(b) (1, (X - c), $\ldots$, $\frac{(X$ - $c)^n}{n!})$.

Chúng minh.

a(X) $= a_0$ + $a_1X$ + $\cdots$ + $a_nX^n$

b(X) $= b_0$ + $b_1$ X + $\cdots$ + $b_n X^n$



VIIUVINU 2. INIA TIUAIN VA AINII AA TUTEN TIINII

$\frac{d}{dX}(a(X)$ + b(X)) $= \frac{d}{dX}\left(\sum_{k=0}^{n}(a_k$ + $b_k)x^k\right)$

$=\sum^{n} k(a_k$ + $b_k)X^{k-1}$

$= \sum_{k=1}^{n} ka_k X^{k-1}$ + $\sum_{k=1}^{n} b_k X^{k-1}$

$=\frac{d}{dX}a(X)+\frac{d}{dX}b(X)$.

$\frac{d}{dX}(ta(X)) = \frac{d}{dX}\sum_{k=0}^{n} ta_k X^k$

$=$ t $\frac{d}{dX} \sum_{k=1}^{n}$ k $a_k X^{k-1}$

$=$ t $\frac{d}{dX}$ a(X).

Bên cạnh đó

$\deg \frac{d}{dX}a(X) < \deg$ a(X).

Do đó đạo hàm là một tự đồng cấu của không gian $\mathbb{R}[X]_n$.

(a) Ma trận của đạo hàm đối với cơ sở (1, X, $\ldots$, $X^n)$ là:

$ \begin{pmatrix} 0 & 1 & 0 & 0 & \cdots & 0 \\ 0 & 0 & 2 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 3 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & n \\ 0 & 0 & 0 & 0 & \cdots & 0 \end{pmatrix} $

(b) Ma trận của đạo hàm đối với cơ sở (1, (X - c), $\ldots$, $\frac{(X$ - $c)^n}{n!})$ là:

$ \begin{pmatrix} 0 & \frac{1}{0!} & 0 \end{pmatrix} $

$\overline{0}$

$ \begin{matrix}\n0 & \frac{1}{1!} & 0 & \cdots \\
0 & 0 & \frac{1}{2!} & \cdots\n\end{matrix} $

$\mathbb{E}\left[\left\{1\right\},\left\{1\right\},\left\{2\right\},\left\{3\right\}\right]\right]$

0 $\quad$ 0 $\quad$ 0 $\quad \cdots$

0 $\quad$ 0 $\quad$ 0 $\quad \cdots$



VIIUVINU 2. INIA TIUAIN VA AINII AA TUTEN TIINII

Bài tập 2.29. Ma trận của một tự đồng cấu đối với cơ sở $(e_1$, $\ldots$, $e_n)$ thay đổi thế nào nếu ta đổi

chỗ các vector $e_i$ và $e_j$.

Lời giải. Đổi chỗ $f(e_i)$, $f(e_j)$ thì hai cột thứ i, j của M(f) đổi chỗ.

Đổi chỗ $e_i$, $e_j$ thì hai hàng thứ i, j đổi chỗ.

Ma trận mới được dựng như sau

$\bullet$ Đổi chỗ cột i và j.

• Đổi chỗ hàng i và j.

nói cách khác

• Yếu tố hàng i cột i và hàng j cột i đổi chỗ.

• Yếu tố hàng i cột j và hàng j cột i đổi chỗ.

• Yếu tố hàng i cột k và hàng j cột k đổi chỗ (k $\notin \{i$, $j\})$.

• Yếu tố hàng k cột i và hàng k cột j đổi chỗ (k $\notin \{i$, $j\})$.

Bài tập 2.30. Tự đồng cấu f có ma trận

$ A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 3 & 0 & -1 & 2 \\ 2 & 5 & 3 & 1 \\ 1 & 2 & 1 & 2 \end{pmatrix} $

đối với cơ sở $(e_1$, $e_2$, $e_3$, $e_4)$. Hãy tìm ma trận của f đối với cơ sở $(e_1$, $e_1$ + $e_2$, $e_1$ + $e_2$ + $e_3$, $e_1$ + $e_2)$

$e_2$ + $e_3$ + $e_4$.

Lời giải. Ma trận chuyển từ cơ sở $(e_1$, $e_2$, $e_3$, $e_4)$ sang $(e_1$, $e_1$ + $e_2$, $e_1$ + $e_2$ + $e_3$, $e_1$ + $e_2$ + $e_3$ + $e_4)$ là:

(1 $\$ 1 $\$ 1 $\$ 1)

$ C = \left[ \begin{array}{rrr} 0 & 1 & 1 & 1 \ 0 & 0 & 1 & 1 \ 0 & 0 & 0 & 1 \end{array} \right] $



VIIUVINU 2. INA TIUAIN VA AINII AA TUTEN TIINII

Ma trận chuyển từ cơ sở $(e_1$, $e_1$ + $e_2$, $e_1$ + $e_2$ + $e_3$, $e_1$ + $e_2$ + $e_3$ + $e_4) = (e'_1$, $e'_2$, $e'_3$, $e'_4)$ sang

$(e_1$, $e_2$, $e_3$, $e_4)$ là:

$ C^{-1} = \begin{pmatrix} 1 & -1 & 0 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 0 & 1 \end{pmatrix} $

$f(e_1) = 1e_1$ + $3e_2$ + $2e_3$ + $1e_4$

$=1e'_1+3(e'_2-e'_1)+2(e'_3-e'_2)+1(e'_4-e'_3)$

$= (-2)e'_1$ + $1e'_2$ + $1e'_3$ + $1e'_4$

$f(e_2) = 2e_1$ + $0e_2$ + $5e_3$ + $2e_4$

$=2e'_1+0(e'_2-e'_1)+5(e'_3-e'_2)+2(e'_4-e'_3)$

$=2e'_1+(-5)e'_2+3e'_3+2e'_4$

$f(e_3) = 0e_1$ + $(-1)e_2$ + $3e_3$ + $1e_4$

$=0e'_1+(-1)(e'_2-e'_1)+3(e'_3-e'_2)+1(e'_4-e'_3)$

$=1e'_1+(-4)e'_2+2e'_3+1e'_4$

$f(e_4) = 1e_1$ + $2e_2$ + $1e_3$ + $3e_4$

$=1e'_1+2(e'_2-e'_1)+1(e'_3-e'_2)+3(e'_4-e'_3)$

$= (-1)e'_1$ + $1e'_2$ + $(-2)e'_3$ + $3e'_4$

$f(e'_1) = f(e_1)$

$= (-2)e'_1$ + $1e'_2$ + $1e'_3$ + $1e'_4$

$f(e'_2) = f(e_1)$ + $f(e_2)$

$=0e'_1+(-4)e'_2+4e'_3+2e'_4$

$f(e'_3) = f(e_1)$ + $f(e_2)$ + $f(e_3)$

$=1e'_1+(-8)e'_2+6e'_3+4e'_4$

$f(e'_4) = f(e_1)$ + $f(e_2)$ + $f(e_3)$ + $f(e_4)$

$= 0e'_1$ + $(-7)e'_2$ + $4e'_3$ + $7e'_4$



VIIUVINU 2. INA TIUAIN VA AINII AA TUTEN TIINII

Vậy ma trận của tự đồng cấu f đối với cơ sở $(e'_1$, $e'_2$, $e'_3$, $e'_4)$ là:

$ \begin{pmatrix} -2 & 0 & 1 & 0 \\ 1 & -4 & -8 & -7 \\ 1 & 4 & 6 & 4 \\ 1 & 2 & 4 & 7 \end{pmatrix} $

$\overline{\phantom{a}}$

Bài tập 2.31. Tự đồng cấu $\varphi$ có ma trận

$ \begin{pmatrix} 15 & -11 & 5 \\ 20 & -15 & 8 \\ 20 & 7 & 6 \end{pmatrix} $

đối với cơ sở $(e_1$, $e_2$, $e_3)$. Hãy tìm ma trận của $\varphi$ đối với cơ sở gồm các vector $\epsilon_1 = 2e_1$ + $3e_2$ + $e_3$,

$\epsilon_2 = 3e_1$ + $4e_2$ + $e_3$, $\epsilon_3 = e_1$ + $2e_2$ + $2e_3$.

Lời giải.

$e_1 = (-6)\epsilon_1$ + $4\epsilon_2$ + $1\epsilon_3 e_2 = 5\epsilon_1$ + $(-3)\epsilon_2$ + $(-1)\epsilon_3 e_3 = (-2)\epsilon_1$ + $1\epsilon_2$ + $1\epsilon_3$

$f(e_1) = 15e_1$ + $20e_2$ + $8e_3$

$=(-6)\epsilon_1+8\epsilon_2+3\epsilon_3$

$f(e_2) = (-11)e_1$ + $(-15)e_2$ + $(-7)e_3$

$=5\epsilon_1+(-6)\epsilon_2+(-3)\epsilon_3$

$f(e_3) = 5e_1$ + $8e_2$ + $6e_3$

$= (-2)\epsilon_1$ + $2\epsilon_2$ + $3\epsilon_3$



VIIUVINU 2. INIA TIUAIN VA AINII AA TUTEN TIINII

$f(\epsilon_1) = 2f(e_1)$ + $3f(e_2)$ + $f(e_3)$

$= \epsilon_1$

$f(\epsilon_2) = 3f(e_1)$ + $4f(e_2)$ + $f(e_3)$

$=2\epsilon_2$

$f(\epsilon_3) = f(e_1)$ + $2f(e_2)$ + $2f(e_3)$

$=3\epsilon_3$

Vậy ma trận của tự đồng cấu $\varphi$ đối với cơ sở $(\epsilon_1$, $\epsilon_2$, $\epsilon_3)$ là:

$ \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} $

Bài tập 2.32. Đồng cấu $\varphi$ : $\mathbb{C}_3 \to \mathbb{C}_3$ có ma trận

$ \begin{pmatrix} 1 & -18 & 15 \\ -1 & -22 & 20 \\ 1 & -25 & 22 \end{pmatrix} $

đối với cơ sở gồm các vector $\alpha_1 =$ (8, -6, 7), $\alpha_2 =$ (-16, 7, -13), $\alpha_3 =$ (9, -3, 7). Tìm ma trận

của $\varphi$ đối với cơ sở gồm các vector

$\beta_1 =$ (1, -2, 1), $\quad \beta_2 =$ (3, -1, 2), $\quad \beta_3 =$ (2, 1, 2).

Lời giải.

$ \begin{cases}\n\beta_1 = 1\alpha_1 + 1\alpha_2 + 1\alpha_3 \\
\beta_2 = 1\alpha_1 + 2\alpha_2 + 3\alpha_3 \\
\beta_3 = (-3)\alpha_1 + (-5)\alpha_2 + (-6)\alpha_3\n\end{cases} $

$ \left\{ \begin{array}{ll} \alpha_1 &= 3\beta_1 + 1\beta_2 + 1\beta_3 \\ \alpha_2 &= (-3)\beta_1 + (-3)\beta_2 + (-2)\beta_3 \\ \alpha_3 &= 1\beta_1 + 2\beta_2 + 1\beta_3 \end{array} \right. $



VIIUVINU 2. INIA TIUAIN VA AINII AA TUTEIN TIINII

$\varphi(\alpha_1) = 1\alpha_1$ + $(-1)\alpha_2$ + $1\alpha_3$

$= 7\beta_1$ + $6\beta_2$ + $4\beta_3$

$\varphi(\alpha_2) = (-18)\alpha_1$ + $(-22)\alpha_2$ + $(-25)\alpha_3$

$= (-13)\beta_1$ + $(-2)\beta_2$ + $1\beta_3$

$\varphi(\alpha_3) = 15\alpha_1$ + $20\alpha_2$ + $22\alpha_3$

$= 7\beta_1$ + $(-1)\beta_2$ + $(-3)\beta_3$

$\varphi(\beta_1) = \varphi(\alpha_1)$ + $\varphi(\alpha_2)$ + $\varphi(\alpha_3)$

$= 1\beta_1$ + $3\beta_2$ + $2\beta_3$

$\varphi(\beta_2) = \varphi(\alpha_1)$ + $2\varphi(\alpha_2)$ + $3\varphi(\alpha_3)$

$= 2\beta_1$ + $(-1)\beta_2$ + $(-3)\beta_3$

$\varphi(\beta_3) = (-3)\varphi(\alpha_1)$ + $(-5)\varphi(\alpha_2)$ + $(-6)\varphi(\alpha_3)$

$= 2\beta_1$ + $(-2)\beta_2$ + $1\beta_3$

Vậy ma trận của đồng cấu $\varphi$ đối với cơ sở $(\beta_1$, $\beta_2$, $\beta_3)$ là:

$ \begin{pmatrix} 1 & 2 & 2 \\ 3 & -1 & -2 \\ 2 & -3 & 1 \end{pmatrix} $

Bài tập 2.33. Chứng minh rằng các ma trận của một tự đồng cấu đối với hai cơ sở của không

gian là trùng nhau nếu và chỉ nếu ma trận chuyển giữa hai cơ sở đó giao hoán với ma trận của

đồng cấu đã cho đối với mỗi cơ sở nói trên.

Chứng minh. Gọi A là ma trận của tự đồng cấu đối với cơ sở thứ nhất, B là ma trận của tự đồng

cấu đối với cơ sở thứ hai và C là ma trận chuyển từ cơ sở thứ nhất sang cơ sở thứ hai.

Theo dinh lý 2.13, B $= C^{-1}AC$.

$(\Rightarrow)$ AC $=$ CA, BC $=$ CB.

Suy ra $C^{-1}AC =$ A. Mà B $= C^{-1}AC$ nên A $=$ B.

$(\Leftarrow)$

A $=$ B. B $= C^{-1}AC$ suy ra CB $=$ AC. Mà A $=$ B nên CA $=$ AC và CB $=$ BC. Điều này có

nghĩa là C giao hoán với cả A và B.

$ Bài tập 2.34. Tự đồng cấu \varphi \in End(\mathbb{R}_2) có ma trận \begin{pmatrix} 3 & 5 \\ 4 & 3 \end{pmatrix} đối với cơ sở gồm \alpha_1 = (1, 2), $



VIIUVINU 2. INIA TIUAIN VA AINII AA TUTEN TIINII

$ \alpha_2 = (2,3), và tự đồng cấu \psi \in End(\mathbb{R}_2) có ma trận \begin{pmatrix} 4 & 6 \\ 6 & 9 \end{pmatrix} đối với cơ sở gồm \beta_1 = (3,1), $

$\beta_2 =$ (4, 2). Tìm ma trận của $\varphi$ + $\psi$ đối với cơ sở $(\beta_1$, $\beta_2)$.

$L\delta$ i giải. Ma trận chuyển từ cơ $sở(\alpha_1,\alpha_2) sang(\beta_1,\beta_2)là:$

$ \begin{pmatrix} -7 & -8 \\ 5 & 6 \end{pmatrix} $

Ma trận chuyển từ cơ sở $(\beta_1$, $\beta_2)$ sang $(\alpha_1$, $\alpha_2)$ là:

$ \begin{pmatrix} -3 & -4 \\ \frac{5}{2} & \frac{7}{2} \end{pmatrix} $

Ma trận của tự đồng cấu $\varphi$ đối với cơ sở $(\beta_1$, $\beta_2)$ là:

$ \begin{pmatrix} -3 & -4 \\ \frac{5}{6} & \frac{7}{6} \end{pmatrix} \begin{pmatrix} 3 & 5 \\ 4 & 3 \end{pmatrix} \begin{pmatrix} -7 & -8 \\ 5 & 6 \end{pmatrix} = \begin{pmatrix} 40 & 38 \\ -\frac{71}{8} & -34 \end{pmatrix} $

Vậy ma trận của tự đồng cấu $\varphi$ + $\psi$ đối với cơ sở $(\beta_1$, $\beta_2)$ là:

$ \begin{pmatrix} 40 & 38 \\ -\frac{71}{5} & -34 \end{pmatrix} + \begin{pmatrix} 4 & 6 \\ 6 & 9 \end{pmatrix} = \begin{pmatrix} 44 & 44 \\ -\frac{59}{3} & -25 \end{pmatrix} $

$\Box$

$ Bài tập 2.35. Tự đồng cấu \varphi \in End(\mathbb{R}_2) có ma trận \begin{pmatrix} 2 & -1 \\ 5 & -3 \end{pmatrix} đối với cơ sở \alpha_1 = (-3, 7),
\alpha_2 = (1, -2), và tự đồng cấu \psi \in End(\mathbb{R}_2) có ma trận \begin{pmatrix} 1 & 3 \\ 2 & 7 \end{pmatrix} đối với cơ sở gồm \beta_1 = (6 $

$\beta_2 =$ (-5,6). Tìm ma trận của $\varphi \psi$ đối với cơ sở chính tắc của $\mathbb{R}_2$.

Lời giải. Ma trận chuyển từ cơ sở $(\alpha_1$, $\alpha_2)$ sang cơ sở chính tắc là:

$ \begin{pmatrix} 2 & 1 \\ 7 & 3 \end{pmatrix} $

Ma trận của tự đồng cấu $\varphi$ đối với cơ sở chính tắc là:

$ \begin{pmatrix} -3 & 1 \\ 7 & -2 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ 5 & -3 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 7 & 3 \end{pmatrix} = \begin{pmatrix} -2 & -1 \\ 1 & 1 \end{pmatrix} $



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Ma trận chuyển từ cơ sở $(\beta_1$, $\beta_2)$ sang cơ sở chính tắc là:

$ \begin{pmatrix} 6 & 7 \\ 5 & 6 \end{pmatrix} $

Ma trận của tự đồng cấu $\psi$ đối với cơ sở chính tắc là:

$ \begin{pmatrix} 6 & -7 \\ -5 & 6 \end{pmatrix} \begin{pmatrix} 1 & 3 \\ 2 & 7 \end{pmatrix} \begin{pmatrix} 6 & 7 \\ 5 & 6 \end{pmatrix} = \begin{pmatrix} -203 & -242 \\ 177 & 211 \end{pmatrix} $

Ma trận của $\varphi\psi$ đối với cơ sở chính tắc là:

$ \begin{pmatrix} -2 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} -203 & -242 \\ 177 & 211 \end{pmatrix} = \begin{pmatrix} 229 & 273 \\ -26 & -31 \end{pmatrix} $

Bài tập 2.36. Giả sử tự đồng cấu $\varphi$ : V $\to$ V thỏa mãn hệ thức $\varphi^2 = \varphi$. Chứng minh rằng

V $= \text{im}(\varphi) \oplus \text{ker}(\varphi)$.

Chúng minh. Giả sử v $\in$ V.

$v=(v-\varphi(v))+\varphi(v)$

Rõ ràng $\varphi(v) \in \text{im}(\varphi)$. Bên cạnh đó, $\varphi(v$ - $\varphi(v)) = \varphi(v)$ - $\varphi^2(v) =$ 0 nên v - $\varphi(v) \in \text{ker}(\varphi)$.

Như vậy V $= \text{im}(\varphi)$ + $\text{ker}(\varphi)$.

Giả sử $\alpha \in \text{im}(\varphi) \cap \text{ker}(\varphi)$. Vì $\alpha \in \text{im}(\varphi)$ nên tồn tại $\beta \in$ V sao cho $\varphi(\beta) = \alpha$. Vì $\alpha \in \text{ker}(\varphi)$

nên $\varphi(\alpha) =$ 0.

$\alpha = \varphi(\beta) = \varphi^2(\beta) = \varphi(\varphi(\beta)) = \varphi(\alpha) =$ 0

Do đó $im(\varphi) \cap \ker(\varphi) = \{0\}$. Vậy V $= \text{im}(\varphi) \oplus \ker(\varphi)$.

$\Box$

Bài tập 2.37. Cho các tự đồng cấu $\varphi$, $\psi \in$ End(V).

(a) Phải chăng nếu $\varphi \psi =$ 0 thì $\psi \varphi =$ 0?

(b) Phải chăng nếu $\varphi \psi = \psi \varphi =$ 0 thì $\varphi =$ 0 hoặc $\psi =$ 0?

Chứng minh. Kí hiệu ma trận của $\varphi$, $\psi$ đối với cùng một cơ sở của V là A, B.

(a) $\varphi \psi =$ 0 khi và chỉ khi AB $=$ 0.



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Vì M(n $\times$ n, $\mathbb{F}) \cong$ End(V) nên A, B có thể là bất cứ ma trận vuông cỡ n nào. Chọn

$ A = \begin{pmatrix} 0 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} \qquad B = \begin{pmatrix} 1 & 1 & \cdots & 1 \\ 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 \end{pmatrix} $

Khi đó AB $=$ 0 nhưng BA $\neq$ 0. Như vậy, từ $\varphi \psi =$ 0, không thể suy ra $\psi \varphi =$ 0.

(b) Chọn A $= E_{11}$ là ma trận vuông cỡ n có yếu tố hàng 1 cột 1 bằng 1, các yếu tố còn lại bằng

0. B $= E_{22}$ là ma trận vuông cỡ n có yếu tố hàng 2 cột 2 bằng 1, các yếu tố còn lại bằng 0.

Bằng quy tắc nhân ma trận, ta tính ra được AB $=$ 0, BA $=$ 0. Thế nhưng A, B $\neq$ 0.

Do đó, nếu $\varphi \psi = \psi \varphi =$ 0 thì không thể suy ra $\varphi =$ 0 hoặc $\psi =$ 0.

Bài tập 2.38. Giả sử $\varphi$ và $\psi$ là các tự đồng cấu của không gian vector hữu hạn chiều V. Chứng

minh rằng $\varphi\psi$ là một đẳng cấu nếu và chỉ nếu $\varphi$ và $\psi$ là các đẳng cấu. Khi đó

$(\varphi \psi)^{-1} = \psi^{-1} \psi^{-1}$

Chứng minh. $(\Rightarrow)$ Nếu $\varphi$ và $\psi$ là các đẳng cấu thì $\varphi\psi$ cũng là đẳng cấu vì đồng cấu này có nghịch

dảo là $\psi^{-1}\psi^{-1}$.

$(\varphi \psi)\psi^{-1}\varphi^{-1} = \varphi(\psi \psi^{-1})\varphi^{-1} = \varphi \varphi^{-1} = id_V$

$\psi^{-1} \varphi^{-1}(\varphi \psi) = \psi^{-1}(\varphi^{-1} \varphi) \psi = \psi^{-1} \psi = id_V$

$(\Leftarrow) \varphi \psi$ là đẳng cấu thì nó vừa là đơn cấu vừa là toàn cấu.

Vì $\varphi\psi$ là đơn cấu nên $\psi$ là đơn cấu.

Vì $\varphi\psi$ là toàn cấu nên $\varphi$ là toàn cấu.

Mà $\varphi$ và $\psi$ là các tự đồng cấu của một không gian vector hữu hạn chiều nên $\varphi$ và $\psi$ cũng đồng

thời là đẳng cấu nếu là đơn cấu hoặc toàn cấu.

Do đó $\varphi$ và $\psi$ là các đẳng cấu.

Do tính duy nhất của đẳng cấu ngược, ta suy ra $(\varphi \psi)^{-1} = \psi^{-1} \varphi^{-1}$.

Bài tập 2.39. Ký hiệu vết của ma trận vuông A là tr(A). Chứng minh rằng ánh xạ tr : M(n $\times$

n, F, A $\mapsto \text{tr}(A)$ là một đồng cấu. Tìm một cơ sở của nhân của tr.



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Chứng minh. A $= (a_{ij})_{n \times n}$, B $= (b_{ij})_{n \times n}$.

$ \begin{cases} \operatorname{tr}(A+B) = \sum_{i=1}^{n} (a_{ii} + b_{ii}) = \sum_{i=1}^{n} a_{ii} + \sum_{i=1}^{n} b_{ii} = \operatorname{tr}(A) + \operatorname{tr}(B) \\ \operatorname{tr}(aA) = \sum_{i=1}^{n} a a_{ii} = a \sum_{i=1}^{n} a_{ii} = a \cdot \operatorname{tr}(A) \end{cases} $

Như vậy, tr là một đồng cấu tuyến tính.

Giả sử C $= (c_{ij})_{n \times n}$ là một ma trận có vết bằng không. $E_{ij}$ là ma trận vuông cỡ n có yếu tố

hàng i cột j bằng đơn vị, các yếu tố còn lại bằng không.

$(c_{ij})_{n \times n} = \text{diag}(c_{11}$, $\ldots$, $c_{nn})$ + $\sum_{1 \leq$ i $\neq$ j $\leq n} c_{ij} E_{ij}$.

Ma trận vuông cỡ n mà thỏa mãn hai điều kiện:

(i) là ma trận chéo có vết bằng không

(ii) là ma trận có các yếu tố trên đường chéo chính bằng không

là ma trận không.

Kết hợp với đẳng thức trên, suy ra ker(tr) là tổng trực tiếp của không gian các ma trận vuông

cỡncó các yếu tố trên đường chéo chính bằng không và không gian các ma trận vuông chéo cỡ n

có vết bằng không.

$(E_{ij})_{i\neq j}$ là một cơ sở của không gian các ma trận vuông cỡ n với các yếu tố trên đường chéo

chính bằng không. Cơ sở này gồm n(n-1) ma trận.

Một cơ sở của không gian các ma trận chéo cỡ n có vết bằng không là

$ (n-1) ma trận \begin{cases} \text{diag}(1,-1,0,0,\ldots,0) \\ \text{diag}(1,0,-1,0,\ldots,0) \\ \text{diag}(1,0,0,-1,\ldots,0) \\ \vdots \\ \text{diag}(1,0,0,0,\ldots,-1) \end{cases} $

Hợp của hai cơ sở này tạo thành một cơ sở của ker(tr).

Bài tập 2.40. Chứng minh rằng vết của hai ma trận đồng dạng bằng nhau. (Từ đó người ta định

nghĩa vết của một tự đồng cấu là vết của ma trận của nó đối với cơ sở bất kỳ của không gian.)



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Chứng minh. A, B là hai ma trận đồng dạng thì tồn tại ma trận C khả nghịch, cùng cỡ với A và

B sao cho B $= C^{-1}AC$.

Theo Bài 2.7:

tr(B) $= tr(C^{-1}AC) = tr(ACC^{-1}) =$ tr(A).

Bài tập 2.41. Chứng minh rằng nếu tích ma trận AB có nghĩa thì

$(AB)^{\top} = B^{\top}A^{\top}$

Từ đó suy ra rằng ma trận vuông A khả nghịch nếu và chỉ nếu $A^{\dagger}$ khả nghịch, và khi đó

$(A^{\top})^{-1} = (A^{-1})^{\top}$

Chúng minh. Dặt A $= (a_{ij})_{m \times n}$, B $= (b_{ij})_{n \times p}$.

$ A = \begin{pmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{n1} & \cdots & a_{nn} \end{pmatrix} B = \begin{pmatrix} b_{11} & \cdots & b_{1p} \\ \vdots & \ddots & \vdots \\ b_{n1} & \cdots & b_{nn} \end{pmatrix} $

Suy ra $A^{\top} \in$ M(n $\times$ m, $\mathbb{F})$, $B^{\top} \in$ M(p $\times$ n, $\mathbb{F})$.

Do đó tích $B^{\top}A^{\top}$ có nghĩa và hai ma trận $(AB)^{\top}$, $B^{\top}A^{\top}$ đều có p hàng, m cột.

Yếu tố hàng i, cột j của ma trận $(AB)^{\top}$ là:

$\sum_{k=1}^n a_{jk}b_{ki}$

Yếu tố hàng i, cột j của ma trận $B^{\top}A^{\top}$ là:

$\sum_{i=1}^{n}b_{ki}a_{jk}$

$k=1$

Hai tổng trên bằng nhau, với mọi cặp số tự nhiên i, j thỏa mãn 1 $\leq$ i $\leq$ p, 1 $\leq$ j $\leq$ m. Như

vậy, $(AB)^{\top} = B^{\top}A^{\top}$.

Nếu ma trận vuông A cỡ n khả nghịch thì

$(A^{-1})^{\top}A^{\top} = (AA^{-1})^{\top} = E_n^{\top} = E_n$

$A^{\top} (A^{-1})^{\top} = (A^{-1}A)^{\top} = E_n^{\top} = E_n$



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Hai đẳng thức trên có nghĩa là $A^{\top}$ khả nghịch và $(A^{\top})^{-1} = (A^{-1})^{\top}$. Ngược lại, $A^{\top}$ khả nghịch

thì A khả nghịch, bởi vì $(A^{\top})^{\top} =$ A.

Bài tập 2.42. Cho các đồng cấu f: V $\to$ W và g: W $\to$ Z. Chứng minh mối liên hệ giữa các

đồng cấu đối ngẫu:

$(gf)^* = f^*g^*$

Từ đó suy ra rằng đồng $cấuf:V\to$ Wkhả nghịch nếu và chỉ $nếuf^*:W^*\to V^*khả$ nghịch,

và khi đó

$(f^*)^{-1} = (f^{-1})^*$

Chứng minh. Giả sử $\rho \in Z^*$. Theo định nghĩa của ánh xạ đối ngẫu:

$(gf)^*(\rho) = \rho$ gf

$(f^*g^*)(\rho) = f^*(g^*(\rho)) = f^*(\rho$ g) $= \rho$ gf

Do đó, $(gf)^*(\rho) = (f^*g^*)(\rho)$, $\forall \rho \in Z^*$. Suy ra $(gf)^* = f^*g^*$.

Giả sử $(\alpha_1$, $\ldots$, $\alpha_n)$ là một cơ sở của V, $(\beta_1$, $\ldots$, $\beta_m)$ là một cơ sở của W.

$(\alpha_1^*$, $\ldots$, $\alpha_n^*)$ là cơ sở đối ngẫu của $(\alpha_1$, $\ldots$, $\alpha_n)$.

$(\beta_1^*$, $\ldots$, $\beta_m^*)$ là cơ sở đối ngẫu của $(\beta_1$, $\ldots$, $\beta_m)$.

Ma trận của f đối với cặp cơ sở $(\alpha_1,\ldots,\alpha_n)$, $(\beta_1,\ldots,\beta_m)$ là A thì ma trận của $f<sup>*</sup>$ đối với cặp

co sở $(\beta_1^*$, $\ldots$, $\beta_m^*)$, $(\alpha_1^*$, $\ldots$, $\alpha_n^*)$ là $A^{\perp}$.

f khả nghịch khi và chỉ khi A là ma trận vuông và khả nghịch.

$f^*$ khả nghịch khi và chỉ khi $A^{\dagger}$ là ma trận vuông và khả nghịch.

Mà A khả nghịch khi và chỉ khi $A^{\dagger}$ khả nghịch nên f khả nghịch khi và chỉ khi $f<sup>*</sup>$ khả nghịch.

f khả nghịch thì

$\mathrm{id}_{V^*} = \mathrm{id}^*_{V} = (f^{-1}f)^* = f^*(f^{-1})^*$

$\mathrm{id}_{W^*} = \mathrm{id}_W^* = (ff^{-1})^* = (f^{-1})^* f^*$

Như vậy, $(f^*)^{-1} = (f^{-1})^*$.

Bài tập 2.43. Chứng minh rằng ánh xạ hom(V, W) $\to \text{hom}(W^*$, $V^*)$, f $\mapsto f^*$ là một đẳng cấu

tuyến tính.

Chúng minh. $(\alpha_1$, $\ldots$, $\alpha_n)$ là một cơ sở của V; $(\beta_1$, $\ldots$, $\beta_m)$ là một cơ sở của W.

$(\alpha_1^*$, $\ldots$, $\alpha_n^*)$ là cơ sở đối ngẫu của V, $(\beta_1^*$, $\ldots$, $\beta_m^*)$ là cơ sở đối ngẫu của W.

A là ma trận của f đối với cặp cơ sở trên của V và W.

$A^{\dagger}$ là ma trận của $f^*$ đối với cặp cơ sở trên của $W^*$ và $V^*$.



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

Anh xạ hom(V, W) $\to$ M(m $\times$ n, $\mathbb{F})$, f $\mapsto$ A là đẳng cấu tuyến tính.

Ánh xạ $hom(W^*$, $V^*) \to$ M(n $\times$ m, $\mathbb{F})$, $f^* \mapsto A^{\top}$ là đẳng cấu tuyến tính.

Ánh xạ A $\mapsto A^{\top}$ là đẳng cấu tuyến tính.

Do đó ánh xạ hom(V, W) $\to \text{hom}(W^*$, $V^*)$, f $\mapsto f^*$ là đẳng cấu tuyến tính.

$\Box$

### Dịnh lý 4.8. Gọi f^*: W^* \to V^* là đồng cấu đối ngẫu của đồng cấu f: V \to W. Khi đó:

f là một đơn cấu nếu và chỉ nếu $f^*$ là một toàn cấu.

(1)

(2) f là một toàn cấu nếu và chỉ nếu $f^*$ là một đơn cấu.

(3) f là một đẳng cấu nếu và chỉ nếu $f^*$ là một đẳng cấu.

Nhắc lại một kết quả cần thiết.

$\mathbf{B}\mathbf{\hat{o}}$ đề 2.44. V và W là các không gian vector trên trường $\mathbb{F}$.

$(\alpha_1$, $\ldots$, $\alpha_n)$ là một cơ sở của không gian vector V.

$(\omega_1$, $\ldots$, $\omega_n)$ là n vector bất kỳ của không gian vector W.

Khi đó tồn tại duy nhất một ánh xạ tuyến tính $\tau$ : V $\to$ W sao cho $\tau(\alpha_i) = \omega_i$, $\forall$ i $=$ 1, n.

$\mathbf{B}\mathbf{\hat{o}}$ đề 2.45. V là một không gian vector n-chiều và $V^*$ là không gian vector đối ngẫu của V.

$\nu_1$, $\ldots \nu_n$ là một cơ sở của $V^*$.

Chứng minh rằng tồn tại một cơ sở $\alpha_1$, $\ldots$, $\alpha_n$ của V sao cho

$\nu_i(\alpha_j)=\delta_{i,j}$

Chứng minh bổ đề. Suy ra từ phép đối ngẫu kép $\alpha_i \mapsto \alpha_i^* \mapsto \alpha_i^{**}$.

Chứng minh. $(\alpha_1$, $\ldots$, $\alpha_n)$ là một cơ sở của V.

(1) $(\Rightarrow)$

$\{\alpha_1,\ldots,\alpha_n\}$ độc lập tuyến tính trong V và f là đơn ánh nên $\{f(\alpha_1),\ldots,f(\alpha_n)\}$ độc lập

tuyền tính trong W.

Do dim W $=$ m nên n $\leq$ m. Ta bổ sung các vector $\beta_{n+1}$, $\ldots$, $\beta_m$ vào hệ các vector

$f(\alpha_1)$, $\ldots$, $f(\alpha_n)$ để tạo thành một cơ sở của W.

Chọn $\nu$ là một dạng tuyến tính trên V.

Để chỉ ra $f^*$ là một toàn cấu, ta cần xây dựng một dạng tuyến tính $\omega \in W^*$ sao cho $f^*(\omega) = \nu$.

Theo Bổ đề trên, tồn tại duy nhất một dạng tuyến tính $\omega \in W^*$ sao cho:

$\omega(f(\alpha_i)) = \nu(\alpha_i) \quad \forall$ i $=$ 1, n,

$\omega(\beta_i) =$ 0 $\quad \forall$ j $= \overline{n+1,m}$.



VIIUVINU 2. IVIA TIUAIN VA AINII AA TUTEIN TIINII

$\forall \alpha \in$ V, ta có biểu thị tuyến tính duy nhất theo cơ sở $(\alpha_1$, $\ldots$, $\alpha_n):$

$\alpha = x_1 \cdot \alpha_1$ + $\cdots$ + $x_n \cdot \alpha_n$

Khi đó:

$\omega(f(\alpha)) = x_1 \cdot \nu(\alpha_1)$ + $\cdots$ + $x_n \cdot \nu(\alpha_n)$

$= \nu(x_1 \cdot \alpha_1$ + $\cdots$ + $x_n \cdot \alpha_n)$

$= \nu(\alpha) (\forall \alpha \in$ V).

tức là $\omega \circ$ f $= \nu$.

Mà $f^*(\omega) = \omega \circ$ f nên $f^*(\omega) = \nu$.

Ta đã có được dạng tuyến tính $\omega \in W^*$ như mong muốn.

Do đó, $f^*$ là một toàn cấu.

(←) Để chứng minh f là đơn cấu, ta sẽ chỉ ra ker f $= \{0\}$.

Chọn $\nu$ là một dạng tuyến tính trên V và là một đơn cấu.

$\alpha$ là một vector bất kỳ thuộc ker f.

Do $f^*: W^* \to V^*$ là một toàn cấu nên tồn tại một dạng tuyến tính $\omega \in W^*$ sao cho

$f^*: \omega \mapsto \nu$.

Theo định nghĩa của đồng cấu đối ngẫu

$f^*(\omega) = \omega \circ$ f

$\implies \nu = \omega \circ$ f

$\implies \nu(\alpha) = \omega(f(\alpha))$

$\implies \nu(\alpha) =$ 0.

Theo lựa chọn ban đầu, $\nu$ là một đơn cấu. Do đó $\alpha =$ 0.

Điều này chứng tỏ f là một đơn cấu.

(2) $(\Rightarrow)$ Chọn $\omega_1$, $\omega_2$ là hai dạng tuyến tính thuộc $W^*$ sao cho $f^*(\omega_1) = f^*(\omega_2)$.

Theo định nghĩa của đồng cấu đối ngẫu, $\omega_1 \circ$ f $= \omega_2 \circ$ f.

f là toàn cấu nên $\forall \beta \in$ W, tồn tại $\alpha \in$ V sao cho $f(\alpha) = \beta$.

Suy ra $\forall \beta \in$ W, $\omega_1(\beta) = \omega_1(f(\alpha)) = \omega_2(f(\alpha)) = \omega_2(\beta)$. Diều này nghĩa là $\omega_1 = \omega_2$.



VIIUVINU 2. INIA TIUAIN VA AINII AA TUTEN TIINII

Do đó $f^*(\omega_1) = f^*(\omega_2) \rightarrow \omega_1 = \omega_2$.

Vậy $f^*$ là một đơn cấu.

$(\Leftarrow) f^*$ là đơn cấu nên dim $W^* \leq \dim V^*$, kéo theo dim W $\leq \dim$ V.

Chọn $\beta_1$, $\beta_2$, $\ldots$, $\beta_m$ làm cơ sở của W. $\beta_1^*$, $\beta_2^*$, $\ldots$, $\beta_m^*$ là cơ sở đối ngẫu.

Do $f^*$ là một đơn cấu nên $\alpha_1^* = f^*(\beta_1^*)$, $\alpha_2^* = f^*(\beta_2^*)$, $\ldots$, $\alpha_m^* = f^*(\beta_m^*)$ độc lập tuyến tính.

Theo bổ đề trên, tồn tại $\alpha_i$, i $= \overline{1,n}$ sao cho $\alpha_i^*(\alpha_j) = \delta_{i,j}$, tồn tại $\beta_i$, i $= \overline{1,m}$ sao cho

$\beta_i^*(\beta_i) = \delta_{i,j}$.

$\beta$ là một vector thuộc W. Giả sử tọa độ của $\beta$ với cơ sở $\beta_1$, $\ldots$, $\beta_m$ là $(x_1$, $\ldots$, $x_m)$.

Chon $\alpha = x_1 \alpha_1$ + $\cdots$ + $x_m \alpha_m$.

$\beta_i^*(f(\alpha_i)) = f^*(\beta_i^*)(\alpha_i)$

$=\alpha_i^*(\alpha_i)$

$= \delta_{i,j}$

Dặt $\beta^* = \sum_{i=1}^m x_i \beta_i^*$.

$\beta^*(f(\alpha)) = \sum_i x_i \beta_i^*(f(\alpha))$

$=\sum_{i=1}^m x_i\beta_i^*\left(\sum_{i=1}^m x_jf(\alpha_j)\right)$

$= \sum x_i^2 \beta_i^* (f(\alpha_i))$

$= \sum_{i=1} x_i^2$

$= \beta^*(\beta)$

Suy ra, $\forall \beta^* \in W^*$, $\ \beta^*(f(\alpha)$ - $\beta) =$ 0. Do đó, $f(\alpha) = \beta$.

Như vậy, $\forall \beta \in$ W, $\exists \alpha \in$ V : $f(\alpha) = \beta$. Do đó f là một toàn ánh.

(3) f là một đẳng cấu khi và chỉ khi f vừa là đơn cấu, vừa là toàn cấu. Theo hai kết quả vừa

chứng minh, $f^*$ vừa là toàn cấu, vừa là đơn cấu. Do đó $f^*$ là đẳng cấu.

Ngược lại, $f^*$ là một đẳng cấu thì f là một đẳng cấu.



# Chương 3

Định thức và hệ phương trình tuyến tính

Thực hiện các phép nhân sau đây, viết các phép thế thu được thành tích của những xích rời

rạc và tính dấu của chúng.

$ Bài tập 3.1. \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 2 & 4 & 5 & 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 5 & 1 & 2 \end{pmatrix}. $

$L\delta$ i qidi.

$ \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 2 & 4 & 5 & 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 5 & 1 & 2 \end{pmatrix} = \begin{pmatrix} 4 & 3 & 5 & 1 & 2 \\ 1 & 5 & 3 & 2 & 4 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 5 & 1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 5 & 3 & 2 & 4 \end{pmatrix}. $

$ \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 5 & 3 & 2 & 4 \end{pmatrix} = (2, 5, 4). $

$ sgn\begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 5 & 3 & 2 & 4 \end{pmatrix} = sgn(2, 5, 4) = 1. $

$\Box$

$ Bài tập 3.2. \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 4 & 1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 1 & 5 & 2 \end{pmatrix}. $

Lời giải.

$ \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 4 & 1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 1 & 5 & 2 \end{pmatrix} = \begin{pmatrix} 4 & 3 & 1 & 5 & 2 \\ 1 & 4 & 3 & 2 & 5 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 1 & 5 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 4 & 3 & 2 & 5 \end{pmatrix}. $

$ \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 4 & 3 & 2 & 5 \end{pmatrix} = (1)(2,4)(3)(5). $



VIIUVINU 9. DINII TIIUV VA IID LIIUVNU TIIINII TUTEN TIINII

$ sgn\begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 4 & 3 & 2 & 5 \end{pmatrix} = sgn(2, 4) = -1. $

Bài tập 3.3. (1,2)(2,3) $\dots$ (n-1,n).

Bo đề 3.4. $(a_1$, $a_2$, $\ldots$, $a_k)(a_k$, $a_{k+1}) = (a_1$, $a_2$, $\ldots$, $a_{k+1})$.

Chúng minh bổ đề. Xét dãy

$a_1$, $a_2$, $\ldots$, $a_{k-1}$, $a_k$, $a_{k+1}$.

Sau khi tác động bằng $(a_k$, $a_{k+1})$, dãy trên trở thành:

$a_1$, $a_2$, $\ldots$, $a_{k-1}$, $a_{k+1}$, $a_k$.

Sau khi tác động bằng $(a_1$, $a_2$, $\ldots$, $a_k)$, dãy liền trên trở thành:

$a_2$, $a_3$, $\ldots$, $a_k$, $a_{k+1}$, $a_1$.

Theo định nghĩa về xích, ta có điều phải chứng minh.

Lời giải. Theo bổ đề 3.4:

$ (1,2)(2,3)...(n-1,n) = (1,2,...,n) = \begin{pmatrix} 1 & 2 & \cdots & n-1 & n \\ 2 & 3 & \cdots & n & 1 \end{pmatrix} $

(1, 2, $\ldots$, n) chính là một xích.

$sgn(1,2,\ldots,n) =$ sgn(1,2) sgn(2,3) $\ldots$ sgn(n-1,n) $= (-1)^{n-1}$.

Bài tập 3.5. (1,2,3)(2,3,4)(3,4,5) $\dots$ (n-2,n-1,n).

Lời giải. Theo bổ đề 3.4, nếu n $>$ 3:

$(1,2,3)(2,3,4)(3,4,5)\ldots(n-2,n-1,n) = (1,2)(2,3)(2,3)(3,4)(3,4)(4,5)\ldots(n-2,n-1)(n-1,n)$

$=(1,2)(2,3)^2(3,4)^2..$. $(n-2,n-1)^2(n-1,n)$

$=(1,2)(n-1,n)$ (dây là 2 xích rời nhau)

$ = \begin{pmatrix} 1 & 2 & 3 & \cdots & n-2 & n-1 & n \\ 2 & 1 & 3 & \cdots & n-2 & n & n-1 \end{pmatrix}. $



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

Nếu $n=3:$

$ (1,2,3) = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix}. $

Trong cả hai trường hợp, dấu của phép thế (kết quả) là 1.

Bài tập 3.6. Cho hai cách sắp thành dãy $a_1$, $a_2$, $\ldots$, $a_n$ và $b_1$, $b_2$, $\ldots$, $b_n$ của n số tự nhiên đầu

tiên. Chứng minh rằng có thể đưa cách sắp này về cách sắp kia bằng cách sử dụng không quá

n-1 phép thế sơ cấp.

Bố đề 3.7. $\forall \sigma \in S_n$, $\forall$ x $\in \{1$, 2, ..., $n\}$, $\exists$ k $\in \mathbb{N}$, k $\leq$ n sao cho $\sigma^k(x) =$ x.

Chứng minh bổ đề 3.8. Giả sử phản chứng, $\sigma^k(x) \neq$ x, $\ \forall$ k $= \overline{1$, $n}$.

Có hai trường hợp cần xem xét.

Trường hợp 1: n số $\sigma(x)$, $\sigma^2(x)$, ..., $\sigma^n(x)$ đôi một khác nhau.

Vì n số này đôi một khác nhau và đều là các phần tử của tập hợp n số tự nhiên đầu tiên

nên tồn tại một số tự nhiên k $\leq$ n sao cho $\sigma^k(x) =$ x.

Trường hợp 2: Trong n số $\sigma(x)$, $\sigma^2(x)$, ..., $\sigma^n(x)$, có hai số bằng nhau.

Giả sử $\sigma^a(x) = \sigma^{a+b}(x)$, trong đó 1 $\le$ a $<$ a+b $\le$ n.

$(\underbrace{\sigma \circ \cdots \circ \sigma}_{a})(x) = (\underbrace{\sigma \circ \cdots \circ \sigma}_{a+b})(x)$

$\Longleftrightarrow ((\underbrace{\sigma^{-1} \circ \ldots \circ \sigma^{-1}}_{a}) \circ (\underbrace{\sigma \circ \cdots \circ \sigma})(x) = ((\underbrace{\sigma^{-1} \circ \ldots \circ \sigma^{-1}}_{a}) \circ (\underbrace{\sigma \circ \cdots \circ \sigma})(x)$

$\Longleftrightarrow$ x $= \sigma^b(x)$.

Bổ đề được chứng minh.

Bố đề 3.8. Mỗi phần tử của n số tự nhiên đầu tiên luôn thuộc một xích nào đó.

Chúng minh. Theo bổ đề 3.7, cùng với nguyên lý sắp thứ tự tốt (well-ordering principle), ta suy

ra luôn chọn được số tự nhiên k nhỏ nhất sao cho $\sigma^k(x) =$ x.

(x, $\sigma(x)$, $\ldots$, $\sigma^{k-1}(x))$ chính là một xích độ dài k.

Bổ đề 3.9. Mọi phép thế đều có thể được viết dưới dạng tích của các xích rời nhau.

Chứng minh bổ đề 3.9. Theo bổ đề 3.8, mỗi phần tử đều thuộc một xích nào đó.

Nếu hai xích cùng chứa một phần tử x thì hai xích đó trùng nhau.

Do đó hai xích bất kì hoặc trùng nhau, hoặc rời nhau.

Ta tiến hành phân tích một phép thế thành các xích rời nhau.



VIIUVINU 0. DIINII TIIUV VA IID I IIUVINU TIIIINII TUTEN TIINII

Chọn lấy một phần tử bất kì của tập hợp n số tự nhiên đầu tiên.

(1)

Xác định xích của phần tử đó.

(2)

(3) Chọn lấy một phần tử bất kì không thuộc xích, tiếp xúc xác định xích của phần tử mới này.

Quy trình trên được làm liên tục đến khi không còn phần tử nào để chọn. Quy trình này sẽ

dừng lại sau hữu hạn bước vì số phần tử của tập hợp n số tự nhiên là hữu hạn, và độ dài của một

xích cũng không vượt quá số phần tử của tập hợp n số tự nhiên đầu tiên.

Bố đề 3.10. Theo bổ đề trước, mỗi phép thế $\sigma$ viết được dưới dạng tích của $f(\sigma)$ các xích rời nhau

(bao gồm cả các xích độ dài 1), trong đó $f(\sigma)$ là một số nguyên dương xác định.

Với mọi phép thế sơ cấp $\tau$, $f(\tau\sigma) = f(\sigma)$ + 1 hoặc $f(\tau\sigma) = f(\sigma)$ - 1.

Chứng minh. Giả sử $\tau =$ (i, j). Nếu i, j thuộc cùng một xích của $\sigma$ thì $f(\tau \sigma) = f(\sigma)$ + 1. Ngược

lai, $f(\tau \sigma) = f(\sigma)$ - 1.

Bố đề 3.11. Một xích độ dài k (k $>$ 1) có thể viết được dưới dạng tích của k - 1 phép thế sơ cấp

nhưng không thể viết được dưới dạng tích của ít hơn k-1 phép thế sơ cấp.

Chứng minh bổ đề 3.11. Một xích độ dài k sẽ tác động lên dãy $x_1$, $x_2$, $\ldots$, $x_k$ như sau:

$x_1 \mapsto x_2 \mapsto x_3 \mapsto \cdots \mapsto x_k \mapsto x_1$.

Xích trên có thể phân tích được thành tích của k-1 phép thế sơ cấp, theo bổ đề 3.4:

$(x_1$, $x_2$, $\ldots$, $x_k) = (x_1$, $x_2$, $\ldots$, $x_{k-1})(x_{k-1}$, $x_k)$

$=(x_1$, $x_2$, $\ldots$, $x_{k-2})(x_{k-2}$, $x_{k-1})(x_{k-1}$, $x_k)$

$= \ldots$

$=(x_1,x_2)(x_2,x_3)\ldots(x_{k-1},x_k)$.

Không mất tính tổng quát, giả sử chúng ta đang xét các phép thế trên tập hợp $\{1,\ldots,k\}$. Giả

sử phản chứng rằng $(x_1$, $x_2$, $\ldots$, $x_k)$ là tích của $\leq$ k-2 phép thế sơ cấp thì theo Bổ đề 3.10

$f((x_1$, $x_2$, $\ldots$, $x_k)) = f((x_1$, $x_2$, $\ldots$, $x_k))id) \geq$ k - (k - 2) $=$ 2

mà $f((x_1$, $x_2$, $\ldots$, $x_k)) =$ 1 nên giả sử phản chứng là sai. Vậy $(x_1$, $x_2$, $\ldots$, $x_k)$ không thể viết

dưới dạng tích của ít hơn k-1 phép thế sơ cấp.

Chứng minh. Xét phép thế $\sigma$ trên tập hợp n số tự nhiên đầu tiên.

Theo bổ đề 3.9, ta phân tích phép thế $\sigma$ thành các xích rời nhau. Tổng độ dài của các xích này

bằng n. Gọi số xích rời rạc là $\ell$.



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

Theo bổ đề 3.11, mỗi xích độ dài k đều phân tích được thành tích của k-1 phép thế sơ cấp.

Kết hợp hai điều trên, một phép thế có thể phân tích được thành tích của n - $\ell$ phép thế sơ

cấp. Mà n - $\ell \leq$ n - 1 nên ta có điều phải chứng minh.

Điều này tương đương với việc có thể đưa cách sắp dãy $a_1$, $a_2$, $\ldots$, $a_n$ thành $b_1$, $b_2$, $\ldots$, $b_n$ và

ngược lại bằng cách thực hiện không quá n-1 phép thế sơ cấp.

Bài tập 3.12. Với giả thiết như bài trên, chứng minh rằng có thể đưa cách sắp này về cách sắp

kia bằng cách sử dụng không quá n(n-1)/2 phép chuyển vị của hai phần tử đứng kề nhau.

Chứng minh. Ta chỉ cần chứng minh có thể đưa cách sắp thứ nhất thành cách sắp thứ hai bằng

cách sử dụng không quá n(n-1)/2 phép chuyển vị của hai phần tử đứng kề nhau.

Như giả thiết, cách sắp dãy thứ nhất là $a_1$, $a_2$, $\ldots$, $a_n;$ cách sắp dãy thứ hai là $b_1$, $b_2$, $\ldots$, $b_n$.

Lưu ý rằng $\{a_1$, $a_2$, $\ldots$, $a_n\} = \{b_1$, $b_2$, $\ldots$, $b_n\}$.

Tồn tại duy nhất $a_{k_1}$ sao cho $a_{k_1} = b_n$.

(1)

(2) Ta lần lượt thực hiện cách phép chuyển vị hai phần tử kề nhau: $(a_{k_1}$, $a_{k_1+1})$, $(a_{k_1}$, $a_{k_1+2})$,

$\dots (a_{k_1}$, $a_n)$.

(3) Sau khi thực hiện các phép chuyển vị như trên, $a_k$ ở vị trí cuối cùng trong dãy.

Trong quy trình trên, ta thực $hiệnn-k_1phép$ chuyển vị hai phần tử kề nhau.

Trong n-1 phần tử đầu tiên của dãy $a_1$, $a_2$, $\ldots$, $a_n$, tồn tại $a_{k_2} = b_{n-1}$, ta thực hiện các phép

chuyển vị $(a_{k_2}$, $a_{k_2+1})$, $(a_{k_2}$, $a_{k_2+2})$, $\ldots (a_{k_2}$, $a_{n-1})$. Ta đã thực hiện (n-1) - $k_2$ phép chuyển vị hai

phần tử kề nhau.

Liên tiếp thực hiện việc dồn dãy như trên, ta đưa được cách sắp thứ nhất về cách sắp thứ hai

- chỉ bằng các phép chuyển vị hai phần tử kề nhau.

Số phép chuyển vị hai phần tử kề nhau đã được sử dụng không vượt quá

(n-1) + (n-2) + $\cdots$ + 2 + 1 $= \frac{n(n-1)}{2}$.

Đó cũng là điều phải chứng minh.

Bài tập 3.13. Cho ví dụ về một cách sắp dãy n số tự nhiên đầu tiên thành dãy sao cho dãy này

không thế đưa về dãy sắp tự nhiên bằng cách dùng ít hơn n-1 phép thế sơ cấp.

Lời giải. Cách sắp như vậy được tạo ra từ một xích độ dài n.

(1, 2, 3, $\ldots$, n).

Theo Bổ đề 3.10, xích trên không viết được dưới dạng tích của ít hơn n-1 phép thế sơ cấp. $\square$



VIIUVINU 9. DIINII TIIUV VA IIIJ I IIUVINU TIURIII TUTER TIINII

Bài tập 3.14. Biết số nghịch thế của dãy $a_1$, $a_2$, $\ldots$, $a_n$ là k. Hãy tìm số nghịch thế của dãy $a_n$,

$a_{n-1}$, $\ldots$, $a_1$.

Lời giải. Không mất tính tổng quát, ta giả sử $a_1$, $a_2$, $\ldots$, $a_n$ là một hoán vị của n số tự nhiên đầu

tiên.

Nếu cặp $(a_i$, $a_j)$ trong dãy $a_1$, $a_2$, $\ldots$, $a_n$ là nghịch thế thì trong dãy $a_n$, $a_{n-1}$, $\ldots$, $a_1$ lại không

phải nghịch thế.

Nếu cặp $(a_i$, $a_j)$ trong dãy $a_1$, $a_2$, $\ldots$, $a_n$ không phía nghịch thế thì trong dãy $a_n$, $a_{n-1}$, $\ldots$, $a_1$

lại là phải nghịch thế.

Do đó, số nghịch thế trong $a_n$, $a_{n-1}$, ..., $a_1$ là $\frac{n(n-1)}{2}$ - k.

└

Bài tập 3.15. Tính các định thức sau đây

$ (a) \begin{vmatrix} 2 & -5 & 4 & 3 \\ 3 & -4 & 7 & 5 \\ 4 & -9 & 8 & 5 \end{vmatrix} $

|-3 2 -5 3

$ (b) \begin{vmatrix} 3 & -3 & -2 & -5 \\ 2 & 5 & 4 & 6 \\ 5 & 5 & 8 & 7 \\ 4 & 4 & 5 & 6 \end{vmatrix} $

Lời giải.

(a)

$ \begin{vmatrix} 2 & -5 & 4 & 3 \\ 3 & -4 & 7 & 5 \\ 4 & -9 & 8 & 5 \\ -3 & 2 & -5 & 3 \end{vmatrix} = \begin{vmatrix} 2 & -5 & 4 & 3 \\ 3 & -4 & 7 & 5 \\ 0 & 1 & 0 & -1 \\ 0 & -2 & 2 & 8 \end{vmatrix} = \begin{vmatrix} 2 & -5 & 4 & 3 \\ 0 & 3.5 & 1 & 0.5 \\ 0 & 1 & 0 & -1 \\ 0 & -2 & 2 & 8 \end{vmatrix} = \begin{vmatrix} 2 & -5 & 4 & 3 \\ 0 & 1 & 0 & -1 \\ 0 & -2 & $

$ = \begin{vmatrix} 2 & -5 & 4 & 3 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 2 & 6 \\ 0 & 0 & 1 & 4 \end{vmatrix} = \begin{vmatrix} 2 & -5 & 4 & 3 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 2 & 6 \\ 0 & 0 & 0 & 1 \end{vmatrix} = 2 \cdot 1 \cdot 2 \cdot 1 = 4. $



VIIUVINU 9. DIINII TIIUV VA IIIJ I IIUVINU TIURIII TUTER TIINII

(b)

$ \begin{vmatrix} 3 & -3 & -2 & -5 \\ 2 & 5 & 4 & 6 \\ 5 & 5 & 8 & 7 \\ 4 & 4 & 5 & 6 \end{vmatrix} = \begin{vmatrix} 1 & -8 & -6 & -11 \\ 2 & 5 & 4 & 6 \\ 5 & 5 & 8 & 7 \\ 4 & 4 & 5 & 6 \end{vmatrix} = \begin{vmatrix} 1 & -8 & -6 & -11 \\ 0 & 21 & 16 & 28 \\ 0 & 45 & 38 & 62 \\ 0 & 36 & 29 & 50 \end{vmatrix} = \begin{vmatrix} 21 & 16 & 28 \\ 45 & 38 & 62 $

$=$ 21(38 $\cdot$ 50 - 62 $\cdot$ 29) + 16(62 $\cdot$ 36 - 45 $\cdot$ 50) + 28(45 $\cdot$ 29 - 36 $\cdot$ 38) $=$ 90.

Bài tập 3.16. Tính các định thức sau bằng cách đưa về dạng tam giác:

$ (a) \begin{vmatrix} 1 & 2 & 3 & \cdots & n \\ -1 & 0 & 3 & \cdots & n \\ -1 & -2 & 0 & \cdots & n \\ \vdots & \vdots & \vdots & \ddots & \vdots \end{vmatrix} $

-1 -2 -3 $\cdots$ 0

$ (b) \begin{vmatrix} a_0 & a_1 & a_2 & \cdots & a_n \\ -x & x & 0 & \cdots & 0 \\ 0 & -x & x & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x \end{vmatrix} $

$ (c) \begin{vmatrix} a_1 & a_2 & a_3 & \cdots & a_n \\ -x_1 & x_2 & 0 & \cdots & 0 \\ 0 & -x_2 & x_3 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x_n \end{vmatrix}. $

Lời giải. (a) $r_k := r_k$ + $r_1$, $\forall$ 1 $<$ k $\leq$ n.

$ \begin{vmatrix} 1 & 2 & 3 & \cdots & n \\ -1 & 0 & 3 & \cdots & n \\ -1 & -2 & 0 & \cdots & n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ -1 & -2 & -3 & \cdots & 0 \end{vmatrix} = \begin{vmatrix} 1 & 2 & 3 & \cdots & n \\ 0 & 2 & 6 & \cdots & 2n \\ 0 & 0 & 3 & \cdots & 2n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & n \end{vmatrix} = n! $

(b) Thực hiện lần lượt các biến đổi sơ cấp sau:



VIIUVINU 9. DINII THUU VA HIJ LHUUNU TIIINII TUTEN TINII

• $c_0 = \sum_{k=0}^{n} c_k$.

• $c_1 = \sum_{k=1}^{n} c_k$.

• $c_n = \sum_{k=1}^{n} c_k$.

$k=n$

$ \begin{vmatrix} a_0 & a_1 & a_2 & \cdots & a_n \\ -x & x & 0 & \cdots & 0 \\ 0 & -x & x & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x \end{vmatrix} = \begin{vmatrix} \sum_{k=0}^n a_k & a_1 & a_2 & \cdots & a_n \\ 0 & x & 0 & \cdots & 0 \\ 0 & -x & x & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x \end{vmatrix} = \begin{vmatrix} \sum_{k=0}^n a_k & \sum $

$\left|\sum_{k=0}^n a_k \sum_{k=1}^n a_k \sum_{k=n}^n a_k \cdots a_n\right|$

$ =\begin{vmatrix} 0 & x & 0 & \cdots & 0 \\ 0 & 0 & x & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & 0 \\ 0 & 0 & 0 & \cdots & x \end{vmatrix}=\left(\sum_{k=0}^n a_k\right)x^n. $

(c) Nếu $x_1=0$

$ \begin{vmatrix} a_1 & a_2 & a_3 & \cdots & a_n \\ -x_1 & x_2 & 0 & \cdots & 0 \\ 0 & -x_2 & x_3 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x_n \end{vmatrix} = \begin{vmatrix} a_1 & a_2 & a_3 & \cdots & a_n \\ 0 & x_2 & 0 & \cdots & 0 \\ 0 & -x_2 & x_3 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x_n \end{vmatrix} $

$ \begin{vmatrix} x_2 & 0 & \cdots & 0 \\ -x_2 & x_3 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & x_n \end{vmatrix} = a_1 x_2 x_3 \cdots x_n $

$= a_1$



VIIUVINU 9. DINII TIIUV VA IID LIIUVNU TIIINII TUTEN TIINII

Nếu $x_k =$ 0

$ \begin{vmatrix} a_1 & a_2 & a_3 & \cdots & a_n \\ -x_1 & x_2 & 0 & \cdots & 0 \\ 0 & -x_2 & x_3 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x_n \end{vmatrix} = a_k \prod_{i=1, i \neq k}^n x_i $

Nếu $x_k \neq$ 0, $\forall$ k $= \overline{1$, $n}$.

$ \begin{vmatrix} a_1 & a_2 & a_3 & \cdots & a_n \\ -x_1 & x_2 & 0 & \cdots & 0 \\ 0 & -x_2 & x_3 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x_n \end{vmatrix} = \frac{1}{x_1 x_2} \begin{vmatrix} a_1 x_2 & a_2 x_1 & a_3 & \cdots & a_n \\ -x_1 x_2 & x_1 x_2 & 0 & \cdots & 0 \\ 0 & -x_1 x_2 & x_3 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 $

$a_1x_2$ + $a_2x_1$

$a_2x_1$

$a_3$

$a_n$

$\bullet$ , $\bullet$ , $\bullet$

$\overline{0}$

$\theta$

$\theta$

$x_1x_2$

$\bullet$ , $\bullet$ , $\bullet$

$-x_1x_2$

$-x_1x_2$

$\cup$

$x_3$

$\bullet$ , $\bullet$ , $\bullet$

$x_1x_2$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\boldsymbol{x}_n$

$\bullet$ , $\bullet$ , $\bullet$

$a_1x_2x_3$ + $a_2x_1x_3$

$a_3x_1x_2$

$a_2x_1x_3$

$a_n$

$\bullet$ , $\bullet$ , $\bullet$

$\overline{0}$

$\overline{0}$

$x_1x_2x_3$

$\cup$

$\bullet$ , $\bullet$ , $\bullet$

$x_1x_2x_3$

$\left( \right)$

$-x_1x_2x_3$

$-x_1x_2x_3$

$\bullet$ , $\bullet$ , $\bullet$

$\sqrt{x_1^2x_2^2x_3^2}$

$\left\langle \cdot\right\rangle _{+}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$x_n$

$\bullet$ , $\bullet$ , $\bullet$ .

$a_1x_2x_3$ + $a_2x_1x_3$ + $a_3x_1x_2$

$a_2x_1x_3$

$a_3x_1x_2$

$a_n$

$\bullet$ , $\bullet$ , $\bullet$

$\vert$ 0 $\vert$

$\overline{0}$

$\overline{0}$

$x_1x_2x_3$

$\bullet$ , $\bullet$ , $\bullet$

$\overline{0}$

$\overline{0}$

$x_1x_2x_3$

$-x_1x_2x_3$

$x_1^2x_2^2x_3^2$

$\mathcal{O}(\mathcal{E}_{\mathcal{A}})$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$|x_n|$

$\bullet$ , $\bullet$ , $\bullet$

$= \frac{1}{(x_1x_2...x_n)^{n-1}} (a_1x_2x_3...x_n$ + $a_2x_1x_3...x_n$ + $\cdots$ + $a_nx_1x_2...x_{n-1})$

$\times (x_2x_3 \ldots x_n)(x_1x_3 \ldots x_n) \cdots (x_1x_2 \ldots x_{n-1})$

$a_1x_2x_3...x_n+a_2x_1x_3...x_n+\cdots+a_nx_1x_2...x_{n-1}$

$=\sum_{k=1}^n \left(a_k \prod_{i \neq k}^n x_i\right)$



VIIUVINU 9. DIINII TIIUV VA IID I IIUVINU TIIIINII TUTEN TIINII

Bài tập 3.17. Tính định thức của ma trận vuông cỡ n với yếu tố nằm ở hàng i cột j bằng |i - j|.

Lời giải.

$ \begin{vmatrix} 0 & 1 & 2 & \cdots & n-1 \\ 1 & 0 & 1 & \cdots & n-2 \\ 2 & 1 & 0 & \cdots & n-3 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ n-1 & n-2 & n-3 & \cdots & 0 \end{vmatrix} = \begin{vmatrix} 0 & 1 & 2 & \cdots & n-1 \\ 1 & -1 & -1 & \cdots & -1 \\ 1 & 1 & -1 & \cdots & -1 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & 1 & 1 & \cdots & -1 \end{vmatrix} (r_k := r_k - r_{k-1}) $

$ =\begin{vmatrix} n-1 & 1 & 2 & \cdots & n-1 \\ 0 & -1 & -1 & \cdots & -1 \\ 0 & 1 & -1 & \cdots & -1 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 1 & 1 & \cdots & -1 \end{vmatrix} (c_1 := c_1 + c_n) $

$ =\begin{vmatrix} n-1 & 1 & 2 & \cdots & n-1 \\ 0 & -1 & -1 & \cdots & -1 \\ 0 & 0 & -2 & \cdots & -2 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & -2 \end{vmatrix} (r_k := r_k + r_{k-1}) $

$=(-2)^{n-1}(n-1)$.

Bài tập 3.18. Tính các định thức sau đây bằng phương pháp rút ra các nhân tử tuyến tính:

$ (a) \begin{vmatrix} 1 & 2 & 3 & \cdots & n \\ 1 & x+1 & 3 & \cdots & n \\ 1 & 2 & x+1 & \cdots & n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & 2 & 3 & \cdots & x+1 \end{vmatrix}, $

1+x

$ (b) \begin{vmatrix} 1 & 1-x & 1 & 1 \\ 1 & 1 & 1+y & 1 \\ 1 & 1 & 1 & 1-y \end{vmatrix}. $



VIIUVINU 9. DINII THUU VA HUTTIIUVINU TIIINII TUTEN TIINII

Lời giải. (a)

$ \begin{vmatrix} 1 & 2 & 3 & \cdots & n \\ 1 & x+1 & 3 & \cdots & n \\ 1 & 2 & x+1 & \cdots & n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & 2 & 3 & \cdots & x+1 \end{vmatrix} = \begin{vmatrix} 1 & 0 & 0 & \cdots & 0 \\ 1 & x-1 & 0 & \cdots & 0 \\ 1 & 0 & x-2 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & 0 & 0 & \cdots & x-(n-1) \end{vmatrix} (c_k := c_k - k \times c_1) $

$ =\begin{vmatrix} 1 & 0 & 0 & \cdots & 0 \\ 0 & x-1 & 0 & \cdots & 0 \\ 0 & 0 & x-2 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \cdots & \cdots & \cdots & \cdots \end{vmatrix} (r_k := r_k - r_1) $

$ \begin{vmatrix} 0 & 0 & 0 & \cdots & x-(n-1) \end{vmatrix} $

$=(x-1)(x-2)\cdots(x-n+1)$.

$ (b) Dặt \varepsilon_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \varepsilon_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \varepsilon_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \varepsilon_4 = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}, \varepsilon = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}. $

$ \begin{vmatrix} 1+x & 1 & 1 & 1 \\ 1 & 1-x & 1 & 1 \\ 1 & 1 & 1+y & 1 \\ 1 & 1 & 1 & 1-y \end{vmatrix} = det (\varepsilon + x\varepsilon_1, \varepsilon - x\varepsilon_2, \varepsilon + y\varepsilon_3, \varepsilon - y\varepsilon_4) $

$=\det(\varepsilon$, $-x\varepsilon_2$, $y\varepsilon_3$, $-y\varepsilon_4)$ + $\det(x\varepsilon_1$, $\varepsilon$, $y\varepsilon_3$, $-y\varepsilon_4)$

+ $det(x\varepsilon_1$, $-x\varepsilon_2$, $\varepsilon$, $-y\varepsilon_4)$ + $det(x\varepsilon_1$, $-x\varepsilon_2$, $y\varepsilon_3$, $\varepsilon)$

$+\det(x\varepsilon_1,-x\varepsilon_2,y\varepsilon_3,-y\varepsilon_4)$

$= xy^{2}$ - $xy^{2}$ + $x^{2}y$ - $x^{2}y$ + $x^{2}y^{2}$

$= x^2 y^2$.

Bài tập 3.19. Tính các định thức sau đây bằng cách sử dụng các quan hệ hồi quy:

$ \begin{vmatrix} a_1b_1 & a_1b_2 & a_1b_3 & \cdots & a_1b_n \end{vmatrix} $

$|a_1b_2 \quad a_2b_2 \quad a_2b_3 \quad \cdots \quad a_2b_n|$

(a) $|a_1b_3 \quad a_2b_3 \quad a_3b_3 \quad \cdots \quad a_3b_n|$

$ \begin{vmatrix} \vdots & \vdots & \vdots & \ddots & \vdots \\ a_1b_n & a_2b_n & a_3b_n & \cdots & a_nb_n \end{vmatrix} $



VIIUVINU 9. DINII THUU VA HIJ LHUUNU TIIINII TUTEN TINII

$a_1 \quad a_2 \quad \cdots \quad a_n$

$a_0$

$-y_1 x_1$ 0 $\cdots$ 0

$ (b) \begin{vmatrix} 0 & -y_2 & x_2 & \cdots & 0 \end{vmatrix} $

$ \left|\begin{array}{ccccccccc} \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x_n \end{array}\right| $

Lời giải. (a)

$ \begin{vmatrix} a_1b_1 & a_1b_2 & a_1b_3 & \cdots & a_1b_n \end{vmatrix} \begin{vmatrix} b_1 & a_1b_2 & a_1b_3 & \cdots & a_1b_n \end{vmatrix} $

$ \begin{vmatrix} a_1b_2 & a_2b_2 & a_2b_3 & \cdots & a_2b_n \end{vmatrix} \qquad \begin{vmatrix} b_2 & a_2b_2 & a_2b_3 & \cdots & a_2b_n \end{vmatrix} $

$|a_1b_3 \quad a_2b_3 \quad a_3b_3 \quad \cdots \quad a_3b_n| = a_1b_n|b_3 \quad a_2b_3 \quad a_3b_3 \quad \cdots \quad a_3b_n$

$ \begin{vmatrix} \vdots & \vdots & \vdots & \ddots & \vdots \\ a_1b_n & a_2b_n & a_3b_n & \cdots & a_nb_n \end{vmatrix} \begin{vmatrix} \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & a_2 & a_3 & \cdots & a_n \end{vmatrix} $

$ \begin{vmatrix} 0 & a_1b_2 - a_2b_1 & a_1b_3 - a_3b_1 & \cdots & a_1b_n - a_nb_1 \end{vmatrix} $

0 $a_2b_3$ - $a_3b_2 \cdots a_2b_n$ - $a_nb_2$

$|0\rangle$

0 0 $\cdots a_3b_n$ - $a_nb_3$ | $(r_k := r_k$ - $b_kr_n)$

$= a_1 b_n$ |0

$ \begin{vmatrix} \vdots & \vdots & \ddots & \vdots \\ 1 & a_2 & a_3 & \cdots & a_n \end{vmatrix} $

$ =(-1)^{n-1}a_{1}b_{n}\begin{vmatrix} 1 & a_{2} & a_{3} & \cdots & a_{n} \\ 0 & a_{1}b_{2} - a_{2}b_{1} & a_{1}b_{3} - a_{3}b_{1} & \cdots & a_{1}b_{n} - a_{n}b_{1} \\ 0 & 0 & a_{2}b_{3} - a_{3}b_{2} & \cdots & a_{2}b_{n} - a_{n}b_{2} \\ 0 & 0 & 0 & \cdots & a_{3}b_{n} - a_{n}b_{3} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & a_{n-1} $

$= (-1)^{n-1} a_1 b_n (a_1 b_2$ - $a_2 b_1)(a_2 b_3$ - $a_3 b_2) \cdots (a_{n-1} b_n$ - $a_n b_{n-1})$.



VIIUVINU 9. DINII TIIUV VA IID LIIUVNU TIIINII TUTEN TIINII

(b)

$ \begin{vmatrix} a_0 & a_1 & a_2 & \cdots & a_n \\ -y_1 & x_1 & 0 & \cdots & 0 \\ 0 & -y_2 & x_2 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x_n \end{vmatrix} = \begin{vmatrix} a_0 & a_1 & a_2 & \cdots & a_n \\ 0 & x_1 & 0 & \cdots & 0 \\ 0 & -y_2 & x_2 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x_n \end{vmatrix} + \begin{vmatrix} 0 & a_1 $

$ = a_0 x_1 x_2 \cdots x_n + \begin{vmatrix} y_1 & -x_1 & 0 & \cdots & 0 \\ 0 & a_1 & a_2 & \cdots & a_n \\ 0 & -y_2 & x_2 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & x_n \end{vmatrix} $

$ = a_0x_1x_2 \cdots x_n + y_1 \begin{vmatrix} a_1 & a_2 & \cdots & a_n \\ -y_2 & x_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & x_n \end{vmatrix} (hệ thức truy hồi) $

$= a_0x_1x_2\cdots x_n$ + $y_1(a_1x_2\cdots x_n)$ + $\cdots$ + $y_1y_2\cdots y_n(a_n)$

$=\sum_{i=0}^n a_k \left(\prod_{i=1}^{\kappa} y_i\right) \left(\prod_{i=1}^{n-1} x_{i+1}\right)$.

Bài tập 3.20. Tính các định thức sau đây bằng cách biểu diễn chúng thành tổng của các định

thức nào đó:

$ (a) \begin{vmatrix} x+a_1 & a_2 & \cdots & a_n \\ a_1 & x+a_2 & \cdots & a_n \\ \vdots & \vdots & \ddots & \vdots \\ a_1 & a_2 & \cdots & x+a_n \end{vmatrix}, $

$ (b) \begin{vmatrix} x_1 & a_2 & \cdots & a_n \\ a_1 & x_2 & \cdots & a_n \\ \vdots & \vdots & \ddots & \vdots \\ a_1 & a_2 & \cdots & x_n \end{vmatrix}. $

Lời giải. Đặt $\varepsilon_1 =$ (1, 0, $\ldots$, 0), $\varepsilon_2 =$ (0, 1, $\ldots$, 0), $\ldots \varepsilon_n =$ (0, 0, $\ldots$, 1), $\varepsilon = \sum \varepsilon_i$.



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

(a)

$ \begin{vmatrix} x+a_1 & a_2 & \cdots & a_n \\ a_1 & x+a_2 & \cdots & a_n \\ \vdots & \vdots & \ddots & \vdots \\ a_1 & a_2 & \cdots & x+a_n \end{vmatrix} = \det(x\varepsilon_1 + a_1\varepsilon, x\varepsilon_2 + a_2\varepsilon, \ldots, x\varepsilon_n + a_n\varepsilon) $

$=\det(x\varepsilon_1$, $x\varepsilon_2$, $\ldots$, $x\varepsilon_n)$

+ $det(a_1 \varepsilon$, x $\varepsilon_2$, ..., x $\varepsilon_n)$ + det(x $\varepsilon_1$, $a_2 \varepsilon$, ..., x $\varepsilon_n)$

$+\cdots+\det(x\epsilon_1$, $x\epsilon_2,\ldots$, $a_n\varepsilon)$

$= x^{n}$ + $x^{n-1} \sum_{i=1}^{n} a_{i}$.

(b)

$ \begin{vmatrix} x_1 & a_2 & \cdots & a_n \\ a_1 & x_2 & \cdots & a_n \\ \vdots & \vdots & \ddots & \vdots \\ a_1 & a_2 & \cdots & x_n \end{vmatrix} = \begin{vmatrix} (x_1 - a_1) + a_1 & a_2 & \cdots & a_n \\ a_1 & (x_2 - a_2) + a_2 & \cdots & a_n \\ \vdots & \vdots & \ddots & \vdots \\ a_1 & a_2 & \cdots & (x_n - a_n) + a_n \end{vmatrix} $

$= det((x_1$ - $a_1)\varepsilon_1$ + $a_1\varepsilon$, $(x_2$ - $a_2)\varepsilon_2$ + $a_2\varepsilon$, $\ldots$, $(x_n$ - $a_n)\varepsilon_n$ + $a_n\varepsilon)$

$=(x_1-a_1)\cdots(x_n-a_n)\det(\varepsilon_1,\ldots,\varepsilon_n)$

$+\sum_{i=1}^n a_i \left(\prod_{\substack{j=1 \$ j $\neq i}}^n (x_j$ - $a_j)\right) \det(\ldots$, $\varepsilon_{i-1}$, $\varepsilon$, $\varepsilon_{i+1}$, $\ldots)$

$=\prod_{i=1}^{n} (x_i$ - $a_i)$ + $\sum_{i=1}^{n} a_i \left( \prod_{\substack{j=1 \$ j $\neq i}}^{n} (x_j$ - $a_j) \right)$.

Kí hiệu định thức Vandermonde cỡ n với n biến:

$ D_n = D_n(x_1, ..., x_n) = \begin{vmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ 1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_1^{n-1} \end{vmatrix}. $



VIIUVINU 9. DIINII TIIUV VA IIIJ I IIUVINU TIURIII TUTER TIINII

Kí hiệu đa thức đối xứng sơ cấp:

$e_k(x_1,...,x_n) = \sum_{1 \leq i_1 <$ ... $< i_k \leq n} \left( \prod_{i=1}^k x_{i_j} \right)$.

Ví dụ

$e_1(x_1$, $x_2$, $x_3) = x_1$ + $x_2$ + $x_3$

$e_2(x_1$, $x_2$, $x_3$, $x_4) = x_1x_2$ + $x_1x_3$ + $x_1x_4$ + $x_2x_3$ + $x_3x_4$ + $x_2x_4$

$e_3(x_1$, $x_2$, $x_3) = x_1x_2x_3$.

Kí hiệu đa thức đối xứng thuần nhất đầy đủ:

$h_k(x_1,\ldots,x_n) = \sum \prod_{i=1}^n x_j^{i_j}$

$i_1$ + $\cdots$ + $i_n =$ k i $=$ 1

Ví dụ

$h_1(x_1$, $x_2$, $x_3) = x_1$ + $x_2$ + $x_3$

$h_2(x_1$, $x_2$, $x_3) = x_1^2$ + $x_2^2$ + $x_3^2$ + $x_1x_2$ + $x_2x_3$ + $x_1x_3$

$h_3(x_1$, $x_2$, $x_3) = x_1^3$ + $x_2^3$ + $x_3^3$ + $x_1^2x_2$ + $x_1^2x_3$ + $x_2^2x_1$ + $x_2^2x_3$ + $x_3^2x_1$ + $x_3^2x_2$ + $x_1x_2x_3$.

Tính các định thức sau đây:

$ Bài tập 3.21.
\begin{vmatrix} a_1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ a_2 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_n & x_n & x_n^2 & \cdots & x_n^{n-1} \end{vmatrix}. $



VIIUVINU 9. DIINII TIIUV VA IID I IIUVINU TIUINII TUTEN TIINII

Lời giải. Khai triển Laplace theo cột thứ nhất:

$ \begin{vmatrix} a_1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ a_2 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_n & x_n & x_n^2 & \cdots & x_n^{n-1} \end{vmatrix} = \sum_{i=1}^n (-1)^{1+i} a_i \begin{vmatrix} \vdots & \vdots & \vdots & \ddots & \vdots \\ x_{i-1} & x_{i-1}^2 & x_{i-1}^3 & \cdots & x_{i-1}^{n-1} \\ x_{i+1} & x_{i+1}^2 & x_{i+1}^3 & \ $

$ = \sum_{i=1}^{n} (-1)^{1+i} a_i \prod_{j \neq i}^{n} \begin{vmatrix} \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_{i-1} & x_{i-1}^2 & \cdots & x_{i-1}^{n-2} \\ 1 & x_{i+1} & x_{i+1}^2 & \cdots & x_{i+1}^{n-2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \end{vmatrix} $

$= \sum_{i=1}^n (-1)^{1+i} a_i \left( \prod_{i=1}^n x_i \right) D_{n-1}(\ldots$, $x_{i-1}$, $x_{i+1}$, $\ldots)$.

$ Bài tập 3.22. (a) D_n^{(1)} = \begin{vmatrix} 1 & x_1^2 & x_1^3 & \cdots & x_1^n \\ 1 & x_2^2 & x_2^3 & \cdots & x_2^n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n^2 & x_n^3 & \cdots & x_n^n \end{vmatrix} $

$ (b) D_n^{(s)} = \begin{vmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^{s-1} & x_1^{s+1} & \cdots & x_1^n \\ 1 & x_2 & x_2^2 & \cdots & x_2^{s-1} & x_2^{s+1} & \cdots & x_2^n \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^{s-1} & x_n^{s+1} & \cdots & x_n^n \end{vmatrix}. $



VIIUVINU 0. DIINII TIIUV VA IID I IIUVINU TIIIINII TUTEN TIINII

$L\delta$ i giải. (a)

$ \begin{vmatrix} 1 & x_1^2 & x_1^3 & \cdots & x_1^n \\ 1 & x_2^2 & x_2^3 & \cdots & x_2^n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n^2 & x_n^3 & \cdots & x_n^n \end{vmatrix} = \begin{vmatrix} 1 & x_1^2 & x_1^3 & \cdots & x_1^{n-1}(x_1 - x_n) \\ 1 & x_2^2 & x_2^3 & \cdots & x_2^{n-1}(x_2 - x_n) \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n^2 & x_n^3 & \cdots & 0 \end{vm $

$ = \begin{vmatrix} 1 & x_1^2 & x_1^2(x_1 - x_n) & \cdots & x_1^{n-1}(x_1 - x_n) \\ 1 & x_2^2 & x_2^2(x_2 - x_n) & \cdots & x_2^{n-1}(x_2 - x_n) \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n^2 & 0 & \cdots & 0 \end{vmatrix} (c<sub>3</sub> := c<sub>3</sub> - x<sub>n</sub>c<sub>2</sub>) $

$ =\begin{vmatrix} 1 & (x_1 + x_n)(x_1 - x_n) & x_1^2(x_1 - x_n) & \cdots & x_1^{n-1}(x_1 - x_n) \\ 1 & (x_2 + x_n)(x_2 - x_n) & x_2^2(x_2 - x_n) & \cdots & x_2^{n-1}(x_2 - x_n) \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & 0 & 0 & \cdots & 0 \end{vmatrix} (c<sub>2</sub> := c<sub>2</sub> - x<sub>n</sub><sup>2</sup>c<sub>1</sub>) $

Khai triển Laplace theo cột thứ nhất

$ = (-1)^{n+1}(x_1 - x_n)(x_2 - x_n) \cdots (x_{n-1} - x_n) \begin{vmatrix} x_1 + x_n & x_1^2 & \cdots & x_1^{n-1} \\ x_2 + x_n & x_2^2 & \cdots & x_2^{n-1} \\ \vdots & \vdots & \ddots & \vdots \end{vmatrix} $

$|x_{n-1}$ + $x_n x_{n-1}^2 \cdots x_{n-1}^{n-1}|$

$ =\prod_{i=1}^{n-1}(x_n-x_i)\left(\begin{vmatrix}x_1&x_1^2&\cdots&x_1^{n-1}\\x_2&x_2^2&\cdots&x_2^{n-1}\\ \vdots&\vdots&\ddots&\vdots\\x_{n-1}&x_{n-1}^2&\cdots&x_{n-1}^{n-1}\end{vmatrix}+\begin{vmatrix}x_n&x_1^2&\cdots&x_1^{n-1}\\x_n&x_2^2&\cdots&x_2^{n-1}\\ \vdots&\vdots&\ddots&\vdots\\x_n&x_{n-1}^2&\cdots&x_{n-1}^{n-1}\end{vmatrix}\right) $

$D_n^{(1)} = (x_n$ - $x_1) \cdots (x_n$ - $x_{n-1}) \left( x_1 x_2 \cdots x_{n-1} D_{n-1}$ + $x_n D_{n-1}^{(1)} \right)$

$= x_n(x_n$ - $x_1) \cdots (x_n$ - $x_{n-1}) D_{n-1}^{(1)}$ + $(x_n$ - $x_1) \cdots (x_n$ - $x_{n-1}) x_1 x_2 \cdots x_{n-1} D_{n-1}$

$= x_n \prod_{i=1}^{n-1} (x_n$ - $x_i) \cdot D_{n-1}^{(1)}$ + $\prod_{i=1}^{n-1} x_i \cdot D_n$

$= x_n \prod_{i=1}^{n-1} (x_n$ - $x_i) \cdot \left( x_{n-1} \prod_{i=1}^{n-2} (x_{n-1}$ - $x_i) \cdot D_{n-2}^{(1)}$ + $\prod_{i=1}^{n-2} x_i \cdot D_{n-1} \right)$ + $\prod_{i=1}^{n-1} x_i \cdot D_n$



CHOONG 9. DINII THUU VA HIP LHUUNG TRINII TUTEN TINII

$x_n = x_n x_{n-1} \prod_{i=1}^{n-1} (x_n$ - $x_i) \prod_{i=1}^{n-2} (x_{n-1}$ - $x_i) \cdot D_{n-2}^{(1)}$ + $\prod_{1 \leq$ i $\neq n-1}^{n} x_i \cdot D_n$ + $\prod_{1 \leq$ i $\neq n}^{n} x_i \cdot D_n$

$= \cdot \cdot \cdot$

$= D_n x_1 x_2 \cdots x_n \sum_{i=1}^n \frac{1}{x_i}$

$D_n \sum_{i=1}^n \left( \prod_{1 \leq$ j $\neq i}^n x_j \right)$

$= D_n e_{n-1}(x_1,...,x_n)$.



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

(b) Ta xét trường hợp đặc biệt

$ D_n^{(n-1)} = \begin{vmatrix} 1 & x_1 & \cdots & x_1^{n-2} & x_1^n \\ 1 & x_2 & \cdots & x_2^{n-2} & x_2^n \\ \vdots & \vdots & \ddots & \cdots & \vdots \\ 1 & x_n & \cdots & x_n^{n-2} & x_n^n \end{vmatrix} $

$ = \begin{vmatrix} 1 & x_1 - x_n & \cdots & x_1^{n-3}(x_1 - x_n) & x_1^{n-2}(x_1 + x_n)(x_1 - x_n) \\ 1 & x_2 - x_n & \cdots & x_2^{n-3}(x_2 - x_n) & x_2^{n-2}(x_2 + x_n)(x_2 - x_n) \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 1 & 0 & \cdots & 0 & 0 \end{vmatrix} $

$ =\prod_{1\leq i\neq n}^{n}(x_n-x_i)\begin{vmatrix} 1 & x_1 & \cdots & x_1^{n-3} & x_1^{n-1}+x_1^{n-2}x_n \\ 1 & x_2 & \cdots & x_2^{n-3} & x_2^{n-1}+x_2^{n-2}x_n \\ \vdots & \vdots & \ddots & \cdots & \vdots \\ 1 & x_{n-1} & \cdots & x_{n-1}^{n-3} & x_{n-1}^{n-1}+x_{n-1}^{n-2}x_n \end{vmatrix} $

$= \prod (x_n$ - $x_i) \cdot D_{n-1}^{(n-2)}$ + $x_n \prod (x_n$ - $x_i) \cdot D_{n-1}$

1 $\leq$ i $\neq$ n

1 $\leq$ i $\neq$ n

$= \prod (x_n$ - $x_i) \cdot D_{n-1}^{(n-2)}$ + $x_n D_n$

$1\leq i\neq$ n

$= \prod_{i=1}^n (x_n$ - $x_i) \prod_{i=1}^n (x_{n-1}$ - $x_i) \cdot D_{n-2}^{(n-3)}$ + $\prod_{i=1}^n (x_n$ - $x_i) \prod_{i=1}^n (x_{n-1}$ - $x_i) \cdot x_{n-1}D_{n-2}$ + $x_nD_n$

1 $\leq$ i $\neq$ n-1

1 $\leq$ i $\neq$ n

1 $\leq$ i $\neq$ n-1

1 $\leq$ i $\neq$ n

$= \prod (x_n$ - $x_i) \prod (x_{n-1}$ - $x_i) \cdot D_{n-2}^{(n-3)}$ + $(x_{n-1}$ + $x_n)D_n$

$1\leq i\neq$ n

1 $\leq$ i $\neq$ n-1

$= \prod (x_n$ - $x_i) \cdots \prod (x_3$ - $x_i) \cdot D_2^{(1)}$ + $(x_3$ + $\cdots$ + $x_n)D_n$

1 $\leq$ i $\neq$ n

1 $\leq$ i $\neq$ 3

$= \prod (x_n$ - $x_i) \cdots \prod (x_3$ - $x_i)(x_2$ - $x_1)(x_1$ + $x_2)$ + $(x_3$ + $\cdots$ + $x_n)D_n$

$1\leq i\neq$ n

$1\leq i\neq$ 3

$= D_n \sum x_i$

$= D_n e_1(x_1,...,x_n)$.

Ta sẽ chứng minh $D_n^{(s)} = D_n e_{n-s}(x_1$, $\ldots$, $x_n) \forall$ n, 0 $\leq$ s $\leq$ n.

Khẳng định trên đúng với n $=$ 1, 2, 3.

Nếu khẳng định này đúng với n-1, $\forall$ 0 $\leq$ s $\leq$ n-1, ta cần chứng minh khẳng định vẫn



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

đúng với n, ∀ 0 ≤ s ≤ n.

$ \begin{vmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^{s-1} & x_1^{s+1} & \cdots & x_1^n \\ 1 & x_2 & x_2^2 & \cdots & x_2^{s-1} & x_2^{s+1} & \cdots & x_2^n \end{vmatrix} $

$ \begin{vmatrix} \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^{s-1} & x_n^{s+1} & \cdots & x_n^n \end{vmatrix} $

$ =\begin{vmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^{s-1} & x_1^{s+1} & \cdots & x_1^{n-1}(x_1 - x_n) \\ 1 & x_2 & x_2^2 & \cdots & x_2^{s-1} & x_2^{s+1} & \cdots & x_2^{n-1}(x_2 - x_n) \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^{s-1} & x_n^{s+1} & \cdots & 0 \end{vmatrix} \quad (c_s := c_s - x_n c_{s-1}) $

$ =\begin{vmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^{s-1} & x_1^{s-1}(x_1^2 - x_n^2) & \cdots & x_1^{n-1}(x_1 - x_n) \\ 1 & x_2 & x_2^2 & \cdots & x_2^{s-1} & x_2^{s-1}(x_2^2 - x_n^2) & \cdots & x_2^{n-1}(x_2 - x_n) \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \end{vmatrix} \quad (c_s := c_s - x_n c_{s-1}) $

$ \begin{array}{ccccccccc}\n1 & x_n & x_n^2 & \cdots & x_n^{s-1} & 0 & \cdots & 0\n\end{array} $

$ \begin{vmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^{s-2}(x_1-x_n) & x_1^{s-1}(x_1^2-x_n^2) & \cdots & x_1^{n-1}(x_1-x_n) \end{vmatrix} $

$ \begin{vmatrix} 1 & x_2 & x_2^2 & \cdots & x_2^{s-2}(x_2-x_n) & x_2^{s-1}(x_2^2-x_n^2) & \cdots & x_2^{n-1}(x_2-x_n) \end{vmatrix} $

$ \label{eq:3.1} \begin{split} \mathbb{E} \left[ \begin{array}{cccccccccccc} \mathbb{E} \left[ \begin{array}{cccccccc} \mathbb{E} \left[ \begin{array}{cccccccc} \mathbb{E} \left[ \begin{array}{cccccccc} \mathbb{E} \left[ \begin{array}{cccc} \mathbb{E} \left[ \begin{array}{cccc} \mathbb{E} \left[ \begin{array}{cccc} \mathbb{E} \left[ \begin{array}{cccc} \mathbb{E} \left[ \begin{array}{cccc} \mathbb{E} \left[ \begin{array}{cccc} \mathbb{E} \left[ \begin{array}{cccc} \mathbb{E} \left[ \begin{array}{cccc} \mathbb{E} \left[ $

$ \begin{vmatrix} 1 & x_n & x_n^2 & \cdots & 0 & 0 & \cdots & 0 \end{vmatrix} $

$ \begin{vmatrix} 1 & x_1 - x_n & x_1(x_1 - x_n) & \cdots & x_1^{s-2}(x_1 - x_n) & x_1^{s-1}(x_1^2 - x_n^2) & \cdots & x_1^{n-1}(x_1 - x_n) \end{vmatrix} $

$ \begin{vmatrix} 1 & x_2 - x_n & x_2(x_2 - x_n) & \cdots & x_2^{s-2}(x_2 - x_n) & x_2^{s-1}(x_2^2 - x_n^2) & \cdots & x_2^{n-1}(x_2 - x_n) \end{vmatrix} $

$ \begin{array}{|cccccccccccc|}\hline \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & $

$\ddot{\phantom{a}}$ .



$<u>UNUUNU$ 9. DINII TIIUU YA IID FIIUUNU TIUNII TUTEN $TINII</u>$

Khai triển Laplace theo dòng thứ n:

$ = (-1)^{n+1}(x_1 - x_n)(x_2 - x_n) \cdots (x_{n-1} - x_n)
\begin{vmatrix}\n1 & x_1 & \cdots & x_1^{s-2} & x_1^{s-1}(x_1 + x_n) & \cdots & x_1^{n-1} \\
1 & x_2 & \cdots & x_2^{s-2} & x_2^{s-1}(x_2 + x_n) & \cdots & x_2^{n-1} \\
\vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
1 & x_{n-1} & \cdots & x_{n-1}^{s-2} & x_{n-1}^{s-1}(x_{n-1} + x_n) & $

$ = (x_n - x_1) \cdots (x_n - x_{n-1})
\begin{vmatrix}\n1 & x_1 & \cdots & x_1^{s-2} & x_1^s & \cdots & x_1^{n-1} \\
1 & x_2 & \cdots & x_2^{s-2} & x_2^s & \cdots & x_2^{n-1} \\
\vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
1 & x_{n-1} & \cdots & x_{n-1}^{s-2} & x_{n-1}^s & \cdots & x_n^{n-1}\n\end{vmatrix} $

$ + (x_n - x_1) \cdots (x_n - x_{n-1}) x_n \begin{vmatrix} 1 & x_1 & \cdots & x_1^{s-1} & x_1^{s+1} & \cdots & x_1^{n-1} \\ 1 & x_2 & \cdots & x_2^{s-1} & x_2^{s+1} & \cdots & x_2^{n-1} \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n-1} & \cdots & x_{n-1}^{s-1} & x_{n-1}^{s+1} & \cdots & x_n^{n-1} \end{vmatrix} $

$= \prod (x_n$ - $x_i) \cdot \left( D_{n-1}^{(s-1)}$ + $x_n D_{n-1}^{(s)} \right)$

1 $\leq$ i $\neq$ n

$= \prod (x_n$ - $x_i) \cdot (D_{n-1}e_{n-s}(x_1$, $\ldots$, $x_{n-1})$ + $x_n D_{n-1}e_{n-1-s}(x_1$, $\ldots$, $x_{n-1}))$

$1\leq i\neq$ n

$= \prod (x_n$ - $x_i) \cdot D_{n-1} (e_{n-s}(x_1$, $\ldots$, $x_{n-1})$ + $x_n e_{n-1-s}(x_1$, $\ldots$, $x_{n-1}))$

$1\leq i\neq$ n

$= D_n e_{n-s}(x_1,\ldots,x_{n-1},x_n)$.

Phép chứng minh quy nạp hoàn tất.

Vây $D_n^{(s)} = D_n e_{n-s}(x_1$, $\ldots$, $x_n)$.

Ta kí hiệu các vector cột gồm n thành phần:

$ \alpha_0 = \begin{pmatrix} 1 \\ 1 \\ \vdots \end{pmatrix} \qquad \alpha_k = \begin{pmatrix} x_1^k \\ x_2^k \\ \vdots \end{pmatrix} $



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

$ Bài tập 3.23.
\begin{vmatrix} 1 & x_1(x_1 - 1) & x_1^2(x_1 - 1) & \cdots & x_1^{n-1}(x_1 - 1) \\ 1 & x_2(x_2 - 1) & x_2^2(x_2 - 1) & \cdots & x_2^{n-1}(x_2 - 1) \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n(x_n - 1) & x_n^2(x_n - 1) & \cdots & x_n^{n-1}(x_n - 1) \end{vmatrix}. $

Lời giải. Ta lần lượt thực hiện các biến đổi sau:

$ \begin{cases}\nc_n &:= c_n + c_{n-1} + \cdots + c_2 \\
c_{n-1} &:= c_{n-1} + c_{n-2} + \cdots + c_2 \\
\vdots & \\
c_3 &:= c_3 + c_2\n\end{cases} $

$ \begin{vmatrix} 1 & x_1(x_1 - 1) & x_1^2(x_1 - 1) & \cdots & x_1^{n-1}(x_1 - 1) \\ 1 & x_2(x_2 - 1) & x_2^2(x_2 - 1) & \cdots & x_2^{n-1}(x_2 - 1) \end{vmatrix} $

$ \begin{vmatrix} \vdots & \vdots & \ddots & \vdots \\ 1 & x_n(x_n-1) & x_n^2(x_n-1) & \cdots & x_n^{n-1}(x_n-1) \end{vmatrix} $

$ \begin{vmatrix} 1 & x_1^2 - x_1 & x_1^3 - x_1^2 & \cdots & x_1^n - x_1^{n-1} \end{vmatrix} \begin{vmatrix} 1 & x_1^2 - x_1 & x_1^3 - x_1 & \cdots & x_1^n - x_1 \end{vmatrix} $

$ =\begin{vmatrix} 1 & x_2^2-x_2 & x_2^3-x_2^2 & \cdots & x_2^n-x_2^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \end{vmatrix}=\begin{vmatrix} 1 & x_2^2-x_2 & x_2^3-x_2 & \cdots & x_2^n-x_2 \\ \vdots & \vdots & \vdots & \ddots & \vdots \end{vmatrix} $

$ \begin{vmatrix} 1 & x_n^2 - x_n & x_n^3 - x_n^2 & \cdots & x_n^n - x_n^{n-1} \end{vmatrix} \begin{vmatrix} 1 & x_n^2 - x_n & x_n^3 - x_n & \cdots & x_n^n - x_n \end{vmatrix} $

$=\det(\alpha_0,\alpha_2-\alpha_1,\alpha_3-\alpha_1,\ldots,\alpha_n-\alpha_1)$

$=\det(\alpha_0,\alpha_2,\alpha_3,\ldots,\alpha_n)+(\det(\alpha_0,-\alpha_1,\alpha_3,\ldots,\alpha_n)+\cdots+\det(\alpha_0,\alpha_2,\alpha_3,\ldots,\alpha_{n-1},-\alpha_1))$

$=D_ne_{n-1}(x_1,\ldots,x_n)+\sum_{n=0}^{\infty}(-1)^{s+1}D_n^{(s)}$

$=D_ne_{n-1}(x_1,\ldots,x_n)+\sum_{n=0}^{\infty}(-1)^{s+1}D_ne_{n-s}(x_1,\ldots,x_n)$

$=D_n\sum_{n=0}^{\infty}(-1)^{s+1}e_{n-s}(x_1,\ldots,x_n)$

$= D_n \sum_{n=1}^{\infty} (-1)^{s+1} e_{n-s}(x_1,\ldots,x_n)$ + $D_n \prod_{n=1}^{\infty} x_n$

$_{i=0}=D_n \prod_{i=1}^{n} x_i$ - $D_n \prod_{i=1}^{n} (x_i$ - 1).

$i=1$



DINII HIUV VA HE LIIUVING TIUNII TUTEN TINII

$ Bài tập 3.24.
\begin{vmatrix} 1+x_1 & 1+x_1^2 & \cdots & 1+x_1^n \\ 1+x_2 & 1+x_2^2 & \cdots & 1+x_2^n \\ \vdots & \vdots & \ddots & \vdots \\ 1+x_n & 1+x_n^2 & \cdots & 1+x_n^n \end{vmatrix}. $

Lời giải.

$ \begin{vmatrix} 1+x_1 & 1+x_1^2 & \cdots & 1+x_1^n \\ 1+x_2 & 1+x_2^2 & \cdots & 1+x_2^n \\ \vdots & \vdots & \ddots & \vdots \\ 1+x_n & 1+x_n^2 & \cdots & 1+x_n^n \end{vmatrix} = \begin{vmatrix} 1+x_1 & x_1^2-x_1 & \cdots & x_1^n-x_1 \\ 1+x_2 & x_2^2-x_2 & \cdots & x_2^n-x_2 \\ \vdots & \vdots & \ddots & \vdots \\ 1+x_n & x_n^2-x_n & \cdots & x_n^n-x_n \end{vmatrix} $

$ =\begin{vmatrix} 1 & x_1^2 - x_1 & \cdots & x_1^n - x_1 \\ 1 & x_2^2 - x_2 & \cdots & x_2^n - x_2 \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_n^2 - x_n & \cdots & x_n^n - x_n \end{vmatrix} + \begin{vmatrix} x_1 & x_1^2 - x_1 & \cdots & x_1^n - x_1 \\ x_2 & x_2^2 - x_2 & \cdots & x_2^n - x_2 \\ \vdots & \vdots & \ddots & \vdots \\ x_n & x_n^2 - x_n & \cdots & x_n^n - x_n \end{vmatrix} $

$ =\begin{vmatrix} 1 & x_1^2 - x_1 & \cdots & x_1^n - x_1 \\ 1 & x_2^2 - x_2 & \cdots & x_2^n - x_2 \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_n^2 - x_n & \cdots & x_n^n - x_n \end{vmatrix} + \begin{vmatrix} x_1 & x_1^2 & \cdots & x_1^n \\ x_2 & x_2^2 & \cdots & x_2^n \\ \vdots & \vdots & \ddots & \vdots \\ x_n & x_n^2 & \cdots & x_n^n \end{vmatrix} $

$= D_n \prod_{i=1}^n x_i$ - $D_n \prod_{i=1}^n (x_i$ - 1) + $D_n \prod_{i=1}^n x_i$

$= 2D_n \prod_{i=1}^{n} x_i$ - $D_n \prod_{i=1}^{n} (x_i$ - 1).

$ Bài tập 3.25.
\begin{vmatrix} 1 & \cos(\varphi_1) & \cos(2\varphi_1) & \cdots & \cos((n-1)\varphi_1) \\ 1 & \cos(\varphi_2) & \cos(2\varphi_2) & \cdots & \cos((n-1)\varphi_2) \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & \cos(\varphi_n) & \cos(2\varphi_n) & \cdots & \cos((n-1)\varphi_n) \end{vmatrix}. $

Lời giải. Áp dụng các công thức cộng, trừ cung:

$\cos(n\varphi) = \cos(\varphi$ + $(n-1)\varphi) = \cos(\varphi)\cos((n-1)\varphi)$ - $\sin(\varphi)\sin((n-1)\varphi)$

$=2\cos(\varphi)\cos((n-1)\varphi)-\cos((n-2)\varphi)$.

Dựa vào liên hệ này và nhận xét rằng $cos(0\varphi) =$ 1, $cos(\varphi) = cos(\varphi)$, ta có thể chứng minh quy

nạp được cho khẳng định:



VIIUVINU 9. DIINII TIIUV VA IIIJ I IIUVINU TIURIII TUTER TIINII

$\cos(n\varphi)$ là một đa thực bậc n với biến $\cos(\varphi)$, hệ số cao nhất là $2^{n-1}$.

$ \begin{vmatrix} 1 & \cos(\varphi_1) & \cos(2\varphi_1) & \cdots & \cos((n-1)\varphi_1) \\ 1 & \cos(\varphi_2) & \cos(2\varphi_2) & \cdots & \cos((n-1)\varphi_2) \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & \cos(\varphi_n) & \cos(2\varphi_n) & \cdots & \cos((n-1)\varphi_n) \end{vmatrix} = \begin{vmatrix} 1 & \cos(\varphi_1) & 2\cos(\varphi_1)^2 & \cdots & \cos((n-1)\varphi_1) \\ 1 & \cos(\varphi_2) & 2\cos(\varphi_2)^2 & $

$ \begin{vmatrix} 1 & \cos(\varphi_1) & 2\cos(\varphi_1)^2 & \cdots & 2^{n-2}\cos((n-1)\varphi_1) \\ 1 & \cos(\varphi_2) & 2\cos(\varphi_2)^2 & \cdots & 2^{n-2}\cos((n-1)\varphi_2) \\ \vdots & \vdots & \ddots & \vdots & \ddots \end{vmatrix} $

$ \begin{vmatrix} \cdots & \cdots & \cdots \\ 1 & \cos(\varphi_n) & 2\cos(\varphi_n)^2 & \cdots & 2^{n-2}\cos((n-1)\varphi_n) \end{vmatrix} $

$ =\frac{1}{2^{n-1}} \begin{vmatrix} 1 & 2\cos(\varphi_1) & 2^2\cos(\varphi_1)^2 & \cdots & 2^{n-1}\cos(\varphi_1)^{n-1} \\ 1 & 2\cos(\varphi_2) & 2^2\cos(\varphi_2)^2 & \cdots & 2^{n-1}\cos(\varphi_2)^{n-2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & 2\cos(\varphi_n) & 2^2\cos(\varphi_n)^2 & \cdots & 2^{n-1}\cos(\varphi_n)^{n-1} \end{vmatrix} $

$= \frac{1}{2^{n-1}} \prod_{i > j} 2(\cos(\varphi_i)$ - $\cos(\varphi_j))= 2^{(n-1)(n-2)/2} \prod(\cos(\varphi_i)$ - $\cos(\varphi_j))$.

$ Bài tập 3.26.
\begin{vmatrix} x_1y_1 & 1 + x_1y_2 & \cdots & 1 + x_1y_n \\ 1 + x_2y_1 & x_2y_2 & \cdots & 1 + x_2y_n \\ \vdots & \vdots & \ddots & \vdots \\ 1 + x_ny_1 & 1 + x_ny_2 & \cdots & x_ny_n \end{vmatrix} $

Bổ đề 3.27.

(i)

$ \begin{vmatrix} 0 & 1 & 1 & \cdots & 1 \\ 1 & 0 & 1 & \cdots & 1 \\ 1 & 1 & 0 & \cdots & 1 \\ \vdots & \vdots & \vdots & \ddots & \vdots \end{vmatrix} = (-1)^{n-1}(n-1). $

n $\times$ n



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

$ (ii) Thay cột thứ k của định thức trên bởi cột \begin{pmatrix} x_1 & x_2 & \cdots & x_n \end{pmatrix}^T thì định thức mới bằng: $

$(-1)^{n-1}\left((1-n)x_k+\sum_{i=1}^n x_i\right)$

Chứng minh bổ đề.

(i)

$ \begin{vmatrix} 0 & 1 & 1 & \cdots & 1 \\ 1 & 0 & 1 & \cdots & 1 \\ 1 & 1 & 0 & \cdots & 1 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & 1 & 1 & \cdots & 0 \end{vmatrix} = \begin{vmatrix} 0 & 1 & 1 & \cdots & 1 \\ 1 & -1 & 0 & \cdots & 0 \\ 1 & 0 & -1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & 0 & 0 & \cdots & -1 \end{vmatrix} \quad (r_i := r_i - r_1) $

$ \begin{vmatrix} n-1 & 1 & 1 & \cdots & 1 \\ 0 & -1 & 0 & \cdots & 0 \\ 0 & 0 & -1 & \cdots & 0 \end{vmatrix} = (-1)^{n-1}(n-1). $

$ \begin{bmatrix} \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & -1 \end{bmatrix} $

Trường hợp k $=$ 1:

(ii)

$ \begin{vmatrix} x_1 & 1 & 1 & \cdots & 1 \\ x_2 & 0 & 1 & \cdots & 1 \\ x_3 & 1 & 0 & \cdots & 1 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ x_n & 1 & 1 & \cdots & 0 \end{vmatrix} = \begin{vmatrix} x_1 & 1 & 1 & \cdots & 1 \\ x_2 - x_1 & -1 & 0 & \cdots & 0 \\ x_3 - x_1 & 0 & -1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ x_n - x_1 & 0 & 0 & \cdots & -1 \end{vmatrix} \quad (r_i := r_i - r_ $

$ =\begin{vmatrix} (1-n)x_1+\sum_{i=1}^n x_i & 0 & 0 & \cdots & 0 \\ x_2-x_1 & -1 & 0 & \cdots & 0 \\ x_3-x_1 & 0 & -1 & \cdots & 0 \end{vmatrix} (r_1 := r_1 + \sum_{i=2}^n r_i) $

$ \begin{bmatrix} 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & $

$x_n$ - $x_1$ 0 0 $\cdots$ -1

$= (-1)^{n-1} \left( (1-n)x_1$ + $\sum_{i=1}^n x_i \right)$.



VIIUVINU 9. DIINII TIIUV VA IID I IIUVINU TIIIINII TUTEN TIINII

Trường hợp k $\neq$ 1:

$ \begin{vmatrix} 0 & 1 & \cdots & x_1 & \cdots & 1 \\ 1 & 0 & \cdots & x_2 & \cdots & 1 \\ \vdots & \vdots & \ddots & \vdots & \ddots & 1 \\ 1 & 1 & \cdots & x_k & \cdots & 1 \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 1 & 1 & \cdots & x_n & \cdots & 0 \end{vmatrix} = \begin{vmatrix} x_1 & 1 & \cdots & 0 & \cdots & 1 \\ x_2 & 0 & \cdots & 1 & \cdots & 1 \\ \vdots & \vdots & \ddots & \vdots & \ddots & 1 \\ x_k & 1 & \cd $

$ =\begin{vmatrix} x_k & 1 & \cdots & 1 & \cdots & 1\\ x_2 & 0 & \cdots & 1 & \cdots & 1\\ \vdots & \vdots & \ddots & \vdots & \ddots & 1\\ x_1 & 1 & \cdots & 0 & \cdots & 1\\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots\\ x_n & 1 & \cdots & 1 & \cdots & 0 \end{vmatrix} \quad (r_1 \leftrightarrow r_k) $

$= (-1)^{n-1} \left( (1-n)x_k$ + $\sum_{i=1}^n x_i \right)$ (áp dụng trường hợp k $=$ 1)

Lời giải.

$ \begin{vmatrix} x_1y_1 & 1 + x_1y_2 & \cdots & 1 + x_1y_n \\ 1 + x_2y_1 & x_2y_2 & \cdots & 1 + x_2y_n \end{vmatrix} $

$ \begin{vmatrix} \vdots & \vdots & \ddots & \vdots \\ 1 + x_n y_1 & 1 + x_n y_2 & \cdots & x_n y_n \end{vmatrix} $

$ \begin{pmatrix} 0 \\ 1 \\ \vdots \\ 1 \end{pmatrix} + y_1 \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x \end{pmatrix}, \dots, \begin{pmatrix} 1 \\ 1 \\ \vdots \\ 0 \end{pmatrix} + y_n \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x \end{pmatrix} $

$ =\begin{vmatrix} 0 & 1 & \cdots & 1 \\ 1 & 0 & \cdots & 1 \\ \vdots & \vdots & \ddots & \vdots \\ 1 & 1 & \cdots & 0 \end{vmatrix} + \sum_{k=1}^{n} y_k \begin{vmatrix} 0 & 1 & \cdots & x_1 & \cdots & 1 \\ 1 & 0 & \cdots & x_2 & \cdots & 1 \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 1 & 1 & \cdots & x_k & \cdots & 1 \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 1 & 1 & \cdots & x_n & \cdots & 0 \end{vmatrix} $



VIIUVINU 0. DIINII TIIUV VA IID I IIUVINU TIIIINII TUTEN TIINII

$=(-1)^{n-1}(n-1)+(-1)^{n-1}\sum_{k=1}^n y_k\left((1-n)x_k+\sum_{i=1}^n x_i\right)$

$=(-1)^{n-1}(n-1)+(-1)^{n-1}\left(\sum_{i=1}^{n}x_{i}\right)\left(\sum_{i=1}^{n}y_{i}\right)-(-1)^{n-1}(n-1)\sum_{i=1}^{n}x_{i}y_{i}$.

$ Bài tập 3.28. C_n = \begin{vmatrix} (a_1 + b_1)^{-1} & (a_1 + b_2)^{-1} & \cdots & (a_1 + b_n)^{-1} \ (a_2 + b_1)^{-1} & (a_2 + b_2)^{-1} & \cdots & (a_2 + b_n)^{-1} \ \vdots & \vdots & \ddots & \vdots \ (a_n + b_1)^{-1} & (a_n + b_2)^{-1} & \cdots & (a_n + b_n)^{-1} \end{vmatrix}. $

$L\delta$ i giải.

$ \begin{vmatrix} (a_1 + b_1)^{-1} & (a_1 + b_2)^{-1} & \cdots & (a_1 + b_n)^{-1} \ (a_2 + b_1)^{-1} & (a_2 + b_2)^{-1} & \cdots & (a_2 + b_n)^{-1} \end{vmatrix} $

$\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{L}(\mathcal{$

$|(a_n$ + $b_1)^{-1} (a_n$ + $b_2)^{-1} \cdots (a_n$ + $b_n)^{-1}|$

$\left| (b_n$ - $b_1)(a_1$ + $b_1)^{-1}(a_1$ + $b_n)^{-1} \right| (b_n$ - $b_2)(a_1$ + $b_2)^{-1}(a_1$ + $b_n)^{-1} \cdots (a_1$ + $b_n)^{-1} \right|$

$ \begin{vmatrix} (b_n-b_1)(a_2+b_1)^{-1}(a_2+b_n)^{-1} & (b_n-b_2)(a_2+b_2)^{-1}(a_2+b_n)^{-1} & \cdots & (a_2+b_n)^{-1} \\ \vdots & \vdots & \ddots & \vdots \end{vmatrix} (c_i := c_i - c_n) $

$\left| (b_n$ - $b_1)(a_n$ + $b_1)^{-1}(a_n$ + $b_n)^{-1} \right| (b_n$ - $b_2)(a_n$ + $b_2)^{-1}(a_n$ + $b_n)^{-1} \cdots (a_n$ + $b_n)^{-1} \right|$

$ =\prod_{1 \leq i &lt; n}^{n} (b_n - b_i) \prod_{i=1}^{n} (a_i + b_n)^{-1} \begin{vmatrix} (a_1 + b_1)^{-1} &amp; (a_1 + b_2)^{-1} &amp; \cdots &amp; 1 \\ (a_2 + b_1)^{-1} &amp; (a_2 + b_2)^{-1} &amp; \cdots &amp; 1 \\ \vdots &amp; \vdots &amp; \ddots &amp; \vdots \end{vmatrix} $

$ =\prod_{1\leq i<n}^{n} (b_n-b_i) \prod_{i=1}^{n} (a_i+b_n)^{-1} \begin{vmatrix} (a_n-a_1)(a_1+b_1)^{-1}(a_n+b_1)^{-1} & (a_n-a_1)(a_1+b_2)^{-1}(a_n+b_2)^{-1} & \cdots & 0 \\ (a_n-a_2)(a_2+b_1)^{-1}(a_n+b_1)^{-1} & (a_n-a_2)(a_2+b_2)^{-1}(a_n+b_2)^{-1} & \cdots & 0 \end{vmatrix} $

$|(a_n$ + $b_1)^{-1} (a_n$ + $b_2)^{-1}$ ... 1

$(a_n$ + $b_2)^{-1}$

$(a_n$ + $b_1)^{-1}$

Ap dụng khai triển Laplace cho cột thứ n và tách nhân tử chung:

$= \prod_{i=1}^{n} (b_{n}$ - $b_{i}) \prod_{i=1}^{n} (a_{i}$ + $b_{n})^{-1} \prod_{i=1}^{n} (a_{n}$ - $a_{i}) \prod_{i=1}^{n} (a_{n}$ + $b_{i})^{-1}$

$1\leq i\leq$ n

1 $\leq$ i $<$ n

$i=1$



VIIUVINU 0. DIINII TIIUV VA IID I IIUVINU TIIIINII TUTEN TIINII

$ \times \begin{vmatrix} (a_1 + b_1)^{-1} & (a_1 + b_2)^{-1} & \cdots & (a_1 + b_{n-1})^{-1} \\ (a_2 + b_1)^{-1} & (a_2 + b_2)^{-1} & \cdots & (a_2 + b_{n-1})^{-1} \\ \vdots & \vdots & \ddots & \vdots \\ (a_{n-1} + b_1)^{-1} & (a_{n-1} + b_2)^{-1} & \cdots & (a_{n-1} + b_{n-1})^{-1} \end{vmatrix} $

Từ hệ thức truy hồi trên, và nhận xét $C_1 = (a_1$ + $b_1)^{-1}$, ta được:

$C_n = \prod_{i > j} (a_i$ - $a_j)(b_i$ - $b_j) \times \prod_{i \neq j} (a_i$ + $b_j)^{-1}$.

Bài tập 3.29. Dãy Fibonacci là dãy số bắt đầu với các số hạng 1, 2 và mỗi số hạng, kế từ số hạng

thứ ba, đều bằng tổng của hai số hạng đứng ngay trước nó. Chứng minh rằng số hạng thứ n của

dãy Fibonacci bằng định thức cỡ n sau đây:

1 $\quad$ 0 $\quad \cdots \quad$ 0 $\quad$ 0

$ \begin{bmatrix} -1 & 1 & 1 & \cdots & 0 & 0 \\ 0 & -1 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & -1 & 1 \end{bmatrix}. $

Lời giải.

$F_1 =$ 1 $=$ |1|

$ F_2 = 2 = \begin{vmatrix} 1 & 1 \\ -1 & 1 \end{vmatrix} $

Ta chứng minh bằng quy nạp, giả sử đẳng thức đúng đến n-1.

Với n $>$ 2, áp dụng khai triển Laplace cho hàng thứ nhất:

$ \begin{vmatrix} 1 & 1 & 0 & \cdots & 0 & 0 \\ -1 & 1 & 1 & \cdots & 0 & 0 \\ 0 & -1 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \end{vmatrix} = \begin{vmatrix} 1 & 1 & 0 & \cdots & 0 & 0 \\ -1 & 1 & 1 & \cdots & 0 & 0 \\ 0 & -1 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \end{vmatrix} + (-1)^{1+2} \begin{vmatrix} -1 & 1 & 0 & \cdots & 0 & 0 \\ - $

$\overline{0}$

0

$(n-1)\times(n-1)$

$(n-2)\times(n-2)$

$n\!\times\!n$



VIIUVINU 9. DIINII TIIUV VA IIIJ I IIUVINU TIURIII TUTER TIINII

$ =\begin{vmatrix} 1 & 1 & 0 & \cdots & 0 & 0 \\ -1 & 1 & 1 & \cdots & 0 & 0 \\ 0 & -1 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & -1 & 1 \end{vmatrix}+\begin{vmatrix} 1 & 1 & 0 & \cdots & 0 & 0 \\ -1 & 1 & 1 & \cdots & 0 & 0 \\ 0 & -1 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & -1 & 1 \end{vm $

$(n-1)\times$ (n-1) $(n-2)\times$ (n-2)

$= F_{n-1}$ + $F_{n-2}$

$= F_n$.

Vậy giả thiết quy nạp đúng, ta có được điều phải chứng minh.

Bài tập 3.30. Tính định thức sau đây bằng cách viết nó thành tích của hai định thức:

$ \begin{vmatrix} s_0 & s_1 & s_2 & \cdots & s_{n-1} & 1 \\ s_1 & s_2 & s_3 & \cdots & s_n & x \end{vmatrix} $

$ \begin{vmatrix} s_2 & s_3 & s_4 & \cdots & s_{n+1} & x^2 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ s_n & s_{n+1} & s_{n+2} & \cdots & s_{2n-1} & x^n \end{vmatrix} $

trong đó $s_k = \sum_i x_i^k$.

Lời giải.

$ \begin{pmatrix} s_0 & s_1 & s_2 & \cdots & s_{n-1} & 1 \\ s_1 & s_2 & s_3 & \cdots & s_n & x \\ s_2 & s_3 & s_4 & \cdots & s_{n+1} & x^2 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ s_n & s_{n+1} & s_{n+2} & \cdots & s_{2n-1} & x^n \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 & \cdots & 1 & 1 \\ x_1 & x_2 & x_3 & \cdots & x_n & x \\ x_1^2 & x_2^2 & x_3^2 & \cdots & x_n^2 & x^2 \\ \ $

$ \begin{vmatrix} s_0 & s_1 & s_2 & \cdots & s_{n-1} & 1 \\ s_1 & s_2 & s_3 & \cdots & s_n & x \\ s_2 & s_3 & s_4 & \cdots & s_{n+1} & x^2 \end{vmatrix} = \prod (x_i - x_j) \prod_{i=1}^n (x_i - x_i) = \prod_{i>i} (x_i - x_j)^2 \prod_{i=1}^n (x - x_i). $

i $>$ j

$i=1$

i $>$ j

i $>$ j

$\{x_{i}^{(i)}\}_{i=1}^{n}$ , $\{x_{i}^{(i)}\}_{i=1}^{n}$ , $\{x_{i}^{(i)}\}_{i=1}^{n}$

$s_{n+2} \cdots s_{2n-1}$



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

Bài tập 3.31. Chứng minh rằng

$ \begin{vmatrix} a_1 & a_2 & a_3 & \cdots & a_n \\ a_n & a_1 & a_2 & \cdots & a_{n-1} \\ a_{n-1} & a_n & a_1 & \cdots & a_{n-2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_2 & a_3 & a_4 & \cdots & a_1 \end{vmatrix} = f(\varepsilon_1) f(\varepsilon_2) \cdots f(\varepsilon_n), $

trong đó, f(X) $= a_1$ + $a_2X$ + $\cdots$ + $a_nX^{n-1}$ và $\varepsilon_1$, $\varepsilon_2$, $\ldots$, $\varepsilon_n$ là các căn bậc n khác nhau của 1.

Chúng minh.

$ \begin{pmatrix} a_1 & a_2 & a_3 & \cdots & a_n \\ a_n & a_1 & a_2 & \cdots & a_{n-1} \\ a_{n-1} & a_n & a_1 & \cdots & a_{n-2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \end{pmatrix} \begin{pmatrix} 1 \\ \varepsilon_k \\ \varepsilon_k^2 \\ \vdots \\ \vdots \end{pmatrix} = \begin{pmatrix} f(\varepsilon_k) \\ \varepsilon_k f(\varepsilon_k) \\ \varepsilon_k^2 f(\varepsilon_k) \\ \vdots \\ \vdots \end{pmatrix} = f(\varepsilon_k) \begin{pmatrix} 1 \\ \varepsilon_k \\ \varepsilon_k^2 \\ $

$ \begin{pmatrix} a_2 & a_3 & a_4 & \cdots & a_1 \end{pmatrix} \begin{pmatrix} \varepsilon_k^{n-1} \end{pmatrix} \begin{pmatrix} \varepsilon_k^{n-1} f(\varepsilon_k) \end{pmatrix} \begin{pmatrix} \varepsilon_k^{n-1} \end{pmatrix} $

$ \implies \begin{pmatrix} a_1 & a_2 & a_3 & \cdots & a_n \\ a_n & a_1 & a_2 & \cdots & a_{n-1} \\ a_{n-1} & a_n & a_1 & \cdots & a_{n-2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_2 & a_3 & a_4 & \cdots & a_1 \end{pmatrix} \begin{pmatrix} 1 & 1 & \cdots & 1 \\ \varepsilon_1 & \varepsilon_2 & \cdots & \varepsilon_n \\ \varepsilon_1^2 & \varepsilon_2^2 & \cdots & \varepsilon_n^2 \\ \vdots & \vdots & \ddots & \vdots \\ \varepsilon_1^{n-1} $

Bên cạnh đó

$ \begin{vmatrix}\n1 & 1 & \cdots & 1 \\
\varepsilon_1 & \varepsilon_2 & \cdots & \varepsilon_n \\
\varepsilon_1^2 & \varepsilon_2^2 & \cdots & \varepsilon_n^2 \\
\vdots & \vdots & \ddots & \vdots \\
\varepsilon_1^{n-1} & \varepsilon_2^{n-1} & \cdots & \varepsilon_n^{n-1}\n\end{vmatrix} = \prod_{i>j}(\varepsilon_i - \varepsilon_j) \neq 0 $

nên ma trận

$ \begin{pmatrix} 1 & 1 & \cdots & 1 \\ \varepsilon_1 & \varepsilon_2 & \cdots & \varepsilon_n \end{pmatrix} $

$\varepsilon_1^2 \varepsilon_2^2 \cdots \varepsilon_n^2 \vdots \varepsilon_1^{n-1} \varepsilon_2^{n-1} \cdots \varepsilon_n^{n-1} \varepsilon_n^{n-1} \varepsilon_n^{n-1}$



VIIUVINU 9. DIINII TIIUV VA IID I IIUVINU TIIIINII TUTEN TIINII

khả nghịch, suy ra

$ \begin{vmatrix} a_1 & a_2 & a_3 & \cdots & a_n \\ a_n & a_1 & a_2 & \cdots & a_{n-1} \\ a_{n-1} & a_n & a_1 & \cdots & a_{n-2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_2 & a_3 & a_4 & \cdots & a_1 \end{vmatrix} \begin{vmatrix} 1 & 1 & \cdots & 1 \\ \varepsilon_1 & \varepsilon_2 & \cdots & \varepsilon_n \\ \varepsilon_1^2 & \varepsilon_2^2 & \cdots & \varepsilon_n^2 \\ \vdots & \vdots & \ddots & \vdots \\ \varepsilon_1^{n-1} & \v $

$ \begin{array}{c|cccc}\n & a_1 & a_2 & a_3 & \cdots & a_n \\
a_n & a_1 & a_2 & \cdots & a_{n-1} \\
a_{n-1} & a_n & a_1 & \cdots & a_{n-2} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a_2 & a_3 & a_4 & \cdots & a_1\n\end{array} = \prod_{i=1}^n f(\varepsilon_i). $

Bài tập 3.32. Dùng khai triển Laplace chứng minh rằng nếu một định thức cỡ n có các yếu tố

nằm trên giao của k hàng và $\ell$ cột xác định nào đó đều bằng 0, trong đó k + $\ell >$ n, thì định thức

$\mathrm{d}\acute{o}$ bằng $\mathrm{0}$.

Chứng minh. Khi đổi chỗ các hàng, hay đổi chỗ các cột thì giá trị định thức chỉ đổi dấu.

Do đó, không mất tính tổng quát, ta có thể giả sử các yếu tố nằm trên giao của k hàng đầu

tiên và $\ell$ cột đầu tiên đều bằng 0.

Ma trận khi đó có dạng sau:

$ A = \left( \begin{array}{ccccc} 0 & 0 & \cdots & 0 & a_{1(\ell+1)} & \cdots & a_{1n} \\ 0 & 0 & \cdots & 0 & a_{2(\ell+1)} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & a_{k(\ell+1)} & \cdots & a_{kn} \\ a_{(k+1)1} & a_{(k+1)2} & \cdots & a_{(k+1)\ell} & a_{(k+1)(\ell+1)} & \cdots & a_{(k+1)n} \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & $

Áp dụng khai triển Laplace cho k hàng đầu tiên

det A $= \sum_{m=1$, ..., $k} (-1)^{1+...+k+j_1+...+j_k} D^{j_1,...,j_k}_{1,...,k} \overline{D}^{j_1,...,j_k}_{1,...,k}$.

1 $\leq i_1 \leq \cdots \leq i_k \leq$ n

Giả sử trong các cột 1 $\leq j_1 < \cdots < j_k \leq$ n, không có cột nào thuộc $\ell$ cột đầu tiên. Như vậy,

số cột của ma trận A sẽ lớn hơn hoặc bằng k + $\ell$, tức là n $\geq$ k + $\ell$. Điều này mâu thuẫn với giả

thiết k + $\ell >$ n.



VIIUVINU 9. DINII TIIUV VA IID I IIUVINU TIUINII TUTEN TIINII

Do đó, trong các $cột1\leq j_1<\cdots< j_k\leq$ n, có ít nhất một cột $thuộc\ellcột$ đầu tiên. Điều này

dẫn tới việc, bất kể chọnkcột nào thì giá trị của định thức $conD^{j_1,\dots,j_k}_{1,\dots,k}$ bằng không.

Vậy det $A=0$.

Bài tập 3.33. Giải hệ phương trình sau đây bằng phương pháp Cramer và phương pháp khử:

$3x_1$ + $4x_2$ + $x_3$ + $2x_4$ + 3 $=$ 0,

$3x_1$ + $5x_2$ + $3x_3$ + $5x_4$ + 6 $=$ 0,

$6x_1$ + $8x_2$ + $x_3$ + $5x_4$ + 8 $=$ 0,

$3x_1$ + $5x_2$ + $3x_3$ + $7x_4$ + 8 $=$ 0.

Lời giải. Sử dụng công thức Cramer.

Định thức của ma trận hệ số:

$ det A = \begin{vmatrix} 3 & 4 & 1 & 2 \\ 3 & 5 & 3 & 5 \\ 6 & 8 & 1 & 5 \end{vmatrix} = \begin{vmatrix} 3 & 4 & 1 & 2 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & -1 & 1 \end{vmatrix} $

$ \begin{vmatrix} 0 & 1 \end{vmatrix} $

$5\overline{)}$

|7|

$\overline{2}$

$\overline{3}$

$5\overline{)}$

3

$|3\rangle$

$ \begin{array}{cc} 2 & 3 \\ -1 & 1 \end{array} $

$=-6$.

$\overline{2}$

$\overline{0}$

Áp dụng công thức Cramer

-6 5 3 5

-8

1 $\quad$ 5

8

$\frac{-12}{-} =$ 2,

-8 5 3 7

$x_1 =$

$\det$ A

|3|

$\sqrt{3}$

-6 3 5

$ \begin{vmatrix} 6 & -8 & 1 & 5 \end{vmatrix} $

$ x_2 = \frac{\begin{vmatrix} 3 & -8 & 3 & 7 \end{vmatrix}}{\det A} = \frac{12}{-6} = -2, $



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

$ \begin{vmatrix} 3 & 4 & -3 & 2 \\ 3 & 5 & -6 & 5 \\ 6 & 8 & -8 & 5 \\ 3 & 5 & -8 & 7 \\ \hline \end{vmatrix} = \frac{-6}{-6} = 1, $

$x_3 =$

$\det$ A

$ \begin{vmatrix} 3 & 4 & 1 & -3 \\ 3 & 5 & 3 & -6 \\ 6 & 8 & 1 & -8 \\ 3 & 5 & 3 & -8 \end{vmatrix} = \frac{6}{6} = -1. $

$\det$ A

Sử dụng phương pháp khử.

$ \begin{pmatrix} 3 & 4 & 1 & 2 & -3 \\ 3 & 5 & 3 & 5 & -6 \\ 3 & 3 & 5 & 5 & -6 \end{pmatrix} \Leftrightarrow \begin{pmatrix} 3 & 4 & 1 & 2 & -3 \\ 0 & 1 & 2 & 3 & -3 \\ 0 & 0 & 1 & 1 & 2 \end{pmatrix} \Leftrightarrow \begin{pmatrix} 3 & 4 & 1 & 2 & -3 \\ 0 & 1 & 2 & 3 & -3 \\ 0 & 0 & 1 & 1 & 2 \end{pmatrix} $

$ \begin{bmatrix} 6 & 8 & 1 & 5 & -8 \\ 3 & 5 & 3 & 7 & -8 \end{bmatrix} (0 0 -1 1 -2 )0 0 -1 1 -2 (0 0 -1 1 -2 ) $

Suy ra $x_4 =$ -1, $x_3 =$ 1, $x_2 =$ -2, $x_1 =$ 2.

Bài tập 3.34. Chứng minh rằng một đa thức bậc n trong $\mathbb{F}[X]$ được hoàn toàn xác định bởi giá

trị của nó lại (n+1) điểm khác nhau của trường $\mathbb$ F. Tìm ví dụ về hai đa thức khác nhau cùng bậc

n nhận các giá trị bằng nhau tại mọi điểm của $\mathbb{F}$, nếu số phần tử của $\mathbb{F}$ không vượt quá n.

Lời giải. Giả sử ta có n+1 cặp giá trị $(x_i$, $y_i)$, trong đó i $\in \{0;$ 1; $\ldots; n\}$ sao cho $x_i \neq x_j$, $\forall$ i $\neq$ j.

Một đa thức f(X) $= a_0$ + $a_1X$ + $\cdots$ + $a_nX^n$ bậc n thỏa mãn $f(x_i) = y_i$, $\forall$ i nếu và chỉ nếu hệ

phương trình tuyến tính sau có nghiệm

$a_0$ + $a_1 x_0$ + $\cdots$ + $a_n x_0^n = y_0$

$a_0$ + $a_1 x_1$ + $\cdots$ + $a_n x_1^n = y_1$

$a_0$ + $a_1 x_2$ + $\cdots$ + $a_n x_2^n = y_2$

$\ddot{\cdot}$

$a_0$ + $a_1 x_n$ + $\cdots$ + $a_n x_n^n = y_n$

Hệ phương trình tuyến tính này có(n+1)ẩn $a_0$, $a_1$, $\ldots$, $a_nvà$ (n+1) phương trình. Bên cạnh

đó, hệ này có ma trận hệ số là ma trận Vandermonde của (n + 1) biến đôi một khác nhau, tức là

định thức của ma trận hệ số khác không.



VIIUVINU 9. DIINII TIIUV VA IIIJ I IIUVINU TIURIII TUTER TIINII

Do đó hệ phương trình tuyến tính trên có nghiệm duy nhất. Điều này cũng chứng tỏ đa thức

f(X) bậc n được xác định duy nhất bởi giá trị của nó tại (n+1) điểm khác nhau.

Với trường $\mathbb{F}_2$, hai đa thức phân biệt sau

$ \begin{cases} f(X) = 0, \\ q(X) = X(X - 1). \end{cases} $

luôn cùng nhận giá trị 0 tại mọi điểm của $\mathbb{F}_2$.

$\mathcal{L}_{\mathcal{A}}$

Giải các hệ phương trình sau đây bằng phương pháp thích hợp:

Bài tập 3.35.

ax + by + cz + dt $=$ p,-bx + ay + dz - ct $=$ q,

-cx - dy + az + bt $=$ r,

-dx + cy - bz + at $=$ s.

Lời giải. Ta tính định thức của ma trận hệ số

$ \begin{vmatrix} a & b & c & a \\ -b & a & d & -c \\ -c & -d & a & b \\ -d & a & b & c \end{vmatrix} = (-1)^{1+2+1+2} \begin{vmatrix} a & b \\ -b & a \end{vmatrix} \begin{vmatrix} a & b \\ -b & a \end{vmatrix} + (-1)^{1+2+1+3} \begin{vmatrix} a & b \\ -c & -d \end{vmatrix} \begin{vmatrix} d & -c \\ -b & a \end{vmatrix} + (-1)^{1+2+1+4} \begin{vmatrix} a & b \\ -d & c \end{vmatrix} \begin{vmatrix} d & -c \\ -d & c \end{vmatrix} $

$ +(-1)^{1+2+2+3}\begin{vmatrix}-b&a\\-c&-d\end{vmatrix}\begin{vmatrix}c&d\\-b&a\end{vmatrix}+(-1)^{1+2+2+4}\begin{vmatrix}-b&a\\-d&c\end{vmatrix}\begin{vmatrix}c&d\\a&b\end{vmatrix}+(-1)^{1+2+3+4}\begin{vmatrix}-c&-d\\-d&c\end{vmatrix}\begin{vmatrix}c\\d&c\end{vmatrix} $

$= (a^{2}$ + $b^{2})^{2}$ + (ad - $bc)^{2}$ + (ac + $bd)^{2}$ + (ac + $bd)^{2}$ + (bc - $ad)^{2}$ + $(c^{2}$ + $d^{2})^{2}$

$(a^{2}+b^{2})^{2}+ (c^{2}+d^{2})^{2}+2(ac+bd)^{2}+2(ad-bc)^{2}$

$=(a^2+b^2)^2+(c^2+d^2)^2+2(a^2+b^2)(c^2+d^2)$

$=(a^2+b^2+c^2+d^2)^2$.

Nếu $a^2$ + $b^2$ + $c^2$ + $d^2 \neq$ 0 thì hệ phương trình tuyến tính trên có nghiệm duy nhất:

$ x_1 = \frac{1}{(a^2 + b^2 + c^2 + d^2)^2} \begin{vmatrix} p & b & c & a \ q & a & d & -c \ r & -d & a & b \ s & c & -b & a \end{vmatrix}, $



VIIUVINU 0. DIINII TIIUV VA IID I IIUVINU TIIIINII TUTEN TIINII

$ x_2 = \frac{1}{(a^2 + b^2 + c^2 + d^2)^2} \begin{vmatrix} a & p & c & d \ -b & q & d & -c \ -c & r & a & b \ -d & s & -b & a \end{vmatrix}, $

$ x_3 = \frac{1}{(a^2 + b^2 + c^2 + d^2)^2} \begin{vmatrix} a & b & p & d \\ -b & a & q & -c \\ -c & -d & r & b \\ -d & c & s & a \end{vmatrix}, $

$ x_4 = \frac{1}{(a^2 + b^2 + c^2 + d^2)^2} \begin{vmatrix} a & b & c & p \ -b & a & d & q \ -c & -d & a & r \ -d & c & -b & e \end{vmatrix}. $

Ngược lại, nếu $a^2$ + $b^2$ + $c^2$ + $d^2 =$ 0 thì a $=$ b $=$ c $=$ d $=$ 0. Nếu (p, q, r, s) $\neq$ (0, 0, 0, 0) thì hệ

phương trình vô nghiệm, ngược lại, tập nghiệm của hệ phương trình là $\mathbb{R}^4$.

Bài tập 3.36.

$x_n$ + $a_1x_{n-1}$ + $a_1^2x_{n-2}$ + $\cdots$ + $a_1^{n-1}x_1$ + $a_1^n =$ 0

$x_n$ + $a_2x_{n-1}$ + $a_2^2x_{n-2}$ + $\cdots$ + $a_2^{n-1}x_1$ + $a_2^n =$ 0

$x_n$ + $a_n x_{n-1}$ + $a_n^2 x_{n-2}$ + $\cdots$ + $a_n^{n-1} x_1$ + $a_n^n =$ 0

Lời giải. A là ma trận hệ số của hệ phương trình tuyến tính trên.

Như vậy A là một ma trận Vandermonde.

Trường hợp 1. $a_1$, $a_2$, $\ldots a_n$ đôi một khác nhau.

Lúc này, định thức Vandermonde của nó khác không.

Áp dụng công thức Cramer:

$x_{n-k} = \frac{\det A_k}{\det A}$

$ \begin{pmatrix} a_1^k \\ 1 \end{pmatrix} \qquad \begin{pmatrix} -a_1^n \\ 1 \end{pmatrix} $

$ \mathcal{A} \cup \left[ \begin{array}{c} a_2^k \ \vdots \ a_k \end{array} \right] \ \text{b} \ddot{\mathcal{O}} \text{i} \ \text{ } \left[ \begin{array}{c} \end{array} \right] $

trong $đó\mathcal{A}_klà$ ma $trận\mathcal{A}$ sau khi thay cột



VIIUVINU 0. DIINII TIIUV VA IID I IIUVINU TIIIINII TUTEN TIINII

Sử dụng kết quả từ bài toán 3.22:

$ det A_k = (-1)(-1)^{n-k-1}
\begin{vmatrix} 1 & a_1 & \cdots & a_1^{k-1} & a_1^{k+1} & \cdots & a_1^n \\ 1 & a_1 & \cdots & a_1^{k-1} & a_1^{k+1} & \cdots & a_1^n \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 1 & a_1 & \cdots & a_1^{k-1} & a_1^{k+1} & \cdots & a_1^n \end{vmatrix} = (-1)^{n-k} D_n e_{n-k}. $

Suy ra $x_{n-k} = (-1)^{n-k} e_{n-k}(a_1$, $\ldots$, $a_n)$.

$ \left\{ \begin{aligned} x_1 &= (-1)e_1(a_1,\ldots,a_n) \ x_2 &= (-1)^2 e_2(a_1,\ldots,a_n) \ &\vdots \ x_n &= (-1)^n e_n(a_1,\ldots,a_n) \end{aligned} \right. $

trong đó, nhắc lại rằng $e_k$ là đa thức đối xứng sơ cấp bậc k.

Trường hợp 2. Trong n hệ số $a_1$, $a_2$, $\ldots a_n$, có ít nhất hai hệ số bằng nhau.

Giả sử rằng, sau khi loại bỏ các hệ số dư thừa, ta còn lại m hệ số (m $<$ n). Không giảm

tổng quát, có thể đánh số lại các hệ số. m hệ số đôi một khác nhau được đánh số lại là $a_1$,

$a_2$, $\ldots a_m$.

Thực hiện các phép biến đổi sơ cấp trên các hàng của ma trận m $\times$ (n + 1) sau:

$ \begin{pmatrix} 1 & a_1 & a_1^2 & \cdots & a_1^{n-1} & a_1^n \ 1 & a_2 & a_2^2 & \cdots & a_2^{n-1} & a_2^n \ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \ 1 & a_m & a_m^2 & \cdots & a_m^{n-1} & a_m^n \end{pmatrix} $

$ \begin{pmatrix} 1 & a_m & a_m^* & \cdots & a_m^{n-1} & a_m^* \end{pmatrix}
\Longleftrightarrow \begin{pmatrix} 1 & a_1 & a_1^2 & \cdots & a_1^{n-1} & a_1^n \ 0 & a_2 - a_1 & a_2^2 - a_1^2 & \cdots & a_2^{n-1} - a_1^{n-1} & a_2^n - a_1^n \ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \ 0 & a_m - a_1 & a_m^2 - a_1^2 & \cdots & a_m^{n-1} - a_1^{n-1} & a_m^n - a_m^n \end{pmatrix} $

$ \begin{pmatrix} 1 & a_1 & a_1^2 & a_1^3 & \cdots & a_1^{n-1} & a_1^n \end{pmatrix} $

$ \Longleftrightarrow \begin{pmatrix} - & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & $



CHOONG 9. DINII THUU VA HU LHUUNG TRINII TUTEN THUI

$ \iff \begin{pmatrix} 1 & a_1 & a_1^2 & a_1^3 & \cdots & a_1^{n-1} & a_1^n \\ 0 & 1 & h_1(a_1, a_2) & h_2(a_1, a_2) & \cdots & h_{n-2}(a_1, a_2) & h_{n-1}(a_1, a_2) \\ 0 & 0 & a_3 - a_2 & (a_3 - a_2)h_1(a_1, a_2, a_3) & \cdots & (a_3 - a_2)h_{n-3}(a_1, a_2, a_3) & (a_3 - a_2)h_{n-2}(a_1, a_2, a_3) \\ \vdots & \vdots & \vdots & $

0 $a_m$ - $a_2 (a_m$ - $a_2)h_1(a_1$, $a_2$, $a_m) \cdots (a_m$ - $a_2)h_{n-3}(a_1$, $a_2$, $a_m) (a_m$ - $a_2)h_{n-2}(a_1$, $a_m)$

$ \Longleftrightarrow \begin{pmatrix} 1 & a_1 & a_1^2 & a_1^3 & \cdots & a_1^{n-1} & a_1^n \\ 0 & 1 & h_1(a_1, a_2) & h_2(a_1, a_2) & \cdots & h_{n-2}(a_1, a_2) & h_{n-1}(a_1, a_2) \\ 0 & 0 & 1 & h_1(a_1, a_2, a_3) & \cdots & h_{n-3}(a_1, a_2, a_3) & h_{n-2}(a_1, a_2, a_3) \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 & 1 & h_1(a_1 $

$ \begin{pmatrix} 1 & a_1 & a_1^2 & \cdots & a_1^{m-1} & \cdots & a_1^{n-1} & a_1^n \\ 0 & 1 & h_1(a_1, a_2) & \cdots & h_{m-2}(a_1, a_2) & \cdots & h_{n-2}(a_1, a_2) & h_{n-1}(a_1, a_2) \\ 0 & 0 & 1 & \cdots & h_{m-3}(a_1, a_2, a_3) & \cdots & h_{n-3}(a_1, a_2, a_3) & h_{n-2}(a_1, a_2, a_3) \end{pmatrix} $

$ \begin{pmatrix} \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1 & \cdots & h_{n-m}(a_1,\ldots,a_m) & h_{n-m+1}(a_1,\ldots,a_m) \end{pmatrix} $

(trong đó, nhắc lại $h_k$ là đa thức đối xứng thuần nhất đầy đủ bậc k).

Như vậy, hệ phương trình tuyến tính có nghiệm.

$x_{n-m}$, $x_{n-m-1}$, $\ldots$, $x_0$ có thể nhận giá trị bất kì.

$x_{n-m+1}$ được xác định từ phương trình thứ m.

$x_{n-m+2}$ được xác định từ phương trình thứ m-1.

$\ddots$

$x_n$ được xác định từ phương trình thứ 1.

Bài tập 3.37. Đặt $s_n(k) = 1^n$ + $2^n$ + $\cdots$ + $(k-1)^n$. Hãy thiết lập phương trình

$k^{n} =$ 1 + ${n \choose n-1} s_{n-1}(k)$ + $\cdots$ + ${n \choose 1} s_{1}(k)$ + $s_{0}(k)$



VIIUVINU 9. DIINII TIIUV VA IID I IIUVINU TIUINII TUTEN TIINII

và chứng minh rằng

$ s_{n-1}(k) = \frac{1}{n!} \begin{vmatrix} k^n & \binom{n}{n-2} & \binom{n}{n-3} & \cdots & \binom{n}{1} & 1 \\ k^{n-1} & \binom{n-1}{n-2} & \binom{n-1}{n-3} & \cdots & \binom{n-1}{1} & 1 \\ k^{n-2} & 0 & \binom{n-2}{n-3} & \cdots & \binom{n-2}{1} & 1 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ k^2 & 0 & 0 & \cdots & \binom{2}{1} & 1 \\ k & 0 & 0 & \cdots & 0 & 1 \end{vmatrix $

Chúng minh. Ap dụng định lý nhị thức Newton:

$k^{n} =$ 1 + ${n \choose 1}(k-1)$ + $\cdots$ + ${n \choose n-1}(k-1)^{n-1}$ + $(k-1)^{n}$

$(k-1)^n =$ 1 + $\binom{n}{1}(k-2)$ + $\cdots$ + $\binom{n}{n-1}(k-2)^{n-1}$ + $(k-2)^n$

$2^{n} =$ 1 + ${n \choose 1}$ 1 + $\cdots$ + ${n \choose n-1} 1^{n-1}$ + $1^{n}$

Cộng về theo về của tất cả đẳng thức trên:

$k^{n}$ + $(k-1)^{n}$ + $\cdots$ + $2^{n} = s_{0}(k)$ + ${n \choose 1} s_{1}(k)$ + $\cdots$ + ${n \choose n-1} s_{n-1}(k)$ + $(k-1)^{n}$ + $\cdots$ + 1

$\iff k^{n} = s_{0}(k)$ + ${n \choose 1} s_{1}(k)$ + $\cdots$ + ${n \choose n-1} s_{n-1}(k)$ + 1

$\iff k^n =$ 1 + $\binom{n}{n-1} s_{n-1}(k)$ + $\dots$ + $\binom{n}{1} s_1(k)$ + $s_0(k)$.

Ap dụng công thức trên với các giá trị n nhỏ hơn:

$k^{n} =$ 1 + ${n \choose n-1} s_{n-1}(k)$ + $\cdots$ + ${n \choose 1} s_{1}(k)$ + $s_{0}(k)$

$k^{n-1} =$ 1 + $\binom{n-1}{n-2} s_{n-2}(k)$ + $\cdots$ + $\binom{n-1}{1} s_1(k)$ + $s_0(k)$

$\mathcal{L}_{\mathcal{A}}$

k $=$ 1 + $s_0(k)$



VIIUVINU 0. DIINII TIIUV VA IID I IIUVINU TIIIINII TUTEN TIINII

$s_{n-1}(k)$, $s_{n-2}(k)$, ..., $s_0(k)$ là nghiệm của hệ phương trình tuyến tính:

$\binom{n}{n-1}x_{n-1}$ + $\binom{n}{n-2}x_{n-2}$ + $\cdots$ + $\binom{n}{1}x_1$ + $x_0 = k^n$ - $1\binom{n-1}{n-2}x_{n-2}$ + $\cdots$ + $\binom{n-1}{1}x_1$ + $x_0 = k^{n-1}$ - 1

$x_0 =$ k-1

Dịnh thức của ma trận hệ số bằng:

$ \begin{pmatrix} {n \choose n-1} & {n \choose n-2} & \cdots & {n \choose 1} & 1 \\ 0 & {n-1 \choose n-2} & \cdots & {n-1 \choose 1} & 1 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 0 & 1 \end{pmatrix} = {n \choose n-1} {n-1 \choose n-2} \cdots {2 \choose 1} = n! $

Áp dụng công thức Cramer:

$ s_{n-1}(k)=x_{n-1}=\frac{1}{n!}\begin{vmatrix}k^n-1&\binom{n}{n-2}&\binom{n}{n-3}&\cdots&\binom{n}{1}&1\\k^{n-1}-1&0&\binom{n-1}{n-3}&\cdots&\binom{n-1}{1}&1\\k^{n-2}-1&0&0&\cdots&\binom{n-2}{1}&1\\ \vdots&\vdots&\vdots&\vdots&\ddots&\vdots&\vdots\\ k-1&0&0&\cdots&0&1\end{vmatrix}=\frac{1}{n!}\begin{vmatrix}k^n&\binom{n}{n-2}&\binom{n}{n-3}&\cdots&\binom{n}{1}& $

Bài tập 3.38. Xét khai triển $\frac{x}{e^x-1} =$ 1 + $b_1x$ + $b_2x^2$ + $b_3x^3$ + $\cdots$. Ta đặt $b_{2n} = \frac{(-1)^{n-1}B_n}{(2n)!}$, trong đó

$B_n$ được gọi là số Bernoulli thứ n. Chứng minh rằng

$ B_n = (-1)^{n-1}(2n)! \begin{array}{|l|}\n\frac{1}{2!} & 1 & 0 & 0 & \cdots & 0 \\
\frac{1}{3!} & \frac{1}{2!} & 1 & 0 & \cdots & 0 \\
\frac{1}{4!} & \frac{1}{3!} & \frac{1}{2!} & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
\frac{1}{(2n+1)!} & \frac{1}{(2n)!} & \frac{1}{(2n-1)!} & \frac{1}{(2n-2)!} & \cdots & \frac{1}{2!}\n\end{array} $

và chỉ ra rằng

$\theta$

$\vert$ 0 $\vert$

$\frac{1}{2!}\frac{1}{3!}\frac{1}{4!}$

$\frac{1}{2!} \frac{1}{3!}$

$\frac{1}{2!}$

$\overline{0}$

$b_{2n-1}$

$=$ 0

$rac{1}{2!}$

$\overline{(2n)!}$

$\overline{(2n-3)!}$

$\overline{(2n-1)!}$

$\overline{(2n-2)!}$



VIIUVINU 9. DINII TIIUV VA IID LIIUVNU TIIINII TUTEN TIINII

với mọi n $>$ 1.

Chúng minh.

$\frac{x}{e^x-1} =$ 1 + $b_1x$ + $b_2x^2$ + $b_3x^3$ + $\cdots$

$\Leftrightarrow$ 1 $=$ (1 + $b_1x$ + $b_2x^2$ + $b_3x^3$ + $\cdots) \left(1$ + $\frac{x}{2!}$ + $\frac{x^2}{3!}$ + $\frac{x^3}{4!}$ + $\cdots \right)$

Đồng nhất hệ số $củax,\,x^2,\,x^3,\,\ldots,\,x^{2n}$ trong khai triển trên, ta được hệ phương trình tuyến

tính gồm (2n) phương trình:

$=\frac{-1}{2!}$

$b_1$

$rac{b_1}{2!}$ + $b_2rac{b_1}{3!}$ + $\frac{b_2}{2!}$ + $b_3$

$=\frac{-1}{3!}$

$=\frac{-1}{4!}$

$rac{b_1}{(2n-1)!}$ + $\frac{b_2}{(2n-2)!}$ + $\cdots$ + $b_{2n-1}rac{b_1}{(2n)!}$ + $\frac{b_2}{(2n-1)!}$ + $\cdots$ + $b_{2n}$

$\overline{(2n)!}$

$=\frac{-1}{(2n+1)!}$

Dịnh thức của ma trận hệ số của hệ (2n) phương trình tuyến tính này bằng:

$ \begin{vmatrix} 1 & 0 & 0 & \cdots & 0 & 0 \\ \frac{1}{2!} & 1 & 0 & \cdots & 0 & 0 \\ \frac{1}{3!} & \frac{1}{2!} & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ \frac{1}{(2n)!} & \frac{1}{(2n-1)!} & \frac{1}{(2n-2)!} & \cdots & \frac{1}{2!} & 1 \end{vmatrix} = 1 \neq 0. $

$ \begin{array}{|rrrrrr} 1 & 0 & 0 & \cdots & 0 & \frac{-1}{2!} \\ \hline \frac{1}{2!} & 1 & 0 & \cdots & 0 & \frac{-1}{2!} \\ \frac{1}{3!} & \frac{1}{2!} & 1 & & & & \end{array} $

Áp dụng công thức Cramer

$\frac{1}{2!}$ 1 $...\vdots \vdots$ ...

$b_{2n} =$

$\frac{1}{(2n-1)!} \frac{1}{(2n-2)!}$

$\frac{1}{2!}$

$\frac{-1}{(2n+1)!}$



CHOONG 9. DINII THUU VA HU LHUUNG TRINII TUTEN TINII

$ =(-1)^{2n-1}\begin{vmatrix}\frac{-1}{2!} & 1 & 0 & 0 & \cdots & 0\\ \frac{-1}{3!} & \frac{1}{2!} & 1 & 0 & \cdots & 0\\ \frac{-1}{4!} & \frac{1}{3!} & \frac{1}{2!} & 1 & \cdots & 0\\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots\end{vmatrix} $

$\frac{-1}{(2n+1)!}$

$\frac{1}{(2n)!}$

$\frac{1}{(2n-1)!}$

$\frac{1}{2!}$

$\frac{1}{(2n-2)!}$

$\ddot{\cdot} \ddot{\cdot}$

$ \begin{array}{cccc} \frac{1}{2!} & 1 & 0 & 0 & \cdots & 0 \\ \frac{1}{3!} & \frac{1}{2!} & 1 & 0 & \cdots & 0 \\ \frac{1}{4!} & \frac{1}{3!} & \frac{1}{2!} & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \end{array} $

$\equiv$

$\frac{1}{2!}$

$\ddotsc$

$\overline{(2n-1)!}$

$\overline{(2n-2)!}$

$\sqrt{(2n+1)!}$

$\overline{(2n)!}$

$Dod\acute{o}$

$\frac{1}{2!}$ 1 0 0 ... 0 $\frac{1}{3!} \frac{1}{2!}$ 1 0 ... 0 $\frac{1}{4!} \frac{1}{3!} \frac{1}{2!}$ 1 ... 0 $\vdots \vdots \vdots \vdots \vdots$

$B_n = (-1)^{n-1}(2n)!$

$\vert$ 0 $\vert$

$\frac{1}{(2n)!}$

$\frac{1}{(2n+1)!}$

$\frac{1}{2!}$

$\cdot \cdot \cdot$

$\frac{1}{(2n-1)!}$

$\overline{(2n-2)!}$

Áp dụng công thức Cramer cho 2n-1 phương trình tuyến tính đầu tiên:

$ \begin{array}{|rrrrrr} 1 & 0 & 0 & \cdots & 0 & \frac{-1}{2!} \\ \hline \frac{1}{2!} & 1 & 0 & \cdots & 0 & \frac{-1}{3!} \\ \frac{1}{3!} & \frac{1}{2!} & 1 & \cdots & 0 & \frac{-1}{4!} \end{array} $

$b_{2n-1} =$

$\ddot{\cdot}$

$\frac{1}{2!}$

$\frac{-1}{(2n)!}$

$\frac{1}{(2n-3)!}$

$\cdots$

$\overline{(2n-2)!}$

$\overline{(2n-1)!}$

$ \begin{array}{cccccc} 1 & 0 & \cdots & 0 & 0 \ \frac{1}{2!} & 1 & \cdots & 0 & 0 \ \frac{1}{3!} & \frac{1}{2!} & \cdots & 0 & 0 \end{array} $

$rac{1}{2!}rac{1}{3!}rac{1}{4!}$

$\vdots$

$\ddot{\cdot}$

$\mathcal{O}(\mathcal{E}_{\mathcal{A}})$

$\mathbf{1}$

$rac{1}{3!}$

$\frac{1}{2!}$

$\bullet \bullet \bullet$

$\sqrt{(2n-2)!}$

$\overline{(2n)!}$

$\overline{(2n-1)!}$



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

$\frac{x}{e^x-1} =$ 1 + $b_1x$ + $b_2x^2$ + $b_3x^3$ + $\cdots$

$\frac{-x}{e^{-x}-1} =$ 1 - $b_1x$ + $b_2x^2$ - $b_3x^3$ + $\cdots$

$\iff \frac{x}{e^x$ - $1}$ + $\frac{x}{e^{-x}$ - $1} = 2b_1x$ + $2b_3x^3$ + $\cdots$

$\iff$ -x $= 2b_1x$ + $2b_3x^3$ + $\cdots$

Đồng nhất hệ số của hai đa thức, ta được $b_1 = \frac{-1}{2}$, $b_3 = b_5 = \cdots = b_{2n-1} = \cdots =$ 0.

Vậy với $n>1$

$ b_{2n-1} = \begin{vmatrix} \frac{1}{2!} & 1 & 0 & \cdots & 0 & 0 \\ \frac{1}{3!} & \frac{1}{2!} & 1 & \cdots & 0 & 0 \\ \frac{1}{4!} & \frac{1}{3!} & \frac{1}{2!} & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ \frac{1}{(2n)!} & \frac{1}{(2n-1)!} & \frac{1}{(2n-2)!} & \cdots & \frac{1}{3!} & \frac{1}{2!} \end{vmatrix} = 0. $

Bài tập 3.39. Diễn đạt hệ số $a_n$ trong khai triển

$e^{-x} =$ 1 - $a_1$ x + $a_2 x^2$ - $a_3 x^3$ + $\cdots$

như một định thức cỡ n, từ đó tính định thức thu được.

Lời giải.

$e^{-x} =$ 1 - $a_1x$ + $a_2x^2$ - $a_3x^3$ + $\cdots$

1 $=$ (1 - $a_1x$ + $a_2x^2$ - $a_3x^3$ + $\cdots) \left(1$ + x + $\frac{x^2}{2!}$ + $\frac{x^3}{3!}$ + $\cdots\right)$

Đồng nhất hệ số của các hạng tử x, $x^2$, $x^3$, ..., $x^n$, ta thu được hệ phương trình tuyến tính:

$(-1)^{1}a_{1}$ + $\frac{1}{1!} =$ 0

$(-1)^{2}a_{2}+(-1)^{1}a_{1}\frac{1}{1!}+\frac{1}{2!}=0$

$(-1)^3 a_3$ + $(-1)^2 a_2 \frac{1}{1!}$ + $(-1)^1 a_1 \frac{1}{2!}$ + $\frac{1}{3!} =$ 0

$(-1)^n a_n$ + $(-1)^{n-1} a_{n-1} \frac{1}{1!}$ + $\cdots$ + $(-1)^1 a_1 \frac{1}{(n-1)!}$ + $\frac{1}{n!} =$ 0



VIIUVINU 9. DINII THUU VA HIJ LHUUNU TIIINII TUTEN TINII

$(-1)^{1}a_{1}$, $(-1)^{2}a_{2}$, ..., $(-1)^{n}a_{n}$ là nghiệm của hệ phương tình tuyến tính:

$=\frac{-1}{1!}=\frac{-1}{2!}=\frac{-1}{3!}$

$x_1$

$\frac{1}{1!}x_1$ + $x_2 \frac{1}{2!}x_1$ + $\frac{1}{1!}x_2$ + $x_3$

$\frac{1}{(n-1)!}x_1$ + $\frac{1}{(n-2)!}x_2$ + $\cdots$ + $\frac{1}{1!}x_{n-1}$ + $x_n$

$=\frac{-1}{n!}$

Định thức của ma trận hệ số bằng 1. Áp dụng công thức Cramer:

$ (-1)^n a_n = x_n = \begin{vmatrix} 1 & 0 & 0 & \cdots & 0 & \frac{-1}{1!} \\ \frac{1}{1!} & 1 & 0 & \cdots & 0 & \frac{-1}{2!} \\ \frac{1}{2!} & \frac{1}{1!} & 1 & \cdots & 0 & \frac{-1}{3!} \end{vmatrix} $

$\mathcal{L}_{\text{max}}$

$\frac{1}{(n-3)!} \cdots \frac{1}{1!} \frac{-1}{n!}$

$\frac{1}{(n-2)!}$

$\frac{1}{(n-1)!}$

$ =(-1)^{n-1}\begin{vmatrix}\frac{-1}{1!} & 1 & 0 & 0 & \cdots & 0\\ \frac{-1}{2!} & \frac{1}{1!} & 1 & 0 & \cdots & 0\\ \frac{-1}{3!} & \frac{1}{2!} & \frac{1}{1!} & 1 & \cdots & 0\\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots\\ \frac{-1}{n!} & \frac{1}{(n-1)!} & \frac{1}{(n-2)!} & \frac{1}{(n-3)!} & \cdots & \frac{1}{1!} \end{vmatrix} $

$ = (-1)^n \begin{vmatrix} \frac{1}{1!} & 1 & 0 & 0 & \cdots & 0 \\ \frac{1}{2!} & \frac{1}{1!} & 1 & 0 & \cdots & 0 \\ \frac{1}{3!} & \frac{1}{2!} & \frac{1}{1!} & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & 1 & 1 & 1 & 1 & 1 \end{vmatrix} $

$\frac{1}{(n-3)!}$

$\frac{1}{n!}$

$\frac{1}{(n-1)!}$

$\cdots \frac{1}{1!}$

$\frac{1}{(n-2)!}$

$ \begin{vmatrix}\n\frac{1}{1!} & 1 & 0 & 0 & \cdots & 0 \\
\frac{1}{2!} & \frac{1}{1!} & 1 & 0 & \cdots & 0 \\
\frac{1}{3!} & \frac{1}{2!} & \frac{1}{1!} & 1 & \cdots & 0\n\end{vmatrix} $

$\Longleftrightarrow a_n =$

$ \begin{vmatrix} \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \frac{1}{n!} & \frac{1}{(n-1)!} & \frac{1}{(n-2)!} & \frac{1}{(n-3)!} & \cdots & \frac{1}{1!} \end{vmatrix} $

Áp dụng khai triển Taylor:

$e^{-x} = \sum_{n=0}^{+\infty} \frac{(-1)^n x^n}{n!}$



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

Đồng nhất hệ số với $e^{-x} =$ 1 - $a_1x$ + $a_2x^2$ - $a_3x^3$ + $\cdots$, ta được:

$ a_n = \begin{vmatrix} \frac{1}{1!} & 1 & 0 & 0 & \cdots & 0 \\ \frac{1}{2!} & \frac{1}{1!} & 1 & 0 & \cdots & 0 \\ \frac{1}{3!} & \frac{1}{2!} & \frac{1}{1!} & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \frac{1}{n!} & \frac{1}{(n-1)!} & \frac{1}{(n-2)!} & \frac{1}{(n-3)!} & \cdots & \frac{1}{1!} \end{vmatrix} = \frac{1}{n!}. $

Bài tập 3.40. Không dùng ma trận của tự đồng cấu, hãy chứng minh trực tiếp rằng nếu f là

một tự đồng cấu của không gian vector hữu hạn chiều V và $f^*$ là đồng cấu đối ngẫu của f,

thì $det(f<sup>*</sup>) =$ det(f). (Gợi ý: Xét định thức của ma trận $(\langle \alpha_i$, $\xi_j \rangle)_{n \times n}$, trong đó $\alpha_1$, $\ldots$, $\alpha_n \in$ V,

$\xi_1$, $\ldots$, $\xi_n \in V^*$.

Chứng minh. $(\alpha_1$, $\alpha_2$, $\ldots$, $\alpha_n)$ là một cơ sở của V.

$(\xi_1$, $\xi_2$, $\ldots$, $\xi_n)$ là một cơ sở đối ngẫu của $(\alpha_1$, $\alpha_2$, $\ldots$, $\alpha_n)$.

Ta sử dụng hai dạng đa tuyến tính thay $phiên<sup>1</sup> \varphi \in \Lambda^n(V)^*$, $\psi \in \Lambda^n(V^*)^*$ sau:

$ \varphi(v_1, v_2, \ldots, v_n) = \begin{vmatrix} \langle v_1, \xi_1 \rangle & \langle v_1, \xi_2 \rangle & \cdots & \langle v_1, \xi_n \rangle \\ \langle v_2, \xi_1 \rangle & \langle v_2, \xi_2 \rangle & \cdots & \langle v_2, \xi_n \rangle \\ \vdots & \vdots & \ddots & \vdots \\ \langle v_n, \xi_1 \rangle & \langle v_n, \xi_2 \rangle & \cdots & \langle v_n, \xi_n \rangle \end{vmatrix},
\psi(\tau_1, \tau_2, \ldots, \tau_n) = \begin{vmatrix} \langle \alpha_1, \tau_1 \rangle & \langle \alpha_1 $

Theo định nghĩa định thức của tự đồng cấu:

$\varphi(f(\alpha_1)$, $f(\alpha_2)$, $\ldots$, $f(\alpha_n)) = \det(f) \cdot \varphi(\alpha_1$, $\alpha_2$, $\ldots$, $\alpha_n)$,

$\psi(f^*(\xi_1)$, $f^*(\xi_2)$, $\ldots$, $f^*(\xi_n)) = \det(f^*) \cdot \psi(\xi_1$, $\xi_2$, $\ldots$, $\xi_n)$.

$<sup>1</sup>Oversimplified:$ Hai ánh xạ này đa tuyến tính thay phiên bởi biểu thức mà chúng được định nghĩa theo là một

định thức, và định thức có tính chất đa tuyến tính thay phiên (ở đây định thức được nhìn nhận là một hàm của

các vector cột).



VIIUVINU 9. DIINII TIIUV VA IID FIIUVINU TIURIII TUTEN TIINII

Khai triển các đẳng thức trên, ta thu được:

$ \begin{vmatrix} \langle f(\alpha_1), \xi_1 \rangle & \langle f(\alpha_1), \xi_2 \rangle & \cdots & \langle f(\alpha_1), \xi_n \rangle \\ \langle f(\alpha_2), \xi_1 \rangle & \langle f(\alpha_2), \xi_2 \rangle & \cdots & \langle f(\alpha_2), \xi_n \rangle \\ \vdots & \vdots & \ddots & \vdots \\ \end{vmatrix} = \det(f) \begin{vmatrix} \langle \alpha_1, \xi_1 \rangle & \langle \alpha_1, \xi_2 \rangle & \cdots & \langle \alpha_1, \xi_n \rangle \\ \langle \alpha_2, \xi_1 \rangle & \langle \alpha_2, \xi_2 \rangle & \cdots & \langle \alpha_2, \ $

$|\langle f(\alpha_n)$, $\xi_1 \rangle \langle f(\alpha_n)$, $\xi_2 \rangle \cdots \langle f(\alpha_n)$, $\xi_n \rangle$ | $\qquad |\langle \alpha_n$, $\xi_1 \rangle \langle \alpha_n$, $\xi_2 \rangle \cdots \langle \alpha_n$, $\xi_n \rangle$ |

$ \begin{vmatrix} \langle \alpha_1, f^*(\xi_1) \rangle & \langle \alpha_1, f^*(\xi_2) \rangle & \cdots & \langle \alpha_1, f^*(\xi_n) \rangle \\ \langle \alpha_2, f^*(\xi_1) \rangle & \langle \alpha_2, f^*(\xi_2) \rangle & \cdots & \langle \alpha_2, f^*(\xi_n) \rangle \\ \vdots & \vdots & \ddots & \vdots \\ \langle \alpha_n, f^*(\xi_1) \rangle & \langle \alpha_n, f^*(\xi_2) \rangle & \cdots & \langle \alpha_n, f^*(\xi_n) \rangle \end{vmatrix} = \det(f^*) \begin{vmatrix} \langle \alpha_1, \xi_1 \rangle $

Theo định nghĩa của đồng cấu tuyến tính đối ngẫu, $f^*(\varphi) = \varphi \circ$ f, $\forall \varphi \in V^*$, suy ra:

$ det(f) \begin{vmatrix} \langle \alpha_1, \xi_1 \rangle & \langle \alpha_1, \xi_2 \rangle & \cdots & \langle \alpha_1, \xi_n \rangle \\ \langle \alpha_2, \xi_1 \rangle & \langle \alpha_2, \xi_2 \rangle & \cdots & \langle \alpha_2, \xi_n \rangle \\ \vdots & \vdots & \ddots & \vdots \\ \langle \alpha_n, \xi_1 \rangle & \langle \alpha_n, \xi_2 \rangle & \cdots & \langle \alpha_n, \xi_n \rangle \end{vmatrix} = det(f^*) \begin{vmatrix} \langle \alpha_1, \xi_1 \rangle & \langle \alpha_1, \xi_2 \rangle & \cdots & \langle \alpha_1, \xi_n \ $

Bên cạnh đó, theo định nghĩa của cơ sở đối ngẫu, $\langle \alpha_i$, $\xi_j \rangle = \delta_{ij}$, $\forall$ i, j $\in \{1$, 2, ..., $n\}$. Do đó

$(\langle \alpha_i$, $\xi_j \rangle)_{i \times j} = I_n$, và det $(\langle \alpha_i$, $\xi_j \rangle)_{i \times j} =$ 1, kéo theo:

$\det(f) = \det(f^*)$.

Bài tập 3.41. Tính hạng của các ma trận sau đây bằng phương pháp biến đối sơ cấp và phương

pháp dùng định thức con:

$ (a) \begin{pmatrix} 2 & -1 & 3 & -2 & 4 \\ 4 & -2 & 5 & 1 & 7 \\ 2 & -1 & 1 & 8 & 2 \end{pmatrix}, $

$ (b) \begin{pmatrix} 3 & -1 & 3 & 2 & 5 \\ 5 & -3 & 2 & 3 & 4 \\ 1 & -3 & -5 & 0 & -7 \\ 7 & -5 & 1 & 4 & 1 \end{pmatrix}. $



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

Lời giải. (a)

$ rank \begin{pmatrix} 2 & -1 & 3 & -2 & 4 \\ 4 & -2 & 5 & 1 & 7 \\ 2 & -1 & 1 & 8 & 2 \end{pmatrix} = rank \begin{pmatrix} 2 & -1 & 3 & -2 & 4 \\ 0 & 0 & -1 & 5 & -1 \\ 0 & 0 & -2 & 10 & -2 \end{pmatrix} = rank \begin{pmatrix} 2 & -1 & 3 & -2 & 4 \\ 0 & 0 & -1 & 5 & -1 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix} = 2. $

(b)

$ \text{rank}\begin{pmatrix} 3 & -1 & 3 & 2 & 5 \\ 5 & -3 & 2 & 3 & 4 \\ 1 & -3 & -5 & 0 & -7 \\ 7 & -5 & 1 & 4 & 1 \end{pmatrix} = \text{rank}\begin{pmatrix} 1 & -3 & -5 & 0 & -7 \\ 3 & -1 & 3 & 2 & 5 \\ 5 & -3 & 2 & 3 & 4 \\ 7 & -5 & 1 & 4 & 1 \end{pmatrix} = \text{rank}\begin{pmatrix} 1 & -3 & -5 & 0 & -7 \\ 0 & 8 & 18 & 2 & 26 \\ 0 & 12 & 27 & 3 & 39 \\ 0 & 16 &  $

$ = rank \begin{pmatrix} 1 & -3 & -5 & 0 & -7 \\ 0 & 4 & 9 & 1 & 13 \\ 0 & 4 & 9 & 1 & 13 \\ 0 & 8 & 18 & 2 & 25 \end{pmatrix} = rank \begin{pmatrix} 1 & -3 & -5 & 0 & -7 \\ 0 & 4 & 9 & 1 & 13 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & -1 \end{pmatrix} = 3. $

Bài tập 3.42. Tìm giá trị của $\lambda$ sao cho ma trận sau đây có hạng thấp nhất

$ \left(\begin{array}{cccc} 0 & 1 & 1 & 4 \\ \lambda & 4 & 10 & 1 \\ 1 & 7 & 17 & 3 \\ 0 & 0 & 4 & 3 \end{array}\right). $

Lời giải.

$ rank \begin{pmatrix} 3 & 1 & 1 & 4 \\ \lambda & 4 & 10 & 1 \\ 1 & 7 & 17 & 3 \\ 2 & 2 & 4 & 3 \end{pmatrix} = rank \begin{pmatrix} \lambda & 4 & 10 & 1 \\ 1 & 7 & 17 & 3 \\ 2 & 2 & 4 & 3 \\ 3 & 1 & 1 & 4 \end{pmatrix} = rank \begin{pmatrix} \lambda & 4 & 10 & 1 \\ 1 & 7 & 17 & 3 \\ 0 & -12 & -30 & -3 \\ 0 & -20 & -50 & -5 \end{pmatrix} $

$ = \text{rank}\begin{pmatrix} \lambda & 4 & 10 & 1 \\ 1 & 7 & 17 & 3 \\ 0 & 4 & 10 & 1 \\ 0 & 4 & 10 & 1 \end{pmatrix} = \text{rank}\begin{pmatrix} \lambda & 0 & 0 & 0 \\ 1 & 7 & 17 & 3 \\ 0 & 4 & 10 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}. $

Để ma trận trên có hạng thấp nhất, $\lambda =$ 0.



VIIUVINU 9. DIINII TIIUV VA IID I IIUVINU TIUINII TUTEN TIINII

Bài tập 3.43. Tìm hạng của ma trận sau đây như một hàm phụ thuộc $\lambda:$

$ \begin{pmatrix} 1 & \lambda & -1 & 2 \\ 2 & -1 & \lambda & 5 \\ 1 & 10 & 6 & 1 \end{pmatrix}. $

$ Lời giải. Ma trận trên có định thức con \begin{vmatrix} 2 & -1 \\ 1 & 10 \end{vmatrix} = 21 \neq 0. $

Do đó hạng của ma trận trên lớn hơn hoặc bằng 2. Tính tất cả các định thức con cỡ 3:

$ \begin{vmatrix} 1 & \lambda & -1 \\ 2 & -1 & \lambda \\ 1 & 10 & -6 \end{vmatrix} = (\lambda - 3)(\lambda + 5) $

$ \begin{vmatrix} 1 & \lambda & 2 \\ 2 & -1 & 5 \\ 1 & 10 & 1 \end{vmatrix} = 3(\lambda - 3) $

$ \begin{vmatrix} 1 & -1 & 2 \\ 2 & \lambda & 5 \\ 1 & -6 & 1 \end{vmatrix} = -(\lambda - 3) $

$ \begin{vmatrix} \lambda & -1 & 2 \\ -1 & \lambda & 5 \\ 10 & -6 & 1 \end{vmatrix} = (\lambda - 3)(\lambda + 13) $

Vậy hạng của ma trận trên bằng 3 nếu $\lambda \neq$ 3, bằng 2 nếu $\lambda =$ 3.

Bài tập 3.44. Chứng minh rằng nếu hạng của một ma trận bằng r thì mỗi định thức con nằm

trên giao của bất kì r hàng độc lập tuyến tính và r cột độc lập tuyến tính của ma trận đó đều

khác 0.

Chứng minh. Giả sử ma trận A đang xét có m hàng và n cột.

Việc thay đổi thứ tự các hàng hay thay đổi thứ tự các cột không làm ảnh hưởng đến sự độc

lập tuyến tính/phụ thuộc tuyến tính của các vector hàng, vector cột mà chỉ thay đổi thứ tự các

vector đó, cũng như thứ tự của các yếu tố trong các vector đó.

Do đó, không mất tính tổng quát, giả sử r hàng đầu tiên của A độc lập tuyến tính và r cột



VIIUVINU 9. DINII TIIUV VA IID LIIUVNU TIIINII TUTEN TIINII

đầu tiên của A độc lập tuyến tính.

$ A = \left( \begin{array}{ccccc} a_{11} & a_{12} & \cdots & a_{1r} & a_{1(r+1)} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2r} & a_{2(r+1)} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ a_{r1} & a_{r2} & \cdots & a_{rr} & a_{r(r+1)} & \cdots & a_{rn} \\ a_{(r+1)1} & a_{(r+1)2} & \cdots & a_{(r+1)r} & a_{(r+1)(r+1)} & \cdots & a_{(r+1)n} \\ \vdots $

$Do\mathrm{rank}(A)=rvà$ rhàng đầu tiên củaAđộc lập tuyến tính nên hàng $cộtr+1,\,\ldots,\,nđều$

biểu thị tuyến tính được theo r hàng đầu tiên, ta đặt:

$(a_{(r+1)1}$, $a_{(r+1)2}$, $\ldots$, $a_{(r+1)r}$, $\ldots$, $a_{(r+1)n}) = \sum_{k=1}^r b_k^{(r+1)}(a_{k1}$, $a_{k2}$, $\ldots$, $a_{kr}$, $\ldots$, $a_{kn})$

$(a_{(r+2)1}$, $a_{(r+2)2}$, $\ldots$, $a_{(r+2)r}$, $\ldots$, $a_{(r+2)n}) = \sum_{k=1} b_k^{(r+2)}(a_{k1}$, $a_{k2}$, $\ldots$, $a_{kr}$, $\ldots$, $a_{kn})$

$(a_{m1}$, $a_{m2}$, $\ldots$, $a_{mr}$, $\ldots$, $a_{mn}) = \sum_{k=1}^r b_k^{(m)}(a_{k1}$, $a_{k2}$, $\ldots$, $a_{kr}$, $\ldots$, $a_{kn})$

Từ các biểu thị tuyến tính trên, ta suy ra:

$ \begin{cases}\n(a_{(r+1)1}, a_{(r+1)2}, \ldots, a_{(r+1)r}, 0, \ldots, 0) & = \sum_{k=1}^r b_k^{(r+1)}(a_{k1}, a_{k2}, \ldots, a_{kr}, 0, \ldots, 0) \\
(a_{(r+2)1}, a_{(r+2)2}, \ldots, a_{(r+2)r}, 0, \ldots, 0) & = \sum_{k=1}^r b_k^{(r+2)}(a_{k1}, a_{k2}, \ldots, a_{kr}, 0, \ldots, 0) \\
\vdots & \vdots & \vdots \\
(a_{m1}, a_{m2}, \ldots, a_{mr}, 0, \ldots $

$(\star)$

Do rank(A) $=$ r và r cột đầu tiên của A độc lập tuyến tính nên từng cột r + 1, $\ldots$, n đều biểu

thị tuyến tính được theo r cột đầu tiên, do đó nếu xóa các cột r+1, $\ldots$, n thì hạng của A không



VIIUVINU 9. DINII TIIUV VA IID LIIUVNU TIIINII TUTEN TIINII

đổi. Nói cách khác:

$ \left( \begin{array}{cccc} a_{11} & a_{12} & \cdots & a_{1r} \\ a_{21} & a_{22} & \cdots & a_{2r} \\ \vdots & \vdots & \ddots & \vdots \end{array} \right) $

$a_{1(r+1)}$

$a_{1n}$

$a_{2(r+1)}\vdots$

$ \begin{aligned} \mathbf{1} & \mathbf{1} \\ \mathbf{2} & \mathbf{1} \\ \mathbf{3} & \mathbf{1} \\ \mathbf{4} & \mathbf{1} \end{aligned} $

$a_{2n}$

$a_{r1} a_{r2} \cdots a_{rr} a_{r(r+1)} \cdots a_{r+1} a_{(r+1)2} \cdots a_{(r+1)r} a_{(r+1)(r+1)} \cdots \vdots \vdots \vdots \vdots \vdots \vdots a_{m1} a_{m2} \cdots a_{mr} a_{m(r+1)} \cdots$

rank

$a_{r1}$

$a_{rn}$

$a_{mn}$

$a_{m1}$

$ \left(\begin{array}{ccccccccc} a_{11} & & a_{12} & & \cdots & & a_{1r} & & 0 & \cdots & 0 \ a_{21} & & a_{22} & & \cdots & & a_{2r} & & 0 & \cdots & 0 \ \vdots & & \vdots & & \ddots & & \vdots & & \vdots & & \ddots & \vdots \end{array}\right) $

$\dots \dots \dots \dots a_{(r+1)r}$

$a_{r2}$

$a_{r1}$

$=$ rank |

$a_{(r+1)2}$

$a_{(r+1)1}$

$ \begin{pmatrix} \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mr} & 0 & \cdots & 0 \end{pmatrix} $

Ma trận mới có các vector cột thứ r+1, $\ldots$, n bằng không.

Mặt khác, theo các đẳng thức $(\star)$, ta có thể xóa các hàng r+1, $\ldots$, n của ma trận mới mà

vẫn bảo toàn hạng, điều này kéo theo:

$ \text{rank}\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1r} & 0 & \cdots & 0 \\ a_{21} & a_{22} & \cdots & a_{2r} & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ a_{r1} & a_{r2} & \cdots & a_{rr} & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \end{pmatrix} = \text{rank}(A) $

Giả sử phản chứng rằng:

$a_{11} \quad a_{12} \quad \cdots \quad a_{1r}$

$ \begin{vmatrix} a_{21} & a_{22} & \cdots & a_{2r} \\ \vdots & \vdots & \ddots & \vdots \\ a_{r1} & a_{r2} & \cdots & a_{rr} \end{vmatrix} = 0. $

Khi đó, mọi định thức con cỡ r của ma trận trên đều bằng không, kéo theo rank(A) $<$ r.

Điều mâu thuẫn này chứng tỏ giả sử phản chứng là sai. Như vậy, định thức con nằm trên giao



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

của r hàng độc lập tuyến tính và r cột độc lập tuyến tính khác không.

$\Box$

Bài tập 3.45. Cho A là một ma trận vuông cỡ n $>$ 1 và $\tilde{A}$ là ma trận phụ hợp (gồm những phần

bù đại số của các yếu tố) của A. Hãy xác định $rank\tilde{A}$ như một hàm của rankA.

Chứng minh. Đặt $\tilde{a}_{ij}$ là phần bù đại số của $a_{ij}$ trong ma trận A. Khi đó, theo định nghĩa của ma

trận phụ hợp:

$ \tilde{A} = \begin{pmatrix} \tilde{a}_{11} & \tilde{a}_{21} & \cdots & \tilde{a}_{n1} \ \tilde{a}_{12} & \tilde{a}_{22} & \cdots & \tilde{a}_{n2} \ \vdots & \vdots & \ddots & \vdots \ \tilde{a}_{1n} & \tilde{a}_{2n} & \cdots & \tilde{a}_{nn} \end{pmatrix} $

Trường hợp 1. rank(A) $=$ n.

Lúc này, $\det(A) \neq$ 0. Mà $\det(A) \cdot \det(\tilde{A}) =$ 1 nên $\det(\tilde{A})$, dẫn tới $rank(\tilde{A}) =$ n.

Trường hợp 2. $\text{rank}(A) <$ n-1.

Lúc này, mọi định thức con cỡ(n-1)củaAđều bằng không, do $đó\tilde{A}là$ ma trận không.

Như vậy $\text{rank}(A) =$ 0.

Trường hợp 3. rank(A) $=$ n - 1.

Vì rank(A) $=$ n – 1 nên A sẽ có ít nhất một định thức con cỡ (n – 1) với giá trị khác không.

Diều này đảm bảo $rank(\overline{A}) \geq$ 1.

Nhận xét rằng:

• Đối chỗ hai cột j và j' của A thì ma trận phụ hợp mới là ma trận phụ hợp cũ sau khi

đổi chỗ hai hàng j và j'.

• Đối chỗ hai hàng i và i' của A thì ma trận phụ hợp mới là ma trận phụ hợp cũ sau khi

đổi chỗ hai cột i và i'.

Như vậy, không mất tính tổng quát, giả sử (n-1) cột đầu tiên của A độc lập tuyến tính và

(n-1) hàng đầu tiên của A độc lập tuyến tính.

Khi đó, $\tilde{a}_{nn} \neq$ 0 và trong ma trận A, hàng cuối cùng biểu thị tuyến tính được duy nhất theo

(n-1) hàng đầu tiên. Vì (n-1) cột đầu tiên của A là độc lập tuyến tính và hạng của A

bằng (n-1) nên cột thứ n của A là một tổ hợp tuyến tính của (n-1) cột đầu tiên của A.

Như vậy, tồn tại các vô hướng $\lambda_1$, $\ldots$, $\lambda_{n-1}$ sao cho

$\lambda_1 column<sub>1</sub>(A)$ + $\cdots$ + $\lambda_{n-1} column<sub>n-1</sub>(A) = column<sub>n</sub>(A)$.

hay



VIIUVINU 9. DIINII TIIUV VA IIIJ I IIUVINU TIURIII TUTER TIINII

$ \lambda_1\begin{pmatrix}a_{1,1}\ \vdots\ a_{n,1}\end{pmatrix}+\cdots+\lambda_{n-1}\begin{pmatrix}a_{1,n-1}\ \vdots\ a_{n,1}\end{pmatrix}=\begin{pmatrix}a_{1,n}\ \vdots\ a_n\end{pmatrix} $

Các yếu tố trên hàng thứ n của $A^*$, theo định nghĩa của ma trận phụ hợp, được xác định

như sau

$ \tilde{a}_{\ell,n} = (-1)^{\ell+n}\begin{vmatrix} a_{1,1} & \cdots & a_{1,n-1} \ \vdots & & \vdots \ a_{\ell-1,1} & \cdots & a_{\ell-1,n-1} \ a_{\ell+1,1} & \cdots & a_{\ell+1,n-1} \ \vdots & & \vdots \ a_{n,1} & \cdots & a_{n,n-1} \end{vmatrix} $

Ngoài ra, nếu 1 $\leq$ k $\leq$ n-1 thì

$ \tilde{a}_{\ell,k} = (-1)^{\ell+k} \begin{vmatrix}\na_{1,1} & \cdots & a_{1,k-1} & a_{1,k+1} & \cdots & a_{1,n} \\
\vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
a_{\ell-1,1} & \cdots & a_{\ell-1,k-1} & a_{\ell+1,k-1} & \cdots & a_{\ell-1,n} \\
a_{\ell+1,1} & \cdots & a_{\ell+1,k-1} & a_{\ell+1,k+1} & \cdots & a_{\ell+1,n} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
a_{n,1} & \cdots & a_{ $

Áp dụng tính chất đa tuyến tính và thay phiên (cho cột cuối cùng)

$ \tilde{a}_{\ell,k} = (-1)^{\ell+k}\begin{vmatrix} a_{1,1} & \cdots & a_{1,k-1} & a_{1,k+1} & \cdots & \lambda_k a_{1,k} \ \vdots & \ddots & \vdots & \ddots & \vdots \ a_{\ell-1,1} & \cdots & a_{\ell-1,k-1} & a_{\ell+1,k-1} & \cdots & \lambda_k a_{\ell-1,k} \ a_{\ell+1,1} & \cdots & a_{\ell+1,k-1} & a_{\ell+1,k+1} & \cdots & \lambda_k a_{\ell+1,n} \ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \ a_{n,1} & \cd $

Rồi đổi chỗ các cột (lưu ý dấu)



VIIUVINU 9. DINII TIIUV VA IID LIIUVNU TIIINII TUTEN TIINII

$ \tilde{a}_{\ell,k} = (-1)^{\ell+k+(n-k-1)}\lambda_k \begin{vmatrix} a_{1,1} & \cdots & a_{1,k-1} & a_{1,k} & a_{1,k+1} & \cdots & a_{1,n-1} \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ a_{\ell-1,1} & \cdots & a_{\ell-1,k-1} & a_{\ell+1,k} & a_{\ell+1,k-1} & \cdots & a_{\ell-1,n-1} \\ a_{\ell+1,1} & \cdots & a_{\ell+1,k-1} & a_{\ell+1,k} & a_{\ell+1,k+1} & \cdots & a_{\ell+1,n-1} $

Do đó hàng thứ k của $A^*$ bằng hàng thứ n của $A^*$ nhân với $-\lambda_k$, với mọi 1 $\leq$ k $\leq$ n-1. Mà

hàng thứ n của $A^*$ khác không, nên rank $A^* =$ 1.

Vậy, với A $\in$ M(n $\times$ n, $\mathbb{F})$, n $>$ 1:

rank(A) $=$ n $\Longrightarrow rank(\overline{A}) =$ n,

rank(A) $=$ n - 1 $\Longrightarrow rank(\tilde{A}) =$ 1,

rank(A) $<$ n-1 $\Longrightarrow rank(\tilde{A}) =$ 0.

Bài tập 3.46. Chứng minh rằng nếu các vector

$\alpha_i = (a_{i1}$, $a_{i2}$, $\dots$, $a_{in}) \in \mathbb{R}_n \quad$ (i $=$ 1, 2, $\dots$, s; s $\leq$ n),

thỏa mãn điều kiện $|a_{jj}| > \sum_{i \neq j} |a_{ij}|$, thì chúng độc lập tuyến tính.

Chứng minh. Tìm đọc định lý Gershgorin. Bài tập này là một hệ quả dễ dàng của định lý này.

$\Box$

Bài tập 3.47. Chứng minh rằng nếu A và B là các ma trận cùng số hàng và số cột thì

rank(A+B) $\le$ rank(A) + rank(B).

Chúng minh. $\alpha_1$, $\ldots$, $\alpha_n$ là các vector cột của A.

$\beta_1$, $\ldots$, $\beta_n$ là các vector cột của B.

Như vậy, các vector cột của (A + B) là $\alpha_1$ + $\beta_1$, $\ldots$, $\alpha_n$ + $\beta_n$.

Dặt $V_A = \text{span}(\alpha_1$, $\ldots$, $\alpha_n)$, $V_B = \text{span}(\beta_1$, $\ldots$, $\beta_n)$ và $V_{A+B} = \text{span}(\alpha_1$ + $\beta_1$, $\ldots$, $\alpha_n$ + $\beta_n)$.

$\gamma = \underbrace{\sum_{i=1}^{n} c_i (\alpha_i$ + $\beta_i)}_{=1} = \underbrace{\sum_{i=1}^{n} c_i \alpha_i}_{=1}$ + $\underbrace{\sum_{i=1}^{n} c_i \beta_i}_{=1} \in V_A$ + $V_B$.



VIIUVINU 9. DIINII TIIUV VA IID I IIUVINU TIIIINII TUTEN TIINII

Do đó $V_{A+B}$ là không gian con của $V_A$ + $V_B$.

$\dim V_{A+B} \leq \dim(V_A$ + $V_B) = \dim(V_A)$ + $\dim(V_B)$ - $\dim(V_A \cap V_B) \leq \dim(V_A)$ + $\dim(V_B)$.

Bất đẳng thức dim $V_{A+B} \leq \dim V_A$ + $\dim V_B$ tương đương với rank(A + B) $\leq \text{rank}(A)$ +

rank(B).

Bài tập 3.48. Chứng minh rằng mỗi ma trận có hạng r có thể viết thành tổng của r ma trận có

hạng 1, nhưng không thể viết thành tổng của một số ít hơn r ma trận có hạng 1.

Chứng minh. Giả sử ma trận A có n cột và các vector cột $\alpha_1$, $\ldots$, $\alpha_r$ của A độc lập tuyến tính

cực đại.

Khi đó, từng vector cột $\alpha_{r+1}$, $\ldots$, $\alpha_n$ của A có thể biểu thị tuyến tính theo $\alpha_1$, $\ldots$, $\alpha_r$. Ta đặt:

$ \left\{\n\begin{aligned}\n\alpha_{r+1} &amp;= a_1^{(r+1)}\alpha_1 + \dots + a_r^{(r+1)}\alpha_r, \\
\alpha_{r+2} &amp;= a_1^{(r+2)}\alpha_1 + \dots + a_r^{(r+2)}\alpha_r, \\
\vdots \\
\alpha_n &amp;= a_1^{(n)}\alpha_1 + \dots + a_r^{(n)}\alpha_r.\n\end{aligned}\n\right. $

Dựa vào những biểu thị tuyến tính này, ta có thể tách A thành tổng của r ma trận như sau:

$ A = \begin{pmatrix} \alpha_1 & \cdots & \alpha_r & \alpha_{r+1} & \cdots & \alpha_n \end{pmatrix} = \begin{pmatrix} \alpha_1 & \cdots & \alpha_r & \sum_{i=1}^r a_i^{(r+1)} \alpha_i & \cdots & \sum_{i=1}^r a_i^{(n)} \alpha_i \end{pmatrix} $

$ = \begin{pmatrix} \alpha_1 & \cdots & 0 & a_1^{(r+1)}\alpha_1 & \cdots & a_1^{(n)}\alpha_1 \end{pmatrix} $

+ $\cdots$

$ +\begin{pmatrix} 0 & \cdots & \alpha_r & a_r^{(r+1)}\alpha_r & \cdots & a_r^{(n)}\alpha_r \end{pmatrix} $

Như vậy A có thể viết thành tổng của r ma trận có hạng 1.

Giả sử phản chứng rằng A có thể viết thành tổng của s ma trận $A_i$, i $= \overline{1$, $s}$ có hạng 1, trong

$\mathrm{d}\acute{o}$ s $<$ r.

Theo bài toán 3.47, rank(A) $\leq \sum_{i=1}^{s}rank(A_i) =$ s $<$ r. Bất đẳng thức trên là sai vì rank(A) $=$ r.

Vậy A không thể viết thành tổng của ít hơn r ma trận có hạng 1.

Bài tập 3.49. Chứng minh bất đẳng thức Sylvester cho các ma trận vuông cỡ n bất kì A và B:

rank(A) + rank(B) - n $\le$ rank(AB) $\le min\{rank(A)$, $rank(B)\}$.

Chứng minh thứ nhất. Xét các tự đồng cấu tuyến tính S,T trên không gian vector $\mathbb{F}^n$ với ma

trận A, B theo cơ sở chính tắc của $\mathbb{F}^n$. Khi đó, rank(ST) $=$ rank(AB), rank(S) $=$ rank(A),

rank(T) $=$ rank(B).



VIIUVINU 9. DIINII TIIUV VA IIIJ I IIUVINU TIURIII TUTER TIINII

Theo định nghĩa hạng của ánh xạ tuyến tính, $\text{rank}(ST) = \dim \text{im}(ST)$. Mà $\text{im}(ST)$ là không

gian con của im(S), kéo theo dim im(ST) $\leq$ dim im(S). Bên cạnh đó, im(ST) $= im(S|<sub>im(T)</sub>)$ (trong

đó $S|_{\text{im}(T)}$ là hạn chế của S trong không gian vector im(T)). Do đó

$\dim \text{im}(ST) = \dim \text{im}(S|_{\text{im}(T)}) \leq \dim \text{im}(T)$.

Như vậy

rank(AB) $=$ rank(ST) $=$ dim im(ST) $\le min{dim$ im(S), dim $im(T)} = min{rank(A)$, $rank(B)}$.

Với bất đẳng thức còn lại, sử dụng định lý về số chiều của nhân và ảnh của tự đồng cấu tuyến

tính

$\dim \ker(ST) = \dim \mathbb{F}^n$ - $\dim \text{im}(ST)$

$=$ (dim ker(T) + dim im(T)) – dim im(ST),

$\dim \text{im}(T) = \dim \ker (S|_{\text{im}(T)})$ + $\dim \text{im}(ST)$

$= \dim(\ker(S) \cap \text{im}(T))$ + $\dim \text{im}(ST)$.

Mặt khác, dim(ker(S) $\cap$ im(T)) $\leq$ dim ker(S). Cùng với hai đẳng thức trên, chúng ta suy ra

$\dim \ker(ST) = \dim \ker(T)$ + $(\dim \text{im}(T)$ - $\dim \text{im}(ST))$

$= \dim \ker(T)$ + $\dim(\ker(S) \cap \text{im}(T))$

$\leq$ dim ker(T) + dim ker(S).

Do đó

rank(AB) $=$ rank(ST) $=$ n - dim ker(ST)

$\geq$ n - $(\dim \ker(T)$ + $\dim \ker(S))$

$=$ (n - $\dim \ker(T))$ + (n - $\dim \ker(S))$ - n

$=$ rank(T) + rank(S) - n

$=$ rank(B) + rank(A) - n.

Vậy ta có được điều cần chứng minh.

Chứng minh thứ hai. rank(A) $=$ a, rank(B) $=$ b.

Nhận xét rằng:

(i) Nếu đổi chỗ hai hàng của A thì hai hàng tương ứng của AB đổi chỗ,



$<u>UNUUNU$ 9. DINII TIIUU YA IID FIIUUNU TIUNII TUTEN $TINII</u>$

(ii) Nếu đổi chỗ hai cột của B thì hai cột tương ứng của AB đổi chỗ,

(iii) Nếu cộng một hàng của A với tổ hợp tuyến tính của các hàng còn lại thì hàng tương ứng

của AB cũng được cộng với tổ hợp tuyến tính của các hàng tương ứng còn lại (cùng hệ số

tổ hợp tuyến tính),

(iv) Nếu cộng một cột của B với tổ hợp tuyến tính của các hàng còn lại thì cột tương ứng của

AB cũng được cộng với tổ hợp tuyến tính của các cột tương ứng còn lại (cùng hệ số tổ hợp

tuyến tính).

Nhân một hàng của A với một vô hướng $\lambda$ khác không thì hàng tương ứng của AB cũng

(v)

được nhân với $\lambda$.

(vi) Nhân một cột của B với một vô hướng $\lambda$ khác không thì cột tương ứng của AB cũng được

nhân với $\lambda$.

Do đó, nếu thực hiện các phép biến đổi như trên, rank(A), rank(B), rank(AB) không đổi.

Vì những lý do trên, không mất tính tổng quát, ta có thể giả sử:

• a hàng đầu tiên của A độc lập tuyến tính (i)

$\bullet$ b cột đầu tiên của B độc lập tuyến tính (ii)

• n - a hàng cuối của A là các vector không (iii)

• n - b cột cuối của B là các vector không (iv)

$\alpha_1^T$, $\alpha_2^T$, $\ldots$, $\alpha_a^T$ là a vector hàng đầu tiên của A.

$\beta_1$, $\beta_2$, $\ldots$, $\beta_b$ là b vector cột đầu tiên của B.

$ \underbrace{\left(\begin{matrix} \beta_1 & \beta_2 & \cdots & \beta_b & 0 & \cdots & 0 \end{matrix}\right)}_{B} = \begin{pmatrix} \alpha_1^T \beta_1 & \cdots & \alpha_1^T \beta_b & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ \alpha_a^T \beta_1 & \cdots & \alpha_a^T \beta_b & 0 & \cdots & 0 \\ 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \end{pmatrix} $

$\alpha_a^T$

$ \begin{matrix} 0 & \cdots & 0 & 0 & \cdots & 0 \end{matrix} $

Do đó, rank(AB) $\le \min\{a$, $b\} = \min\{\text{rank}(A)$, $\text{rank}(B)\}$.

Nếu A $=$ 0 thì rank(A) +rank(B) - n $=rank(B)$ - n $\leq$ 0 $=rank(AB)$.



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

Ngược lại:

Ta sử dụng các phép biến đổi sơ cấp khác để đưa ma trận A về dạng đơn giản hơn:

(vii) Nhân một cột i, j của A với vô hướng c $\neq$ 0 và hàng i, j của B với $c^{-1}$. Biến đổi này không

làm thay đổi rank(A), rank(B) và không làm thay đổi AB.

(viii) Đổi chỗ hai cột i, j của A và đổi chỗ hai hàng i, j của B. Biến đổi này không làm thay đổi

rank(A), rank(B) và không làm thay đổi AB.

(ix) Cộng thêm cột j vào cột i của A và trừ hàng i khỏi hàng j của B. Biến đổi này không làm

thay đổi rank(A), rank(B) và không làm thay đổi AB.

Như vậy, cả chín phép biến đổi trên sẽ bảo toàn $\text{rank}(A)$, $\text{rank}(B)$, $\text{rank}(AB)$. Ta thực hiện

các biến đổi sau, với ma trận A có a hàng đầu tiên độc lập tuyến tính và n - a hàng còn lại bằng

không:

• Tồn tại $a_{ij} \neq$ 0 (vì A $\neq$ 0). Ta đổi chỗ hàng 1 và hàng i của A.

• Đổi chỗ cột 1 và cột j của A, đồng thời đổi chỗ hàng 1 và hàng j của B.

• Nhân hàng thứ 1 của A với một vô hướng khác không, sao cho yếu tố hàng 1 cột 1 bằng 1.

• Với 2 $\leq$ i $\leq$ a, cộng hàng i với hàng 1 (sau khi nhân hàng 1 với đối của yếu tố hàng i, cột

1). Đến lúc này tất cả yêu tố trên cột 1 đều bằng 0, trừ yếu tố hàng 1 cột 1.

• Tiếp tục quá trình trên, đến khi A đạt được dạng sau (hàng i có yếu tố hàng i, cột i bằng

1, các yếu tố đứng trước bằng 0):

$ \begin{pmatrix} 1 & * & \cdots & * & * & \cdots & * \\ 0 & 1 & \cdots & * & * & \cdots & * \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 & * & \cdots & * \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \end{pmatrix} $

• Đối với các cột i $>$ a. Bắt đầu từ hàng a, rồi đến a-1, $\ldots$, 1, ta áp dụng biến đối (vii), (ix)



VIIUVINU 9. DIINII TIIUV VA IID LIIUVINU TIURIII TUTER TIINII

để đưa A về dạng:

$ \begin{pmatrix} 1 & * & \cdots & * & 0 & \cdots & 0 \\ 0 & 1 & \cdots & * & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \end{pmatrix} $

• Đối với các hàng i $<$ a. Ta thực hiện biến đối (iii) để đưa A về dạng:

$ \begin{pmatrix} 1 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \end{pmatrix} $

Như vậy, ta chỉ cần chứng minh bất đẳng thức cho trường hợp A có dạng:

$ \begin{pmatrix} 1 & 0 & \cdots & 0 & 0 & \cdots & 0\ 0 & 1 & \cdots & 0 & 0 & \cdots & 0\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots\ 0 & 0 & \cdots & 1 & 0 & \cdots & 0\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \end{pmatrix} $

Phần còn lại của chứng minh được triển khai chi tiết hơn từ chứng minh sau: https://math.

stackexchange.com/questions/298836/sylvester-rank-inequality-operatornamerank-a-operatorna

rank(A) + rank(B) $=$ rank(A) + rank(AB + $B(I_n$ - A))

$\leq$ rank(A) + rank(AB) + $rank(B(I_n$ - A))



VIIUVINU 9. DINII TIIUV VA IID LIIUVNU TIIINII TUTEN TIINII

$ B(I_n-A)=\begin{pmatrix} b_{11} & b_{12} & \cdots & b_{1n} \\ b_{21} & b_{22} & \cdots & b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ b_{n1} & b_{n2} & \cdots & b_{nn} \end{pmatrix}\begin{pmatrix} 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ 0 & \cdots & 0 & 1 & \cdots & 0 \\ \vdots & \ddots & \vd $

Dắng thức trên chứng tỏ $rank(B(I_n$ - A)) $\leq$ n - $\text{rank}(A)$.

rank(A) + rank(B) $=$ rank(A) + rank(AB + $B(I_n$ - A))

$\leq$ rank(A) + rank(AB) + $rank(B(I_n$ - A))

(tiếp tục)

$\leq$ rank(A) + rank(AB) + n - rank(A)

$=$ rank(AB) + n.

Vậy $\text{rank}(A)$ + $\text{rank}(B)$ - n $\leq \text{rank}(AB)$.

Bài tập 3.50. Chứng minh rằng nếu trường $\mathbb$ F có đặc số khác 2 và A là một ma trận vuông cỡ n

với các yếu tố trong $\mathbb$ F sao cho $A^2 =$ E, thì rank(A + E) +rank(A - E) $=$ n. Tìm phản ví dụ cho

kết luận nói trên khi đặc số của F bằng 2.

Chúng minh. Nếu $Char(\mathbb{F}) \neq$ 2, áp dụng bất đẳng thức Sylvester và bài toán 3.47:

rank(A) $=$ rank(2A) $=$ rank(A+E+A-E) $\leq$ rank(A+E) + rank(A-E) $\leq$ n + $rank(A^2-E) =$ n.

Vì $A^2 =$ E nên A khả nghịch, do đó rank(A) $=$ n.

Nếu rank(A + E) + rank(A - E) $<$ n thì rank(A) $<$ n, mâu thuẫn với đẳng thức rank(A) $=$ n.

Do đó, rank(A + E) + rank(A - E) $=$ n.

Nếu $Char(\mathbb{F}) =$ 2, chọn A $=$ E.

A $=$ E và Char(F) $=$ 2 kéo theo A + E $=$ A - E $=$ 0, suy ra rank(A + E) + rank(A - E) $=$

0 $<$ n.

$\Box$

Bài tập 3.51. Tìm ma trận nghịch đảo của các ma trận sau đây bằng phương pháp định thức và

phương pháp biến đổi sơ cấp:

$ (a) \begin{pmatrix} 0 & 1 & 3 \\ 2 & 3 & 5 \\ 3 & 6 & 7 \end{pmatrix}, (b) \begin{pmatrix} 1 & 2 & -1 & -2 \\ 3 & 8 & 0 & -4 \\ 2 & 2 & -4 & -3 \\ 2 & 8 & 1 & 6 \end{pmatrix}. $



DIMIT THUS AN HEITHOOM THUMIT TO LEAR THAIL

Lời giải.

(a)

$ \left(\begin{array}{ccc|ccc} 0 & 1 & 3 & 1 & 0 & 0 \\ 2 & 3 & 5 & 0 & 1 & 0 \\ 3 & 6 & 7 & 0 & 0 & 1 \end{array}\right) \stackrel{r_3:=r_3-r_2}{\Longleftrightarrow} \left(\begin{array}{ccc|ccc} 0 & 1 & 3 & 1 & 0 & 0 \\ 2 & 3 & 5 & 0 & 1 & 0 \\ 1 & 3 & 2 & 0 & -1 & 1 \end{array}\right) $

$ \stackrel{r_1:=r_1+r_2}{\Longleftrightarrow} \left(\begin{array}{rrrrr} 1 & 4 & 5 & 1 & -1 & 1 \\ 0 & -3 & 1 & 0 & 3 & -2 \\ 1 & 3 & 2 & 0 & -1 & 1 \end{array}\right) \stackrel{r_3:=r_3-r_1}{\Longleftrightarrow} \left(\begin{array}{rrrrr} 1 & 4 & 5 & 1 & -1 & 1 \\ 0 & -3 & 1 & 0 & 3 & -2 \\ 0 & -1 & -3 & -1 & 0 & 0 \end{array}\right) $

$ \stackrel{r_3:=3r_3-r_2}{\Longleftrightarrow} \left(\begin{array}{rrrrrr} 1 & 4 & 5 & 1 & -1 & 1 \\ 0 & -3 & 1 & 0 & 3 & -2 \\ 0 & 0 & -10 & -3 & -3 & 2 \end{array}\right) \stackrel{r_2:=10r_2+r_3}{\Longleftrightarrow} \left(\begin{array}{rrrr} 1 & 4 & 5 & 1 & -1 & 1 \\ 0 & -30 & 0 & -3 & 27 & -18 \\ 0 & 0 & -10 & -3 & -3 & 2 \end{array}\right) $

$ \stackrel{r_2:=\frac{1}{3}r_2}{\Longleftrightarrow} \left(\begin{array}{rrrrr} 1 & 4 & 5 \\ 0 & -10 & 0 \\ 0 & 0 & -10 \end{array} \middle| \begin{array}{rrrrr} 1 & -1 & 1 \\ -1 & 9 & -6 \\ -3 & -3 & 2 \end{array} \right) \stackrel{r_1:=2r_1+r_3}{\Longleftrightarrow} \left(\begin{array}{rrrrr} 2 & 8 & 0 \\ 0 & -10 & 0 \\ 0 & 0 & -10 \end{array} \middle| \begin{array}{rrrrr} -1 & -5 & 4 \\ -1 & 9 & -6 \\ -3 & -3 & 2 \end{array} $

$r_1:=\frac{1}{2}r_1$

$ \stackrel{r_1:=r_1+\frac{4}{5}r_2}{\Longleftrightarrow} \left(\begin{array}{rrrrrr}2 & 0 & 0 & \frac{-9}{5} & \frac{11}{5} & \frac{-4}{5} \\ 0 & -10 & 0 & -10 & -3 & -3 & 2\end{array}\right) \stackrel{r_2:=\frac{-1}{10}r_2}{\Longleftrightarrow} \left(\begin{array}{rrrr}1 & 0 & 0 & \frac{-9}{10} & \frac{11}{10} & \frac{-2}{5} \\ 0 & 1 & 0 & \frac{1}{10} & \frac{-9}{10} & \frac{3}{5} \\ 0 & 0 & 1 & \frac{3}{10} $

Vậy

$ \begin{pmatrix} 0 & 1 & 3 \\ 2 & 3 & 5 \\ 2 & 6 & 7 \end{pmatrix} = \begin{pmatrix} \frac{-9}{10} & \frac{11}{10} & \frac{-2}{5} \\ \frac{1}{10} & \frac{-9}{10} & \frac{3}{5} \\ \frac{3}{5} & \frac{3}{5} & \frac{-1}{5} \end{pmatrix}. $

(b)

$ \begin{pmatrix} 1 & 2 & -1 & -2 & 1 & 0 & 0 & 0 \\ 3 & 8 & 0 & -4 & 0 & 1 & 0 & 0 \\ 2 & 2 & -4 & -3 & 0 & 0 & 1 & 0 \\ 3 & 8 & -1 & -6 & 0 & 0 & 0 & 1 \end{pmatrix} \stackrel{r_2:=r_2-3r_1}{\underset{r_4:=r_4-3r_1}{\rightleftharpoons}} \begin{pmatrix} 1 & 2 & -1 & -2 & 1 & 0 & 0 & 0 \\ 0 & 2 & 3 & 2 & -3 & 1 & 0 & 0 \\ 0 & -2 & -2 & 1 & -2 & 0 & $

$ \stackrel{r_3:=r_3+r_2}{\Longleftrightarrow} \left(\begin{array}{cccccc} 1 & 2 & -1 & -2 & 1 & 0 & 0 & 0 \\ 0 & 2 & 3 & 2 & -3 & 1 & 0 & 0 \\ 0 & 0 & 1 & 3 & -5 & 1 & 1 & 0 \\ 0 & 0 & -1 & -2 & 0 & -1 & 0 & 1 \end{array}\right) \stackrel{r_4:=r_4+r_3}{\Longleftrightarrow} \left(\begin{array}{cccccc} 1 & 2 & -1 & -2 & 1 & 0 & 0 & 0 \\ 0 & 2 & 3 & 2 & -3 & 1 & 0 & 0 \\ 0 & 0 & 1 & 3 & $



VIIUVINU 9. DINII TIIUV VA IID LIIUVINU TIURII TUTER TIINII

$ \begin{array}{c|cccc} r_1 := r_1 + 2r_4 \ r_2 := r_2 - 2r_4 \ r_3 := r_3 - 3r_4 \ r_4 \ \hline \begin{pmatrix} 1 & 2 & -1 & 0 & -9 & 0 & 2 & 2 \\ 0 & 2 & 3 & 0 & 7 & 1 & -2 & -2 \\ 0 & 0 & 1 & 0 & 10 & 1 & -2 & -3 \\ 0 & 0 & 0 & 1 & -5 & 0 & 1 & 1 \end{pmatrix} & \stackrel{r_1 := r_1 + r_3}{\overbrace{\longleftarrow}} \begin{pmatrix} 1 & 2 & 0 & 0 & 1 & 1 & 0 & -1 $

$ \begin{array}{c|cccccc} r_1:_{\overline{e}^{r_1}\xrightarrow{r_2}} \begin{pmatrix} 1 & 0 & 0 & 0 & 24 & 3 & -4 & -8 \\ 0 & 2 & 0 & 0 & -23 & -2 & 4 & 7 \\ 0 & 0 & 1 & 0 & 10 & 1 & -2 & -3 \\ 0 & 0 & 0 & 1 & -5 & 0 & 1 & 1 \end{pmatrix} & \stackrel{r_2:={\frac{1}{2}}r_2}{\Longleftrightarrow} \begin{pmatrix} 1 & 0 & 0 & 0 & 24 & 3 & -4 & -8 \\ 0 & 1 & 0 & 0 & {\frac{-23}{2}} & $

Vậy

$ \begin{pmatrix} 1 & 2 & -1 & -2 \\ 3 & 8 & 0 & -4 \\ 2 & 2 & -4 & -3 \\ 3 & 8 & -1 & -6 \end{pmatrix}^{-1} = \begin{pmatrix} 24 & 3 & -4 & -8 \\ \frac{-23}{2} & -1 & 2 & \frac{7}{2} \\ 10 & 1 & -2 & -3 \\ -5 & 0 & 1 & 1 \end{pmatrix}. $

Nghiên cứu tính tương thích của các hệ phương trình sau, tìm một nghiệm riêng và nghiệm

tổng quát của chúng:

Bài tập 3.52.

3x - 2y + 5z + 4t $=$ 2,

6x - 4y + 4z + 3t $=$ 3,

9x - 6y + 3z + 2t $=$ 4.

Lời giải. Thực hiện phép biến đổi sơ cấp trên ma trận hệ số mở rộng:

$ \left(\begin{array}{ccc|c}3 & -2 & 5 & 4 & 2\\6 & -4 & 4 & 3 & 3\\9 & -6 & 3 & 2 & 4\end{array}\right) \overset{r_2:=r_2-2r_1}{\Longleftrightarrow} \left(\begin{array}{ccc|c}3 & -2 & 5 & 4 & 2\\0 & 0 & -6 & -5 & -1\\0 & 0 & -12 & -10 & -2\end{array}\right) \overset{r_3:=r_3-2r_2}{\Longleftrightarrow} \left(\begin{array}{ccc|c}3 & -2 & 5 & 4 & 2\\0 & 0 & -6 & -5 & -1\\0 & 0 & 0 & 0 & 0\end{array}\right $

Theo định lý Kronecker-Capelli, hệ phương trình tuyến tính trên có nghiệm.

Một nghiệm riêng của hệ trên là:

(x, y, z, t) $=$ (1, 1, 1, -1).

Nghiệm của hệ phương trình tuyến tính thuần nhất:

(x, y, z, t) $=$ (a, b, -15a + 10b, 18a - 12b).



VIIUVING 9. DINII TIIUV VA IID I IIUVING TIURII TUTER TIINII

Nghiệm tổng quát của hệ phương trình tuyến tính trên là:

(x, y, z, t) $=$ (1 + a, 1 + b, 1 - 15a + 10b, -1 + 18a - 12b).

Bài tập 3.53.

8x + 6y + 5z + 2t $=$ 21,

3x + 3y + 2z + t $=$ 10,

4x + 2y + 3z + t $=$ 8,

3x + 5y + z + t $=$ 15,

7x + 4y + 5z + 2t $=$ 18.

Lời giải. Thực hiện phép biến đổi sơ cấp trên ma trận hệ số mở rộng:

$ \begin{pmatrix} 8 & 6 & 5 & 2 & 21 \ 3 & 3 & 2 & 1 & 10 \ \end{pmatrix} \xrightarrow[n]{\substack{r_2:=2r_2-r_1 \ r_3:=2r_3-r_1 \ r_4:=2r_4-r_1}} \begin{pmatrix} 8 & 6 & 5 & 2 & 21 \ -2 & 0 & -1 & 0 & -1 \ \end{pmatrix} \xrightarrow[n]{\substack{r_3:=r_3+r_2 \ r_4:=r_4-3r_2}} \begin{pmatrix} 8 & 6 & 5 & 2 & 21 \ -2 & 0 & -1 & 0 & -1 \ \end{pmatrix} $

$r_5 = -r_5$

$r_5 = r_5$ - $r_1$

$\overline{3}$

-5

-6

8

$\overline{0}$

$\overline{2}$

$\overline{0}$

$\overline{0}$

4

15

-3

12

$\overline{0}$

$\overline{3}$

9

$\overline{0}$

$\overline{0}$

$\overline{5}$

$\overline{4}$

$-3\$,

18

-2

$\mathfrak{Z}$

$\overline{5}$

$\mathbf{1}$

$\overline{2}$

$\overline{0}$

$\overline{7}$

$\overline{0}$

$\overline{2}$

$\overline{0}$

$\overline{0}$

$\overline{4}$

$21\$,

$6\phantom{.}6$

21

8

$6\phantom{.}6$

$\overline{2}$

21

6

$5\overline{)}$

$\overline{2}$

8

$\overline{2}$

8

$\overline{5}$

$\overline{5}$

-2

$\overline{0}$

$\overline{2}$

-1

$\overline{0}$

-1

$\overline{2}$

$\overline{0}$

$\overline{0}$

$\left( \right)$

$\mathbf{1}$

$\theta$

$r_2 = -r_2$

$r_3:=\frac{-1}{2}r_3$

$r_4:={r_4+2r_3}$

$r_5:=r_5-r_3$

3

-6

3

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\theta$

$\overline{0}$

$\theta$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\theta$

$\boldsymbol{0}$

$\overline{0}$

$\overline{2}$

$\mathfrak{Z}$

$\overline{0}$

$\overline{2}$

3

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

21

$\sqrt{2}$

$22\$,

$\overline{5}$

$\overline{5}$

21

6

$\overline{2}$

6

$\overline{0}$

$\overline{2}$

$\overline{0}$

8

8

$\theta$

$-5\$,

$\theta$

$\bigcap$

$-5\$,

$\overline{0}$

$\overline{2}$

$\overline{0}$

$\theta$

$\mathbf{1}$

$\Omega$

$\overline{0}$

$\cup$

$r_2:=r_2-2r_3$

$-5r_2-6r_5$

$r_3:=r_3-r_5$

$r_1 = r_1$

3

$\overline{0}$

3

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

3

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\theta$

$\theta$

$\overline{0}$

$\theta$

$\overline{0}$

$\theta$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\theta$

$\overline{0}$

$\overline{0}$

$\theta$

$\theta$

$\overline{0}$

$\theta$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\vert$ 1

$\overline{0}$

$\overline{0}$

$\overline{0}$

$\overline{0}$

Vậy hệ phương trình có nghiệm duy nhất:

(x, y, z, t) $=$ (3, 0, -5, 11).



