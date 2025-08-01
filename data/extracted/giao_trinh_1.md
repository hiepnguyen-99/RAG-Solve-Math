# Chương I

KHÔNG GIAN VÉCTO

Đối tượng ban đầu của môn Đại số tuyến tính là việc giải và biện luận các hệ

phương trình tuyến tính. Tuy vậy, để có thể hiểu thấu đáo điều kiện đảm bảo cho

một hệ phương trình tuyến tính có nghiệm và cấu trúc nghiệm của nó, người ta

đã đưa ra khái niệm không gian véctơ và khái niệm này đã trở thành một trong

những trụ cột của môn Đại số tuyến tính. Không gian vécto sau đó đã được sử

dụng phổ biến trong mọi lĩnh vực của toán học.

Khái niệm không gian véctơ

$\mathbf$ 1

Trong suốt chương này, ta luôn giả sử K là một trường.

### Định nghĩa 1.1 Tập hợp V \neq \emptyset được gọi là một không gian vécto trên K nếu nó

được trang bị hai phép toán, gồm

(a) Phép công vécto:

+: V $\times$ V $\rightarrow$ V

$(\alpha$, $\beta) \mapsto \alpha$ + $\beta$,

(b) Phép nhân vécto với vô hướng:

$\cdot: \mathbf{K} \times$ V $\to$ V

(a, $\alpha) \mapsto a\alpha;$



Các phép toán này thoả mãn những điều kiên (hoặc tiên đề) sau đây:

(V1) $(\alpha$ + $\beta)$ + $\gamma = \alpha$ + $(\beta$ + $\gamma)$,

$\forall \alpha$, $\beta$, $\gamma \in$ V,

(V2) $\quad \exists$ 0 $\in$ V : 0 + $\alpha = \alpha$ + 0 $= \alpha$,

$\forall \alpha \in$ V,

(V3) $\forall \alpha \in$ V, $\exists \alpha' \in$ V : $\alpha$ + $\alpha' = \alpha'$ + $\alpha =$ 0,

$\forall \alpha$, $\beta \in$ V,

(V4) $\alpha$ + $\beta = \beta$ + $\alpha$,

$\forall$ a, b $\in \mathbf{K}$, $\forall \alpha \in$ V,

(V5) (a + $b)\alpha = a\alpha$ + $b\alpha$,

(V6) $a(\alpha$ + $\beta) = a\alpha$ + $a\beta$,

$\forall$ a $\in \mathbf{K}$, $\forall \alpha$, $\beta \in$ V,

(V7) $a(b\alpha) = (ab)\alpha$,

$\forall$ a, b $\in \mathbf{K}$, $\forall \alpha \in$ V,

(V8) $1\alpha = \alpha$,

$\forall \alpha \in$ V.

Các phần tử của V được gọi là các vécto, các phần tử của $\bf{K}$ được gọi là các

$v\hat{o}$ huớng.

Bốn tiên đề đầu nói rằng V là một nhóm abel đối với phép cộng. Các tiên đề

(V5) - (V7) nói rằng phép nhân với vô hướng có tính phân phối đối với phép cộng

vô hướng, phân phối đối với phép cộng vécto và có tính chất của một "tác động".

Tiên đề (V8) nói rằng phép nhân với vô hướng được chuẩn hoá.

Một không gian vécto trên K còn được gọi là một K-không gian vécto, hay đơn

giản: một không gian vécto, nếu K đã rõ.

Khi $\mathbf{K} = \mathbf{R}$, V được gọi là một không gian vécto thực. Khi $\mathbf{K} = \mathbf{C}$, V được

gọi là một không gian vécto phức.

Ví dụ 1.2 (a) Các vécto tự do trong hình học sơ cấp với các phép toán cộng

vécto và nhân vécto với số thực lập nên một không gian vécto thực.

Tập hợp các đa thức $\mathbf{K}[X]$ (của một ẩn X, với hệ số trong K) với phép cộng

(b)

đa thức và phép nhân đa thức với vô hướng thông thường lập nên một không

gian vécto trên trường K.

K là một không gian vécto trên chính nó đối với phép công và phép nhân

(c)

của trường K. R vừa là một Q-không gian vécto vừa là một R-không gian

vécto. C là một không gian vécto đồng thời trên các trường Q, R và C.



(d) Tập hợp ${0}$ gồm chỉ một véctơ 0 là một không gian véctơ trên môi trường

$\mathbf{K}$, với các phép toán tầm thường

0 + 0 $=$ 0,

a0 $=$ 0, $\quad \forall$ a $\in \mathbf{K}$.

(e) Gọi $\mathbf{K}_n$ là tập hợp gồm tất cả các hàng n-thành phần $(x_1$, ..., $x_n)$ với $x_i \in \mathbf{K}$.

Nó lập nên một K-không gian véctơ với hai phép toán sau đây:

$(x_1$, ..., $x_n)$ + $(y_1$, ..., $y_n) = (x_1$ + $y_1$, ..., $x_n$ + $y_n)$,

$a(x_1$, ..., $x_n) = (ax_1$, ..., $ax_n)$, $\qquad$ a $\in \mathbf{K}$.

$ Gọi{\bf K}^n là tập hợp gồm tất cả các cột n\text{-th\`anh}phần\left(\begin{array}{c} x_1 \\ \vdots \\ x_n \end{array}\right), vớix_i\in {\bf K}. Nó <br/>ũng lập nên một{\bf K}\text{-kh\`ong}gian véctor với hiệu cho cho $

$ \left(\begin{array}{c} x_1 \\ \vdots \\ x_n \end{array}\right) + \left(\begin{array}{c} y_1 \\ \vdots \\ y_n \end{array}\right) = \left(\begin{array}{c} x_1 + y_1 \\ \vdots \\ x_n + y_n \end{array}\right), \qquad a \left(\begin{array}{c} x_1 \\ \vdots \\ x_n \end{array}\right) = \left(\begin{array}{c} ax_1 \\ \vdots \\ ax_n \end{array}\right). $

$ Để trình bày cho gọn, chúng ta sẽ đôi khi ký hiệu vécto\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} bởi (x_1, ..., x_n)^t. $

Một ma trận m hàng, n cột với các phần tử trong $\bf{K}$ là một bảng có dạng

(g)

$ \left( \begin{array}{cccc} a_{11} & a_{12} & \ldots & a_{1n} \end{array} \right) $

$ (a_{ij})_{m \times n} = \left( \begin{array}{cccc} \dots & \dots & \dots & \dots \ a_{21} & a_{22} & \dots & a_{2n} \ \dots & \dots & \dots & \dots \ a_{m1} & a_{m2} & \dots & a_{mn} \end{array} \right), $



trong đó $a_{ij} \in \mathbf{K}$. Gọi M(m $\times$ n, $\mathbf{K})$ là tập hợp tất cả các ma trận m hàng,

n cột với các phần tử trong $\mathbf$ K. Nó lập nên một $\mathbf$ K-không gian vécto với hai

phép toán sau dây:

$(a_{ij})_{m \times n}$ + $(b_{ij})_{m \times n} = (a_{ij}$ + $b_{ij})_{m \times n}$,

$a(a_{ij})_{m \times n} = (aa_{ij})_{m \times n}$.

Chúng ta sẽ nghiên cứu kỹ hơn về các ma trận ở chương sau.

Tập hợp C[a, b] các hàm thực liên tục trên đoạn [a, b] $\subset \mathbf{R}$ là một không gian

(h)

vécto thực với các phép toán thông thường

(f+g)(x) $=$ f(x) + g(x),

(a f)(x) $=$ af(x).

Giả sử V và W là các K-không gian vécto. Khi đó, V $\times$ W cũng là một

(i)

K-không gian vécto đối với các phép toán định nghĩa như sau

(v, w) + (v', w') $=$ (v + v', w + w')

a(v, w) $=$ (av, aw),

trong đó a $\in \mathbf{K}$, v, v' $\in$ V, w, w' $\in$ W. Không gian V $\times$ W được gọi là tích

trực tiếp của các không gian V và W

Giả sử V là một không gian vécto. Các tính chất sau đây được suy ngay từ

định nghĩa của không gian vécto.

(1) Phần tử trung lập của phép cộng 0 $\in$ V là duy nhất. Nó được gọi là vécto

$kh\hat{o}ng$.

Thật vậy, giả sử $0_1$ cũng là một phần tử trung lập của phép cộng trong V.

Khi đó

0 + $0_1 = 0_1$ (vì 0 là trung lập)

$=$ 0 (vì $0<sub>1</sub>$ là trung lập).

Vậy 0 $= 0_1$.



(2) Với mọi vécto $\alpha \in$ V, phần tử đối $\alpha'$ thoả mãn tiên đề (V3) là duy nhất. Nó

sẽ được ký hiệu là $(-\alpha)$.

Thật vậy, giả sử $\alpha'_1$ cũng là một phần tử đối của $\alpha$. Khi đó

$(\alpha'$ + $\alpha)$ + $\alpha'_1 =$ 0 + $\alpha'_1 = \alpha'_1$ (vì $\alpha'$ là một phần tử đối)

$= \alpha'$ + $(\alpha$ + $\alpha'_1)$ (theo tiên đề (V1))

$= \alpha'$ + 0 $= \alpha'$ (vì $\alpha'_1$ là một phần tử đối).

Như vậy, $\alpha' = \alpha'_1$.

Ta định nghĩa: $\alpha$ - $\beta = \alpha$ + $(-\beta)$.

Ta có các quy tắc giản ước và chuyển vế:

(3)

$\alpha$ + $\gamma = \beta$ + $\gamma \implies \alpha = \beta$,

$\alpha$ + $\beta = \gamma \implies \alpha = \gamma$ - $\beta$.

Thật vậy, cộng $(-\gamma)$ vào hai vế của đẳng thức $\alpha$ + $\gamma = \beta$ + $\gamma$ và cộng $(-\beta)$

vào hai về của đẳng thức $\alpha$ + $\beta = \gamma$ ta thu được điều phải chứng minh.

(4) $0\alpha =$ 0 và a0 $=$ 0.

Thật vậy,

$0\alpha$ + 0 $= 0\alpha =$ (0 + $0)\alpha = 0\alpha$ + $0\alpha$.

Từ đó, theo luật giản ước, $0\alpha =$ 0. Tương tự,

a0 + 0 $=$ a0 $=$ a(0 + 0) $=$ a0 + a0.

Cũng theo luật giản ước, ta có a0 $=$ 0.

(5) Nếu $a\alpha =$ 0 (với a $\in \mathbf{K}$, $\alpha \in$ V), thì hoặc a $=$ 0 hoặc $\alpha =$ 0.

Thật vậy, giả sử a $\neq$ 0, nhân hai vế của đẳng thức đã cho với $a^{-1} \in \mathbf{K}$ ta có

$\alpha = 1\alpha = (a^{-1}a)\alpha = a^{-1}(a\alpha) = a^{-1}0 =$ 0.



(6) $(-a)\alpha = a(-\alpha) = -(a\alpha)$, $\forall$ a $\in \mathbf{K}$, $\alpha \in$ V.

Thật vậy,

$a\alpha$ + $(-a)\alpha =$ (a + $(-a))\alpha =$ 0

Từ đó, $(-a)\alpha = -(a\alpha)$. Tương tự,

$a\alpha$ + $a(-\alpha) = a(\alpha$ + $(-\alpha)) =$ a0 $=$ 0.

Do đó, $a(-\alpha) = -(a\alpha)$.

(7) $(\sum_{i=1}^{m} a_i)(\sum_{i=1}^{n} \alpha_i) = \sum_{i=1}^{m} \sum_{i=1}^{n} (a_i \alpha_i)$.

Dằng thức này có thể được chứng minh bằng quy nạp theo m và n, trên cơ

sở sử dụng các tiên đề (V5) và (V6).

Độc lập tuyến tính và phụ thuộc tuyến tính

$\boldsymbol{2}$

Trong suốt tiết này ta luôn giả sử V là một không gian vécto trên trường $\mathbf$ K.

### Định nghĩa 2.1 (Tổ hợp tuyến tính, biểu thị tuyến tính)

(a) Một tổ hợp tuyến tính của các vécto $\alpha_1$, ..., $\alpha_n \in$ V là một biểu thức dạng

$\sum_{i=1}^n a_i \alpha_i = a_1 \alpha_1$ + $\cdots$ + $a_n \alpha_n$,

trong đó $a_i \in \mathbf{K}$.

(b) Giả sử $\alpha = a_1 \alpha_1$ + $\cdots$ + $a_n \alpha_n \in$ V. Đằng thức đó được gọi là một biểu thị

tuyến tính của $\alpha$ qua các vécto $\alpha_1$, ..., $\alpha_n$ (hoặc qua hệ vécto $(\alpha_1$, ..., $\alpha_n))$. Khi

có đẳng thức đó, ta nói $\alpha$ biểu thị tuyến tính được qua $\alpha_1$, ..., $\alpha_n$.

Nhận xét: Một véctơ có thể có nhiều biểu thị tuyến tính khác nhau qua một hệ

vécto.

Ta nói $hệ(\alpha_1,...,\alpha_n)$ biểu thị tuyến tính được qua $hệ(\beta_1,...,\beta_m)nếu$ mỗi véctor

$\alpha_i$, trong đó 1 $\leq$ i $\leq$ n, biểu thị tuyến tính được qua $(\beta_1$, ..., $\beta_m)$.



Giả sử hệ $(\alpha_1$, ..., $\alpha_n)$ biểu thị tuyến tính được qua hệ $(\beta_1$, ..., $\beta_m)$, và hệ $(\beta_1$, ..., $\beta_m)$

biểu thị tuyến tính được qua hệ $(\gamma_1$, ..., $\gamma_k)$. Khi đó, rõ ràng $(\alpha_1$, ..., $\alpha_n)$ cũng biểu

thị tuyến tính được qua hệ $(\gamma_1$, ..., $\gamma_k)$.

### Định nghĩa 2.2 (Độc lập tuyến tính và phụ thuộc tuyến tính.)

(a) Hệ $(\alpha_1$, ..., $\alpha_n)$ được gọi là độc lập tuyến tính nếu hệ thức

$a_1\alpha_1$ + $\cdots$ + $a_n\alpha_n =$ 0

chỉ xảy ra khi $a_1 = \cdots = a_n =$ 0.

(b) Hệ $(\alpha_1$, ..., $\alpha_n)$ được gọi là phụ thuộc tuyến tính nếu nó không độc lập tuyến

tính.

Nếu hệ $(\alpha_1$, ..., $\alpha_n)$ độc lập (hoặc phụ thuộc) tuyến tính, ta cũng nói các vécto

$\alpha_1$, ..., $\alpha_n$ độc lập (hoặc phụ thuộc) tuyến tính.

Dằng thức $a_1\alpha_1$ + $\cdots$ + $a_n\alpha_n =$ 0 được gọi là một ràng buộc tuyến tính giữa

các vécto $\alpha_1$, ..., $\alpha_n$. Nếu $a_1 = \cdots = a_n =$ 0 thì ta gọi ràng buộc đó là tầm thường.

Theo định nghĩa, hệ $(\alpha_1$, ..., $\alpha_n)$ độc lập tuyến tính nếu và chỉ nếu mọi ràng buộc

tuyến tính giữa $\alpha_1$, ..., $\alpha_n$ đều là ràng buộc tầm thường. Hệ $(\alpha_1$, ..., $\alpha_n)$ phụ thuộc

tuyến tính khi và chỉ khi có các vô hướng $a_1$, ..., $a_n \in \mathbf{K}$ không đồng thời bằng 0

$\mathrm{d}\mathring{\mathrm{e}}$ cho

$a_1\alpha_1$ + $\cdots$ + $a_n\alpha_n =$ 0,

nghĩa là có một ràng buộc tuyến tính không tầm thường giữa các vécto $\alpha_1$, ..., $\alpha_n$.

(a) Trong không gian các vécto tự do của hình học sơ cấp, hệ 2 vécto

Ví du 2.3

là độc lập tuyến tính nếu và chỉ nếu chúng không đồng phương, hệ 3 véctơ

là độc lập tuyến tính khi và chỉ khi chúng không đồng phẳng, hê 4 vécto bất

kỳ luôn luôn phụ thuộc tuyến tính.



(b) Trong không gian $\mathbf{R}_2$, các vécto $e_1 =$ (1,0), $e_2 =$ (0,1) độc lập tuyến tính.

Thật vậy, hệ thức

$a_1e_1$ + $a_2e_2 = (a_1$, $a_2) =$ (0, 0)

xảy ra khi và chỉ khi $a_1 = a_2 =$ 0.

Với mọi $\alpha \in \mathbf{R}_2$, các vécto $e_1$, $e_2$, $\alpha$ phụ thuộc tuyến tính. Thật vậy, nếu

$\alpha =$ (a, b) thi

$\alpha$ - $ae_1$ - $be_2 =$ 0.

Hãy xét xem các véc tơ sau đây độc lập hay phụ thuộc tuyến tính trong $C_3:$

(c)

$\alpha_1 =$ (5,3,4),

$\alpha_2 =$ (3, 2, 3),

$\alpha_3 =$ (8,3,1).

Ta muốn tìm xem có hay không một ràng buộc tuyến tính không tầm thường

giữa các vécto đó, tức là có hay không các số phức $x_1$, $x_2$, $x_3$ không đồng thời

$b\overset{\simeq}{\text{ang}}$ 0 sao cho:

$x_1(5,3,4)$ + $x_2(3,2,3)$ + $x_3(8,3,1) =$ (0,0,0).

Phương trình véctơ đó tương đương với hệ phương trình

$ \begin{cases}\n5x_1 + 3x_2 + 8x_3 &= 0 \\
3x_1 + 2x_2 + 3x_3 &= 0 \\
4x_1 + 3x_2 + 1x_3 &= 0.\n\end{cases} $

Hệ phương trình này có thể giải bằng cách khử thông thường. Trước hết,

nhân phương trình cuối lần lượt với (-8)và (-3)rồi cộng vào các phương

trình thứ nhất và thứ hai, ta thu được:

$ \begin{cases}\n-27x_1 - 21x_2 = 0 \\
-9x_1 - 7x_2 = 0 \\
4x_1 + 3x_2 + x_3 = 0.\n\end{cases} $



Hai phương trình đầu của hệ này tương đương với nhau. Do đó, một nghiệm

không tầm thường của hệ này là:

$x_1 =$ 7, $x_2 =$ -9, $x_3 =$ -1.

Như vậy, ba vécto đã cho phụ thuộc tuyến tính.

Nhận xét: Từ ví dụ trên ta thấy rằng việc xét xem một hệ vécto độc lập hay phụ

thuộc tuyến tính được đưa về việc giải một hệ phương trình tuyến tính thuần nhất.

Tương tự, việc xét xem một véctơ có biểu thị tuyến tính được hay không qua một

hệ véctơ được đưa về việc giải một hệ phương trình tuyến tính (nói chung không

thuần nhất).

Lý thuyết tổng quát về hệ phương trình tuyến tính sẽ được trình bày ở Chương III

của cuốn sách này.

Các tính chất sau đây là hệ quả trực tiếp của các định nghĩa.

Các tính chất:

Hệ một véctơ $(\alpha)$ phụ thuộc tuyến tính nếu và chỉ nếu $\alpha =$ 0.

(1)

Thật vậy, vì 1 $\cdot$ 0 $=$ 0 là một ràng buộc tuyến tính không tầm thường, nên hệ

(0) phụ thuộc tuyến tính. Ngược lại, giả sử $(\alpha)$ phụ thuộc tuyến tính, tức là

có a $\neq$ 0 sao cho $a\alpha =$ 0. Nhân hai vế với $a^{-1}$ ta có

$\alpha = (a^{-1}a)\alpha = a^{-1}(a\alpha) = a^{-1}0 =$ 0.

(2) Với $n>1,hệ (\alpha_1,...,\alpha_n)phụ$ thuộc tuyến tính nếu và chỉ nếu một véctơ nào

đó của hệ biểu thị tuyến tính được qua các vécto còn lại của hệ.

Thật vậy, giả sử có một ràng buộc tuyến tính không tầm thường

$a_1\alpha_1$ + $\cdots$ + $a_n\alpha_n =$ 0.

Nếu $a_i \neq$ 0, ta nhân hai vế của đẳng thức trên với $a_i^{-1}$ và thu được

$\alpha_i = \sum_{j \neq i} (a_i^{-1} a_j) \alpha_j$.



Ngược lại, nếu $\alpha_i$ biểu thị tuyến tính được qua hệ $(\alpha_1$, ..., $\alpha_{i-1}$, $\alpha_{i+1}$, ..., $\alpha_n)$,

tức là có các vô hướng $b_i$ sao cho

$\alpha_i = b_1 \alpha_1$ + $\cdots$ + $b_{i-1} \alpha_{i-1}$ + $b_{i+1} \alpha_{i+1}$ + $\cdots$ + $b_n \alpha_n$,

thì ta có ràng buộc tuyến tính không tầm thường

$b_1\alpha_1$ + $\cdots$ + $b_{i-1}\alpha_{i-1}$ + $(-1)\alpha_i$ + $b_{i+1}\alpha_{i+1}$ + $\cdots$ + $b_n\alpha_n =$ 0.

Do đó, hệ $(\alpha_1$, ..., $\alpha_n)$ phụ thuộc tuyến tính.

(3) Mỗi hệ con của một hệ độc lập tuyến tính cũng là một hệ độc lập tuyến tính.

Thật vậy, giả sử $(\alpha_1$, ..., $\alpha_n)$ là một hệ độc lập tuyến tính. Xét một ràng buộc

tuyến tính bất kỳ

$a_{i_1}\alpha_{i_1}$ + $\cdots$ + $a_{i_k}\alpha_{i_k} =$ 0

giữa các vécto của một hệ con $(\alpha_{i_1}$, ..., $\alpha_{i_k})$. Ta coi nó là một ràng buộc tuyến

tính $\sum_i a_i \alpha_i =$ 0 giữa các vécto $(\alpha_1$, ..., $\alpha_n)$ bằng cách chọn $a_i =$ 0 với mọi

i $\neq i_1$, ..., $i_k$. Bởi vì hệ $(\alpha_1$, ..., $\alpha_n)$ độc lập tuyến tính, nên tất cả các hệ số

của ràng buộc đều bằng 0:

$a_1 = a_2 = \cdots = a_n =$ 0.

Do đó, hệ con $(\alpha_{i_1}$, ..., $\alpha_{i_k})$ độc lập tuyến tính.

Một cách phát biểu khác của tính chất trên là như sau:

Mỗi hệ véctơ chứa một hệ con phụ thuộc tuyến tính cũng là một hệ phụ thuộc

(4)

tuyến tính. Nói riêng, mỗi hệ chứa véctơ 0 đều phụ thuộc tuyến tính.

(5) Giả sử hệ $(\alpha_1$, ..., $\alpha_n)$ độc lập tuyến tính. Khi đó hệ $(\alpha_1$, ..., $\alpha_n$, $\beta)$ phụ thuộc

tuyến tính nếu và chỉ nếu $\beta$ biểu thị tuyến tính được qua $(\alpha_1$, ..., $\alpha_n)$. Trong

trường hợp đó, biểu thị tuyến tính này là duy nhất.



Thật vậy, nếu $(\alpha_1$, ..., $\alpha_n$, $\beta)$ phụ thuộc tuyến tính, thì có một ràng buộc tuyến

tính không tầm thường

$a_1\alpha_1$ + $\cdots$ + $a_n\alpha_n$ + $b\beta =$ 0.

Khi đó, b $\neq$ 0, vì nếu trái lại thì có một ràng buộc tuyến tính không tầm

thường $a_1\alpha_1$ + $\cdots$ + $a_n\alpha_n =$ 0 giữa các vécto của hệ độc lập tuyến tính

$(\alpha_1$, ..., $\alpha_n)$. Điều này vô lý. Vì b $\neq$ 0, nên ta có biểu thị tuyến tính sau đây

của $\beta$ qua $(\alpha_1$, ..., $\alpha_n):$

$\beta = -\sum_{i=1}^{n} (b^{-1}a_i)\alpha_i$.

Ngược lại, mỗi biểu thị tuyến tính như thế

$\beta = \sum_{i=1}^{n} b_i \alpha_i$

đều dẫn tới một ràng buộc tuyến tính không tầm thường $\sum_{i=1}^{n} b_i \alpha_i$ - $\beta =$ 0

giữa các véto của $hệ(\alpha_1,...,\alpha_n,\beta)$. Do đó, hệ này phụ thuộc tuyến tính.

Giả sử có hai biểu thị tuyến tính của $\beta$ qua hệ $(\alpha_1$, ..., $\alpha_n):$

$\beta = b_1 \alpha_1$ + $\cdots$ + $b_n \alpha_n$

$= b'_1\alpha_1$ + $\cdots$ + $b'_n\alpha_n$.

Khi đó 0 $= (b_1$ - $b'_1)\alpha_1$ + $\cdots$ + $(b_n$ - $b'_n)\alpha_n$. Do $(\alpha_1$, ..., $\alpha_n)$ độc lập tuyến tính,

nên hệ thức trên kéo theo

$b_1 = b'_1$, $\cdots$, $b_n = b'_n$.

Nhận xét 2.4 Các khái niệm tổ hợp tuyến tính, biểu thị tuyến tính, độc lập tuyến

tính, phụ thuộc tuyến tính được mở rộng cho hệ tuỳ ý (có thể có vô hạn vécto)

nhur sau.

Giả sử $(\alpha_i)_{i\in I}$ là một hệ vécto tuỳ ý của K-không gian vécto V. Một tổ hợp

tuyến tính của hệ này là một tổng $\sum_{i \in I} a_i \alpha_i$ trong đó $a_i \in \mathbf{K}$, và hầu hết (có thể



trừ một số hữu hạn) $a_i$ đều bằng 0. Như thế, tổng này thật ra là một tổng hữu

han, và do đó có nghĩa trong V.

Trên cơ sở đó, các khái niệm biểu thị tuyến tính, độc lập tuyến tính, phụ thuộc

tuyến tính được định nghĩa đối với họ đó.

Ví dụ: Trong không gian vécto các đa thức K[X], hệ vô hạn vécto (1, X, $X^2$, ...)

là một hệ độc lập tuyến tính.

Cơ sở và số chiều của không gian véctơ

3

Số chiều của một không gian véctơ là chỉ số đo độ "lớn", độ "thoải mái" của không

gian vécto dó.

### Định nghĩa 3.1 (a) Một hệ vécto của V được gọi là một hệ sinh của V nếu mọi

vécto của V đều biểu thị tuyến tính được qua hệ đó.

(b) Một hệ vécto của V được gọi là một cơ sở của V nếu mọi vécto của V đều

biểu thị tuyến tính duy nhất qua hệ này.

Như vậy, mỗi cơ sở đều là một hệ sinh. Dưới đây ta sẽ nghiên cứu sâu hơn mối

quan hệ giữa các khái niệm hệ sinh, cơ sở và độc lập tuyến tính.

Ta cần thuật ngữ sau đây: Một hệ vécto của không gian V được gọi là độc lập

tuyến tính cực đại nếu nó độc lập tuyến tính và nếu thêm bất kỳ véctơ nào của V

vào hệ đó thì hệ mới thu được trở thành phụ thuộc tuyến tính.

### Dịnh lý 3.2 Cho hệ hữu hạn các vécto (\alpha_1, ..., \alpha_n) của V. Khi đó các khẳng định

sau đây là tương đương:

(i) $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở của V.

(ii) $(\alpha_1$, ..., $\alpha_n)$ là một hệ sinh độc lập tuyến tính của V.

(iii) $(\alpha_1$, ..., $\alpha_n)$ là một hệ véctơ độc lập tuyến tính cực đại của V.



Chứng minh: (i) $\implies$ (ii) : $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở của V nên nó là một hệ sinh

của V. Hơn nữa, vécto 0 có biểu thị tuyến tính duy nhất qua $(\alpha_1$, ..., $\alpha_n):$

0 $= 0\alpha_1$ + $\cdots$ + $0\alpha_n$.

Nói cách khác, hệ thức $a_1\alpha_1$ + $\cdots$ + $a_n\alpha_n =$ 0 tương đương với $a_1 = a_2 = \cdots =$

$a_n =$ 0. Điều này có nghĩa là hệ $(\alpha_1$, ..., $\alpha_n)$ độc lập tuyến tính.

(iii) $\implies$ (iii): Mọi vécto $\beta \in$ V đều biểu thị tuyến tính được qua $(\alpha_1$, ..., $\alpha_n)$,

cho nên hệ $(\alpha_1$, ..., $\alpha_n$, $\beta)$ phụ thuộc tuyến tính.

(iii) $\Longrightarrow$ (i) : Vì hệ $(\alpha_1$, ..., $\alpha_n)$ độc lập tuyến tính cực đại nên mỗi vécto $\beta \in$ V

đều biểu thị tuyến tính qua $(\alpha_1$, ..., $\alpha_n)$. Nói cách khác, hệ này sinh ra V. Biểu thị

tuyến tính của mỗi vécto $\beta \in$ V qua hệ độc lập tuyến tính $(\alpha_1$, ..., $\alpha_n)$ là duy nhất.

$\Box$

### Định nghĩa 3.3 Không gian vécto V được gọi là hữu hạn sinh nếu nó có một hệ

sinh gồm hữu hạn phần tử.

### Dịnh lý 3.4 Giả sử V \neq \{0\} là một không gian vécto hữu hạn sinh. Khi đó, V

có một cơ sở gồm hữu hạn phần tử. Hơn nữa, mọi cơ sở của V đều có số phần

tử bằng nhau.

Trên cơ sở kết quả này, ta đi đến định nghĩa sau đây.

### Định nghĩa 3.5 (i) Số phần tử của mỗi cơ sở của K-không gian vécto hữu hạn

sinh V $\neq \{0\}$ được gọi là số chiều (hay thứ nguyên) của V trên trường K,

và được ký hiệu là dimV, hoặc rõ hơn $\dim_K$ V. Nếu V $= \{0\}$, ta quy ước

$\dim$ V $=$ 0.

(ii) Nếu V không có một cơ sở nào gồm hữu hạn phần tử thì nó được gọi là một

không gian vécto vô hạn chiều.

Để chuẩn bị cho việc chứng minh định lý trên, ta cần bổ đề sau đây.



Bổ đề 3.6 Trong không gian vécto V, giả sử hệ vécto $(\alpha_1$, ..., $\alpha_r)$ độc lập tuyến

tính và biểu thị tuyến tính được qua hệ $(\beta_1$, ..., $\beta_s)$. Khi đó r $\leq$ s.

Chứng minh: Theo giả thiết, có một biểu thị tuyến tính

$\alpha_1 = a_1 \beta_1$ + $\cdots$ + $a_s \beta_s \qquad (a_i \in \mathbf{K})$.

Vì $hệ(\alpha_1$, ..., $\alpha_r)độc$ lập tuyến tính, $nên\alpha_1 \neq$ 0. Do đó, có ít nhất một vô hướng

$a_i \neq$ 0. Không giảm tổng quát, ta giả sử $a_1 \neq$ 0. Khi đó, $\beta_1$ biểu thị tuyến tính

được qua hệ $(\alpha_1$, $\beta_2$, ..., $\beta_s):$

$\beta_1 = a_1^{-1} \alpha_1$ - $\sum_{i=2}^n (a_1^{-1} a_i) \beta_i$.

Như vậy, hệ $(\alpha_1$, ..., $\alpha_r)$ biểu thị tuyến tính qua hệ $(\beta_1$, ..., $\beta_s);$ hệ thứ hai lại biểu

thị tuyến tính qua hệ $(\alpha_1$, $\beta_2$, ..., $\beta_s)$. Hệ quả là $(\alpha_1$, ..., $\alpha_r)$ biểu thị tuyến tính qua

$(\alpha_1,\beta_2,...,\beta_s)$.

Ta sẽ chứng minh rằng $(\alpha_1,...,\alpha_r)$ biểu thị tuyến tính $qua(\alpha_1,...,\alpha_i,\beta_{i+1},...,\beta_s)$

với mọi i $\le \min\{r$, $s\}$ (sai khác một phép đánh số lại các vécto $\beta_1$, ..., $\beta_s)$. Thật vậy,

ở trên ta đã chứng minh khẳng định này cho i $=$ 1. Giả sử khẳng định đã được

chứng minh cho i. Ta sẽ chứng minh nó còn đúng cho i+1, nếu số này $\leq \min\{r,s\}$.

Theo giả thiết quy nạp, $\alpha_{i+1}$ biểu thị tuyến tính qua $(\alpha_1$, ..., $\alpha_i$, $\beta_{i+1}$, ..., $\beta_s):$

$\alpha_{i+1} = b_1 \alpha_1$ + $\cdots$ + $b_i \alpha_i$ + $c_{i+1} \beta_{i+1}$ + $\cdots$ + $c_s \beta_s$.

Có ít nhất một vô hướng $c_j \neq$ 0, bởi vì nếu trái lại thì $\alpha_{i+1}$ biểu thị tuyến tính

$qua(\alpha_1,...,\alpha_i)$, điều này trái với giả thiết $hệ(\alpha_1,...,\alpha_r)độc$ lập tuyến tính. Nếu

cần thì đánh số lại các vécto $\beta_{i+1},...,\beta_s$, ta có thể giả sử mà không giảm tổng

quát $c_{i+1} \neq$ 0. Kết hợp điều này với đẳng thức trên ta có một biểu thị tuyến

tính của $\beta_{i+1}$ qua $(\alpha_1$, ..., $\alpha_{i+1}$, $\beta_{i+2}$, ..., $\beta_s)$. Vì $(\alpha_1$, ..., $\alpha_r)$ biểu thị tuyến tính qua

$(\alpha_1$, ..., $\alpha_i$, $\beta_{i+1}$, ..., $\beta_s)$, hệ này lại biểu thị tuyến tính qua $(\alpha_1$, ..., $\alpha_{i+1}$, $\beta_{i+2}$, ..., $\beta_s)$,

nên $(\alpha_1$, ..., $\alpha_r)$ biểu thị tuyến tính qua $(\alpha_1$, ..., $\alpha_{i+1}$, $\beta_{i+2}$, ..., $\beta_s)$.



$Nếur\,>\,s,\,áp$ dụng điều vừa được chứng minh $vớii\,=\,s,\,ta$ khẳng định

$(\alpha_1$, ..., $\alpha_r)$ biểu thị tuyến tính qua $(\alpha_1$, ..., $\alpha_s)$. Điều này mâu thuẫn với tính độc

lập tuyến tính của hệ $(\alpha_1$, ..., $\alpha_r)$. Như vậy, ta có r $\leq$ s.

$\Box$

Chứng minh Dinh lý 2.5.

Giả sử $(\gamma_1$, ..., $\gamma_s)$ là một hệ sinh hữu hạn của V. Vì V $\neq \{0\}$, nên có véctor

$\alpha \neq$ 0 trong V. Hệ gồm một véctơ khác không $(\alpha_1)$ độc lập tuyến tính. Nếu hệ này

không độc lập tuyến tính cực đại, thì có hệ $(\alpha_1$, $\alpha_2)$ độc lập tuyến tính.

Giả sử $(\alpha_1$, ..., $\alpha_r)$ là một hệ độc lập tuyến tính trong V. Hệ này biểu thị tuyến

tính qua $(\gamma_1$, ..., $\gamma_s)$. Theo Bổ đề 3.6, ta có r $\leq$ s. Như thế quá trình chọn các

vécto $\alpha_1$, $\alpha_2$, ... để thu được một hệ độc lập tuyến tính phải dừng lại sau một số

hữu hạn bước. Ta có một hệ vécto $(\alpha_1$, ..., $\alpha_n)$ độc lập tuyến tính cực đại trong V,

với n $\leq$ s. Theo Định lý 3.2, hệ này là một cơ sở của V.

Giả sử $(\beta_1$, ..., $\beta_m)$ cũng là một cơ sở của V. Vì $(\alpha_1$, ..., $\alpha_n)$ độc lập tuyến tính

và biểu thị tuyến tính được qua $(\beta_1$, ..., $\beta_m)$, nên theo Bổ đề 3.6, ta có n $\leq$ m. Tráo

đổi vai trò của hai cơ sở nói trên, ta cũng có m $\leq$ n. Như vậy, m $=$ n.

$\Box$

Ví dụ 3.7 (a) $\mathbf{K}^n$ là một K-không gian vécto n chiều. Các vécto sau đây lập

nên một cơ sở, được gọi là cơ sở chính tắc của không gian $\mathbf{K}^{n}:$

$ e_1 = \left( \begin{array}{c} 1 \ 0 \ \vdots \ 0 \end{array} \right), \;\; e_2 = \left( \begin{array}{c} 0 \ 1 \ \vdots \ 0 \end{array} \right), ..., e_n = \left( \begin{array}{c} 0 \ 0 \ \vdots \ 1 \end{array} \right). $

Thật vậy, vécto 0 $\in \mathbf{K}^n$ là vécto có mọi thành phần bằng 0 $\in \mathbf{K}$, vì thế hệ

thức

$ a_1e_1 + \cdots + a_ne_n = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} $



xảy ra khi và chỉ khi $a_1 = a_2 = \cdots = a_n =$ 0. Như vậy, hệ $(e_1$, $e_2$, ..., $e_n)$ độc lập

tuyến tính trong $\mathbf{K}^n$. Hệ này sinh ra $\mathbf{K}^n$, bởi vì mỗi vécto $\beta = (b_1$, $b_2$, ..., $b_n)^t$

đều có biểu thị tuyến tính

$\beta = b_1 e_1$ + $b_2 e_2$ + $\cdots$ + $b_n e_n$.

C là một C-không gian vécto 1 chiều với cơ sở (1). Đồng thời C cũng là một

(b)

R-không gian vécto 2 chiều với cơ sở (1, i), trong đó i là đơn vị ảo. Điều này

suy từ chỗ mọi số phức z đều có biểu thị duy nhất dưới dạng z $=$ a + bi,

trong đó a, b $\in \mathbf{R}$.

Một cách tổng quát $\mathbb{C}^n$ là một không gian vécto thực 2n chiều.

Dường thẳng số thực R là một không gian vécto vô hạn chiều trên trường số

(c)

hữu tỷ Q. Thật vậy, giả sử phản chứng $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở của R trên

Q. Mỗi phần tử $\beta \in \mathbf{R}$ có biểu thị tuyến tính duy nhất $\beta = a_1 \alpha_1$ + $\cdots$ + $a_n \alpha_n$

với $a_i \in \mathbf{Q}$. Tương ứng $\mathbf{R} \to \mathbf{Q}_n$, $\beta \mapsto (a_1$, ..., $a_n)$ là một song ánh. Do đó $\mathbf{R}$

có lực lượng đếm được. Điều vô lý này bác bỏ giả thiết phản chứng.

Mệnh đề 3.8 Giả sử V là một không gian vécto hữu hạn sinh. Khi đó, mọi hệ

sinh của V đều chứa một cơ sở. Mọi hệ độc lập tuyến tính trong V đều có thể bổ

sung để trở thành một cơ sở của V. Nếu dim V $=$ n, thì mọi hệ độc lập tuyến tính

$g\ddot{o}m$ n vécto của V đều là một cơ sở.

Chứng minh: Giả sử $\Gamma$ là một hệ sinh của V. Gọi $\Gamma'$ là một hệ độc lập tuyến tính

cực đại trong $\Gamma$. Khi đó $\Gamma$ biểu thị tuyến tính qua $\Gamma'$, và do đó V cũng biểu thị

tuyến tính $qua\Gamma'$. Như $thế\Gamma'$ là một hệ sinh độc lập tuyến tính, tức là một cơ sở

của V. (Theo Bổ đề 3.6, $\Gamma'$ có hữu hạn phần tử. Cụ thể hơn, số phần tử của $\Gamma'$

không vượt quá số phần tử của mọi hệ sinh hữu hạn của V.)

Giả sử $(\alpha_1$, ..., $\alpha_i)$ là một hệ độc lập tuyến tính trong V. Nếu hệ này không độc

lập tuyến tính cực đại thì có thể bổ sung các vécto $\alpha_{i+1}$, $\alpha_{i+2}$, ... để hệ thu được



vẫn độc lập tuyến tính. Quá trình này phải dừng lại sau một số hữu hạn bước, bởi

vì theo Định lý 2.5, dim V $< \infty$. Ta thu được hệ $(\alpha_1$, ..., $\alpha_n)$ độc lập tuyến tính cực

đại trong V, tức là một cơ sở của V.

Nếu dim V $=$ n, thì mọi hệ độc lập tuyến tính gồm n vécto $(\beta_1$, ..., $\beta_n)$ đều cực

đại. Thậy vậy, giả sử phản chứng có thể thêm vào hệ đó một vécto $\beta_{n+1}$ nào đó

của V sao cho hệ thu được vẫn độc lập tuyến tính. Khi đó, hệ $(\beta_1$, ..., $\beta_{n+1})$ biểu

thị tuyến tính qua một cơ sở $(\alpha_1$, ..., $\alpha_n)$ nào đó của V, cho nên theo Bổ đề 3.6, ta

có n + 1 $\leq$ n. Điều vô lý này bác bỏ giả thiết phản chứng. Vậy, theo Định lý 3.2,

$(\beta_1$, ..., $\beta_n)$ là một cơ sở của V.

$\Box$

Trong suốt giáo trình này, nếu không nói gì ngược lại, chúng ta chỉ nghiên cứu

các không gian vécto hữu hạn chiều.

Nhận xét: Người ta chứng minh được rằng, trong một không gian vécto vô hạn

sinh (tức là không hữu hạn sinh), hai cơ sở bất kỳ đều có cùng lực lượng. Nhưng

một hệ vécto độc lập tuyến tính có cùng lực lượng với cơ sở thì không nhất thiết

là môt co sở.

Chẳng hạn, hệ véctor (1, X, $X^2$, ...) là một cơ sở của K-không gian véctor K[X].

Hệ (X, $X^2$, $X^3$, $\ldots)$ độc lập tuyến tính và có cùng lực lượng với cơ sở (1, X, $X^2$, $\ldots)$,

nhưng không phải là một cơ sở của K[X], bởi vì đa thức 1 không biểu thị tuyến

tính được qua hệ đó.

Giả sử $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở của không gian vécto V. Mỗi vécto $\alpha \in$ V có

biểu thị tuyến tính duy nhất

$\alpha = a_1 \alpha_1$ + $\cdots$ + $a_n \alpha_n$, $\qquad a_i \in \mathbf{K}$.

### Định nghĩa 3.9 (Toạ độ). Bộ vô hướng (a_1, ..., a_n) xác định bởi điều kiện \alpha =

$\sum_i a_i \alpha_i$ được gọi là toạ độ của vécto $\alpha$ trong cơ sở $(\alpha_1$, ..., $\alpha_n)$. Vô hướng $a_i$ được

gọi là toa độ thứ i của $\alpha$ trong cơ sở đó.

Giả sử $\alpha$ và $\beta$ có toạ độ trong cơ sở $(\alpha_1$, ..., $\alpha_n)$ tương ứng là $(a_1$, ..., $a_n)$ và

$(b_1$, ..., $b_n)$. Khi đó, từ tính độc lập tuyến tính của $(\alpha_1$, ..., $\alpha_n)$ suy ra rằng $\alpha = \beta$



nếu và chỉ nếu $(a_1,...,a_n)=(b_1,...,b_n)$. Thật vậy, $\alpha=\betakhi$ và chỉ khi

$\alpha$ - $\beta = (a_1$ - $b_1)\alpha_1$ + $\cdots$ + $(a_n$ - $b_n)\alpha_n =$ 0.

Diều này xảy ra nếu và chỉ nếu $a_1 = b_1$, ..., $a_n = b_n$.

Hơn nữa, $\alpha$ + $\beta$ có toạ độ là $(a_1$ + $b_1$, ..., $a_n$ + $b_n)$ và kα có toạ độ là $(ka_1$, ..., $ka_n)$,

(k $\in \mathbf{K})$, trong hệ cơ sở $(\alpha_1$, ..., $\alpha_n)$.

Bây giờ ta xét xem toạ độ của một vécto trong những cơ sở khác nhau có liên

hệ với nhau như thế nào.

Giả sử $(\beta_1$, ..., $\beta_n)$ cũng là một cơ sở của không gian vécto V. Mỗi vécto $\beta_j$ biểu

thị tuyến tính được qua cơ sở $(\alpha_1$, ..., $\alpha_n)$, tức là có các vô hướng $c_{ij}$ để cho

$\beta_j = \sum_{i=1} c_{ij} \alpha_i$, (j $=$ 1, ..., n).

Giả sử $\alpha$ có toạ độ là $(a_1$, ..., $a_n)$ và $(b_1$, ..., $b_n)$ tương ứng trong các cơ sở $(\alpha_1$, ..., $\alpha_n)$

và $(\beta_1$, ..., $\beta_n)$. Ta có

$\alpha = \sum_{j=1}^n b_j \beta_j$

$= \sum_{i=1}^{n} \sum_{j=1}^{n} b_j c_{ij} \alpha_i$

$j=1 i=1$

$= \sum_{i=1}^{n} (\sum_{i=1}^{n} c_{ij} b_{j}) \alpha_i = \sum_{i=1}^{n} a_i \alpha_i$.

Do tính duy nhất của toạ độ của $\alpha$ trong cơ sở $(\alpha_1$, ..., $\alpha_n)$, ta nhận được

$a_i = \sum_{j=1}^n c_{ij} b_j$, $\qquad$ (i $=$ 1, ..., n).

Người ta gọi hệ thức nói trên là công thức đổi toạ độ khi đổi cơ sở. Ma trận

C $= (c_{ij})_{n \times n}$ được gọi là ma trận chuyển từ cơ sở $(\alpha_1$, ..., $\alpha_n)$ sang cơ sở $(\beta_1$, ..., $\beta_n)$.

Công thức đổi toạ độ sẽ được diễn đạt dưới một hình thức dễ tiếp nhận hơn

nhờ khái niệm tích của các ma trận, sẽ được nghiên cứu ở chương sau.



Không gian con - Hạng của một hệ véctơ

$\bf{4}$

Giả sử V là một không gian vécto trên trường $\mathbf{K}$. Chúng ta quan tâm đến những

tâp con của V có tính chất là chúng cũng lập nên những không gian vécto đối với

các phép toán là thu hẹp của những phép toán tương ứng trên V. Ta có định nghĩa

hình thức sau đây:

### Định nghĩa 4.1 Tập con không rỗng W \subset V được gọi là một không gian vécto

con của V nếu W khép kín đối với hai phép toán trên V, nghĩa là nếu

$\alpha$ + $\beta \in$ W, $\forall \alpha$, $\beta \in$ W,

$a\alpha \in$ W, $\forall$ a $\in \mathbf{K}$, $\forall \alpha \in$ W.

Nhận xét: Khi đó, W với hai phép toán là hạn chế của hai phép toán trên V cũng

là một không gian vécto trên K. Thật vậy, các tiên đề (V1), (V4), (V5), (V6),

(V7), (V8) nghiệm đúng với mọi phần tử của V, nên cũng nghiệm đúng với mọi

phần tử của W. Ta chỉ cần kiểm tra lại các tiên đề (V2), (V3) nói về sự tồn tại

của các phầnt ử 0 và phần tử đối.

Vì W $\neq \emptyset$, nên có ít nhất một phần tử $\alpha \in$ W. Khi đó 0 $= 0\alpha \in$ W. Phần

tử 0 $\in$ V đóng vai trò phần tử 0 $\in$ W. mặt khác, với mọi $\alpha \in$ W, ta có $(-\alpha) =$

$(-1)\alpha \in$ W. Đó cũng chính là phần tử đối của $\alpha$ trong W.

Ví dụ 4.2 (a) $\{0\}$ và V là hai không gian vécto con của V. Chúng được gọi là

các không gian véctor con tầm thường của V.

(b) Dường thẳng số thực $\bf{R}$ là một $\bf{R}-không$ gian vécto con của mặt phẳng phức

$\mathbf$ C.

Tập hợp các đa thức bậc $\leq$ n là một không gian véctor con của $\mathbf{K}[X]$.

(c)

Không gian $C^{1}[a$, b] các hàm khả vi liên tục trên [a, b] là một không gian vécto

(d)

con của không gian các hàm liên tục C[a, b].



(e) Giả sử m $\leq$ n. Khi đó tập hợp các vécto có dạng

$ \left( \begin{array}{c} x_1 \ \vdots \ x_m \ 0 \ \vdots \end{array} \right), $

trong đó $x_1$, ..., $x_m \in \mathbf{K}$, là một không gian véctor con có số chiều bằng m của

không gian $\mathbf{K}^n$.

Mệnh đề 4.3 Nếu W là một không gian véctor con của V thì dim W $\leq \dim$ V.

$D\ddot{a}ng$ thức dim W $= \dim$ V xảy ra khi và chỉ khi W $=$ V.

Chứng minh: Vì W là một không gian véctơ con của V, nên mỗi hệ độc lập tuyến

tính trong W thì cũng độc lập tuyến tính trong V. Do đó dim W $\leq \dim$ V. Đẳng

thức dim W $= \dim$ V xảy ra khi và chỉ khi mỗi cơ sở của W cũng là một cơ sở của

V. Diều này tương đương với W $=$ V.

$\Box$

Mệnh đề 4.4 Giao của một họ bất kỳ (có thể vô hạn) các không gian vécto con

của V lại là một không gian vécto con của V.

Chứng minh: Giả sử $\{V_i\}_{i\in I}$ là một họ các không gian con của V. Vì mỗi $V_i$ khép

kín đối với phép cộng vécto và phép nhân vécto với vô hướng, nên giao của chúng

$\bigcap_{i\in I}V_i$ cũng có tính chất đó.

$\Box$

Dinh nghĩa 4.5 Giả sử X là một tập con của không gian vécto V. Giao của tất

cả các không gian véctor con của V chứa X được gọi là không gian véctor con của

V sinh bởi X và được ký hiệu là $\mathcal{L}(X)$.

Từ định nghĩa suy ngay ra rằng $\mathcal{L}(X)$ là không gian véctor con nhỏ nhất của V

chứa X.



Hai trường hợp đặc biệt là $\mathcal{L}(\emptyset) = \{0\}$ và $\mathcal{L}(W) =$ W đối với mọi không gian

véctor con W của V.

Mệnh đề 4.6 Giả sử X $\neq \emptyset$. Khi đó $\mathcal{L}(X)$ là tập hợp các tổ hợp tuyến tính của

các phần tử của X. Nói riêng, nếu X $= \{\gamma_1$, ..., $\gamma_k\}$ thì

$\mathcal{L}(\gamma_1$, ..., $\gamma_k) = \{\sum_{i=1}^k a_i \gamma_i$ | $a_i \in \mathbf{K} \}$.

Chứng minh: Tập hợp các tổ hợp tuyến tính của các phần tử của X tất nhiên là

một không gian véctor con chứa X. Mặt khác, mỗi tổ hợp tuyến tính của các phần

tử của X đều nằm trong mọi không gian vécto con chứa X. Vậy tập hợp các tổ

hợp tuyến tính của các phần tử của X chính là không gian véctor con bé nhất của

V chứa X.

$\Box$

### Định nghĩa 4.7 Số chiều của không gian \mathcal{L}(X) được gọi là hạng của tập (hoặc hệ)

vécto X và được ký hiệu là rank(X).

Ta gọi một tập con của X là độc lập tuyến tính cực đại trong X nếu tập đó độc

lập tuyến tính và nếu thêm bất kỳ véctơ nào của X vào tập đó thì ta thu được

một tập phụ thuộc tuyến tính.

Mệnh đề sau đây chỉ ra cách tính hạng của một tập vécto trong thực hành.

Mệnh đề 4.8 Hạng của tập vécto X bằng số vécto của mỗi tập con độc lập tuyến

tính cực đại trong X.

Chứng minh: Nếu tập con A độc lập tuyến tính cực đại trong X thì mọi phần tử

của X biểu thị tuyến tính qua A, do đó mọi phần tử của $\mathcal{L}(X)$ cũng vậy. Nói cách

khác A cũng là độc lập tuyến tính cực đại trong $\mathcal{L}(X)$. Vậy số phần tử của A là

số chiều của không gian vécto $\mathcal{L}(X)$.

$\Box$

Hệ quả 4.9 Hai tập con độc lập tuyến tính cực đại trong X có cùng số phần tử.



Nhân xét: Trong Chương III, Nhân xét 8.2, chúng ta sẽ giới thiêu một phương

pháp đơn giản, dễ thực hành để tính hạng của một hệ véctơ trong $\mathbf{K}_n$ hoặc $\mathbf{K}^n$.

Phương pháp này dựa trên nhận xét là hạng của một hệ véctơ không thay đổi sau

các phép biến đổi sơ cấp. Người ta dùng các phép biến đổi sơ cấp để đưa hệ vécto

đã cho về dang "tam giác trên". Số các phần tử khác 0 trên đường chéo của "tam

giác” này chính là hang của hệ vécto.

Tổng và tổng trực tiếp

$5\overline{)}$

Giả sử $W_1$, ..., $W_m$ là các không gian véctor con của V. Tập hợp

$W_1$ + $\cdots$ + $W_m = \{ \alpha_1$ + $\cdots$ + $\alpha_m$ | $\alpha_i \in W_i$, i $=$ 1, ..., m $\}$

hiển nhiên lập nên một không gian véctor con của V.

### Định nghĩa 5.1 Không gian vécto W_1 + \cdots + W_m được gọi là tổng của các không

gian $W_1$, ..., $W_m$. Nó cũng được ký hiểu bởi $\sum_{i=1}^m W_i$.

Mỗi vécto của $W_1$ + $\cdots$ + $W_m$ có thể viết dưới dạng

$\alpha = \alpha_1$ + $\cdots$ + $\alpha_m$, $\quad \alpha_i \in W_i$.

Cách viết này nói chung không duy nhất. Chẳng hạn, nếu $W_1 \cap W_2 \neq \{0\}$, thì mỗi

$vécto\alpha \in W_1 \cap W_2 \setminus \{0\}có$ hai biểu $thị\alpha = \alpha$ + 0 $=$ 0 + $\alpha$, trong đó vécto thứ

nhất trong tổng thuộc $W_1$ còn vécto thứ hai trong tổng thuộc $W_2$.

### Định nghĩa 5.2 Nếu mọi vécto trong tổng W_1 + \cdots + W_m đều viết được duy nhất

dưới dạng $\alpha = \alpha_1$ + $\cdots$ + $\alpha_m$, với $\alpha_i \in W_i$ (i $=$ 1, ..., m) thì $W_1$ + $\cdots$ + $W_m$ được gọi

là tổng trực tiếp của các không gian $W_1$, ..., $W_m$, và được ký hiệu là $W_1 \oplus \cdots \oplus W_m$.

Dinh lý 5.3 $W_1$ + $\cdots$ + $W_m$ là tổng trực tiếp của $W_1$, $\ldots$, $W_m$ nếu và chỉ nếu một

trong hai điều kiện tương đương sau đây được thoả mãn:



(i) $W_i \cap (\sum_{j \neq i} W_j) = \{0\}$, $\quad$ (i $=$ 1, ..., m),

(ii) $W_i \cap (\sum_{j>i} W_j) = \{0\}$, $\quad$ (i $=$ 1, ..., m - 1).

Chứng minh: Giả sử $W_1$ + $\cdots$ + $W_m$ là một tổng trực tiếp. Khi đó điều kiện (i)

được thoả mãn. Thật vậy, giả sử phản chứng có chỉ số i sao cho

$W_i \cap (\sum_{j \neq i} W_j) \neq \{0\}$.

Gọi $\gamma \neq$ 0 là một vécto của giao đó. Vì $\gamma \in \sum_{j \neq i} W_j$, nên $\gamma$ có thể viết dưới dạng

$\gamma = \sum_{j \neq i} \gamma_j$, $\quad \gamma_j \in W_j$.

Ta đặt $\gamma_i = -\gamma$, và thu được hai cách biểu thi khác nhau của 0 dưới dạng tổng

của những phần tử của $W_i:$

0 $= \gamma_1$ + $\cdots$ + $\gamma_m$

$=$ 0 + $\cdots$ + 0.

Diều vô lý này bác bỏ giả thiết phản chứng.

Rõ ràng điều kiện (i) kéo theo điều kiện (ii).

Giả sử điều kiện (ii) được thoả mãn. Nếu $\alpha \in W_1$ + $\cdots$ + $W_m$ có hai biểu thị

$\alpha = \alpha_1$ + $\cdots$ + $\alpha_m = \beta_1$ + $\cdots$ + $\beta_m$,

với $\alpha_i$, $\beta_i \in W_i$, thì

$\alpha_1$ - $\beta_1 = \sum_{j>1} -(\alpha_j$ - $\beta_j) \in W_1 \cap (\sum_{j>1} W_j) = \{0\}$.

Do đó $\alpha_1 = \beta_1$ và $\alpha_2$ + $\cdots$ + $\alpha_m = \beta_2$ + $\cdots$ + $\beta_m$.

Lặp lại quá trình lập luận trên để có $\alpha_2 = \beta_2$, ..., $\alpha_m = \beta_m$. Vậy $W_1$ + $\cdots$ + $W_m$

là một tổng trực tiếp.

$\Box$

Dinh lý 5.4 Giá sử U và W là các không gian vécto con của một không gian vécto

hữu hạn chiều V. Khi đó

$\dim$ U + $\dim$ W $= \dim(U+W)$ + $\dim(U \cap$ W).



Chứng minh: Giả sử $(\alpha_1$, ..., $\alpha_r)$ là một cơ sở của U $\cap$ W. (Nếu U $\cap$ W $= \{0\}$, thì

ta coi r $=$ 0.) Ta bổ sung hệ này để có một cơ sở $(\alpha_1$, ..., $\alpha_r$, $\beta_1$, ..., $\beta_s)$ của U và một

cơ sở $(\alpha_1$, ..., $\alpha_r$, $\gamma_1$, ..., $\gamma_t)$ của W. Ta sẽ chứng tỏ rằng $(\alpha_1$, ..., $\alpha_r$, $\beta_1$, ..., $\beta_s$, $\gamma_1$, ..., $\gamma_t)$

là một cơ sở của U+W.

Rõ ràng $(\alpha_1$, ..., $\alpha_r$, $\beta_1$, ..., $\beta_s$, $\gamma_1$, ..., $\gamma_t)$ là một hệ sinh của U+W. Để chứng minh

đó là một hệ độc lập tuyến tính, ta giả sử có một ràng buộc tuyến tính

$a_1\alpha_1+\cdots+a_r\alpha_r+b_1\beta_1+\cdots+b_s\beta_s+c_1\gamma_1+\cdots+c_t\gamma_t=0$,

trong đó $a_i$, $b_j$, $c_k \in \mathbf{K}$. Véctor

$a_1\alpha_1$ + $\cdots$ + $a_r\alpha_r$ + $b_1\beta_1$ + $\cdots$ + $b_s\beta_s = -c_1\gamma_1$ - $\cdots$ - $c_t\gamma_t$

vừa thuộc U (do biểu thức ở vế trái), vừa thuộc W (do biểu thức ở vế phải), nên

nó thuộc U $\cap$ W, và do đó biểu thị tuyến tính qua $\alpha_1$, ..., $\alpha_r:$

$-c_1\gamma_1-\cdots-c_t\gamma_t=d_1\alpha_1+\cdots+d_r\alpha_r$.

Ta viết lại đẳng thức này như sau

$d_1\alpha_1+\cdots+d_r\alpha_r+c_1\gamma_1+\cdots+c_t\gamma_t=0$.

Vì hệ $(\alpha_1$, ..., $\alpha_r$, $\gamma_1$, ..., $\gamma_t)$ độc lập tuyến tính, nên $c_1 = \cdots = c_t = d_1 = \cdots = d_r =$ 0.

Do đó

$a_1\alpha_1+\cdots+a_r\alpha_r+b_1\beta_1+\cdots+b_s\beta_s=0$.

Hệ véctor $(\alpha_1$, ..., $\alpha_r$, $\beta_1$, ..., $\beta_s)$ cũng độc lập tuyến tính, cho nên $a_1 = \cdots = a_r =$

$b_1=\cdots=b_s=0.Kết$ hợp điều này với các hệ thức $c_1=\cdots=c_t=0ta$ suy ra

hệ $vécto(\alpha_1$, ..., $\alpha_r$, $\beta_1$, ..., $\beta_s$, $\gamma_1$, ..., $\gamma_t)độc$ lập tuyến tính, và do đó nó là một cơ sở

của U+W.

Dếm số vécto của các cơ sở đã xây dựng cho U, W, U $\cap$ W, U + W, ta có

$\dim(U+W) =$ r+s+t $=$ (r+s) + (r+t) - r

$=$ dim U + $\dim$ W - $\dim(U \cap$ W).

$\Box$



Hệ quả 5.5

$\dim(U \oplus$ W) $= \dim$ U + $\dim$ W.

$\Box$

Dinh nghĩa 5.6 Nếu V $=$ U $\oplus$ W thì W được gọi là một phần bù tuyến tính của

U trong V, và dim W $= \dim$ V - $\dim$ U được gọi là đối chiều của U trong V.

Giả sử V $=$ U $\oplus$ W. Khi đó mỗi vécto v $\in$ V có thể viết duy nhất dưới dạng

v $=$ u + w, trong đó u $\in$ U, w $\in$ W. Ta định nghĩa một ánh xạ

$pr_U:$ V $\rightarrow$ U,

$pr_U(v) =$ u.

Nó được gọi là phép chiếu của V lên U theo phương W.

Phép chiếu $pr_W$ của V lên W theo phương U được định nghĩa tương tự.

Phép chiếu có các tính chất sau:

$pr_U(v$ + v') $= pr_U(v)$ + $pr_U(v')$, $\qquad \forall$ v, v' $\in$ V,

$pr_U(av) = apr_U(v)$, $\quad \forall$ a $\in \mathbf{K}$, v $\in$ V.

6

Không gian thương

Giả sử W là một không gian vécto con của không gian V. Ta định nghĩa quan hệ

$\sim$ trên V như sau:

$\alpha \sim \beta \Longleftrightarrow \alpha$ - $\beta \in$ W.

Dễ dàng kiểm tra lại rằng $\sim$ là một quan hệ tương đương, tức là một quan hệ có

ba tính chất phản xạ, đối xứng và bắc cầu.

Tập thương của V theo quan hệ $\sim$ được ký hiệu là V/W. Lớp tương đương

của phần tử $\alpha \in$ V được ký hiệu là $[\alpha]$, hoặc $\alpha$ + W.

Ta trang bị cho V/W hai phép toán sau đây:

$[\alpha]$ + $[\beta] = [\alpha$ + $\beta]$, $\quad \forall \alpha$, $\beta \in$ V,

$a[\alpha] = [a\alpha]$, $\quad \forall$ a $\in \mathbf{K}$, $\alpha \in$ V.



Mênh đề 6.1 Hai phép toán nói trên được định nghĩa không phụ thuộc vào việc

chọn đại biểu. Hơn nữa, V/W được trang bị hai phép toán đó là một $\mathbf{K}\text{-}kh\hat{o}ng$

gian vécto.

Dinh nghĩa 6.2 Không gian vécto V/W được gọi là không gian thương của V theo

không gian con W.

Chứng minh Mệnh đề 6.1. Giả sử $[\alpha] = [\alpha']$, $[\beta] = [\beta']$, nghĩa là $\alpha$ - $\alpha' \in$

W, $\beta$ - $\beta' \in$ W. Khi đó, vì W là một không gian vécto con, cho nên

$(\alpha$ + $\beta)$ - $(\alpha'$ + $\beta') = (\alpha$ - $\alpha')$ + $(\beta$ - $\beta') \in$ W.

Diều này chứng tỏ rằng $[\alpha$ + $\beta] = [\alpha'$ + $\beta']$.

Tương tự, nếu $[\alpha] = [\alpha']$, tức là $\alpha$ - $\alpha' \in$ W, thì

$a\alpha$ - $a\alpha' = a(\alpha$ - $\alpha') \in$ W.

Diều này có nghĩa là $[a\alpha] = [a\alpha']$.

Phần tử trung lập của phép cộng trong V/W chính là [0] $=$ 0 + W. Phần tử đối

của $[\alpha]$ chính là $[-\alpha]$. Dễ dàng kiểm tra rằng các tiên đề khác về không gian vécto

được thoã mãn cho không gian V/W.

$\Box$

Hai trường hợp đặc biệt của không gian thương là

V/V $= \{0\},V/\{0\} =$ V.

Dinh lý 6.3

$\dim$ V/W $= \dim$ V - $\dim$ W.

Chứng minh: Giả $sử(\alpha_1,...,\alpha_r)là$ một cơ sở của W. (Nếu W $= \{0\}$ thì ta coi

r $=$ 0.) Ta bổ sung hệ véctơ nói trên để có một cơ sở $(\alpha_1$, ..., $\alpha_r$, $\beta_1$, ..., $\beta_s)$ của V.

Ta sẽ chứng minh rằng $([\beta_1]$, ..., $[\beta_s])$ là một cơ sở của V/W.



Giả sử có một ràng buộc tuyến tính

$b_1[\beta_1]$ + $\cdots$ + $b_s[\beta_s] =$ [0].

Diều này có nghĩa là $b_1\beta_1$ + $\cdots$ + $b_s\beta_s \in$ W. Vì thế vécto đó biểu thị tuyến tính

qua co só đã chọn của W:

$b_1\beta_1+\cdots+b_s\beta_s=a_1\alpha_1+\cdots+a_r\alpha_r$.

Vì hệ $(\alpha_1$, ..., $\alpha_r$, $\beta_1$, ..., $\beta_s)$ độc lập tuyến tính, nên $a_1 = \cdots = a_r = b_1 = \cdots = b_s =$ 0.

Như thế, hệ $([\beta_1]$, ..., $[\beta_s])$ độc lập tuyến tính.

Mặt khác, rõ $ràng([\beta_1],...,[\beta_s])là$ một hệ sinh của không gianV/W. Thật vậy,

mỗi véctor $\alpha \in$ V biểu thị tuyến tính qua $(\alpha_1$, ..., $\alpha_r$, $\beta_1$, ..., $\beta_s):$

$\alpha = c_1 \alpha_1$ + $\cdots$ + $c_r \alpha_r$ + $d_1 \beta_1$ + $\cdots$ + $d_s \beta_s (c_i$, $d_j \in \mathbf{K})$.

Vi $c_1\alpha_1$ + $\cdots$ + $c_r\alpha_r \in$ W, cho nên

$[\alpha] = [d_1\beta_1$ + $\cdots$ + $d_s\beta_s] = d_1[\beta_1]$ + $\cdots$ + $d_s[\beta_s]$.

Như vậy, mỗi vécto $[\alpha] \in$ V/W đều biểu thị tuyến tính được qua $([\beta_1]$, ..., $[\beta_s])$.

$\widetilde{D}ếm$ số véctor của các cơ sở đã xây dựng cho W, V, V/W ta có

$\dim$ V/W $=$ s $=$ (r + s) - r $= \dim$ V - $\dim$ W.

$\Box$

Ta định nghĩa ánh xạ

$\pi:$ V $\rightarrow$ V/W

$\pi(\alpha) = [\alpha] = \alpha$ + W.

và gọi nó là phép chiếu từ V lên V/W. Phép chiếu có những tính chất sau đây:

$\pi(\alpha$ + $\beta) = \pi(\alpha)$ + $\pi(\beta)$, $\quad \forall \alpha$, $\beta \in$ V,

$\pi(a\alpha) = a\pi(\alpha)$, $\quad \forall$ a $\in \mathbf{K}$, $\beta \in$ V.



Trong chương sau chúng ta sẽ nghiên cứu một cách có hệ thống những ánh xa

có hai tính chất như thế. Chúng được gọi là các ánh xạ tuyến tính.

Bài tâp

1. Xét xem các tập hợp sau đây có lập thành K-không gian véctơ hay không đối

với các phép toán thông thường (được định nghĩa theo từng thành phần):

(a) Tập hợp tất cả các dãy $(x_1$, ..., $x_n) \in \mathbf{K}_n$ thoả mãn điều kiện $x_1$ + $\cdots$ +

$x_n=0$.

(b) Tập hợp tất cả các dãy $(x_1$, ..., $x_n) \in \mathbf{K}_n$ thoả mãn điều kiện $x_1$ + $\cdots$ +

$x_n=1$.

(c) Tập hợp tất cả các dãy $(x_1$, ..., $x_n) \in \mathbf{K}_n$ thoả mãn điều kiện $x_1 = x_n =$

-1.

(d) Tập hợp tất cả các dãy $(x_1$, ..., $x_n) \in \mathbf{K}_n$ thoả mãn điều kiện $x_1 = x_3 =$

$x_5 = \cdots$, $x_2 = x_4 = x_6 = \cdots$

(e) Tập hợp các ma trận vuông $(a_{ij})_{n\times n}$ đối xứng cấp n, nghĩa là các ma

trận thoả mãn $a_{ij} = a_{ji}$, với 1 $\leq$ i, j $\leq$ n.

2. Tập hợp tất cả các dãy $(x_1$, ..., $x_n) \in \mathbf{R}_n$ với tất cả các thành phần $x_1$, ..., $x_n$

đều nguyên có lập thành một R-không gian vecto hay không?

3. Với các phép toán thông thường, Q có là một R-không gian vécto hay không?

R có là một C-không gian vécto hay không?

4. Chứng minh rằng nhóm Z không đẳng cấu với nhóm cộng của bất kỳ một

không gian vécto trên bất kỳ trường nào.



5. Chứng minh rằng nhóm abel A đối với phép cộng + có thể trở thành một

không gian vécto trên trường $\mathbf{F}_p$ nếu và chỉ nếu

px $=$ x + x + $\cdots$ + x $=$ 0, $\quad \forall$ x $\in$ A.

6. Xét xem các véctor sau đây độc lập hay phụ thuộc tuyến tính trong $\mathbf{R}_4:$

(a) $e_1 =$ (-1, -2, 1, 2), $e_2 =$ (0, -1, 2, 3), $e_3 =$ (1, 4, 1, 2), $e_4 =$ (-1, 0, 1, 3).

(b) $\alpha_1 =$ (-1, 1, 0, 1), $\alpha_2 =$ (1, 0, 1, 1), $\alpha_3 =$ (-3, 1, -2, -1).

7. Chứng minh rằng hai hệ vécto sau đây là các cơ sở của $C<sub>3</sub>$. Tìm ma trận

chuyển từ cơ sở thứ nhất sang cơ sở thứ hai:

$e_1 =$ (1, 2, 1), $e_2 =$ (2, 3, 3), $e_3 =$ (3, 7, 1);

$e'_1 =$ (3, 1, 4), $e'_2 =$ (5, 2, 1), $e'_3 =$ (1, 1, -6).

8. Chứng minh rằng hai hệ véctơ sau đây là các cơ sở của $C_4$. Tìm mối liên hệ

giữa toạ độ của cùng một vécto trong hai cơ sở đó:

$e_1 =$ (1, 1, 1, 1), $e_2 =$ (1, 2, 1, 1), $e_3 =$ (1, 1, 2, 1), $e_4 =$ (1, 3, 2, 3);

$e'_1 =$ (1, 0, 3, 3), $e'_2 =$ (2, 3, 5, 4), $e'_3 =$ (2, 2, 5, 4), $e'_4 =$ (2, 3, 4, 4).

9. Xét xem các tập hợp hàm số thực sau đây có lập thành không gian véctơ đối

với các phép toán thông thường hay không? Nếu có, hãy tìm số chiều của các

không gian đó.

(a) Tập $\mathbf{R}[X]$ các đa thức của một ẩn X.

(b) Tập $C^{\infty}(\mathbf{R})$ các hàm thực khả vi vô hạn trên R.

(c) Tập $C^0(\mathbf{R})$ các hàm thực liên tục trên R.

(d) Tập các hàm thực bị chặn trên R.

(e) Tập các hàm f: $\mathbf{R} \to \mathbf{R}$ sao cho $sup<sub>x \in \mathbf{R}</sub>$ |f(x)| $\leq$ 1.

(f) Tập các hàm f: $\mathbf{R} \to \mathbf{R}$ thoả mãn điều kiện f(0) $=$ 0.



(g) Tập các hàm f: $\mathbf{R} \to \mathbf{R}$ thoả mãn điều kiện f(0) $=$ -1.

(h) Tập các hàm thực đơn điệu trên $\mathbf$ R.

10. Định nghĩa hai phép toán cộng và nhân với vô hướng trên tập hợp

V $= \{(x$, y) $\in \mathbf{R} \times \mathbf{R} \mid$ y $> 0\}$

như sau:

(x, y) + (u, v) $=$ (x + u, yv), $\forall$ (x, y), (u, v) $\in$ V,

a(x, y) $=$ (ax, $y^a)$, $\forall$ a $\in \mathbf{R}$, (x, y) $\in$ V.

Xét xem V có là một không gian vécto thực đối với hai phép toán đó không.

Nếu có, hãy tìm một cơ sở của không gian ấy.

11. Ma trận chuyển từ một cơ sở sang một cơ sở khác thay đổi thế nào nếu:

(a) đổi chỗ hai vécto trong cơ sở thứ nhất?

(b) đổi chỗ hai vécto trong cơ sở thứ hai?

(c) đặt các vécto trong mỗi cơ sở theo thứ tự hoàn toàn ngược lại?

12. Cho a là một số thực. Chứng minh rằng hai hệ vécto (1, X, $X^2$, ..., $X^n)$ và

(1, (X - a), (X - $a)^2$, ..., (X - $a)^n)là$ các cơ sở của không gian $\mathbf{R}[X]_ncác$ đa

thức hệ số thực với bậc không vượt quá n. Tìm ma trận chuyển từ cơ sở thứ

nhất sang cơ sở thứ hai.

13. Tìm các toạ độ của đa thức f(X) $= a_0$ + $a_1X$ + $\cdots$ + $a_nX^n$ trong hai cơ sở

nói trên.

14. Cho không gian véctor con L của không gian $\mathbf{R}[X]$. Chứng minh rằng nếu L

chứa ít nhất một đa thức bậc k với mọi k $=$ 0, 1, ..., n nhưng không chứa đa

thức nào với bậc lớn hơn n thì L chính là không gian con $\mathbf{R}[X]_n$ tất cả các

đa thức với bậc không vược quá n.



15. Chứng minh rằng tập hợp các vécto $(x_1,...,x_n) \in \mathbf{R}_n$ thoả mãn hệ thức

$x_1$ + $2x_2$ + $\cdots$ + $nx_n =$ 0 là một không gian véctor con của $\mathbf{R}_n$. Tìm số chiều

và một cơ sở cho không gian véctơ con đó.

16. Tìm tất cả các $\mathbf{F}_2-không$ gian véctor con một và hai chiều của $\mathbf{F}_2^3$. Giải bài

toán tương tự đối với không gian $\mathbf{F}_p^3$, trong đó p là một số nguyên tố.

17. Chứng minh rằng các ma trận vuông đối xứng cấp n với các phần tử trong

trường K lập thành một không gian véctor con của M(n $\times$ n, $\mathbf{K})$. Tìm số chiều

và một cơ sở cho K-không gian véctor con đó.

18. Chứng minh rằng các ma trận vuông $(a_{ij})_{n \times n}$ phản đối xứng cấp n, nghĩa là

các ma trận thoả mãn $a_{ij} = -a_{ji}$, với 1 $\leq$ i, j $\leq$ n, lập thành một không gian

vécto con của M(n $\times$ n, $\mathbf{K})$. Tìm số chiều và một cơ sở cho K-không gian

vécto con dó.

19. Giả sử $V_1 \subset V_2$ là các không gian véctor con của V. Chứng minh rằng dim $V_1 \leq$

dim $V_2$, đẳng thức xảy ra khi và chỉ khi $V_1 = V_2$. Khẳng định đó còn đúng

hay không nếu $V_1$ và $V_2$ là các không gian véctor con bất kỳ của V?

20. Giả sử $V_1$, $V_2$ là các không gian véctor con của V. Chứng minh rằng nếu

$\dim V_1$ + $\dim V_2 > \dim$ V thì $V_1 \cap V_2$ chứa ít nhất một vécto khác không.

21. Với giả thiết như bài tập trước, chứng minh rằng nếu $dim(V_1$ + $V_2) = \dim(V_1 \cap$

$V_2)$ + 1 thì $V_1$ + $V_2$ trùng với một trong hai không gian con đã cho, còn $V_1 \cap V_2$

trùng với không gian con còn lại.

Tìm hang của các hệ véctơ sau đây:

22. $\alpha_1 =$ (1, 2, 0, 1), $\alpha_2 =$ (1, 1, 1, 0), $\alpha_3 =$ (1, 0, 1, 0), $\alpha_4 =$ (1, 3, 0, 1).

23. $\alpha_1 =$ (1, 1, 1, 1), $\alpha_2 =$ (1, 3, 1, 3), $\alpha_3 =$ (1, 2, 0, 2), $\alpha_4 =$ (1, 2, 1, 2), $\alpha_5 =$

(3, 1, 3, 1).



Tìm cơ sở của tổng và giao của các không gian véctơ con sinh bởi các hê

véctor $\alpha_1$, ..., $\alpha_k$ và $\beta_1$, ..., $\beta_\ell$ sau đây:

24. $\alpha_1 =$ (1, 2, 1), $\alpha_2 =$ (1, 1, -1), $\alpha_3 =$ (1, 3, 3),

$\beta_1 =$ (2, 3, -1), $\ \beta_2 =$ (1, 2, 2), $\ \beta_3 =$ (1, 1, -3).

25. $\alpha_1 =$ (1, 2, 1, -2), $\alpha_2 =$ (2, 3, 1, 0), $\alpha_3 =$ (1, 2, 2, -3),

$\beta_1 =$ (1, 1, 1, 1), $\beta_2 =$ (1, 0, 1, -1), $\beta_3 =$ (1, 3, 0, -4).

26. $\alpha_1 =$ (1, 1, 0, 0), $\alpha_2 =$ (0, 1, 1, 0), $\alpha_3 =$ (0, 0, 1, 1),

$\beta_1 =$ (1, 0, 1, 0), $\beta_2 =$ (0, 2, 1, 1), $\beta_3 =$ (1, 2, 1, 2).

27. Chứng minh rằng với mọi không gian véctơ con $V_1$ của V tồn tại một không

gian véctor con $V_2$ của V sao cho V $= V_1 \oplus V_2$. Không gian $V_2$ có xác định duy

nhất hay không?

28. Chứng minh rằng không gian $C_n$ là tổng trực tiếp của không gian véctor con

U xác định bởi phương trình $x_1$ + $x_2$ + $\cdots$ + $x_n =$ 0 và không gian véctor con V

xác định bởi phương trình $x_1 = x_2 = \cdots = x_n$. Tìm hình chiếu của các vécto

trong cơ sở chính tắc của $\mathbf{C}_n$ lên U theo phương V và lên V theo phương U.

29. Cho K là một trường có đặc số khác 2. Chứng minh rằng không gian M(n $\times$

n, K) các ma trận vuông cấp n là tổng trực tiếp của không gian S(n) gồm các

ma trận đối xứng và không gian A(n) gồm các ma trận phản đối xứng. Tìm

hình chiếu của ma trận C $\in$ M(n $\times$ n, $\mathbf{K})$ lên S(n) theo phương A(n) và lên

A(n) theo phorong S(n).

30. Gọi $\mathbf{K}[X]_n$ là K-không gian vécto các đa thức với hệ số trong $\mathbf{K}$ có bậc $\leq$ n.

Tìm không gian thương $\mathbf{K}[X]_n/\mathbf{K}[X]_m$ và số chiều của nó khi m $<$ n.



# Chương II

MA TRẬN VÀ ÁNH XA TUYẾN TÍNH

Cấu trúc của các không gian vécto chỉ lộ rõ khi chúng ta nghiên cứu chúng

không phải như những đối tượng riêng rẽ, mà trái lại đặt chúng trong mối liên hệ

với nhau. Công cụ dùng để xác lập mối liên hệ giữa các không gian véctơ là các

ánh xạ tuyến tính. Ngôn ngữ giúp cho việc mô tả cụ thể các ánh xạ tuyến tính là

các ma trân.

Ma trân

Giả sử $\bf{K}$ là một trường tuỳ ý.

### Định nghĩa 1.1 Mỗi bảng có dạng

$ A = \left( \begin{array}{cccc} a_{11} & a_{12} & \ldots & a_{1n} \ a_{21} & a_{22} & \ldots & a_{2n} \ . & . & . & . \ . & . & . & . \ a_{m1} & a_{m2} & \ldots & a_{mn} \ \end{array} \right), $

trong đó $a_{ij} \in \mathbf{K}$ (1 $\le$ i $\le$ m, 1 $\le$ j $\le$ n), được gọi là một ma trận m hàng (hay

dòng) n cột với các phần tử trong K. Nếu m $=$ n, thì ta nói A là một ma trận

vuông cấp n. Véctor hàng

$(a_{i1}$, $a_{i2}$, ..., $a_{in})$

được gọi là hàng thứ i của ma trận A. Vécto cột

$(a_{1j}$, $a_{2j}$, ..., $a_{mj})^t$

được gọi là cột thứ j của ma trận A.



Ma trận nói trên thường được ký hiệu gọn là A $= (a_{ij})_{m \times n}$.

Tập hợp tất cả các ma trận m hàng, n cột với các phần tử trong $\bf{K}$ được ký

hiệu là M(m $\times$ n, $\mathbf{K})$, hay Mat(m $\times$ n, $\mathbf{K})$.

Ta định nghĩa hai phép toán cộng và nhân với vô hướng trên M(m $\times$ n, $\mathbf{K})$ như

sau:

$ \left( \begin{array}{cccc} a_{11} & \ldots & a_{1n} \\ a_{21} & \ldots & a_{2n} \\ . & \ldots & . \\ a_{m1} & \ldots & a_{mn} \end{array} \right) + \left( \begin{array}{cccc} b_{11} & \ldots & b_{1n} \\ b_{21} & \ldots & b_{2n} \\ . & \ldots & . \\ b_{m1} & \ldots & b_{mn} \end{array} \right) = \left( \begin{array}{cccc} a_{11} + b_{11} & \ldots & a_{1n} + b_{1n} \\ a_{21} + b_{21} & \ldots & a_{2n} + b_{2n} \\ . & \ldots & . \\ $

$ a \left( \begin{array}{cccc} a_{11} & a_{12} & \ldots & a_{1n} \\ a_{21} & a_{22} & \ldots & a_{2n} \\ . & . & \ldots & . \\ a_{m1} & a_{m2} & \ldots & a_{mn} \end{array} \right) = \left( \begin{array}{cccc} a a_{11} & a a_{12} & \ldots & a a_{1n} \\ a a_{21} & a a_{22} & \ldots & a a_{2n} \\ . & . & \ldots & . \\ a a_{m1} & a a_{m2} & \ldots & a a_{mn} \end{array} \right), \quad (a \in \mathbf{K}). $

Mệnh đề 1.2 M(m $\times$ n, $\mathbf{K})$ được trang bị hai phép toán nói trên là một không

gian vécto trên trường $\bf{K}$ với số chiều bằng

$\dim$ M(m $\times$ n, $\mathbf{K}) =$ m $\times$ n.

Chứng minh: Dễ dàng kiểm tra khẳng định M(m $\times$ n, $\mathbf{K})$ là một K-không gian

vécto. Lưu ý rằng phần tử trung lập của phép cộng trong M(m $\times$ n, $\mathbf{K})$ là

$ 0 = \left( \begin{array}{cccc} 0 & 0 & ... & 0 \ . & . & ... & . \ 0 & 0 & ... & 0 \end{array} \right), $

và phần tử đối của A $= (a_{ij})_{m \times n}$ là -A $= (-a_{ij})_{m \times n}$.

Để chứng minh khẳng định về số chiều của M(m $\times$ n, $\mathbf{K})$ ta xét ma trận $E_{ij}$

(1 $\leq$ i $\leq$ m, 1 $\leq$ j $\leq$ n) gồm toàn phần tử 0, loại trừ phần tử duy nhất bằng 1 nằm

trên giao của hàng i và cột j. Giả sử A $= (a_{ij})_{m \times n} \in$ M(m $\times$ n, $\mathbf{K})$. Ta có

A $= \sum_{i=1}^{n} \sum_{j=1}^{n} a_{ij} E_{ij}$.



Như vậy hệ $(E_{ij}|1 \leq$ i $\leq$ m, 1 $\leq$ j $\leq$ n) là một hệ sinh của M(m $\times$ n, $\mathbf{K})$. Mặt khác,

mỗi ràng buộc tuyến tính

$\sum \sum b_{ij} E_{ij} =$ 0

$i=1 i=1$

kéo theo B $= (b_{ij})_{m \times n} =$ 0. Tức là $b_{ij} =$ 0 với mọi i, j. Điều này chứng tỏ

$(E_{ij}|1 \leq$ i $\leq$ m, 1 $\leq$ j $\leq$ n) độc lập tuyến tính.

$\Box$

Cho hai ma trận A $= (a_{ij}) \in$ M(m $\times$ n, $\mathbf{K})$, B $= (b_{ik}) \in$ M(n $\times$ p, $\mathbf{K})$.

### Định nghĩa 1.3 Tích AB của ma trận A và ma trận B là ma trận C = (c_{ik}) \in

M(m $\times$ p, $\mathbf{K})$ với các phần tử được xác định như sau

$c_{ik} = \sum_{i=1}^{n} a_{ij} b_{jk}$, $\quad$ (1 $\leq$ i $\leq$ m, 1 $\leq$ k $\leq$ p).

$j=1$

### Định nghĩa này được minh họa bằng hình vẽ sau đây:

$\!\!\!=\!\!\!$

Ví dụ:

$ \left(\begin{array}{ccc} a & b & c \\ d & e & f \\ g & h & i \end{array}\right) \left(\begin{array}{ccc} x & t \\ y & u \\ z & v \end{array}\right) = \left(\begin{array}{ccc} ax+by+cz & at+bu+cv \\ dx+ey+ fz & dt+eu+fv \\ gx+hy+iz & gt+hu+iv \end{array}\right). $

Nhận xét: Điều kiện để định nghĩa được ma trận tích AB là

số cột của A $=$ số hàng của B.



Có thể xảy ra trường hợp tích AB thì định nghĩa được, mà tích BA thì không.

Trường hợp đặc biệt, khi A và B đều là các ma trận vuông cấp n thì cả hai

tích AB và BA đều định nghĩa được. Nhưng nói chung AB $\neq$ BA. Chẳng hạn,

với $n=2$, ta có

$ \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \neq \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}. $

Các đẳng thức sau đây được hiểu theo nghĩa: nếu một về được xác định thì

vế kia cũng vậy và hai vế bằng nhau.

(AB)C $=$ A(BC),

$A(B_1$ + $B_2) = AB_1$ + $AB_2$

$(A_1$ + $A_2)B = A_1B$ + $A_2B$.

Chúng ta chứng minh đẳng thức thứ nhất. Hai đẳng thức còn lại được xem

như những bài tập.

Giả sử A $= (a_{ij})_{m \times n}$, B $= (b_{jk})_{n \times p}$, C $= (c_{k\ell})_{p \times q}$. Khi đó phần tử nằm ở hàng i

cột $\ell$ của ma trận (AB)C là

$\sum_{k=1}^{p} (\sum_{j=1}^{n} a_{ij} b_{jk}) c_{k\ell}$.

Còn phần tử nằm ở hàng icột $\ellcủa$ ma trận A(BC) là

$\sum_{j=1}^n a_{ij}(\sum_{k=1}^p b_{jk}c_{k\ell})$.

Hiển nhiên cả hai phần tử nói trên đều bằng

$\sum_{j=1}^{n} \sum_{k=1}^{p} a_{ij} b_{jk} c_{k\ell}$.

Vì điều đó đúng với mọi i, $\ell$, nên (AB)C $=$ A(BC).

Những nhận xét nói trên dẫn ta tới khẳng định sau đây cho các ma trận vuông.

Mệnh đề 1.4 Tập hợp các ma trận vuông M(n $\times$ n, $\mathbf{K})$ cùng với các phép toán

cộng và nhân ma trận lập thành một vành có đơn vị. Vành này không giao hoán

n $\epsilon$ u $\approx$ 1.

$\Box$



Lưu ý rằng phần tử đơn vi của vành M(n $\times$ n, $\mathbf{K})$ là ma trân sau đây

$ E = E_n = \left( \begin{array}{cccc} 1 & 0 & \ldots & 0 \ 0 & 1 & \ldots & 0 \ . & . & \ldots & . \ 0 & 0 & \ldots & 1 \end{array} \right). $

Nó được gọi là ma trận đơn vị cấp n.

Dinh nghĩa 1.5 Ma trận A $\in$ M(n $\times$ n, $\mathbf{K})$ được gọi là một ma trận khả nghịch

(hoặc ma trận không suy biến) nếu có ma trận B $\in$ M(n $\times$ n, $\mathbf{K})$ sao cho AB $=$

BA $= E_n$. Khi đó, ta nói B là nghịch đảo của A và ký hiệu B $= A^{-1}$.

Nhận xét rằng nếu A khả nghịch thì ma trận nghịch đảo của nó được xác định

duy nhất. Thật vậy, giả sử B và B' đều là các nghịch đảo của A. Khi đó

B $= BE_n =$ B(AB') $=$ (BA)B' $= E_nB' =$ B'.

Trong chương sau chúng ta sẽ chỉ ra một điều kiện cần và đủ rất đơn giản để

cho một ma trận vuông là khả nghịch.

Sau đây là ví dụ về một lớp các ma trận khả nghịch.

Mệnh đề 1.6 Gọi C là ma trận chuyển từ cơ sở $(\alpha_1$, ..., $\alpha_n)$ sang cơ sở $(\alpha'_1$, ..., $\alpha'_n)$

của không gian véctơ V. Khi đó, C là một ma trận khả nghịch, với nghịch đảo là

ma trận chuyển C' từ cơ sở $(\alpha'_1$, ..., $\alpha'_n)$ sang cơ sở $(\alpha_1$, ..., $\alpha_n)$.

Chứng minh: Giả sử C $= (c_{ij})$, C' $= (c'_{ij})$. Ta có

$\alpha'_{j} = \sum_{i=1}^{n} c_{ij} \alpha_{i} = \sum_{i=1}^{n} c_{ij} \sum_{k=1}^{n} c'_{ki} \alpha'_{k} = \sum_{k=1}^{n} (\sum_{i=1}^{n} c'_{ki} c_{ij}) \alpha'_{k}$.

Vì biểu thị tuyến tính của mỗi vétơ qua cơ sở là duy nhất, nên ta nhận được

$ \sum_{i=1}^{n} c'_{ki} c_{ij} = \delta_{kj} = \begin{cases} 1 & \text{néu } k = j, \\ 0 & \text{néu } k \neq j. \end{cases} $



Nghĩa là C'C $= E_n$. Tương tự, tráo đổi vai trò của hai cơ sở cho nhau, ta có

CC' $= E_n$. Như vậy, C khả nghịch và $C^{-1} =$ C'.

$\Box$

Nhận xét: Giả sử $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở của không gian vécto V, và C $= (c_{ij})$

là một ma trận vuông cấp n và khả nghịch. Khi đó hệ vécto $(\alpha'_1$, ..., $\alpha'_n)$ xác định

bởi $\alpha'_i = \sum_{i=1}^n c_{ij} \alpha_i$ cũng là một cơ sở của V. Thật vậy, nếu C' $= (c'_{ij})$ là ma trận

nghịch đảo của C thì $\alpha_j = \sum_{i=1}^n c'_{ij} \alpha'_i$. Do đó $(\alpha'_1$, ..., $\alpha'_n)$ là một hệ sinh của V. Hệ

này có số phần tử đúng bằng số chiều của V, nên nó là một cơ sở của V. Tất

nhiên, C chính là ma trận chuyển từ cơ sở $(\alpha_1$, ..., $\alpha_n)$ sang cơ sở $(\alpha'_1$, ..., $\alpha'_n)$.

Trong ngôn ngữ tích ma trận, sự kiện C là ma trận chuyển từ cơ sở $(\alpha_1$, ..., $\alpha_n)$

sang cơ sở $(\alpha'_1$, ..., $\alpha'_n)$, tức là hệ đẳng thức $\alpha'_j = \sum_{i=1}^n c_{ij} \alpha_i$ (j $=$ 1, ..., n), được viết

gọn như sau

$(\alpha'_1 \dots \alpha'_n) = (\alpha_1 \dots \alpha_n)C$.

Hơn nữa, nếu $\alpha = \sum_{i=1}^n x_i \alpha_i = \sum_{i=1}^n x'_i \alpha'_i$, thì ta có

$ \alpha = (\alpha'_1 \dots \alpha'_n) \left( \begin{array}{c} x'_1 \\ \vdots \\ x'_n \end{array} \right) = (\alpha_1 \dots \alpha_n) C \left( \begin{array}{c} x'_1 \\ \vdots \\ x'_n \end{array} \right) = (\alpha_1 \dots \alpha_n) \left( \begin{array}{c} x_1 \\ \vdots \\ x_n \end{array} \right). $

Do biểu thị tuyến tính của mỗi vécto qua cơ sở là duy nhất, nên

$ \left(\begin{array}{c} x_1 \ \vdots \ x_n \end{array}\right) = C \left(\begin{array}{c} x'_1 \ \vdots \ x'_n \end{array}\right). $

### Định nghĩa 1.7 Ta ký hiệu bởi GL(n, K) tập hợp tất cả các ma trận khả nghịch

trong M(n $\times$ n, $\mathbf{K})$.

Mệnh đề 1.8 GL(n, K) lập thành một nhóm đối với phép nhân các ma trận.

Chứng minh: Trước hết ta chứng minh rằng GL(n, $\mathbf{K})$ khép kín đối với phép

nhân ma trận. Giả sử A, B $\in$ GL(n, $\mathbf{K})$. Khi đó, tồn tại các ma trận $A^{-1}$, $B^{-1} \in$



M(n $\times$ n, $\mathbf{K})$. Ta có

(A $B)(B^{-1}A^{-1}) =$ A(B $B^{-1})A^{-1} =$ A $E_n A^{-1} =$ A $A^{-1} = E_n$,

$(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1}E_nB = B^{-1}B = E_n$.

Như vậy, AB cũng khả nghịch, hơn nữa $(AB)^{-1} = B^{-1}A^{-1}$.

Ta đã biết rằng phép nhân các ma trận vuông (nói riêng phép nhân các ma trận

trong GL(n, $\mathbf{K})$ có tính kết hợp.

Phần tử trung lập (đơn vị) đối với phép nhân trong GL(n, $\mathbf{K})$ chính là ma trận

don vị $E_n \in$ GL(n, $\mathbf{K})$.

Theo định nghĩa của GL(n, K), mỗi ma trận trong nó đều có nghịch đảo. Hiển

nhiên, nghịch đảo $A^{-1}$ của mỗi ma trận A $\in$ GL(n, $\mathbf{K})$ cũng là một phần tử của

GL(n, $\mathbf{K})$.

$\Box$

### Định nghĩa 1.9 Hai ma trận vuông A, A' \in M(n \times n, \mathbf{K}) được gọi là đồng dạng

nếu có một ma trận khả nghịch C $\in$ GL(n, $\mathbf{K})$ sao cho A' $= C^{-1}AC$.

Dễ thấy rằng đồng dạng là một quan hệ tương đương.

Trong tiết sau chúng ta sẽ chứng minh rằng mỗi lớp tương đương của các ma

trận theo quan hệ đồng dạng được đặt tương ứng một đối một với một tự đồng

cấu tuyến tính của một không gian vécto hữu hạn chiều nào đó.

Ánh xạ tuyến tính

$\boldsymbol{2}$

Giả sử V và W là các không gian vécto trên trường K.

Dinh nghĩa 2.1 (Ánh xạ tuyến tính).

Ánh xạ f: V $\to$ W được gọi là một ánh xạ tuyến tính (hoặc rõ hơn, một ánh

xa K-tuyến tính), nếu

$f(\alpha$ + $\beta) = f(\alpha)$ + $f(\beta)$,

$f(a\alpha) = af(\alpha)$,



với mọi $\alpha$, $\beta \in$ V và mọi vô hướng a $\in \mathbf{K}$.

Ánh xạ tuyến tính cũng được gọi là đồng cấu tuyến tính, hay đồng cấu cho đơn

giản.

Nhận xét rằng hai điều kiện trong định nghĩa ánh xạ tuyến tính tương đương

với điều kiện sau:

$f(a\alpha$ + $b\beta) = af(\alpha)$ + $bf(\beta)$, $\quad \forall \alpha$, $\beta \in$ V, $\forall$ a, b $\in \mathbf{K}$.

Các tính chất sau đây của ánh xạ tuyến tính được suy ngay từ định nghĩa. Giả

sử f: V $\to$ W là một ánh xạ tuyến tính. Khi đó, ta có

(1) f(0) $=$ 0.

Thật vậy, f(0) $=$ f(0 + 0) $=$ f(0) + f(0). Theo luật giản ước, f(0) $=$ 0.

(2) $f(-\alpha) = -f(\alpha)$, $\forall \alpha \in$ V.

Thật vậy, $f(\alpha)$ + $f(-\alpha) = f(\alpha$ + $(-\alpha)) =$ f(0) $=$ 0. Do đó, $f(-\alpha) = -f(\alpha)$.

(3) $f(a_1\alpha_1+\cdots+a_n\alpha_n)=a_1f(\alpha_1)+\cdots+a_nf(\alpha_n)$, $\forall a_1,\ldots,a_n\in\mathbf{K},\forall\alpha_1,\ldots,\alpha_n\in$ V.

Đằng thức này có thể được chứng minh bằng quy nạp.

Ví dụ 2.2 (a) Anh xạ 0: V $\to$ W xác định bởi công thức $0(\alpha) =$ 0 với mọi

$\alpha \in$ V là một ánh xạ tuyến tính.

(b) Ánh xạ đồng nhất $id_V:$ V $\to$ V, $id_V(\alpha) = \alpha$ là một ánh xạ tuyến tính.

(c) Dạo hàm hình thức

$\frac{d}{dX}: \mathbf{K}[X] \rightarrow \mathbf{K}[X]$,

$\frac{d}{dX}(a_nX^n$ + $\dots$ + $a_1X_1$ + $a_0) = na_nX^{n-1}$ + $\dots$ + $a_1$

là một ánh xạ tuyến tính.



(d) Phép liên hợp phức c: $\mathbf{C} \to \mathbf{C}$, z $\mapsto \bar{z}$ là một ánh xạ $\mathbf{R}-tuyến$ tính, nhưng

không phải là một ánh xạ C-tuyến tính. Thậy vậy,

-1 $=$ c(-1) $= c(i^2) \neq$ ic(i) $=$ i(-i) $=$ 1.

(e) Giả sử A $= (a_{ij}) \in$ M(m $\times$ n, $\mathbf{K})$. Khi đó ánh xạ

$\tilde{A}: \mathbf{K}^n \rightarrow \mathbf{K}^m$,

$ \left(\begin{array}{c} x_1 \\ \vdots \\ x_n \end{array}\right) \mapsto A \left(\begin{array}{c} x_1 \\ \vdots \\ x_n \end{array}\right) $

là một ánh xa tuyến tính.

Các phép chiếu

(f)

$pr_i: V_1 \times V_2 \rightarrow V_i$,

$pr_i(v_1$, $v_2) = v_i$

là các ánh xạ tuyến tính, với i $=$ 1, 2.

(g) Giả sử W là một không gian vécto con của V. Khi đó phép chiếu

$\pi:$ V $\rightarrow$ V/W

$\pi(\alpha) = [\alpha] = \alpha$ + W

là một ánh xạ tuyến tính.

### Định nghĩa 2.3 Giả sử V và W là các K-không gian vécto. Tập hợp tất cả các

ánh xạ tuyến tính từ V vào W được ký hiệu là $\mathcal{L}(V$, W) (hoặc Hom(V, W)).

Vì $\mathcal{L}(V$, W) chứa ánh xạ 0, nên $\mathcal{L}(V$, W) $\neq \emptyset$.

Ta trang bị cho $\mathcal{L}(V$, W) hai phép toán cộng và nhân với vô hướng được định

nghĩa như sau

$(f+g)(\alpha) = f(\alpha)$ + $g(\alpha)$,

$(af)(\alpha) = af(\alpha) \quad \alpha \in$ V, a $\in \mathbf{K}$,



với moi f, g $\in \mathcal{L}(V$, W).

Dễ dàng kiểm tra lại rằng $\mathcal{L}(V$, W) là một K-không gian vécto đối với hai phép

toán đó.

### Dịnh lý sau đây chỉ ra một tính chất quan trọng của ánh xạ tuyến tính.

Dinh lý 2.4 Mỗi ánh xa tuyến tính từ V vào W được hoàn toàn xác định bởi ảnh

của nó trên một cơ sở. Nói rõ hơn, giả sử $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở của V, còn

$\omega_1$, ..., $\omega_n$ là các véctor bất kỳ của W. Khi đó, tồn tại duy nhất một ánh xạ tuyến

tinh f: V $\to$ W sao cho $f(\alpha_i) = \omega_i$ (i $=$ 1, 2, ..., n).

Chứng minh: Sự tồn tại: Nếu $\alpha = a_1 \alpha_1$ + $\cdots$ + $a_n \alpha_n$, thì ta đặt

$f(\alpha) = a_1\omega_1$ + $\cdots$ + $a_n\omega_n$.

Dễ dàng thử lại rằng f: V $\to$ W là một ánh xạ tuyến tính, và $f(\alpha_i) = \omega_i$

(i $=$ 1, 2, ..., n).

Tính duy nhất: Nếu f và g là các ánh xạ tuyến tính từ V vào W với $f(\alpha_i) =$

$q(\alpha_i)=\omega_i (i=1,2,...,n),thì$ với mọi $\alpha=a_1\alpha_1+\cdots+a_n\alpha_n,ta$ có

$f(\alpha) = f(\sum_{i=1}^{n} a_i \alpha_i) = \sum_{i=1}^{n} a_i f(\alpha_i) = \sum_{i=1}^{n} a_i g(\alpha_i) = g(\sum_{i=1}^{n} a_i \alpha_i) = g(\alpha)$.

### Định nghĩa 2.5 Một đồng cấu (tuyến tính) f: V \to W đồng thời là một đơn ánh

được gọi là một đơn cấu (tuyến tính). Một đồng cấu (tuyến tính) đồng thời là một

toàn ánh được gọi là một toàn cấu (tuyến tính). Một đồng cấu (tuyến tính) đồng

thời là một song ánh được gọi là một đẳng cấu (tuyến tính).

Nếu f: V $\to$ W là một đẳng cấu, thì $f^{-1}:$ W $\to$ V cũng là một đẳng cấu; nó

được gọi là nghịch đảo của f. Do đó mỗi đẳng cấu còn được gọi là một đồng cấu

khả nghịch. Nếu có một đẳng cấu f: V $\to$ W, thì ta nói V đẳng cấu với W và viết

V $\cong$ W.

Quan hê $\cong$ là môt quan hê tương đương.



Nhận xét rằng đồng cấu f: V $\to$ W là một đẳng cấu nếu và chỉ nếu có một

đồng cấu g: W $\to$ V sao cho gf $= id_V$ và fg $= id_W$. Khi đó, g $= f^{-1}$. Thật

vậy, nếu f là một đẳng cấu thì $f^{-1}f = id_V$, $ff^{-1} = id_W$. Ngược lại, nếu có một

đồng cấu g: W $\to$ V sao cho gf $= id_V$, fg $= id_W$, thì f vừa là một đơn cấu (do

gf $= id_V)$, vừa là một toàn cấu (do fg $= id_W)$. Vì thế, f là một đẳng cấu. Khi đó,

nhân hai về của đẳng thức gf $= id_V$ với $f^{-1}$ từ bên phải, ta thu được g $= f^{-1}$.

Mệnh đề 2.6 Giả sử V và W là các không gian vécto hữu hạn chiều. Khi đó

V $\cong$ W $\Longleftrightarrow \dim$ V $= \dim$ W.

Chứng minh: Giả sử V $\cong$ W, tức là có một đẳng cấu tuyến tính f: V $\stackrel{\cong}{\to}$ W.

Khi đó, nếu $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở của V thì $(f(\alpha_1)$, ..., $f(\alpha_n))$ là một cơ sở của

W. Thật vậy, mỗi vécto $\beta \in$ W có dạng $\beta = f(\alpha)$ với $\alpha$ nào đó trong W. Vì $\alpha$ có

biểu thị tuyến tính $\alpha = a_1 \alpha_1$ + $\cdots$ + $a_n \alpha_n$, nên

$\beta = f(\alpha) = f(a_1\alpha_1$ + $\cdots$ + $a_n\alpha_n) = a_1f(\alpha_1)$ + $\cdots$ + $a_nf(\alpha_n)$.

Nếu $\beta$ còn có biểu thị tuyến tính $\beta = b_1 f(\alpha_1)$ + $\cdots$ + $b_n f(\alpha_n)$, thì $\alpha = f^{-1}(\beta) =$

$b_1\alpha_1$ + $\cdots$ + $b_n\alpha_n$. Vì $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở của V cho nên $a_1 = b_1$, ..., $a_n = b_n$.

Như vậy, mỗi vécto $\beta$ biểu thị tuyến tính duy nhất qua hệ $(f(\alpha_1),...,f(\alpha_n))$, nên

hệ này là một cơ sở của W. Nói riêng, dim V $= \dim$ W.

Ngược lại, giá sử dim V $= \dim$ W $=$ n. Chọn các cơ sở $(\alpha_1$, ..., $\alpha_n)$ của V và

$(\beta_1,...,\beta_n)$ của W.Ánh xạ tuyến tính duy nhất $\varphi\,:\,V\,\to\,W$ được xác định bởi

$\varphi(\alpha_1) = \beta_1$, ..., $\varphi(\alpha_n) = \beta_n$ là một đẳng cấu tuyến tính. Thật vậy, nghịch đảo

của $\varphi$ là ánh xạ tuyến tính $\psi$ : W $\to$ V được xác định bởi điều kiện $\psi(\beta_1) =$

$\alpha_1$, ..., $\psi(\beta_n) = \alpha_n$.

$\Box$

Tương ứng đặt mỗi ánh xạ tuyến tính với ma trận của nó mà ta sắp định nghĩa

là một ví dụ điển hình về đẳng cấu tuyến tính. Nhờ đẳng cấu này mà người ta có

thể tính toán cụ thể với các ánh xạ tuyến tính.



Giả sử V và W là các K-không gian vécto với các cơ sở tương ứng là $(\alpha_1$, ..., $\alpha_n)$

và $(\beta_1$, ..., $\beta_m)$. Theo Định lý 2.4, ánh xạ tuyến tính f: V $\to$ W được xác định duy

nhất bởi $f(\alpha_1),...,f(\alpha_n)$. Các véctơ này lại có biểu thị tuyến tính duy nhất qua

co sò $(\beta_1$, ..., $\beta_m)$ của W:

$f(\alpha_j) = \sum_{i=1}^m a_{ij} \beta_i \quad$ (j $=$ 1, ..., n),

trong đó $a_{ij} \in \mathbf{K}$. Nói gọn lại, ánh xạ tuyến tính f: V $\to$ W được xác định duy

nhất bởi hệ thống các vô hướng $\{a_{ij}|1 \leq$ i $\leq$ m, 1 $\leq$ j $\leq n\}$, chúng được xếp thành

ma trận sau đây:

$ \left(\begin{array}{cccc} a_{11} & a_{12} & \dots & a_{1n} \\ & & \ddots & \ddots & \vdots \\ & & & a_{n} \end{array}\right) $

$ A = \begin{bmatrix} a_{21} & a_{22} & \dots & a_{2n} \\ \cdot & \cdot & \dots & \cdot \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{bmatrix} = (a_{ij})_{m \times n}. $

Ta gọi A là ma trận của ánh xạ tuyến tính f: V $\to$ W trong cặp cơ sở $(\alpha_1$, ..., $\alpha_n)$

và $(\beta_1$, ..., $\beta_m)$.

Nếu véctor $\alpha$ có toạ độ $(x_1,...,x_n)$ trong cơ sở $(\alpha_1,...,\alpha_n)$ thì toạ độ của $f(\alpha)$

trong cơ sở $(\beta_1$, ..., $\beta_m)$ được tính bằng công thức

$y_i = \sum_{i=1}^n a_{ij} x_j$ (i $=$ 1, 2, ..., m).

Thật vậy,

$\sum_{i=1}^{m} y_i \beta_i = f(\alpha) = f(\sum_{j=1}^{n} x_j \alpha_j) = \sum_{j=1}^{n} x_j f(\alpha_j)$

$= \sum_{j=1}^{n} x_j \sum_{i=1}^{m} a_{ij} \beta_i$

$= \sum_{i=1}^{\infty} (\sum_{j=1}^{\infty} a_{ij} x_j) \beta_i$.

Vì biểu thị tuyến tính của mỗi véctor thuộc W qua cơ sở $(\beta_1$, ..., $\beta_m)$ là duy nhất,

nên ta thu được công thức xác định $(y_1$, ..., $y_m)$ qua ma trận A và $(x_1$, ..., $x_n)$ đã nói

ở trên.



Trong ngôn ngữ tích ma trận, sự kiện A $= (a_{ij})_{m \times n}$ là ma trận của ánh xạ tuyến

tính f: V $\to$ W trong cặp cơ sở $(\alpha_1$, ..., $\alpha_n)$ và $(\beta_1$, ..., $\beta_m)$, tức là hệ đẳng thức

$f(\alpha_j) = \sum_{i=1}^m a_{ij} \beta_i$ (j $=$ 1, ..., n) được quy vớc viết như sau:

$ (f(\alpha_1) ... f(\alpha_n)) = (\beta_1 ... \beta_m) \begin{pmatrix} a_{11} & a_{12} & ... & a_{1n} \\ a_{21} & a_{22} & ... & a_{2n} \\ ... & ... & ... & ... \\ a_{m1} & a_{m2} & ... & a_{mn} \end{pmatrix}. $

Công thức tính toạ độ $(y_1$, ..., $y_m)$ của $f(\alpha)$ trong cơ sở $(\beta_1$, ..., $\beta_m)$ qua toạ độ

$(x_1,...,x_n)$ của $\alphatrong$ cơ sở $(\alpha_1,...,\alpha_n)được$ diễn đạt lại trong ngôn ngữ ma trận

nhu sau:

$ \left( \begin{array}{c} y_1 \\ . \\ . \\ y_m \end{array} \right) = \left( \begin{array}{cccc} a_{11} & a_{12} & \ldots & a_{1n} \\ a_{21} & a_{22} & \ldots & a_{2n} \\ . & . & \ldots & . \\ a_{m1} & a_{m2} & \ldots & a_{mn} \end{array} \right) \left( \begin{array}{c} x_1 \\ . \\ . \\ . \\ x_n \end{array} \right). $

### Dịnh lý 2.7 Ánh xạ đặt tương ứng đồng cấu f với ma trận của nó A = M(f)

trong một cặp cơ sở cố định của V và W là một đẳng cấu tuyến tính từ $\mathcal{L}(V$, W)

lên M(m $\times$ n, $\mathbf{K})$. Nói riêng, dim $\mathcal{L}(V$, W) $= \dim$ V $\times \dim$ W.

Chứng minh: Giả sử trong cặp cơ sở $(\alpha_1$, ..., $\alpha_n)$ của V và $(\beta_1$, ..., $\beta_m)$ của W các

đồng cấu f và g có các ma trận tương ứng là A $= (a_{ij})_{m \times n}$ và B $= (b_{ij})_{m \times n}$. tức

là:

$f(\alpha_j) = \sum_{i=1}^m a_{ij} \beta_i$,

$g(\alpha_j) = \sum_{i=1}^m b_{ij} \beta_i$, $\quad$ (j $=$ 1, ..., n).

Khi đó

$(f+g)(\alpha_j) = \sum_{i=1}^{\infty} (a_{ij}$ + $b_{ij})\beta_i$,

(a $f)(\alpha_j) = \sum_{i=1}^m$ a $a_{ij} \beta_i$, $\quad$ (j $=$ 1, ..., n).



Như vậy, ma trận của f + g là A + B, ma trận của af là aA (trong cặp cơ sở đã

cho). Nói cách khác

M(f+g) $=$ M(f) + M(g),

M(af) $=$ aM(f).

Các hệ thức này chứng tỏ rằng phép đặt tương ứng mỗi đồng cấu với ma trận của

nó trong một cặp cơ sở cố định là một ánh xạ tuyến tính.

Mặt khác, theo Định lý 2.4, ánh xạ nói trên là một song ánh. Tóm lại, đó là

một đẳng cấu tuyến tính.

$\Box$

Mệnh đề 2.8 Nếu f: V $\to$ W và g: W $\to$ Z là các ánh xạ tuyến tính, thì

gf: V $\to$ Z cũng là một ánh xạ tuyến tính.

Chứng minh: Thật vậy, ta có

$gf(a\alpha$ + $b\beta) =$ g(a $f(\alpha)$ + $bf(\beta))$

$= a(gf)(\alpha)$ + $b(gf)(\beta)$,

với mọi a, b $\in \mathbf{K}$ và mọi $\alpha$, $\beta \in$ V.

$\Box$

Mệnh đề 2.9 Giả sử đồng cấu f có ma trận A trong cặp cơ sở $(\alpha_1$, ..., $\alpha_n)$,

$(\beta_1$, ..., $\beta_m)$ và đồng cấu g có ma trận B trong cặp cơ sở $(\beta_1$, ..., $\beta_m)$, $(\gamma_1$, ..., $\gamma_\ell)$.

Khi đó, ma trận của đồng cấu gf trong cặp cơ sở $(\alpha_1$, ..., $\alpha_n)$, $(\gamma_1$, ..., $\gamma_\ell)$ chính là

ma trận tích BA.

Chứng minh: Theo giả thiết, ta có

$f(\alpha_i) = \sum_{j=1}^m a_{ji} \beta_j$,

$g(\beta_j) = \sum_{k=1}^{\ell} b_{kj} \gamma_k$.



Từ đó, do g là một ánh xạ tuyến tính, ta có

$(gf)(\alpha_i) = g(\sum_{j=1}^m a_{ji}\beta_j) = \sum_{j=1}^m a_{ji}g(\beta_j)$

$= \sum_{j=1}^m a_{ji} \sum_{k=1}^{\ell} b_{kj} \gamma_k = \sum_{k=1}^{\ell} (\sum_{j=1}^m b_{kj} a_{ji}) \gamma_k$.

Gọi C $= (c_{ki})_{\ell \times n}$ là ma trận của gf trong cặp cơ sở $(\alpha_1$, ..., $\alpha_n)$, $(\gamma_1$, ..., $\gamma_\ell)$. Khi

đó

$(gf)(\alpha_i) = \sum_{k=1}^{\ell} c_{ki} \gamma_k$.

Vì biểu thị tuyến tính của $(gf)(\alpha_i)$ qua cơ sở $(\gamma_1$, ..., $\gamma_\ell)$ là duy nhất, nên ta thu

duoc

$c_{ki} = \sum b_{kj} a_{ji}$, $\quad$ (1 $\le$ k $\le \ell$, 1 $\le$ i $\le$ n).

$i=1$

Hệ đẳng thức này tương đương với đẳng thức ma trận

C $=$ BA. $\Box$

Nếu một trong hai vế của các đẳng thức sau đây giữa các ánh xạ tuyến tính là

có nghĩa thì về kia cũng vậy. Khi đó, ta có các đẳng thức (dễ kiểm tra):

h(gf) $=$ (hg)f,

$g(f_1$ + $f_2) = gf_1$ + $gf_2$,

$(g_1$ + $g_2)f = g_1f$ + $g_2f$.

### Định nghĩa 2.10 Mỗi đồng cấu (tuyến tính) từ không gian vécto V vào chính nó

được gọi là một tự đồng cấu (tuyến tính) của V. Một tự đồng cấu của V đồng thời

là một đẳng cấu được gọi là một tự đẳng cấu của V.

Không gian vécto tất cả các tự đồng cấu của V được ký hiệu là End(V). Tập

hợp tất cả các tự đẳng cấu của V được ký hiệu là GL(V).

Dễ dàng kiểm tra lại rằng End(V) là một vành đối với hai phép toán cộng và

nhân (hợp thành) các tự đồng cấu. Nó được gọi là vành các tự đồng cấu của V.

Vành này có đơn vị là $id_V$ và không giao hoán nếu dim V $>$ 1.



Để cho gọn, ta sẽ gọi ma trận của f $\in$ End(V) trong cặp cơ sở $(\alpha_1$, ..., $\alpha_n)$,

$(\alpha_1$, ..., $\alpha_n)$ là ma trận của f trong cơ sở $(\alpha_1$, ..., $\alpha_n)$.

Dinh lý 2.11 Giá sử V là một K-không gian vécto với dim V $=$ n. Khi đó ánh xạ

đặt tương ứng mỗi tự đồng cấu f $\in$ End(V) với ma trận của nó M(f) trong cơ sở

$(\alpha_1$, ..., $\alpha_n)$ là một đẳng cấu vành từ End(V) vào M(n $\times$ n, $\mathbf{K})$.

Chứng minh: Đây là một hệ quả trực tiếp của Định lý 2.7 và Mệnh đề 4.5.

$\Box$

Nhận xét rằng f $\in$ End(V) là một đẳng cấu nếu và chỉ nếu tồn tại đồng cấu

g $\in$ End(V) sao cho

qf $=$ fg $= id_V$.

Khi đó g $= f^{-1}$.

Do nhận xét này ta dễ dàng kiểm tra rằng GL(V) là một nhóm đối với phép

nhân là phép hợp thành các ánh xạ. GL(V) được gọi là nhóm tuyến tính tổng quát

của không gian vécto V.

Theo Định lý 2.11, f $\in$ End(V) là một đẳng cấu nếu và chỉ nếu M(f) $\in$

M(n $\times$ n, $\mathbf{K})$ là một ma trận khả nghịch.

Tương ứng f $\leftrightarrow$ M(f) nói trong Định lý 2.11 được mô tả trong biểu đồ sau:

End(V) dẳng cấu vành M(n $\times$ n, $\mathbf{K})$

$\bigcup$

U

$\ddot{\text{d}}ằng$ cấu nhóm

GL(n, $\mathbf{K})$.

GL(V)

Mệnh đề 2.12 Giả sử A là ma trận của tự đồng cấu f: V $\to$ V trong cơ sở

$(\alpha_1$, ..., $\alpha_n)$, và C là ma trận chuyển từ cơ sở $(\alpha_1$, ..., $\alpha_n)$ sang cơ sở $(\alpha'_1$, ..., $\alpha'_n)$.

Khi đó, ma trận của f trong cơ sở $(\alpha'_1$, ..., $\alpha'_n)$ là $C^{-1}AC$.

Chứng minh: C là ma trận chuyển từ cơ sở $(\alpha_1$, ..., $\alpha_n)$ sang cơ sở $(\alpha'_1$, ..., $\alpha'_n)$ của

không gian véctor V, nghĩa là ta có

$(\alpha'_1 \dots \alpha'_n) = (\alpha_1 \dots \alpha_n)C$.



Nhân hai vế của đẳng thức trên với $C^{-1}$ từ bên phải, ta thu được

$(\alpha_1$ ... $\alpha_n) = (\alpha'_1$ ... $\alpha'_n)C^{-1}$.

Tự đồng cấu f $\in$ End(V) có ma trận là A trong cơ sở $(\alpha_1$, ..., $\alpha_n)$, nghĩa là

$(f(\alpha_1)$ ... $f(\alpha_n)) = (\alpha_1$ ... $\alpha_n)A$.

Vì f là một đồng cấu, cho nên ta có

$(f(\alpha'_1)$ ... $f(\alpha'_n)) = (f(\alpha_1)$ ... $f(\alpha_n))C$

$= (\alpha_1 \dots \alpha_n)AC$

$= (\alpha'_1$ ... $\alpha'_n) C^{-1}$ A C.

Do tính duy nhất của biểu thị tuyến tính của mỗi véctơ qua một cơ sở, cho nên

$C^{-1}AC$ chính là ma trận của f trong cơ sở $(\alpha'_1$, ..., $\alpha'_n)$.

$\Box$

Một hệ luận trực tiếp của mệnh đề trên là như sau.

Hệ quả 2.13 Hai ma trận vuông đồng dạng với nhau nếu và chỉ nếu chúng là ma

trận của cùng một tự đồng cấu của một không gian vécto trong các cơ sở nào đó

của không gian này.

$\Box$

Hat nhân và ảnh của đồng cấu

$3\phantom{.}$

Chúng ta mở đầu tiết này bằng nhận xét đơn giản sau đây.

Mệnh đề 3.1 Giả sử f: V $\to$ W là một đồng cấu. Khi đó, ảnh bởi f của mỗi

không gian vécto con của V là một không gian vécto con của W. Nghịch ảnh bởi

f của mỗi không gian vécto con của W là một không gian vécto con của V.

Chứng minh: Giả sử T là một không gian vécto con của V. Khi đó, f(T) $\neq \emptyset$,

bởi vì nó chứa véctor 0. Hơn nữa, nếu $\alpha'$, $\beta'$ là những véctor của f(T) thì chúng có



dạng $\alpha' = f(\alpha)$, $\beta' = f(\beta)$, trong đó $\alpha$, $\beta \in$ T. Khi đó, vì f là một đồng cấu, cho

nên với vô hướng bất kỳ a $\in \mathbf{K}$, ta có

$\alpha'$ + $\beta' = f(\alpha)$ + $f(\beta) = f(\alpha$ + $\beta) \in$ f(T),

$a\alpha' = af(\alpha) = f(a\alpha) \in$ f(T).

Vậy f(T) là một không gian véctor con của W.

Bây giờ giả sử U là một không gian véctor con của W. Khi đó, $f^{-1}(U) \neq \emptyset$, bởi

vì nó cũng chứa vécto 0. Nếu $\alpha$, $\beta \in f^{-1}(U)$ thì $f(\alpha)$, $f(\beta) \in$ U. Vì f là một đồng

cấu, cho nên với moi vô hướng a $\in \mathbf{K}$, ta có

$f(\alpha$ + $\beta) = f(\alpha)$ + $f(\beta) \in$ U

$f(a\alpha) = af(\alpha) \in$ U

Vì thế $\alpha$ + $\beta$ và $a\alpha \in f^{-1}(U)$. Vậy $f^{-1}(U)$ là một không gian véctor con của V. $\Box$

Hạt nhân và ảnh của một đồng cấu là những không gian vécto đặc biệt quan

trọng đối với việc khảo sát đồng cấu đó. Chúng được định nghĩa như sau.

### Định nghĩa 3.2 Giả sử f: V \to W là một đồng cấu.

(i) Ker(f) $= f^{-1}(0) = \{x \in$ V | f(x) $= 0\} \subset$ V được gọi là hạt nhân (hay hạch)

của f. Số chiều của Ker(f) được gọi là số khuyết của f.

(ii) Im(f) $=$ f(V) $= {f(x)|x \in V} \subset$ W được gọi là ảnh của f. Số chiều của

Im(f) được gọi là hang của f và được ký hiệu là rank(f).

Hai định lý sau đây nêu những điều kiện cần và đủ để một đồng cấu là một

toàn cấu hay một đơn cấu.

### Dịnh lý 3.3 Đồng cấu f: V \to W là một toàn cấu nếu và chỉ nếu rank(f) =

$\dim$ W.



Chứng minh: Theo định nghĩa, f là một toàn cấu nếu và chỉ nếu Im(f) $=$ W.

Vì Im(f) là một không gian véctor con của W, cho nên đẳng thức nói trên tương

dương với $\text{rank}(f) := \dim$ f(V) $= \dim$ W.

Thật vậy, nếu f(V) $=$ W thì hiển nhiên dim f(V) $= \dim$ W. Ngược lại, giả

sử dim f(V) $= \dim$ W; do f(V) là một không gian véctor con của W, nên mỗi co

sở của f(V) cũng là một hệ độc lập tuyến tính trong W với số phần tử bằng

$\dim$ f(V) $= \dim$ W. Nói cách khác, mỗi cơ sở của f(V) cũng là một cơ sở của W.

Vây f(V) $=$ W.

$\Box$

### Định lý 3.4 Đối với đồng cấu f: V \to W các điều kiện sau đây là tương đương:

(i) f là một đơn cấu.

(ii) Ker(f) $= \{0\}$.

(iii) Ánh bởi f của mỗi hệ véctơ độc lập tuyến tính là một hệ véctơ độc lập tuyến

tinh.

(iv) Ánh bởi f của mỗi cơ sở của V là một hệ véctơ độc lập tuyến tính.

(v) Ánh bởi f của một cơ sở nào đó của V là một hệ véctơ độc lập tuyến tính.

(vi) rank(f) $=$ dim V.

Chứng minh: (i) $\Rightarrow$ (ii) : Giả sử $\alpha \in$ Ker(f). Khi đó $f(\alpha) =$ f(0) $=$ 0. Vì f là

một đơn cấu, cho nên $\alpha =$ 0. Do đó Ker(f) $= \{0\}$.

(ii) $\Rightarrow$ (iii): Giả sử $(\alpha_1$, ..., $\alpha_k)$ là một hệ vécto độc lập tuyến tính trong V.

Nếu có một ràng buộc tuyến tính giữa các ảnh bởi f của các phần tử đó

$\sum_{i=1} a_i f(\alpha_i) =$ 0 $\ (a_i \in \mathbf{K})$,

thì $f(\sum_{i=1}^k a_i \alpha_i) =$ 0. Vì Ker(f) $= \{0\}$, cho nên $\sum_{i=1}^k a_i \alpha_i =$ 0. Từ đó, ta có

$a_1 = \cdots = a_k =$ 0, bởi vì hệ vécto $(\alpha_1$, ..., $\alpha_k)$ độc lập tuyến tính. Như thế, hệ

$(f(\alpha_1),...,f(\alpha_k))$ cũng độc lập tuyến tính.



Các suy luận (iii) $\Rightarrow$ (iv), (iv) $\Rightarrow$ (v) đều hiển nhiên.

(v) $\Rightarrow$ (vi): Giả sử $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở của V sao cho $(f(\alpha_1)$, ..., $f(\alpha_n))$ là

một hệ độc lập tuyến tính. Rõ ràng hệ này sinh ra f(V). Ta có

rank(f) $= \dim$ f(V) $= \text{rank}(f(\alpha_1)$, ..., $f(\alpha_n)) =$ n $= \dim$ V.

(vi) $\Rightarrow$ (i): Giả sử $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở của V. Ta có

rank(f) $= rank(f(\alpha_1)$, ..., $f(\alpha_n)) =$ dim V $=$ n,

cho nên hệ vécto $(f(\alpha_1),...,f(\alpha_n))$ độc lập tuyến tính. Giả sử $\alpha = \sum_i a_i \alpha_i$, $\beta =$

$\sum_i b_i \alpha_i$ và $f(\alpha) = f(\beta)$. Khi đó,

0 $= f(\alpha)$ - $f(\beta) = f(\alpha$ - $\beta) = f(\sum_i (a_i$ - $b_i)\alpha_i = \sum_i (a_i$ - $b_i)f(\alpha_i)$.

Từ đó $a_1 = b_1$, ..., $a_n = b_n$, bởi vì $(f(\alpha_1)$, ..., $f(\alpha_n))$ độc lập tuyến tính. Điều này có

nghĩa là $\alpha = \beta$. Vậy f là một đơn cấu.

$\Box$

### Định lý 3.5 (Định lý về đồng cấu các không gian vécto). Giả sử f: V \to W là

một đồng cấu. Khi đó, ánh xạ $\overline{f}:$ V/Ker(f) $\to$ W, xác định bởi $\overline{f}([\alpha]) = f(\alpha)$, là

một đơn cấu. Nó cảm sinh đẳng cấu $\overline{f}:V/Ker(f) \stackrel{\cong}{\rightarrow}$ Im(f).

Chứng minh: Trước tiên, cần chứng tỏ rằng f được định nghĩa không phụ thuộc

việc chọn đại biểu của lớp $[\alpha]$. Thật vậy, nếu $[\alpha] = [\alpha']$, thì $\alpha$ - $\alpha' \in$ Ker(f). Nói

cách khác $f(\alpha$ - $\alpha') =$ 0, hay là $f(\alpha) = f(\alpha')$.

Vì f là một đồng cấu, nên dễ dàng kiểm tra $\overline{f}$ cũng là một đồng cấu.

Giả sử $\overline{f}([\alpha]) = \overline{f}([\beta])$, tức là $f(\alpha) = f(\beta);$ khi đó $f(\alpha$ - $\beta) =$ 0. Vì thế

$\alpha$ - $\beta \in$ Ker(f), nghĩa là $[\alpha] = [\beta]$. Điều đó chứng tỏ rằng $\overline{f}$ là một đơn cấu. Hơn

nữa, từ định nghĩa của $\overline{f}$ ta có $Im(\overline{f}) =$ Im(f). Cho nên, nếu xét $\overline{f}$ như một đồng

cấu từ V/Ker(f) tới Im(f) thì đó là một đẳng cấu.

$\Box$

Hệ quả 3.6 Đối với đồng cấu bất kỳ f: V $\to$ W, ta có

$\dim$ V $= \dim$ Ker(f) + $\dim$ Im(f).



Chứng minh: Theo định lý trên, ta có

$\dim$ Im(f) $= \dim Im(\overline{f}) = \dim$ V/Ker(f) $= \dim$ V - $\dim$ Ker(f).

Hệ quả 3.7 Giả sử f: V $\to$ W là một đồng cấu. Khi đó, với mọi không gian

vécto con U của V, ta có

$\dim$ f(U) $\leq \dim$ U.

Nói cách khác, ánh xạ tuyến tính không làm tăng chiều của các không gian véctơ.

Chứng minh: Xét hạn chế $f|_U$ của ánh xạ f trên không gian véctor con U, ta có

$\dim$ U $= \dim Ker(f|_U)$ + $\dim Im(f|_U) \geq \dim Im(f|_U) = \dim$ f(U).

Hệ quả 3.8 Giả sử f: V $\to$ V là một tự đồng cấu của không gian vécto hữu hạn

chiều V. Khi đó, các khẳng định sau đây là tương đương:

(i) f là một đẳng cấu.

(ii) f là một đơn cấu.

(iii) f là một toàn cấu.

Chứng minh: Theo Định lý 3.4, f là một đơn cấu nếu và chỉ nếu dim Ker(f) $=$ 0.

Mặt khác, theo Định lý 3.3, f là một toàn cấu khi và chỉ khi dim Im(f) $= \dim$ V.

Theo Hệ quả 3.6, hai điều kiện nói trên tương đương với nhau. Do đó, chúng cùng

tương đương với sự kiện f là một đẳng cấu.

$\Box$

Nhận xét: Hệ quả trên không còn đúng nếu V là một không gian vécto vô hạn

chiều. Thật vậy, đồng cấu

$\varphi$ : $\mathbf{K}[X] \rightarrow \mathbf{K}[X]$

$\varphi(X^n) = X^{n+1}$ (n $=$ 0, 1, 2...)



là một đơn cấu nhưng không là một toàn cấu. Ngược lại, đồng cấu

$\psi$ : $\mathbf{K}[X] \rightarrow \mathbf{K}[X]$

$\varphi(X^n) = X^{n-1}$ (n $=$ 0, 1, 2...),

trong đó quy $ướcX^{-1}=\psi(1)=0$, là một toàn cấu nhưng không là một đơn cấu.

Trên cơ sở hệ quả nói trên, các Định lý 3.3 và 3.4 cho ta hàng loạt điều kiện để

một tự đồng cấu tuyến tính của một không gian vécto hữu hạn chiều là một đẳng

cấu.

### Định nghĩa 3.9 (Hạng của ma trận). Giả sử A là một ma trận m hàng n cột với

các phần tử trong trường K. Hạng của hệ n vécto cột của A trong $\mathbf{K}^m$ được gọi

là hang của ma trận A và được ký hiệu là rankA.

### Định lý sau đây cho ta một phương pháp để tính hạng của các đồng cấu.

### Định lý 3.10 Giả sử đồng cấu f: V \to W có ma trận là A trong một cặp cơ sở

nào đó của V và W. Khi đó:

rankf $=rankA$.

Chứng minh: Giả sử f có ma trận là A trong cặp cơ sở $(\alpha_1$, ..., $\alpha_n)$ của V và

$(\beta_1$, ..., $\beta_m)$ của W. Theo định nghĩa, ta có

rankf $= \dim$ Im(f) $= \text{rank}(f(\alpha_1)$, ..., $f(\alpha_n))$.

Vì $(\beta_1$, ..., $\beta_m)$ là một cơ sở của W cho nên ánh xạ

$\varphi:W\;\;\rightarrow\;\;{\bf K}^m$,

$ \sum_{j=1}^m b_j \beta_j ~~\mapsto~~\left(\begin{array}{c} b_1\\ \vdots\\ b_m \end{array}\right) $



là một đẳng cấu tuyến tính. (Thật vậy, ánh xạ đó chuyển cơ sở $(\beta_1$, ..., $\beta_m)$ thành

cơ sở chính tắc của $\mathbf{K}^m.)$

Dằng cấu $\varphi$ đưa $f(\alpha_i)$ vào cột thứ i của ma trận A, bởi vì

$ f(\alpha_i) = \sum_{j=1}^m a_{ji} \beta_j \quad \stackrel{\varphi}{\mapsto} \quad \left( \begin{array}{c} a_{1i} \ \vdots \ a_{mi} \end{array} \right). $

Vì các đẳng cấu tuyến tính đều bảo toàn hạng của mỗi hệ véctơ, nên ta có

rankf $= \text{rank}(f(\alpha_1)$, ..., $f(\alpha_n)) = \text{rank}A$.

$\Box$

Không gian véctơ đối ngẫu

$\bf{4}$

Ý chính của tiết này là ta có thể nghiên cứu một không gian vécto thông qua tập

hợp tất cả các hàm tuyến tính trên không gian này. Nói một cách nôm na, tập hợp

các hàm như thế lập nên cái gọi là không gian véctơ đối ngẫu, nó có thể coi là "ảnh

đối xứng qua gương" của không gian vécto đã cho.

Giả sử V là một không gian vécto trên trường $\mathbf{K}$.

### Định nghĩa 4.1 Không gian V^* = \mathcal{L}(V, \mathbf{K}) các ánh xạ tuyến tính từ V vào K

được gọi là không gian vécto đối ngẫu của V. Mỗi phần tử của $V<sup>*</sup>$ được gọi là một

dạng tuyến tính trên V.

Ta đã biết rằng $V^*$ là một không gian vécto với số chiều bằng

$\dim V^* = \dim$ V $\cdot \dim$ K $= \dim$ V.

Như thế $V^* \cong$ V nếu dim V $< \infty$. Điều này không còn đúng nếu V là một không

gian vécto vô hạn chiều. Tính không tự nhiên của đẳng cấu nói trên sẽ được thảo

luận ở phần sau của tiết này.



Giả sử f: V $\to$ W là một đồng cấu. Ta định nghĩa ánh xạ $f^*: W^* \to V^*$ bởi

công thức sau đây

$(f^*(\varphi))(\alpha) = \varphi(f(\alpha))$, $\ \ \forall \varphi \in W^*$, $\ \forall \alpha \in$ V.

Ta sẽ chỉ ra rằng $f^*$ là một đồng cấu từ $W^*$ vào $V^*$. Thật vậy, với mọi vô hướng

a, b $\in \mathbf{K}$ và mọi $\varphi$, $\psi \in W^*$ ta có

$f^*(a\varphi$ + $b\psi)(\alpha) = (a\varphi$ + $b\psi)(f(\alpha))$

$= a\varphi(f(\alpha))$ + $b\psi(f(\alpha))$

$= af^*(\varphi)(\alpha)$ + $bf^*(\psi)(\alpha)$

$= (af^*(\varphi)$ + $bf^*(\psi))(\alpha)$.

Hệ thức này đúng với mọi $\alpha \in$ V, nên ta thu được

$f^*(a\varphi$ + $b\psi) = af^*(\varphi)$ + $bf^*(\psi)$.

Diều này chứng tỏ $f^*$ là một đồng cấu.

### Dịnh nghĩa 4.2 f^*: W^* \to V^* được gọi là đồng cấu (hay ánh xạ) đối ngẫu của

dồng cấu f: V $\to$ W.

Nếu ta ký hiệu giá trị của dạng tuyến tính $\theta \in V^*$ trên vécto $\alpha \in$ V bởi

$\langle \alpha$, $\theta \rangle \in \mathbf{K}$, thì công thức dùng để định nghĩa $f^*$ có thể viết lại thành

$\langle \alpha$, $f^*(\varphi) \rangle = \langle f(\alpha)$, $\varphi \rangle$.

Ý nghĩa của tính đối ngẫu được thấy rõ trong cách diễn đạt này.

Người ta gọi ánh xạ $\langle \cdot$, $\cdot \rangle$ : V $\times V^* \to \mathbf{K}$ là phép ghép cặp đối ngẫu. Đó là một

ánh xạ song tuyến tính, tức là nó tuyến tính với từng biến khi cổ định biến còn lại.

Giả sử V có số chiều bằng n, với một cơ sở là $(\alpha_1$, ..., $\alpha_n)$. Trên cơ sở Định lý

## 2.4, ta định nghĩa các dạng tuyến tính \alpha_1^*,...,\alpha_n^* \in V^* bởi hệ điều kiện sau đây: Giả sử V có số chiều bằng n, với một cơ sở là (\alpha_1, ..., \alpha_n). Trên cơ sở Định lý

$ \langle \alpha_i, \alpha_j^* \rangle = \delta_{ij} = \begin{cases} 1, & \text{m\'eu } i = j, \\ 0, & \text{m\'eu } i \neq j. \end{cases} $



Mệnh đề 4.3 Giả sử $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở của V. Khi đó $(\alpha_1^*$, ..., $\alpha_n^*)$ là một

$\overrightarrow{co} s\overrightarrow{\sigma} c\overrightarrow{u}a V^*$.

Chứng minh: Thật vậy, mỗi $\theta \in V^*$ thừa nhận biểu thị tuyến tính sau đây:

$\theta = \sum_{j=1}^n \langle \alpha_j$, $\theta \rangle \alpha_j^*$.

Để chứng tỏ điều đó ta chỉ cần chứng minh rằng hai về có giá trị như nhau trên

các vécto của cơ sở $(\alpha_1$, ..., $\alpha_n)$. Thật vậy

$\sum_{i=1}^n \langle \alpha_j$, $\theta \rangle \alpha_j^*(\alpha_i) = \sum_{j=1}^n \langle \alpha_j$, $\theta \rangle \delta_{ij}$

$= \langle \alpha_i$, $\theta \rangle = \theta(\alpha_i)$, $\ \$ (1 $\leq$ i $\leq$ n).

Như thế, hệ gồm $nvécto(\alpha_1^*,...,\alpha_n^*)sinh$ ra không gian véctonchiều V. Do đó,

hệ này là một cơ sở của $V^*$.

$\Box$

### Định nghĩa 4.4 Cơ sở (\alpha_1^*, ..., \alpha_n^*) của không gian V^* được gọi là cơ sở đối ngẫu

với cơ sở $(\alpha_1$, ..., $\alpha_n)$ của không gian $V^*$.

Ta có đẳng cấu tuyến tính

V $\rightarrow V^* \alpha = \sum_{i=1}^n a_i \alpha_i \rightarrow \alpha^* = \sum_{i=1}^n a_i \alpha_i^*$.

Đằng cấu này không tự nhiên, vì nó phụ thuộc vào cơ sở $(\alpha_1$, ..., $\alpha_n)$ đã chọn.

Tuy vậy, đẳng cấu V $\to V^{**}$, biến $\alpha$ thành $\alpha^{**}$, trong đó $\alpha^{**}$ được xác định bởi

hệ thức sau

$\langle \varphi$, $\alpha^{**} \rangle = \langle \alpha$, $\varphi \rangle$, $\ \ \forall \varphi \in V^*$,

là một đẳng cấu tự nhiên, vì nó được định nghĩa không phụ thuộc vào cơ sở.

Để chứng minh rằng tương ứng nói trên là một đồng cấu, cần thử lại rằng

$(a\alpha$ + $b\beta)^{**} = a\alpha^{**}$ + $b\beta^{**}$, $\ \ \forall$ a, b $\in \mathbf{K}$, $\ \forall \alpha$, $\beta \in$ V.



Thật vậy, hệ thức trên được chứng minh bằng các đẳng thức sau, trong đó $\varphi$ là

phần tử bất kỳ trong $V^*:$

$\langle \varphi$, $(a\alpha$ + $b\beta)^{**} \rangle = \langle a\alpha$ + $b\beta$, $\varphi \rangle$

$=$ a $\langle \alpha$, $\varphi \rangle$ + b $\langle \beta$, $\varphi \rangle$

$=$ a $\langle \varphi$, $\alpha^{**} \rangle$ + b $\langle \varphi$, $\beta^{**} \rangle$

$= \langle \varphi$, $a\alpha^{**}$ + $b\beta^{**} \rangle$.

Nhận xét rằng dim $V^{**} = \dim V^* = \dim$ V. Vì thế, để chứng minh rằng tương

ứng V $\to V^{**}$ nói trên là một đẳng cấu, ta chỉ cần chứng tỏ nó là một đơn cấu.

Nói rõ hơn, ta chỉ cần chứng minh rằng nếu $\alpha^{**} =$ 0 thì $\alpha =$ 0. Giả sử phản chứng

$\alpha \neq$ 0. Ta chọn một cơ sở $(\alpha_1$, ..., $\alpha_n)$ của V sao cho $\alpha_1 = \alpha$. Khi đó, với $\varphi = \alpha_1^*$,

ta có

1 $= \langle \alpha$, $\alpha_1^* \rangle = \langle \alpha_1^*$, $\alpha^{**} \rangle$.

Dằng thức này chứng tỏ $\alpha^{**} \neq$ 0. Điều vô lý này bác bỏ giả thiết phản chứng.

Nhận xét 4.5 Với mỗi $\alpha \in$ V, phần tử $\alpha^{**} \in V^{**}$ được xác định hoàn toàn và chỉ

phụ thuộc vào $\alpha$. Ngược lại, $\alpha^*$ chỉ được xác định khi đã chọn một cơ sở của V

và $\alpha^*$ phụ thuộc vào cơ sở này. Tuy vậy, ta có thể coi

$\alpha^{**} = (\alpha^*)^*$,

trong đó, đối ngẫu thứ nhất được lấy theo một cơ sở $(\alpha_1$, ..., $\alpha_n)$ nào đó của V,

còn đối ngẫu thứ hai được lấy theo cơ sở đối ngẫu $(\alpha_1^*,...,\alpha_n^*)$ của $V^*$. Mỗi phép

đối ngẫu như thế đều phụ thuộc vào cơ sở đã chọn, nhưng kết quả của hai lần đối

ngẫu liên tiếp thì lại không phụ thuộc bất kỳ cơ sở nào.

Để chứng minh đẳng thức trên ta giả sử

$\alpha = \sum_{i=1}^n a_i \alpha_i$.



Khi đó, $\alpha^* = \sum_{i=1}^n a_i \alpha_i^*$, và $(\alpha^*)^* = \sum_{i=1}^n a_i (\alpha_i^*)^*$. Theo định nghĩa của $\alpha^{**}$, ta có

$\langle \alpha_j^*$, $\alpha^{**} \rangle = \langle \alpha$, $\alpha_j^* \rangle$

$= \langle \sum_{i=1}^n a_i \alpha_i$, $\alpha_j^* \rangle = a_j$.

Giả sử $\alpha^{**}$ có biểu thị tuyến tính

$\alpha^{**} = \sum_{i=1}^n b_i (\alpha_i^*)^*$.

Khi đó ta có

$\langle \alpha_j^*$, $\alpha^{**} \rangle = \langle \alpha_j^*$, $\sum_{i=1}^n b_i (\alpha_i^*)^* \rangle$

$= \sum_{i=1}^n b_i \delta_{ji} = b_j$.

Từ đó suy ra $a_j = b_j$ với j $=$ 1, 2, ..., n. Kết quả là $\alpha^{**} = (\alpha^*)^*$.

$\Box$

Ta cần định nghĩa sau đây trước khi phát biểu định lý chính của tiết này.

### Định nghĩa 4.6 Chuyển vị của ma trận A = (a_{ij}) \in M(m \times n, \mathbf{K}) là ma trận

$A^t = (a^t_{ii}) \in$ M(n $\times$ m, $\mathbf{K})$ được xác định bởi hệ thức

$a_{ji}^t = a_{ij}$ (i $=$ 1, ..., m, j $=$ 1, ..., n).

Nói một cách không hình thức, chuyển vị một ma trận A tức là viết các vécto

hàng của nó thành các vécto cột của ma trận mới At. Khi đó, các vécto cột của A

cũng trở thành các vécto hàng tương ứng của $A^t$.

Một hệ quả trực tiếp của định nghĩa trên là

$(A^t)^t =$ A,

với mọi ma trận A.

Ví dụ:

$ \begin{pmatrix} 1 & 1 & 0 & 3 \\ 1 & 9 & 8 & 4 \\ 2 & 8 & 5 & 4 \end{pmatrix}^t = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 9 & 8 \\ 0 & 8 & 5 \\ 3 & 4 & 4 \end{pmatrix}. $



### Dịnh lý 4.7 Giả sử đồng cấu f: V \rightarrow W có ma trận là A trong cặp cơ sở

$(\alpha_1$, ..., $\alpha_n)$, $(\beta_1$, ..., $\beta_m)$. Khi đó, đồng cấu đối ngẫu $f^*$ : $W^* \to V^*$ có ma trận

là $A^t$ trong cặp cơ sở $(\beta_1^*,...,\beta_m^*)$, $(\alpha_1^*,...,\alpha_n^*)$.

Chứng minh: Vì f có ma trận là A trong cặp cơ sở $(\alpha_1$, ..., $\alpha_n)$, $(\beta_1$, ..., $\beta_m)$, cho

nên

$f(\alpha_j) = \sum_{k=1}^{m} a_{kj} \beta_k$ (j $=$ 1, ..., n).

Theo định nghĩa của ánh xạ đối ngâu, ta có

$\langle \alpha_j$, $f^*(\beta_i^*) \rangle = \langle f(\alpha_j)$, $\beta_i^* \rangle$

$= \langle \sum_{k=1}^m a_{kj} \beta_k$, $\beta_i^* \rangle = a_{ij}$.

Sử dụng công thức được đưa ra trong chứng minh Mệnh đề 4.3 áp dụng cho vécto

$\theta = f^*(\beta_i^*)$, ta thu được

$f^*(\beta_i^*) = \sum_{j=1}^n \langle \alpha_j$, $f^*(\beta_i^*) \rangle \alpha_j^*$

$= \sum_{j=1}^n a_{ij} \alpha_j^*$.

Mặt khác, gọi B $= (b_{ji}) \in$ M(n $\times$ m, $\mathbf{K})$ là ma trận của $f^*$ trong cặp cơ sở

$(\beta_1^*$, ..., $\beta_m^*)$, $(\alpha_1^*$, ..., $\alpha_n^*)$, ta có

$f^*(\beta_i^*) = \sum_{i=1}^n b_{ji} \alpha_j^*$.

Vécto $f^*(\beta_i^*)$ có biểu thị tuyến tính duy nhất qua cơ sở $(\alpha_1^*,...,\alpha_n^*)$, cho nên

$b_{ji} = a_{ij}$, $\quad$ (i $=$ 1, ..., m, j $=$ 1, ..., n).

Diều này có nghĩa là B $= A^t$.

$\Box$

### Định lý sau đây cho thấy các khái niệm đơn cấu và toàn cấu là đối ngẫu với

nhau.

### Dịnh lý 4.8 Gọi f^*: W^* \to V^* là đồng cấu đối ngẫu của đồng cấu f: V \to W.

Khi $d\delta:$



(i) f là một đơn cấu nếu và chỉ nếu $f^*$ là một toàn cấu.

(iii) f là một toàn cấu nếu và chỉ nếu $f^*$ là một đơn cấu.

(iii) f là một đẳng cấu nếu và chỉ nếu $f<sup>*</sup>$ là một đẳng cấu.

Độc giả hãy tự tìm một chứng minh trực tiếp cho định lý này. Trong chương

sau ta sẽ chứng minh rằng rankA $= \text{rank} A^t$, đối với mọi ma trận A. Kết hợp đẳng

thức đó với Định lý 4.7 ta sẽ có một chứng minh gián tiếp cho định lý nói trên.

Bài tập

1. Tính tích của hai ma trận sau đây:

$ \left( \begin{array}{rrrrr} 0 & 4 & 7 & 1 \ 2 & 1 & 7 & 6 \ 1 & 0 & 8 & 3 \ 0 & 1 & 9 & 6 \end{array} \right) \left( \begin{array}{rrrrr} -2 & 8 & -5 & 4 \ 7 & 8 & 5 & 5 \ 0 & 3 & 8 & 4 \ -8 & 9 & -8 & 9 \end{array} \right). $

Tính các lũy thừa sau đây

2.

$ \begin{pmatrix} \cos\varphi & -\sin\varphi \ \sin\varphi & \cos\varphi \end{pmatrix}, \begin{pmatrix} \lambda & 1 \ 0 & \lambda \end{pmatrix}. $

3.

$ \left(\begin{array}{cccc} a_1 & 0 & \dots & 0 \end{array}\right)^{\kappa} $

$ \left.\begin{array}{ccc} 0 & a_2 & ... & 0\ & & \ddots & ... & \ & & & 0 & 0 & ... & a_n \end{array} \right| \;\;. $



4.

$ \left( \begin{array}{cccccc} 1 & 1 & 0 & 0 & ... & 0 & 0 \ 0 & 1 & 1 & 0 & ... & 0 & 0 \ 0 & 0 & 1 & 1 & ... & 0 & 0 \ . & . & . & . & ... & . & . \ 0 & 0 & 0 & 0 & ... & 0 & 1 \ \end{array} \right)^{n-1}. $

5. Cho hai ma trận A và B với các phần tử trong $\bf{K}$. Chứng minh rằng nếu các

tích AB và BA đều có nghĩa và AB $=$ BA, thì A và B là các ma trận vuông

cùng cấp.

6. Ma trận tích AB sẽ thay đổi thế nào nếu ta

(a) đổi chỗ các hàng thứ i và thứ j của ma trận A?

(b) cộng vào hàng thứ i của A tích của vô hướng c với hàng thứ j của A?

(c) đổi chỗ các cột thứ i và thứ j của ma trận B?

(d) cộng vào cột thứ i của B tích của vô hướng c với cột thứ j của B?

7. Vết của một ma trận vuông là tổng của tất cả các phần tử nằm trên đường

chéo chính của ma trận đó. Chứng minh rằng vết của AB bằng vết của BA.

8. Chứng minh rằng nếu A và B là các ma trận vuông cùng cấp, với AB $\neq$ BA,

thì

(a) (A + $B)^2 \neq A^2$ + 2AB + $B^2$,

(b) (A + B)(A - B) $\neq A^2$ - $B^2$.

9. Chứng minh rằng nếu A và B là các ma trận vuông với AB $=$ BA thì

(A + $B)^n = A^n$ + $nA^{n-1}B$ + $\frac{n(n-1)}{2}A^{n-2}B^2$ + $\dots$ + $B^n$.



10. Hai ma trận vuông A và B được gọi là giao hoán với nhau nếu AB $=$ BA.

Chứng minh rằng A giao hoán với mọi ma trận vuông cùng cấp với nó nếu

và chỉ nếu nó là một ma trận vô hướng, tức là A $=$ cE trong đó c $\in \mathbf{K}$ và E

là ma trận đơn vị cùng cấp với A.

11. Ma trận vuông A được gọi là một ma trận chéo nếu các phần tử nằm ngoài

đường chéo chính của nó đều bằng 0. Chứng minh rằng ma trân vuông A

giao hoán với mọi ma trận chéo cùng cấp với nó nếu và chỉ nếu chính A là

một ma trận chéo.

12. Chứng minh rằng nếu A là một ma trận chéo với các phần tử trên đường

chéo chính đôi một khác nhau, thì mọi ma trận giao hoán với A cũng là một

ma trận chéo.

13. Gọi D $= diag(a_1$, $a_2$, ..., $a_n)là$ ma trận chéo với các phần tử trên đường chéo

chính lần lượt bằng $a_1$, $a_2$, ..., $a_n$. Chứng minh rằng nhân Dvới Atừ bên trái

có nghĩa là nhân các hàng của A theo thứ tự với $a_1$, $a_2$, ..., $a_n;$ còn nhân D với

A từ bên phải có nghĩa là nhân các cột của A theo thứ tự với $a_1$, $a_2$, ..., $a_n$.

14. Tìm tất cả các ma trận giao hoán với ma trận sau đây:

$ \left(\begin{array}{ccc} 3 & 1 & 0 \ 0 & 3 & 1 \ 0 & 0 & 3 \end{array}\right). $

$ 15. Chứng minh rằng ma trận A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} thoả mãn phương trình $

$X^2$ - (a+d)X + (ad-bc) $=$ 0.

16. Chứng minh rằng đối với mỗi ma trận vuông A, tồn tại một đa thức khác

không f(X) sao cho f(A) $=$ 0. Hơn nữa, mọi đa thức có tính chất đó đều là



bội của một đa thức $f_0(X)$ như thế, được xác định duy nhất bởi điều kiện:

hệ số của số hạng bậc cao nhất của nó bằng 1. (Đa thức $f_0(X)$ với tính chất

nói trên được gọi là $đ<br/>a$ thức tối thiểu của ma trận A.)

17. Giả sử n không chia hết cho đặc số p của trường K. Chứng minh rằng không

tồn tại các ma trận A, B $\in$ M(n $\times$ n, $\mathbf{K})$ sao cho AB - BA $= E_n$.

18. Giả sử A là một ma trận vuông cấp 2 và k là một số nguyên $\geq$ 2. Chứng

minh rằng $A^k =$ 0 nếu và chỉ nếu $A^2 =$ 0.

19. Tìm tất cả các ma trận vuông cấp hai A sao cho $A^2 =$ 0.

20. Tìm tất cả các ma trận vuông cấp hai A sao cho $A^2 = E_2$.

21. Giải phương trình AX $=$ 0, trong đó A là ma trận vuông cấp hai đã cho còn

X là ma trận vuông cấp hai cần tìm.

22. Tìm ma trận nghịch đảo (nếu có) của ma trận

$ A = \left( \begin{array}{cc} a & b \ c & d \end{array} \right). $

23. Giả sử V $= V_1 \oplus V_2$, trong đó $V_1$ có cơ sở $(\alpha_1$, ..., $\alpha_k)$, $V_2$ có cơ sở $(\alpha_{k+1}$, ..., $\alpha_n)$.

Tìm ma trận của phép chiếu lên $V_1$ theo phương $V_2$ trong cơ sở $(\alpha_1$, ..., $\alpha_n)$.

24. Chứng minh rằng nếu V $= V_1 \oplus V_2$, thì V đẳng cấu với tích trực tiếp $V_1 \times V_2$.

25. Chứng minh rằng tồn tại duy nhất tự đồng cấu f: $\mathbf{R}_3 \to \mathbf{R}_3$ chuyển các

vécto $\alpha_1 =$ (2, 3, 5), $\alpha_2 =$ (0, 1, 2), $\alpha_3 =$ (1, 0, 0) tương ứng thành các vécto

$\beta_1 =$ (1, 1, 1), $\beta_2 =$ (1, 1, -1), $\beta_3 =$ (2, 1, 2). Tìm ma trận của f trong cơ sở

chính tắc của không gian.

26. Tự đồng cấu f của không gian vécto $\mathbf{K}^n$ chuyển các vécto độc lập tuyến tính

$\alpha_1$, ..., $\alpha_n$ tương ứng thành các vécto $\beta_1$, ..., $\beta_n$. Chứng minh rằng ma trận



M(f) của f trong một cơ sở nào đó $(e_1$, ..., $e_n)$ thoả mãn hệ thức M(f) $=$

$BA^{-1}$, trong đó các cột của ma trận A và ma trận B là toạ độ tương ứng của

các véctor $\alpha_1$, ..., $\alpha_n$ và $\beta_1$, ..., $\beta_n$ trong co sở $(e_1$, ..., $e_n)$.

$ 27. Chứng minh rằng phép nhân với ma trận A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} (a) từ bên trái, (b) $

từ bên phải là các tự đồng cấu của không gian các ma trận vuông cấp hai.

Hãy tìm ma trận của tự đồng cấu đó trong cơ sở gồm các ma trận sau đây:

$ \left(\begin{array}{cc} 1 & 0 \\ 0 & 0 \end{array}\right), \left(\begin{array}{cc} 0 & 1 \\ 0 & 0 \end{array}\right), \left(\begin{array}{cc} 0 & 0 \\ 1 & 0 \end{array}\right), \left(\begin{array}{cc} 0 & 0 \\ 0 & 1 \end{array}\right). $

28. Chứng minh rằng đạo hàm là một tự đồng cấu của không gian vécto các đa

thức hệ số thực có bậc không vượt quá n. Tìm ma trận của tự đồng cấu đó

trong các cơ sở sau đây:

(a) (1, X, ..., $X^n)$,

(b) (1, (X - c), ..., $\frac{(X$ - $c)^n}{n!})$, trong đó c là một hằng số thực.

29. Ma trận của một tự đồng cấu trong cơ sở $(e_1$, ..., $e_n)$ thay đổi thế nào nếu ta

đổi chỗ các vécto $e_i$ và $e_j?$

30. Tự đồng cấu f có ma trận

$ \begin{pmatrix} 1 & 2 & 0 & 1 \\ 3 & 0 & -1 & 2 \\ 2 & 5 & 3 & 1 \\ 1 & 2 & 1 & 3 \end{pmatrix} $

trong cơ sở $(e_1$, $e_2$, $e_3$, $e_4)$. Hãy tìm ma trận của f trong cơ sở $(e_1$, $e_1$ + $e_2$, $e_1$ +

$e_2$ + $e_3$, $e_1$ + $e_2$ + $e_3$ + $e_4$.



31. Tự đồng cấu $\varphi$ có ma trận

$ \begin{pmatrix} 15 & -11 & 5 \\ 20 & -15 & 8 \\ 8 & -7 & 6 \end{pmatrix} $

trong cơ sở $(e_1$, $e_2$, $e_3)$. Hãy tìm ma trận của $\varphi$ trong cơ sở gồm các vécto

$\epsilon_1 = 2e_1$ + $3e_2$ + $e_3$, $\epsilon_2 = 3e_1$ + $4e_2$ + $e_3$, $\epsilon_3 = e_1$ + $2e_2$ + $2e_3$.

32. Đồng cấu $\varphi$ : $\mathbf{C}_3 \to \mathbf{C}_3$ có ma trận

$ \begin{pmatrix} 1 & -18 & 15 \\ -1 & -22 & 20 \end{pmatrix} $

1 -25 22

trong cơ sở gồm các vécto $\alpha_1 =$ (8, -6, 7), $\alpha_2 =$ (-16, 7, -13), $\alpha_3 =$ (9, -3, 7).

Tìm ma trận của $\varphi$ trong cơ sở gồm các vécto

$\beta_1 =$ (1, -2, 1), $\ \beta_2 =$ (3, -1, 2), $\ \beta_3 =$ (2, 1, 2).

Chứng minh rằng các ma trận của một tự đồng cấu trong hai cơ sở của không

33.

gian là trùng nhau nếu và chỉ nếu ma trận chuyển giữa hai cơ sở đó giao hoán

với ma trận của đồng cấu đã cho trong mỗi cơ sở nói trên.

$ 34. Tự đồng cấu \varphi \in End(\mathbf{R}_2) có ma trận \begin{pmatrix} 3 & 5 \\ 4 & 3 \end{pmatrix} trong cơ sở gồm \alpha_1 = $

$ (1,2), \alpha_2 = (2,3), và tự đồng cấu \psi \in End(\mathbf{R}_2) có ma trận \begin{pmatrix} 4 & 6 \\ 6 & 9 \end{pmatrix} trong $

cơ sở gồm $\beta_1 =$ (3, 1), $\beta_2 =$ (4, 2). Tìm ma trận của $\varphi$ + $\psi$ trong cơ sở $(\beta_1$, $\beta_2)$.

$ 35. Tự đồng cấu \varphi \in End(\mathbf{R}_2) có ma trận \begin{pmatrix} 2 & -1 \\ 5 & -3 \end{pmatrix} trong cơ sở gồm \alpha_1 = $

$ (-3, 7), \alpha_2 = (1, -2), và tự đồng cấu \psi \in End(\mathbf{R}_2) có ma trận \begin{pmatrix} 1 & 3 \\ 2 & 7 \end{pmatrix} $



trong cơ sở gồm $\beta_1 =$ (6, -7), $\beta_2 =$ (-5, 6). Tìm ma trận của $\varphi \psi$ trong cơ sở

chính tắc của $\mathbf{R}_2$.

36. Giả sử tự đồng cấu $\varphi$ : V $\to$ V thoả mãn hệ thức $\varphi^2 = \varphi$. Chứng minh rằng

V $= Im(\varphi) \oplus Ker(\varphi)$.

37. Cho các tự đồng cấu $\varphi$, $\psi \in$ End(V).

(a) Phải chăng nếu $\varphi \psi =$ 0 thì $\psi \varphi =$ 0?

(b) Phải chăng nếu $\varphi \psi =$ 0 và $\psi \varphi =$ 0 thì hoặc $\varphi =$ 0 hoặc $\psi =$ 0?

38. Giả sử $\varphi$ và $\psi$ là các tự đồng cấu của không gian vécto hữu hạn chiều V.

Chứng minh rằng $\varphi\psi$ là một đẳng cấu nếu và chỉ nếu $\varphi$ và $\psi$ là các đẳng

cấu. Khi đó

$(\varphi \psi)^{-1} = \psi^{-1} \varphi^{-1}$.

39. Ký hiệu vết của ma trận vuông A là Tr(A). Chứng minh rằng ánh xạ Tr:

M(n $\times$ n, $\mathbf{K}) \to \mathbf{K}$, A $\mapsto$ Tr(A) là một đồng cấu. Tìm một cơ sở của hạt

nhân của Tr.

40. Chứng minh rằng vết của hai ma trận đồng dạng bằng nhau. (Từ đó người

ta định nghĩa vết của một tự đồng cấu là vết của ma trận của nó trong cơ sở

bất kỳ của không gian.)

41. Chứng minh rằng nếu tích ma trận AB có nghĩa thì

$(AB)^t = B^t A^t$.

Từ đó suy ra rằng ma trận vuông A khả nghịch nếu và chỉ nếu At khả nghịch,

và khi đó

$(A^t)^{-1} = (A^{-1})^t$.



42. Cho các đồng $cấuf:V\to$ Wvà $g:W\to$ Z.Chứng minh mối liên hệ giữa

các đồng cấu đối ngẫu:

$(gf)^* = f^*g^*$.

Từ đó suy ra rằng đồng $cấuf:V\to$ Wkhả nghịch nếu và chỉ $nếuf^*:W^*\to$

$V^*khả$ nghịch, và khi đó

$(f^*)^{-1} = (f^{-1})^*$.

43. Chứng minh rằng ánh xạ $\mathcal{L}(V$, W) $\to \mathcal{L}(W^*$, $V^*)$, f $\mapsto f^*$ là một đẳng cấu

tuyến tính.

110



# Chương III

DỊNH THỨC VÀ HỆ PHƯƠNG TRÌNH

TUYẾN TÍNH

Định thức là một công cụ hữu hiệu để giải các hệ phương trình tuyến tính, và góp

phần giải quyết hầu hết các bài toán định lượng cũng như định tính trong Đại số

tuyến tính.

Các phép thể

### Định nghĩa 1.1 Mỗi song ánh từ tập \{1, 2, ..., n\} vào chính nó được gọi là một

phép thể bậc n. Tập hợp tất cả các phép thể bậc n được ký hiệu bởi $S_n$.

$S_n$ cùng với phép hợp thành các ánh xạ lập thành một nhóm, được gọi là nhóm

đối xứng bậc n. Nhóm này có n! phần tử.

Nếu $\sigma \in S_n$, ta thường biểu thị nó dưới dạng

$ \sigma = \left( \begin{array}{cccc} 1 & 2 & \ldots & n \\ \sigma(1) & \sigma(2) & \ldots & \sigma(n) \end{array} \right). $

Giả sử $x_1$, $x_2$, ..., $x_k$ là các phần tử đôi một khác nhau trong tập hợp $\{1$, 2, ..., $n\}$.

Ta ký hiệu bởi $(x_1$, $x_2$, ..., $x_k)$ phép thế giữ nguyên các phần tử khác $x_1$, $x_2$, ..., $x_k$,

và tác động trên các phần tử đó như sau:

$x_1 \mapsto x_2$, $x_2 \mapsto x_3$, ..., $x_{k-1} \mapsto x_k$, $x_k \mapsto x_1$.

Nó được gọi là một xích độ dài k trên tập nền $\{x_1$, $x_2$, ..., $x_k\}$. Xích $(x_1$, $x_2$, ..., $x_k)$

được gọi là một xích của phép thế $\sigma$ nếu $\sigma$ tác động như $(x_1$, $x_2$, ..., $x_k)$ trên các

phần tử $x_1$, $x_2$, ..., $x_k$. (Tuy nhiên, $\sigma$ có thể tác động không tầm thường trên các

phần tử khác $x_1$, $x_2$, ..., $x_k$.



Mệnh đề 1.2 Mọi phép thế $\sigma \in S_n$ đều là tích của tất cả các xích khác nhau của

nó. Các tập nền của các xích này là các tập con rời nhau của $\{1$, 2, ..., $n\}$.

Chứng minh: Với mọi $x_1 \in \{1$, 2, ..., $n\}$, nếu $\sigma(x_1) = x_1$ thì $(x_1)$ là một xích của $\sigma$.

Trái lại, nếu $\sigma(x_1) \neq x_1$, ta đặt $x_2 = \sigma(x_1)$. Giả sử $x_1$, $x_2 = \sigma(x_1)$, ..., $x_k = \sigma(x_{k-1})$

là những phần tử đôi một khác nhau, còn $\sigma(x_k)$ trùng với một trong các phần tử

$x_1$, $x_2$, ..., $x_k$. Ta khẳng định rằng $\sigma(x_k) = x_1$. Thật vậy, nếu $\sigma(x_k) = x_i$ với i $>$ 1,

thì $\sigma(x_k) = \sigma(x_{i-1})$. Do đó $x_{i-1} = x_k$. Điều này mâu thuẫn với giả thiết rằng

$x_1$, $x_2$, ..., $x_k$ đôi một khác nhau. Như thế $(x_1$, $x_2$, ..., $x_k)$ là một xích của $\sigma$.

Môi phần tử của tập $\{1$, 2, ..., $n\}$ đều thuộc một tập con, là tập nền của một

xích nào đó của $\sigma$. Hai tập con như thế nếu có một phần tử chung thì phải trùng

nhau. Thật vậy, phương trình $\sigma(x) =$ y hoàn toàn xác định y theo x và x theo y

$(\text{do } \sigma \text{$ là một song $ánh})$.

$\Box$

### Định nghĩa 1.3 Phép đổi chỗ hai phần tử khác nhau i,j \in \{1,2,...,n\}và giữ

nguyên các phần tử khác được gọi là một phép thế sơ cấp.

Nói cách khác, một phép thể sơ cấp là một xích độ dài bằng hai: (i, j).

Mệnh đề 1.4 Mỗi phép thế cấp n đều là tích của một số phép thế sơ cấp. (Nói

khác đi, các phép thế sơ cấp sinh ra nhóm $S_n.)$

Chứng minh: Áp dụng Mệnh đề 1.2, ta chỉ cần chứng minh mệnh đề này cho các

xích. Ta dễ kiểm tra lại rằng

$(x_1$, $x_2$, ..., $x_k) = (x_1$, $x_2$, ..., $x_{k-1})(x_{k-1}$, $x_k) = \cdots$

$= (x_1$, $x_2)(x_2$, $x_3) \cdots (x_{k-1}$, $x_k)$.

Trong đó, phép thể ở bên phải tác động trước.

$\Box$

### Định nghĩa 1.5 Dấu của phép thế \sigma \in S_n là số sau đây

$sgn(\sigma) = \prod_{i \neq j} \frac{\sigma(i)$ - $\sigma(j)}{i$ - $j} \in \{\pm 1\}$.

Tích này chạy trên mọi cặp số (không có thứ tự) $\{i$, $j\} \subset \{1$, 2, ..., $n\}$.



Ta gọi cặp số $\{i$, $j\} \subset \{1$, 2, ..., $n\}$ là một nghịch thể của $\sigma$ nếu $\sigma(i)$ - $\sigma(j)$ trái

dấu với i - j, tức là nếu $\frac{\sigma(i)$ - $\sigma(j)}{i$ - $j} <$ 0. Như vậy, $sgn(\sigma)$ bằng +1 hay -1 tuỳ theo

số nghịch thế của $\sigma$ là chẵn hay lẻ.

$ Ví dụ: \sigma = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 3 & 4 & 1 \end{pmatrix} có ba nghịch thế là {1,4}, {2,4} và {3,4}, cho nên $

$sgn(\sigma) =$ -1.

### Định nghĩa 1.6 \sigma được gọi là một phép thể chẵn nếu sgn(\sigma) = 1, nó được gọi là

một phép thể lẻ nếu $sgn(\sigma) =$ -1.

Mệnh đề 1.7 Mỗi phép thế sơ cấp đều là một phép thế lẻ.

Chứng minh: Giả sử i $<$ j và

$ \tau = \left( \begin{array}{cccccc} 1 & 2 & \ldots & i & \ldots & j & \ldots & n \ 1 & 2 & \ldots & j & \ldots & i & \ldots & n \end{array} \right). $

Khi đó, tất cả các nghịch thế của $\tau$ là

$\{i,k\}$ với mọi k mà i $<$ k $\leq$ j

$\{\ell$, $j\}$ với mọi $\ell$ mà i $< \ell <$ j.

Vậy $\tau$ có tất cả (j - i) + (j - i - 1) $=$ 2(j - i) - 1 nghịch thế, do đó $\tau$ là một phép

thế lẻ.

$\Box$

Dinh lý 1.8

$sgn(\lambda\mu) = sgn(\lambda)sgn(\mu)$,

với mọi $\lambda$, $\mu \in S_n$.

Chứng minh: Vì $\mu$ là một song ánh, cho nên khi $\{i$, $j\}$ chạy một lần qua mọi cặp

(không có thứ tự) trong $\{1$, 2, ..., $n\}$ thì $\{\mu(i)$, $\mu(j)\}$ cũng chạy một lần qua mọi cặp

như thể. Do đó

$sgn(\lambda) = \prod_{i \neq j} \frac{\lambda(i)$ - $\lambda(j)}{i$ - $j} = \prod_{i \neq j} \frac{\lambda(\mu(i))$ - $\lambda(\mu(j))}{\mu(i)$ - $\mu(j)}$.



Ta có

$sgn(\lambda\mu) = \prod_{i \neq j} \frac{\lambda(\mu(i))$ - $\lambda(\mu(j))}{i$ - $j}$

$= \prod_{i \neq i} \frac{\lambda(\mu(i))$ - $\lambda(\mu(j))}{\mu(i)$ - $\mu(j)} \prod_{i \neq i} \frac{\mu(i)$ - $\mu(j)}{i$ - $j} = \text{sgn}(\lambda)\text{sgn}(\mu)$. $\Box$

Hệ quả 1.9 Một phép thể là chẵn hay lẻ tuỳ theo nó là tích của một số chẵn hay

le các phép thế sơ cấp.

Nhận xét: Có nhiều cách viết một phép thể thành tích các phép thể sơ cấp, chẳng

hạn (i, j) $=$ (i, $j)^3$. Nhưng tính chẵn lẻ của số nhân tử trong tích là không thay đổi.

Dinh thức của ma trận

$\bf{2}$

Cho một ma trận vuông A $= (a_{ij})_{n \times n}$ với các phần tử trong trường K.

### Định nghĩa 2.1 Dinh thức của ma trận A, được ký hiệu bởi det A hoặc |A|, là

phần tử sau đây của trường K

det A $=$ |A| $= \sum_{\sigma \in S_n} sgn(\sigma) a_{\sigma(1)1} \cdots a_{\sigma(n)n}$.

Nếu A là một ma trận vuông cấp n thì det A được gọi là một định thức cấp n.

Tổng ở vế phải của đẳng thức trên có tất cả $|S_n| =$ n! số hạng.

Ví dụ: (a) Định thức cấp 1:

$\det(a) =$ a, $\qquad \forall$ a $\in \mathbf{K}$.

(b) Dinh thức cấp 2:

$ det \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = a_{11}a_{22} - a_{21}a_{12}. $



(c) Dinh thức cấp 3:

$ det \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} = a_{11}a_{22}a_{33} + a_{21}a_{32}a_{13} + a_{31}a_{12}a_{23}-a_{11}a_{32}a_{23} - a_{21}a_{12}a_{33} - a_{31}a_{22}a_{13}. $

Trên thực tế người ta không trực tiếp dùng định nghĩa để tính các định thức

cấp n $>$ 3, vì việc này quá phức tạp. Dưới đây, chúng ta sẽ tìm hiểu những tính

chất cơ bản của định thức. Từ đó, ta sẽ nhận được những phương pháp tính định

thức hiệu quả và tiết kiệm sức lao động hơn so với cách trực tiếp dùng định nghĩa.

Gọi $\alpha_j \in \mathbf{K}^n$ là vécto cột thứ j của ma trận A, và coi det A là một hàm của các

vécto $\alpha_1$, ..., $\alpha_n$. Ta viết

$\det$ A $= \det(\alpha_1$, ..., $\alpha_n)$.

Dịnh thức có 3 tính chất cơ bản dưới đây.

Tính chất 1 (Đa tuyến tính): Định thức của ma trận là một hàm tuyến tính

với mỗi cột của nó, khi cố định các cột khác. Tức là:

$\det(\alpha_1$, ..., $\alpha_{j}$ + $b\beta_j$, ..., $\alpha_n) =$ a $\det(\alpha_1$, ..., $\alpha_j$, ..., $\alpha_n)$ + b $\det(\alpha_1$, ..., $\beta_j$, ..., $\alpha_n)$,

với mọi a, b $\in \mathbf{K}$, $\alpha_1$, ..., $\alpha_j$, $\beta_j$, ..., $\alpha_n \in \mathbf{K}^n$, j $=$ 1, ..., n.

Chứng minh: Ký hiệu

$ \alpha_j=\left(\begin{array}{c} a_{1j}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $

Ta có

$\det(\alpha_1$, ..., $\alpha_{j}$ + $b\beta_j$, ..., $\alpha_n) = \sum \text{sgn}(\sigma)a_{\sigma(1)1} \cdots$ (a $a_{\sigma(j)j}$ + b $b_{\sigma(j)j}) \cdots a_{\sigma(n)n}$

$\sigma \in S_n$

$=$ a $\sum \text{sgn}(\sigma) a_{\sigma(1)1} \cdots a_{\sigma(j)j} \cdots a_{\sigma(n)n}$

$\sigma \in S_n$

+b $\sum sgn(\sigma)a_{\sigma(1)1} \cdots b_{\sigma(j)j} \cdots a_{\sigma(n)n}$

$\sigma \in S_n$

$=$ a $\det(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_n)$ + b $\det(\alpha_1$, ..., $\beta_i$, ..., $\alpha_n)$. $\Box$



Tính chất 2 (Thay phiên): Nếu ma trận vuông A có hai cột bằng nhau, thì

$\det$ A $=$ 0.

Chứng minh: Giả sử $\alpha_i = \alpha_j$ với i $<$ j, tức là $a_{ki} = a_{kj}$ (1 $\leq$ k $\leq$ n. Theo định

nghĩa

det A $= \sum sgn(\sigma) a_{\sigma(1)1} \cdots a_{\sigma(i)i} \cdots a_{\sigma(j)j} \cdots a_{\sigma(n)n}$.

$\sigma \in S_n$

Ta ghép các số hạng trong tổng thành từng cặp

$sgn(\sigma)a_{\sigma(1)1}\cdots a_{\sigma(i)i}\cdots a_{\sigma(j)j}\cdots a_{\sigma(n)n}$

$\text{sgn}(\sigma') a_{\sigma(1)1} \cdots a_{\sigma(j)i} \cdots a_{\sigma(i)j} \cdots a_{\sigma(n)n}$,

với

trong đó $\sigma' = \tau \sigma$, ở đây $\tau$ là phép thế sơ cấp đổi chỗ $\sigma(i)$ và $\sigma(j)$. Hiển nhiên ta

$\overline{c}$

$sgn(\sigma') = -sgn(\sigma)$,

$a_{\sigma(1)1}\cdots a_{\sigma(i)i}\cdots a_{\sigma(j)j}\cdots a_{\sigma(n)n} = a_{\sigma(1)1}\cdots a_{\sigma(j)i}\cdots a_{\sigma(i)j}\cdots a_{\sigma(n)n}$.

Như thế det A là một tổng có các cặp số hạng đối nhau. Vậy det A $=$ 0.

$\Box$

Tính chất 3 (Chuẩn hoá): Định thức của ma trận đơn vị bằng 1:

$ det E_n = \det \begin{pmatrix} 1 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \cdot & \cdot & \dots & \cdot \\ 0 & 0 & \dots & 1 \end{pmatrix} = 1. $

Chứng minh: Ký hiệu $e_{ij}chỉ$ phần tử nằm ở hàng icột j của $E_n$. Ta có

$ e_{ij} = \begin{cases} 1 & \text{néu } i = j, \\ 0 & \text{néu } i \neq j. \end{cases} $

Theo định nghĩa

det $E_n = \sum_{\sigma \in S_n} \text{sgn}(\sigma) e_{\sigma(1)1} \cdots e_{\sigma(n)n}$.



Tống này chỉ có đúng một số hang khác không, ứng với phép thể đồng nhất

$\sigma(1) =$ 1, ..., $\sigma(n) =$ n. Dấu của phép thế này bằng 1. Như vậy

$\det E_n =$ 1 $\cdot$ 1 $\cdots$ 1 $=$ 1.

Nhận xét 2.2 Trong tiết sau ta sẽ chứng tỏ rằng định thức là hàm duy nhất trên

các ma trận vuông có 3 tính chất nói trên.

(i) (Tính phản đối xứng của định thức). Nếu đổi chỗ hai cột của

Hệ quả 2.3

$m\hat{o}t$ ma trần thì định thức của nó đối dấu:

$det(...,\alpha_i,...,\alpha_j,...) = -\det(...,\alpha_j,...,\alpha_i,...)$.

(ii) Nếu các véctơ cột của một ma trận phụ thuộc tuyến tính thì định thức của

ma trận bằng không. Nói riêng, nếu ma trận có một cột bằng 0 thì định thức

$c\dot{u}a$ nó bằng 0.

(iii) Nếu thêm vào một cột của ma trận một tổ hợp tuyến tính của các cột khác

thì định thức của nó không thay đổi.

Chứng minh: (i) Theo các tính chất cơ bản của định thức, ta có

0 $= \det($ ..., $\alpha_i$ + $\alpha_j$, ..., $\alpha_i$ + $\alpha_j$, ... )

$= det(...,\alpha_i,...,\alpha_i,...)$ + $det(...,\alpha_i,...,\alpha_i,...)$

$+\det(...,\alpha_i,...,\alpha_i,...)+\det(...,\alpha_i,...,\alpha_i,...)$.

Hai định thức đầu tiên của vế phải bằng 0, do tính thay phiên của định thức. Từ

dó ta thu dược

$det(...,\alpha_i,...,\alpha_j,...) = -\det(...,\alpha_j,...,\alpha_i,...)$.

(ii) Giả sử cột j của ma trận A là một tổ hợp tuyến tính của các cột còn lại:

$\alpha_j = \sum_{i \neq j} a_i \alpha_i$.



Theo tính chất đa tuyến tính của định thức, ta có

det A $= \sum_{i \neq j} a_i \det($ ..., $\alpha_i$, ..., $\alpha_i$, ...).

Mỗi định thức ở vế phải đều có hai cột bằng nhau, vì thế det A $=$ 0.

(iii) Theo phần (ii) ta có

$\det(\alpha_1$, ..., $\alpha_i$ + $\sum_{i \neq i} a_i \alpha_i$, ..., $\alpha_n)$

$=\det(\alpha_1,...,\alpha_i,...,\alpha_n)$ + $\det(\alpha_1,...,\sum_{i\neq i}a_i\alpha_i,...,\alpha_n)$

$=\det(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_n)$ + 0

$=\det(\alpha_1,...,\alpha_i,...,\alpha_n)$.

$\Box$

Trong §5 ta sẽ chứng minh rằng các tính chất của định thức đối với các hàng

cũng tương tự các tính chất của định thức đối với các cột, như đã nói trong hệ quả

trên. Một phương pháp tính định thức có hiệu quả là ứng dụng những tích chất

đó để biến đổi ma trận thành một ma trận tam giác có cùng định thức. Chúng ta

sẽ tính định thức của ma trận tam giác trong ví dụ sau đây.

Ví dụ: Ma trận A được gọi là một ma trận tam giác trên nếu nó có dạng

$ A = \left( \begin{array}{cccc} a_{11} & a_{12} & \ldots & a_{1n} \ & 0 & a_{22} & \ldots & a_{2n} \ & & \ddots & \ldots & \ldots \ & & & 0 & 0 & \ldots & a_{nn} \ \end{array} \right), $

trong đó $a_{ij} =$ 0 với i $>$ j. Tương tự, A được gọi là một ma trận tam giác duới

nếu $a_{ij} =$ 0 với i $<$ j. Ma trận tam giác trên và ma trận tam giác dưới được gọi

chung là ma trận tam giác.

Chứng minh rằng, nếu A là một ma trận tam giác cấp n thì

$\det$ A $= a_{11}a_{22}\cdots a_{nn}$.

Ta sẽ chỉ xét trường hợp A là một ma trận tam giác trên. Đối với ma

Lò i giai:

trận tam giác dưới, chứng minh hoàn toàn tương tự. Theo định nghĩa định thức,



ta có

det A $= \sum sgn(\sigma) a_{\sigma(1)1} \cdots a_{\sigma(n)n}$.

$\sigma \in S_n$

Vì A là một ma trận tam giác trên, nên điều kiện để $a_{\sigma(1)1}$ có thể khác không là

$\sigma(1) \leq$ 1, do đó $\sigma(1) =$ 1. Giả sử quy nạp rằng điều kiện để $a_{\sigma(1)1} \cdots a_{\sigma(i-1)i-1}$ có

thể khác không là $\sigma(1) =$ 1, ..., $\sigma(i-1) =$ i-1. Khi đó, $a_{\sigma(1)1} \cdots a_{\sigma(i)i}$ chỉ có thể

khác không nếu $\sigma(1) =$ 1, ..., $\sigma(i-1) =$ i-1 và $\sigma(i) \leq$ i. Vì $\sigma$ là một song ánh,

nên điều kiện nói trên kéo theo $\sigma(i) =$ i. Như thế, số hạng duy nhất có khả năng

khác không trong det A là số hạng ứng với phép thể đồng nhất

$\sigma(1) =$ 1, $\sigma(2) =$ 2, ..., $\sigma(n) =$ n.

Hiển nhiên, dấu của phép thế đó bằng 1 (vì nó không có nghịch thế nào cả). Từ

đó suy ra

det A $= a_{11}a_{22}\cdots a_{nn}$.

Anh xạ đa tuyến tính thay phiên

$3\phantom{.}$

### Định nghĩa 3.1 Giả sử V và W là các không gian vécto trên trường K. Ánh xạ

$\varphi: \underbrace{V \times \cdots \times V}_{k} \to$ W

được gọi là đa tuyến tính (hay nói rõ hơn: k-tuyến tính) nếu nó tuyến tính với từng

thành phần trong tích V $\times \cdots \times$ V khi cố định các thành phần còn lại, tức là nếu

$\varphi(\alpha_1$, ..., $\alpha_{i}$ + $b\beta_i$, ..., $\alpha_k) = a\varphi(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_k)$ + $b\varphi(\alpha_1$, ..., $\beta_i$, ..., $\alpha_k)$,

với mọi a, b $\in \mathbf{K}$, $\alpha_1$, ..., $\alpha_k$, $\beta_i \in$ V và với mọi i $=$ 1, ..., k.

Nếu W $= \mathbf{K}$ thì $\varphi$ được gọi là một dạng k-tuyến tính trên V.

Ví dụ: Giả sử $\varphi_1$, ..., $\varphi_k$ : V $\to \mathbf{K}$ là các ánh xạ tuyến tính. Khi đó

$\varphi:$ V $\times \cdots \times$ V $\rightarrow \mathbf{K}$

k lần

$\varphi(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_k) = \varphi_1(\alpha_1) \cdots \varphi_k(\alpha_k)$



là một dạng k-tuyến tính trên V.

### Định nghĩa 3.2 Ánh xạ k-tuyến tính \varphi: V \times \cdots \times V \rightarrow W được gọi là thay phiên

nếu

$\varphi(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_j$, ..., $\alpha_k) =$ 0,

khi $\alpha_i = \alpha_j$, với cặp chỉ số i $\neq$ j nào đó.

Ví dụ:

(a) Ánh xạ đồng nhất không 0: V $\times \cdots \times$ V $\to$ W là k-tuyến tính và thay phiên.

Định thức det : $\mathbf{K}^n \times \cdots \times \mathbf{K}^n \to \mathbf{K}$ là một hàm n-tuyến tính và thay phiên.

(b)

Mệnh đề 3.3 Giả sử $\varphi$ là một ánh xạ k-tuyến tính thay phiên. Khi đó

(i) $\varphi$ có tính phản đối xứng, tức là

$\varphi(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_j$, ..., $\alpha_k) = -\varphi(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_i$, ..., $\alpha_k)$,

với moi $\alpha_1$, ..., $\alpha_k \in$ V và moi căp chỉ số i $\neq$ j.

(ii) Nếu hệ $\alpha_1$, ..., $\alpha_k$ phụ thuộc tuyến tính thì

$\varphi(\alpha_1$, ..., $\alpha_k) =$ 0.

Chứng minh: Mệnh đề được chứng minh bằng cách lặp lại các lập luận trong

chứng minh Hệ quả 2.3.

$\Box$

Nhận xét 3.4 Nếu Char(K) $\neq$ 2 thì một ánh xạ đa tuyến tính $\varphi:$ V $\times \cdots \times$ V $\to$ W

là thay phiên khi và chỉ khi nó phản đối xứng. Thật vậy, theo mệnh đề trên, tính

phản đối xứng là hệ quả của tính thay phiên. Ngược lại, giả sử $\varphi$ phản đối xứng,

tức là

$\varphi(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_j$, ..., $\alpha_k) = -\varphi(\alpha_1$, ..., $\alpha_j$, ..., $\alpha_i$, ..., $\alpha_k)$,



với mọi $\alpha_1$, ..., $\alpha_k \in$ V và mọi cặp chỉ số i $\neq$ j. Lấy $\alpha_i = \alpha_j$, ta có

$\varphi(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_i$, ..., $\alpha_k) = -\varphi(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_i$, ..., $\alpha_k)$.

Từ đó $2\varphi(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_i$, ..., $\alpha_k) =$ 0. Vì Char(K) $\neq$ 2 cho nên đẳng thức trên kéo

theo

$\varphi(\alpha_1$, ..., $\alpha_i$, ..., $\alpha_i$, ..., $\alpha_k) =$ 0.

Diều này có nghĩa là $\varphi$ có tính thay phiên.

Nếu $Char(\mathbf{K}) =$ 2 thì tính thay phiên mạnh hơn tính phản đối xứng.

Khái niệm định thức như một hàm đa tuyến tính thay phiên của các vécto cột

của một ma trận vuông được tổng quát hoá như sau.

Giả sử dim V $=$ n và $\varepsilon = (\varepsilon_1$, ..., $\varepsilon_n)$ là một cơ sở của V. Giả sử $\alpha_j = \sum_{i=1}^n a_{ij} \varepsilon_i$,

nói các khác

$(\alpha_1...\alpha_n)=(\varepsilon_1...\varepsilon_n)A$,

trong đó $A=(a_{ij})_{n\times n}$.

Dinh nghĩa 3.5 Ta gọi det A là định thức của hệ vécto $\alpha_1$, ..., $\alpha_n$ trong co sở $\varepsilon$

(hay đối với cơ sở $\varepsilon)$, và ký hiệu là $\det_{\varepsilon}(\alpha_1$, ..., $\alpha_n)$.

Như vậy

$\det_{\varepsilon}(\alpha_1$, ..., $\alpha_n) = \det$ A $= \sum \text{sgn}(\sigma) a_{\sigma(1)1} \cdots a_{\sigma(n)n}$,

$\sigma \in S_n$

trong đó $\alpha_i = \sum_{i=1}^n a_{ij} \varepsilon_i$.

Theo $\S2$ thì $det<sub>\varepsilon</sub>$ là một dạng n-tuyến tính thay phiên trên V.

Ký hiệu bởi $\Lambda^n(V)^*$ tập hợp tất cả các dạng n-tuyến tính thay phiên trên V.

Nó lập nên một không gian vécto trên K đối với phép cộng ánh xạ và nhân ánh xạ

với vô hướng được định nghĩa như sau:

$(\varphi$ + $\psi)(\alpha_1$, ..., $\alpha_n) = \varphi(\alpha_1$, ..., $\alpha_n)$ + $\psi(\alpha_1$, ..., $\alpha_n)$,

$(a\varphi)(\alpha_1$, ..., $\alpha_n) = a\varphi(\alpha_1$, ..., $\alpha_n)$,

với moi $\varphi$, $\psi \in \Lambda^n(V)^*$, a $\in \mathbf{K}$.



Dinh lý 3.6 Nếu dim V $=$ n thì dim $\Lambda^n(V)^* =$ 1. Hơn nữa, nếu $\varepsilon = (\varepsilon_1$, ..., $\varepsilon_n)$ là

một cơ sở của V, thì $(\det_{\varepsilon})$ là một cơ sở của $\Lambda^{n}(V)^{*}$.

Chứng minh: Ta đã biết $det<sub>\varepsilon \in \Lambda^n(V)^*$. Giả sử $\varphi \in \Lambda^n(V)^*$. Với mọi $\alpha_j =</sub>$

$\sum_{i=1}^{n} a_{ij} \varepsilon_i$ (j $=$ 1, ..., n), ta có

$\varphi(\alpha_1$, ..., $\alpha_n) = \varphi(\sum_{i_1}^n a_{i_1 1} \varepsilon_{i_1}$, ..., $\sum_{i_n}^n a_{i_n n} \varepsilon_{i_n})$

$= \sum a_{i_1 1} \cdots a_{i_n n} \varphi(\varepsilon_{i_1}$, ..., $\varepsilon_{i_n})$.

$i_1,...,i_n$

Nếu có hai trong các chỉ số $i_1$, ..., $i_n$ bằng nhau, thì số hạng tương ứng bằng 0, do

$\varphi$ có tính thay phiên. Vì vậy, tổng chỉ cần lấy trên các bộ chỉ số $i_1$, ..., $i_n$ đôi một

khác nhau. Khi đó, mỗi bộ chỉ số $i_1$, ..., $i_n$ xác định một phép thế $\sigma \in S_n$ bởi công

thức

$\sigma(1) = i_1$, $\sigma(2) = i_2$, ..., $\sigma(n) = i_n$.

Do $\varphi$ có tính phản đối xứng, nên

$\varphi(\varepsilon_{i_1},...,\varepsilon_{i_n})=\varphi(\varepsilon_{\sigma(1)},...,\varepsilon_{\sigma(n)})=\text{sgn}(\sigma)\varphi(\varepsilon_1,...,\varepsilon_n)$.

Từ đó

$\varphi(\alpha_1$, ..., $\alpha_n) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) a_{\sigma(1)1} \cdots a_{\sigma(n)n} \varphi(\varepsilon_1$, ..., $\varepsilon_n)$

$= \varphi(\varepsilon_1$, ..., $\varepsilon_n) \det_{\varepsilon}(\alpha_1$ ... $\alpha_n)$.

Như thế, $\varphi$ sai khác $det<sub>\varepsilon</sub>$ một nhân tử $\varphi(\varepsilon_1,...,\varepsilon_n) \in \mathbf{K}$. Vậy $det<sub>\varepsilon</sub>$ là một hệ sinh

của không gian $\Lambda^n(V)^*$. Do tính chuẩn hoá của định thức, nên $det<sub>\varepsilon \neq$ 0. Vì $thế,</sub>$

hệ gồm một vécto $(\det_{\varepsilon})$ là một cơ sở của không gian vécto $\Lambda^n(V)^*$.

$\Box$

Hệ quả 3.7 (Tính duy nhất của định thức). Dinh thức det là hàm duy nhất từ

tập hợp các ma trận vuông M(n $\times$ n, $\mathbf{K})$ vào $\mathbf{K}$ có các tính chất đa tuyến tính, thay

phiên và chuẩn hoá nói ở $\S2$.



Chứng minh: Chọn e $= (e_1$, ..., $e_n)$ là hệ cơ sở chính tắc của $\mathbf{K}^n$. Nếu coi định

thức của ma trận A là một hàm của các vécto cột $\alpha_1$, ..., $\alpha_n$ của nó, thì

$\det$ A $= \det_{\mathbf{e}} (\alpha_1$, ..., $\alpha_n)$.

Nói cách khác det $= det_{e}$.

Giả sử $\varphi:$ M(n $\times$ n, $\mathbf{K}) \to \mathbf{K}$ là một hàm đa tuyến tính, thay phiên và chuẩn

hoá theo nghĩa đã nói ở §2. Ta cũng coi $\varphi(A)$ là hàm của các cột của A, như vậy

$\varphi \in \Lambda^n(\mathbf{K}^n)^*$. Theo Dinh lý 3.6,

$\varphi = \varphi(e_1$, ..., $e_n) \det_{\mathbf{e}} = \varphi(e_1$, ..., $e_n) \det$.

Nhưng $\varphi$ được chuẩn hoá, tức là $\varphi(e_1$, ..., $e_n) =$ 1, cho nên $\varphi = \det$.

$\Box$

Hệ quả 3.8 det A $\neq$ 0 nếu và chỉ nếu các vécto cột của A độc lập tuyến tính trong

$\mathbf{K}^n$.

Chứng minh: Nếu các vécto cột $\alpha_1$, ..., $\alpha_n$ của A phụ thuộc tuyến tính, thì theo

Hệ quả 2.3 ta có $\det(\alpha_1$, ..., $\alpha_n) =$ 0.

Ngược lại, giả sử $\alpha_1$, ..., $\alpha_n$ độc lập tuyến tính. Khi đó $\alpha = (\alpha_1$, ..., $\alpha_n)$ là một

cơ sở của $\mathbf{K}^n$. Gọi $\mathbf{e} = (e_1$, ..., $e_n)$ là cơ sở chính tắc của $\mathbf{K}^n$. Khi đó det $= det<sub>e</sub>$ lập

nên một cơ sở của $\Lambda^n(\mathbf{K}^n)^*$. Ta có

$\det_{\alpha} =$ c $\det$, $\qquad$ (c $\in \mathbf{K})$.

Do đó c $\det(\alpha_1$, ..., $\alpha_n) = \det_{\alpha}(\alpha_1$, ..., $\alpha_n) = \det E_n =$ 1. Vậy

$\det$ A $= \det(\alpha_1$, ..., $\alpha_n) \neq$ 0.

$\Box$

Dinh thức của tự đồng cấu

$\overline{4}$

Mỗi phần tử $\varphi \in \Lambda^n(V)^*$ có thể được coi là một phép đo "thể tích" có hướng trong

V. Cụ thể, $\varphi(\alpha_1$, ..., $\alpha_n)$ được xem như "thể tích" của hình hộp n chiều tựa trên

các vécto $\alpha_1$, ..., $\alpha_n$.



Với quan điểm đó thì định thức của một tự đồng cấu f: V $\to$ V chính là hệ

số giãn nở thể tích của các hình hộp n-chiều sau phép biến đổi f. Định lý sau đây

nói rõ điều đó.

Dinh lý 4.1 Giá sử f $\in$ End(V), trong đó V là một K-không gian vécto n chiều.

Khi đó, có duy nhất một phần tử được ký hiệu là $\det(f) \in \mathbf{K}$ sao cho

$\varphi(f(\alpha_1),...,f(\alpha_n))=\det(f)\varphi(\alpha_1,...,\alpha_n)$,

$v\acute{o}i$ mọi $\varphi \in \Lambda^n(V)^*$ và mọi $\alpha_1$, ..., $\alpha_n \in$ V.

Dinh nghĩa 4.2 Ta gọi det(f) là dinh thức của tự đồng cấu f.

Chứng minh Định lý 4.1. Chọn bất kỳ một phần tử $\eta \neq$ 0 trong $\Lambda^n(V)^*$. Vì

$\dim \Lambda^n(V)^* =$ 1, cho nên $(\eta)$ là một cơ sở của $\Lambda^n(V)^*$.

Xét ánh $xạ\theta: \underbrace{V\times\cdots\times V}\to \mathbf{K}xác$ định như sau

n $\; \hat{\text{lan}}$

$\theta(\alpha_1$, ..., $\alpha_n) = \eta(f(\alpha_1)$, ..., $f(\alpha_n))$.

Vì f tuyến tính, và $\eta$ đa tuyến tính thay phiên, nên $\theta$ cũng là đa tuyến tính thay

phiên, tức là $\theta \in \Lambda^n(V)^*$. Như vậy, có d $\in \mathbf{K}$ sao cho $\theta = d\eta$.

Mặt khác, vì (η) là một cơ sở của $\Lambda^{n}(V)^{*}$, cho nên với mọi $\varphi \in \Lambda^{n}(V)^{*}$ ta có

$\varphi = c\eta$ với một vô hướng nào đó c $\in \mathbf{K}$. Do đó

$\varphi(f(\alpha_1),...,f(\alpha_n)) = c\eta(f(\alpha_1),...,f(\alpha_n)) = c\theta(\alpha_1,...,\alpha_n)$

$= cd\eta(\alpha_1$, ..., $\alpha_n) = d\varphi(\alpha_1$, ..., $\alpha_n)$.

Dằng thức nói trong định lý được nghiệm đúng đối với hằng số $\det(f) =$ d không

phụ thuộc $\varphi$. Như vậy, ta đã chỉ ra sự tồn tại của $\det(f)$.

Để chứng minh tính duy nhất của $\det(f)$, ta chọn $\varphi = \eta$. Đẳng thức

$\varphi(f(\alpha_1),...,f(\alpha_n))=\det(f)\varphi(\alpha_1,...,\alpha_n)$



kéo theo $\theta = \det(f)\eta$. Do biểu thị tuyến tính của $\theta$ qua cơ sở $(\eta)$ là duy nhất, nên

$\det(f)$ xác định duy nhất.

$\Box$

### Định lý sau đây cho thấy mối liên hệ giữa định thức của tự đồng cấu với định

thức của ma trận, đồng thời chỉ ra một phương pháp để tính định thức của tự

đồng cấu.

### Định lý 4.3 Nếu tự đồng cấu f: V \to V có ma trận là A trong một cơ sở nào đó

của V, thì $\det(f) = \det$ A.

Chứng minh: Gọi $\varepsilon = (\varepsilon_1$, ..., $\varepsilon_n)$ là cơ sở của không gian V trong đó f có ma trận

là A. Ta có $f(\varepsilon_i) = \sum_{i=1}^n a_{ij} \varepsilon_i$. Nói cách khác

$(f(\varepsilon_1)...f(\varepsilon_n)) = (\varepsilon_1...\varepsilon_n)A$.

Chọn $\varphi = \det_{\varepsilon} \in \Lambda^n(V)$, và áp dụng Định lý 4.1, ta có

$\det(f) = \det(f) \det E_n = \det(f) \det_{\varepsilon}(\varepsilon_1$, ..., $\varepsilon_n)$

$= \det_{\varepsilon}(f(\varepsilon_1),...,f(\varepsilon_n)) = \det$ A.

$\Box$

Hệ quả 4.4 Nếu A và B là các ma trận của tự đồng cấu f: V $\to$ V trong những

$\cos s\dot{\sigma}$ khác nhau, thì det A $= \det$ B.

Dinh lý 4.5 (i) det $id_V =$ 1.

(ii) $\det(gf) = \det(g) \det(f)$, $\forall$ f, g $\in$ End(V).

Nói riêng, nếu f khả nghịch thì $\det(f^{-1}) = (\det(f))^{-1}$.

Chứng minh: (i) Đối với mỗi $\varphi \in \Lambda^n(V)^*$, ta có

$\varphi(id_V(\alpha_1),...,id_V(\alpha_n))=1\cdot\varphi(\alpha_1,...,\alpha_n)$,

với mọi $\alpha_1$, ..., $\alpha_n \in$ V. Do đó, theo định nghĩa của định thức của tự đồng cấu,

$\det(id_V)=1$.



(ii) Nếu $\varphi \in \Lambda^n(V)^*$, thì

$\det(gf)\varphi(\alpha_1,...,\alpha_n) = \varphi(gf(\alpha_1),...,gf(\alpha_n))$

$= \det(g)\varphi(f(\alpha_1),...,f(\alpha_n))$

$=$ det(q) det(f) $\varphi(\alpha_1$, ..., $\alpha_n)$,

với mọi $\alpha_1$, ..., $\alpha_n \in$ V. Do đó $\det(gf) = \det(g) \det(f)$.

Nếu f khả nghịch thì tồn tại $f^{-1} \in$ End(V) sao cho $ff^{-1} = id_V$. Từ đó

$\det(f) \det(f^{-1}) = \det(f f^{-1}) = \det(id_V) =$ 1. Hệ quả là $\det(f^{-1}) = (\det(f))^{-1}$. $\Box$

### Dịnh lý 4.6 Tự đồng cấu f: V \to V là một đẳng cấu nếu và chỉ nếu \det(f) \neq 0.

Chứng minh: Giả sử $\varepsilon = (\varepsilon_1$, ..., $\varepsilon_n)$ là một cơ sở của không gian vécto V. Gọi C

là ma trận của f trong cơ sở đó:

$(f(\varepsilon_1)$ ... $f(\varepsilon_n)) = (\varepsilon_1$ ... $\varepsilon_n)C$.

Nói cách khác, C là ma trận mà vécto cột thứ j của nó là vécto toạ độ của $f(\varepsilon_j)$

trong co sở $(\varepsilon_1$, ..., $\varepsilon_n)$.

Ta có

$\det(f) = \det(f) \det E_n = \det(f) \det(\varepsilon_1$, ..., $\varepsilon_n)$

$= \det_{\varepsilon}(f(\varepsilon_1),...,f(\varepsilon_n)) = \det$ C.

Nhận xét rằng, f là một đẳng cấu tuyến tính nếu và chỉ nếu $(f(\varepsilon_1),...,f(\varepsilon_n))$

là một hệ véctơ độc lập tuyến tính. Điều này tương đương với sự kiện hệ véctơ

cột của C độc lập tuyến tính, tức là tương đương với det C $=$ det(f) $\neq$ 0.

$\Box$

Các tính chất sâu hơn của định thức

$\overline{5}$

Tiết này dành để nghiên cứu sâu thêm các tính chất của định thức của ma trận.

Dinh lý 5.1 Giá sử A, B $\in$ M(n $\times$ n, $\mathbf{K})$. Khi đó



det(AB) $= \det$ A $\det$ B.

(i)

(ii) A khá nghịch nếu và chỉ nếu det A $\neq$ 0. Hơn nữa

$\det(A^{-1}) = (\det A)^{-1}$.

Chứng minh: (i) là một hệ quả của các Định lý 4.3 và 4.5.

(ii) là một hệ quả của Đinh lý 4.6 và của phần (i).

Dinh lý 5.2 (Dinh thức của ma trận chuyển vị).

$\det(A^t) = \det$ A, $\quad \forall$ A $\in$ M(n $\times$ n, $\mathbf{K})$.

Chứng minh: Giả sử A $= (a_{ij})_{n \times n}$, $A^t = (a_{ij}^t)_{n \times n}$. Theo định nghĩa định thức, ta

$\overline{c}$

$\det(A^t) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) a^t_{\sigma(1)1} \cdots a^t_{\sigma(n)n}$

$= \sum \text{sgn}(\sigma) a_{1\sigma(1)} \cdots a_{n\sigma(n)}$.

$\sigma{\in}S_n$

Nếu k $= \sigma(j)$, thì j $= \sigma^{-1}(k)$, và $a_{j\sigma(j)} = a_{\sigma^{-1}(k)k}$. Đặt $\omega = \sigma^{-1}$. Bởi vì $\omega \sigma =$ id,

cho nên $sgn\omega = \text{sgn}\sigma$. Hơn nữa, khi $\sigma$ chạy một lượt trên $S_n$ thì $\sigma^{-1}$ cũng chạy

một lượt trên $S_n$. Do đó

$det(A^t) = \sum_{\omega \in S_n} sgn(\omega)a_{\omega(1)1} \cdots a_{\omega(n)n}$

$=$ det A (theo định nghĩa). $\square$

Theo định lý trên, tất cả các tính chất của định thức đối với các cột của nó vẫn

đúng đối với các hàng của nó. Chẳng hạn, định thức là một hàm đa tuyến tính,

thay phiên và chuẩn hoá đối với các hàng của nó...

Bây giờ ta xét bài toán tính định thức cấp n thông qua các định thức cấp nhỏ

hon.



Cho A $= (a_{ij}) \in$ M(n $\times$ n, $\mathbf{K})$ và k là một số nguyên bất kỳ thoả mãn 1 $\leq$ k $<$ n.

Xét hai bộ chỉ số

1 $\leq i_1 < i_2 < \cdots < i_k \leq$ n

1 $\leq j_1 < j_2 < \cdots < j_k \leq$ n.

Các phần tử nằm trên giao của các hàng $i_1,...,i_kvà$ các $cộtj_1,...,j_kcủa$ ma trận

A lập nên một ma trận cấp k (được gọi là một ma trận con cấp k của A), và định

thức của ma trận con đó, được ký hiệu $làD_{i_1,\dots,i_k}^{j_1,\dots,j_k},được$ gọi là một định thức con

cấp k của A.

Nếu xoá tất cả các hàng $i_1$, ..., $i_k$ và các cột $j_1$, ..., $j_k$ thì phần còn lại của ma

trận A lập nên một ma trận vuông cấp n - k, mà định thức của nó được ký hiệu

là $\overline{D}_{i_1,\dots,i_k}^{j_1,\dots,j_k}$ và được gọi là định thức con bù của $D_{i_1,\dots,i_k}^{j_1,\dots,j_k}$.

Ta gọi $(-1)^{s(I,J)}\overline{D}_{i_1,\dots,i_k}^{j_1,\dots,j_k}$ là phần bù đại số của $D_{i_1,\dots,i_k}^{j_1,\dots,j_k}$, trong đó $s(I,J)=(i_1+1)$

$\cdots$ + $i_k)$ + $(j_1$ + $\cdots$ + $j_k)$.

Dinh lý 5.3 (Khai triển Laplace). Giả sử đã chọn ra k cột (tương ứng, k hàng)

trong một định thức cấp n (1 $\leq$ k $<$ n). Khi đó, định thức đã cho bằng tổng của

tất cả các tích của các định thức con cấp k lấy ra từ k cột (tương ứng, k hàng) đã

chọn với phần bù đại số của chúng. Nói rõ hơn, ta có:

(i) Công thức khai triển định thức theo k cột $j_1 < \cdots < j_k:$

det A $= \sum_{i_1 < \dots < i_k} (-1)^{s(I,J)} D_{i_1$, $\dots$, $i_k}^{j_1$, $\dots$, $j_k} \overline{D}_{i_1$, $\dots$, $i_k}^{j_1$, $\dots$, $j_k};$

(ii) Công thức khai triển định thức theo k hàng $i_1 < \cdots < i_k:$

det A $= \sum_{i_1$, ..., $i_k} (-1)^{s(I,J)} D^{j_1,...,j_k}_{i_1,...,i_k} \overline{D}^{j_1,...,j_k}_{i_1,...,i_k}$.

$j_1 < \cdots < j_k$

Chứng minh: Ta sẽ chỉ chứng minh công thức khai triển Laplace theo k hàng.

Từ đó, áp dụng Định lý 5.2, ta thu được công thức khai triển theo k cột.

Trước hết, ta chứng minh công thức khai triển Laplace theo k hàng đặc biệt

$i_1 =$ 1, $i_2 =$ 2, ..., $i_k =$ k.



Ký hiệu vécto cột thứ j của ma trận A là $\alpha_i$. Với mỗi bộ chỉ số 1 $\leq j_1 < \cdots <$

$j_k \leq$ n, ta gọi $j'_1$, ..., $j'_\ell$ là bộ chỉ số $\{1$, 2, ..., $n\} \setminus \{j_1$, ..., $j_k\}$ được xếp theo thứ tự

tăng dần:

1 $\leq j'_1 < \cdots < j'_\ell \leq$ n.

Xét hàm sau đây

$\eta(A) = \eta(\alpha_1$, ..., $\alpha_n) = \sum_{j_1 <$ ... $< j_k} (-1)^{s(I,J)} D_{1,...,k}^{j_1,...,j_k} \overline{D}_{1,...,k}^{j_1,...,j_k}$.

Dễ thấy rằng $\eta$ là một hàm đa tuyến tính đối với $\alpha_1$, ..., $\alpha_n$.

Nếu A $= E_n$ (ma trận đơn vị), thì $D_{1,...,k}^{j_1,...,j_k} \neq$ 0 nếu và chỉ nếu $j_1 =$ 1, $j_2 =$ 1

$2,...,j_k =$ k. Khi đó $D^{1,...,k}_{1,...,k} =$ 1 và $\overline{D}^{1,...,k}_{1,...,k} =$ 1. Do đó, $\eta$ có tính chuẩn hoá, tức là

$\eta(E_n)=1$.

Ta sẽ chứng minh $\eta$ có tính thay phiên.

Trước hết giả sử $\alpha_r = \alpha_{r+1}$. Lấy một số hạng bất kỳ trong tổng xác định $\eta$, nếu

$j_t =$ r, $j_{t+1} =$ r + 1 thì $D_{1,...,k}^{j_1,...,j_k} =$ 0; còn nếu $j'_u =$ r, $j'_{u+1} =$ r + 1 thì $\overline{D}_{1,...,k}^{j_1,...,j_k} =$ 0

(trong cả hai trường hợp, định thức tương ứng bằng 0 vì có hai cột bằng nhau).

Các số hạng còn lại được ghép thành từng cặp: số hạng có $j_t =$ r, $j'_u =$ r + 1 được

ghép với số hạng $cój_t=r+1,\,j'_u=r(các$ chỉ số khác của hai số hạng này như

nhau). Khi đó, hai số hạng được ghép cặp có phần $D^{j_1,\ldots,j_k}_{1,\ldots,k}\overline{D}^{j_1,\ldots,j_k}_{1,\ldots,k}$ bằng nhau (vì

$\alpha_r = \alpha_{r+1}$, và có dấu $(-1)^{s(I,J)}$ trái nhau (vì chỉ số $j_t$ của chúng tương ứng bằng

r và r+1).Do đó chúng là các phần tử đối nhau. Tóm lại, $\eta(\alpha_1,...,\alpha_n)=0nếu$

$\alpha_r = \alpha_{r+1}$ với r bất kỳ (1 $\leq$ r $<$ n).

Từ đó, theo phương pháp đã dùng để chứng minh Hệ quả 2.3, ta có

$\eta(\alpha_1$, ..., $\alpha_r$, $\alpha_{r+1}$, ..., $\alpha_n) = -\eta(\alpha_1$, ..., $\alpha_{r+1}$, $\alpha_r$, ..., $\alpha_n)$,

với mọi $\alpha_1$, ..., $\alpha_n \in \mathbf{K}^n$ và mọi r (1 $\leq$ r $<$ n).

Bây giờ ta sẽ chứng minh rằng $\eta$ có tính thay phiên, tức là

$\eta(\alpha_1$, ..., $\alpha_r$, ..., $\alpha_s$, ..., $\alpha_n) =$ 0,



nếu $\alpha_r = \alpha_s$ với cặp chỉ số r $\neq$ s bất kỳ. Thật vậy, ta lần lượt hoán vị $\alpha_s$ với $\alpha_{s-1}$

rồi với $\alpha_{s-2},..$. để đưa $\alpha_s$ về vị trí của $\alpha_{r+1}$. Ta có

$\eta(\alpha_1$, ..., $\alpha_r$, ..., $\alpha_s$, ..., $\alpha_n) = (-1)^{s-r-1} \eta(\alpha_1$, ..., $\alpha_r$, $\alpha_s$, ..., $\alpha_n) =$ 0,

bởi vì $\alpha_r$ và $\alpha_s$ đứng kề nhau trong vế ở giữa.

Theo Hệ quả 3.7, định thức là hàm duy nhất trên các cột của ma trận có các

tính chất đa tuyến tính, thay phiên và chuẩn hoá, cho nên

$\det(\alpha_1$, ..., $\alpha_n) = \eta(\alpha_1$, ..., $\alpha_n)$.

Đó chính là công thức khai triển Laplace theo k hàng $i_1 =$ 1, ..., $i_k =$ k.

Cuối cùng, ta xét trường hợp k hàng tùy ý I $= (i_1$, ..., $i_k)$. Ký hiệu I' $=$ (1, ..., k).

Ta lần lượt hoán vị hàng $i_1$ với $(i_1$ - 1) hàng đứng trước nó (để đưa hàng $i_1về$

hàng 1 và giữ nguyên vị trí tương đối của các hàng còn lại), rồi lại lần lượt hoán vị

hàng $i_2với (i_2-2)hàng$ đứng trước nó... Cuối cùng, lần lượt hoán vị hàng $i_kvới$

$(i_k$ - k) hàng đứng trước nó. Sau phép biến đổi đó, các hàng $i_1$, ..., $i_k$ được đưa về

các hàng 1, ..., k và vị trí tương đối của các hàng còn lại được giữ nguyên. Ma trận

A được biến đổi thành ma trậnA'với $\det A=(-1)^{(i_1-1)+\cdots+(i_k-k)}\det$ A'. Ta cũng

$\overline{c}$

$(-1)^{s(I,J)} = (-1)^{(i_1+\cdots+i_k)-(1+\cdots+k)}(-1)^{s(I',J)}$,

$D^{j_1,...,j_k}_{i_1,...,i_k}(A) = D^{j_1,...,j_k}_{1,...,k}(A')$,

$\overline{D}^{j_1,\ldots,j_k}_{i_1,\ldots,i_k}(A) = \overline{D}^{j_1,\ldots,j_k}_{1,\ldots,k}(A')$.

Dùng khai triển Laplace theokhàng 1,...,kcủa ma $trậnA^{\prime},ta$ có

det A $= (-1)^{(i_1-1)+\cdots+(i_k-k)} \det$ A'

$= (-1)^{(i_1+\cdots+i_k)-(1+\cdots+k)} \sum (-1)^{s(I',J)}D^{j_1,\ldots,j_k}_{1,\ldots,k}(A')\overline{D}^{j_1,\ldots,j_k}_{1,\ldots,k}(A')$

$j_1 < \cdots < j_k$

$= \sum (-1)^{s(I,J)} D^{j_1,...,j_k}_{i_1,...,i_k}(A) \overline{D}^{j_1,...,j_k}_{i_1,...,i_k}(A)$.

$j_1 < \cdots < j_k$

Dinh lý được hoàn toàn chứng minh.

$\Box$



Tính định thức Vandermonde

Ví du:

$ D_n = \begin{vmatrix} 1 & x_1 & x_1^2 & \dots & x_1^{n-1} \\ 1 & x_2 & x_2^2 & \dots & x_2^{n-1} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_n & x_n^2 & \dots & x_n^{n-1} \end{vmatrix}. $

Lời giải: Ta làm cho hầu hết các phần tử trên hàng cuối của định thức trở thành

bằng không bằng cách lấy cột thứ (n-1) nhân với $-x_n$ rồi cộng vào cột n, sau đó

lấy cột thứ(n-2)nhân với $-x_n$ rồi cộng vào cột (n-1),..., cuối cùng lấy cột thứ

nhất nhân với $-x_n$ rồi cộng vào cột 2. Sau biến đổi đó, ta thu được

$ D_n = \begin{vmatrix} 1 & x_1 - x_n & x_1(x_1 - x_n) & \dots & x_1^{n-2}(x_1 - x_n) \\ 1 & x_2 - x_n & x_2(x_2 - x_n) & \dots & x_2^{n-2}(x_2 - x_n) \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 1 & x_{n-1} - x_n & x_{n-1}(x_{n-1} - x_n) & \dots & x_{n-1}^{n-2}(x_{n-1} - x_n) \\ 1 & 0 & 0 & \dots & 0 \end{vmatrix}. $

Khai triển Laplace theo hàng thứ n, rồi đưa các thừa số chung của mỗi hàng ra

ngoài dấu định thức, ta có

$ D_n = (-1)^{n+1}(x_1 - x_n)(x_2 - x_n) \cdots (x_{n-1} - x_n) \begin{vmatrix} 1 & x_1 & x_1^2 & \dots & x_1^{n-2} \\ 1 & x_2 & x_2^2 & \dots & x_2^{n-2} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n-1} & x_{n-1}^2 & \dots & x_{n-1}^{n-2} \end{vmatrix}. $

Từ đó ta thu được công thức truy toán

$D_n = (x_n$ - $x_1)(x_n$ - $x_2) \cdots (x_n$ - $x_{n-1}) D_{n-1}$.

Xuất phát với $D_1 =$ 1, và bằng quy nạp sử dụng công thức trên, ta có

$D_n = \prod_{i > j} (x_i$ - $x_j)$.

Một ứng dụng quan trọng của khai triển Laplace là công thức tính ma trận

nghịch đảo.



Dinh lý 5.4 Nếu ma trận vuông A $= (a_{ij}) \in$ M(n $\times$ n, $\mathbf{K})$ có định thức khác 0 thì

A khả nghịch và

$ A^{-1} = \frac{1}{\det A} \left( \begin{array}{ccc} \tilde{a}_{11} & \ldots & \tilde{a}_{n1} \ \ldots & \ldots & \ldots \ \tilde{a}_{1n} & \ldots & \tilde{a}_{nn} \end{array} \right), $

trong đó $\tilde{a}_{ij}$ là phần bù đại số của $a_{ij}$.

Chứng minh: Ký hiệu ma trận nói trong định lý là B. Theo định lý Laplace về

khai triển det A theo hàng i, ta có

$a_{i1}\tilde{a}_{i1}$ + $\cdots$ + $a_{in}\tilde{a}_{in} = \det$ A, $\quad \forall$ i.

Hơn nữa, với mọi j $\neq$ i, xét ma trận thu được từ A bằng cách thay hàng j bởi

hàng i và giữ nguyên các hàng khác, kể cả hàng i. Ma trận này có hai hàng i và j

đều bằng $(a_{i1},...,a_{in})$. Do đó, định thức của nó bằng 0. Khai triển Laplace định

thức này theo hàng j, ta có

$a_{i1}\tilde{a}_{j1}$ + $\cdots$ + $a_{in}\tilde{a}_{jn} =$ 0, $\quad \forall$ i $\neq$ j.

Kết hợp hai đẳng thức trên, ta thu được AB $= E_n$. Tương tự, bằng cách áp dụng

khai triển Laplace theo cột, ta có BA $= E_n$.

Tóm lại, A khả nghịch, và $A^{-1} =$ B.

$\Box$

Trong phần sau, chúng ta sẽ giới thiệu một phương pháp khác tìm ma trận

nghịch đảo bằng cách giải hệ phương trình tuyến tính.

Dịnh thức và hạng của ma trận

6

Chúng ta đã đinh nghĩa hang của một ma trân là hang của hệ vécto cột của nó.

### Định lý sau đây cho phép tính hạng của ma trận thông qua định thức. Đồng thời

nó đặt cơ sở cho khẳng định: hạng của ma trận cũng bằng hạng của hệ véctơ hàng

của ma trân đó.



### Định lý 6.1 Giả sử A là một ma trận m hàng, n cột với các phần tử trong trường

K. Khi đó, hạng của ma trận A bằng cấp cao nhất của các định thức con khác 0

của A. Nói rõ hơn, rankA $=$ r nếu có một định thức con cấp r của A khác 0, và

mọi định thức con cấp $>$ r (nếu có) của A đều bằng 0.

Chứng minh: Việc đổi chỗ các cột rõ ràng không làm thay đổi rankA. Việc đổi

chỗ các hàng cũng vậy, bởi vì đổi chỗ các hàng tương ứng với việc đổi chỗ các toạ

độ của các vécto cột trong $\mathbf{K}^n$, đó là một đẳng cấu tuyến tính của $\mathbf{K}^n$.

Mặt khác, đổi chỗ các hàng và các cột của A cũng không làm thay đổi cấp cao

nhất của các định thức con của A.

Vì thế, để cho dễ trình bày và không giảm tổng quát, ta có thể giả sử định thức

con cấp r ở góc trái trên của A khác 0, và mọi định thức con cấp (r+1) của A đều

$b\mathrm{ång}$ 0.

Khi đó, r cột đầu tiên của A độc lập tuyến tính. (Nếu trái lại, thì định thức

cấp r ở góc trái trên của A bằng 0.) Ta sẽ chứng minh rằng cột thứ j của A, ký

hiệu $\alpha_j$, biểu thị tuyến tính quarcột đầu tiên, với r $<$ j $\leq$ n.Để làm điều đó, với

môi i $tho<br/>ã$ mãn1 $\leq$ i $\leq$ m,ta xét định thức sau đây:

$ \det \left( \begin{array}{cccc} a_{11} & ... & a_{1r} & a_{1j} \ . & ... & . & . \ a_{r1} & ... & a_{rr} & a_{rj} \ a_{i1} & ... & a_{ir} & a_{ij} \end{array} \right). $

Định thức này luôn bằng 0. Thật vậy, nếu 1 $\leq$ i $\leq$ r, thì định thức có 2 hàng bằng

nhau; còn nếu r $<$ i $\leq$ m, thì nó là một định thức con cấp (r+1) của A. Khai triển

Laplace định thức này theo hàng cuối, và gọi $\lambda_k$ là phần bù đại số của $a_{ik}$, ta có

$\lambda_1 a_{i1}$ + $\cdots$ + $\lambda_r a_{ir}$ + $\lambda a_{ij} =$ 0.

Ở đây $\lambda = \lambda_j \neq$ 0, vì đó là định thức con cấp r ở góc trái trên. Lưu ý rằng

$\lambda_1$, ..., $\lambda_r$, $\lambda$ đều không phụ thuộc vào i. Từ đó

$\alpha_j = -\frac{\lambda_1}{\lambda}\alpha_1$ - $\cdots$ - $\frac{\lambda_r}{\lambda}\alpha_r$.



Theo đinh nghĩa hang của ma trân, rankA $=$ r.

$\Box$

Hệ quả 6.2 Hạng của một ma trận bằng hạng của hệ các véctơ hàng của nó.

Chứng minh: Ta có

rankA $= \text{rank} A^t$ (theo Dinh lý 3.4)

$=$ Hang của hệ véctor cột của At

$=$ Hang của hê véctor hàng của A.

$\Box$

Hệ phương trình tuyến tính - Quy tắc Cramer

$7\phantom{.}$

Một hệ thống có dang

$ \begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\ \cdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m, \end{cases} $

trong đó $a_{ij}$, $b_i$ là các phần tử cho trước trong trường K, được gọi là một hệ phương

trình tuyến tính gồm m phương trình với nẩn $x_1$, ..., $x_n$. Ký hiệu

$ A = (a_{ij})_{m \times n}, x = \begin{pmatrix} x_1 \\ \cdot \\ \cdot \\ \cdot \\ x_n \end{pmatrix}, \beta = \begin{pmatrix} b_1 \\ \cdot \\ \cdot \\ \cdot \\ b_m \end{pmatrix}. $

Khi đó, hệ phương trình nói trên có thể viết dưới dạng phương trình véctơ

Ax $= \beta$.

Một nghiệm của hệ này là một vécto $x^0 \in \mathbf{K}^n$ sao cho $Ax^0 = \beta$. Một hệ phương

trình có ít nhất một nghiêm được gọi là một hệ phương trình tương thích.

Hệ phương trình Ax $=$ 0 được gọi là hệ phương trình tuyến tính thuần nhất liên

kết với hê Ax $= \beta$.



Theo kinh nghiệm, ta cảm nhận rằng hệ phương trình tuyến tính Ax $= \beta$ có

nghiệm duy nhất nếu số phương trình của hệ bằng số ẩn, và không có phương trình

nào của hệ là "hệ quả" của các phương trình khác. Điều này được diễn đạt chính

xác trong định nghĩa sau đây.

### Định nghĩa 7.1 Hệ phương trình tuyến tính Ax = \beta được gọi là một hệ không suy

biến (hay một hệ Cramer) nếu nó có số phương trình bằng số ẩn (nói cách khác,

nếu A là một ma trận vuông) và nếu det A $\neq$ 0.

Dinh lý 7.2 Hệ phương trình tuyến tính không suy biến Ax $= \beta$ có một nghiệm

duy nhất, được tính bằng công thức

$x_j = \frac{\det A_j}{\det A}$, $\quad$ (1 $\le$ j $\le$ n),

trong đó $A_j$ là ma trận nhận được từ ma trận A bằng cách thay cột thứ j bởi cột

$h\hat{e}$ số tư do $\beta$.

Chứng minh: Vì det A $\neq$ 0, nên A là một ma trận khả nghịch. Khi đó

Ax $= \beta \iff A^{-1}Ax = A^{-1}\beta$

$\iff$ x $= A^{-1}\beta$.

Theo Dinh lý 5.4, ta có

$ A^{-1} = \frac{1}{\det A} \left( \begin{array}{ccc} \tilde{a}_{11} & \ldots & \tilde{a}_{n1} \ \ldots & \ldots & \ldots \ \tilde{a}_{1n} & \ldots & \tilde{a}_{nn} \end{array} \right), $

trong đó $\tilde{a}_{ij}$ là phần bù đại số của $a_{ij}$ trong det A. Từ đó x $= A^{-1}\beta$ có nghĩa là

$x_j = \frac{1}{\det A} (\tilde{a}_{1j}b_1$ + $\tilde{a}_{2j}b_2$ + $\cdots$ + $\tilde{a}_{nj}b_n)= \frac{\det A_j}{\det A}$, $\quad$ (1 $\le$ j $\le$ n).



Dằng thức cuối nhận được bằng cách khai triển Laplace định thức của $A_i$ theo cột

thứ j.

$\square$.

Giải hệ phương trình sau đây:

Ví du:

$ \begin{cases}\n x + y + 3z + 4t = -3 \\
 x + y + 5z + 2t = 1 \\
 2x + y + 3z + 2t = -3 \\
 2x + 3y + 11z + 5t = 2.\n\end{cases} $

Trước hết ta tính định thức của ma trận hệ số

Lò i giai:

$ det A = \begin{bmatrix} 1 & 1 & 3 & 4 \\ 1 & 1 & 5 & 2 \\ 2 & 1 & 3 & 2 \\ 2 & 3 & 11 & 5 \end{bmatrix} = \begin{bmatrix} 1 & 1 & 3 & 4 \\ 0 & 0 & 2 & -2 \\ 0 & -1 & -3 & -6 \\ 0 & 1 & 5 & -3 \end{bmatrix} $

$ =\begin{vmatrix} 0 & 2 & -2 \\ -1 & -3 & -6 \\ 1 & 5 & -3 \end{vmatrix}=\begin{vmatrix} 0 & 2 & -2 \\ 0 & 2 & -9 \\ 1 & 5 & -3 \end{vmatrix}=(-1)^{3+1}\begin{vmatrix} 2 & -2 \\ 2 & -9 \end{vmatrix}=2\cdot(-9)-2\cdot(-2)=-14. $

Theo quy tắc Cramer, hệ phương trình có nghiệm duy nhất

$ x = \frac{\begin{vmatrix} -3 & 1 & 3 & 4 \\ 1 & 1 & 5 & 2 \\ -3 & 1 & 3 & 2 \\ 2 & 3 & 11 & 5 \\ \end{vmatrix}}{x \cdot \frac{1}{2} + \frac{1}{2}} = \frac{28}{-14} = -2, \qquad y = \frac{\begin{vmatrix} 1 & -3 & 3 & 4 \\ 1 & 1 & 5 & 2 \\ 2 & -3 & 3 & 2 \\ 2 & 2 & 11 & 5 \\ \end{vmatrix}}{x \cdot \frac{1}{2} + \frac{1}{2}} = \frac{0}{-14} = 0, $

$ \begin{vmatrix} 1 & 1 & 3 & -3 \end{vmatrix} $

$ \begin{vmatrix} 1 & 1 & -3 & 4 \end{vmatrix} $

$ \begin{vmatrix} 1 & 1 & 1 & 2 \\ 2 & 1 & -3 & 2 \\ 2 & 3 & 2 & 5 \\ \end{vmatrix} = \frac{-14}{-14} = 1, $

$ t = \frac{\begin{vmatrix} 1 & 1 & 5 & 1 \\ 2 & 1 & 3 & -3 \\ 2 & 3 & 11 & 2 \end{vmatrix}}{\det A} = \frac{14}{-14} = $



Hệ phương trình tuyến tính - Phương pháp khử

8

Gauss

Phương pháp Cramer chỉ áp dụng được cho các hệ phương trình tuyến tính không

suy biến (nói riêng, các hệ này có số phương trình bằng số ẩn). Thế nhưng rất

nhiều hệ phương trình tuyến tính mà người ta gặp lại suy biến. Phương pháp khử

Gauss, mà ta sẽ trình bày dưới đây, có ưu điểm là có thể áp dụng cho hệ phương

trình tuyến tính tùy ý. Nhược điểm của phương pháp này là không đưa ra được

thông tin nào về nghiệm của hệ phương trình trước khi giải xong hệ đó.

Nội dung của phương pháp khử Gauss như sau.

Ta gọi hai hệ phương trình là tương đương nếu nghiệm của hệ này cũng là

nghiệm của hệ kia và ngược lại.

Nhận xét rằng nếu ta áp dụng các phép biến đổi sau đây, được gọi là các phép

biến đổi sơ cấp, trên một hệ phương trình tuyến tính, ta nhận được một hệ phương

trình tuyến tính tương đương với hê ban đầu.

(1) Đổi chỗ hai phương trình của hệ.

(2) Nhân một phương trình của hệ với một vô hướng khác 0 thuộc trường K.

Cộng vào một phương trình một tổ hợp tuyến tính của các phương trình khác

(3)

trong hệ.

Bây giờ ta xét một hệ phương trình tuyến tính tổng quát

$\int a_{11}x_1$ + $a_{12}x_2$ + $\cdots$ + $a_{1n}x_n = b_1$

$a_{m1}x_1$ + $a_{m2}x_2$ + $\cdots$ + $a_{mn}x_n = b_m$.



Ta gọi A $= (a_{ij})_{m \times n}$ là ma trận các hệ số, và

$ \overline{A} = \left( \begin{array}{cccc} a_{11} & a_{12} & \ldots & a_{1n} & b_1 \ a_{21} & a_{22} & \ldots & a_{2n} & b_2 \ . & . & . & . & . \ a_{m1} & a_{m2} & \ldots & a_{mn} & b_m \end{array} \right) $

là ma trận các hệ số mở rộng của hệ phương trình nói trên.

Giả sử có một hệ số nào đó $a_{ij} \neq$ 0. Không giảm tổng quát (nếu cần, đổi chỗ

các phương trình và đánh số lại các ẩn) ta có thể coi $a_{11} \neq$ 0. Khi đó, nhân phương

trình thứ nhất với $\left(-\frac{a_{i1}}{a_{i1}}\right)$ rồi cộng vào phương trình thứ i (i $=$ 2, ..., m), ta nhận

được hệ phương trình tương đương có dạng

$ \left\{\n\begin{array}{rcl}\na_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n & = & b_1 \\
a'_{22}x_2 + \cdots + a'_{2n}x_n & = & b'_2 \\
\vdots & \vdots & \ddots & \vdots \\
a'_{m2}x_2 + \cdots + a'_{mn}x_n & = & b'_m.\n\end{array}\n\right. $

Lặp lại lập luận trên đối với hệ con gồm (n-1) phương trình cuối với các ẩn

$x_2$, $\ldots$, $x_n$.

Sau một số hữu hạn bước, hệ phương trình Ax $= \beta$ được đưa về một hệ tương

đương, với ma trận mở rộng có dạng

$ \left( \begin{array}{cccccc} \bar{a}_{11} & * & ... & * & * & ... & * & \bar{b}_1 \ 0 & \bar{a}_{22} & ... & * & * & ... & * & \bar{b}_2 \ . & . & ... & * & * & ... & * & . \ 0 & 0 & ... & \bar{a}_{rr} & * & ... & * & \bar{b}_r \ 0 & 0 & ... & 0 & 0 & ... & 0 & \bar{b}_{r+1} \ . & . & ... & . & . & ... & . & . \ 0 & 0 & ... & 0 & 0 & ... & 0 & \bar{b}_m \ \end{array} \right), $

trong đó $\bar{a}_{ii} \neq$ 0 (i $=$ 1, ..., r), và các dấu * ký hiệu các phần tử có thể khác 0 trong

trường K.



Nếu một trong các vô hướng $\bar{b}_{r+1},...,\bar{b}_m$ khác 0, thì hệ phương trình vô nghiệm.

Nếu $\bar{b}_{r+1} = \cdots = \bar{b}_m =$ 0, thì hệ phương trình có nghiệm. Hơn nữa, mỗi nghiệm

của hệ phương trình đều có thể nhận được bằng cách gán cho $x_{r+1},...,x_n$ những

giá trị tuỳ ý thuộc trường K (nếu n $>$ r), rồi giải duy nhất $x_1$, ..., $x_r$ theo những

giá trị đã gán cho $x_{r+1},...,x_n$. (Cụ thể, $x_r$ được tìm từ phương trình thứ $r,...,x_1$

được tìm từ phương trình thứ nhất.)

Ví dụ: Giải hệ phương trình

$x_1$ + $3x_2$ + $5x_3$ - $2x_4 =$ 3 $x_1$ + $5x_2$ - $9x_3$ + $8x_4 =$ 1 $2x_1$ + $7x_2$ + $3x_3$ + $x_4 =$ 5

$ \begin{bmatrix} 5x_1 + 18x_2 + 4x_3 + 5x_4 = 12. \end{bmatrix} $

Dùng phương pháp khử Gauss, ta thấy hệ phương trình trên tương

Lòn giai:

duong với

$ \begin{cases}\nx_1 + 3x_2 + 5x_3 - 2x_4 &=& 3 \\
2x_2 - 14x_3 + 10x_4 &=& -2 \\
x_2 - 7x_3 + 5x_4 &=& -1 \\
3x_2 - 21x_3 + 15x_4 &=& -3\n\end{cases}
\begin{cases}\nx_1 + 3x_2 + 5x_3 - 2x_4 &=& 3 \\
x_2 - 7x_3 + 5x_4 &=& -1 \\
0x_2 + 0x_3 + 0x_4 &=& 0 \\
0x_2 + 0x_3 + 0x_4 &=& 0\n\end{cases}
\begin{cases}\nx_1 &=& 6 -  $

Nhận xét 8.1 Để cho gọn, trong quá trình giải hệ phương trình tuyến tính, ta chỉ

cần ghi nhận sự biến đổi của ma trận hệ số suy rộng. Chẳng hạn trong ví dụ trên,



ta chỉ cần viết

$ \begin{pmatrix} 1 & 3 & 5 & -2 & 3 \\ 1 & 5 & -9 & 8 & 1 \\ 2 & 7 & 3 & 1 & 5 \\ 5 & 18 & 4 & 5 & 12 \end{pmatrix} \Longleftrightarrow \begin{pmatrix} 1 & 3 & 5 & -2 & 3 \\ 0 & 2 & -14 & 10 & -2 \\ 0 & 1 & -7 & 5 & -1 \\ 0 & 3 & -21 & 15 & -3 \end{pmatrix} $

$ \iff \begin{pmatrix} 1 & 3 & 5 & -2 \\ 0 & 1 & -7 & 5 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \xrightarrow{3} \begin{pmatrix} x_1 & = & 6 - 26x_3 + 17x_4 \\ x_2 & = & -1 + 7x_3 - 5x_4 \\ x_3, & x_4 & \text{tuy } \circ \circ. \end{pmatrix} $

Nhận xét 8.2 Tương ứng với các phép biến đổi sơ cấp trên hệ phương trình tuyến

tính là các phép biến đổi sơ cấp trên ma trận. Đó là các phép biến đổi thuộc một

trong các dang sau đây

(1) Đổi chỗ hai hàng (hoặc hai cột) của ma trận.

(2) Nhân một hàng (hoặc một cột) của ma trận với một vô hướng khác 0.

Cộng vào một hàng (hoặc một cột) một tổ hợp tuyến tính của các hàng (tương

(3)

úng: các cột) khác.

Dễ thấy rằng các phép biến đổi sơ cấp không làm thay đổi hạng của ma trận.

Nhận xét này dẫn tới một cách tính hạng của ma trận rất có ích trong thực hành.

Cụ thể là, mỗi ma trận A $= (a_{ij})_{m \times n}$ sau một số hữu hạn phép biến đổi sơ cấp



đều có thể đưa về một ma trận dạng (tam giác trên suy rộng)

$ \left( \begin{array}{cccccc} \bar{a}_{11} & * & ... & * & * & ... & * \ 0 & \bar{a}_{22} & ... & * & * & ... & * \ . & . & ... & * & * & ... & * \ 0 & 0 & ... & \bar{a}_{rr} & * & ... & * \ 0 & 0 & ... & 0 & 0 & ... & 0 \ . & . & ... & . & ... & . & . & . & . & . \ 0 & 0 & ... & 0 & 0 & ... & 0 & \end{array} \right), $

trong đó $\bar{a}_{ii} \neq$ 0 (i $=$ 1, ..., r), và các dấu * ký hiệu các phần tử có thể khác 0 trong

trường K.

Bằng cách trực tiếp dùng định nghĩa của hạng hoặc dùng Định lý 6.1, ta dễ

thấy rằng hạng của ma trận nói trên bằng r.

Nhận xét 8.3 Phương pháp khử Gauss được ứng dụng vào việc tìm ma trận

nghịch đảo.

Giả sử cần tìm nghịch đảo của ma trận A $= (a_{ij}) \in$ M(n $\times$ n, $\mathbf{K})$ nếu như nó

khả nghịch. Ta xét hệ phương trình

$\sum_{j=1}^{n} a_{ij} x_j = y_i$ (i $=$ 1, ..., n).

Khi đó, A khả nghịch nếu và chỉ nếu hệ phương trình trên có nghiệm với mọi vế

phải $y_1$, ..., $y_n$. Hơn nữa, nếu nghiệm của hệ được cho bởi công thức

$x_i = \sum_{j=1}^n b_{ij} y_j$ (i $=$ 1, ..., n),

thì ma trận nghịch đảo của A chính là $A^{-1} = (b_{ij})_{n \times n}$. (Công thức biểu thị tường

minh $x_1$, ..., $x_n$ qua $y_1$, ..., $y_n$ có thể được tìm bằng cách dùng phương pháp khử

Gauss.)

Thật vậy, ta xét phép biến đổi tuyến tính $\tilde{A}: \mathbf{K}^n \to \mathbf{K}^n$, x $\mapsto$ Ax. Nó có ma

trận là A trong cơ sở chính tắc của $\mathbf{K}^n$. Hệ phương trình Ax $=$ y có nghiệm với



moi y nếu và chỉ nếu $\tilde{A}$ là một đẳng cấu tuyến tính, điều này xảy ra khi và chỉ

khi A khả nghịch. Hơn nữa, ta có Ax $=$ y tương đương với x $= A^{-1}y$. Do đó

$A^{-1} = (b_{ij})_{n \times n}$.

Cấu trúc nghiệm của hệ phương trình tuyến

9

tính

Ta xét các hệ phương trình tuyến tính thuần nhất và không thuần nhất liên kết

với nhau

Ax $=$ 0 và Ax $= \beta$,

trong đó A $= (a_{ij})_{m \times n} \in$ M(m $\times$ n, $\mathbf{K})$, $\beta \in \mathbf{K}^m$. Như vậy, cả hai hệ phương trình

nói trên đều gồm m phương trình và n ẩn.

### Dịnh lý 9.1 Tập hợp L tất cả các nghiệm của hệ phương trình tuyến tính thuần

nhất Ax $=$ 0 là một không gian vécto con của $\mathbf{K}^n$, có số chiều thoả mãn hệ thức

$\dim$ L $=$ n - $\text{rank}$ A.

Chứng minh: Ta xét ánh xạ tuyến tính

$\tilde{A}: \mathbf{K}^n \rightarrow \mathbf{K}^m$,

x $\mapsto$ Ax.

Rõ ràng L $=$ Ker $\tilde{A}$ là một không gian véctơ con của $\mathbf{K}^n$. Hơn nữa, vì ánh xạ tuyến

tính $\tilde{A}$ có ma trận là A trong cơ sở chính tắc của các không gian véctơ $\mathbf{K}^n$ và $\mathbf{K}^m$,

cho nên

$\dim$ L $= \dim$ Ker $\tilde{A} = \dim \mathbf{K}^n$ - $\dim$ Im $\tilde{A}$

$=$ n - $\text{rank}$ A.

$\Box$

### Định lý 9.2 Giả sử L là không gian vécto con gồm các nghiệm của hệ phương

trình tuyến tính thuần nhất Ax $=$ 0, và $x<sup>0</sup>$ là một nghiệm của hệ Ax $= \beta$. Khi đó



tâp hợp các nghiệm của hệ Ax $= \beta$ là

$x^{0}$ + L $= \{x^{0}$ + $\alpha$ | $\alpha \in L\}$.

Chứng minh: $y^0$ là một nghiệm của hệ Ax $= \beta$ nếu và chỉ nếu $y^0$ - $x^0$ là một

nghiệm của hệ Ax $=$ 0, tức là nếu và chỉ nếu $y^0$ - $x^0 \in$ L. Bao hàm thức cuối cùng

tương đương với $y^0 \in x^0$ + L.

$\Box$

### Định nghĩa 9.3 Với các giả thiết của định lý trên, x^0 được gọi là một nghiệm

riêng của hệ phương trình tuyến tính không thuần nhất Ax $= \beta$. Còn $x^0$ + $\alpha$, với

$\alpha \in$ L, được gọi là nghiệm tổng quát của hệ phương trình đó.

### Định lý 9.4 (Tiêu chuẩn Kronecker - Capelli). Hệ phương trình tuyến tính Ax = \beta

có nghiệm khi và chỉ khi rankA $= \text{rank}$ A, trong đó

$ \overline{A} = \left( \begin{array}{cccc} a_{11} & a_{12} & \ldots & a_{1n} & b_{1} \ . & . & . & . & . \ a_{m1} & a_{m2} & \ldots & a_{mn} & b_{m} \end{array} \right) $

là ma trận các hệ số mở rộng của hệ.

Chứng minh: Gọi $\alpha_j$ là vécto cột thứ j của A, còn $\beta$ là vécto cột tự do (tức là

cột cuối cùng của A. Ta có

rankA $= \text{rank}(\alpha_1$, ..., $\alpha_n) \leq \text{rank}(\alpha_1$, ..., $\alpha_n$, $\beta) = \text{rank}\overline{A}$.

Dấu bằng xảy ra nếu và chỉ nếu $\beta$ biểu thị tuyến tính qua các vécto $\alpha_1$, ..., $\alpha_n$. Gọi

$x_1^0$, ..., $x_n^0$ là các hệ số của biểu thị đó, tức là

$\beta = x_1^0 \alpha_1$ + $\cdots$ + $x_n^0 \alpha_n$.

Hệ thức này tương đương với $việcx^0=(x_1^0,...,x_n^0)^tlà$ một nghiệm của hệ phương

trình Ax $= \beta$.

$\Box$



Bài tâp

Thực hiện các phép nhân sau đây, viết các phép thể thu được thành tích của

những xích rời rạc và tính dấu của chúng.

$ 1. \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 2 & 4 & 5 & 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 5 & 1 & 2 \end{pmatrix}. $

$ 2. \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 4 & 1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 1 & 5 & 2 \end{pmatrix}. $

3. $(1,2)(2,3)\cdots(n,n-1)$.

4. $(1,2,3)(2,3,4)(3,4,5)\cdots$ (n-2,n-1,n).

5. Cho hai cách sắp thành dãy $a_1$, $a_2$, ..., $a_n$ và $b_1$, $b_2$, ..., $b_n$ của $n<br/>$ số tự nhiên đầu

tiên. Chứng minh rằng có thể đưa cách sắp này về cách sắp kia bằng cách sử

dụng không quá n-1 phép thế sơ cấp.

6. Với giả thiết như bài trên, chứng minh rằng có thể đưa cách sắp này về cách

sắp kia bằng cách sử dụng không $quá\sqrt{n-1}/2phép$ chuyển vị trí của hai

phần tử đứng kề nhau.

7. Cho ví dụ về một cách sắp n số tự nhiên đầu tiên thành dãy sao cho dãy này

không thể đưa về dãy sắp tự nhiên bằng cách dùng ít hơn n-1 phép thế sơ

cấp.

8. Biết số nghịch thế của dãy $a_1$, $a_2$, ..., $a_n$ bằng k. Hãy tìm số nghịch thế của

$d\tilde{a}y \ a_n$, $a_{n-1},...$, $a_1$.

9. Tính các định thức sau đây

$ (a) \begin{vmatrix} 2 & -5 & 4 & 3 \\ 3 & -4 & 7 & 5 \\ 4 & -9 & 8 & 5 \\ -3 & 2 & -5 & 3 \end{vmatrix}, (b) \begin{vmatrix} 3 & -3 & -2 & -5 \\ 2 & 5 & 4 & 6 \\ 5 & 5 & 8 & 7 \\ 4 & 4 & 5 & 6 \end{vmatrix}. $



10. Tính các định thức sau đây bằng cách đưa về dạng tam giác:

$ (a) \begin{vmatrix} 1 & 2 & 3 & \ldots & n \\ -1 & 0 & 3 & \ldots & n \\ -1 & -2 & 0 & \ldots & n \\ \cdot & \cdot & \cdot & \cdots & \cdot \\ -1 & -2 & -3 & \ldots & 0 \end{vmatrix}, $

$ \begin{pmatrix} a_0 & a_1 & a_2 & \dots & a_n \\ -x & x & 0 & \dots & 0 \\ 0 & -x & x & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \end{pmatrix}, \begin{pmatrix} a_1 & a_2 & a_3 & \dots & a_n \\ -x_1 & x_2 & 0 & \dots & 0 \\ 0 & -x_2 & x_3 & \dots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \end{pmatrix}. $

$ \begin{vmatrix} 0 & 0 & 0 & \dots & x \end{vmatrix} \begin{vmatrix} 0 & 0 & \dots & x_n \end{vmatrix} $

11. Tính định thức của ma trận vuông cấp n với phần tử nằm ở hàng i cột j

$b\arg$ |i-j|.

12. Tính các định thức sau đây bằng phương pháp rút ra các nhân tử tuyến tính:

$ (a) \begin{vmatrix} 1 & 2 & 3 & \dots & n \\ 1 & x+1 & 3 & \dots & n \\ 1 & 2 & x+1 & \dots & n \\ \cdot & \cdot & \cdot & \dots & \cdot \\ 1 & 2 & 3 & \dots & x+1 \end{vmatrix}, \qquad (b) \begin{vmatrix} 1+x & 1 & 1 & 1 \\ 1 & 1-x & 1 & 1 \\ 1 & 1 & 1+y & 1 \\ 1 & 1 & 1 & 1-y \end{vmatrix}. $

13. Tính các định thức sau đây bằng cách sử dụng các quan hệ hồi qui:

$a_1b_1 \quad a_1b_2 \quad a_1b_3 \quad \dots \quad a_1b_n$ | $a_0 \quad a_1 \quad a_2 \quad \dots \quad a_n$ |

$ (a) \begin{vmatrix} a_1b_2 & a_2b_2 & a_2b_3 & \dots & a_2b_n \ a_1b_3 & a_2b_3 & a_3b_3 & \dots & a_3b_n \end{vmatrix}, $

$-y_1 x_1$ 0 ... 0

$ \begin{array}{c|cccc} (b) & 0 & -y_2 & x_2 & \dots & 0 \end{array} $

$a_1b_n a_2b_n a_3b_n$ ... $a_nb_n$

0 $\qquad$ 0 $\qquad$ 0 $\qquad$ ... $\quad x_n$



14. Tính các định thức sau đây bằng cách biểu diễn chúng thành tổng của các

$\dim$ h thức nào đó:

$ (a) \begin{vmatrix} x+a_1 & a_2 & a_3 & \dots & a_n \\ a_1 & x+a_2 & a_3 & \dots & a_n \\ a_1 & a_2 & x+a_3 & \dots & a_n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_1 & a_2 & a_3 & \dots & x+a_n \end{vmatrix}, (b) \begin{vmatrix} x_1 & a_2 & a_3 & \dots & a_n \\ a_1 & x_2 & a_3 & \dots & a_n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_1 & a_2 & a_3 & \dots & x_n \end{vmatrix}. $

Tính các định thức sau đây:

$ \begin{bmatrix} a_1 & x_1 & x_1^2 & ... & x_1^{n-1} \\ a_2 & x_2 & x_2^2 & ... & x_2^{n-1} \\ . & . & . & ... & . \\ a_n & x_n & x_n^2 & ... & x_n^{n-1} \end{bmatrix}. $

15.

$ 16. \ (a) \left|\begin{array}{cccccc} 1 & x_1^2 & x_1^3 & \ldots & x_1^n \\ 1 & x_2^2 & x_2^3 & \ldots & x_2^n \\ . & . & . & . & . \\ 1 & x_n^2 & x_n^3 & \ldots & x_n^n \end{array}\right|, \quad \  \  (b) \left|\begin{array}{cccccc} 1 & x_1 & x_1^2 & \ldots & x_1^{s-1} & x_1^{s+1} & \ldots & x_1^n \\ 1 & x_2 & x_2^2 & \ldots & x_2^{s-1} & x_2^{s+1} & \ldots & x_2^n \\ . & . & . & . & . & $

$ \begin{vmatrix} 1 & x_1(x_1 - 1) & x_1^2(x_1 - 1) & \dots & x_1^{n-1}(x_1 - 1) \\ 1 & x_2(x_2 - 1) & x_2^2(x_2 - 1) & \dots & x_2^{n-1}(x_2 - 1) \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n(x_n - 1) & x_n^2(x_n - 1) & \dots & x_n^{n-1}(x_n - 1) \end{vmatrix}. $

17.

$1+x_1 1+x_1^2$ ... $1+x_1^n$

$1+x_2 1+x_2^2$ ... $1+x_2^n$

18.

$\left|$ 1 + $x_n \right|$ 1 + $x_n^2 \dots$ 1 + $x_n^n$



1 $\cos \varphi_1 \cos 2\varphi_1$ ... $\cos(n-1)\varphi_1$ 1 $\cos \varphi_2 \cos 2\varphi_2$ ... $\cos(n-1)\varphi_2$ 1 $\cos \varphi_n \cos 2\varphi_n$ ... $\cos(n-1)\varphi_n$

19.

$ \begin{bmatrix} x_1y_1 & 1 + x_1y_2 & \dots & 1 + x_1y_n \\ 1 + x_2y_1 & x_2y_2 & \dots & 1 + x_2y_n \\ \vdots & \vdots & \dots & \vdots \\ 1 + x_ny_1 & 1 + x_ny_2 & \dots & x_ny_n \end{bmatrix}. $

20.

21. Dãy Fibonacci là dãy số bắt đầu với các số hạng 1,2 và mỗi số hạng, kể từ

số hạng thứ ba, đều bằng tổng của hai số hạng đứng ngay trước nó. Chứng

minh rằng số hạng thứ n của dãy Fibonacci bằng định thức cấp n sau đây:

$ \begin{bmatrix} 1 & 1 & 0 & 0 & \dots & 0 & 0 \ -1 & 1 & 1 & 0 & \dots & 0 & 0 \ 0 & -1 & 1 & 1 & \dots & 0 & 0 \ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots $

$ \begin{vmatrix}\n(a_1 + b_1)^{-1} & (a_1 + b_2)^{-1} & \dots & (a_1 + b_n)^{-1} \\
(a_2 + b_1)^{-1} & (a_2 + b_2)^{-1} & \dots & (a_2 + b_n)^{-1} \\
\vdots & \vdots & \ddots & \vdots \\
(a_n + b_1)^{-1} & (a_n + b_2)^{-1} & \dots & (a_n + b_n)^{-1}\n\end{vmatrix}. $

22.

23. Tính định thức sau đây bằng cách viết nó thành tích của hai định thức:

$ \begin{vmatrix} s_0 & s_1 & s_2 & \dots & s_{n-1} & 1 \end{vmatrix} $

$s_3$ ... $s_n$

$S_1$

$s_2$

$s_3 s_4$ ... $s_{n+1} x^2$

$S_2$

$s_n s_{n+1} s_{n+2}$ ... $s_{2n-1} x^n$



trong đó $s_k = x_1^k$ + $x_2^k$ + $\cdots$ + $x_n^k$.

24. Chứng minh rằng

$ \begin{vmatrix}\na_1 & a_2 & a_3 & \dots & a_n \\
a_n & a_1 & a_2 & \dots & a_{n-1} \\
a_{n-1} & a_n & a_1 & \dots & a_{n-2} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a_2 & a_3 & a_4 & \dots & a_1\n\end{vmatrix} = f(\varepsilon_1) f(\varepsilon_2) \cdots f(\varepsilon_n), $

trong đó f(X) $= a_1$ + $a_2X$ + $\cdots$ + $a_nX^{n-1}$ và $\varepsilon_1$, $\varepsilon_2$, ..., $\varepsilon_n$ là các căn bậc n

khác nhau của 1.

25. Dùng khai triển Laplace chứng minh rằng nếu một định thức cấp n có các

phần tử nằm trên giao của k hàng và $\ell$ cột xác định nào đó đều bằng 0, trong

đó k + $\ell >$ n, thì định thức đó bằng 0.

26. Giải hệ phương trình sau đây bằng phương pháp Cramer và phương pháp

khử:

$3x_1$ + $4x_2$ + $x_3$ + $2x_4$ + 3 $=$ 0

$3x_1$ + $5x_2$ + $3x_3$ + $5x_4$ + 6 $=$ 0

$6x_1$ + $8x_2$ + $x_3$ + $5x_4$ + 8 $=$ 0

$3x_1$ + $5x_2$ + $3x_3$ + $7x_4$ + 8 $=$ 0.

27. Chứng minh rằng một đa thức bậc n trong K[X] được hoàn toàn xác định

bởi giá trị của nó tại (n + 1) điểm khác nhau của trường K. Tìm ví dụ về

hai đa thức khác nhau cùng bậc n nhận các giá trị bằng nhau tại mọi điểm

của $\mathbf{K}$, nếu số phần tử của $\mathbf{K}$ không vượt quá n.

Giải các hệ phương trình sau đây bằng phương pháp thích hợp:



28.

ax + by + cz + dt $=$ p

-bx + ay + dz - ct $=$ q

-cx - dy + az + bt $=$ r

-dx + cu - bz + at $=$ s.

$x_n$ + $a_1 x_{n-1}$ + $a_1^2 a_{n-2}$ + $\cdots$ + $a_1^{n-1} x_1$ + $a_1^n =$ 0,

29.

$x_n$ + $a_2 x_{n-1}$ + $a_2^2 a_{n-2}$ + $\cdots$ + $a_2^{n-1} x_1$ + $a_2^n =$ 0,

. . . . . . . . . . . . . . . . . . . .

$x_n$ + $a_n x_{n-1}$ + $a_n^2 a_{n-2}$ + $\cdots$ + $a_n^{n-1} x_1$ + $a_n^n =$ 0.

30. Đặt $s_n(k) = 1^n$ + $2^n$ + $\cdots$ + $(k-1)^n$. Hãy thiết lập phương trình

$k^{n} =$ 1 + $C_{n}^{n-1} s_{n-1}(k)$ + $\cdots$ + $C_{n}^{1} s_{1}(k)$ + $s_{0}(k)$

và chứng minh rằng

$ s_{n-1}(k)=\frac{1}{n!}\left|\begin{array}{cccccc} k^n & C_n^{n-2} & C_n^{n-3} & \ldots & C_n^1 & 1\\ k^{n-1} & C_{n-1}^{n-2} & C_{n-1}^{n-3} & \ldots & C_{n-1}^1 & 1\\ k^{n-2} & 0 & C_{n-2}^{n-3} & \ldots & C_{n-2}^1 & 1\\ . & . & . & . & . & . & .\\ . & . & . & . & . & .\\ . & . & . & . & . & .\\ . & . & . & . & . & .\\ . & . & . & . & . & .\\ . & . & . & . & . & .\\ . & . & . $

31. Xét khai triển $\frac{x}{e^x-1} =$ 1 + $b_1x$ + $b_2x^2$ + $b_3x^3$ + $\cdots$ Ta đặt $b_{2n} = \frac{(-1)^{n-1}B_n}{(2n)!}$, trong

đó $B_n$ được gọi là số Bernoulli thứ n. Chứng minh rằng

$ B_n = (-1)^{n-1}(2n)! \begin{array}{|l|}\n\frac{1}{2!} & 1 & 0 & 0 & \dots & 0 \\
\frac{1}{3!} & \frac{1}{2!} & 1 & 0 & \dots & 0 \\
\frac{1}{4!} & \frac{1}{3!} & \frac{1}{2!} & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
\frac{1}{(2n+1)!} & \frac{1}{(2n)!} & \frac{1}{(2n-1)!} & \frac{1}{(2n-2)!} & \dots & \frac{1}{2!}\n\end{array} $



và chỉ ra rằng

$ b_{2n-1}=\left|\begin{array}{cccccc} \frac{1}{2!} & 1 & 0 & 0 & \ldots & 0 \\[0.3em] \frac{1}{3!} & \frac{1}{2!} & 1 & 0 & \cdots & 0 \\[0.3em] \frac{1}{4!} & \frac{1}{3!} & \frac{1}{2!} & 1 & \ldots & 0 \\[0.3em] \ddots & \ddots & \ddots & \ddots & \cdots & \vdots \\[0.3em] \frac{1}{(2n)!} & \frac{1}{(2n-1)!} & \frac{1}{(2n-2)!} & \frac{1}{(2n-3)!} & \cdots & \frac{1}{2!} $

với mọi n $>$ 1.

32. Diễn đạt hệ số $a_n$ trong khai triển

$e^{-x} =$ 1 - $a_1x$ + $a_2x^2$ - $a_3x^3$ + $\cdots$

như một định thức cấp n, từ đó tính định thức thu được.

33. Không dùng ma trận, hãy chứng minh trực tiếp rằng $\det(f^*) = \det(f)$, trong

đó $f^*$ là đồng cấu đối ngẫu của f, với mọt tự đồng cấu f: V $\to$ V.

34. Tính hạng của các ma trận sau đây bằng phương pháp biến đổi sơ cấp và

phương pháp dùng định thức con:

$ (a) \begin{pmatrix} 2 & -1 & 3 & -2 & 4 \\ 4 & -2 & 5 & 1 & 7 \\ 2 & -1 & 1 & 8 & 2 \end{pmatrix}, (b) \begin{pmatrix} 3 & -1 & 3 & 2 & 5 \\ 5 & -3 & 2 & 3 & 4 \\ 1 & -3 & -5 & 0 & -7 \\ 7 & -5 & 1 & 4 & 1 \end{pmatrix}. $

35. Tìm giá trị của $\lambda$ sao cho ma trận sau đây có hạng thấp nhất

$ \begin{pmatrix} 3 & 1 & 1 & 4 \end{pmatrix} $

$\lambda$ 4 10 1

$ \begin{array}{ccc} 1 & 7 & 17 & 3 \end{array} $

$\overline{3}$

$\overline{2}$

$\overline{2}$



36. Tìm hạng của ma trận sau đây như một hàm phụ thuộc $\lambda:$

$ \left(\begin{array}{ccc} 1 & \lambda & -1 & 2 \\ 2 & -1 & \lambda & 5 \\ 1 & 10 & -6 & 1 \end{array}\right). $

37. Chứng minh rằng nếu hạng của một ma trận bằng r thì mỗi định thức con

nằm trên giao của bất kỳ r hàng độc lập tuyến tính và r cột độc lập tuyến

tính của ma trận đó đều khác 0.

38. Cho Alà một ma trận vuông cấp n $>$ 1 và $\tilde{A}$ là ma trận phụ hợp (gồm những

phần bù đại số của các phần tử) của A. Hãy xác định $rank\tilde{A}$ như một hàm

cua rankA.

39. Chứng minh rằng nếu các véctơ

$\alpha_i = (a_{i1}$, $a_{i2}$, ..., $a_{in}) \in \mathbf{R}_n \quad$ (i $=$ 1, 2, ..., s; s $\leq$ n),

thoả mãn điều kiện $|a_{jj}| > \sum_{i \neq j} |a_{ij}|$, thì chúng độc lập tuyến tính.

40. Chứng minh rằng nếu A và B là các ma trận cùng số hàng và số cột thì

rank(A + B) $\leqrank(A)$ + rank(B).

41. Chứng minh rằng mỗi ma trận có hạng r có thể viết thành tổng của r ma

trận có hạng 1, nhưng không thể viết thành tổng của một số ít hơn r ma trận

$\overline{\text{co}}$ hang 1.

42. Chứng minh bất đẳng thức Sylvester cho các ma trận vuông cấp n bất kỳ A

và B:

rank(A) + rank(B) - n $\le$ rank(AB) $\le min\{rank(A)$, $rank(B)\}$.

43. Chứng minh rằng nếu A là một ma trận vuông cấp n sao cho $A^2 =$ E, thì

rank(A + E) + rank(A - E) $=$ n.



44. Tìm ma trận nghịch đảo của các ma trận sau đây bằng phương pháp định

thức và phương pháp biến đổi sơ cấp:

$ (a) \begin{pmatrix} 0 & 1 & 3 \\ 2 & 3 & 5 \\ 3 & 5 & 7 \end{pmatrix}, (b) \begin{pmatrix} 1 & 2 & -1 & -2 \\ 3 & 8 & 0 & -4 \\ 2 & 2 & -4 & -3 \\ 3 & 8 & -1 & -6 \end{pmatrix}. $

Nghiên cứu tính tương thích của các hệ phương trình sau, tìm một nghiệm

riêng và nghiệm tổng quát của chúng:

3x - 2y + 5z + 4t $=$ 2

45.

6x - 4y + 4z + 3t $=$ 3,

9x - 6y + 3z + 2t $=$ 4.

8x + 6y + 5z + 2t $=$ 21,

46.

3x + 3y + 2z + t $=$ 10,

4x + 2y + 3z + t $=$ 8,

3x + 5y + z + t $=$ 15,

7x + 4y + 5z + 2t $=$ 18.



# Chương IV

CẤU TRÚC CỦA TƯ ĐỒNG CẤU

Mục đích của chương này là tìm cho mỗi tự đồng cấu (trong trường hợp có thể

được) một cơ sở của không gian, sao cho trong cơ sở đó tự đồng cấu có ma trận

đơn giản, cụ thể là càng gần ma trận chéo càng tốt.

Véctơ riêng và giá trị riêng

$\mathbf$ 1

Giả sử V là một không gian vécto trên trường K, và f: V $\to$ V là một tự đồng

cấu của V. Việc nghiên cứuf trên toàn không gian V đôi khi gặp khó khăn, vì V

quá lớn. Người ta muốn tránh điều đó bằng cách hạn chế f lên một số không gian

con nào đó U của V. Nhưng để cho hạn chế đó vẫn còn là một tự đồng cấu của U

thì không gian con này phải có tính chất đặc biệt nói trong định nghĩa sau đây.

### Định nghĩa 1.1 Không gian véctor con U của V được gọi là một không gian con

ổn định đối với f (hay một không gian con f-ổn định) nếu f(U) $\subset$ U.

Đôi khi người ta cũng nói cho gọn rằng U là một không gian con ổn định, nếu

f đã rõ.

Một số tài liệu dùng thuật ngữ không gian con bất biến trong trường hợp này.

Chúng tôi cho rằng thuật ngữ không gian con ổn định chính xác hơn. Còn thuật

ngữ không gian con bất biến đối với f dùng để chỉ không gian con sau đây:

$V^f := \{v \in$ V | f(v) $= v\}$.

Đối với tự đồng cấu f: V $\to$ V bất kỳ, các không gian con sau đây đều là f-ổn

dinh: $\{0\}$, V, Ker f, Im f.



Nếu may mắn có các không gian con f-ổn định $U_1$ và $U_2$ sao cho V $= U_1 \oplus U_2$,

thì $f_1 = f|_{U_1}$ và $f_2 = f|_{U_2}$ đều là các tự đồng cấu. Mỗi vécto v $\in$ V có thể viết duy

nhất dưới dạng v $= u_1$ + $u_2$, trong đó $u_1 \in U_1$, $u_2 \in U_2$, và

f(v) $= f(u_1)$ + $f(u_2)$.

Khi đó việc nghiên cứu tự đồng cấu f trên V có thể qui về việc nghiên cứu các

tự đồng cấu $f_i$ của $U_i$ (i $=$ 1, 2). Nói rõ hơn, nếu $f_1$ có ma trận A trong cơ sở

$(e_1$, ..., $e_m)$ của $U_1$, và $f_2$ có ma trận B trong cơ sở $(e_{m+1}$, ..., $e_n)$ của $U_2$, thì f có

ma trận

$ \left(\begin{array}{c|c} A & 0 \\ \hline 0 & B \end{array}\right) $

trong cơ sở $(e_1$, ..., $e_m$, $e_{m+1}$, ..., $e_n)$ của V. Như thế,

$\det$ f $= \det f_1 \cdot \det f_2$.

Nói riêng, f là một đẳng cấu tuyến tính nếu và chỉ nếu $f_1$ và $f_2$ cùng là các đẳng

cấu tuyến tính.

Tuy vậy, một không gian con ổn định nói chung không có phần bù tuyến tính

cũng là một không gian con ổn định. Sau đây là một ví dụ.

Giả sử V là một không gian vécto 2 chiều trên $\bf{K}$ với một cơ sở gồm hai vécto

$\alpha$ và $\beta$. Tự đồng cấu f: V $\to$ V được xác định bởi $f(\alpha) =$ 0, $f(\beta) = \alpha$. Khi đó

U $= \mathcal{L}(\alpha)$ là không gian con f-ổn định một chiều duy nhất của V. Độc giả hãy tự

chứng minh điều này xem như một bài tập.

Một câu hỏi được đặt ra là làm thế nào để tìm các không gian con ổn định đối

với một tự đồng cấu đã cho? Đáng tiếc là không có một phương pháp chung nào

để làm điều đó trong trường hợp tổng quát.

Sau đây ta sẽ xét một trường hợp riêng đặc biệt thú vị, có nhiều ứng dụng

trong Vật lý và Cơ học. Đó là trường hợp các không gian con ổn định một chiều.

Giả sử L là một không gian con f-ổn định một chiều. Giả sử $\alpha \in$ L là một

vécto khác 0. Khi đó $(\alpha)$ là một cơ sở của L. Vì f(L) $\subset$ L, cho nên có một vô



hướng $\lambda \in \mathbf{K}$ sao cho

$f(\alpha) = \lambda \alpha$.

Ngược lại, nếu có một $véct<br/>ơ\alpha\neq$ 0và một vô $hướng\lambda\in {\bf K}sao cho<br/> f(\alpha)=\lambda\alpha$,

thì L $= \mathcal{L}(\alpha)$ là một không gian con f-ổn định một chiều. Ta đi tới định nghĩa sau

dây.

### Định nghĩa 1.2 Giả sử f là một tự đồng cấu của K-không gian vécto V. Nếu có

vécto $\alpha \neq$ 0 và vô hướng $\lambda \in \mathbf{K}$ sao cho $f(\alpha) = \lambda \alpha$, thì $\lambda$ được gọi là một giá trị

riêng của f còn $\alpha$ được gọi là một vécto riêng của f ứng với giá trị riêng $\lambda$.

Như vậy việc tìm các không gian con ổn định một chiều tuơng đương với việc

tim các vécto riêng.

Nhận xét rằng các vécto riêng của f ứng với giá trị riêng $\lambda$ cùng với vécto 0

lập nên không gian véctor con Ker(f - $\lambda id_V)$.

### Định nghĩa 1.3 Giả sử \lambda là một giá trị riêng của tự đồng cấu f: V \to V. Không

gian véctor Ker(f - $\lambda id_V)$ gồm véctor 0 và tất cả các véctor riêng của f ứng với giá

trị riêng $\lambda$ được gọi là không gian con riêng của f úng với giá trị riêng $\lambda$.

Vấn đề đặt ra là làm thế nào để tìm các vécto riêng và các giá trị riêng của

một tự đồng cấu?

Nhận xét rằng $\lambda$ là một giá trị riêng của f nếu và chỉ nếu Ker(f - $\lambda id_V) \neq \{0\}$.

Điều này tương đương $với\det(f$ - $\lambda$ i $d_V) =$ 0. Nói cách khác, $\lambdalà$ một nghiệm của

đa thức $\det(f$ - X $id_V)$ với ấn X.

Vì sao ta có thể khẳng định $\det(f$ - X $id_V)$ là một đa thức của X? Giả sử số

chiều của V bằng n, và f có ma trận là A trong một cơ sở nào đó $(e_1$, ..., $e_n)$ của

V. Khi đó đồng cấu (f - X $id_V)$ có ma trận là (A - X $E_n)$ trong cơ sở nói trên. Vì

$th\tilde{e}$

$\det(f$ - X $id_V) = \det(A$ - X $E_n)$.



Nếu $A=(a_{ij})_{n\times n}$, thì

$ det(A - XE_n) = \begin{vmatrix} a_{11} - X & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} - X & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nn} - X \end{vmatrix} $

rõ ràng là một đa thức bậc n của ẩn X.

### Định nghĩa 1.4 Đa thức bậc n của một ẩn X với hệ số trong \mathbf{K}

$P_f(X) = \det(f$ - X $id_V)$

được gọi là đa thức đặc trưng của tự đồng cấu f.

Da thức bậc n của một ẩn X với hệ số trong $\mathbf$ K

$P_A(X) = \det(A$ - X $E_n)$

được gọi là đa thức đặc trưng của ma trận A. Nghiệm của đa thức này được gọi

là giá trị riêng của A.

Những lập luận ở trên đã chứng minh mệnh đề sau đây:

Mệnh đề 1.5 Vô hướng $\lambda \in \mathbf{K}$ là một giá trị riêng của tự đồng cấu f: V $\to$ V nếu

và chỉ nếu $\lambda$ là một nghiệm của đa thức đặc trưng $\det(f$ - X $id_V) = \det(A$ - X $E_n)$

$c\mathcal{u}a$ f.

$\Box$

Trong thực hành, để tìm giá trị riêng và véctơ riêng của một tự đồng cấu f

người ta làm như sau:

Bước 1: Tìm ma trận A của f trong một cơ sở tuỳ ý $(e_1$, ..., $e_n)$ của V.

Bước 2: Tính đa thức đặc trưng $\det(A$ - X $E_n)$.

Bước 3: Giải phương trình đa thức bậc n đối với ẩn X:

$\det(A$ - X $E_n) =$ 0.



Bước 4: Giả sử $\lambda$ là một nghiệm của phương trình đó. Giải hệ phương trình tuyến

tính thuần nhất suy biến

$ \left\{\n\begin{aligned}\n(a_{11} - \lambda)x_1 + a_{12}x_2 + \dots & a_{1n}x_n & = 0 \\
a_{21}x_1 + (a_{22} - \lambda)x_2 + \dots & a_{2n}x_n & = 0 \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1}x_1 + a_{n2}x_2 + \dots & (a_{nn} - \lambda)x_n & = 0.\n\end{aligned}\n\right. $

Giả sử $x^0 = (x_1^0$, ..., $x_n^0)^t$ là một nghiệm không tầm thường của hệ này. Khi đó,

$\alpha = x_1^0 e_1$ + $\cdots$ + $x_n^0 e_nlà$ một $véc<br/>tơ$ riêng củafứng với giá trị riêng $\lambda$.

Ví dụ: Tự đồng cấu f của không gian vécto thực 3 chiều V có ma trận là

$ A = \left( \begin{array}{ccc} 4 & -5 & 2 \\ 5 & -7 & 3 \\ 6 & -9 & 4 \end{array} \right) $

trong cơ sở $(e_1$, $e_2$, $e_3)$. Hãy tìm các giá trị riêng và các vécto riêng của f.

Lời giải: Đa thức đặc trưng của f là

$ \begin{vmatrix} 4-X & -5 & 2 \\ 5 & -7-X & 3 \\ 6 & -9 & 4-X \end{vmatrix} = -X^2(X-1). $

Vậy f có các giá trị riêng là $\lambda_1 = \lambda_2 =$ 0, $\lambda_3 =$ 1.

Với $\lambda_1 = \lambda_2 =$ 0, hê phương trình

$ \begin{cases}\n4x - 5y + 2z &= 0 \\
5x - 7y + 3z &= 0 \\
6x - 9y + 4z &= 0\n\end{cases} $

có nghiệm không tầm thường x $=$ a, y $=$ 2a, z $=$ 3a trong đó a $\neq$ 0. Vậy $a(e_1$ +

$(2e_2$ + $3e_3)$ với a $\neq$ 0 là vécto riêng của f ứng với giá trị riêng bằng 0.



Với $\lambda_3 =$ 1, hê phương trình

$ \begin{cases}\n3x - 5y + 2z &= 0 \\
5x - 8y + 3z &= 0 \\
6x - 9y + 3z &= 0\n\end{cases} $

có nghiệm không tầm thường x $=$ a, y $=$ a, z $=$ a trong đó a $\neq$ 0. Vậy $a(e_1$ + $e_2$ + $e_3)$

với a $\neq$ 0 là vécto riêng của f ứng với giá trị riêng bằng 1.

Trong thuật toán 4 bước để tìm vécto riêng và giá trị riêng nói trên, bước 3 là

khó hơn cả. Nói chung, ta không biết phương trình $\det(A$ - X $E_n) =$ 0 có nghiệm

hay không, và nếu có thì tìm bằng cách nào.

Mệnh đề 1.6 Giả sử U là một không gian véctơ con ổn định đối với tự đồng cấu

f: V $\to$ V. Gọi $\bar{f}:$ V/U $\to$ V/U, $\bar{f}[\alpha] = [f(\alpha)]$ là đồng cấu cảm sinh bởi f. Khi

đó, đa thức đặc trưng của f bằng tích các đa thức đặc trưng của $f|_U$ và của f.

Chứng minh: Chọn một cơ sở bất kỳ $(e_1$, ..., $e_m)$ của U rồi bổ sung nó để nhận

được một cơ sở $(e_1$, ..., $e_m$, ..., $e_n)$ của V. Vì U là một không gian con ổn định đối

với f cho nên ma trận của f trong cơ sở nói trên có dạng

$ A = \left(\begin{array}{c|c} B & C \ \hline 0 & D \end{array}\right), $

trong đóBlà ma trận của $f|_Utrong$ cơ sở $(e_1,...,e_m)$. Vì $[e_1] = \cdots = [e_m] =$ 0

trong V/U cho nên D chính là ma trận của f trong cơ sở $([e_{m+1}]$, ..., $[e_n])$. Rõ ràng

$\det(A$ - X $E_n) = \det(B$ - X $E_m) \det(D$ - X $E_{n-m})$.

Nói cách khác, ta có

$P_f(X) = P_{f|_{U}}(X) P_{\bar{f}}(X)$.

$\Box$



Không gian con ổn định của các tự đồng cấu

$\boldsymbol{2}$

thưc và phức

Trong tiết này, ta sẽ xét hai trường hợp đặc biệt, trong đó $\bf{K}$ là trường số thực hay

trường số phức, để có thêm những thông tin bổ sung về nghiệm của các đa thức

với hệ số trong những trường ấy.

Vì mọi đa thức hệ số phức đều có nghiệm phức, nên ta có định lý sau đây.

Dinh lý 2.1 Mỗi tự đồng cấu của một không gian vécto phức đều có ít nhất một

giá trị riêng, và do đó có ít nhất một không gian con ổn định một chiều.

Chứng minh: Giả sử tự đồng cấu f: V $\to$ V của không gian vécto phức V có

ma trận là A trong một cơ sở nào đó $(e_1$, ..., $e_n)$ của V. Vì C là một trường đóng

đại số nên phương trình đa thức với hệ số phức $P_f(X) = \det(A$ - X $E_n) =$ 0 có

ít nhất một nghiệm phức, ký hiệu là $\lambda$. Xét hệ phương trình tuyến tính thuần

nhất (A - $\lambda E_n)x =$ 0, trong đó x là một ẩn vécto cột gồm n thành phần phức. Vì

$\det(A$ - $\lambda E_n) =$ 0nên hệ nói trên có nghiệm không tầm thường $x^0 = (x_1^0$, ..., $x_n^0)^t \in$

$\mathbf{C}^n$. Khi đó $\alpha = \sum_{i=1}^n x_i^0 e_i$ là một vécto riêng ứng với giá trị riêng $\lambda$.

$\Box$

Các đa thức hệ số thực có thể không có nghiệm thực, nhưng luôn luôn có nghiệm

phức. Điều đó là cơ sở của định lý sau đây.

### Định lý 2.2 Mỗi tự đồng cấu của một không gian vécto thực đều có ít nhất một

không gian con ổn định một hoặc hai chiều.

Chứng minh: Giả sử V là một không gian vécto thực, và tự đồng cấu f: V $\to$ V

có ma trận là A $= (a_{kj})$ trong một cơ sở nào đó $(e_1$, ..., $e_n)$ của V. Khi đó đa thức

đặc trưng $P_f(X) = \det(A$ - X $E_n)$ là một đa thức với hệ số thực.

Nếu phương trình $\det(A$ - X $E_n) =$ 0 có một nghiệm thực thì f có vécto riêng,

do đó nó có không gian con ổn định một chiều.



Trái lại, giả sử phương trình $\det(A$ - X $E_n) =$ 0 không có nghiệm thực. Gọi $\lambda =$

a+ib là một nghiệm phức không thực của nó, ở đây i là đơn vị ảo, a, b $\in \mathbf{R}$, b $\neq$ 0.

Ta xét hệ phương trình tuyến tính thuần nhất suy biến hệ số phức

(A - $\lambda E_n)z =$ 0,

trong đó z là một ẩn vécto cột gồm n thành phần. Gọi $z^0 = (z_1^0$, ..., $z_n^0)^t \in \mathbb{C}^n$ là

một nghiệm không tầm thường của hệ đó. Giả sử $z_j^0 = x_j^0$ + $iy_j^0$, (j $=$ 1, 2, ..., n).

Ta có

$\sum_{j=1}^{n} a_{kj} z_j^0 = \lambda z_k^0$

$\iff \sum_{i=1}^n a_{ki}(x_i^0$ + $iy_i^0) = \lambda (x_k^0$ + $iy_k^0)$ (k $=$ 1, ..., n)

$ \iff \left\{\begin{array}{rcl}\sum_j a_{kj}x_j^0 & = & ax_k^0 - by_k^0\\ \sum_j a_{kj}y_j^0 & = & bx_k^0 + ay_k^0. \end{array}\right. $

Đặt $\alpha = \sum_{j=1}^n x_j^0 e_j$, $\beta = \sum_{j=1}^n y_j^0 e_j \in$ V. Các hệ thức trên tương đương với

$ \begin{cases}\nf(\alpha) = a\alpha - b\beta \\
f(\beta) = b\alpha + a\beta.\n\end{cases} $

Nghĩa là L $= \mathcal{L}(\alpha$, $\beta)$ là một không gian con ổn định của f. Ta khẳng định rằng

$\dim \mathcal{L}(\alpha$, $\beta) =$ 2. Giả sử trái lại dim $\mathcal{L}(\alpha$, $\beta) \neq$ 2. Vì $z^0 \neq$ 0, cho nên hoặc $\alpha \neq$ 0

hoặc $\beta \neq$ 0. Do đó dim $\mathcal{L}(\alpha$, $\beta) =$ 1. Như thế L là một không gian con f-ổn định

một chiều, nói cách khác f có một giá trị riêng thực. Điều này mâu thuẫn với giả

thiết phương trình đặc trưng $\det(A$ - X $E_n) =$ 0 không có nghiệm thực.

$\Box$

Mệnh đề 2.3 Mỗi tự đồng cấu của một không gian vécto thực số chiều lẻ đều có

ít nhất một không gian con ổn định một chiều.

Chứng minh: Nếu không gian vécto V có số chiều n lẻ, thì đa thức đặc trưng

$P_f(X)$ của mỗi tự đồng cấu f cũng có bậc lẻ, cụ thể là bằng n. Do đó đa thức này

có ít nhất một nghiệm thực. Thật vậy, giả sử trái lại $P_f(X)$ không có một nghiệm



thực nào. Nhận xét rằng nếu z $=$ a + ib là một nghiệm của $P_f(X)$ thì liên hợp phức

của nó $\bar{z} =$ a - ib cũng vậy. Hai nghiệm này phân biệt, vì z không là một số thực.

Như vậy, n nghiệm phức của $P_f(X)$ được ghép thành từng cặp liên hợp với nhau.

Vì thế n là một số chẵn. Điều này mâu thuẫn với giả thiết.

Ta đã chứng minh đa thức đặc trưng $P_f(X)$ có ít nhất một nghiệm thực. Vậy

f có ít nhất một giá trị riêng thực. Do đó, nó có ít nhất một không gian con ổn

định một chiều.

$\Box$

Ví dụ: Phép quay mặt phẳng $\mathbb{R}^2$ xung quanh gốc tọa độ một góc $\varphi$ có ma trận

trong cơ sở chính tắc là

$ A = \left( \begin{array}{cc} \cos \varphi & -\sin \varphi \\ \sin \varphi & \cos \varphi \end{array} \right). $

Da thức đặc trưng của phép quay này là

$ \begin{vmatrix} \cos \varphi - X & -\sin \varphi \\ \sin \varphi & \cos \varphi - X \end{vmatrix} = (\cos \varphi - X)^2 + \sin^2 \varphi = X^2 - 2\cos \varphi X + 1. $

Biệt thức $\Delta' = \cos^2 \varphi$ - 1 $= -\sin^2 \varphi <$ 0 nếu $\varphi \neq k\pi$. Vì thế, phép quay mặt phẳng

$\mathbb{R}^2$ xung quanh gốc tọa độ một góc $\varphi$ không có vécto riêng nếu $\varphi \neq k\pi$.

Tuy nhiên, nếu ta xét tự đồng cấu f của $\mathbb{C}^2$ cũng có ma trận là A trong cơ sở

chính tắc, thì đa thức đặc trưng của f cũng là đa thức nói trên. Vậy f có hai giá

$ trị riêng phức là\lambda_{1,2}=\cos\varphi\pm i\sin\varphi. Dễ thấy rằng\left(\begin{array}{c}1\\ \pm i\end{array}\right) là các véc<br/>tơ riêng của $

f ứng với các giá trị riêng nói trên.

Tự đồng cấu chéo hoá được

$\boldsymbol{3}$

Chúng ta vẫn giả sử V là một không gian vécto trên trường $\mathbf$ K.

### Định nghĩa 3.1 Tự đồng cấu f của không gian vécto V được gọi là chéo hoá được

nếu có một cơ sở của V gồm toàn những véctơ riêng của f. Nói cách khác, f chéo

hoá được nếu ma trận của nó trong một cơ sở nào đó của V là một ma trận chéo.



Gọi A $\in$ M(n $\times$ n, $\mathbf{K})$ là ma trận của f trong một cơ sở bất kỳ của V. Từ định

nghĩa ta suy ngay ra rằng f là chéo hoá được nếu và chỉ nếu có một ma trận khả

nghịch C $\in$ M(n $\times$ n, $\mathbf{K})$ sao cho $C^{-1}AC$ là một ma trận chéo. Nói cách khác, f là

chéo hoá được nếu và chỉ nếu A đồng dạng (trên $\mathbf{K})$ với một ma trận chéo.

### Định nghĩa 3.2 Ma trận A \in M(n \times n, \mathbf{K}) đồng dạng (trên K) với một ma trận

chéo được gọi là chéo hoá được (trên K).

Theo định nghĩa, A chéo hoá được nếu và chỉ nếu mọi ma trận đồng dạng với

nó cũng chéo hoá được.

Việc tìm một cơ sở (nếu có) của V gồm toàn những vécto riêng của f được gọi

là việc chéo hoá tự đồng cấu f.

Việc tìm một ma trận khả nghịch C (nếu có) sao cho $C^{-1}AC$ là một ma trận

chéo được gọi là việc chéo hoá ma trận A.

### Định lý sau đây sẽ cho một điều kiện đủ cho sự chéo hoá.

Dinh lý 3.3 Gid sử $\alpha_1$, ..., $\alpha_k$ là các vécto riêng của tự đồng cấu f: V $\to$ V ứng

với những giá trị riêng đôi một khác nhau $\lambda_1$, ..., $\lambda_k$. Khi đó, các vécto $\alpha_1$, ..., $\alpha_k$

$\hat{d}\hat{o}c$ lập tuyến tính.

Chứng minh: Định lý được chứng minh bằng quy nạp theo k.

Với k $=$ 1, vécto riêng $\alpha_1 \neq$ 0, nên hệ chỉ gồm một vécto $\alpha_1$ độc lập tuyến tính.

Giả sử quy nạp rằng định lý đã được chứng minh cho hệ gồm k-1 vécto. Bây giờ

ta giả sử có một ràng buộc tuyến tính

$a_1\alpha_1$ + $\cdots$ + $a_k\alpha_k =$ 0,

trong đó $a_1$, ..., $a_k \in \mathbf{K}$. Tác động f vào hai vế của đẳng thức trên, ta nhận được

$a_1 f(\alpha_1)$ + $\cdots$ + $a_k f(\alpha_k) = a_1 \lambda_1 \alpha_1$ + $\cdots$ + $a_k \lambda_k \alpha_k =$ 0.

Nhân đẳng thức thứ nhất với $\lambda_k$ rồi trừ vào đẳng thức thứ hai, ta có

$a_1(\lambda_1-\lambda_k)\alpha_1+\cdots+a_{k-1}(\lambda_{k-1}-\lambda_k)\alpha_{k-1}=0$.



Theo giả thiết quy nạp, các vécto $\alpha_1$, ..., $\alpha_{k-1}$ độc lập tuyến tính, cho nên

$a_1(\lambda_1$ - $\lambda_k) = \cdots = a_{k-1}(\lambda_{k-1}$ - $\lambda_k) =$ 0.

Từ đó, do $\lambda_i$ - $\lambda_k \neq$ 0 (i $=$ 1, ..., k - 1), nên

$a_1 = \cdots = a_{k-1} =$ 0.

Thay các giá trị đó vào đẳng thức đầu tiên, ta thu được $a_k \alpha_k =$ 0. Vì vécto riêng

$\alpha_k \neq$ 0, nên $a_k =$ 0.

Tóm lại $a_1 = \cdots = a_{k-1} = a_k =$ 0. Điều này chứng tỏ hệ vécto $\alpha_1$, ..., $\alpha_k$ là một

hệ độc lập tuyên tính.

$\Box$

Hệ quả 3.4 Giả sử $V_1$, ..., $V_k$ là các không gian con riêng của tự đồng cấu f:

V $\rightarrow$ V úng với những giá trị riêng đôi một khác nhau $\lambda_1$, ..., $\lambda_k$. Khi đó, tổng

$V_1$ + $\cdots$ + $V_k$ là một tổng trực tiếp.

Chứng minh: Theo định lý trên

$V_i \cap (\sum_{j \neq i} V_j) = \{0\},\$

với mọi i $=$ 1, ..., k. Vậy, tổng $V_1$ + $\cdots$ + $V_k$ là một tổng trực tiếp.

$\Box$

Hệ quả 3.5 (i) Nếu dim V $=$ n và tự đồng cấu f : V $\to$ V có n giá trị riêng đôi

$m\delta$ t khác nhau, thì f chéo hoá được.

(ii) Nếu ma trận A $\in$ M(n $\times$ n, $\mathbf{K})$ có n giá trị riêng đôi một khác nhau trong $\mathbf{K}$,

thì A chéo hoá được trên $\mathbf$ K.

Chứng minh: Gọi $\alpha_1$, ..., $\alpha_n$ là hệ gồm n vécto riêng ứng với n giá trị riêng đôi

một khác nhau của f. Theo định lý trên, đó là một hệ độc lập tuyến tính. Vì dim V

đúng bằng số véctơ của hệ, cho nên hệ này lập nên một cơ sở của V. Như vậy f

và ma trận của nó trong cơ sở bất kỳ của V chéo hoá được.

$\Box$



Nhận xét: Hệ quả nói trên chỉ nêu một điều kiện đủ, mà không phải là điều kiện

cần cho sự chéo hoá. Thật vậy, tự đồng cấu f $= id_V$ có giá trị riêng $\lambda =$ 1 với bội

n, nhưng $id_V$ đương nhiên chéo hoá được.

### Định lý sau đây là một thái cực khác của điều kiện đủ cho sự chéo hoá. Nó chỉ

ra rằng mọi phép chiếu lên một không gian con nào đó đều chéo hoá được, mặc

dù các phép chiếu này chỉ có thể có các giá trị riêng bằng 0 hoặc 1, thường là với

bội rất lớn. Định lý này cũng đồng thời cho một tiêu chuẩn để nhận biết các phép

chiếu.

### Dịnh lý 3.6 Giả sử tự đồng cấu f: V \to V có tính chất f^2 = f. Khi đó f chéo

$ho\ \tilde{a} \ d\boldsymbol{u} \sigma$ c.

Chứng minh: Đặt U $=$ Imf và W $=$ Kerf. Ta sẽ chứng minh rằng V $=$ U $\oplus$ W

và f $= pr_U$ là phép chiếu từ V lên U theo phương W. Trước hết, nhắc lại rằng

U và W là các không gian con f-ổn định. Giả sử $\alpha \in$ U $\cap$ W. Vì $\alpha \in$ W, nên

$f(\alpha) =$ 0. Mặt khác $\alpha \in$ U $=$ Imf, nên $\alpha = f(\beta)$ với $\beta$ nào đó thuộc V. Ta có

$f(\alpha) = f(f(\beta)) = f^2(\beta) = f(\beta) = \alpha$. Kết hợp hai sự kiện trên, ta có $\alpha = f(\alpha) =$ 0.

Vậy U $\cap$ W $= \{0\}$.

Mỗi vécto $\gamma \in$ V đều có thể phân tích

$\gamma = f(\gamma)$ + $(\gamma$ - $f(\gamma))$,

trong đó $f(\gamma) \in$ U và $\gamma$ - $f(\gamma) \in$ W. Thậy vậy,

$f(\gamma$ - $f(\gamma)) = f(\gamma)$ - $f^2(\gamma) = f(\gamma)$ - $f(\gamma) =$ 0.

Tóm lại, ta đã chứng minh rằng V $=$ U $\oplus$ W.

Giả sử $(e_1$, ..., $e_m)$ là một cơ sở của U, (ở đây m $=$ 0 nếu U $= \{0\})$. Trong phần

trên ta đã chỉ ra rằng $f|_{U} = id_{U}$. Vì thế các vécto $e_{1},...,e_{m}$ đều là vécto riêng của

f ứng với giá trị riêng bằng 1.



Giả sử $(e_{m+1},...,e_n)$ là một cơ sở của W, (ở đây $n-m=0$ nếu W $= \{0\})$. Vì

W $=$ Ker f, nên các véctor $e_{m+1},...,e_n$ đều là véctor riêng của f ứng với giá trị riêng

$b\mathrm{ång}$ 0.

Bởi vì V $=$ U $\oplus$ W, cho nên $(e_1$, ..., $e_m$, $e_{m+1}$, ..., $e_n)$ là một cơ sở của V gồm toàn

những vécto riêng của f. Điều này có nghĩa là f chéo hoá được.

$\Box$

Dinh lý sau đây đưa ra điều kiện cần và đủ cho sự chéo hoá.

### Dịnh lý 3.7 Tự đồng cấu f của \mathbf{K}-không gian véctơ n chiều V chéo hoá được nếu

và chỉ nếu hai điều kiện sau đây được thoả mãn:

Da thức đặc trung của f có đủ nghiệm trong trường $\mathbf{K}:$

$\left( \iota \right)$

$P_f(X) = (-1)^n$ (X - $\lambda_1)^{s_1} \cdots$ (X - $\lambda_m)^{s_m}$,

trong đó $\lambda_1$, ..., $\lambda_m$ là các vô hướng đôi một khác nhau trong K.

(ii) rank(f - $\lambda_i id_V) =$ n - $s_i$ (với i $=$ 1, ..., m).

Chứng minh: Giả sử f chéo hoá được. Cụ thể hơn, giả sử ma trận của f trong

một cơ sở nào đó của V là một ma trận chéo D với $s_1$ phần tử trên đường chéo

bằng $\lambda_1$, ..., $s_m$ phần tử trên đường chéo bằng $\lambda_m$, trong đó $\lambda_1$, ..., $\lambda_m$ đôi một khác

nhau, và n $= s_1$ + $\cdots$ + $s_m$. Khi đó

$P_f(X) = P_D(X) = (\lambda_1$ - $X)^{s_1} \cdots (\lambda_m$ - $X)^{s_m}$

$= (-1)^n$ (X - $\lambda_1)^{s_1} \cdots$ (X - $\lambda_m)^{s_m}$.

Nhận xét rằng ma trận (D - $\lambda_i E_n)$ là một ma trận chéo, với $s_i$ phần tử trên đường

chéo bằng $\lambda_i$ - $\lambda_i =$ 0, các phần tử còn lại bằng $\lambda_j$ - $\lambda_i \neq$ 0 (với j $\neq$ i nào đó). Vì

thế

rank(f - $\lambda_i id_V) =$ rank(D - $\lambda_i E_n) =$ n - $s_i$,

với i $=$ 1, ..., m.



Ngược lại, giả sử các điều kiện (i) và (ii) được thoả mãn. Xét không gian con

riêng của f ứng với giá trị riêng $\lambda_i$ : $V_i =$ Ker(f - $\lambda_i id_V)$ (i $=$ 1, ..., m). Ta có

$\dim V_i = \dim$ Ker(f - $\lambda_i id_V) =$ n - $\operatorname{rank}(f$ - $\lambda_i id_V) = s_i$.

Theo Hệ quả 3.4, tổng $V_1$ + $\cdots$ + $V_m$ là một tổng trực tiếp, với số chiều bằng

$s_1$ + $\cdots$ + $s_m =$ n. Vậy tổng đó bằng toàn bộ không gian V:

V $= V_1 \oplus V_2 \oplus \cdots \oplus V_m$.

Lấy một cơ sở bất kỳ $(e_{i1},...,e_{is_i})$ của $V_i$ (với i $=$ 1,...,m). Khi đó $(e_{11},...,e_{1s_1},...,e_{1s_i})$

$(e_{m1},...,e_{ms_m})$ là một cơ sở của V gồm toàn những véctơ riêng của f. Như vậy f

chéo hoá được.

$\Box$

Tự đồng cấu lũy linh

$\overline{4}$

Không phải bất kỳ tự đồng cấu nào cũng chéo hoá được. Tuy thế, với những giả

thiết nhẹ, người ta có thể đưa ma trận của một tự đồng cấu về một dạng rất gần

với dạng chéo, được gọi là dạng chuẩn tắc Jordan. Đối với mỗi tự đồng cấu, dạng

này được xác định duy nhất, sai kém thứ tự của các khối khác 0 trên đường chéo.

Cho f: V $\to$ V là một tự đồng cấu của V. Giả sử ta có phân tích V $=$

$V_1 \oplus \cdots \oplus V_r$, trong đó mỗi $V_i$ là một không gian con f-ổn định. Giả sử thêm rằng

tự đồng cấu $f|_{V_i}$ có ma trận là $J_i$ trong cơ sở $(e_{i1},...,e_{is_i})$ của $V_i$. Khi đó, ma trận

của ftrong cơ sở $(e_{11},...,e_{1s_1},...,e_{r1},...,e_{rs_r})$ của V có dạng (đường) chéo khối sau

$\overline{\phantom{a}}$



đây, được gọi là tổng trực tiếp của các ma trận $J_1$, ..., $J_r:$

$ J_1 \oplus \cdots \oplus J_r := \left( \begin{array}{cccccc} J_1 &| & 0 &| & \ldots & 0 \ -- & . & - & . & \ldots & \ 0 &| & J_2 &| & \ldots & 0 \ -- & . & -- & . & \ldots & \ \cdot & \cdot & \cdot & \cdot & \cdot \ \cdot & \cdot & \cdot & \cdot & \cdot \ \cdot & \cdot & \cdot $

Trong tiết này, chúng ta sẽ nghiên cứu một lớp các tự đồng cấu f mà ma trận

của nó trong một cơ sở nào đó có dạng chéo khối như trên, với các khối $J_i$ thật

"đơn giản". Đó là lớp các tự đồng cấu luỹ linh.

### Định nghĩa 4.1 (i) Tự đồng cấu \varphi của K-không gian vécto V được gọi là lũy

linh nếu có số nguyên dương k sao cho $\varphi^k =$ 0. Nếu thêm vào đó $\varphi^{k-1} \neq$ 0,

thì k được gọi là bậc lũy linh của $\varphi$.

(ii) Cơ sở $(e_1,...,e_n)$ của V được gọi là một cơ sở xyclic đối với $\varphinếu \varphi(e_1)$

$e_2$, $\varphi(e_2) = e_3$, ..., $\varphi(e_n) =$ 0.

(iii) Không gian vécto con U của V được gọi là một không gian con xyclic đối với

$\varphi$ nếu U có một cơ sở xyclic đối với $\varphi$.

Nhận xét rằng mỗi tự đồng cấu luỹ linh đều có giá trị riêng duy nhất bằng 0.

Thật vậy, giả sử $\varphi$ có bậc luỹ linh bằng k. Theo định nghĩa, tồn tại vécto $\alpha$ sao

cho $\varphi^{k-1}(\alpha) \neq$ 0 và $\varphi^k(\alpha) =$ 0. Như thế $\beta = \varphi^{k-1}(\alpha)$ chính là một vécto riêng của

$\varphi$ ứng với giá trị riêng bằng 0. Ngược lại, giả sử $\alpha$ là một vécto riêng của $\varphi$ ứng

với giá trị riêng $\lambda$. Ta có $\varphi(\alpha) = \lambda \alpha$, do đó $\varphi^k(\alpha) = \lambda^k \alpha$. Vì k là bậc luỹ linh của

$\varphi$ nên $\varphi^k =$ 0. Do đó $λ<sup>k</sup>α =$ 0. Vì α là một vécto riêng, nên α ≠ 0. Từ đó suy ra

$\lambda =$ 0.



Hơn nữa, $(e_1$, ..., $e_n)$ là một cơ sở xyelic đối với $\varphi$ nếu và chỉ nếu ma trận của

$\varphi$ trong co sở này có dạng

$ \left( \begin{array}{cccccc} 0 & 0 & 0 & ... & 0 & 0 \ 1 & 0 & 0 & ... & 0 & 0 \ 0 & 1 & 0 & ... & 0 & 0 \ . & . & . & ... & . & . \ 0 & 0 & 0 & ... & 0 & 0 \ 0 & 0 & 0 & ... & 1 & 0 \end{array} \right). $

### Định lý 4.2 Giả sử \varphi là một tự đồng cấu lũy linh của không gian vécto hữu hạn

chiều V. Khi đó, V phân tích được thành tổng trực tiếp của các không gian con

xyclic đối với $\varphi$. Hơn nữa, với mỗi số nguyên dương s, số không gian con s chiều

xyclic đối với $\varphi$ trong mọi phân tích như thế là không đổi, và bằng

$rank(\varphi^{s-1})$ – $2rank(\varphi^s)$ + $rank(\varphi^{s+1})$.

Chứng minh: Gọi k là bậc lũy linh của $\varphi$. Đặt $V_i = \varphi^{k-i}(V)$, ta thu được dãy

không gian vécto lồng nhau:

V $= V_k \supset V_{k-1} \supset \cdots \supset V_1 \supset V_0 = \{0\}$.

Ta sẽ xây dựng các không gian vécto con $V_i^j$ với 1 $\leq$ j $\leq$ i $\leq$ k có các tính chất sau

$d\hat{a}y:$

(1) $\varphi|_{V_2^j}: V_n^j \stackrel{\cong}{\to} V_{n-1}^j \quad$ (n $>$ 1, j $=$ 1, 2, ..., n-1),

(2) $\text{Ker}(\varphi|_{V_n}) = V_1^1 \oplus V_2^2 \oplus \cdots \oplus V_n^n \quad$ (1 $\leq$ n $\leq$ k),

(3) $V_n = \bigoplus_{1 \leq$ i $\leq n} V_i^j$ (1 $\leq$ n $\leq$ k).

Ta đặt $V_1^1 = V_1$ và dễ dàng kiểm tra lại 3 tính chất trên với n $=$ 1.



Giả sử đã xây dựng được các không $gianV_i^{\jmath}với 1\leq j\leq i<$ nthoả mãn các

tính chất nói trên. Vì $\varphi|_{V_n}: V_n \to V_{n-1}là$ một toàn ánh, nên có thể chọn các không

gian $V_n^1$, ..., $V_n^{n-1}$ sao cho

$\varphi|_{V_n^j}: V_n^j \stackrel{\cong}{\rightarrow} V_{n-1}^j$, (j $=$ 1, ..., n-1).

Tiếp theo, ta chọn $V_n^n$ là một phần bù tuyến tính của $Ker(\varphi|_{V_{n-1}})$ trong $Ker(\varphi|_{V_n})$.

Như vậy, ta có

$Ker(\varphi|_{V_n}) = Ker(\varphi|_{V_{n-1}}) \oplus V_n^n$

$= V_1^1 \oplus V_2^2 \oplus \cdots \oplus V_n^n$.

Khi đó, có thể chứng minh đẳng thức sau bằng quy nạp theo n:

$V_n = (\bigoplus_{i=1}^{n-1} V_n^j) \oplus (\bigoplus_{1 \leq$ j $\leq$ i $\leq n} V_i^j) \oplus Ker(\varphi|_{V_n})$.

Kết hợp hai đẳng thức ở trên ta thu được

$V_n = \bigoplus_{1 \leq$ i $\leq$ i $\leq n} V_i^j$.

Như vậy họ không gian con $V_i^j$ với 1 $\leq$ j $\leq$ k đã được xây dựng bằng quy nạp

theo i.

Xét dãy các không gian vécto

$V_k^j \stackrel{\cong}{\to} V_{k-1}^j \stackrel{\cong}{\to} \cdots \stackrel{\cong}{\to} V_{i+1}^j \stackrel{\cong}{\to} V_i^j \to$ 0,

trong đó các mũi tên đều chỉ các hạn chế của đồng cấu $\varphi$. Nhận xét rằng mỗi vécto

e $\neq$ 0 trong $V_k^j$ được đặt tương ứng với một không gian con xyclic (k-j+1) chiều

đối với $\varphi$, với một cơ sở xyelic gồm các vécto sau đây:

(e, $\varphi(e)$, ..., $\varphi^{k-j}(e))$.

Như thế $V_k^j \oplus V_{k-1}^j \oplus \cdots \oplus V_i^j$ là tổng trực tiếp của một số hữu hạn không gian con

xyclic (k - j + 1) chiều đối với $\varphi$. (Số không gian trong tổng này bằng dim $V_k^j.)$



Do đó

V $= V_k = \bigoplus_{i=1}^k (V_k^j \oplus V_{k-1}^j \oplus \cdots \oplus V_i^j)$

là tổng trực tiếp của một số hữu hạn không gian con xyclic đối với $\varphi$.

Giả sử V $= \bigoplus_i W_i$ là một phân tích của V thành tổng tực tiếp của các không

gian con xyclic đối với $\varphi$. Vì mỗi $W_i$ đều là một không gian $\varphi-ổn$ định, cho nên

$rank(\varphi) = \sum_i rank(\varphi|_{W_i})$.

Nếu $W_i$ là một không gian m chiều xyclic đối với $\varphi$ thì dễ thấy rằng

$ rank(\varphi^s|_{W_i}) = \begin{cases} m-s & \text{n\'eu } s \leq m, \\ 0 & \text{n\'eu } s > m. \end{cases} $

Từ đó

$ \mathrm{rank}(\varphi^{s-1}|_{W_i}) - 2\mathrm{rank}(\varphi^s|_{W_i}) + \mathrm{rank}(\varphi^{s+1}|_{W_i}) = \left\{ \begin{array}{ll} 1 &amp; \mathrm{n\acute{e}u}\ s = m, \\ 0 &amp; \mathrm{n\acute{e}u}\ s \neq m. \end{array} \right. $

Vì thế, với mỗi số nguyên dương s,

$rank(\varphi^{s-1})$ - $2rank(\varphi^s)$ + $rank(\varphi^{s+1})$

chính là số không gian con s chiều xyelic đối với $\varphi$ trong mọi phân tích của V. $\Box$

Ma trận chuẩn tắc Jordan của tự đồng cấu

$\overline{5}$

Bây giờ ta giả sử f: V $\to$ V là một đồng cấu bất kỳ, không nhất thiết lũy linh.

Với mỗi $\lambda \in \mathbf{K}$, ta xét tập

$R_{\lambda} = {\alpha \in$ V : $\exists$ m $= m(\alpha)}$ sao cho (f - $\lambda$ i $d_V)^m(\alpha) = 0}$.

Đó là một không gian véctơ con, bởi vì nó là hợp của một dãy các không gian véctơ

con lồng vào nhau

$R_{\lambda} = \bigcup_{m=1}^{\infty}$ Ker(f - $\lambda id_V)^m$.



Vì f giao hoán với f - $\lambda$ i $d_V$, cho nên $R_\lambda$ là một không gian con ổn định đối với f.

Thật vậy, nếu $\alpha \in R_{\lambda}$ thì có m $>$ 0 sao cho (f - $\lambda$ i $d_V)^m(\alpha) =$ 0. Do đó

(f - $\lambda$ i $d_V)^m f(\alpha) =$ f(f - $\lambda$ i $d_V)^m(\alpha) =$ f(0) $=$ 0.

Nhận xét rằng $R_{\lambda} \neq \{0\}$ nếu và chỉ nếu $\lambda$ là một giá trị riêng của f. Thật vậy,

nếu $\lambda$ là một giá trị riêng của f, thì không gian con riêng $P_{\lambda} =$ Ker(f - $\lambda id_V)$ là

một không gian con của $R_{\lambda}: P_{\lambda} \subset R_{\lambda}$. Ngược lại, giả sử $\alpha \in R_{\lambda} \setminus \{0\}$, chọn m là số

nguyên dương nhỏ nhất sao cho(f - $\lambda$ i $d_V)^m(\alpha) =$ 0. Khi $đó\beta =$ (f - $\lambda$ i $d_V)^{m-1}(\alpha) \neq$ 0

0 là một vécto riêng của f ứng với giá trị riêng $\lambda$, bởi vì (f - $\lambda$ i $d_V)(\beta) =$ 0.

Dinh nghĩa 5.1 Giả sử $\lambda$ là một giá trị riêng của f.

(a) $R_{\lambda}$ được gọi là không gian con riêng suy rộng ứng với giá trị riêng $\lambda$.

(b) dim $P_{\lambda}$ và dim $R_{\lambda}$ được gọi tương ứng là số chiều hình học và số chiều đại số

của giá trị riêng $\lambda$.

Mệnh đề sau đây giải thích một phần ý nghĩa của những thuật ngữ này.

Mệnh đề 5.2 Nếu $\lambda$ là một giá trị riêng của tự đồng cấu f: V $\to$ V thì dim $R_{\lambda}$

$b\ddot{a}ng\ \dot{o}\dot{o}i\ \dot{c}\dot{a}\ \lambda\ \text{xem}\ \text{nhu}\ \text{nghi}\hat{e}\text{m}\ \text{c}\dot{a}\ \text{da}\ \text{th}\hat{u}\text{c}\ \text{d}\check{a}\text{c}\ \text{tr}\text{u}\text{ng}\ \text{c}\dot{a}\ \text{f}$.

Chứng minh: Theo định nghĩa của không gian con riêng suy rộng, đồng cấu

(f - $\lambda$ i $d_V)|_{R_\lambda}$ là luỹ linh. Do đó, áp dụng Định lý 4.2 cho (f - $\lambda$ i $d_V)|_{R_\lambda}$, ta có thể

chọn một cơ sở của $R_{\lambda}$ sao cho trong cơ sở đó ma trận của $f|_{R_{\lambda}}$ có dạng chéo khối,

với các khối trên đường chéo có dạng

$ \left(\begin{array}{cccc} \lambda & 0 & 0 & \dots & 0 & 0 \\ 1 & \lambda & 0 & \dots & 0 & 0 \end{array}\right) $

$ \begin{array}{ccccccccc} 0 & 1 & \lambda & \ldots & 0 & 0 \end{array} $

$ \begin{array}{ccccccccc} 0 & 0 & 0 & \ldots & \lambda & 0 \\ & & & & & & \\ 0 & 0 & 0 & \ldots & 1 & \lambda \end{array} $



Từ đó suy ra đa thức đặc trưng của $f|_{R_{\lambda}}$ là

$P_{f|_{R_{\lambda}}}(X) = (\lambda$ - $X)^{\dim R_{\lambda}}$.

Theo Mênh đề 1.6, ta có

$P_f(X) = P_{f|_{R_1}}(X)P_{\bar{f}}(X)$

$= (\lambda$ - $X)^{\dim R_{\lambda}} P_{\bar{f}}(X)$,

trong đó f là đồng cấu cảm sinh bởi f trên không gian thương $V/R_{\lambda}$. Vì thế, nếu

gọi s là bội của $\lambda$ xem như nghiệm của đa thức đặc trưng của f, thì dim $R_{\lambda} \leq$ s.

Giả sử phản chứng dim $R_{\lambda} <$ s. Khi đó $\lambda$ là một nghiệm của $P_{\bar{f}}(X)$. Gọi

$[\alpha] \in V/R_{\lambda}$ là một véctơ riêng của $\bar{f}$ ứng với giá trị riêng $\lambda$. Khi đó $\bar{f}[\alpha] = \lambda[\alpha]$.

Nghĩa là có vécto $\beta \in R_{\lambda}$ sao cho $f(\alpha) = \lambda \alpha$ + $\beta$. Do đó $\beta =$ (f - $\lambda id_V)(\alpha) \in R_{\lambda}$.

Vì thế, có số nguyên m sao cho (f - $\lambda$ i $d_V)^m(\alpha) =$ 0, nghĩa là $\alpha \in R_\lambda$. Điều này

mâu thuẫn với giả thiết $[\alpha] \neq$ 0 trong $V/R_{\lambda}$, vì đó là một vécto riêng.

Tóm lai, ta có dim $R_{\lambda} =$ s.

$\Box$

### Định lý sau đây là một tổng quát hoá của Hệ quả 3.5.

### Định lý 5.3 (Dạng chuẩn Jordan của ma trận của tự đồng cấu tuyến tính).

Giả sử tự đồng cấu f của K-không gian vécto n chiều V có đa thức đặc trưng

$P_f(X)$ phân tích được thành các nhân tử tuyến tính trong K[X], tức là

$P_f(X) = (-1)^n$ (X - $\lambda_1)^{s_1} \cdots$ (X - $\lambda_m)^{s_m}$,

trong đó $\lambda_1$, ..., $\lambda_m$ là những vô hướng đôi một khác nhau trong K. Khi đó, V phân

tích được thành tổng trực tiếp các không gian con riêng suy rộng ứng với những

giá tri riêng $\lambda_1$, ..., $\lambda_m:$

V $= R_{\lambda_1} \oplus \cdots \oplus R_{\lambda_m}$,

$\phi$ đây dim $R_{\lambda_k} = s_k$. Hơn nữa, V có một cơ sở sao cho ma trận của f trong đó là



tống trực tiếp của các khối Jordan cấp s có dang

$ J_{s,\lambda_k} = \left( \begin{array}{cccccc} \lambda_k & 0 & 0 & ... & 0 & 0 \ & 1 & \lambda_k & 0 & ... & 0 & 0 \ & & 0 & 1 & \lambda_k & ... & 0 & 0 \ & & & . & . & ... & . & . \ 0 & 0 & 0 & ... & \lambda_k & 0 \ & & & 0 & 0 & ... & 1 & \lambda_k \end{array} \right). $

Số khối Jordan cấp s với phần tử $\lambda_k$ trên đường chéo bằng

rank(f - $\lambda_k id_V)^{s-1}$ - 2rank(f - $\lambda_k id_V)^s$ + rank(f - $\lambda_k id_V)^{s+1}$.

Ma trận này được xác định duy nhất bởi f sai khác thứ tự sắp xếp các khối Jordan

$tr\hat{e}n \$, $du\hat{\sigma}nq \$, $ch\hat{e}o \$, $ch\hat{n}h$.

Ma trận nói trong định lý trên được gọi là ma trận dạng chuẩn Jordan của tự

$\dim$ g $\operatorname{c\tilde{a}}$ u f.

Chứng minh: Ta sẽ chứng minh định lý theo nhiều bước.

Bước 1: Giả sử $\lambda \neq \mu$ là các giá trị riêng của f. Vì các đồng cấu (f - $\lambda id_V)$ và

(f - $\mu id_V)$ giao hoán với nhau, nên ta có đồng cấu

(f - $\lambda id_V)|_{R_\mu}: R_\mu \to R_\mu$.

Ta sẽ chứng minh rằng đó là một đẳng cấu. Vì $R_{\mu}$ hữu hạn chiều, cho nên chỉ cần

chứng minh đồng cấu nói trên là một đơn cấu. Giả sử phản chứng tồn tại vécto

$\alpha \in R_{\mu} \setminus \{0\}$ sao cho (f - $\lambda id_V)(\alpha) =$ 0. Theo định nghĩa của không gian con riêng

suy rộng, có số nguyên dương m sao cho

$\beta =$ (f - $\mu$ i $d_V)^{m-1}(\alpha) \neq$ 0,

(f - $\mu$ i $d_V)(\beta) =$ (f - $\mu$ i $d_V)^m(\alpha) =$ 0.

Vì các đồng cấu (f - $\lambda$ i $d_V)$ và (f - $\mu$ i $d_V)$ giao hoán với nhau, cho nên

(f - $\lambda$ i $d_V)(\beta) =$ (f - $\lambda$ i $d_V)(f$ - $\mu$ i $d_V)^{m-1}(\alpha)$

$=$ (f - $\mu$ i $d_V)^{m-1}$ (f - $\lambda$ i $d_V)(\alpha) =$ 0.



Kết hợp hai đẳng thức trên ta có $f(\beta) = \lambda \beta = \mu \beta$. Vì $\lambda \neq \mu$, nên đẳng thức trên

dẫn tới $\beta =$ 0. Mâu thuẫn này bác bỏ giả thiết phản chứng.

Bước 2: Ta chứng tỏ rằng $R_{\lambda_1}$ + $\cdots$ + $R_{\lambda_m}$ là một tổng trực tiếp trong V. Để làm

điều đó, ta chứng minh rằng với mọi $\alpha_i \in R_{\lambda_i} \setminus \{0\}$, hệ vécto $(\alpha_1$, ..., $\alpha_m)$ độc lập

tuyến tính.

Khẳng định đó hiển nhiên đúng với m $=$ 1. Giả sử qui nạp điều đó đúng với

m-1. Xét một ràng buộc tuyến tính bất kỳ $\sum_{i=1}^{m} a_i \alpha_i =$ 0 với các hệ số $a_i \in \mathbf{K}$.

Chọn số nguyên dương ksao $cho(f-\lambda_m id_V)^k(\alpha_m)=0.Tác$ động $(f-\lambda_m id_V)^k$

vào hai về của ràng buộc tuyến tính nói trên, ta thu được

m-1

$\sum_{i=1} a_i$ (f - $\lambda_m id_V)^k (\alpha_i) =$ 0,

i $=$ 1

trong đó, theo Bước 1, các $véct<br/>ơ\beta_i=(f-\lambda_{m}id_{V})^k(\alpha_i)đều$ khác không trong $R_{\lambda_i}$

với mọi $i=1,...,m-1$. Do đó, theo giả thiết qui nạp, các $véc<br/>tơ$ đó độc lập tuyến

tính, nghĩa là

$a_1 = \cdots = a_{m-1} =$ 0.

Thay các giá trị này vào ràng buộc tuyến tính ban đầu, ta có $a_m \alpha_m =$ 0. Từ đó, vì

$\alpha_m \neq$ 0, nên $a_m =$ 0. Vậy hệ vécto $(\alpha_1$, ..., $\alpha_m)$ độc lập tuyến tính.

Bước 3: V $= R_{\lambda_1} \oplus \cdots \oplus R_{\lambda_m}$.

Thật vậy, theo Mệnh đề 5.2, dim $R_{\lambda_i} = s_i$. Do đó, điều phải chứng minh được

suy từ đẳng thức sau

dim $(R_{\lambda_1} \oplus \cdots \oplus R_{\lambda_m}) = \sum_{i=1}^m s_i =$ n $= \dim$ V.

Bước 4: Bởi vì (f - $\lambda_k id_V)$ luỹ linh trên $R_{\lambda_k}$, cho nên theo Định lý 4.2 thì $f|_{R_{\lambda_k}}$

có ma trận dạng chuẩn Jordan trong một cơ sở nào đó của $R_{\lambda_k}$. Mặt khác, V $=$

$R_{\lambda_1}\oplus\cdots\oplus R_{\lambda_m}$, cho nênfcó ma trận dạng chuẩn Jordan trong một cơ sở nào đó

$\chi$ của V.

Bước 5: Theo Bước 1, với mỗi $\lambda_k \neq \lambda_i$, đồng cấu hạn chế (f - $\lambda_k id_V)|_{R_{\lambda_i}}$ : $R_{\lambda_i} \to$



$R_{\lambda_i}$ là một đẳng cấu. Vì thế, ta có

$\text{rank}(f$ - $\lambda_k id_V)|_{R_{\lambda_i}}^{s-1}$ - $2\text{rank}(f$ - $\lambda_k id_V)|_{R_{\lambda_i}}^s$ + $\text{rank}(f$ - $\lambda_k id_V)|_{R_{\lambda_i}}^{s+1} =$ 0.

Kết hợp điều này với đẳng thức V $= R_{\lambda_1} \oplus \cdots \oplus R_{\lambda_m}$ và một lần nữa áp dụng Định

lý 4.2, ta thấy trong mọi ma trận dạng chuẩn Jordan của f, số khối Jordan cấp s

với phần tử $\lambda_k$ trên đường chéo chính bằng

rank(f - $\lambda_k id_V)^{s-1}$ - 2rank(f - $\lambda_k id_V)^s$ + rank(f - $\lambda_k id_V)^{s+1}$

$= \operatorname{rank}(f$ - $\lambda_k id_V)|_{R_{\lambda_k}}^{s-1}$ - $2\operatorname{rank}(f$ - $\lambda_k id_V)|_{R_{\lambda_k}}^s$ + $\operatorname{rank}(f$ - $\lambda_k id_V)|_{R_{\lambda_k}}^{s+1}$.

Vì số này như nhau đối với mọi ma trận dạng chuẩn Jordan của f, cho nên hai ma

trận như vậy chỉ khác nhau thứ tự của các khối Jordan trên đường chéo.

Một trường hợp riêng quan trọng của định lý trên là hệ quả sau đây.

Hệ quả 5.4 Nếu K là một trường đóng đại số (chẳng hạn K $=$ C), thì mọi tự

đồng cấu của một $\mathbf{K}-không$ gian vécto đều có ma trận dạng chuẩn Jordan trong

một cơ sở nào đó của không gian.

$\Box$

Ví dụ: Tìm dạng chuẩn Jordan trên trường số thực của ma trận sau đây

$ A = \left( \begin{array}{cccc} 3 & -4 & 0 & 2 \ 4 & -5 & -2 & 4 \ 0 & 0 & 3 & -2 \ 0 & 0 & 2 & -1 \end{array} \right). $

Trước hết ta tìm đa thức đặc trưng của A:

Lò i giai:

$ det(A - XE<sub>4</sub>) = \begin{vmatrix} 3 - X & -4 & 0 & 2 \\ 4 & -5 - X & -2 & 4 \\ 0 & 0 & 3 - X & -2 \\ 0 & 0 & 2 & -1 - X \end{vmatrix} = (X - 1)<sup>2</sup>(X + 1)<sup>2</sup>. $



Da thức này có đủ nghiệm thực $\lambda_1 = \lambda_2 =$ 1, $\lambda_3 = \lambda_4 =$ -1. Vậy, ma trận A đồng

dạng trên trường số thực với một ma trận Jordan J. Các khối Jordan của ma trận

J này có các phần tử trên đường chéo bằng 1 hoặc -1, và có cấp tối đa bằng 2 (là

bội của các giá trị riêng 1 và -1). Với $\lambda_1 = \lambda_2 =$ 1, ta có

$ rank(A - 1E_4) = rank \begin{pmatrix} 2 & -4 & 0 & 2 \\ 4 & -6 & -2 & 4 \\ 0 & 0 & 2 & -2 \\ 0 & 0 & 2 & -2 \end{pmatrix} = rank 2 \begin{pmatrix} 1 & -2 & 0 & 1 \\ 2 & -3 & -1 & 2 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 1 & -1 \end{pmatrix} = 3, $

bởi vì ma trận này suy biến, và có định thức con cấp 3 ở góc trái trên khác 0. Hơn

nūa,

$ rank(A - 1E_4)^2 = rank 4 \begin{pmatrix} 1 & -2 & 0 & 1 \\ 2 & -3 & -1 & 2 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 1 & -1 \end{pmatrix}^2 = rank 4 \begin{pmatrix} -3 & 4 & 3 & -4 \\ -4 & 5 & 4 & -5 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} = 2, $

bởi vì hai hàng cuối của ma trận bằng 0, và định thức cấp 2 ở góc trái trên khác

0. Như thế, số khối Jordan cấp 1 của ma trận Jordan J với phần tử trên đường

chéo bằng 1 là

rank(A - $1E_4)^0$ – 2rank(A - 1 $\cdot E_4)^1$ + rank(A - 1 $\cdot E_4)^2 =$ 4 – 6 + 2 $=$ 0.

Kết hợp điều đó với sự kiện $\lambda =$ 1 là nghiệm kép của đa thức đặc trưng của A, ta

suy ra J chứa đúng một khối Jordan cấp 2 với các phần tử trên đường chéo bằng

1. Tương tư, với $\lambda_3 = \lambda_4 =$ -1, ta có

$ rank(A + 1E_4) = rank \begin{pmatrix} 4 & -4 & 0 & 2 \\ 4 & -4 & -2 & 4 \\ 0 & 0 & 4 & -2 \\ 0 & 0 & 2 & 0 \end{pmatrix} = rank 2 \begin{pmatrix} 2 & -2 & 0 & 1 \\ 2 & -2 & -1 & 2 \\ 0 & 0 & 2 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix} = 3, $



bởi vì đó là một ma trận suy biến và định thức con cấp 3 ở góc phải dưới của nó

khác 0. Tiếp theo,

$ rank(A + 1E_4)^2 = rank 4 \begin{pmatrix} 2 & -2 & 0 & 1 \\ 2 & -2 & -1 & 2 \\ 0 & 0 & 2 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix} = rank 4 \begin{pmatrix} 0 & 0 & 3 & -2 \\ 0 & 0 & 2 & -1 \\ 0 & 0 & 5 & -2 \\ 0 & 0 & 2 & -1 \end{pmatrix} = 2. $

Như thế, số khối Jordan cấp 1 của ma trận Jordan J với phần tử trên đường chéo

$b\tilde{a}ng$ -1 là

rank(A + $1E_4)^0$ – 2rank(A + 1 $\cdot E_4)^1$ + rank(A + 1 $\cdot E_4)^2 =$ 4 – 6 + 2 $=$ 0.

Từ đó, vì $\lambda =$ -1 là nghiệm kép của đa thức đặc trưng của A, ta suy ra J chứa

đúng một khối Jordan cấp 2 với các phần tử trên đường chéo bằng -1.

Tóm lại, dạng chuẩn Jordan của ma trận A là

$ J=\left( \begin{array}{cccc} 1 & 0 & 0 & 0 \ 1 & 1 & 0 & 0 \ 0 & 0 & -1 & 0 \ 0 & 0 & 1 & -1 \end{array} \right). $

Bài tập

1. Tìm giá trị riêng và vécto riêng của các tự đồng cấu có ma trận sau đây trong

một cơ sở nào đó của không gian:

$ (a) \begin{pmatrix} 2 & -1 & 2 \\ 5 & -3 & 3 \\ -1 & 0 & -2 \end{pmatrix}, (b) \begin{pmatrix} 4 & -5 & 2 \\ 5 & -7 & 3 \\ 6 & -9 & 4 \end{pmatrix}, $



$ (c) \begin{pmatrix} 1 & -3 & 3 \\ -2 & -6 & 13 \\ -1 & -4 & 8 \end{pmatrix}, (d) \begin{pmatrix} 1 & -3 & 4 \\ 4 & -7 & 8 \\ 6 & -7 & 7 \end{pmatrix}, $

$ (e) \left( \begin{array}{cccc} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 1 \end{array} \right), \qquad (f) \left( \begin{array}{cccc} 3 & -1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 3 & 0 & 5 & -3 \\ 4 & -1 & 3 & -1 \end{array} \right). $

2. Chứng minh rằng nếu tự đồng cấu $\varphi$ của không gian vécto n chiều V có n giá

trị riêng khác nhau và $\psi$ là một tự đồng cấu giao hoán với $\varphi$, thì mỗi vécto

riêng của $\varphi$ cũng là một vécto riêng của $\psi$ và $\psi$ có một cơ sở gồm toàn vécto

riêng của nó.

3. Xác định xem những tự đồng cấu được cho bởi các ma trận sau trong một

cơ sở nào đó của không gian véctơ V có chéo hoá được không. Nếu có, hãy

xác định cơ sở trong đó ma trận của tự đồng cấu có dạng chéo và xác định

ma trận này.

$ (a) \begin{pmatrix} -1 & 3 & -1 \\ -3 & 5 & -1 \\ -3 & 3 & 1 \end{pmatrix}, (b) \begin{pmatrix} 6 & -5 & -3 \\ 3 & -2 & -2 \\ 2 & -2 & 0 \end{pmatrix}, $

$ (c) \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 1 & -1 \\ 1 & -1 & -1 & 1 \end{pmatrix}, (d) \begin{pmatrix} 4 & -3 & 1 & 2 \\ 5 & -8 & 5 & 4 \\ 6 & -12 & 8 & 5 \\ 4 & -3 & 2 & 2 \end{pmatrix}. $



4. Cho ma trận cấp n

$ A = \left( \begin{array}{cccc} 0 & 0 & \ldots & 0 & 1 \ 0 & 0 & \ldots & 1 & 0 \ . & . & \ldots & . & . \ 0 & 1 & \ldots & 0 & 0 \ 1 & 0 & \ldots & 0 & 0 \end{array} \right). $

Tìm ma trận khả nghịch T sao cho B $= T^{-1}AT$ là một ma trận chéo, và tìm

B.

5. Ma trận A có các vô hướng $a_1$, $a_2$, ..., $a_n$ nằm trên đường chéo thứ hai (theo

thứ tự từ hàng một tới hàng n) còn tất cả các phần tử khác bằng 0. Tìm

điều kiên để A chéo hoá được.

6. Tìm giá trị riêng và vécto riêng của tự đồng cấu xác định bởi phép đạo hàm

trong không gian véctor các đa thức hệ số thực có bậc không vượt quá n.

7. Chứng minh rằng nếu ít nhất một trong hai ma trận A và B khả nghịch, thì

các ma trận tích AB và BA đồng dạng với nhau. Tìm ví dụ về các ma trận

A, B sao cho AB không đồng dạng với BA.

8. Tìm tất cả các ma trận chỉ đồng dạng với chính nó mà thôi.

9. Ma trận B nhận được từ ma trận A bằng cách đổi chỗ các hàng i và j

đồng thời đổi chỗ các cột i và j. Tìm ma trận không suy biến T sao cho

B $= T^{-1}AT$.

10. Chứng minh rằng ma trận A đồng dạng với ma trận B nhận được từ A bằng

phép đối xứng qua tâm của nó.

11. Giả sử $(i_1$, $i_2$, ..., $i_n)$ là một phép thế bất kỳ của (1, 2, ..., n). Chứng minh rằng



các ma trận sau đồng dạng:

$ A = \left( \begin{array}{cccc} a_{11} & a_{12} & \ldots & a_{1n} \ a_{21} & a_{22} & \ldots & a_{2n} \ . & . & . & . \ a_{n1} & a_{n2} & \ldots & a_{nn} \end{array} \right) \quad \text{và} \quad B = \left( \begin{array}{cccc} a_{i_1i_1} & a_{i_1i_2} & \ldots & a_{i_1i_n} \ a_{i_2i_1} & a_{i_2i_2} & \ldots & a_{i_2i_n} \ . & . & . & . & . \ . & . & . & . \ a_{i_ni_1} & a_{i_ni_2} & \ldots & $

Các ma trận sau đây có đồng dạng với nhau hay không?

12.

$ A = \begin{pmatrix} 3 & 2 & -5 \\ 2 & 6 & -10 \\ 1 & 2 & -3 \end{pmatrix} và B = \begin{pmatrix} 6 & 20 & -34 \\ 6 & 32 & -51 \\ 4 & 20 & -32 \end{pmatrix}. $

13.

$ A = \begin{pmatrix} 4 & 6 & -15 \\ 1 & 3 & -5 \\ 1 & 2 & -4 \end{pmatrix}, B = \begin{pmatrix} 1 & -3 & 3 \\ -2 & -6 & 13 \\ -1 & -4 & 8 \end{pmatrix}, C = \begin{pmatrix} -13 & -70 & 119 \\ -4 & -19 & 34 \\ -4 & -20 & 35 \end{pmatrix}. $

Chứng minh rằng các hệ số của đa thức đặc trưng của ma trận A có thể mô

14.

tå như sau:

|A - XE| $= (-X)^n$ + $c_1(-X)^{n-1}$ + $c_2(-X)^{n-2}$ + $\cdots$ + $c_n$,

trong đó $c_k$ là tổng của tất cả các định thức con chính cấp k của ma trận A.

(Một định thức con được gọi là chính nếu các chỉ số hàng và các chỉ số cột

của nó trùng nhau.)

15. Giả sử p $>$ 0 là bội của $\lambda_0$ xem như nghiệm của đa thức đặc trưng của ma

trận vuông A cấp n. Gọi r là hạng của ma trận (A - $\lambda_0$ E). Chứng minh rằng

1 $\leq$ n-r $\leq$ p.



16. Chứng minh rằng các giá trị riêng của ma trận nghịch đảo $A^{-1}$ bằng nghịch

đảo của các giá trị riêng của ma trận A (kể cả bội).

17. Chứng minh rằng các giá trị riêng của ma trận $A^2$ bằng bình phương của các

giá trị riêng của ma trận A (kể cả bội).

18. Chứng minh rằng nếu $\lambda_1$, ..., $\lambda_n$ là các giá trị riêng của ma trận A và f(X) là

một đa thức thì $f(\lambda_1),...,f(\lambda_n)$ là các giá trị riêng của ma trận f(A).

19. Chứng minh rằng nếu A và B là các ma trận vuông cùng cấp thì các đa thức

đặc trưng của các ma trận AB và BA trùng nhau.

20. Tìm các giá trị riêng của ma trận xyclic

$ A = \left( \begin{array}{cccc} a_1 & a_2 & a_3 & \ldots & a_n \ a_n & a_1 & a_2 & \ldots & a_{n-1} \ a_{n-1} & a_n & a_1 & \ldots & a_{n-2} \ . & . & . & . & . \ a_2 & a_3 & a_4 & \ldots & a_1 \end{array} \right). $

21. Tìm các giá trị riêng của ma trận cấp n sau đây

$ A = \left( \begin{array}{llllllll} 0 & -1 & 0 & 0 & \ldots & 0 & 0 \\ 1 & 0 & -1 & 0 & \ldots & 0 & 0 \\ 0 & 1 & 0 & -1 & \ldots & 0 & 0 \\ . & . & . & . & . & . & . \\ 0 & 0 & 0 & 0 & \ldots & 1 & 0 \end{array} \right). $

$\mbox{Tim } \mbox{dang$ chuán Jordan cúa $} \mbox{các } \mbox{ma$ trân sau $} \mbox{dây:}$

22.

$ (a) \begin{pmatrix} 2 & 6 & -15 \\ 1 & 1 & -5 \\ 1 & 2 & -6 \end{pmatrix}, (b) \begin{pmatrix} 1 & -3 & 3 \\ -2 & -6 & 13 \\ -1 & -4 & 8 \end{pmatrix}, $

1 ∩ ∩



$ (c) \begin{pmatrix} 1 & -3 & 4 \\ 4 & -7 & 8 \\ 6 & -7 & 7 \end{pmatrix}, (d) \begin{pmatrix} a & 0 & 0 \\ 0 & a & 0 \\ a & 0 & a \end{pmatrix} (với a \neq 0). $

23.

$ (a) \begin{pmatrix} 3 & -1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 3 & 0 & 5 & -3 \\ 4 & -1 & 3 & -1 \end{pmatrix}, (b) \begin{pmatrix} 3 & -4 & 0 & 2 \\ 4 & -5 & -2 & 4 \\ 0 & 0 & 3 & -2 \\ 0 & 0 & 2 & -1 \end{pmatrix}. $

24.

$ \left( \begin{array}{cccccc} 1 & -1 & 0 & 0 & \ldots & 0 & 0 \ 0 & 1 & -1 & 0 & \ldots & 0 & 0 \ 0 & 0 & 1 & -1 & \ldots & 0 & 0 \ \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \ 0 & 0 & 0 & 0 & \ldots & 0 & 1 \end{array} \right). $

25.

$ \begin{pmatrix} 1 & 0 & 0 & 0 & \dots & 0 \\ 1 & 2 & 0 & 0 & \dots & 0 \\ & & 2 & 3 & 0 & \dots & 0 \\ & & & \ddots & \ddots & \ddots & \ddots \\ & & & & 1 & 2 & 3 & 4 & \dots & n \end{pmatrix}. $

26.

$ \left(\begin{array}{cccccc} 0 & a & 0 & 0 & \ldots & 0 \\ 0 & 0 & a & 0 & \ldots & 0 \\ 0 & 0 & 0 & a & \ldots & 0 \end{array}\right) $

$ \left( \begin{array}{cccccc} . & . & . & . & ... & . \\ 0 & 0 & 0 & 0 & ... & a \\ a & 0 & 0 & 0 & ... & 0 \end{array} \right) $



27.

$ \left( \begin{array}{cccc} a & a_{12} & a_{13} & ... & a_{1n} \ 0 & a & a_{23} & ... & a_{2n} \ 0 & 0 & a & ... & a_{3n} \ . & . & . & ... & . \ 0 & 0 & 0 & ... & a \end{array} \right), $

trong đó $a_{12}a_{23}\cdots a_{n-1 n} \neq$ 0.

28. Giả sử K là một trường đóng đại số. Chứng minh rằng ma trận A với các

phần tử trong K là lũy linh (tức là $A^k =$ 0 với một số nguyên dương k nào

đó) nếu và chỉ nếu tất cả các giá trị riêng của nó bằng 0.

29. Chứng minh rằng mọi ma trận lũy linh khác 0 đều không chéo hoá được.

30. Tìm dạng chuẩn Jordan của ma trận lũy đẳng A (tức là ma trận với tính chất

$A^2 =$ A).

31. Chứng minh rằng mọi ma trận đối hợp A (tức là ma trận với tính chất

$A^2 =$ E) đều đồng dạng với một ma trận chéo. Tìm dạng của các ma trận

chéo đó.

32. Chứng minh rằng mọi ma trận tuần hoàn A (tức là ma trận với tính chất

$A^k =$ E, với một số nguyên dương k nào đó) đều đồng dạng với một ma trận

chéo. Tìm dạng của các ma trận chéo đó.

33. Cho A là một khối Jordan cấp n

$ \left(\begin{array}{cccccc} a & 1 & 0 & \dots & 0 \end{array}\right) $

$ A = \left[ \begin{array}{cccc} 0 & a & 1 & \dots & 0 \ \cdot & \cdot & \cdot & \dots & \cdot \ 0 & 0 & 0 & \dots & a \end{array} \right]. $



Chứng minh rằng giá trị của đa thức f(X) khi thay X $=$ A được heo bởi

công thức sau đây

$ f(A) = \begin{pmatrix} f(a) & \frac{f'(a)}{1!} & \frac{f''(a)}{2!} & \ldots & \frac{f^{(n-1)}(a)}{(n-1)!} \\ 0 & f(a) & \frac{f'(a)}{1!} & \ldots & \frac{f^{(n-2)}(a)}{(n-2)!} \\ \cdot & \cdot & \cdot & \cdots & \cdot \\ 0 & 0 & 0 & \ldots & f(a) \end{pmatrix}. $

34. Tìm dạng chuẩn Jordan của bình phương của một khối Jordan với 0 nằm

trên đường chéo chính.

35. Tìm dạng chuẩn Jordan của ma trận sau đây với cấp n $\geq$ 3.

$ \left(\begin{array}{ccccccccc}\na & 0 & 1 & 0 & \dots & 0\n\end{array}\right) $

$ A = \left[ \begin{array}{cccccc} 0 & a & 0 & 1 & \ldots & 0 \ & & \ddots & \ddots & \ddots & \ldots & \vdots \ 0 & 0 & 0 & \ldots & a \end{array} \right]. $

36. Chứng minh rằng mọi ma trận vuông với các phần tử trong một trường đóng

đại số đều có thể viết thành tích của hai ma trận đối xứng mà một trong hai

ma trận ấy không suy biến.

37. Chứng minh rằng nếu ma trận A có dạng đường chéo khối

$ A = \left( \begin{array}{cccc} A_1 & 0 & ... & 0 \ \ 0 & A_2 & ... & 0 \ \ . & . & ... & . \ 0 & 0 & ... & A_s \end{array} \right), $

trong đó $A_1$, $A_2$, ..., $A_s$ là các ma trận vuông, và f(X) là một đa thức của ẩn

X thi

$ f(A) = \left( \begin{array}{cccc} f(A_1) & 0 & \dots & 0 \\ 0 & f(A_2) & \dots & 0 \\ \cdot & \cdot & \dots & \cdot \\ 0 & 0 & \dots & f(A_s) \end{array} \right). $



38. Cho A là một ma trận vuông cấp n với các phần tử trong một trường đóng

đại số K. Gọi $\lambda_1$, $\lambda_2$, ..., $\lambda_n$ là các giá trị riêng (kể cả bội) của A. Chứng minh

rằng nếu f(X) là một đa thức với các hệ số trong K thì

det f(A) $= f(\lambda_1) f(\lambda_2) \cdots f(\lambda_n)$.

$\overline{1} \cap \overline{2}$



# Chương V

KHÔNG GIAN VÉCTO EUCLID

Cấu trúc không gian vécto cho phép diễn đạt các khái niêm như độc lập tuyến

tính và phụ thuộc tuyến tính, tập sinh, hạng, cơ sở và toạ độ, không gian con k

chiều (đường thẳng, mặt phẳng)... Tuy nhiên cấu trúc này chưa cho phép nói đến

các khái niệm mang nội dung hình học nhiều hơn như độ dài của véctơ và góc giữa

hai vécto... Để diễn đạt những khái niệm này, người ta cần cấu trúc không gian

vécto Euclid.

Các không gian vécto loại đặc biệt này không định nghĩa được trên một trường

cơ sở tùy ý. Vì thế trong hầu như toàn bộ chương này ta chỉ xét các không gian

vécto (trên trường số) thực. Tiết cuối của chương sẽ được dành để xét những thay

đổi cần thiết khi chuyển sang không gian vécto phức.

Không gian vécto Euclid

$\mathbf$ 1

Nhắc lại rằng, trong hình học sơ cấp, tích vô hướng của hai vécto được định nghĩa

bằng tích của độ dài hai vécto đó và côsin của góc xen giữa chúng. Dễ thấy rằng,

ngược lại, độ dài của vécto và góc xen giữa hai vécto có thể biểu thị qua tích vô

hướng. Người ta nhận thấy rằng, để đưa những khái niệm này vào các không gian

vécto trừu tương, việc trưc tiếp trừu tương hoá các khái niệm đô dài của vécto và

góc xen giữa hai vécto khó hơn nhiều so với việc trừu tượng hoá khái niệm tích

vô hướng. Vì thế, trước hết chúng ta nghiên cứu khái niệm tích vô hướng. Rồi sử

dụng nó để định nghĩa độ dài của vécto và góc xen giữa hai vécto.

Giả sử E là một không gian vécto thực. Nhắc lại rằng một hàm

$\eta:$ E $\times$ E $\to \mathbf{R}$



được gọi là song tuyến tính nếu nó tuyến tính đối với từng biến khi cố định biến

còn lại. Mỗi hàm song tuyến tính như thế được gọi là một dạng song tuyến tính

trên E.

### Dịnh nghĩa 1.1 (i) Dạng song tuyến tính \eta : E \times E \to \mathbf{R} được gọi là đối xứng

n $\tilde{e}$ u

$\eta(\alpha$, $\beta) = \eta(\beta$, $\alpha)$, $\quad \forall \alpha$, $\beta \in$ E.

(ii) $\eta$ được gọi là $du\sigma$ ng nếu

$\eta(\alpha$, $\alpha) \geq$ 0, $\quad \forall \alpha \in$ E.

(iii) $\eta$ được gọi là xác định dương nếu nó dương và

$\eta(\alpha,\alpha) =$ 0 $\Leftrightarrow \alpha =$ 0.

(iv) Một dạng song tuyến tính, đối xứng và xác định dương trên E được gọi là

một tích vô hướng trên E.

Tích vô hướng trên không gian E thường được ký hiệu là $\langle \cdot$, $\cdot \rangle:$

$\langle \cdot$, $\cdot \rangle$ : E $\times$ E $\rightarrow \mathbf{R}$

$(\alpha$, $\beta) \rightarrow \langle \alpha$, $\beta \rangle$.

Số thực $\langle \alpha$, $\beta \rangle$ được gọi là tích vô hướng của hai vécto $\alpha$ và $\beta$. Những điều kiện

$d\tilde{e} \langle \cdot$, $\cdot \rangle$ là một tích vô hướng được liệt kê như sau:

Tính song tuyến tính $\langle \alpha_1$ + $\alpha_2$, $\beta \rangle = \langle \alpha_1$, $\beta \rangle$ + $\langle \alpha_2$, $\beta \rangle$,

$\langle a\alpha$, $\beta \rangle =$ a $\langle \alpha$, $\beta \rangle$,

$\langle \alpha$, $\beta_1$ + $\beta_2 \rangle = \langle \alpha$, $\beta_1 \rangle$ + $\langle \alpha$, $\beta_2 \rangle$,

$\langle \alpha$, $a\beta \rangle =$ a $\langle \alpha$, $\beta \rangle$,

$\langle \alpha$, $\beta \rangle = \langle \beta$, $\alpha \rangle$,

Tính đối xứng

Tính xác định dương $\langle \alpha$, $\alpha \rangle \geq$ 0,

$\eta(\alpha,\alpha) =$ 0 $\Leftrightarrow \alpha =$ 0.

với mọi $\alpha$, $\alpha_i$, $\beta$, $\beta_i \in$ E, a $\in \mathbf{R}$.



Dinh nghĩa 1.2 Không gian vécto thực E cùng với một tích vô hướng trên E

được gọi là một không gian vécto Euclid.

Ví dụ 1.3 (a) Không gian các vécto tự do đã học ở hình học sơ cấp là một không

gian véctor Euclid với tích vô hướng thông thường

$\langle \alpha$, $\beta \rangle = |\alpha| |\beta| \cos \angle(\alpha$, $\beta)$.

(b) Giả sử E là một không gian vécto thực n chiều và $(e_1$, $e_2$, ..., $e_n)$ là một co

sở của nó. Có thể định nghĩa một tích vô hướng trên E như sau. Nếu

$\alpha = \sum_i x_i e_i$, $\beta = \sum_i y_i e_i$, thì ta đăt

$\langle \alpha$, $\beta \rangle = \sum x_i y_i$.

$i=1$

Nói riêng, nếu E $= \mathbf{R}^n$ và $(e_1$, $e_2$, ..., $e_n)$ là cơ sở chính tắc của $\mathbf{R}^n$, thì tích vô

$ hướng của hai vécto \alpha = \begin{pmatrix} x_1 \\ x_2 \\ \cdot \\ \cdot \\ x_n \end{pmatrix}, \beta = \begin{pmatrix} y_1 \\ \cdot \\ \cdot \\ \cdot \\ y_n \end{pmatrix} được định nghĩa là $

$\langle \alpha$, $\beta \rangle = \sum_{i=1}^{n} x_i y_i$.

Nó được gọi là tích vô hướng chính tắc trên $\mathbb{R}^n$. Nhận xét rằng theo cách

này mỗi cơ sở của E cho phép xác định trên E một tích vô hướng. Hai tích

vô hướng xác định bởi hai cơ sở khác nhau thì nói chung khác nhau.

Giả sử E $=$ C[a, b] là không gian các hàm thực liên tục trên [a, b]. Công thức

(c)

$\langle$ f, g $\rangle = \int_{a}^{b}$ f(x)g(x)dx, $\quad$ f, g $\in$ C[a, b]

xác định một tích vô hướng trên không gian vô hạn $chiều{\cal C}[a,b].Tính$ liên

tục của các hàm trong C[a, b] được dùng để chứng minh tính xác định dương

của dạng song tuyến tính (f, g) $\mapsto \langle$ f, g $\rangle$.



Môi không gian vécto con F của không gian vécto Euclid E được trang bị một

tích vô hướng, là thu hẹp của tích vô hướng đã cho trên E. Vì thế F cũng là một

không gian vécto Euclid. Nó được gọi là một không gian vécto Euclid con của E.

Bây giờ ta định nghĩa độ dài của vécto và góc giữa hai vécto trong một không

gian vécto Euclid.

### Định nghĩa 1.4 Giả sử E là một không gian vécto Euclid với tích vô hướng \langle \cdot, \cdot \rangle.

Khi đó, độ dài (hay chuẩn) của vécto $\alpha \in$ E là số thực không âm $|\alpha| = \sqrt{\langle \alpha$, $\alpha \rangle}$.

Nhận xét rằng, ngược lại, tích vô hướng cũng được hoàn toàn xác định bởi độ

dài vécto. Thật vậy

$\langle \alpha$, $\beta \rangle = \frac{1}{2} \{ |\alpha$ + $\beta|^2$ - $|\alpha|^2$ - $|\beta|^2 \}$.

Để định nghiã được góc giữa hai vécto, ta cần mệnh đề sau đây.

Mệnh đề 1.5 (Bất đẳng thức Cauchy-Schwarz)

$|\langle \alpha$, $\beta \rangle| \leq |\alpha| |\beta|$, $\quad \forall \alpha$, $\beta \in$ E.

Chứng minh: Ta có $\langle t\alpha$ + $\beta$, $t\alpha$ + $\beta \rangle \geq$ 0, $\forall$ t $\in \mathbf{R}$. Hay là

$t^2 \langle \alpha$, $\alpha \rangle$ + 2t $\langle \alpha$, $\beta \rangle$ + $\langle \beta$, $\beta \rangle \geq$ 0, $\forall$ t $\in \mathbf{R}$.

Vế trái là một tam thức bậc hai đối với t. Nó không âm với mọi giá trị của t, cho

nên

$\Delta' = \langle \alpha$, $\beta \rangle^2$ - $\langle \alpha$, $\alpha \rangle \langle \beta$, $\beta \rangle \leq$ 0.

Từ đó

$\langle \alpha$, $\beta \rangle^2 \leq \langle \alpha$, $\alpha \rangle \langle \beta$, $\beta \rangle$.

Khai căn hai vế của bất đẳng thức, ta có

$|\langle \alpha$, $\beta \rangle| \leq \sqrt{\langle \alpha$, $\alpha \rangle} \sqrt{\langle \beta$, $\beta \rangle} = |\alpha||\beta|$.

$\Box$



Trong $\mathbb{R}^n$ với tích vô hướng chính tắc, bất đẳng thức trên có dạng

$\left|\sum_{i=1}^n x_i y_i\right| \leq \sqrt{\sum_{i=1}^n x_i^2} \sqrt{\sum_{i=1}^n y_i^2}$, $\quad \forall x_i$, $y_i \in \mathbf{R}$.

### Định nghĩa 1.6 Góc giữa hai vécto khác không \alpha và \beta được ký hiệu bởi \angle(\alpha, \beta)

và được xác định duy nhất bởi các điều kiện sau

$ \begin{cases} \cos \angle(\alpha, \beta) = \frac{\langle \alpha, \beta \rangle}{|\alpha||\beta|}, \\ 0 < \angle(\alpha, \beta) < \pi \end{cases} $

Ta coi góc giữa véctơ 0 và một véctơ khác là không xác định.

### Dịnh nghĩa 1.7 Hai vécto \alpha, \beta \in E được gọi là vuông góc (hay trực giao) với

nhau, và được ký hiệu là $\alpha \perp \beta$, nếu

$\langle \alpha$, $\beta \rangle =$ 0.

Như vậy, $\langle \alpha$, $\beta \rangle =$ 0 nếu và chỉ nếu hoặc là ít nhất một trong hai vécto $\alpha$, $\beta$ bằng

0, hoặc là $\angle(\alpha$, $\beta) = \frac{\pi}{2}$.

Mệnh đề 1.8 (Định lý Pythagore) Nếu $\alpha \perp \beta$, thì

$|\alpha$ + $\beta|^2 = |\alpha|^2$ + $|\beta|^2$.

Chứng minh: Ta có

$\langle \alpha$ + $\beta$, $\alpha$ + $\beta \rangle = \langle \alpha$, $\alpha \rangle$ + 2 $\langle \alpha$, $\beta \rangle$ + $\langle \beta$, $\beta \rangle$.

Vì $\alpha \perp \beta$, cho nên $\langle \alpha$, $\beta \rangle =$ 0. Do đó $|\alpha$ + $\beta|^2 = |\alpha|^2$ + $|\beta|^2$. $\Box$

Các tính chất cơ bản của độ dài vécto được liệt kê trong mệnh đề sau đây.

Mệnh đề 1.9 (i) $|\alpha| \ge$ 0, $\forall \alpha \in$ E,

$|\alpha| =$ 0 $\Leftrightarrow \alpha =$ 0.

(ii) $|a\alpha| = |a||\alpha| \quad \forall$ a $\in \mathbf{R}$, $\forall \alpha \in$ E.



(iii) (Bất đẳng thức tam giác)

$|\alpha$ + $\beta| \leq |\alpha|$ + $|\beta|$, $\quad \forall \alpha$, $\beta \in$ E.

Chứng minh: Các phần (i) và (ii) được suy ngay từ định nghĩa của độ dài vécto.

(iii) Theo bất đẳng thức Cauchy-Schwarz ta có

$|\alpha$ + $\beta|^2 = \langle \alpha$ + $\beta$, $\alpha$ + $\beta \rangle = \langle \alpha$, $\alpha \rangle$ + $2\langle \alpha$, $\beta \rangle$ + $\langle \beta$, $\beta \rangle$

$\leq |\alpha|^2$ + $2|\alpha||\beta|$ + $|\beta|^2 = (|\alpha|$ + $|\beta|)^2$.

$\Box$

$\bullet$

Khoảng cách từ vécto $\alpha$ tới vécto $\beta$ được định nghĩa như sau:

$d(\alpha$, $\beta) = |\alpha$ - $\beta|$.

Hàm khoảng cách có những tính chất cơ bản sau đây:

(i) $d(\alpha$, $\beta) \ge$ 0, $\forall \alpha$, $\beta \in$ E,

$d(\alpha$, $\beta) =$ 0 $\Leftrightarrow \alpha = \beta$.

(ii) $d(\alpha$, $\beta) = d(\beta$, $\alpha) \quad \forall \alpha$, $\beta \in$ E.

(iii) (Bất đẳng thức tam giác)

$d(\alpha$, $\gamma) \leq d(\alpha$, $\beta)$ + $d(\beta$, $\gamma) \quad \forall \alpha$, $\beta$, $\gamma \in$ E.

### Định nghĩa 1.10 (i) Hệ vécto (e_1, ..., e_k) của không gian vécto Euclid E được

gọi là một hệ trực giao nếu các vécto của hệ đôi một vuông góc với nhau, tức

$l\grave{a}$

$\langle e_i$, $e_j \rangle =$ 0, nếu i $\neq$ j.

(ii) Hệ vécto $(e_1$, ..., $e_k)$ được gọi là một hệ trực chuẩn nếu nó là một hệ trực giao

và mỗi véctơ của hệ đều có độ dài bằng 1, tức là

$ \langle e_i, e_j \rangle = \begin{cases} 0, & \text{m\'eu } i \neq j, \\ 1, & \text{m\'eu } i = j. \end{cases} $



Mệnh đề 1.11 (i) Mỗi hệ trực giao không chứa véctơ 0 đều độc lập tuyến tính.

(ii) Nếu hệ véctơ $(e_1$, ..., $e_k)$ là trực giao và không chứa véctơ 0, thì hệ $(\frac{e_1}{|e_1|}$, ..., $\frac{e_k}{|e_k|})$

là trực chuẩn.

Chứng minh: (i) Giả sử $(e_1$, ..., $e_k)$ là một hệ trực giao và không chứa vécto 0.

Giả sử có một ràng buộc tuyến tính

$a_1e_1$ + $\cdots$ + $a_ke_k =$ 0.

Nhân vô hướng hai vế với $e_k$, và sử dụng giả thiết $e_j \perp e_j$ với i $\neq$ j, ta có:

0 $= \langle a_1e_1$ + $\cdots$ + $a_ke_k$, $e_k \rangle = a_1 \langle e_1$, $e_k \rangle$ + $\cdots$ + $a_k \langle e_k$, $e_k \rangle$

$= a_k \langle e_k$, $e_k \rangle$.

Vì $e_k \neq$ 0, nên $\langle e_k$, $e_k \rangle >$ 0. Do đó $a_k =$ 0. Từ đó ta thu được ràng buộc

$a_1e_1$ + $\cdots$ + $a_{k-1}e_{k-1} =$ 0.

Lặp lại lập luận trên với k được thay bởi k-1, ta thu được $a_{k-1} =$ 0. Cuối cùng

ta thu được

$a_1 = a_2 = \cdots = a_k =$ 0.

Vậy hệ $(e_1$, ..., $e_k)$ độc lập tuyến tính.

(ii) Ta có

$ \langle \frac{e_i}{|e_i|}, \frac{e_j}{|e_j|} \rangle = \frac{1}{|e_i||e_j|} \langle e_i, e_j \rangle = \begin{cases} 0, & \text{if } i \neq j, \\ 1, & \text{if } i = j. \Box \end{cases} $

Một cơ sở của E đồng thời là một hệ trực chuẩn được gọi là một cơ sở trực

$\omega'chuẩn$. Định lý sau đây nói lên tính phổ biến của cơ sở trực chuẩn.

Dinh lý 1.12 Mọi không gian vécto Euclid hữu hạn chiều đều có cơ sở trực chuẩn.



Chứng minh: Định lý được chứng minh bằng phép trực giao hoá Shmidt.

Giả sử $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở bất kỳ của không gian véctor Euclid E. Trực

giao hoá Shmidt là phép dựng một cơ sở trực giao $(e_1$, ..., $e_n)$ của E với tính chất

sau

$\mathcal{L}(e_1$, ..., $e_k) = \mathcal{L}(\alpha_1$, ..., $\alpha_k)$, $\qquad$ (k $=$ 1, 2, ..., n).

Sau đó, ta chuẩn $hoá(e_1,...,e_n)để$ thu được một cơ sở trực chuẩn của E.

Ta đặt $e_1 = \alpha_1$. Như thế $\mathcal{L}(e_1) = \mathcal{L}(\alpha_1)$. Giả sử đã xây dựng được hệ trực giao

$(e_1$, ..., $e_{i-1})$ sao cho

$\mathcal{L}(e_1$, ..., $e_k) = \mathcal{L}(\alpha_1$, ..., $\alpha_k)$, $\qquad$ (k $=$ 1, 2, ..., i - 1).

Tiếp theo, ta tìm $e_i$ dưới dạng

$e_i = \lambda_{i1}e_1$ + $\cdots$ + $\lambda_{i_{i-1}}e_{i-1}$ + $\alpha_i$

trong đó $\lambda_{i1},...,\lambda_{ii-1}$ là i-1 số thực được xác định bởi i-1 điều kiện $e_i \perp e_1,...,e_i \perp$

$e_{i-1}$. Tức là

$ \left\{\n\begin{array}{rcl}\n\langle e_i, e_1 \rangle & = & \lambda_{i1} \langle e_1, e_1 \rangle + \langle \alpha_i, e_1 \rangle & = & 0 \\
\cdots & \cdots & \cdots & \cdots \\
\langle e_i, e_{i-1} \rangle & = & \lambda_{ii-1} \langle e_{i-1}, e_{i-1} \rangle + \langle \alpha_i, e_{i-1} \rangle & = & 0.\n\end{array}\n\right. $

Hệ này có nghiệm duy nhất

$\lambda_{ik} = -\frac{\langle \alpha_i$, $e_k \rangle}{\langle e_k$, $e_k \rangle}$ (k $=$ 1, 2, ..., i - 1).

Vì $\alpha_i$ không nằm trong không gian $\mathcal{L}(e_1$, ..., $e_{i-1}) = \mathcal{L}(\alpha_1$, ..., $\alpha_{i-1})$, cho nên

$e_i = \lambda_{i1} e_1$ + $\cdots$ + $\lambda_{i i-1} e_{i-1}$ + $\alpha_i \neq$ 0.

Hơn nữa, theo đẳng thức trên $\alpha_i \in \mathcal{L}(e_1$, ..., $e_i)$, và $e_i \in \mathcal{L}(e_1$, ..., $e_{i-1}$, $\alpha_i)$

$\mathcal{L}(\alpha_1$, ..., $\alpha_i)$. Kết hợp điều đó với giả thiết $\mathcal{L}(e_1$, ..., $e_{i-1}) = \mathcal{L}(\alpha_1$, ..., $\alpha_{i-1})$, ta

$\overline{c}$

$\mathcal{L}(e_1$, ..., $e_i) = \mathcal{L}(\alpha_1$, ..., $\alpha_i)$.



Quá trình này tiếp diễn cho tới i $=$ n. Hệ gồm n vécto trực giao $e_1$, ..., $e_n$ sinh ra

không gian n chiều E. Vậy hệ đó là một cơ sở trực giao của E. Cuối cùng, chuẩn

hoá cơ sở trực giao này như đã làm ở phần (ii) của mệnh đề trước, ta thu được

một cơ sở trực chuẩn của E.

$\Box$

Ví dụ: Trực giao hoá hệ véctơ sau đây trong không gian $\mathbf{R}_4$ với tích vô hướng

$(\text{dinh ngh\tilde{a}nh\tilde{\sigma} c\sigma s\tilde{\sigma})$ chính tắc:

$\alpha_1 =$ (1,0,0,0),

$\alpha_2 =$ (2, 1, 0, 0),

$\alpha_3 =$ (3, 2, 1, 0),

$\alpha_4 =$ (4, 3, 2, 1).

Lời giải: Ta đặt $e_1 = \alpha_1 =$ (1, 0, 0, 0). Vécto thứ hai được tìm dưới dạng

$e_2 = \lambda_{21}e_1$ + $\alpha_2$, trong đó

$\lambda_{21} = -\frac{\langle \alpha_2$, $e_1 \rangle}{\langle e_1$, $e_1 \rangle} = -\frac{1.2}{1.1} =$ -2.

Vậy $e_2 = -2e_1$ + $\alpha_2 =$ -2(1,0,0,0) + (2,1,0,0) $=$ (0,1,0,0). Vécto thứ ba được

tìm dưới dạng $e_3 = \lambda_{31}e_1$ + $\lambda_{32}e_2$ + $\alpha_3$, trong đó

$\lambda_{31} = -\frac{\langle \alpha_3$, $e_1 \rangle}{\langle e_1$, $e_1 \rangle} = -\frac{1.3}{1.1} =$ -3,

$\lambda_{32} = -\frac{\langle \alpha_3$, $e_2 \rangle}{\langle e_2$, $e_2 \rangle} = -\frac{1.2}{1.1} =$ -2.

Vậy $e_3 = -3e_1$ - $2e_2$ + $\alpha_3 =$ (0, 0, 1, 0). Tương tự, $e_4 = \lambda_{41}e_1$ + $\lambda_{42}e_2$ + $\lambda_{43}e_3$ + $\alpha_4$,

trong đó

$\lambda_{41} = -\frac{\langle \alpha_4$, $e_1 \rangle}{\langle e_1$, $e_1 \rangle} = -\frac{1.4}{1.1} =$ -4,

$\lambda_{42} = -\frac{\langle \alpha_4$, $e_2 \rangle}{\langle e_2$, $e_2 \rangle} = -\frac{1.3}{1.1} =$ -3,

$\lambda_{43} = -\frac{\langle \alpha_4$, $e_3 \rangle}{\langle e_3$, $e_3 \rangle} = -\frac{1.2}{1.1} =$ -2.

Như thế $e_4 = -4e_1$ - $3e_2$ - $2e_3$ + $\alpha_4 =$ (0, 0, 0, 1).



Tóm lại, hệ $(e_1$, $e_2$, $e_3$, $e_4)$ chính là cơ sở chính tắc của $\mathbf{R}_4$.

Mệnh đề sau đây cho thấy cơ sở trực chuẩn giúp cho việc tính tích vô hướng

duoc dê dàng.

Mệnh đề 1.13 Giả sử $(e_1,...,e_n)$ là một cơ sở trực chuẩn của không gian véctơ

Euclid E. Khi đó, nếu $\alpha = \sum_i a_i e_i$, và $\beta = \sum_i b_i e_i$, thì

$\langle \alpha$, $\beta \rangle = a_1 b_1$ + $\cdots$ + $a_n b_n$.

Chứng minh: Do tính song tuyến tính của tích vô hướng, ta có

$\langle \alpha$, $\beta \rangle = \langle \sum_i a_i e_i$, $\sum_j b_j e_j \rangle = \sum_{i,j} a_i b_j \langle e_i$, $e_j \rangle$.

Vì $(e_1$, ..., $e_n)$ là một cơ sở trực chuẩn, cho nên

$\langle \alpha$, $\beta \rangle = \sum_i a_i b_i \langle e_i$, $e_i \rangle = \sum_i a_i b_i$.

Dinh nghĩa 1.14 Giả sử U và V là các không gian véctor con của không gian véctor

Euclid E.

Ta nói vécto $\alpha \in$ E vuông góc (hay trực giao) với U, và viết $\alpha \perp$ U, nếu

(i)

$\alpha \perp$ u với mọi u $\in$ U.

(ii) Ta nói U vuông góc (hay trực giao) với V, và viết U $\perp$ V, nếu

u $\perp$ v, $\forall$ u $\in$ U, $\forall$ v $\in$ V.

Do tính đối xứng của tích vô hướng, nếu U $\perp$ V thì V $\perp$ U. Khi đó U $\cap$ V $= \{0\}$.

Thật vậy, nếu $\alpha \in$ U $\cap$ Vthì $\langle \alpha$, $\alpha \rangle =$ 0, do đó $\alpha =$ 0. Khi đó, tổng U + Vlà một

tổng trực tiếp, U $\oplus$ V. Nó được gọi là tổng trực giao của U và V, và được ký hiệu

là U $\oplus^{\perp}$ V.

Giả sử $U_1$, ..., $U_k$ là các không gian con của E đôi một trực giao với nhau: $U_i \perp U_j$

với i $\neq$ j. Dễ thấy rằng $U_i \perp (\sum_{j \neq i} U_j)$, cho nên

$U_i \cap (\sum_{j \neq i} U_j) = \{0\}$, (i $=$ 1, ..., k).

Do đó, tổng $U_1$ + $\cdots$ + $U_k$ là một tổng trực tiếp.



### Định nghĩa 1.15 Tổng trực tiếp của các không gian con đôi một trực giao với

nhau $U_1$, ..., $U_k$ được gọi là một tổng trực giao, và được ký hiệu là $U_1 \oplus^{\perp} \cdots \oplus^{\perp} U_k$.

Nếu $(e_1$, ..., $e_n)$ là một cơ sở trực chuẩn của E thì E phân tích được thành tổng

truc giao

E $= \mathcal{L}(e_1) \oplus^{\perp} \cdots \oplus^{\perp} \mathcal{L}(e_n)$.

Dinh nghĩa 1.16 Giả sử U là một không gian vécto con của E. Khi đó

$U^{\perp} = \{ \alpha \in$ E | $\alpha \perp$ U $\}$

được gọi là phần bù trực qiao của U trong E.

Dễ thấy rằng $U^{\perp}$ cũng là một không gian véctor con của E.

Mệnh đề 1.17 Giả sử U là một không gian vécto con của không gian vécto Euclid

hữu hạn chiều E. Khi đó, $(U^{\perp})^{\perp} =$ U, và E có thể phân tích thành tổng trực giao

E $=$ U $\oplus^{\perp} U^{\perp}$.

Chứng minh: Chọn một cơ sở trực giao $(e_1$, ..., $e_m)$ của U, và bổ sung nó để có

một cơ sở $(e_1$, ..., $e_m$, $\alpha_{m+1}$, ..., $\alpha_n)$ của E. Áp dụng phép trực giao hoá Shmidt cho

cơ sở đó, ta thấy m vécto đầu của cơ sở không thay đổi, bởi vì chúng đã trực giao

sẵn rồi. Kết quả là ta thu được một cơ sở trực giao $(e_1$, ..., $e_m$, $e_{m+1}$, ..., $e_n)$ của E.

Các vécto $e_{m+1},...,e_n$ trực giao với mỗi phần tử trong cơ sở $(e_1,...,e_m)$ của U, cho

nên chúng trực giao với U. Vì thế, $e_{m+1},...,e_n \in U^{\perp}$.

Hơn nữa, nếu $\alpha$ là một véc tơ bất kỳ của $U^{\perp}$, ta xét khai triển của nó theo cơ

sở $(e_1$, ..., $e_n)$ của E: $\alpha = a_1e_1$ + $\cdots$ + $a_ne_n$. Do tính trực giao của cơ sở nói trên, ta

thu duoc:

$a_1 = \frac{\langle \alpha$, $e_1 \rangle}{\langle e_1$, $e_1 \rangle} =$ 0, ..., $a_m = \frac{\langle \alpha$, $e_m \rangle}{\langle e_m$, $e_m \rangle} =$ 0.

Hệ quả là $\alpha$ biểu thị tuyến tính qua $(e_{m+1},...,e_n)$. Kết hợp điều này với việc

$e_{m+1},...,e_n \in U^{\perp}$, ta suy ra $(e_{m+1},...,e_n)$ là một cơ sở của $U^{\perp}$.



Từ đó, lập luận tương tự ta thấy: nếu $\beta \perp U^{\perp}$, thì $\beta$ biểu thị tuyến tính qua

$(e_1$, ..., $e_m)$, tức là $\beta \in$ U. Như vậy, $(U^{\perp})^{\perp} =$ U.

Cuối cùng, ta có phân tích trực giao

E $= \mathcal{L}(e_1$, ..., $e_m) \oplus^{\perp} \mathcal{L}(e_{m+1}$, ..., $e_n) =$ U $\oplus^{\perp} U^{\perp}$.

$\Box$

Bây giờ ta trở lại với chủ đề khoảng cách trong không gian vécto Euclid.

Khoảng cách từ tập con A tới tập con B của E được định nghĩa như sau:

d(A, B) $= \inf_{\alpha \in$ A, $\beta \in B} d(\alpha$, $\beta)$.

Nói riêng, nếu A chỉ gồm một phần tử $\alpha$ thì ta sẽ ký hiệu đơn giản $d(\{\alpha\},B)$ bởi

$d(\alpha$, B). Như vậy

$d(\alpha$, B) $= \inf_{\beta \in B} d(\alpha$, $\beta)$.

Tập $\alpha$ + U $= {\alpha$ + u | u $\in U}$, trong đó U là một không gian véctor con của E

được gọi là phẳng song song với U và đi qua $\alpha$. Ta sẽ xét trường hợp đặc biệt khi

A và B là những phẳng song song với các không gian véctor con U và V.

Mệnh đề 1.18 Giả sử $\alpha$ - $\beta =$ v + $v^{\perp}$, trong đó v $\in$ V, $v^{\perp} \in V^{\perp}$. Khi đó

$d(\alpha$, $\beta$ + V) $= |v^{\perp}|$.

Tổng quát hơn, nếu $\alpha$ - $\beta =$ t + $t^{\perp}$, trong đó t $\in$ (U + V), $t^{\perp} \in$ (U + $V)^{\perp}$, thì

$d(\alpha$ + U, $\beta$ + V) $= |t^{\perp}|$.

Chứng minh: Rõ ràng $d(\alpha$, $\beta$ + V) là một trường hợp đặc biệt của $d(\alpha$ + U, $\beta$ + V)

với U $= \{0\}$. Theo định nghĩa

$d(\alpha+U,\beta+V)=\inf_{u\in U,v\in V}d(\alpha+u,\beta+v)=\inf_{u\in U,v\in V}|\alpha-\beta+u-v|$.

Dăt u - v $=$ t' $\in$ (U + V). Ta có

$\alpha$ - $\beta$ + t' $= t^{\perp}$ + $(\alpha$ - $\beta$ - $t^{\perp}$ + t').



Vi $(\alpha$ - $\beta$ - $t^{\perp}$ + t') $=$ t + t' $\in$ (U + V), nên $t^{\perp} \perp (\alpha$ - $\beta$ - $t^{\perp}$ + t'). Theo định lý

Pythagore, ta có

$|\alpha$ - $\beta$ + $t'|^2 = |t^{\perp}|^2$ + $|\alpha$ - $\beta$ - $t^{\perp}$ + $t'|^2 > |t^{\perp}|^2$.

Vì thế $d(\alpha$ + U, $\beta$ + V) $= \inf_{t' \in (U+V)} |\alpha$ - $\beta$ + t'| $= |t^{\perp}|$. Giá trị nhỏ nhất này đạt

dược với t' $=$ -t.

$\Box$

Ví dụ: Trong không gian $\mathbf{R}_4$ với tích vô hướng chính tắc, tìm khoảng cách từ

$\alpha =$ (2, 4, -4, 2) tới phẳng B xác định bởi hệ phương trình

x + 2y + z - t $=$ 1,

x + 3y + z - 3t $=$ 2.

Lời giải: Rõ ràng $\beta =$ (0, 1, -1, 0) $\in$ B. Vậy B $= \beta$ + V, trong đó V là không

gian các nghiệm của hệ phương trình thuần nhất

x + 2y + z - t $=$ 0.

x + 3y + z - 3t $=$ 0.

Do đó, $V^{\perp}$ là không gian sinh bởi hai vécto hệ số của hệ phương trình trên: $V^{\perp} =$

$\mathcal{L}((1,2,1,-1),(1,3,1,-3))$. Giả sử $\alpha$ - $\beta =$ (2,3,-3,2) $=$ v + $v^{\perp}$, trong đó v $\in$

V, $v^{\perp} \in V^{\perp}$. Khi đó $v^{\perp}$ thừa nhận phân tích

$v^{\perp} =$ r(1, 2, 1, -1) + s(1, 3, 1, -3) $=$ (r + s, 2r + 3s, r + s, -r - 3s).

Vì thế, véctơ

v $= \alpha$ - $\beta$ - $v^{\perp} =$ (2, 3, -3, 2) - (r + s, 2r + 3s, r + s, -r - 3s)

$=$ (2-r-s, 3-2r-3s, -3-r-s, 2+r+3s)

thoả mãn hệ phương trình xác định V. Tức là

(2-r-s)+2(3-2r-3s)+(-3-r-s)-(2+r+3s) $=$ 3-7r-11s $=$ 0,

(2-r-s)+3(3-2r-3s)+(-3-r-s)-3(2+r+3s) $=$ 2-11r-20s $=$ 0.



Từ đó r $=$ 2, s $=$ -1. Thay các giá trị đó vào $v^{\perp}$ ta có

$d(\alpha$, B) $= |v^{\perp}| =$ |(1, 1, 1, 1)| $=$ 2.

Anh xa trưc giao

$\boldsymbol{2}$

Để nghiên cứu cấu trúc của các không gian vécto Euclid, người ta cần sử dụng

các ánh xạ không chỉ bảo toàn các phép toán trên vécto, mà còn bảo toàn tích vô

hướng.

### Định nghĩa 2.1 Giả sử E và E' là các không gian vécto Euclid. Ánh xạ f: E \to E'

được gọi là một ánh xạ trực giao nếu nó là một ánh xạ tuyến tính và nó bảo toàn

tích vô hướng, nghĩa là:

$\langle f(\alpha)$, $f(\beta) \rangle = \langle \alpha$, $\beta \rangle$, $\quad \forall \alpha$, $\beta \in$ E.

Hiển nhiên là mỗi ánh xạ trực giao đều bảo toàn dộ dài của các vécto:

$|f(\alpha)| = |\alpha|$, $\qquad \forall \alpha \in$ E.

Mệnh đề 2.2 Nếu f: E $\to$ E' bảo toàn tích vô hướng thì nó là một ánh xạ tuyến

tính, và do đó là một ánh xạ trực giao.

Chứng minh: Đặt $\omega = f(a\alpha$ + $b\beta)$ - $af(\alpha)$ - $bf(\beta)$ với a, b $\in \mathbb{R}$, $\alpha$, $\beta \in$ E. Vì f

bảo toàn tích vô hướng, nên với mỗi $\gamma \in$ E, ta có

$\langle \omega$, $f(\gamma) \rangle = \langle f(a\alpha$ + $b\beta)$ - $af(\alpha)$ - $bf(\beta)$, $f(\gamma) \rangle$

$= \langle f(a\alpha$ + $b\beta)$, $f(\gamma) \rangle$ - a $\langle f(\alpha)$, $f(\gamma) \rangle$ - b $\langle f(\beta)$, $f(\gamma) \rangle$

$= \langle a\alpha$ + $b\beta$, $\gamma \rangle$ - $a\langle \alpha$, $\gamma \rangle$ - $b\langle \beta$, $\gamma \rangle =$ 0.

Như thế $\omega$ trực giao với mọi vécto có dạng $f(\gamma)$, do đó $\omega$ trực giao với mọi tổ hợp

tuyến tính của các vécto có dạng $f(\gamma)$. Nói riêng, $\omega \perp \omega$. Từ đó suy ra $\omega =$ 0, hay

là

$f(a\alpha$ + $b\beta) = af(\alpha)$ + $bf(\beta) \quad \forall$ a, b $\in \mathbf{R}$, $\forall \alpha$, $\beta \in$ E.

$\Box$



Mệnh đề 2.3 Giả sử E và E' là các không gian vécto Euclid. Khi đó ánh xạ

tuyến tính f: E $\to$ E' là một ánh xạ trực giao nếu nó biến mỗi cơ sở trực chuẩn

của E thành một hệ trực chuẩn của E'.

Chứng minh: Nếu $(e_1$, ..., $e_n)$ là một cơ sở trực chuẩn của E thì

$ \langle f(e_i), f(e_j) \rangle = \langle e_i, e_j \rangle = \begin{cases} 1, & \text{n\'eu } i = j, \\ 0, & \text{n\'eu } i \neq j. \end{cases} $

$Vậy(f(e_1),...,f(e_n))$ là một hệ trực chuẩn của E'. (Nó có thể không phải là một

cơ sở của E' nếu số chiều của E' lớn hơn n.)

Ngược lại, giả $sử(e_1,...,e_n)là$ một cơ sở trực chuẩn của E,và $(f(e_1),...,f(e_n))$

là một hệ trực chuẩn của E'. Khi đó, với mọi $\alpha = \sum_i a_i e_i$, $\beta = \sum_j b_j e_j$, ta có

$\langle f(\alpha)$, $f(\beta) \rangle = \langle f(\sum_i a_i e_i)$, $f(\sum_j b_j e_j) \rangle$

$= \langle \sum_i a_i f(e_i)$, $\sum_j b_j f(e_j) \rangle$

$= \sum_{i,j} a_i b_j \langle f(e_i)$, $f(e_j) \rangle = \sum_i a_i b_i$

(do tính trực chuẩn của $hệ(f(e_1),...,f(e_n))$

$= \langle \sum_i a_i e_i$, $\sum_j b_j e_j \rangle$

$= \langle \alpha$, $\beta \rangle$.

Như vậy, f là một ánh xạ trực giao.

$\Box$

Mệnh đề 2.4 Mỗi ánh xạ trực giao đều là một đơn cấu tuyến tính. Nói riêng,

n $\in \omega \varphi$ : E $\to$ E là một tự đồng cấu trực giao của một không gian véctơ Euclid hữu

hạn chiều E, thì $\varphi$ là một đẳng cấu tuyến tính.

Chứng minh: Giả sử f: E $\to$ E' là một ánh xạ trực giao. Nếu $f(\alpha) =$ 0 thì

$|\alpha| = |f(\alpha)| =$ 0, nên $\alpha =$ 0. Như thế Ker f $= \{0\}$. Do đó f là một đơn cấu tuyến

tính.



Nếu $\varphi$ : E $\to$ E là một ánh xạ trực giao, thì

$\dim$ E $= \dim Im\varphi$ + $\dim Ker\varphi$.

Vậy dim E $= \dim Im\varphi$. Do đó, $\varphi$ là một toàn cấu. Phần trên của mệnh đề đã

khẳng định $\varphi$ là một đơn cấu. Tóm lại, $\varphi$ là một đẳng cấu tuyến tính.

$\Box$

Theo mệnh đề trên thì mọi ánh xạ trực giao h: E $\to$ E' đều là một đẳng cấu

từ Evào Im(h). Hơn nữa, mọi đẳng cấu trực giao $f:E\rightarrow$ Im(h)đều có dạng

f $= h\varphi$, trong đó $\varphi$ là một tự đẳng cấu trực giao của E. Thật vậy, chỉ cần lấy

$\varphi = h^{-1}f$ : E $\to$ E.

Như vậy, việc nghiên cứu các ánh xạ trực giao có thể quy về việc nghiên cứu

các tự đẳng cấu trực giao (hay còn được gọi là các phép biến đổi trực giao).

Mệnh đề 2.5 Tập hợp O(E) các phép biến đổi trực giao của một không gian

vécto Euclid E lập nên một nhóm đối với phép hợp thành các ánh xạ. Đó là một

nhóm con của nhóm GL(E) tất cả các tự đẳng cấu tuyến tính của E.

Chứng minh: Theo định nghĩa của phép biến đổi trực giao, nếu f, g $\in$ O(E) thì

f $\circ$ g $\in$ O(E).

Giả thiết thêm h $\in$ O(E). Hiển nhiên ta có

(f $\circ$ g) $\circ$ h $=$ f $\circ$ (g $\circ$ h).

Phần tử $id_E \in$ O(E) là đơn vị của phép nhân trong O(E). Thật vậy, với mọi

f $\in$ O(E) ta có

$id_E \circ$ f $=$ f $\circ id_E =$ f.

Anh xạ ngược $f^{-1}$ của f $\in$ O(E) cũng là một phép biến đổi trực giao, tức là

$f^{-1} \in$ O(E), và ta có

f $\circ f^{-1} = f^{-1} \circ$ f $= id_E$.

Mỗi phép biến đổi trực giao đều là một tự đẳng cấu tuyến tính, nghĩa là

O(E) $\subset$ GL(E). Hơn nữa, phép nhân trong O(E) là thu hẹp của phép nhân trong

GL(E). Vậy O(E) là một nhóm con của GL(E).

$\Box$



Dinh nghĩa 2.6 O(E) được gọi là nhóm biến đổi trực giao của không gian vécto

Euclid E.

Mệnh đề sau đây là hiển nhiên

Mệnh đề 2.7 Nếu $\varphi$ là một phép biến đổi trực giao của E thì nó biến mỗi cơ sở

trực chuẩn thành một cơ sở trực chuẩn. Nguợc lại, nếu tự đồng cấu $\varphi$ : E $\to$ E

biến một cơ sở trực chuẩn nào đó thành một cơ sở trực chuẩn thì $\varphi$ là một phép

$bi\acute{e}n\ \tilde{d}\acute{o}i\ true\$ giao.

Giả sử $(e_1$, ..., $e_n)$ là một cơ sở trực chuẩn của không gian vécto Euclid E, và A

là ma trận chuyển từ cơ sở đó sang một cơ sở nào đó $(\varepsilon_1$, ..., $\varepsilon_n)$ của E. Như vậy

$(\varepsilon_1...\varepsilon_n)=(e_1...e_n)A$.

Diều kiện cần và đủ để hệ $(\varepsilon_1$, ..., $\varepsilon_n)$ cũng là một cơ sở trực chuẩn của E là

$\langle \varepsilon_i$, $\varepsilon_j \rangle = \langle \sum_k a_{ki} e_k$, $\sum_k a_{kj} e_k \rangle$

$= \sum_{k=1}^{n} a_{ki} a_{kj} = \delta_{ij}$ (i, j $=$ 1, ..., n).

Nói cách khác

$A^t$ A $= E_n$.

### Định nghĩa 2.8 Ma trận thực A vuông cấp n được gọi là trực giao nếu AtA = E_n,

nói cách khác, nếu hệ vécto cột của A là một hệ trực chuẩn trong $\mathbb{R}^n$ với tích vô

hướng chính tắc.

Theo phân tích ở trên, ta đã chứng minh khẳng định sau đây:

Mệnh đề 2.9 Giả sử A là ma trận chuyển từ một cơ sở trục chuẩn $(e_1$, ..., $e_n)$

sang một cơ sở nào đó $(\varepsilon_1,...,\varepsilon_n)$. Khi đó, $(\varepsilon_1,...,\varepsilon_n)$ cũng là một cơ sở trực chuẩn

nếu và chỉ nếu A là một ma trận trực giao.



Mệnh đề 2.10 Giả sử A là một ma trận thục, vuông cấp n. Khi đó, các tính chất

sau đây là tương đương:

(i) A true giao.

(ii) A khả nghịch và $A^{-1} = A^t$.

(iii) Hệ véctơ hàng của A là trực chuẩn trong $\mathbf{R}_n$ với tích vô hướng chính tắc,

hay là

$AA^t = E_n$.

Chứng minh: Giả sử $A^t$ A $= E_n$. Khi đó $(\det A)^2 = \det(A^t$ A) $= \det E_n =$ 1. Do

đó ma trận A khả nghịch. Nhân hai vế của đẳng thức AtA $= E_n$ với A-1 từ bên

phải, ta thu $đượcA^t=A^tAA^{-1}=E_nA^{-1}=A^{-1}$. Bây giờ lại nhân hai vế của đẳng

thức $A^t = A^{-1}$ với A từ bên trái, ta nhận được A $A^t = E_n$. Như vậy ta đã chứng

minh rằng (i) $\Rightarrow$ (ii) $\Rightarrow$ (iii). Suy luận ngược lại được tiến hành hoàn toàn tương

$\Box$

tự.

Mệnh đề 2.11 Nếu $\varphi$ là một phép biến đổi trực giao của E thì ma trận của nó

trong mỗi cơ sở trực chuẩn của E là một ma trận trực giao. Nguợc lại, nếu $\varphi$ có

ma trận trong một cơ sở trực chuẩn nào đó của E là một ma trận trực giao thì $\varphi$

là một phép biến đổi trực giao.

Chứng minh: Giả sử $\varphi$ là một phép biến đổi trực giao và $(e_1$, ..., $e_n)$ là một cơ sở

trực chuẩn của E. Khi đó $(\varphi(e_1)$, ..., $\varphi(e_n))$ cũng là một cơ sở trực chuẩn. Gọi A

là ma trận của $\varphi$ trong cơ sở $(e_1,...,e_n)$. Khi đó, Achính là ma trận chuyển từ cơ

sở $(e_1$, ..., $e_n)$ tới cơ sở $(\varphi(e_1)$, ..., $\varphi(e_n))$. Theo Mệnh đề 2.9, A là một ma trận trực

giao.

Ngược lại, nếu $\varphi$ có ma trận A trong một cơ sở trực chuẩn nào đó $(e_1$, ..., $e_n)$ là

một ma trận trực giao, thì cũng theo Mệnh đề 2.9 $(\varphi(e_1)$, ..., $\varphi(e_n)) = (e_1$, ..., $e_n)A$

là một cơ sở trực chuẩn. Do đó, $\varphi$ là một phép biến đổi trực giao.

$\Box$



Hệ quả 2.12 Tập hợp O(n) các ma trận trực giao cấp n lập nên một nhóm đối

với phép nhân ma trận. Đó là một nhóm con của nhóm GL(n, $\mathbf{R})$ các ma trận thực

$c\tilde{a}p$ n khả nghịch.

Chứng minh: Cố định một cơ sở trực chuẩn $(e_1$, ..., $e_n)$ của không gian véctor

Euclid n chiều E. Khi đó, mỗi phần tử $\varphi \in$ O(E) được đặt tương ứng 1-1 với ma

trận của nó $A_{\varphi} \in$ O(n) trong cơ sở nói trên. Tương ứng này bảo toàn phép toán,

nghĩa là

$A_{\varphi \circ \psi} = A_{\varphi} \circ A_{\psi}$.

Vì O(E) là một nhóm, nên O(n) cũng vậy. Ngoài ra, ta có

GL(E) $\longleftrightarrow GL(n,\mathbf{R})$

$\bigcup$

$\bigcup$

O(E)

O(n).

$\longleftrightarrow$

$\Box$

Dinh nghĩa 2.13 O(n) được gọi là nhóm các ma trận trực giao cấp n.

Mệnh đề 2.14 Nếu A là một ma trận trực giao thì

$\det$ A $= \pm$ 1.

Chứng minh: Từ đẳng thức $AA^t = E_n$, ta có

1 $=$ det $E_n = \det(AA^t) = \det$ A $\det A^t = (\det A)^2$.

Kết quả là det A $= \pm$ 1.

$\Box$

Mệnh đề 2.15 SO(E) $= \{ \varphi \in$ O(E) | $\det \varphi =$ 1 $\}$ và SO(n) $= \{$ A $\in$ O(n) | $\det$ A $=$

$1}$ là các nhóm con tương ứng của O(E) và O(n).



Chứng minh: Nếu $\varphi$, $\psi \in$ SO(E) thì $\varphi \psi \in$ O(E) và

$\det(\varphi\psi) = \det\varphi \cdot \det\psi =$ 1 $\cdot$ 1 $=$ 1.

Như thế, theo định nghĩa, $\varphi \psi \in$ SO(E).

Nếu $\varphi \in$ SO(E) thì $\varphi^{-1} \in$ O(E) và

$\det(\varphi^{-1}) = (\det \varphi)^{-1} = 1^{-1} =$ 1.

Từ đó $\varphi^{-1} \in$ SO(E).

Tóm lại SO(E) là một nhóm con của nhóm O(E).

Trường hợp SO(n) được chứng minh tương tự.

$\Box$

Kết quả là ta có biểu đồ sau đây:

GL(E)

$GL(n,\mathbf{R})$

$\longleftrightarrow$

$\bigcup$

$\bigcup$

O(E)

O(n)

$\longleftrightarrow$

$\bigcup$

$\bigcup$

SO(n).

SO(E)

$\longleftrightarrow$

SO(E) được gọi là nhóm biến đổi trực giao đặc biệt của E, còn SO(n) được

gọi là nhóm các ma trận trực giao đặc biệt cấp n.

Bây giờ ta xét cấu trúc của một phép biến đổi trực giao.

Mệnh đề 2.16 Nếu $\varphi$ là một phép biến đổi trực giao, thì mọi giá trị riêng (nếu

có) của $\varphi$ đều bằng $\pm$ 1. Các không gian con riêng $P_1(\varphi)$ và $P_{-1}(\varphi)$ (nếu có) của

$\varphi$ (ứng với các giá trị riêng 1 và -1) trực giao với nhau.

Chứng minh: Giả sử $\alpha$ là một vécto riêng ứng với giá trị riêng $\lambda$ của $\varphi$, nghĩa là

$\varphi(\alpha) = \lambda \alpha$. Ta có

$\langle \alpha$, $\alpha \rangle = \langle \varphi(\alpha)$, $\varphi(\alpha) \rangle = \langle \lambda \alpha$, $\lambda \alpha \rangle = \lambda^2 \langle \alpha$, $\alpha \rangle$.



Vì $\alpha \neq$ 0, nên $\lambda^2 =$ 1. Do đó, $\lambda = \pm$ 1.

Giả sử $\alpha \in P_1(\varphi)$, $\beta \in P_{-1}(\varphi)$. Ta có

$\langle \alpha$, $\beta \rangle = \langle \varphi(\alpha)$, $\varphi(\beta) \rangle = \langle \alpha$, $-\beta \rangle = -\langle \alpha$, $\beta \rangle$.

Từ đó $\langle \alpha$, $\beta \rangle =$ 0 và $\alpha \perp \beta$.

$\Box$

Mệnh đề 2.17 (i) A $\in$ O(1) nếu và chỉ nếu A $= (\pm$ 1).

(ii) A $\in$ O(2) nếu và chỉ nếu A là một trong hai ma trận dạng sau đây

$ A_1 = \begin{pmatrix} \cos \omega & -\sin \omega \\ \sin \omega & \cos \omega \end{pmatrix}, A_2 = \begin{pmatrix} \cos \omega & \sin \omega \\ \sin \omega & -\cos \omega \end{pmatrix}. $

Ma trận $A_1$ chéo hoá được nếu và chỉ nếu $\omega = k\pi$ với k $\in \mathbb{Z}$. Ma trận $A_2$

luôn chéo hoá được nhờ một ma trận trực giao. Nói rõ hơn, tồn tại Q $\in$ O(2)

sao cho

$ Q^{-1}A_2Q = \left(\begin{array}{cc} 1 & 0 \\ 0 & -1 \end{array}\right). $

Chứng minh: (i) A $=$ (a) $\in$ O(1) nếu và chỉ nếu $a^2 =$ 1, tức là a $= \pm$ 1.

$ (ii) Giả sửA = \left( \begin{array}{cc} a & c \\ b & d \end{array} \right). Khi đó,A \in O(2)nếu và chỉ nếu $

$a^{2}$ + $b^{2} =$ 1, $c^{2}$ + $d^{2} =$ 1, ac + bd $=$ 0.

Hai đẳng thức cuối chứng tỏ (c, d) là nghiệm duy nhất của hệ phương trình tuyến

tính không suy biến

$ \begin{cases}\nax + by &= 0, \\
\infty, & 1\n\end{cases} $

cx + ay - 1.

Theo quy tắc Cramer, ta có

$ c = \frac{\det \left(\begin{array}{cc} 0 & b \ 1 & d \end{array}\right)}{\det A} = -\frac{b}{\det A}, d = \frac{\det \left(\begin{array}{cc} a & 0 \ c & 1 \end{array}\right)}{\det A} = \frac{a}{\det A}. $

ററ



Ta xét hai trường hợp:

Trường hợp 1: det A $=$ 1. Khi đó c $=$ -b, d $=$ a. Kết quả là

$ A = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}, với a^2 + b^2 = 1. $

Dăt a $= \cos \omega$, b $= \sin \omega$, ta thu được

$ A = \begin{pmatrix} \cos \omega & -\sin \omega \\ \sin \omega & \cos \omega \end{pmatrix}. $

Da thức đặc trưng của A bằng $X^2$ - $2\cos\omega$ X + 1. Nó có nghiệm thực nếu và chỉ

nếu $\Delta' = -\sin^2 \omega \ge$ 0, hay là $\omega = k\pi$ với k là một số nguyên. Khi đó

$ A = \left( \begin{array}{cc} \pm 1 & 0 \\ 0 & \pm 1 \end{array} \right). $

Trường hợp 2: det A $=$ -1. Khi đó c $=$ b, d $=$ -a, và

$ A = \begin{pmatrix} a & b \\ b & -a \end{pmatrix}, với a^2 + b^2 = 1. $

Dăt a $= \cos \omega$, b $= \sin \omega$, ta có

$ A = \left( \begin{array}{cc} \cos \omega & \sin \omega \\ \sin \omega & -\cos \omega \end{array} \right). $

Da thức đặc trưng của A là

$ det \begin{pmatrix} \cos \omega - X & \sin \omega \\ \sin \omega & -\cos \omega - X \end{pmatrix} = X^2 - (\cos^2 \omega + \sin^2 \omega) = X^2 - 1 = (X - 1)(X + 1). $

Vây A có hai giá tri riêng là 1 và -1.

Giả sử $\varphi$ là phép biến đổi trực giao của $\mathbb{R}^2$ có ma trận là A trong cơ sở chính

tắc. Gọi $\alpha$ và $\beta$ là các vécto riêng có độ dài bằng đơn vị của $\varphi$ ứng với các giá trị

riêng 1 và -1. Ta biết rằng $\alpha \perp \beta$. Vậy $(\alpha$, $\beta)$ là một cơ sở trực chuẩn của $\mathbb{R}^2$.



Nếu Q là ma trận chuyển từ cơ sở chính tắc của $\mathbb{R}^2$ sang cơ sở $(\alpha$, $\beta)$ thì Q $\in$ O(2)

$\mathbf{v}\grave{\mathbf{a}}$

$ Q^{-1}AQ = \left(\begin{array}{cc} 1 & 0 \\ 0 & -1 \end{array}\right). $

Phép biến đổi trực giao $\varphi$ của không gian vécto Euclid hai chiều E có ma trận

dang

$ \begin{pmatrix} \cos \omega & -\sin \omega \\ \sin \omega & \cos \omega \end{pmatrix}, \text{hoac} \begin{pmatrix} \cos \omega & \sin \omega \\ \sin \omega & -\cos \omega \end{pmatrix} $

trong một cơ sở trực chuẩn nào đó được gọi thứ tự là phép quay góc $\omega$ xung quanh

$g\tilde{o}c$ toa đô và phép đối xứng truc.

Mệnh đề 2.18 Giả sử $\varphi$ là một phép biến đổi trực giao của không gian vécto

Euclid E. Khi đó, nếu U $\subset$ E là một không gian véctơ con $\varphi-ổn$ định thì $U^{\perp}$ cũng

$v\hat{a}y$.

Chứng minh: $\varphi|_U:$ U $\to$ U là một phép biến đổi trực giao, nên nó là một đẳng

cấu tuyến tính. Nói riêng, $\varphi(U) =$ U. Với mỗi u $\in$ U, có một t $\in$ U nào đó sao cho

u $= \varphi(t)$. Giả sử v $\in U^{\perp}$. Ta có

$\langle \varphi(v)$, u $\rangle = \langle \varphi(v)$, $\varphi(t) \rangle = \langle$ v, t $\rangle =$ 0.

Nghĩa là $\varphi(v) \in U^{\perp}$.

$\Box$

Mệnh đề 2.19 Giả sử $\varphi \in$ O(E), trong đó E hữu hạn chiều. Khi đó, tồn tại một

co sở trực chuẩn của E sao cho ma trận của $\varphi$ trong cơ sở này có dạng

$ E_p \oplus (-E_q) \oplus \begin{pmatrix} \cos \omega_1 & -\sin \omega_1 \\ \sin \omega_1 & \cos \omega_1 \end{pmatrix} \oplus \cdots \oplus \begin{pmatrix} \cos \omega_r & -\sin \omega_r \\ \sin \omega_r & \cos \omega_r \end{pmatrix} $



$=$

$-\sin \omega_1$

$\cos \omega_1$

$\sin \omega_1$

$\cos \omega_1$

$\mathcal{O}_{\mathcal{A}_{\mathcal{A}}}$

$\theta$

$-\sin \omega_r$

$\cos \omega_r$

$\sin \omega_r \cos \omega_r$

trong đó $\omega_1$, ..., $\omega_r$ là những số thực khác $k\pi$ (k $\in \mathbb{Z})$.

Chứng minh: Áp dụng mệnh đề trước và nhớ rằng mỗi phép biến đổi tuyến tính

thực đều có không gian con ổn định một hoặc hai chiều, ta nhận được phân tích

truc giao

E $= U_1 \oplus^{\perp} \cdots \oplus^{\perp} U_m$

trong đó mỗi $U_i$ là một không gian con $\varphi-ổn$ định một hoặc hai chiều. Bây giờ ta

áp dụng Mệnh đề 2.17 cho $\varphi|_{U_i}$. Nhớ rằng mọi phép đối xứng trục hoặc phép quay

góc $k\pi$ đều có thể chéo hoá được. Vì thế, $\varphi$ có ma trận như nói trong mệnh đề

trong một cơ sở trực chuẩn nào đó của E.

$\Box$

### Định nghĩa 2.20 Ma trận nói ở Mệnh đề 2.19

$ E_p \oplus (-E_q) \oplus \begin{pmatrix} \cos \omega_1 & -\sin \omega_1 \\ \sin \omega_1 & \cos \omega_1 \end{pmatrix} \oplus \cdots \oplus \begin{pmatrix} \cos \omega_r & -\sin \omega_r \\ \sin \omega_r & \cos \omega_r \end{pmatrix} $

duoc goi là ma trận trực giao dạng chính tắc.



Hệ quả 2.21 Với mỗi ma trận trực giao A cấp n, có một ma trận trực giao Q

cùng cấp n sao cho $Q^{-1}AQ = Q^tAQ$ là ma trận trực giao dạng chính tắc.

Ví dụ: Tìm dạng chính tắc B của ma trận trực giao

$ A = \left( \begin{array}{ccc} \frac{2}{3} & -\frac{1}{3} & \frac{2}{3} \\[1mm] \frac{2}{3} & \frac{2}{3} & -\frac{1}{3} \\[1mm] -\frac{1}{3} & \frac{2}{3} & \frac{2}{3} \end{array} \right). $

và ma trận trực giao Q sao cho B $= Q^{-1}AQ$.

Lời giải: Trước hết ta tìm đa thức đặc trưng của A:

$ P_A(X) = \det \begin{pmatrix} \frac{2}{3} - X & -\frac{1}{3} & \frac{2}{3} \\ \frac{2}{3} & \frac{2}{3} - X & -\frac{1}{3} \\ -\frac{1}{3} & \frac{2}{3} & \frac{2}{3} - X \end{pmatrix} = -(X-1)(X^2 - X + 1). $

Da thức này có 3 nghiệm: $X_1 =$ 1, $X_{2,3} = \frac{1 \pm \sqrt{3}i}{2}$.

Gọi $\varphi$ là phép biến đổi tuyến tính của $\mathbb{R}^3$ có ma trận là A trong cơ sở chính

tắc. Vécto riêng $e_1 =$ (x, y, $z)^t$ của $\varphi$ ứng với giá trị riêng $X_1 =$ 1 là nghiệm của hệ

phương trình

$ \begin{cases}\n(\frac{2}{3} - 1)x - \frac{1}{3}y + \frac{2}{3}z &= 0 \\
\frac{2}{3}x + (\frac{2}{3} - 1)y - \frac{1}{3}z &= 0 \\
-\frac{1}{3}x + \frac{2}{3}y + (\frac{2}{3} - 1)z &= 0.\n\end{cases} $

Từ đó suy ra x $=$ y $=$ z. Nếu ta đòi hỏi thêm $e_1$ có độ dài đơn vị thì x $=$ y $=$ z $=$ z

$\pm \frac{1}{\sqrt{3}}$. Ta chọn $e_1 = (\frac{1}{\sqrt{3}}$, $\frac{1}{\sqrt{3}}$, $\frac{1}{\sqrt{3}})^t$.

Tiếp theo, ta xét không gian $\varphi-ổn$ định hai chiều ứng với các nghiệm phức liên

hợp $X_{2,3} = \frac{1 \pm \sqrt{3}i}{2}$ của $P_A(X)$. Muốn thế, ta tìm nghiệm phức của hệ phương trình:

$ \begin{cases}\n(\frac{2}{3}-\frac{1+\sqrt{3}i}{2})x-\frac{1}{3}y+\frac{2}{3}z &= 0\\ \n\frac{2}{3}x+(\frac{2}{3}-\frac{1+\sqrt{3}i}{2})y-\frac{1}{3}z &= 0\\ \n-\frac{1}{3}x+\frac{2}{3}y+(\frac{2}{3}-\frac{1+\sqrt{3}i}{2})z &= 0.\n\end{cases} $



Hề này có ho nghiêm phu thuộc một tham số phức t:

x $=$ -2t, y $=$ (1 + $\sqrt{3}i)t$, z $=$ (1 - $\sqrt{3}i)t$.

Chọn t $=$ 1 và tách riêng phần thực và phần do của vécto nghiệm, ta thu được hai

vécto

$e'_2 =$ (-2, 1, $1)^t$, $e'_3 =$ (0, $\sqrt{3}$, $-\sqrt{3})^t$.

Hai véc tơ này trực giao với nhau. Ta chuẩn hoá chúng để có một hệ trực chuẩn :

$e_2 = \left(-\frac{\sqrt{2}}{\sqrt{3}}$, $\frac{1}{\sqrt{6}}$, $\frac{1}{\sqrt{6}}\right)^t$, $e_3 = \left(0$, $\frac{1}{\sqrt{2}}$, $-\frac{1}{\sqrt{2}}\right)^t$.

Theo chứng minh Định lý IV.2.2 ta có

$ (\varphi(e_2) \varphi(e_3)) = (e_2 \ e_3) \left( \begin{array}{cc} \frac{1}{2} & \frac{\sqrt{3}}{2} \\ -\frac{\sqrt{3}}{2} & \frac{1}{2} \end{array} \right). $

Như vậy, trong cơ sở trực chuẩn $(e_1$, $e_2$, $e_3)$ phép biến đổi $\varphi$ có ma trận dạng chính

tac

$ B = \left(\begin{array}{ccc} 1 & 0 & 0 \\ 0 & \frac{1}{2} & \frac{\sqrt{3}}{2} \\ 0 & -\frac{\sqrt{3}}{2} & \frac{1}{2} \end{array}\right). $

Ma trận chuyển Q từ cơ sở chính tắc của $\mathbb{R}^3$ sang cơ sở trực chuẩn $(e_1$, $e_2$, $e_3)$ chính

là ma trận trực giao với các cột là các vécto tọa độ của $e_1$, $e_2$, $e_3:$

$ Q = \begin{pmatrix} \frac{1}{\sqrt{3}} & -\frac{\sqrt{2}}{\sqrt{3}} & 0 \\ \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} \end{pmatrix}. $

Hiển nhiên là B $= Q^{-1}AQ$.

Phép biến đổi liên hợp và phép biến đổi đối

$3<sup>1</sup>$

xứng

Để định nghĩa được phép biến đổi liên hợp, ta cần bổ đề sau đây.



Bổ đề 3.1 Giả sử $\ell$ : E $\to \mathbf{R}$ là một dạng tuyến tính trên không gian vécto Euclid

hữu hạn chiều E. Khi đó tồn tại duy nhất vécto $\alpha \in$ E sao cho $\ell(x) = \langle$ x, $\alpha \rangle$ với

moi x $\in$ E.

Chứng minh: Tính duy nhất: Giả sử có các vécto $\alpha$, $\beta \in$ E sao cho

$\ell(x) = \langle$ x, $\alpha \rangle = \langle$ x, $\beta \rangle$, $\quad \forall$ x $\in$ E.

Khi đó $\langle$ x, $\alpha$ - $\beta \rangle =$ 0 với mọi x $\in$ E. Nói riêng

$|\alpha$ - $\beta|^2 = \langle \alpha$ - $\beta$, $\alpha$ - $\beta \rangle =$ 0.

Do đó $\alpha = \beta$.

$\Box$

Sự tồn tại: Nếu $\ell =$ 0 thì ta chọn $\alpha =$ 0. Ngược lại, nếu $\ell \neq$ 0, thì $Im(\ell) = \mathbf{R}$.

Ta có

$\dim$ E $= \dim$ Ker $\ell$ + $\dim \mathbf{R}$.

Ký hiệu n $= \dim$ E, ta có dim Ker $\ell =$ n - 1. Do đó, không gian (Ker $\ell)^{\perp}$ có số

chiều bằng 1. Gọi e $\in (Ker\ell)^{\perp}$ là một vécto với độ dài đơn vị |e| $=$ 1. Như thế,

e $\neq$ 0, và (Ker $\ell)^{\perp} = \mathcal{L}(e)$. Ta đặt $\alpha = \ell(e) \cdot$ e $\in$ E. Mỗi x $\in$ E đều có phân tích

x $=$ te + z (t $\in \mathbf{R}$, z $\in$ Ker $\ell)$.

Ta có

$\langle$ x, $\alpha \rangle = \langle$ te + z, $\ell(e) \cdot$ e $\rangle = \langle$ te, $\ell(e) \cdot$ e $\rangle = t\ell(e)\langle$ e, e $\rangle$

$= t\ell(e) = \ell(te) = \ell(te$ + z) $= \ell(x)$.

$\Box$

Hệ quả 3.2 Giả sử E là một không gian vécto Euclid hữu hạn chiều. Khi đó ánh

$x\alpha$ f : E $\to E^*$ đặt tương ứng mỗi $\alpha$ với $f_\alpha \in E^*$ xác định bởi hệ thức

$f_{\alpha}(x) = \langle$ x, $\alpha \rangle$, $\quad \forall$ x $\in$ E

là một đẳng cấu tuyến tính.



Chứng minh: Rõ ràng $f_{\alpha}$ xác định bởi hệ thức trên là một dạng tuyến tính trên

E. Hơn nữa, dễ kiểm tra rằng

$ \begin{cases} f_{\alpha+\beta} = f_{\alpha} + f_{\beta}, & \alpha, \beta \in E, \\ f_{a\alpha} = af_{\alpha}, & a \in \mathbf{R}, \alpha \in E. \end{cases} $

Nói cách khác, f: E $\to E^*$ là một ánh xạ tuyến tính. Sự tồn tại và tính duy nhất

của vécto $\alpha$ nói ở bổ đề trước chứng tỏ f là một đẳng cấu.

$\Box$

Anh xạ f được gọi là đẳng cấu chính tắc giữa E và $E^*$. Nó được định nghĩa

không phụ thuộc vào cơ sở của E. Nếu ta viết $f_{\alpha}(x)$ dưới dạng $\langle$ x, $f_{\alpha} \rangle$, trong đó

$\langle\cdot,\cdot\rangle:E\times E^*\to{\mathbf R}$ là ghép cặp đối ngẫu giữaEvà $E^*,thì$ hệ thức xác $địnhf_\alpha$ trở

thành

$\langle$ x, $f_{\alpha} \rangle = \langle$ x, $\alpha \rangle$.

Như thế, đẳng cấu f cho phép đồng nhất ghép cặp đối ngẫu giữa E và $E^*$ với tích

vô hướng trong E.

Bây giờ giả sử $\varphi$ : E $\to$ E là một phép biến đổi tuyến tính. Với mỗi $\beta$ cố định

trong E, tương ứng

E $\rightarrow \mathbf{R}$

$\alpha \mapsto \langle \varphi(\alpha)$, $\beta \rangle$

là một dạng tuyến tính trên E. Do đó, theo Bổ đề 3.1, có duy nhất phần tử được

ký hiệu là $\varphi^*(\beta)$ trong E sao cho

$\langle \varphi(\alpha)$, $\beta \rangle = \langle \alpha$, $\varphi^*(\beta) \rangle$.

Ta dễ kiểm tra lại rằng ánh xạ

$\varphi^*$ : E $\rightarrow E\beta \mapsto \varphi^*(\beta)$

là một ánh xa tuyến tính.



Dinh nghĩa 3.3 $\varphi^*$ được gọi là phép biến đổi liên hợp của $\varphi$.

Phép biến đổi liên hợp có những tính chất sau đây:

Mệnh đề 3.4 Với mọi $\varphi$, $\psi \in \mathcal{L}(E$, E), a $\in \mathbb{R}$, ta có

(i) $(\varphi$ + $\psi)^* = \varphi^*$ + $\psi^*$,

$(a\varphi)^* = a\varphi^*$.

(ii) $(\varphi^*)^* = \varphi$.

(iii) $(\varphi \psi)^* = \psi^* \varphi^*$.

(iv) Nếu $\varphi$ khả nghịch thì $\varphi^*$ cũng vậy, và

$(\varphi^{-1})^* = (\varphi^*)^{-1}$.

Chứng minh: Ta chỉ chứng minh tính chất (iii). Các phần còn lại được coi như

bài tập. Theo định nghĩa, với mọi $\alpha$, $\beta \in$ E, ta có

$\langle \varphi \psi(\alpha)$, $\beta \rangle = \langle \alpha$, $(\varphi \psi)^*(\beta) \rangle$.

Mặt khác

$\langle \varphi \psi(\alpha)$, $\beta \rangle = \langle \psi(\alpha)$, $\varphi^*(\beta) \rangle = \langle \alpha$, $\psi^* \varphi^*(\beta) \rangle$.

Vì $\langle \alpha$, $(\varphi \psi)^*(\beta) \rangle = \langle \alpha$, $\psi^* \varphi^*(\beta) \rangle$ vói mọi $\alpha$, $\beta \in$ E, cho nên ta có $(\varphi \psi)^* = \psi^* \varphi^*$. $\Box$

Mệnh đề 3.5 Nếu A là ma trận của $\varphi$ trong một cơ sở trực chuẩn nào đó của

E, thì $A<sup>t</sup>$ là ma trận của $\varphi^*$ trong cùng cơ sở ấy.

Chứng minh: Giả sử $\varphi$ và $\varphi^*$ có ma trận lần lượt là A $= (a_{ij})$ và B $= (b_{ij})$ trong

co sở trực chuẩn $(e_1$, ..., $e_n)$ của E. Ta có

$\langle \varphi(e_j)$, $e_i \rangle = \langle \sum_{k=1}^n a_{kj} e_k$, $e_i \rangle = \sum_{k=1}^n a_{kj} \langle e_k$, $e_i \rangle = a_{ij}$.



Tuong tu

$\langle e_i$, $\varphi^*(e_i) \rangle = \langle \varphi^*(e_i)$, $e_i \rangle = b_{ii}$

Điều kiện $\langle \varphi(e_i)$, $e_i \rangle = \langle e_i$, $\varphi^*(e_i) \rangle$ tương đương với $a_{ij} = b_{ji}$ với mọi i, j, hay là

$B=A^t$. $\Box$

Dinh nghĩa sau đây đưa ra một lớp các ánh xạ tuyến tính quan trọng.

### Định nghĩa 3.6 (i) Phép biến đổi tuyến tính \varphi : E \to E được gọi là một phép

biến đổi đối xúng (hay tự liên hợp) nếu $\varphi = \varphi^*$, tức là

$\langle \varphi(\alpha)$, $\beta \rangle = \langle \alpha$, $\varphi(\beta) \rangle$, $\quad \forall \alpha$, $\beta \in$ E.

(ii) Ma trận vuông A được gọi là đối xứng nếu A $= A^t$.

Hệ quả 3.7 Nếu phép biến đổi tuyến tính $\varphi$ : E $\to$ E là đối xứng thì ma trận của

nó trong mọi cơ sở trực chuẩn của E là ma trận đối xứng. Nguợc lại, nếu phép

biến đổi tuyến tính $\varphi$ có ma trận đối xứng trong một cơ sở trực chuẩn nào đó của

E thì $\varphi$ là đối xứng.

Chứng minh: Ta dùng các ký hiệu của mệnh đề trước. Khi đó, $\varphi$ đối xứng (tức

là $\varphi = \varphi^*)$ nếu và chỉ nếu A $= A^t$.

$\Box$

Mệnh đề 3.8 Các không gian con riêng ứng với những giá trị riêng khác nhau

của một phép biến đổi đối xứng là trực giao với nhau.

Chứng minh: Giả sử $\alpha$ và $\beta$ là các vécto riêng của phép biến đổi đối xứng $\varphi$ ứng

với các giá trị riêng khác nhau $\lambda$ và $\mu$. Nghĩa là $\varphi(\alpha) = \lambda \alpha$, $\varphi(\beta) = \mu \beta \ (\lambda \neq \mu)$. Ta

$\overline{\text{co}}$

$\langle \varphi(\alpha)$, $\beta \rangle = \langle \alpha$, $\varphi(\beta) \rangle$

$\iff \quad \langle \lambda \alpha$, $\beta \rangle = \langle \alpha$, $\mu \beta \rangle$

$\iff (\lambda$ - $\mu)\langle \alpha$, $\beta \rangle =$ 0

$\iff \quad \langle \alpha$, $\beta \rangle =$ 0.



Mệnh đề 3.9 Mọi giá trị riêng của một ma trận thực đối xứng bất kỳ đều là số

thwc.

Chứng minh: Giả sử A $= (a_{ij})$ là một ma trận thực đối xứng bất kỳ, có cấp n.

Giả sử $\lambda$ là một nghiệm phức của phương trình đặc trưng

$\det(A$ - X $E_n) =$ 0.

Hệ phương trình $\sum_{j=1}^n a_{ij}x_j$ - $\lambda x_i =$ 0 (i $=$ 1, ..., n) có định thức $\det(A$ - $\lambda E_n) =$ 0,

nên hệ đó có một nghiệm phức không tầm thường $(b_1$, ..., $b_n)$. Tức là

$\sum_{j=1}^{n} a_{ij} b_j = \lambda b_i$ (i $=$ 1, ..., n).

Nhân hai về của đẳng thức trên với liên hợp phức $\overline{b_i}$ của $b_i$ rồi cộng lại theo i, ta

$\overline{c}$

$\sum_{i,j=1}^n a_{ij}b_j\overline{b_i} = \lambda \sum_{i=1}^n b_i\overline{b_i} = \lambda (\sum_{i=1}^n |b_i|^2)$.

Hệ số $\sum_{i=1}^n |b_i|^2$ là một số thực, nên để chứng minh $\lambda$ là thực ta chỉ cần chứng minh

vế trái cũng là một số thực. Ta có

$\overline{\sum_{i,j=1}^n a_{ij} b_j \overline{b_i}} = \sum_{i,j=1}^n \overline{a_{ij} b_j \overline{b_i}} = \sum_{i,j=1}^n a_{ij} \overline{b_j} b_i$

$= \sum_{i,j=1}^n a_{ji} \overline{b_j} b_i$ (do A đối xứng)

$= \sum_{i,j=1}^n a_{ij} \overline{b_i} b_j = \sum_{i,j=1}^n a_{ij} b_j \overline{b_i}$.

$\Box$

Bổ đề 3.10 Giả sử $\varphi$ là một phép biến đổi đối xúng của E. Nếu U là một không

gian véctor con $\varphi-ổn$ định của E thì $U^{\perp}$ cũng vậy.

Chứng minh: Nếu u $\in$ U thì $\varphi(u) \in$ U. Với mọi v $\in U^{\perp}$, ta có

$\langle$ u, $\varphi(v) \rangle = \langle \varphi(u)$, v $\rangle =$ 0.

Do đó $\varphi(v) \in U^{\perp}$.

$\Box$

Dinh lý 3.11 Phép biến đổi tuyến tính $\varphi$ của không gian véctor Euclid hữu hạn

chiều E là đối xứng nếu và chỉ nếu có một cơ sở trực chuẩn của E gồm toàn

những vécto riêng của $\varphi$.



Chứng minh: Nếu E có một cơ sở trực chuẩn gồm những vécto riêng của $\varphi$ thì

ma trận của $\varphi$ trong cơ sở đó là một ma trận chéo, và do đó đối xứng. Vì thế $\varphi$

đối xứng.

Ngược lại, giả sử $\varphi$ đối xứng, ta sẽ chứng minh bằng quy nạp theo n $= \dim$ E

rằng có một cơ sở trực chuẩn của E gồm toàn những véctơ riêng của $\varphi$. Kết luận

là hiển nhiên với n $=$ 1, vì khi đó mỗi vécto khác 0 trong E đều là vécto riêng của

$\varphi$. Giả sử quy nạp rằng kết luận đúng với mọi không gian có số chiều nhỏ hơn n.

Theo Mệnh đề 3.9, $\varphi$ có một giá trị riêng thực $\lambda_1$. Gọi $e_1$ là một vécto riêng có

độ dài bằng 1, ứng với giá trị riêng $\lambda_1$. Khi đó $\mathcal{L}(e_1)$ là một không gian vécto con

$\varphi-ổn$ định. Theo bổ đề trên, không gian $\mathcal{L}(e_1)<sup>\perp</sup>$ cũng là $\varphi-ổn$ định. Ngoài ra, ta có

$\dim \mathcal{L}(e_1)^{\perp} = \dim$ E - 1 $=$ n - 1 $<$ n.

Theo giả thiết quy nạp, có một cơ sở trực chuẩn $(e_2$, ..., $e_n)$ của $\mathcal{L}(e_1)^\perp$ gồm toàn

những vécto riêng của $\varphi$. Khi đó $(e_1$, $e_2$, ..., $e_n)$ là co sở trực chuẩn của E cũng gồm

toàn những vécto riêng của $\varphi$.

$\Box$

Hệ quả 3.12 Mọi ma trận thực đối xứng đều chéo hoá được nhờ các ma trận

trực giao. Cụ thể hơn, nếu A là một ma trận thực đối xúng, thì tồn tại ma trận

trực giao Q $\$, $d\hat{e}$ cho

B $= Q^{-1}$ A Q $= Q^t$ A Q

là một ma trận chéo.

Chứng minh: Chọn một không gian vécto Euclid E số chiều n, là số hàng và số

cột của ma trận A. Gọi $\varphi$ là tự đồng cấu của E nhận A làm ma trận trong một cơ

sở trực chuẩn nào đó $(e_1$, ..., $e_n)$ của E. Khi đó $\varphi$ là một phép biến đổi đối xứng,

vì A là đối xứng.

Theo Định lý 3.11, có một cơ sở trực chuẩn $(\varepsilon_1$, ..., $\varepsilon_n)$ của E gồm toàn những

vécto riêng của $\varphi$. Ma trận B của $\varphi$ trong cơ sở này tất nhiên là một ma trận chéo.



Bây giờ gọiQlà ma trận chuyển từ cơ sở trực chuẩn $(e_1,...,e_n)$ sang cơ sở trực

chuẩn $(\varepsilon_1$, ..., $\varepsilon_n)$. Khi đó, Q là một ma trận trực giao. Hơn nữa, ta có

B $= Q^{-1}AQ = Q^tAQ$.

Tìm một ma trận trực giao Q làm chéo hoá ma trận đối xứng sau đây:

Ví du:

$ A = \left( \begin{array}{rrrr} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 1 & -1 \\ 1 & -1 & -1 & 1 \end{array} \right). $

Lời giải: Trước hết ta tìm đa thức đặc trưng của A:

$ det \begin{pmatrix} 1-X & 1 & 1 & 1 \\ 1 & 1-X & -1 & -1 \\ 1 & -1 & 1-X & -1 \\ 1 & -1 & -1 & 1-X \end{pmatrix} = (X-2)^3(X+2). $

Sau đó, ta tìm vécto riêng của A ứng với giá trị riêng $\lambda_4 =$ -2:

$ (A + 2E_4) \begin{pmatrix} x \\ y \\ z \\ t \end{pmatrix} = \begin{pmatrix} 3x + y + z + t \\ x + 3y - z - t \\ x - y + 3z - t \\ x - u - z + 3t \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}. $

Hệ này có họ nghiệm phụ thuộc một tham số -x $=$ y $=$ z $=$ t. Véctor $e_4 =$

$\left(-\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2}\right)^t$ thoả mãn hệ phương trình đó và có độ dài bằng đơn vị.

Tiếp theo, ta tìm các vécto riêng của A ứng với giá trị riêng $\lambda_1 = \lambda_2 = \lambda_3 =$ 2:

$ (A - 2E_4) \begin{pmatrix} x \\ y \\ z \\ t \end{pmatrix} = \begin{pmatrix} -x + y + z + t \\ x - y - z - t \\ x - y - z - t \\ x - y - z - t \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}. $



Hệ này tương đương với chỉ một phương trình

x - y - z - t $=$ 0.

Nếu chọn x $=$ y thì z $=$ -t. Ta muốn tìm các vécto riêng có độ dài bằng đơn vị,

tức là $x^2$ + $y^2$ + $z^2$ + $t^2 = 2x^2$ + $2z^2 =$ 1. Do đó $x^2$ + $z^2 = \frac{1}{2}$. Từ đây ta có thể chọn

hai vécto riêng độc lập tuyến tính $e_1$, $e_2$ với các toạ độ tương ứng là

$x_1 = y_1 = z_1 = \frac{1}{2}$, $t_1 = -\frac{1}{2}$,

và $x_2 = y_2 = t_2 = \frac{1}{2}$, $z_2 = -\frac{1}{2}$.

May mắn, hai vécto này trực giao với nhau. (Nếu trái lại, ta tiến hành trực giao

hoá chúng). Cuối cùng, ta tìm véctơ riêng $e_3$ ứng với $\lambda =$ 2 bằng cách đòi hỏi nó

trực giao với hai véctor $e_1$, $e_2$, tức là thoả mãn thêm hai phương trình

$ \begin{cases} x+y+z-t &= 0, \\ x+y-z+t &= 0. \end{cases} $

Ngoài ra, ta muốn $|e_3| =$ 1. Từ đó, $e_3$ có các toạ độ $x_3 = z_3 = t_3 = \frac{1}{2}$, $y_3 = -\frac{1}{2}$.

Ma trận cần tìm Q có các vécto cột chính là các vécto riêng $(e_1$, $e_2$, $e_3$, $e_4):$

$ Q = \left( \begin{array}{cccc} \frac{1}{2} & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \ \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \ \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \ -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \ \end{array} \right). $

Ta có

$ B = Q^{-1}AQ = Q^tAQ = \left( \begin{array}{cccc} 2 & 0 & 0 & 0 \ & 0 & 2 & 0 & 0 \ & 0 & 0 & 2 & 0 \ & 0 & 0 & -2 \end{array} \right). $

Vài nét về không gian Unita

$\overline{4}$

Trong tiết này ta nói vài nét về những thay đổi cần thiết khi nghiên cứu việc đo

độ dài của các vécto trong một không gian vécto phức. Trong những không gian



như thế, ta không định nghĩa được khái niệm góc giữa hai vécto bất kỳ. Tuy thế,

khái niệm trực giao thì vẫn có nghĩa.

Giả sử E là một không gian vécto phức.

### Định nghĩa 4.1 Một hàm \eta: E \times E \to \mathbb{C} được gọi là một dạng Hermit trên E

nếu nó thoả mãn hai điều kiện sau đây:

(1) $\eta$ tuyến tính đối với biến thứ nhất:

$\eta(\alpha_1$ + $\alpha_2$, $\beta) = \eta(\alpha_1$, $\beta)$ + $\eta(\alpha_2$, $\beta) \quad \forall \alpha_1$, $\alpha_2$, $\beta \in$ E,

$\eta(a\alpha,\beta) = a\eta(\alpha,\beta)$, $\qquad \forall$ a $\in \mathbf{C}$, $\alpha,\beta \in$ E.

(2) $\eta$ là một hàm liên lợp đối xúng:

$\eta(\beta,\alpha) = \overline{\eta(\alpha,\beta)}$, $\qquad \forall \alpha,\beta \in$ E,

trong đó $\eta(\alpha$, $\beta)$ là liên hợp phức của $\eta(\alpha$, $\beta)$.

Mỗi dạng Hermit đều liên hợp tuyến tính đối với biến thứ hai. Tức là

$\eta(\alpha,\beta_1+\beta_2) = \eta(\alpha,\beta_1)$ + $\eta(\alpha,\beta_2) \quad \forall \alpha,\beta_1,\beta_2 \in$ E,

$\eta(\alpha$, $b\beta) = \bar{b}\eta(\alpha$, $\beta)$, $\qquad \forall$ b $\in \mathbf{C}$, $\alpha$, $\beta \in$ E.

Thật vậy:

$\eta(\alpha,\beta_1+\beta_2) = \overline{\eta(\beta_1+\beta_2,\alpha)} = \overline{\eta(\beta_1,\alpha)+\eta(\beta_2,\alpha)}$

$= \overline{\eta(\beta_1,\alpha)}$ + $\overline{\eta(\beta_2,\alpha)} = \eta(\alpha,\beta_1)$ + $\eta(\alpha,\beta_2)$.

$\eta(\alpha$, $b\beta) = \overline{\eta(b\beta$, $\alpha)} = \overline{b\eta(\beta$, $\alpha)}$

$= \overline{b} \ \overline{\eta(\beta,\alpha)} = \overline{b} \eta(\alpha,\beta)$.

Dặc biệt, lấy $\alpha = \beta$, ta có

$\eta(\alpha,\alpha) = \eta(\alpha,\alpha)$.

Vì thế, $\eta(\alpha$, $\alpha)$ là một số thực, với mọi $\alpha \in$ E.

$\bigcap \bigcap$ C



Dinh nghĩa 4.2 Dang Hermit $\eta$ được gọi là một tích vô hướng nếu nó có tính xác

dinh duong:

$\eta(\alpha$, $\alpha) \geq$ 0, $\qquad \forall \alpha \in$ E,

$\eta(\alpha$, $\alpha) =$ 0 $\iff \alpha =$ 0.

Không gian vécto phức E cùng với một tích vô hướng đã cho trên E được gọi là

một không gian Unita.

Khi đó $\eta(\alpha$, $\beta)$ được gọi là tích vô hướng của $\alpha$ và $\beta$, và thường được ký hiệu

bởi $\langle \alpha$, $\beta \rangle$.

Nhận xét: Không thể định nghĩa tích vô hướng trên không gian vécto phức như

một dạng song tuyến tính, đối xứng và xác định dương. Lý do đơn giản là vì không

tồn tại một dạng như vậy. Thật thế, nếu $\langle \cdot$, $\cdot \rangle$ là một dạng song tuyến tính, đối

xứng và xác định dương thì

$\langle a\alpha$, $a\alpha\rangle = a^2\langle \alpha$, $\alpha\rangle$, $\forall$ a $\in \mathbf{C}$, $\alpha \in$ E.

Nếu $\langle \alpha$, $\alpha \rangle$ là một số thực dương thì $a^2 \langle \alpha$, $\alpha \rangle$ không thực, chẳng hạn với a $= \sqrt{i}$,

trong đó i là đơn vị áo.

Ví dụ: Không gian $\mathbb{C}^n$ là một không gian Unita với tích vô hướng chính tắc định

nghĩa như sau:

$\langle \alpha$, $\beta \rangle = x_1 \overline{y_1}$ + $\cdots$ + $x_n \overline{y_n}$,

trong đó $\alpha = (x_1$, ..., $x_n)^t$, $\beta = (y_1$, ..., $y_n)^t$.

Trong không gian UnitaE,số thực không âm $|\alpha|=\sqrt{\langle \alpha$, $\alpha \rangle}$ được gọi là độ dài

của véctor $\alpha$.

Bất đẳng thức Cauchy-Schwarz vẫn còn đúng trong các không gian Unita. Tuy

thế, tỷ số $\frac{\langle \alpha$, $\beta \rangle}{|\alpha||\beta|}$ nói chung là một số phức mà không là số thực, nên ta không định

nghĩa được góc giữa hai véc tơ khác 0 bất kỳ.

Mặc dầu vậy, ta vẫn nói $\alpha$ trực giao với $\beta$ và viết $\alpha \perp \beta$ nếu $\langle \alpha$, $\beta \rangle =$ 0.



Mọi không gian unita đều có cơ sở trực chuẩn. Điều này có thể được chứng

minh bằng cách trực giao hoá Shmidt một cơ sở tuỳ ý của E để xây dựng một cơ

sở trực giao, rồi chuẩn hoá để có một cơ sở trực chuẩn của E.

### Định nghĩa 4.3 Tự đồng cấuf:E\rightarrow E được gọi là một bi\acute{e}n đổi unitanếuf

bảo toàn tích vô hướng:

$\langle f(\alpha)$, $f(\beta) \rangle = \langle \alpha$, $\beta \rangle$, $\quad \forall \alpha$, $\beta \in$ E.

Một phép biến đổi tuyến tính là unita nếu và chỉ nếu nó biến mỗi cơ sở trực

chuẩn thành một cơ sở trực chuẩn.

Giả sử A $= (a_{ij})$ là một ma trận phức vuông cấp n. Ma trận phụ hợp phức

$A^* = (a_{ij}^*)$ của A được định nghĩa như sau:

$a_{ij}^* = \overline{a_{ji}}$.

### Dịnh nghĩa 4.4 A được gọi là một ma trận unita nếu AA^* = A^*A = E_n.

Ma trận chuyển giữa hai cơ sở trực chuẩn bất kỳ của E là một ma trận unita.

Một phép biến đổi tuyến tính là unita nếu và chỉ nếu ma trận của nó trong mỗi

cơ sở trực chuẩn của E là một ma trận unita.

Khác với các phép biến đổi trực giao, mọi phép biến đổi unita đều chéo hoá

được. Điều này là hệ quả của tính đóng đại số của trường số phức. Mọi giá trị

riêng của một phép biến đổi unita đều có môđun bằng 1.

### Định nghĩa 4.5 Phép biến đổi tuyến tính f: E \to E được gọi là tự liên hợp nếu

$\langle f(\alpha)$, $\beta \rangle = \langle \alpha$, $f(\beta) \rangle$, $\quad \forall \alpha$, $\beta \in$ E.

Ma trận A được gọi là tư liên hợp nếu A $= A^*$.

Một phép biến đổi tuyến tính là tự liên hợp nếu và chỉ nếu ma trận của nó

trong mỗi cơ sở trực chuẩn của E là một ma trận tự liên hợp.



Mỗi phép biến đổi tự liên hợp của E đều có một cơ sở trực chuẩn của E gồm

toàn những vécto riêng của nó. Mọi giá trị riêng của các phép biến đổi tự liên hợp

dều thực.

Hệ quả là mọi ma trận tự liên hợp A đều có một ma trận unita C sao cho

$C^*AC = C^{-1}AC$ là ma trận chéo, với các phần tử trên đường chéo đều thực.

Bài tập

1. Chứng minh rằng các véctor (1, -2, 2, -3) và (2, -3, 2, 4) trực giao với nhau.

Bổ sung hệ vécto đó để thu được một cơ sở trực giao của không gian.

2. Bổ sung hệ gồm 2 vécto $(\frac{1}{2}$, $\frac{1}{2}$, $\frac{1}{2}$, $\frac{1}{2})$ và $(\frac{1}{2}$, $\frac{1}{2}$, $-\frac{1}{2}$, $-\frac{1}{2})$ để thu được một cơ sở

trực chuẩn của không gian.

3. Dùng phép trực giao hoá để xây dựng một cơ sở trực giao của không gian

con sinh bởi các vécto sau đây:

(2, 1, 3, -1), (7, 4, 3, 3), (1, 1, -6, 0), (5, 7, 7, 8).

4. Tìm một cơ sở trực giao cho phần bù trực giao $U^{\perp}$ của không gian con U

trong $\mathbb{R}^4$ sinh bởi các véctor sau đây:

$\alpha_1 =$ (1, 0, 2, 1), $\alpha_2 =$ (2, 1, 2, 3), $\alpha_3 =$ (0, 1, -2, 1).

5. Không gian véctor con U được xác định bởi hệ phương trình

$2x_1$ + $x_2$ + $3x_3$ - $x_4 =$ 0,

$3x_1$ + $2x_2$ - $2x_4 =$ 0,

$3x_1$ + $x_2$ + $9x_3$ - $x_4 =$ 0.

Tìm hệ phương trình xác định phần bù trực giao $U^{\perp}$ của U trong $\mathbb{R}^{4}$.



6. Xác định hình chiếu trực giao của $vécto\alpha=(4,-1,-3,4)lên$ không gian con

U $\sinh b\dot{\phi}i$ các vécto

$\alpha_1 =$ (1, 1, 1, 1), $\alpha_2 =$ (1, 2, 2, -1), $\alpha_3 =$ (1, 0, 0, 3).

7. Xác định hình chiếu trực giao của $vécto\alpha=(7,-4,-1,2)lên$ không gian con

U xác định bởi hệ phương trình

$2x_1$ + $x_2$ + $x_3$ + $3x_4 =$ 0,

$3x_1$ + $2x_2$ + $2x_3$ + $x_4 =$ 0,

$x_1$ + $2x_2$ + $2x_3$ - $9x_4 =$ 0.

8. Tìm khoảng cách từ vécto $\alpha =$ (2, 4, -4, 2) tới phẳng được xác định bởi hệ

phương trình:

$x_1$ + $2x_2$ + $x_3$ - $x_4 =$ 1,

$x_1$ + $3x_2$ + $x_3$ - $3x_4 =$ 2.

9. Chứng minh rằng khoảng cách d từ vécto $\alpha$ tới phẳng $\beta$ + U, trong đó U là

không gian con có cơ sở $(\alpha_1$, ..., $\alpha_k)$, nghiệm đúng công thức

$d^2 = \frac{G(\alpha_1$, ..., $\alpha_k$, $\alpha$ - $\beta)}{G(\alpha_1$, ..., $\alpha_k)}$.

$\dot{\mathrm{O}}$ dây

$G(\alpha_1$, ..., $\alpha_k) = \det(\langle \alpha_i$, $\alpha_j \rangle)_{k \times k}$

là định thức Gram (còn gọi là định thức Gram - Shmidt) của hệ vécto

$(\alpha_1$, ..., $\alpha_k)$.

10. Tìm khoảng cách giữa hai phẳng $\alpha$ + U và $\beta$ + V, trong đó $\alpha =$ (4, 5, 3, 2)

$\beta =$ (1, -2, 1, -3), không gian con U sinh bởi các vécto

(1, 2, 2, 2) và (2, -2, 1, 2),

và không gian con V sinh bởi các vécto

(2,0,2,1) và (1,-2,0,-1).



11. Cho các vécto $\alpha$ và $\beta$ trong không gian vécto Euclid E. Chứng minh rằng:

(a) $\alpha = a\beta$ với số thực nào đó a $>$ 0 nếu và chỉ nếu góc giữa hai vécto $\alpha$

và $\beta$ bằng 0;

(b) $\alpha = a\beta$ với số thực nào đó a $<$ 0 nếu và chỉ nếu góc giữa hai vécto $\alpha$

và $\beta$ bằng $\pi$.

12. Chứng minh rằng góc giữa vécto $\alpha$ với các vécto $\beta \in$ L, trong đó L là một

không gian véctor con, đạt giá trị nhỏ nhất khi $\beta$ là hình chiếu vuông góc $\beta_0$

của $\alpha$ lên L. Đẳng thức $\cos \angle(\alpha$, $\beta) = \cos \angle(\alpha$, $\beta_0)$, trong đó $\beta \in$ L, xảy ra nếu

và chỉ nếu $\beta = a\beta_0$ với số thực nào đó a $>$ 0.

13. Ta gọi góc giữa $\alpha$ và hình chiếu vuông góc của nó lên L là góc giữa $\alpha$ và L

(xem bài tập trước). Tìm góc giữa $\alpha =$ (1, 0, 3, 0) và không gian con L sinh

bởi các vécto sau đây:

(5,3,4,-3), (1,1,4,5), (2,-1,1,2).

14. Cho một hệ vécto độc lập tuyến tính $(e_1$, ..., $e_k)$ và hai hệ vécto trực giao

$(f_1,...,f_k)và (g_1,...,g_k)sao$ cho các $véctof_svà g_sbiểu$ thị tuyến tính được

qua các vécto $e_1$, ..., $e_s$ (với s $=$ 1, 2, ..., k). Chứng minh rằng $f_s = a_s g_s$ trong

đó $a_s$ là một số thực khác không (s $=$ 1, 2, ..., k).

15. Xét tích vô hướng sau đây trong không gian $\mathbf{R}[X]_n$ các đa thức thực có bậc

không vượt quá n:

$\langle$ f, g $\rangle = \int_{-1}^{1}$ f(X)g(X) dX.

Chứng minh rằng nếu áp dụng quá trình trực giao hoá vào cơ sở (1, X, ..., Xn)

của không gian nói trên thì ta thu được hệ đa thức chỉ khác với các đa thức

Legendre sau đây các nhân tử thực khác không:

$P_0(X) =$ 1, $P_k(X) = \frac{1}{2^k k!} \frac{d^k}{dX^k} [(X^2$ - $1)^k]$,

với (k $=$ 1, 2, ..., n). Tìm các nhân tử đó.



16. Chứng minh rằng định thức Gram $G(\alpha_1$, ..., $\alpha_k) = \det(\langle \alpha_i$, $\alpha_j \rangle)_{k \times k}$ không thay

đổi sau quá trình trực giao hoá. Cụ thể, giả sử $(e_1$, ..., $e_k)$ là kết quả của quá

trình trực giao hoá áp dụng cho hệ vécto $(\alpha_1$, ..., $\alpha_k)$. Khi đó

$G(\alpha_1$, ..., $\alpha_k) = G(e_1$, ..., $e_k) = \langle e_1$, $e_1 \rangle \langle e_2$, $e_2 \rangle \cdots \langle e_k$, $e_k \rangle$.

(Trên cơ sở đó, người ta gọi $\sqrt{G(\alpha_1$, ..., $\alpha_k)}$ là thể tích k-chiều của hình hộp

với các cạnh $\alpha_1$, ..., $\alpha_k$.

17. Chứng minh rằng các vécto $\alpha_1$, ..., $\alpha_k$ độc lập tuyến tính nếu và chỉ nếu

$G(\alpha_1,...,\alpha_k) \neq$ 0.

18. Chứng minh rằng nếu $(e_1$, ..., $e_k)$ là kết quả của quá trình trực giao hoá áp

dụng cho hệ vécto $(\alpha_1$, ..., $\alpha_k)$ thì

$|e_k|^2 = \frac{G(\alpha_1$, ..., $\alpha_k)}{G(\alpha_1$, ..., $\alpha_{k-1})}$,

với k $=$ 1, 2, ..., n. (Định thức Gram của một hệ gồm không vécto được qui

ước coi là bằng 1.)

19. Chứng minh bất đẳng thức

0 $\leq G(\alpha_1$, ..., $\alpha_k) \leq |\alpha_1|^2 \cdots |\alpha_k|^2$

trong đó dấu bằng xảy ra ở bất đẳng thức thứ hai nếu và chỉ nếu các vécto

$\alpha_1$, ..., $\alpha_k$ đôi một trực giao hoặc ít nhất một trong các vécto đó bằng 0.

20. Chứng minh bất đẳng thức

$G(\alpha_1$, ..., $\alpha_k$, $\beta_1$, ..., $\beta_\ell) \le G(\alpha_1$, ..., $\alpha_k) G(\beta_1$, ..., $\beta_\ell)$,

trong đó dấu bằng xảy ra nếu và chỉ nếu

$\langle \alpha_i$, $\beta_i \rangle =$ 0 $\ \$ (i $=$ 1, ..., k; j $=$ 1, ..., $\ell)$

hoặc một trong các vécto $\alpha_1$, ..., $\alpha_k$, $\beta_1$, ..., $\beta_\ell$ bằng 0.

$\cap$



21. Các cơ sở $(e_1$, ..., $e_n)$ và $f_1$, ..., $f_n$ của một không gian vector Euclid được gọi

là nghịch đảo của nhau nếu

$ \langle e_i, f_j \rangle = \begin{cases} 1 & \text{néu } i = j, \\ 0 & \text{néu } i \neq j. \end{cases} $

Chứng minh rằng tồn tại duy nhất cơ sở nghịch đảo đối với mỗi cơ sở

$(e_1$, ..., $e_n)$.

22. Cho hai hệ $vécto(\alpha_1,...,\alpha_k)và (\beta_1,...,\beta_k)của$ một không gian vécto Euclid

Chứng minh rằng tồn tại một tự đồng cấu trực giao $\varphi$ của E sao cho

E.

$\varphi(\alpha_i) = \beta_i$ (i $=$ 1, 2, ..., k) nếu và chỉ nếu các ma trận Gram của hai hệ véctor

dó trùng nhau:

$(\langle \alpha_i$, $\alpha_j \rangle)_{k \times k} = (\langle \beta_i$, $\beta_j \rangle)_{k \times k}$.

23. Phép biến đổi trực giao $\varphi$ có ma trận là A như dưới đây trong một cơ sở trực

chuẩn nào đó. Hãy tìm một cơ sở trực chuẩn sao cho ma trận B của $\varphi$ trong

cơ sở đó có dạng chính tắc, và tìm ma trận B:

$ (a) A = \begin{pmatrix} \frac{2}{3} & \frac{2}{3} & -\frac{1}{3} \\ \frac{2}{3} & -\frac{1}{3} & \frac{2}{3} \\ -\frac{1}{3} & \frac{2}{3} & \frac{2}{3} \end{pmatrix}, (b) A = \begin{pmatrix} \frac{1}{2} & \frac{1}{2} & -\frac{1}{2}\sqrt{2} \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2}\sqrt{2} \\ \frac{1}{2}\sqrt{2} & -\frac{1}{2}\sqrt{2} & 0 \end{pmatrix}. $

24. Tìm dạng chính tắc B của ma trận trực giao A sau đây và ma trận trực giao

Q sao cho B $= Q^{-1}AQ:$

$ (a) A = \begin{pmatrix} \frac{2}{3} & -\frac{1}{3} & \frac{2}{3} \\ \frac{2}{3} & \frac{2}{3} & -\frac{1}{3} \\ -\frac{1}{3} & \frac{2}{3} & \frac{2}{3} \end{pmatrix}, \quad (b) A = \begin{pmatrix} \frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} \\ -\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\ -\frac{1}{2} & \frac{1}{2} & $

25. Chứng minh toàn bộ Mệnh đề 3.4.



26. Giả sử $(e_1$, $e_2)$ là một cơ sở trực chuẩn của mặt phẳng và tự đồng cấu $\varphi$ có

$ ma trận A = \begin{pmatrix} 1 & 2 \\ 1 & -1 \end{pmatrix} trong cơ sở gồm f_1 = e_1 và f_2 = e_1 + e_2. Tìm ma $

trận của tự đồng cấu liên hợp $\varphi^*$ trong cùng cơ sở $(f_1$, $f_2)$.

27. Phép biến đổi tuyến tính $\varphi$ của không gian vécto Euclid $\mathbf{R}_3$ có ma trận là

$ A = \left( \begin{array}{rrr} 1 & 1 & 3 \\ 0 & 5 & -1 \\ 2 & 7 & -3 \end{array} \right) $

trong cơ sở gồm các vécto $f_1 =$ (1, 2, 1), $f_2 =$ (1, 1, 2), $f_3 =$ (1, 1, 0). Tìm ma

trận của phép biến đổi liên $hợp\varphi^*$ trong cùng cơ sở đó.

28. Tìm ma trận của phép biến đổi liên hợp $\varphi^*$ trong cơ sở chính tắc của $\mathbf{R}_3$ nếu

$\varphi$ biến các véctor $\alpha_1 =$ (0,0,1), $\alpha_2 =$ (0,1,1), $\alpha_3 =$ (1,1,1) tương ứng thành

các véctor $\beta_1 =$ (1, 2, 1), $\beta_2 =$ (3, 1, 2), $\beta_3 =$ (7, -1, 4).

29. Cho một phân tích của không gian véctor Euclid E thành tổng trực tiếp của

hai không gian con: E $= U_1 \oplus U_2$. Gọi $\varphi$ là phép chiếu lên $U_1$ theo phương

$U_2$. Chứng minh rằng E $= U_1^{\perp} \oplus U_2^{\perp}$, và $\varphi^*$ là phép chiếu lên $U_2^{\perp}$ theo phương

$U_1^{\perp}$.

30. Chứng minh rằng nếu U là một không gian con ổn định đối với phép biến

đổi tuyến tính $\varphi$ thì $U^{\perp}$ là một không gian con ổn định đối với phép biến đổi

liên hợp $\varphi^*$.

31. Chứng minh rằng hai phép biến đổi tuyến tính liên hợp với nhau có cùng đa

thức đặc trưng.

32. Chứng minh rằng nếu phép biến đổi tuyến tính $\varphi$ có ma trận A trong cơ sở

$(e_1$, ..., $e_n)$ thì phép biến đổi liên hợp $\varphi^*$ có ma trận $A^t$ trong cơ sở nghịch đảo

với cơ sở nói trên.



33. Giả sử U $= (\langle \alpha_i$, $\alpha_j \rangle)_{n \times n}$ là ma trận Gram của cơ sở $(\alpha_1$, ..., $\alpha_n)$. Chứng minh

rằng ma trận A của phép biến đổi tuyến tính $\varphi$ và ma trận B của phép biến

đổi liên hợp $\varphi^*$ trong cơ sở nói trên liên hệ với nhau bởi công thức:

(a) B $= U^{-1}A^tU$ đối với không gian véctor Euclid;

(b) $\overline{B} = U^{-1} A^t$ U đối với không gian unita.

Từ đó suy ra điều kiện cần và đủ $để\varphilà$ một phép biến đổi tự liên hợp.

34. Giả sử U là ma trận Gram của một cơ sở nào đó của không gian và A là ma

trận của phép biến đổi tuyến tính $\varphi$ trong cơ sở đó. Tìm ma trận của phép

biến đổi liên hợp $\varphi^*$ trong cùng cơ sở nói trên, cho biết

$ U = \left( \begin{array}{rrr} 3 & 1 & -2 \\ 1 & 1 & -1 \\ -2 & -1 & 2 \end{array} \right), \quad A = \left( \begin{array}{rrr} 1 & 2 & 0 \\ 2 & 0 & 3 \\ 0 & 1 & 3 \end{array} \right). $

35. Gọi $\varphi$ là phép chiếu lên $U_1$ theo phương $U_2$ (hoặc phép phản xạ qua $U_1$ theo

phương $U_2)$. Chứng minh rằng $\varphi$ là đối xứng nếu và chỉ nếu các không gian

con $U_1$ và $U_2$ trưc giao.

36. Cho phép biến đổi tuyến tính $\varphi$ xác định bởi ma trận A sau đây trong một cơ

sở trực chuẩn nào đó của không gian. Tìm một cơ sở trực chuẩn gồm những

vécto riêng của $\varphi$ và ma trận của nó trong cơ sở ấy:

$ (a) A = \begin{pmatrix} 11 & 2 & -8 \\ 2 & 2 & 10 \\ -8 & 10 & 5 \end{pmatrix}, (b) A = \begin{pmatrix} 17 & -8 & 4 \\ -8 & 17 & -4 \\ 4 & -4 & 11 \end{pmatrix}. $

37. Chứng minh rằng không gian véctơ Euclid E có một cơ sở trực chuẩn gồm

các vécto đồng thời là các vécto riêng của hai phép biến đổi đối xứng $\varphi$ và

$\psi$ nếu và chỉ nếu hai phép biến đổi này giao hoán với nhau.



38. Chứng minh rằng mỗi tự đồng cấu $\varphi$ của một không gian vécto Euclid đều

có thể phân tích thành $\varphi = \psi_1 \chi_1$ và $\varphi = \chi_2 \psi_2$, trong đó $\psi_1$, $\psi_2$ là các phép

biến đổi đối xứng có mọi giá trị riêng đều dương, còn $\chi_1$, $\chi_2$ là các phép biến

đổi trực giao. Chứng minh rằng mỗi cách phân tích nói trên đều duy nhất.

39. Phân tích các ma trân sau đây theo các cách nói ở bài trước:

$ (a) A = \begin{pmatrix} 2 & -1 \\ 2 & 1 \end{pmatrix}, (b) A = \begin{pmatrix} 4 & -2 & 2 \\ 4 & 4 & -1 \\ -2 & 4 & 2 \end{pmatrix}. $

40. Chứng minh rằng phép biến đổi đối xứng $\varphi$ là xác định dương (tức là

$\langle \varphi(\alpha)$, $\alpha \rangle >$ 0 với mọi $\alpha \neq$ 0) nếu và chỉ nếu các hệ số của đa thức đặc

trưng của nó $X^n$ + $c_1 X^{n-1}$ + $\cdots$ + $c_n$ đều khác không và đan dấu; Hơn nữa,

$\varphi$ là không âm (tức $là\langle \varphi(\alpha)$, $\alpha \rangle \geq$ 0với mọi $\alpha)$ nếu và chỉ nếu có một chỉ số

k sao cho $c_0 =$ 1, $c_1$, ..., $c_k$ khác không và đan dấu, còn $c_{k+1} = \cdots = c_n =$ 0.

41. Chứng minh rằng nếu $\varphi$ và $\psi$ là các phép biến đổi đối xứng, trong đó $\varphi$ xác

định dương, thì các giá trị riêng của varphi $\ d\text{e}u$ thực.

42. Chứng minh rằng nếu $\varphi$ và $\psi$ là các phép biến đổi đối xứng với các giá trị

riêng không âm và một trong hai phép biến đổi là không suy biến thì các giá

tri riêng của varphi $\ddot{\psi}$ đều thực và không âm.

43. Chứng minh rằng mỗi phép biến đổi đối xứng không âm có hạng r đều là

tổng của r phép biến đổi đối xứng không âm có hạng 1.

44. Phép biến đổi $\varphi$ của không gian Euclid E được gọi là phản đối xứng nếu

$\varphi^* = -\varphi$. Chứng minh rằng $\varphi$ là phản đối xứng nếu và chỉ nếu ma trận của

nó trong mỗi cơ sở trực chuẩn của không gian đều là ma trận phản đối xứng.

45. Chứng minh rằng nếu không gian U ổn định đối với phép biến đổi phản đối

xứng $\varphi$ thì phần bù trực giao $U^{\perp}$ của nó cũng vậy.



# Chương VI

DANG SONG TUYẾN TÍNH

VÀ DANG TOÀN PHƯƠNG

Nội dung chính của chương này là phân loại tất cả các dạng song tuyến tính

đối xứng và các dạng toàn phương trên không gian vécto thực hữu hạn chiều.

Khái niệm dạng song tuyến tính và dạng toàn

$\mathbf$ 1

phương

Giả sử V là một không gian vécto thực.

### Định nghĩa 1.1 Ánh xạ \eta: V \times V \to \mathbf{R} được gọi là một dạng song tuyến tính trên

V nếu nó tuyến tính với mỗi biến khi cố định biến còn lại; tức là

$\eta(\alpha_1+\alpha_2,\beta) = \eta(\alpha_1,\beta)$ + $\eta(\alpha_2,\beta)$,

$\eta(a\alpha,\beta) = a\eta(\alpha,\beta)$,

$\eta(\alpha,\beta_1+\beta_2) = \eta(\alpha,\beta_1)$ + $\eta(\alpha,\beta_2)$,

$\eta(\alpha$, $a\beta) = a\eta(\alpha$, $\beta)$,

với mọi $\alpha$, $\alpha_i$, $\beta$, $\beta_i \in$ V, a $\in \mathbf{R}$.

Dạng song tuyến tính $\eta$ được gọi là đối xứng nếu

$\eta(\alpha$, $\beta) = \eta(\beta$, $\alpha)$

với mọi $\alpha$, $\beta \in$ V.

### Định nghĩa 1.2 Giả sử \eta là một dạng song tuyến tính đối xứng trên V. Khi đó

ánh xạ H: V $\to \mathbf{R}$ xác định bởi

$H(\alpha) = \eta(\alpha$, $\alpha)$

ററെ



được gọi là dang toàn phương trên V ứng với dang song tuyến tính đối xứng $\eta$.

Nhận xét: $\eta$ được hoàn toàn xác định bởi H. Thật vậy, ta có

$\eta(\alpha+\beta,\alpha+\beta) = \eta(\alpha,\alpha)$ + $\eta(\alpha,\beta)$ + $\eta(\beta,\alpha)$ + $\eta(\beta,\beta)$

$= \eta(\alpha$, $\alpha)$ + $2\eta(\alpha$, $\beta)$ + $\eta(\beta$, $\beta)$.

Từ đó, ta nhân được

$\eta(\alpha$, $\beta) = \frac{1}{2} [\eta(\alpha$ + $\beta$, $\alpha$ + $\beta)$ - $\eta(\alpha$, $\alpha)$ - $\eta(\beta$, $\beta)]= \frac{1}{2} [H(\alpha$ + $\beta)$ - $H(\alpha)$ - $H(\beta)]$.

Vì thế, $\eta$ được gọi là dạng cực của dạng toàn phương H.

Ví dụ 1.3 (a) $\eta(x$, y) $=$ xy là một dạng song tuyến tính đối xứng trên không

gian véctor V $= \mathbf{R}$. Dang toàn phương ứng với $\eta$ là

H(x) $= x^2$.

(b) Mỗi tích vô hướng trên V là một dạng song tuyến tính, đối xứng và xác định

dương. Dạng toàn phương ứng với nó chính là

$H(\alpha) = |\alpha|^2$.

Giả sử V là một không gian vécto thực hữu hạn chiều, và $(\alpha_1$, ..., $\alpha_n)$ là một co

sở của nó. Nếu $\alpha = \sum_i x_i \alpha_i$, $\beta = \sum_i y_j \alpha_j$, thì

$\eta(\alpha$, $\beta) = \eta(\sum_i x_i \alpha_i$, $\sum_j y_j \alpha_j) = \sum_{i,j=1}^n x_i y_j \eta(\alpha_i$, $\alpha_j)$.

Như vậy, $\eta$ hoàn toàn được xác định bởi bộ các giá trị $(\eta(\alpha_i$, $\alpha_j))_{i,j=1}^n$.

Ta xét ma trận A $= (a_{ij})_{i,j=1}^n = (\eta(\alpha_i$, $\alpha_j))_{i,j=1}^n$. Dạng $\eta$ là đối xứng nếu và chỉ

nếu A là một ma trận đối xứng. Thật vậy, nếu $\eta$ đối xứng thì

$a_{ij} = \eta(\alpha_i$, $\alpha_j) = \eta(\alpha_j$, $\alpha_i) = a_{ji}$,



với mọi i, j, nên A đối xứng. Ngược lại, nếu A đối xứng thì

$\eta(\alpha$, $\beta) = \sum_{i,j=1}^{n} x_i y_j \eta(\alpha_i$, $\alpha_j) = \sum_{i,j=1}^{n} a_{ij} x_i y_j$

$= \sum_{i=1}^{n} a_{ji} x_i y_j = \sum_{i=1}^{n} a_{ij} y_i x_j = \eta(\beta$, $\alpha)$,

i, j $=$ 1 i, j $=$ 1

với mọi $\alpha$, $\beta \in$ V, tức là $\eta$ đối xứng.

Dinh nghĩa 1.4 Ma trận A $= (a_{ij})_{n \times n} = (\eta(\alpha_i$, $\alpha_j))_{n \times n}$ được gọi là ma trận của

dạng song tuyến tính $\eta$ (hoặc ma trận của của dạng toàn phương H ứng với $\eta)$

trong co so $(\alpha_1$, ..., $\alpha_n)$.

Ký hiệu các vécto cột toạ độ của $\alpha$ và $\beta$ bởi

$ x = \left( \begin{array}{c} x_1 \ . \ . \ . \ . \ . \ . \ . \ . \ . \ . \ . \ . \ . \ . \ . \ . \ . \ . \ . $

Đồng nhất ma trận vuông cấp một $x^t$ A y với phần tử duy nhất $\sum_{i,j=1}^n a_{ij} x_i y_j$ của

nó, ta có

$\eta(\alpha$, $\beta) = \sum_{i,j=1}^{n} a_{ij} x_i y_j = x^t$ A y.

Ta gọi đó là biểu thức toạ độ của của dạng song tuyến tính $\eta$ trong cơ sở $(\alpha_1$, ..., $\alpha_n)$.

Cũng như vậy, biểu thức

$H(\alpha) = \sum_{i=1}^{n} a_{ij} x_i x_j = x^t$ A x

$i,j=1$

được gọi là biểu thức toạ độ của của dạng toàn phương H trong cơ sở $(\alpha_1$, ..., $\alpha_n)$.

Mệnh đề sau đây cho thấy ma trận của dạng song tuyến tính thay đổi thế nào

khi đổi cơ sở.



Mệnh đề 1.5 Giả sử A và B là ma trận của dạng song tuyến tính $\eta$ (hay cũng

vậy, của dạng toàn phương H) tương ứng trong các cơ sở $(\alpha_1$, ..., $\alpha_n)$ và $(\beta_1$, ..., $\beta_n)$.

Nếu C là ma trận chuyển từ cơ sở $(\alpha_1$, ..., $\alpha_n)$ sang cơ sở $(\beta_1$, ..., $\beta_n)$ thì ta có

B $= C^t$ A C.

Chứng minh: Ký hiệu A $= (a_{ij})_{n \times n}$, B $= (b_{ij})_{n \times n}$, C $= (c_{ij})_{n \times n}$, ta có

$b_{k\ell} = \eta(\beta_k$, $\beta_\ell) = \eta(\sum_i c_{ik}\alpha_i$, $\sum_i c_{j\ell}\alpha_j)$

$= \sum_{i,j=1}^n c_{ik} c_{j\ell} \eta(\alpha_i$, $\alpha_j) = \sum_{i,j=1}^n c_{ik} a_{ij} c_{j\ell}$,

với mọi k, $\ell$. Đó chính là phần tử nằm ở hàng k cột $\ell$ của ma trận $C^tAC$. Điều này

tương đương với

B $= C^t$ A C.

$\Box$

Dưa dạng toàn phương về dạng chính tắc

$\bf{2}$

Giả sử $\eta$ là một dạng song tuyến tính đối xứng (không nhất thiết xác định dương)

trên không gian véctor thực V và H là dạng toàn phương ứng với nó. Khái niệm

$\eta-trực$ giao sau đây là một tổng quát hoá của khái niệm trực giao đối với một tích

vô hướng trong không gian vécto Euclid.

Đối với các $vécto\alpha$, $\beta \in$ V, nếu $\eta(\alpha$, $\beta) =$ 0thì ta nói $\alpha \eta-vuông$ góc (hay $\eta-trực$

giao) với $\beta$, và ký hiệu $\alpha \perp_n \beta$.

Lưu ý rằng, vì $\eta$ không nhất thiết xác định dương, nên rất có thể $\alpha \perp_n \alpha$ với

một số vécto $\alpha \neq$ 0 nào đó.

### Định nghĩa 2.1 Cơ sở (\alpha_1, ..., \alpha_n) của V được gọi là một cơ sở \eta-trực giao (hay

H-trực giao, hay đơn giản, trực giao, khi $\eta$ và H đã rõ) nếu

$\eta(\alpha_i$, $\alpha_j) =$ 0, $\qquad \forall$ i $\neq$ j.



Điều này tương đương với sự kiện ma trậnAcủa $\eta$ trong cơ sở $(\alpha_1,...,\alpha_n)là$

một ma trận chéo, hay cũng vậy, biểu thức toạ độ của dạng toàn phương H ứng

với $\eta$ trong cơ sở đó có dạng

$H(\alpha) = \sum_{i=1}^{n} a_i x_i^2$,

$\dot{\sigma}$ đây $a_i = a_{ii}$.

Giả sử $(\alpha_1$, ..., $\alpha_n)$ là một cơ sở $\eta-trực$ giao. Khi đó, sau một phép hoán vị các

phần tử trong cơ sở đó (nếu cần), biểu thức tọa độ của dạng toàn phương H tương

ứng với $\eta$ trong cơ sở này có dạng

$H(\alpha) = a_1 x_1^2$ + $\dots$ + $a_p x_p^2$ - $a_{p+1} x_{p+1}^2$ - $\dots$ - $a_{p+q} x_{p+q}^2$,

trong đó $a_i >$ 0 (0 $<$ i $\leq$ p+q, 0 $\leq$ p+q $\leq$ n). Biểu thức này được gọi là dạng

chính tắc của dạng toàn phương H $= H_n$.

Ta "chuẩn hoá" cơ sở $(\alpha_1$, ..., $\alpha_n)$ bằng cách đặt

$\beta_i = \frac{1}{\sqrt{a_i}} \alpha_i$ (i $=$ 1, ..., p + q), $\beta_i = \alpha_i$ (i $>$ p + q).

Khi đó $\alpha = \sum_i x_i \alpha_i = \sum_i y_i \beta_i$, trong đó

$y_i = \sqrt{a_i} x_i$ (i $=$ 1, ..., p + q), $y_i = x_i$ (i $>$ p + q).

Biểu thức toạ độ của H trong cơ sở mới $(\beta_1$, ..., $\beta_n)$ là

$H(\alpha) = y_1^2$ + $\cdots$ + $y_n^2$ - $y_{n+1}^2$ - $\cdots$ - $y_{n+a}^2$

Biểu thức này được gọi là dạng chuẩn tắc của dạng toàn phương H $= H_n$.

### Dịnh lý 2.2 Tồn tại một cơ sở \eta-trực giao cho mỗi dạng song tuyến tính đối xứng

$\eta$ trên không gian vécto thực hữu hạn chiều V.

Chứng minh: Gọi A là ma trận của $\eta$ trong một cơ sở nào đó $(\alpha_1$, ..., $\alpha_n)$. Vì

A là một ma trận đối xứng thực, nên tồn tại ma trận trực giao Q sao cho B $=$



$Q^{-1}AQ=Q^tAQlà$ một ma trận chéo. Gọi $(\beta_1,...,\beta_n)là$ cơ sở mà ma trận chuyển

từ $(\alpha_1$, ..., $\alpha_n)$ sang nó là Q. Khi đó, theo Mệnh đề 1.5, B là ma trận của $\eta$ trong

cơ sở $(\beta_1,...,\beta_n).Vì$ B là một ma trận chéo, nên $(\beta_1,...,\beta_n)$ là một cơ sở $\eta\text{-true}$

$\Box$

giao.

Hệ quả 2.3 Giả sử $\eta$ là một dạng song tuyến tính đối xứng trên một không gian

vécto Euclid E. Khi đó, tồn tại một cơ sở trực chuẩn của E đồng thời là một cơ

$s\dot{\sigma} \eta-truc$ giao.

Chứng minh: Ta lặp lại chứng minh của định lý trước, nhưng xuất phát từ một

cơ sở trực chuẩn nào đó $(\alpha_1$, ..., $\alpha_n)$ của E. Tồn tại ma trận trực giao Q sao cho

B $= Q^{-1}AQ = Q^tAQ$ là một ma trận chéo. Đó chính là ma trận của $\eta$ trong cơ sở

$(\beta_1$, ..., $\beta_n)$ xác định bởi điều kiện ma trận chuyển từ $(\alpha_1$, ..., $\alpha_n)$ sang cơ sở đó là

Q. Vì B là một ma trận chéo, nên $(\beta_1$, ..., $\beta_n)$ là một cơ sở $\eta-trực$ giao. Vì Q trực

giao, cho nên $(\beta_1$, ..., $\beta_n)$ cũng là một cơ sở trực chuẩn của E.

$\Box$

Có thể nhìn hệ quả nói trên từ một khía cạnh khác. Theo cách nhìn này hệ quả

khẳng định có thể đưa đồng thời hai dạng toàn phương, trong đó có một dạng xác

định dương, về dạng chéo trong cùng một cơ sở.

Bây giờ ta trình bày Phương pháp Lagrange đưa dạng toàn phương về dạng

chính tắc. Phương pháp này tiện lợi hơn trong thực hành so với phương pháp

được trình bày trong chứng minh Định lý 2.2.

Giả sử dạng toàn phương H được cho trong một cơ sở nào đó $(\alpha_1$, ..., $\alpha_n)$ bởi

biểu thức

$H(\alpha) = \sum_{ij} a_{ij} x_i x_j$, $(a_{ij} = a_{ji})$.

Ta xét 3 trường hợp sau đây.

Trường hợp 1: Giả sử $a_{ii} \neq$ 0 với i nào đó. Sau một phép đánh số lại các phần

tử của cơ sở $(\alpha_1$, ..., $\alpha_n)$ nếu cần, ta có thể giả sử $a_{11} \neq$ 0. Khi đó

H $= a_{11}(x_1^2$ + $2x_1 \sum_{i=2}^{n} \frac{a_{1i}}{a_{11}}x_i)$ + $(\text{những$ số hang không chứa $} x_1)$



$= a_{11}(x_1$ + $\sum_{i=2}^n \frac{a_{1i}}{a_{11}}x_i)^2$ + $(\text{một$ dạng toàn phương của $} x_2$, ..., $x_n) = a_{11}y_1^2$ + $\sum_{k,\ell=2}^n b_{k,\ell}y_ky_\ell (b_{k\ell} = b_{\ell k})$,

trong đó

$ \begin{cases} y_1 = x_1 + \sum_{i=2}^n \frac{a_{1i}}{a_{11}} x_i, \\ y_k = x_k \end{cases} (k = 2, 3, ..., n) $

là một phép biến đổi toạ độ không suy biến.

Việc đưa H về dạng chính tắc được quy về việc đưa dạng toàn phương H' $=$

$\sum_{k,\ell=2}^n b_{k,\ell} y_k y_{\ell}$ của (n-1) biến về dạng chính tắc. Điều này có thể thực hiện bằng

quy nap.

Trường hợp 2: Mọi $a_{ii} =$ 0 (i $=$ 1, ..., n) nhưng có $a_{ij} \neq$ 0(i $\neq$ j). không giảm

tổng quát ta giả sử $a_{12} \neq$ 0. Thực hiện phép biến đổi toạ độ không suy biến

$ \begin{cases}\nx_1 = y_1 + y_2, \\
x_2 = y_1 - y_2, \\
x_k = y_k \n\end{cases}
(k = 3, ..., n), $

ta có

$2a_{12}x_1x_2 = 2a_{12}(y_1^2$ - $y_2^2)$.

Từ đó

H $= \sum_{ij} a_{ij} x_i x_j = \sum_{ij} b_{ij} y_i y_j$

có hệ số của $y_1^2$ là $2a_{12} \neq$ 0. Ta trở về trường hợp 1 đã xét.

Trường hợp 3: Mọi $a_{ij} =$ 0 (i, j $=$ 1, ..., n).

Khi đó H có dạng chính tắc trong bất kỳ cơ sở nào của không gian V.

Ví dụ: Chứng minh rằng một trong hai dạng toàn phương sau đây

H $= 8x_1^2$ - $28x_2^2$ + $14x_3^2$ + $16x_1x_2$ + $14x_1x_3$ + $32x_2x_3$,

K $= x_1^2$ + $4x_2^2$ + $2x_3^2$ + $2x_1x_3$



là xác đinh dương. Tìm một phép biến đối tuyến tính không suy biến đưa dang

đó về dạng chuẩn tắc, đồng thời đưa dạng còn lại về dạng chính tắc.

Lời giải: Ta sẽ theo sát các bước của chứng minh Hệ quả 2.3.

Dùng phương pháp Lagrange đưa K về dạng chính tắc, ta nhận thấy K xác

dinh dương, bởi vì

K $= x_1^2$ + $4x_2^2$ + $2x_3^2$ + $2x_1x_3 = (x_1$ + $x_3)^2$ + $4x_2^2$ + $x_3^2$.

Trước hết ta đưaKvề dạng chuẩn tắc bằng phép đổi biến $y_1 = x_1$ + $x_3$, $y_2 =$

$2x_2$, $y_3 = x_3$. Khi đó

H $= 8y_1^2$ - $7y_2^2$ + $8y_3^2$ + $8y_1y_2$ - $2y_1y_3$ + $8y_2y_3$,

K $= y_1^2$ + $y_2^2$ + $y_3^2$.

Ma trận của H trong cơ sở mới ứng với các biến $y_1$, $y_2$, $y_3$ là

$ A = \left( \begin{array}{rrr} 8 & 4 & -1 \\ 4 & -7 & 4 \\ -1 & 4 & 8 \end{array} \right). $

Cái khó của bước tiếp theo là phải tìm một phép biến đổi tuyến tính đưa H về

dạng chính tắc nhưng không làm thay đổi dạng chuẩn tắc của K. Ta sẽ tìm một

biến đổi như thế trong lớp các biến đổi trực giao.

Để làm điều đó, trước hết ta tính đa thức đặc trưng của ma trận A của dạng

toàn phương H:

$ det(A - XE<sub>3</sub>) = det \begin{pmatrix} 8 - X & 4 & -1 \\ 4 & -7 - X & 4 \\ -1 & 4 & 8 - X \end{pmatrix} = -(X - 9)<sup>2</sup>(X + 9). $

Da thức này có 3 nghiệm thực kể cả bội $X_1 = X_2 =$ 9, $X_3 =$ -9.

Ta tìm các vécto riêng ứng với các giá trị riêng $X_1 = X_2 =$ 9 (của tự đồng cấu

của $\mathbb{R}^3$ có ma trận A trong cơ sở chính tắc) bằng cách giải hệ phương trình tuyến



tính

$ \begin{cases}\n-x+4y-z &= 0 \\
4x-16y+4z &= 0 \\
-x+4y-z &= 0.\n\end{cases} $

Hệ này tương đương với phương trình đầu tiên của hệ. Ta chọn 2 nghiệm độc lập

tuyến tính của nó:

$\alpha_1 =$ (1, 0, $-1)^t$, $\quad \alpha_2 =$ (0, 1, $4)^t$.

Trực giao hoá hệ gồm hai vécto nói trên:

$e'_1 = \alpha_1$, $e'_2 = \alpha_2$ + $\lambda e'_1$,

trong đó $\lambda$ được xác định duy nhất bởi điều kiện $e'_1 \perp e'_2:$

$\lambda = -\frac{\langle \alpha_2$, $e'_1 \rangle}{\langle e'_1$, $e'_2 \rangle} = -\frac{-4}{2} =$ 2.

Kết quả là $e'_2 = \alpha_2$ + $2e'_1 =$ (2, 1, $2)^t$. Ta chuẩn hoá hai vécto $e'_1$, $e'_2$, tức là chia mỗi

vécto cho độ dài của nó, để thu được:

$e_1 = (\frac{1}{\sqrt{2}}$, 0, $-\frac{1}{\sqrt{2}})^t$,

$e_2 = (\frac{2}{3}$, $\frac{1}{3}$, $\frac{2}{3})^t$.

Tiếp theo, ta tìm vécto riêng ứng với giá trị riêng $X_3 =$ -9 bằng cách giải hệ

phương trình tuyến tính

$ \begin{cases}\n17x + 4y - z &= 0 \\
4x + 2y + 4z &= 0\n\end{cases} $

$ \begin{vmatrix} -x + 4y + 17z = 0. \end{vmatrix} $

Hệ này có hạng bằng 2, nên không gian nghiệm của nó có số chiều bằng 1, và được

sinh bởi vécto sau đây:

$e'_3=(1,-4,1)^t$.



Chuẩn hoá vécto này, ta thu được

$e_3 = (\frac{1}{3\sqrt{2}}$, $-\frac{2\sqrt{2}}{3}$, $\frac{1}{3\sqrt{2}})^t$.

Vì A là một ma trận đối xứng, nên hệ $(e_1$, $e_2$, $e_3)$ là một cơ sở trực chuẩn của

$\mathbb{R}^3$. Xét ma trận trực giao với các cột (theo thứ tự) là $e_1$, $e_2$, $e_3:$

$ Q = \left(\begin{array}{ccc} \frac{1}{\sqrt{2}} & \frac{2}{3} & \frac{1}{3\sqrt{2}} \\ 0 & \frac{1}{3} & -\frac{2\sqrt{2}}{3} \\ -\frac{1}{\sqrt{2}} & \frac{2}{3} & \frac{1}{3\sqrt{2}} \end{array}\right). $

Đó chính là ma trận của phép biến đổi trực giao của $\mathbb{R}^3$ biến cơ sở chính tắc thành

$\cos \dot{\sigma} (e_1$, $e_2$, $e_3)$.

Trong cơ sở mới $(e_1$, $e_2$, $e_3)$, dạng K vẫn có ma trận đơn vị, bởi vì $Q^t E_3$ Q $=$

$Q^{-1}Q = E_3;$ còn H có ma trận chéo, với các phần tử trên đường chéo chính là các

giá trị riêng của A:

$ Q^tAQ = \left(\begin{array}{ccc} 9 & 0 & 0 \\ 0 & 9 & 0 \\ 0 & 0 & -9 \end{array}\right). $

Nói cách khác, sau phép đổi biến thực hiện bởi ma trận Q:

$ \begin{cases}\nz_1 = \frac{1}{\sqrt{2}}y_1 + \frac{2}{3}y_2 + \frac{1}{3\sqrt{2}}y_3 \\
z_2 = \frac{1}{3}y_2 - \frac{2\sqrt{2}}{3}y_3 \\
z_3 = -\frac{1}{\sqrt{2}}y_1 + \frac{2}{3}y_2 + \frac{1}{3\sqrt{2}}y_3\n\end{cases} $

biểu thức của các dạng toàn phương H và K như sau:

H $= 9z_1^2$ + $9z_2^2$ - $9z_3^2$, K $= z_1^2$ + $z_2^2$ + $z_3^2$.

Thế các biểu thức của $y_i$ theo $x_i$ vào $z_i$, ta thu được sự phụ thuộc tường minh của

các biến mới vào các biến ban đầu:

$ \begin{cases}\nz_1 = \frac{1}{\sqrt{2}}x_1 + \frac{4}{3}x_2 + \frac{2\sqrt{2}}{3}x_3 \\
z_2 = \frac{2}{3}x_2 - \frac{2\sqrt{2}}{3}x_3 \\
z_3 = -\frac{1}{\sqrt{2}}x_1 + \frac{4}{3}x_2 - \frac{\sqrt{2}}{3}x_3.\n\end{cases} $



Đó chính là phép biến đổi tuyến tính không suy biến phải tìm.

Nhận xét rằng nghiệm của bài toán trên không duy nhất. Thật vậy, có nhiều

phép biến đổi khác nhau đưa K về dạng chuẩn tắc; cũng có nhiều cách khác nhau

để chọn cơ sở trực chuẩn của $\mathbb{R}^3$ gồm toàn những vécto riêng của ma trận A.

Hang và hạch của dạng toàn phương

$3\phantom{.}$

Giả sử $\eta$ là một dạng song tuyến tính đối xứng trên không gian vécto thực V. Để

có cơ sở sâu sắc cho việc định nghĩa hạng và hạch của $\eta$, ta xây dựng ánh xạ tuyến

tính liên kết f $= f_n$ : V $\to V^*$ bằng điều kiện sau:

$f(\beta)(\alpha) = \langle \alpha$, $f(\beta) \rangle := \eta(\alpha$, $\beta)$, $\quad \forall \alpha$, $\beta \in$ V,

ở đây $\langle \cdot$, $\cdot \rangle$ chỉ phép ghép cặp đối nhẫu giữa V và $V<sup>*</sup>$. Do $\eta$ tuyến tính đối với

biến thứ nhất, nên theo Bổ đề V.3.1, $f(\beta)$ hoàn toàn xác định với mọi $\beta \in$ E. Vì

$\eta$ tuyến tính đối với biến thứ hai, nên f là một ánh xạ tuyến tính.

Mệnh đề 3.1 Ma trận của $\eta$ trong một cơ sở $(\alpha_1$, ..., $\alpha_n)$ trùng với ma trận của

f $= f_n$ trong cặp cơ sở đối ngẫu $(\alpha_1$, ..., $\alpha_n)$ và $(\alpha_1^*$, ..., $\alpha_n^*)$.

Chứng minh: Giả sử vécto $\alpha^* \in$ V có phân tích qua cơ sở $(\alpha_1^*$, ..., $\alpha_n^*)$ như sau

$\alpha^* = x_1 \alpha_1^*$ + $\cdots$ + $x_n \alpha_n^*$.

Tác động cả hai vế lên $\alpha_i$ ta có $x_i = \langle \alpha_i$, $\alpha^* \rangle$. Kết quả là

$\alpha^* = \langle \alpha_1$, $\alpha^* \rangle \alpha_1^*$ + $\cdots$ + $\langle \alpha_n$, $\alpha^* \rangle \alpha_n^*$.

Gọi A $= (a_{ij})$ là ma trận của $\eta$ trong cơ sở $(\alpha_1$, ..., $\alpha_n)$ và A' $= (b_{ij})$ là ma trận của

ftrong cặp cơ sở $(\alpha_1$, ..., $\alpha_n)$ và $(\alpha_1^*$, ..., $\alpha_n^*)$. Theo định nghĩa ma trận của một ánh

xa tuyến tính

$f(\alpha_j) = \sum_i b_{ij} \alpha_i^*$.



Ta có

$b_{ij} = \langle \alpha_i$, $f(\alpha_j) \rangle = \eta(\alpha_i$, $\alpha_j) = a_{ij}$,

với moi i, j. Do đó A $=$ A'.

$\Box$

### Định nghĩa 3.2 (i) Hạng của dạng song tuyến tính đối xứng \eta (hay hang của

dạng toàn phương H tương ứng) là hạng của ánh xạ tuyến tính liên kết với

nó $f_n$.

(ii) Nếu rankH $= \dim$ V, thì dạng toàn phương H và dạng cực $\eta$ của nó được gọi

là không suy biến. Trái lại, nếu rankH $< \dim$ V, thì H và $\eta$ được gọi là suy

$bi\widetilde{\epsilon}n$.

Theo mệnh đề trên, hạng của $\eta$ hay của H bằng hạng của ma trận của chúng

trong cơ sở bất kỳ của V.

Nếu W là một không gian véctor con của V thì $H|_W$ cũng là một dạng toàn

phương trên W.

Lưu ý rằng H (hoặc $\eta)$ có thể không suy biến trên V nhưng lại suy biến trên

một không gian con nào đó của V. Đấy là điểm khác nhau căn bản giữa các dạng

song tuyến tính và các dạng tuyến tính.

Ví dụ: Dạng toàn phương có biểu thức toạ độ trong một cơ sở nào đó H $= x^2$ - $y^2$

không suy biến trên không gian 2 chiều, vì ma trận của nó trong cơ sở đó là

$ \left(\begin{array}{cc} 1 & 0 \\ 0 & -1 \end{array}\right). $

Nhưng H $=$ (x - y)(x + y) suy biến trên các không gian con một chiều xác định

tương ứng bởi các phương trình x $=$ y và x $=$ -y.

### Dịnh nghĩa 3.3 Không gian vécto sau đây được gọi là hạch hay hạt nhân của

dạng song tuyến tính đối xứng $\eta$ (hoặc hạch của dạng toàn phương H tương ứng):

$V^0 =$ Ker $f_n = \{ \alpha \in$ V $\mid \ \eta(\alpha$, $\beta) =$ 0, $\forall \beta \in$ V $\}$.



Vì $f_n$ là một ánh xạ tuyến tính, nên $V^0$ là một không gian véctor con của V.

Giả sử T và U là các không gian véctor con của V. Ta nói T vuông góc (hay

trực giao) với U theo nghĩa $\eta$, và viết T $\perp_{\eta}$ U nếu t $\perp_{\eta}$ u, với mọi t $\in$ T, u $\in$ U.

Nếu T $\cap$ U $= \{0\}$ và T $\perp_{\eta}$ U, thì tổng trực tiếp T $\oplus$ U được gọi là một tổng

$\eta-trực$ giao (hoặc H-trực giao), và được ký hiệu là T $\oplus^{\perp}$ U. (Lưu ý rằng nếu $\eta$ suy

biến thì điều kiện T $\perp_{\eta}$ U không kéo theo T $\cap$ U $= \{0\}.)$

Theo định nghĩa, ta có $V^0 \perp_n$ V.

Mênh đề 3.4 Gọi $V<sup>0</sup>$ là hạch của dạng song tuyến tính đối xứng $\eta$ trên không gian

vécto V. Khi đó

$rank\eta = \dim$ V - $\dim V^0$.

Hơn nữa, nếu W là một phần bù tuyến tính của $V^0$ trong V, thì $\eta|_W$ không suy

biến và V là tổng $\eta-trực$ giao của $V<sup>0</sup>$ và W.

Chứng minh: Ta xét ánh xạ tuyến tính $f_{\eta}:$ V $\to V^*$ liên kết với $\eta$. Theo định lý

về mối liên hệ giữa hạng và số chiều của hạt nhân của một ánh xạ tuyến tính, ta

$\overline{c}$

$rankf_n = \dim$ V - $\dim$ Ker $f_n$.

Theo định nghĩa $rank\eta = \text{rank} f_{\eta}$ và $V^0 =$ Ker $f_{\eta}$, cho nên

$rank\eta = \dim$ V - $\dim V^0$.

Bây giờ giả sử W là một phần bù tuyến tính của $V^0$ trong V, tức là V $= V^0 \oplus$ W.

Hiển nhiên $V^0 \perp_{\eta}$ W, bởi vì $V^0 \perp_{\eta}$ V. Ta chỉ còn phải chứng minh $\eta|_W$ là không

suy biến.

Giả sử phản chứng $\eta|_W$ suy biến. Theo phần trên của mệnh đề, hạch $W^0$ của

$\eta|_W$ có số chiều bằng

$\dim W^0 = \dim$ W - $\text{rank} \eta|_W >$ 0.



Lấy một vécto bất kỳ $\alpha \in W^0 \setminus \{0\}$, ta có $\eta(\alpha$, $\beta) =$ 0, $\forall \beta \in$ W. Mặt khác, theo

định nghĩa $V^0$, ta có $\eta(\alpha$, $\beta) =$ 0, $\forall \beta \in V^0$. Vì V $= V^0 \oplus$ W, nên

$\eta(\alpha$, $\beta) =$ 0, $\quad \forall \beta \in$ V.

Nghĩa là $\alpha \in V^0$. Từ đó $\alpha \in V^0 \cap$ W $= \{0\}$, vậy $\alpha =$ 0. Điều vô lý này bác bỏ giả

thiết phản chứng.

$\Box$

Hệ quả 3.5 Dang song tuyến tính $\eta$ không suy biến khi và chỉ khi hạch của nó

$b\overset{\simeq}{a}ng$ 0.

Chứng minh: Hạch $V^0$ của $\eta$ có số chiều bằng

$\dim V^0 = \dim$ V - $\text{rank} \eta$.

$\eta$ không suy biến nghĩa là $rank\eta = \dim$ V. Điều này xảy ra nếu và chỉ nếu dim $V^0 =$

0, tức là tương đương với $V^0 = \{0\}$.

$\Box$

Chỉ số quán tính

$\overline{4}$

Khái niệm dạng toàn phương xác định dương thật ra đã được định nghĩa ở chương

không gian vécto Euclid. Sau đây ta đặt định nghĩa đó trong mối liên hệ với một

số khái niệm liên quan.

Trong tiết này chúng ta sẽ chứng minh tính duy nhất của dạng chuẩn tắc của

một dạng toàn phương. Nói cách khác, mỗi dạng toàn phương được đưa về cùng

một dạng chuẩn tắc trong những cơ sở khác nhau của không gian.

Giả sử H là một dạng toàn phương trên không gian vécto thực V.

### Dịnh nghĩa 4.1 (i) H được gọi là dương nếu H(\alpha) \geq 0 với mọi \alpha \in V.

(ii) H được gọi là xác định dương nếu nó không âm và

$H(\alpha) =$ 0 $\Longleftrightarrow \alpha =$ 0.



(iii) H được gọi là âm (tương ứng: xác định âm) nếu -H là dương (tương ứng:

xác định dương).

Ta cũng nói dạng cực $\eta$ của H là không âm, không dương, xác định dương, xác

$\dimh$ âm nếu H là như thế.

Dinh lý 4.2 (Dinh lý Sylvester về chỉ số quán tính). Giả sử H là một dạng toàn

phương trên V. Khi đó V thừa nhận một phân tích H-trực giao

V $= V_+ \oplus^{\perp} V_- \oplus^{\perp} V_0$,

trong đó $H|_{V_+}$ xác định dương, $H|_{V_-}$ xác định âm, $H|_{V_0} =$ 0. Trong bất kỳ phân

tích nào như vậy thì $V_0$ là hạch của H, dim $V_+ =$ p, dim $V_- =$ q là những hằng số.

### Định nghĩa 4.3 Ta gọi p là chỉ số quán tính dương, q là chỉ số quán tính âm và

cặp số (p, q) là chỉ số quán tính của dạng toàn phương H (hay của dạng cực $\eta)$

tương ứng với H). Hiệu số p - q được gọi là kí số của H (hay của $\eta)$.

Chứng minh Định lý 4.2:

Giả sử trong cơ sở $(e_1$, ..., $e_n)$ của V dạng toàn phương H có dạng chuẩn tắc

$H(\alpha) = x_1^2$ + $\cdots$ + $x_n^2$ - $x_{n+1}^2$ - $\cdots$ - $x_{n+a}^2$

với $\alpha = x_1 e_1$ + $\cdots$ + $x_n e_n$. Ta đặt

$V_+ = \mathcal{L}(e_1$, ..., $e_p)$,

$V_- = \mathcal{L}(e_{p+1},...,e_{p+q})$,

$V_0 = \mathcal{L}(e_{p+q+1},...,e_n)$.

Khi đó, rõ ràng $H|_{V_+}$ xác định dương, $H|_{V_-}$ xác định âm, $H|_{V_0} =$ 0. Hơn nữa, V

thừa nhận phân tích H-trực giao:

V $= V_+ \oplus^{\perp} V_- \oplus^{\perp} V_0$,



điều này được suy ra từ chỗ dạng cực $\eta$ của H được xác định bởi công thức

$\eta(\alpha$, $\beta) = x_1y_1$ + $\cdots$ + $x_py_p$ - $x_{p+1}y_{p+1}$ - $\cdots$ - $x_{p+q}y_{p+q}$,

với $\alpha = x_1 e_1$ + $\cdots$ + $x_n e_n$, $\beta = y_1 e_1$ + $\cdots$ + $y_n e_n$.

Bây giờ ta hãy xét một phân tích H-trực giao (tức là $\eta-trực$ giao) bất kỳ nào

đó V $= V_+ \oplus^{\perp} V_- \oplus^{\perp} V_0$, trong đó $H|_{V_+}$ xác định dương, $H|_{V_-}$ xác định âm, và

$H|_{V_0} =$ 0. Trước hết ta chứng minh rằng $V_0 = V^0$ là hạch của $\eta$. Giả sử $\alpha \in V_0$, vì

$V_+ \perp_n V_0$, $V_- \perp_n V_0$, cho nên

$\eta(\alpha$, $\beta) =$ 0, $\quad \forall \beta \in V_+ \oplus^{\perp} V_-$.

Hơn nữa, vì $H|_{V_0} =$ 0, nên $\eta|_{V_0} =$ 0, tức là

$\eta(\alpha$, $\beta) =$ 0, $\quad \forall \beta \in V_0$.

Gộp cả hai kết luận trên lại, ta có

$\eta(\alpha$, $\beta) =$ 0, $\quad \forall \beta \in$ V $= V_+ \oplus^{\perp} V_- \oplus^{\perp} V_0$.

Theo định nghĩa của hạch của dạng song tuyến tính, ta thu được $\alpha \in V^0$, tức là

$V_0 \subset V^0$.

Mặt khác, giả sử $\alpha = \alpha_+$ + $\alpha_-$ + $\alpha_0 \in V^0$, trong đó $\alpha_+ \in V_+$, $\alpha_- \in V_-$, $\alpha_0 \in V_0$.

Vì $\alpha \in V^0$, nên ta có

0 $= \eta(\alpha$, $\alpha_+) = \eta(\alpha_+$ + $\alpha_-$ + $\alpha_0$, $\alpha_+) = \eta(\alpha_+$, $\alpha_+)$.

Đẳng thức này cùng với giả thiết $H|_{V_+}$ xác định dương dẫn tới $\alpha_+ =$ 0. Tương tự,

$\alpha_-=0$. Do đó, $\alpha=\alpha_0\in V_0$. Vì điều đó đúng với moi $\alpha\in V^0$, cho nên $V^0\subset V_0$.

Hai bao hàm thức ngược nhau $V_0 \subset V^0$ và $V^0 \subset V_0$ chứng tỏ $V_0 = V^0$.

Bây giờ giả sử V có hai phân tích H-trưc giao như trên

V $= V_+ \oplus^{\perp} V_- \oplus^{\perp} V^0 = V'_+ \oplus^{\perp} V'_- \oplus^{\perp} V^0$.



Ta sẽ chứng minh

p $= \dim V_+ = \dim V'_+ =$ p'

q $= \dim V_{-} = \dim$ V' $=$ q'.

Giả sử phản chứng p $>$ p'. Vì p + q $=$ p' + q' $= \dim$ V - $\dim V^0$, nên q $<$ q'. Do đó

$\dim(V_{+} \oplus^{\perp} V^{0})$ + $\dim V'_{-} =$ p + q' + $\dim V^{0} > \dim$ V. Bởi vậy, có véctơ khác không

$\alpha \in (V_+ \oplus^{\perp} V^0) \cap V'_-$. Khi $đóH(\alpha) \geq$ 0vì $\alpha \in (V_+ \oplus^{\perp} V^0)$ (ta nhấn mạnh điều

kiện $V_+ \perp_n V^0$. Mặt khác, $H(\alpha) <$ 0 vì $\alpha \in V'_-$. Đó là một mâu thuẫn.

Do vai trò đối xứng của hai phân tích của không gian V, giả thiết p $<$ p' cũng

dẫn tới mâu thuẫn. Vậy p $=$ p', do đó q $=$ q'.

$\Box$

Hệ quả 4.4 (Dạng toạ độ của định lý Sylvester) Giả sử dạng toàn phương H

được đưa về dạng chuẩn tắc trong hai cơ sở khác nhau, như sau

$H(\alpha) = x_1^2$ + $\cdots$ + $x_p^2$ - $x_{p+1}^2$ - $\cdots$ - $x_{p+q}^2$

$y_1^2$ + $\cdots$ + $y_{n'}^2$ - $y_{n'+1}^2$ - $\cdots$ - $y_{n'+n'}^2$

Khi đó p $=$ p', q $=$ q' là các chỉ số quán tính dương và âm của H, còn dim V - (p+q)

là số chiều của hạch của H.

$\Box$

### Dịnh nghĩa 4.5 Hai dạng toàn phương H và K trên không gian vécto thực V

được gọi là tuong đương nếu có một tự đẳng cấu tuyến tính $\varphi:$ V $\to$ V sao cho

$H(\alpha) = K(\varphi(\alpha))$.

Dó thực sự là một quan hệ tương đương.

Hệ quả 4.6 Hai dạng toàn phương trên không gian vécto thực V tương đương

với nhau nếu và chỉ nếu chúng có cùng chỉ số quán tính.

Chứng minh: Giả sử hai dạng toàn phương H và K tương đương, tức là có một

tự đẳng cấu tuyến tính $\varphi:$ V $\to$ V sao cho $H(\alpha) = K(\varphi(\alpha))$. Giả sử H có dạng

chuẩn tắc trong cơ sở $(e_1$, ..., $e_n)$, nói rõ hơn

$H(\alpha) = x_1^2$ + $\cdots$ + $x_p^2$ - $x_{p+1}^2$ - $\cdots$ - $x_{p+q}^2$,



với $\alpha = x_1 e_1$ + $\cdots$ + $x_n e_n$. Vì $\varphi$ là một đẳng cấu tuyến tính, nên hệ vécto $\varepsilon_1 =$

$\varphi(e_1)$, ..., $\varepsilon_n = \varphi(e_n)$ cũng lập nên một cơ sở của V. Đặt

$\beta = \varphi(\alpha) = x_1 \varphi(e_1)$ + $\cdots$ + $x_n \varphi(e_n)$

$= x_1 \varepsilon_1$ + $\cdots$ + $x_n \varepsilon_n$

Ta có

$K(\beta) = K(\varphi(\alpha)) = x_1^2$ + $\cdots$ + $x_n^2$ - $x_{n+1}^2$ - $\cdots$ - $x_{n+a}^2$

Vậy H và K có cùng chỉ số quán tính.

Ngược lại, giả sử H và K có cùng chỉ số quán tính (p, q). Gọi $(e_1$, ..., $e_n)$ là một

cơ sở trong đó H nhận dạng chuẩn tắc

$H(\alpha) = x_1^2$ + $\cdots$ + $x_n^2$ - $x_{p+1}^2$ - $\cdots$ - $x_{p+q}^2$

với $\alpha = x_1 e_1$ + $\cdots$ + $x_n e_n$. Giả sử $(\varepsilon_1$, ..., $\varepsilon_n)$ là một cơ sở trong đó K nhận dạng

chuẩn tắc

$K(\beta) = y_1^2$ + $\cdots$ + $y_n^2$ - $y_{n+1}^2$ - $\cdots$ - $y_{n+a}^2$,

với $\beta = y_1 \varepsilon_1$ + $\cdots$ + $y_n \varepsilon_n$. Gọi $\varphi$ là tự đẳng cấu của V chuyển cơ sở $(e_1$, ..., $e_n)$ thành

cơ sở $(\varepsilon_1$, ..., $\varepsilon_n)$. Khi đó, nếu $\alpha = x_1 e_1$ + $\cdots$ + $x_n e_n$, thì $\varphi(\alpha) = x_1 \varepsilon_1$ + $\cdots$ + $x_n \varepsilon_n$.

Vì thế, ta có

$H(\alpha) = K(\varphi(\alpha)) = x_1^2$ + $\cdots$ + $x_n^2$ - $x_{n+1}^2$ - $\cdots$ - $x_{n+a}^2$

Như thế, hai dạng toàn phương H và K tương đương.

$\Box$

Theo hệ quả trên, mỗi lớp tương đương các dạng toàn phương trên không gian

vécto thực n chiều được đặt tương ứng một-một với một cặp số nguyên không âm

(p, q) sao cho p + q $\leq$ n. Vậy, số các lớp tương đương của các dạng toàn phương

trên không gian vécto thực n chiều bằng

$(n+1)+n+\cdots+1=\frac{(n+1)(n+2)}{2}$.



Nhận xét 4.7 Ta nói đôi điều về các dạng song tuyến tính và các dạng toàn

phương (trên không gian véctơ) phức. Mỗi dạng toàn phương H trên không gian

vécto phức V đều đưa được về dạng chính tắc trong một cơ sở nào đó của không

gian:

$H(\alpha) = a_1 z_1^2$ + $\cdots$ + $a_r z_r^2$, $\quad a_i \in \mathbf{C}$,

trong đó r $= \text{rank }$ H $\leq$ n $= \dim$ V. Vì mọi số phức đều có căn bậc hai, nên mỗi

dạng toàn phương phức H đều đưa được về dạng chuẩn tắc:

$H(\alpha) = t_1^2$ + $\cdots$ + $t_r^2$

trong đó $t_1$, ..., $t_n$ là toạ độ của $\alpha$ trong một cơ sở nào đó của V. Như vậy, các dạng

toàn phương phức được đặc trưng hoàn toàn bởi hạng của nó. Do đó, có tất cả

(n+1) lớp tương đương của các dạng toàn phương phức dưới tác động của nhóm

tự đẳng cấu GL(V).

Dạng toàn phương xác định dấu

$\overline{5}$

### Dịnh nghĩa 5.1 Giả sử A là một ma trận vuông. Các định thức con chính của A

là các định thức ở góc trái trên, bao gồm

$ \det(a_{11}), \det\left(\begin{array}{cc} a_{11} & a_{12} \\ a_{21} & a_{22} \end{array}\right), ..., \det A. $

Dinh lý 5.2 (Sylvester) Giá sử dạng toàn phương H trên không gian véctơ hữu

hạn chiều V có ma trận A trong một cơ sở nào đó. Khi đó

(i) H là xác định dương nếu và chỉ nếu mọi định thức con chính của A đều

$div\,\sigma\,nq$.

(ii) H là xác định âm nếu và chỉ nếu mọi định thức con chính cấp chẵn của A

đều dương, và mọi định thức con chính cấp lẻ của A đều âm.



Gọi $\eta$ là dạng cực của H, và $(e_1$, ..., $e_n)$ là cơ sở của không gian V trong đó H

có ma trận là A. Ký hiệu $V_k = \mathcal{L}(e_1$, ..., $e_k)$ (k $=$ 1, ..., n). Nếu H xác định dương

hoặc xác định âm thì $H|_{V_k}$ không suy biến với mọi k $=$ 1, ..., n.

Lặp lại quá trình trực giao hoá Shmidt ta có bổ đề sau.

Bổ đề 5.3 Giả sử hạn chế của H trên mỗi $V_k = \mathcal{L}(e_1$, ..., $e_k)$ đều không suy biến

(k $=$ 1, ..., n). Khi đó hệ vécto $(\varepsilon_1$, ..., $\varepsilon_k)$ xây dựng bởi quy nạp

$ \left\{ \begin{array}{lcl} \varepsilon_1 &=& e_1, \ \varepsilon_k &=& e_k - \sum_{i=1}^{k-1} \frac{\eta(e_k, \varepsilon_i)}{H(\varepsilon_i)} \varepsilon_i \end{array} \right. $

là một cơ sở $\eta-trực$ giao của $V_k$ (k $=$ 1, ..., n).

$\Box$

Chứng minh Định lý 5.2:

Trong cơ sở $\eta-trực$ giao $(\varepsilon_1$, ..., $\varepsilon_n)$, H có ma trận chéo

$ B = \left( \begin{array}{cccc} H(\varepsilon_1) & 0 & \dots & 0 \\ & 0 & H(\varepsilon_2) & \dots & 0 \\ & \cdot & \cdot & \dots & \cdot \\ 0 & 0 & \dots & H(\varepsilon_n) \end{array} \right). $

Gọi $A_k$ (tương ứng $B_k)$ là ma trận nằm ở giao của k hàng đầu và k cột đầu của A

(tương ứng của B). Khi đó $A_k$ và $B_k$ là ma trận của $H|_{V_k}$ tương ứng trong các cơ

sở $(e_1$, ..., $e_k)$ và $(\varepsilon_1$, ..., $\varepsilon_k)$. Gọi $C_k$ là ma trận chuyển từ cơ sở thứ nhất sang cơ sở

thứ hai, ta có

$B_k = C_k^t A_k C_k$.

Theo Bổ đề 5.3, $C_k$ là một ma trận tam giác trên với các phần tử trên đường

chéo bằng 1. Vì thế det $C_k = \det C_k^t =$ 1. Hệ quả là

det $A_k = \det B_k = H(\varepsilon_1) \cdots H(\varepsilon_k)$ (k $=$ 1, ..., n).

H là xác định dương khi và chỉ khi $H(\varepsilon_k) >$ 0 với mọi k $=$ 1, ..., n, tức là nếu

và chỉ nếu det $A_k >$ 0 (k $=$ 1, ..., n).



Hlà xác định âm khi và chỉ $khiH(\varepsilon_k) <$ 0với mọi $k=1,...,n,tức$ là nếu và

chỉ nếu det $A_k$ âm với mọi k lẻ và det $A_k$ dương với mọi k chẵn (k $=$ 1, ..., n).

$\Box$

Ví dụ: Dịnh thức Gram-Shmidt của hệ vécto $(u_1$, ..., $u_k)$ trong không gian vécto

Euclid E được định nghĩa như sau:

$ G(u_1,...,u_k) = \det \begin{pmatrix} \langle u_1, u_1 \rangle & \langle u_1, u_2 \rangle & ... & \langle u_1, u_k \rangle \\ \langle u_2, u_1 \rangle & \langle u_2, u_2 \rangle & ... & \langle u_2, u_k \rangle \\ . & . & ... & . \\ \langle u_k, u_1 \rangle & \langle u_k, u_2 \rangle & ... & \langle u_k, u_k \rangle \end{pmatrix}. $

Nếu vécto $u_j$ biểu thị tuyến tính qua những vécto còn lại của hệ thì cột thứ j

của định thức là một tổ hợp tuyến tính của những cột còn lại. Vậy, định thức

Gram-Shmidt của một hệ vécto phụ thuộc tuyến tính thì bằng 0.

Ngược lại, định thức Gram-Shmidt của một hệ vécto độc lập tuyến tính luôn

luôn dương. Thật vậy, nếu $(u_1$, ..., $u_k)$ là một hệ vécto độc lập tuyến tính thì ma

trận $(\langle u_i$, $u_j \rangle)_{i,j=1}^k$ chính là ma trận của tích vô hướng trong cơ sở $(u_1$, ..., $u_k)$ của

không gian $\mathcal{L}(u_1$, ..., $u_k)$. Vì tích vô hướng cảm sinh một dạng toàn phương xác

$\dim$ din duong, nên theo $\dim$ lý 5.2

$G(u_1,...,u_k)>0$.

Bài tập

Tìm dạng chuẩn tắc của các dạng toàn phương sau đây trên trường số thực:

1. $x_1^2$ + $x_2^2$ + $3x_3^2$ + $4x_1x_2$ + $2x_1x_3$ + $2x_2x_3$.

2. $x_1x_2$ + $x_1x_3$ + $x_1x_4$ + $x_2x_3$ + $x_2x_4$ + $x_3x_4$.

Tìm dạng chuẩn tắc của các dạng toàn phương sau đây và những phép biến

đổi tuyến tính không suy biến đưa dạng đã cho về dạng chuẩn tắc:



3. $2x_1^2$ + $18x_2^2$ + $8x_3^2$ - $12x_1x_2$ + $8x_1x_3$ - $27x_2x_3$.

4. $-12x_1^2$ - $3x_2^2$ - $12x_3^2$ + $12x_1x_2$ - $24x_1x_3$ + $8x_2x_3$.

Dưa các dạng toàn phương sau đây về dạng chính tắc với hệ số nguyên bằng

cách sử dụng các phép biến đổi tuyến tính không suy biến với hệ số hữu tỉ:

5. $2x_1^2$ + $3x_2^2$ + $4x_3^2$ - $2x_1x_2$ + $4x_1x_3$ - $3x_2x_3$.

6. $\frac{1}{2}x_1^2$ + $2x_2^2$ + $3x_4^2$ - $x_1x_2$ + $x_2x_3$ - $x_3x_4$.

Tìm phép biến đổi tuyến tính không suy biến đưa dạng toàn phương H về

dang toàn phương K:

7. H $= 2x_1^2$ + $9x_2^2$ + $3x_3^2$ + $8x_1x_2$ - $4x_1x_3$ - $10x_2x_3$

K $= 2y_1^2$ + $3y_2^2$ + $6y_3^2$ - $4y_1y_2$ - $4y_1y_3$ + $8y_2y_3$.

8. H $= 3x_1^2$ + $10x_2^2$ + $25x_3^2$ - $12x_1x_2$ - $18x_1x_3$ + $40x_2x_3$

K $= 5y_1^2$ + $6y_2^2$ + $12y_1y_2$.

9. H $= 5x_1^2$ + $5x_2^2$ + $2x_3^2$ + $8x_1x_2$ + $6x_1x_3$ + $6x_2x_3$

K $= 4y_1^2$ + $y_2^2$ + $9y_3^2$ - $12y_1y_3$.

Dưa các dạng toàn phương sau đây về dạng chính tắc và biểu thị các ẩn mới

qua các ẩn cũ:

10. $\sum_{i=1}^n x_i^2$ + $\sum_{i \leq i}^n x_i x_j$.

11. $\sum_{i < j}^{n} x_i x_j$.

12. $\sum_{i=1}^{n-1} x_i x_{i+1}$.

13. $\sum_{i=1}^n (x_i$ - $s)^2$, trong đó s $= \frac{x_1$ + $x_2$ + $\dots$ + $x_n}{n}$.

14. $\sum_{i=1}^n$ |i-j| $x_i x_j$.



15. Cho dang toàn phương

H $= f_1^2$ + $f_2^2$ + $\cdots$ + $f_n^2$ - $f_{n+1}^2$ - $f_{n+2}^2$ - $\cdots$ - $f_{n+q}^2$

trong đó $f_1$, ..., $f_{p+q}$ là các dạng tuyến tính thực của các biến $x_1$, ..., $x_n$. Chứng

minh rằng chỉ số quán tính dương của H không vượt quá p và chỉ số quán

tính âm của nó không vượt quá q.

16. Chứng minh rằng nếu có thể đưa mỗi dạng toàn phương H và K về dạng

kia bằng một phép biến đổi tuyến tính (không nhất thiết khả nghịch) thì các

dang này tương đương với nhau.

17. Các dạng toàn phương sau đây có tương đương với nhau trên trường số thực

hay không:

H $= x_1^2$ + $4x_2^2$ + $x_3^2$ + $4x_1x_2$ - $2x_1x_3$,

K $= y_1^2$ + $2y_2^2$ - $y_3^2$ + $4y_1y_2$ - $2y_1y_3$ - $4y_2y_3$,

L $= -4z_1^2$ - $z_2^2$ - $z_3^2$ - $4z_1z_2$ + $4z_1z_3$ + $18z_2z_3$.

18. Tìm hạng và kí số của dạng toàn phương thực H nếu nó tương đương với

-H bởi một phép biến đổi tuyến tính thực không suy biến.

19. Tìm số lớp tương đương của các dạng toàn phương thực n ẩn có kí số bằng

s dã cho.

20. Chứng minh rằng điều kiện cần và đủ để một dạng toàn phương H viết được

thành tích của hai dạng tuyến tính là:

(a) Đối với trường số thực: hạng của H không vượt quá 2, và nếu hạng của

H bằng 2 thì kí số của nó bằng 0.

(b) Đối với trường số phức: hạng của H không vượt quá 2.



21. Chứng minh rằng dang toàn phương thực H xác đinh dương nếu và chỉ nếu

ma trận của nó có thể viết dưới dạng A $=$ CtC, trong đó C là một ma trận

thực không suy biến.

22. Chứng minh rằng trong một dạng toàn phương thực xác định dương mọi

hệ số của các bình phương của các ẩn đều là số dương; nhưng điều kiện đó

không đủ để một dạng toàn phương là xác định dương.

23. Chứng minh rằng:

Diều kiện cần và đủ để ma trận đối xứng A viết được dưới dạng A $=$

(a)

CtC, trong đó C là một ma trận thực không suy biến là các định thức

con chính của A đều dương.

(b) Điều kiện cần và đủ để ma trận đối xứng A viết được dưới dạng A $=$

CtC, trong đó C là một ma trận vuông thực là các định thức con chính

của A đều không âm. Hơn nữa, nếu hạng của A bằng r thì hạng của C

cũng vậy, ngoài ra ta có thể chọn C với r hàng đầu độc lập tuyến tính

và các hàng còn lại bằng 0.

Tìm tất cả các giá trị của tham số $\lambda$ để cho dạng toàn phương sau đây xác

dinh duong:

24. $x_1^2$ + $x_2^2$ + $5x_3^2$ + $2\lambda x_1x_2$ - $2x_1x_3$ + $4x_2x_3$.

25. $x_1^2$ + $4x_2^2$ + $x_3^2$ + $2\lambda x_1x_2$ + $10x_1x_3$ + $6x_2x_3$.

26. Ta gọi hợp thành của hai dạng toàn phương H $= \sum_{i,j=1}^n a_{ij} x_i x_j$ và K $=$

$\sum_{i,j=1}^n b_{ij} x_i x_j$ là dạng toàn phương (H, K) $= \sum_{i,j=1}^n a_{ij} b_{ij} x_i x_j$. Chứng minh

$\hat{\text{rang}}:$

(a) Nếu H và K không suy biến thì (H, K) cũng vậy.

(b) Nếu H và K xác định dương thì (H, K) cũng vậy.



Tìm một phép biến đổi tuyến tính không suy biến đưa một trong hai dạng

toàn phương sau đây về dạng chuẩn tắc đồng thời đưa dạng còn lại về dạng

chính tắc, viết rõ biểu thức của các dang thu được:

27. H $= 8x_1^2$ - $28x_2^2$ + $14x_3^2$ + $16x_1x_2$ + $14x_1x_3$ + $32x_2x_3$

K $= x_1^2$ + $4x_2^2$ + $2x_3^2$ + $2x_1x_3$.

28. H $= 2x_1^2$ + $x_1x_2$ + $x_1x_3$ - $2x_2x_3$ + $2x_2x_4$

K $= \frac{1}{4}x_1^2$ + $x_2^2$ + $x_3^2$ + $2x_4^2$ + $2x_2x_4$.

29. H $= x_1^2$ + $\frac{3}{2}x_2^2$ - $2x_3^2$ + $x_4^2$ + $2x_1x_2$ + $4x_1x_3$

K $= x_1^2$ + $\frac{5}{4}x_2^2$ + $x_3^2$ + $x_4^2$ + $2x_2x_3$.

30. H $= x_1^2$ - $15x_2^2$ + $4x_1x_2$ - $2x_1x_3$ + $6x_2x_3$

K $= x_1^2$ + $17x_2^2$ + $3x_3^2$ + $4x_1x_2$ - $2x_1x_3$ - $14x_2x_3$.

31. Cho cặp dạng toàn phương H và K, trong đó K xác định dương. Xét phép

biến đổi tuyến tính không suy biến bất kỳ đưa K về dạng chuẩn tắc, đồng

thời đưa H về dạng chính tắc

H $= \lambda_1 y_1^2$ + $\cdots$ + $\lambda_n y_n^2$.

Chứng minh rằng các hệ số $\lambda_1$, ..., $\lambda_n$ được xác định duy nhất sai khác thứ tự.

Hơn nữa, chúng là các nghiệm của phương trình đa thức $\det(A$ - XB) $=$ 0

với ẩn X, trong đó A và B là các ma trận tương ứng của H và K trong cùng

một cơ sở nào đó của không gian.

Có thể đưa cặp dạng toàn phương sau đây về dạng chính tắc bởi cùng một

phép biến đổi tuyến tính thực không suy biến hay không?

32. H $= x_1^2$ + $4x_1x_2$ - $x_2^2$,

K $= x_1^2$ + $6x_1x_2$ + $5x_2^2$.

33. H $= x_1^2$ + $x_1x_2$ - $x_2^2$,

K $= x_1^2$ - $2x_1x_2$.



34. Cho cặp dạng toàn phương xác định dương H và K. Giả sử phép biến đổi

tuyến tính không suy biến thứ nhất đưa K về dạng chuẩn tắc, đồng thời đưa

H về dạng chính tắc H $= \sum_{i=1}^{n} \lambda_i y_i^2$ và phép biến đổi tuyến tính không suy

biến thứ hai đưa H về dạng chuẩn tắc, đồng thời đưa K về dạng chính tắc

K $= \sum_{i=1}^n \mu_i z_i^2$. Tìm mối liên hệ giữa các hệ số $\lambda_1$, ..., $\lambda_n$ và $\mu_1$, ..., $\mu_n$.

35. Ta nói các cặp dạng toàn phương $(H_1$, $K_1)$ và $(H_2$, $K_2)$, trong đó $K_1$ và $K_2$

xác định dương, là tương đương nếu có một phép biến đổi tuyến tính không

suy biến đưa $H_1$ về $H_2$ đồng thời đưa $K_1$ về $K_2$. Chứng minh rằng điều kiện

cần và đủ để hai cặp dạng trên tương đương là tập hợp nghiệm (kể cả bội)

của hai phương trình $\det(A_1$ - $XB_1) =$ 0 và $\det(A_2$ - $XB_2) =$ 0 trùng nhau.

Ở đây $A_i$ và $B_i$ là ma trận tương ứng của $H_i$ và $K_i$ trong cùng một cơ sở của

không gian.

36. Chứng minh rằng dạng chính tắc $\sum_{i=1}^{n} \lambda_i y_i^2$ mà dạng toàn phương H có thể

đưa về được nhờ một phép biến đổi trực giao được xác định duy nhất sai

khác thứ tự của các biến. Hơn nữa các hệ $số\lambda_1,...,\lambda_nlà$ các nghiệm của đa

thức đặc trưng của ma trận A của dạng H.

Tìm dạng chính tắc mà dạng toàn phương sau đây có thể đưa về nhờ một

phép biến đổi trực giao. Viết biểu thức tường minh của phép biến đổi đó.

37. $\sum_{i=1}^n x_i^2$ + $\sum_{i < j}^n x_i x_j$.

38. $\sum_{i < j}^{n} x_i x_j$.

39. Hai dạng toàn phương được gọi là tương đương trực giao nếu dạng này có

thể đưa về dang kia nhờ một phép biến đổi trưc giao. Chứng minh rằng điều

kiện cần và đủ để hai dạng toàn phương tương đương trực giao là các đa

thức đặc trưng của các ma trận của chúng trùng nhau.

40. Chứng minh rằng mọi ma trận đối xứng thực A đều có thể viết dưới dạng



$A=Q^{-1}BQ,trong$ đóQlà một ma trận trực giao vàB là một ma trận đường

chéo thực.

41. Chứng minh rằng mọi giá trị riêng của một ma trận thực A đều thuộc đoạn

[a, b]nếu và chỉ nếu dạng toàn phương với ma trận (A - $\lambda$ E) xác định dương

với mọi $\lambda <$ a và xác định âm với mọi $\lambda >$ b.

42. Giả sử A và B là các ma trận đối xứng thực. Chứng minh rằng nếu các trị

riêng của A đều thuộc đoạn [a, b] và các trị riêng của B đều thuộc đoạn [c, d]

thì các giá trị riêng của ma trận A + B đều thuộc đoạn [a + c, b + d].

43. Chứng minh rằng một dạng toàn phương không suy biến có thể đưa về dạng

chuẩn tắc nhờ một phép biến đổi trực giao nếu và chỉ nếu ma trận của nó

trong một cơ sở nào đó là một ma trận trực giao.

44. Chứng minh rằng ma trận của một dạng toàn phương xác định dương là trực

giao nếu và chỉ nếu dạng toàn phương đó là tổng của các bình phương. Hãy

diễn đạt sự kiện này bằng thuật ngữ ma trận.

45. Chứng minh rằng mọi ma trận không suy biến thực A có thể viết một cách

duy nhất dưới dạng A $=$ QB, trong đó Q là một ma trận trực giao và B là

một ma trận tam giác trên với các phần tử dương trên đường chéo chính.

46. Chứng minh rằng:

(a) Mỗi ma trận thực không suy biến A đều có thể viết dưới hai dạng

A $= Q_1 B_1$ và A $= B_2 Q_2$, trong đó $Q_1$, $Q_2$ là các ma trận trực giao và

$B_1$, $B_2$ là các ma trận đối xứng thực với các định thức con chính dương.

Mỗi cách viết đó đều duy nhất.

(b) Mỗi ma trận phức không suy biến A đều có thể viết dưới hai dạng

A $= Q_1 B_1$ và A $= B_2 Q_2$, trong đó $Q_1$, $Q_2$ là các ma trận unita và $B_1$, $B_2$



là các ma trận tự liên hợp, có các định thức con chính dương. Mỗi cách

viết đó đều duy nhất.

$\Omega$



# Chương VII

DAI SỐ ĐA TUYẾN TÍNH

Trong chương này, chúng ta trình bày các cấu trúc đa tuyến tính của đại số

tuyến tính. Vượt xa ra ngoài khuôn khổ của đại số tuyến tính, các cấu trúc này

tìm được nhiều ứng dụng trong Cơ học và Vật lý, trong Hình học vi phân, Giải

tích trên đa tạp và Lý thuyết biểu diễn nhóm...

Để chuẩn bị cho việc trình bày chương này, ta cần mấy định nghĩa sau đây.

### Định nghĩa 0.4 Một đại số trên trường K là một K-không gian vécto A được

trang bị một phép nhân $\cdot$ : A $\times$ A $\to$ A, $(\alpha$, $\beta) \mapsto \alpha \beta$ thoả mãn những điều kiện

sau:

(a) A cùng với phép cộng véctơ và phép nhân lập thành một vành.

(b) Các phép nhân với vô hướng và phép nhân của A liên hệ với nhau bởi hệ

thức

$(a\alpha)\beta = \alpha(a\beta) = a(\alpha\beta)$,

với moi a $\in \mathbf{K}$, $\alpha$, $\beta \in$ A.

Tập con khác rỗng B $\subset$ A được gọi là một đại số con của đại số A nếu nó vừa là

một không gian vécto con vừa là một vành con của A.

Cho các đại số A và A'. Anh xạ $\varphi:$ A $\to$ A' được gọi là một đồng cấu đại số

nếu nó vừa là một đồng cấu không gian vécto vừa là một đồng cấu vành.

Chẳng hạn, K-không gian vécto các ma trận vuông M(n $\times$ n, $\mathbf{K})$ với phép nhân

ma trận là một đại số trên trường K.



### Định nghĩa 0.5 Giả sử A là một đại số trên K. Không gian véctor con B \subset A

được gọi là một idêan của đại số A nếu nó có tính chất hấp thụ, tức là nếu:

$\alpha\beta \in$ B, $\beta\alpha \in$ B,

với mọi $\alpha \in$ A, $\beta \in$ B.

Chẳng hạn, tập các ma trận tam giác trên với các phần tử trên đường chéo

bằng 0 là một iđêan của đại số ma trận M(n $\times$ n, $\mathbf{K})$.

Dễ thấy rằng, nếu B là một iđêan của đại số A thì không gian thương A/B trở

thành một đại số, gọi là đại số thương, với phép nhân định nghĩa như sau:

$(\alpha$ + $B)(\alpha'$ + B) $= (\alpha \alpha')$ + B.

Nền tảng của các cấu trúc đa tuyến tính là khái niệm tích tenxo của các không

gian vécto.

Tích tenxo

$\mathbf$ 1

Giả sử L, M, N là các không gian vécto trên trường K. Ánh xạ $\varphi:$ L $\times$ M $\to$ N

được gọi là song tuyến tính nếu

$\varphi(\alpha_1$ + $\alpha_2$, $\beta) = \varphi(\alpha_1$, $\beta)$ + $\varphi(\alpha_2$, $\beta)$,

$\varphi(a\alpha,\beta) = a\varphi(\alpha,\beta)$,

$\varphi(\alpha,\beta_1+\beta_2) = \varphi(\alpha,\beta_1)$ + $\varphi(\alpha,\beta_2)$,

$\varphi(\alpha$, $a\beta) = a\varphi(\alpha$, $\beta)$,

với mọi $\alpha$, $\alpha_1$, $\alpha_2 \in$ L, $\beta$, $\beta_1$, $\beta_2 \in$ M, a $\in \mathbf{K}$. Nói cách khác, ánh xạ song tuyến tính

là một ánh xạ tuyến tính với mỗi biến khi cổ định biến kia.

Gọi F(L $\times$ M) là tập hợp tất cả các hàm có giá hữu hạn từ L $\times$ M vào trường

K, tức là các hàm chỉ khác 0 tại một số hữu hạn điểm nào đó của L $\times$ M. Tập



hợp này lập nên một K-không gian vécto đối với các phép toán cộng và nhân với

vô hướng được định nghĩa theo giá trị của hàm, cụ thể như sau:

$(f+g)(\alpha,\beta) = f(\alpha,\beta)$ + $g(\alpha,\beta)$,

(a $f)(\alpha$, $\beta) = af(\alpha$, $\beta)$,

với mọi f, g $\in$ F(L $\times$ M), a $\in \mathbf{K}$, $(\alpha$, $\beta) \in$ L $\times$ M.

Mỗi phần tử $(\alpha$, $\beta) \in$ L $\times$ M được đặt tương ứng với một hàm, cũng ký hiệu

là $(\alpha$, $\beta) \in$ F(L $\times$ M) được định nghĩa như sau:

$(\alpha$, $\beta)$ : L $\times$ M $\rightarrow \mathbf{K}$,

$(\alpha$, $\beta) \rightarrow$ 1,

$(\alpha'$, $\beta') \mapsto$ 0, $\forall (\alpha'$, $\beta') \neq (\alpha$, $\beta)$.

Giả sử f $\in$ F(L $\times$ M)là hàm chỉ khác 0 trên tập hữu $hạn\{(\alpha_i$, $\beta_i)$ | i $\in I\}$, với

$f(\alpha_i$, $\beta_i) = a_i$. Dễ thấy rằng

f $= \sum_{i \in I} a_i(\alpha_i$, $\beta_i)$.

Như vậy, một cách trực giác, ta có thể hiểu F(L $\times$ M) là tập hợp các tổng hình

thức có giá hữu hạn của các phần tử trong L $\times$ M với hệ số trong K.

Gọi H là không gian véctor con của F(L $\times$ M) sinh bởi các phần tử có dạng sau

dây:

$(\alpha_1+\alpha_2,\beta)-(\alpha_1,\beta)-(\alpha_2,\beta)$,

$(a\alpha$, $\beta)$ - $a(\alpha$, $\beta)$,

$(\alpha$, $\beta_1$ + $\beta_2)$ - $(\alpha$, $\beta_1)$ - $(\alpha$, $\beta_2)$,

$(\alpha$, $a\beta)$ - $a(\alpha$, $\beta)$,

trong đó $\alpha$, $\alpha_1$, $\alpha_2 \in$ L, $\beta$, $\beta_1$, $\beta_2 \in$ M, a $\in \mathbf{K}$.

Dinh nghĩa 1.1 Ta gọi không gian vécto thương F(L $\times$ M)/H là tích tenxo của

các không gian L và M. Nó được ký hiệu bởi L $\otimes$ M, hoặc chi tiết hơn L $\otimes_K$ M.



Ánh của phần tử $(\alpha$, $\beta)$ bởi phép chiếu chính tắc F(L $\times$ M) $\to$ L $\otimes$ M được ký

hiệu là $\alpha \otimes \beta$. Như vậy

$\alpha \otimes \beta = [(\alpha$, $\beta)] := (\alpha$, $\beta)$ + H.

Theo định nghĩa của không gian con H, ta có

$(\alpha_1$ + $\alpha_2) \otimes \beta = \alpha_1 \otimes \beta$ + $\alpha_2 \otimes \beta$,

$(a\alpha) \otimes \beta = a(\alpha \otimes \beta)$,

$\alpha \otimes (\beta_1$ + $\beta_2) = \alpha \otimes \beta_1$ + $\alpha \otimes \beta_2$,

$\alpha \otimes (a\beta) = a(\alpha \otimes \beta)$,

trong đó $\alpha$, $\alpha_1$, $\alpha_2 \in$ L, $\beta$, $\beta_1$, $\beta_2 \in$ M, a $\in \mathbf{K}$. Nói cách khác, ánh xạ

t: L $\times$ M $\rightarrow$ L $\otimes$ M

định nghĩa bởi công thức $t(\alpha$, $\beta) = \alpha \otimes \beta$ là một ánh xạ song tuyến tính.

Tích tenxo được xây dựng nhằm mục đích tuyến tính hoá các ánh xạ song

tuyến tính. Điều này được nói rõ trong định lý sau đây.

Dinh lý 1.2 (Tính phổ dụng của tích tenxo). Với mọi ánh xạ song tuyến tính

$\varphi:$ L $\times$ M $\to$ N, tồn tại duy nhất ánh xạ tuyến tính h: L $\otimes$ M $\to$ N làm giao hoán

$bi\mathring{e}u\ d\mathring{o}$

L $\times$ M $\longrightarrow$ L $\otimes$ M

N,

tức là $\varphi =$ h $\circ$ t.

Chứng minh: Ta thác triển ánh xạ $\varphi$ thành ánh xạ $\tilde{\varphi}:$ F(L $\times$ M) $\to$ N xác định

bởi công thức

$\tilde{\varphi}(\sum_{i\in I} a_i(\alpha_i,\beta_i)) = \sum_{i\in I} a_i \varphi(\alpha_i,\beta_i)$.



Rõ ràng $\tilde{\varphi}$ là một ánh xạ tuyến tính. Hơn nữa, do $\varphi$ là song tuyến tính cho nên

H $\subset$ Ker $\tilde{\varphi}$. Thật vậy

$\tilde{\varphi}((\alpha_1+\alpha_2,\beta)-(\alpha_1,\beta)-(\alpha_2,\beta))=\varphi(\alpha_1+\alpha_2,\beta)-\varphi(\alpha_1,\beta)-\varphi(\alpha_2,\beta)=0$,

$\tilde{\varphi}((a\alpha,\beta)-a(\alpha,\beta))=\varphi(a\alpha,\beta)-a\varphi(\alpha,\beta)=0$,

$\tilde{\varphi}((\alpha,\beta_1+\beta_2)-(\alpha,\beta_1)-(\alpha,\beta_2))=\varphi(\alpha,\beta_1+\beta_2)-\varphi(\alpha,\beta_1)-\varphi(\alpha,\beta_2)=0$,

$\tilde{\varphi}((\alpha$, $a\beta)$ - $a(\alpha$, $\beta)) = \varphi(\alpha$, $a\beta)$ - $a\varphi(\alpha$, $\beta) =$ 0,

với mọi $\alpha$, $\alpha_1$, $\alpha_2 \in$ L, $\beta$, $\beta_1$, $\beta_2 \in$ M, a $\in \mathbf{K}$.

Do H $\subset$ Ker $\tilde{\varphi}$, ánh xạ tuyến tính $\tilde{\varphi}$ cảm sinh ánh xạ tuyến tính

h: L $\otimes$ M $\ := \$ F(L $\times$ M)/H $\to$ N

h[x] $= \tilde{\varphi}(x)$,

ở đây [x] $=$ x + H là lớp của phần tử x bất kỳ trong F(L $\times$ M).

Với mọi $\alpha \in$ L, $\beta \in$ M, ta có

$\varphi(\alpha,\beta) = \tilde{\varphi}(\alpha,\beta) = h[(\alpha,\beta)] = h(\alpha \otimes \beta) = h(t(\alpha,\beta))$.

Vì thế $\varphi =$ h $\circ$ t.

Tiếp theo, ta chứng minh tính duy nhất của h. Giả sử h' : L $\otimes$ M $\to$ N cũng là

một ánh xạ tuyến tính thoả mãn hệ thức $\varphi =$ h $\circ$ t $=$ h' $\circ$ t. Như thế h $=$ h' trên

Im(t).

Không gian F(L $\times$ M) được sinh bởi các phần tử có dạng $(\alpha$, $\beta)$, do đó L $\otimes$ M $:=$

F(L $\times$ M)/H được sinh bởi các phần tử có dạng $(\alpha$, $\beta)$ + H $= \alpha \otimes \beta = t(\alpha$, $\beta)$. Nói

cách khác, Im(t) sinh ra không gian L $\otimes$ M. Các ánh xạ tuyến tính h và h' bằng

nhau trên Im(t), nên chúng bằng nhau trên toàn không gian L $\otimes$ M.

$\Box$

Gọi $\mathcal{L}(L$, M; N) là không gian vécto các ánh xạ song tuyến tính từ L $\times$ M vào

N. Định lý 1.2 cho phép xây dựng một ánh xạ $\mathcal{L}(L$, M; N) $\to \mathcal{L}(L \otimes$ M, N) bằng

cách chuyển $\varphi$ thành h. Đó là một đẳng cấu tuyến tính:

$H\hat{e}$ quả 1.3

$\mathcal{L}(L,M;N) \cong \mathcal{L}(L \otimes$ M,N).

$\Box$



Tích tenxo của hai ánh xạ tuyến tính được định nghĩa như sau. Giả sử f: L $\to$

N và g: M $\to$ P là các ánh xạ tuyến tính. Dễ thấy rằng ánh xạ

f $\times$ g : L $\times$ M $\rightarrow$ N $\otimes$ P

(f $\times g)(\alpha$, $\beta) = f(\alpha) \otimes g(\beta)$, $\quad \alpha \in$ L, $\beta \in$ M

là song tuyến tính. Do đó, theo Định lý 1.2, tồn tại duy nhất một ánh xạ được ký

hiệu là f $\otimes$ g : L $\otimes$ M $\to$ N $\otimes$ P có tính chất (f $\otimes g)(\alpha \otimes \beta) = f(\alpha) \otimes g(\beta)$. Ánh xạ

f $\otimes$ g được gọi là tích tenxo của f và q.

Các tính chất cơ bản của tích tenxơ

$\bf{2}$

Trong các mệnh đề sau đây, giả sử L, M, N là các không gian vécto trên trường K.

Mệnh đề 2.1 (Tính kết hợp). Tồn tại duy nhất một đẳng cấu tuyến tính

(L $\otimes$ M) $\otimes$ N $\stackrel{\cong}{\rightarrow}$ L $\otimes$ (M $\otimes$ N),

sao cho $(\alpha \otimes \beta) \otimes \gamma \mapsto \alpha \otimes (\beta \otimes \gamma)$ với mọi $\alpha \in$ L, $\beta \in$ M, $\gamma \in$ N.

Chứng minh: Ta xét ánh xạ $\tau$ : (L $\otimes$ M) $\times$ N $\to$ L $\otimes$ (M $\otimes$ N) xác định bởi

$\tau((\alpha \otimes \beta)$, $\gamma) = \alpha \otimes (\beta \otimes \gamma)$. Dễ kiểm tra lại rằng đó là một ánh xạ song tuyến tính

đối với các biến $\alpha \otimes \beta$ và $\gamma$. Theo Định lý 1.2, tồn tại duy nhất một ánh xạ tuyến

tính h: (L $\otimes$ M) $\otimes$ N $\to$ L $\otimes$ (M $\otimes$ N) sao cho $h((\alpha \otimes \beta) \otimes \gamma) = \alpha \otimes (\beta \otimes \gamma)$, với

moi $\alpha \in$ L, $\beta \in$ M, $\gamma \in$ N.

Tương tự, tồn tại duy nhất một ánh xạ tuyến tính k: $L\otimes (M\otimes$ N) $\to (L\otimes M)\otimes$ N

sao cho $k(\alpha \otimes (\beta \otimes \gamma)) = (\alpha \otimes \beta) \otimes \gamma$, với mọi $\alpha \in$ L, $\beta \in$ M, $\gamma \in$ N.

Như vậy, kh : (L $\otimes$ M) $\otimes$ N $\to$ (L $\otimes$ M) $\otimes$ N là một ánh xạ tuyến tính thoả mãn

$kh((\alpha \otimes \beta) \otimes \gamma) = (\alpha \otimes \beta) \otimes \gamma$, với mọi $\alpha \in$ L, $\beta \in$ M, $\gamma \in$ N. Nói cách khác, kh

trùng với ánh xạ đồng nhất id trên tập các vécto có dạng $(\alpha \otimes \beta) \otimes \gamma;$ đó là một

tập sinh của không gian (L $\otimes$ M) $\otimes$ N. Do đó kh $=$ id, bởi vì cả hai đều là các ánh

xạ tuyến tính.



Lập luận tương tự, ta có hk $=$ id. Hai đẳng thức kh $=$ id và hk $=$ id chứng tỏ

rằng h là một đẳng cấu tuyến tính.

$\Box$

Mệnh đề này cho phép ta định nghĩa tích $tenx<br/>ơL_1\otimes L_2\otimes\cdots\otimes L_ncủankhông$

gian vécto $L_1$, $L_2$, ..., $L_n$.

Chúng tôi đề nghị độc giả tự chứng minh ba mệnh đề dưới đây, xem như những

bài tập.

Mệnh đề 2.2 (Tính giao hoán). Tồn tại duy nhất một đẳng cấu tuyến tính

L $\otimes$ M $\stackrel{\cong}{\rightarrow}$ M $\otimes$ L,

sao cho $\alpha \otimes \beta \mapsto \beta \otimes \alpha$ vói mọi $\alpha \in$ L, $\beta \in$ M.

Mệnh đề 2.3 (Tính "có đơn vị"). Tồn tại duy nhất đẳng cấu tuyến tính

$\mathbf{K} \otimes_{\mathbf{K}}$ L $\stackrel{\cong}{\to}$ L $\otimes_{\mathbf{K}} \mathbf{K} \stackrel{\cong}{\to}$ L,

sao cho a $\otimes \alpha \mapsto \alpha \otimes$ a $\mapsto a\alpha$ với mọi a $\in \mathbf{K}$, $\alpha \in$ L.

Mệnh đề 2.4 (Tính phân phối).

(L $\oplus$ M) $\otimes$ N $\cong$ (L $\otimes$ N) $\oplus$ (M $\otimes$ N),

L $\otimes$ (M $\oplus$ N) $\cong$ (L $\otimes$ M) $\oplus$ (L $\otimes$ N).

Hệ quả 2.5 Giả sử $(\alpha_1$, ..., $\alpha_m)$ và $(\beta_1$, ..., $\beta_n)$ là các cơ sở tương ứng của các

không gian véctor L và M. Khi đó, hê véctor

$(\alpha_i\beta_j \mid$ 1 $\leq$ i $\leq$ m, 1 $\leq$ j $\leq$ n)

là một cơ sở của không gian véctơ L $\otimes$ M. Nói riêng

$\dim(L \otimes$ M) $= \dim$ L $\cdot \dim$ M.



Chứng minh: Theo đinh nghĩa của cơ sở, ta có các đẳng cấu tuyến tính

L $\cong \bigoplus_{i=1}^m \mathbf{K}\alpha_i \quad$ M $\cong \bigoplus_{i=1}^n \mathbf{K}\beta_i$.

Áp dụng hai mệnh đề kế trên, ta có

L $\otimes$ M $\cong (\bigoplus_{i=1}^m \mathbf{K}\alpha_i) \otimes (\bigoplus_{i=1}^n \mathbf{K}\beta_i)$

$\cong \oplus_{i=1}^m \oplus_{j=1}^n (\mathbf{K}\alpha_i) \otimes (\mathbf{K}\beta_j)$

$\cong \oplus_{i=1}^m \oplus_{j=1}^n \mathbf{K}(\alpha_i \otimes \beta_j)$.

Dằng thức này chứng tỏ hệ vécto $(\alpha_i\beta_j$ | 1 $\leq$ i $\leq$ m, 1 $\leq$ j $\leq$ n) là một cơ sở của

không gian véctor L $\otimes$ M.

$\Box$

Các ví dụ sau đây giới thiệu một số đẳng cấu chính tắc liên quan đến tích tenxơ.

Ví dụ 2.6 Nếu $L_1$, ..., $L_n$ là các không gian vécto hữu hạn chiều thì

$L_1^* \otimes \cdots \otimes L_n^* \cong (L_1 \otimes \cdots \otimes L_n)^*$.

Bằng phép quy nạp, ta chỉ cần kiểm chứng ví dụ này cho n $=$ 2. Giả sử

$f_1: L_1 \to \mathbf{K}$, $f_2: L_2 \to \mathbf{K}$ là các ánh xạ tuyến tính. Xét hợp thành của ánh xạ

$f_1 \otimes f_2: L_1 \otimes L_2 \to \mathbf{K} \otimes \mathbf{K}$ với đẳng cấu tuyến tuyến tính $\iota: \mathbf{K} \otimes \mathbf{K} \to \mathbf{K}$, $\$ a $\otimes$ b $\mapsto$ ab,

ta có $\iota \circ (f_1 \otimes f_2) \in (L_1 \otimes L_2)^*$. Tuong úng

$L_1^* \times L_2^* \rightarrow (L_1 \otimes L_2)^*$,

$(f_1$, $f_2) \rightarrow \iota \circ (f_1 \otimes f_2)$

hiển nhiên là một ánh xạ song tuyến tính. Theo Định lý 1.2, có duy nhất một ánh

xạ tuyến tính h: $L_1^* \otimes L_2^* \to (L_1 \otimes L_2)^*$ sao cho $h(f_1 \otimes f_2) = \iota \circ (f_1 \otimes f_2)$.

Ánh xạ h chính là đẳng cấu phải tìm.

Ví dụ 2.7 $L^* \otimes$ M $\cong \mathcal{L}(L$, M).



Xét ánh xạ song tuyến tính

$L^* \times$ M $\rightarrow \mathcal{L}(L,M)$,

(f, $\beta) \mapsto [\alpha \mapsto f(\alpha)\beta]$,

trong đó f $\in L^*$, $\alpha \in$ L, $\beta \in$ M. Theo Định lý 1.2, ánh xạ nói trên cảm sinh một

ánh xạ tuyến tính duy nhất

$L^* \otimes$ M $\rightarrow \mathcal{L}(L,M)$,

f $\otimes \beta \mapsto [\alpha \mapsto f(\alpha)\beta]$.

Đó là một đẳng cấu tuyến tính.

Ví dụ 2.8 $\mathcal{L}(L \otimes$ M, N) $\cong \mathcal{L}(L$, $\mathcal{L}(M$, N)).

Ta đã biết rằng $\mathcal{L}(L \otimes$ M, N) $\cong \mathcal{L}(L$, M; N). Ánh xạ

$\mathcal{L}(L,M;N) \rightarrow \mathcal{L}(L,\mathcal{L}(M,N))$,

f $\mapsto [\alpha \mapsto [\beta \mapsto f(\alpha$, $\beta)]]$,

trong đó f $\in \mathcal{L}(L$, M; N), $\alpha \in$ L, $\beta \in$ M, chính là đẳng cấu tuyến tính cần tìm.

Dai số tenxo

$3\overline{)}$

Với mỗi K-không gian vécto L, ta xét tích tenxo

$T_p^q(L) = L^* \otimes \cdots \otimes L^* \otimes$ L $\otimes \cdots \otimes$ L.

### Định nghĩa 3.1 Mỗi phần tử của không gian T_p^q(L) được gọi là một tenxo kiểu

(p, q) hay là một tenxo p lần thuận biến và q lần phản biến trên không gian L.

Ta có thể đồng nhất $T_p^q(L)$ với $(\underbrace{L \otimes \cdots \otimes L}_{p} \otimes \underbrace{L^* \otimes \cdots \otimes L^*}_{q})^*$. Vì thế, mỗi tenxo

p lần thuận biến và q lần phản biến được đồng nhất với một ánh xạ đa tuyến tính

$\underbrace{L \times \cdots \times L}_{n} \times \underline{L}^{*} \times \cdots \times \underline{L}^{*} \to \mathbf{K}$.

$\Delta \alpha \alpha$



Các đẳng cấu tuyến tính nói trong các Mênh đề 2.1 và 2.2 cho phép xác định

đằng cấu tuyến tính chính tắc (có được bằng cách tráo đổi thứ tự các nhân tử)

$\mu_p^q$ : $(\underbrace{L^* \otimes \cdots \otimes L^*}_{p} \otimes \underbrace{L \otimes \cdots \otimes L}_{q}) \quad \otimes \quad (\underbrace{L^* \otimes \cdots \otimes L^*}_{p'} \otimes \underbrace{L \otimes \cdots \otimes L}_{q'})$

$\rightarrow \underbrace{L^*\otimes\cdots\otimes L^*}_{p+p'}\otimes \underbrace{L\otimes\cdots\otimes L}_{n+n'}$ .

Ta viết gọn đẳng cấu nói trên dưới dạng

$\mu_n^q: T_n^q(L) \otimes T_{n'}^{q'}(L) \to T_{n+n'}^{q+q'}(L)$.

Xét tổng trực tiếp

T(L) $= \bigoplus_{p,q=0}^{\infty} T_p^q(L)$.

Họ các ánh $xạ\{\mu_p^q$ | 0 $\leq$ p, q $< \infty\}xác$ định một ánh xạ tuyến tính

$\mu:$ T(L) $\otimes$ T(L) $\rightarrow$ T(L).

Nói cách khác, T(L) được trang bị một phép nhân định nghĩa như sau:

T(L) $\times$ T(L) $\rightarrow$ T(L),

$(\alpha$, $\beta) \mapsto \mu(\alpha \otimes \beta)$.

### Định lý sau đây được kiểm nghiệm không mấy khó khăn.

Dinh lý 3.2 T(L) là một đại số trên trường K.

Dinh nghĩa 3.3 T(L) được gọi là đại số tenxo của không gian vécto L.

Đại số tenxo T(L) có hai đại số con hiển nhiên, đó là $T_*(L) = \bigoplus_{p=0}^{\infty} T_p^0(L)$ và

$T^*(L) = \bigoplus_{q=0}^{\infty} T_0^q(L)$. Hạn chế của tích $\mu$ của T(L) trên các đại số con này đơn giản

chỉ là việc "viết liền" các tenxo với nhau. Vì thế, tích của các đại số con này được

ký hiệu đơn giản bởi $\otimes$.

Tiếp theo, ta xét biểu thức toạ độ của một tenxo.



Giả sử $(e_1$, ..., $e_n)$ là một cơ sở của không gian vécto L. Trong lý thuyết tenxo,

để cho gọn người ta thường ký hiệu cơ sở đối ngẫu với $(e_1$, ..., $e_n)$ là $(e^1$, ..., $e^n)$. Đó

là cơ sở của $L<sup>*</sup>$ được xác định bởi điều kiện sau đây:

$\langle \cdot$, $\cdot \rangle$ : L $\times L^* \rightarrow \mathbf{K}$,

$ \langle e_j, e^i \rangle = \delta^i_j = \begin{cases} 1, & \text{m\'eu } i = j, \\ 0, & \text{m\'eu } i \neq j. \end{cases} $

Theo Hệ quả 2.5, hệ vécto sau đây lập nên một cơ sở của không gian vécto $T_p^q(L):$

$(e^{i_1}\otimes \cdots \otimes e^{i_p}\otimes e_{i_1}\otimes \cdots \otimes e_{i_n}$ 1 $\leq i_1$, ..., $i_p$, $j_1$, ..., $j_q \leq$ n.

Như vậy, mỗi tenxo T $\in T_p^q(L)$ có biểu thị tuyến tính duy nhất

T $= \sum_{i_1,\dots,i_p,j_1,\dots,j_q} T_{i_1,\dots,i_p}^{j_1,\dots,j_q} e^{i_1} \otimes \cdots \otimes e^{i_p} \otimes e_{j_1} \otimes \cdots \otimes e_{j_q}$,

trong đó $T^{j_1,...,j_q}_{i_1,...,i_n} \in \mathbf{K}$ là các toạ độ của T trong cơ sở nói trên.

Dấu tổng trong công thức trên quá cồng kềnh. Để đơn giản hoá, người ta đặt

ra qui vớc cổ điển sau đây.

Quy ước 3.4 Trong các phép tính với tenxo, ta sẽ không viết (mà hiểu ngầm) dấu

tổng trong trường hợp tổng được lấy theo một cặp chỉ số giống nhau, trong đó có

một chỉ số trên và một chỉ số dưới.

Theo qui trớc này thì công thức ở trên có thể viết lại như sau:

$T=T_{i_1,\dots,i_n}^{j_1,\dots,j_q}e^{i_1}\otimes\cdots\otimes e^{i_p}\otimes e_{j_1}\otimes\cdots\otimes e_{j_q}$.

Giả sử $(e'_1$, ..., $e'_n)$ cũng là một cơ sở của L, và A $= (a_\ell^j)$, trong đó $a_\ell^j$ là phần tử

nằm ở hàng j cột $\ell$ của ma trận A, là ma trận chuyển từ $(e_1$, ..., $e_n)$ sang $(e'_1$, ..., $e'_n)$,

nghĩa là

$e'_{\ell} = a_{\ell}^j e_j$.



Gọi B $= (b_i^k)$ là chuyển vị của ma trận chuyển từ $(e^1$, ..., $e^n)$ sang $(e'^1$, ..., $e'^n)$, nghĩa

là $e'^k = b_i^k e^i$. Ta có

$\delta_{\ell}^{k} = \langle e'_{\ell}$, $e'^{k} \rangle = \langle a_{\ell}^{j} e_{j}$, $b_{i}^{k} e^{i} \rangle = a_{\ell}^{j} b_{i}^{k} \langle e_{j}$, $e^{i} \rangle$

$= a^j_{\ell}b^k_i\delta^i_j = a^i_{\ell}b^k_i$.

Diều này tương đương với đẳng thức ma trận BA $= E_n$. Hay là B $= A^{-1}$.

Giả sử biểu thức toạ độ của tenxo T trong cơ sở mới là

T $= T'^{\ell_1,\ldots,\ell_q}_{k_1,\ldots,k_n} e'^{k_1} \otimes \cdots \otimes e'^{k_p} \otimes e'_{\ell_1} \otimes \cdots \otimes e'_{\ell_q}$.

Ta có

T $= T'^{\ell_1$, $\ldots$, $\ell_q}_{k_1$, $\ldots$, $k_n}(b^{k_1}_{i_1}e^{i_1}) \otimes \cdots \otimes (b^{k_p}_{i_p}e^{i_p}) \otimes (a^{j_1}_{\ell_1}e_{j_1}) \otimes \cdots \otimes (a^{j_q}_{\ell_q}e_{j_q})$

$= a_{\ell_1}^{j_1} \cdots a_{\ell_q}^{j_q} b_{i_1}^{k_1} \cdots b_{i_p}^{k_p} T_{k_1,\ldots,k_p}^{\prime \ell_1,\ldots,\ell_q} e^{i_1} \otimes \cdots \otimes e^{i_p} \otimes e_{j_1} \otimes \cdots \otimes e_{j_q}$.

Do tính duy nhất của toạ độ của một vécto trong một cơ sở, ta nhận được

$T^{j_1,...,j_q}_{i_1,...,i_p}=a^{j_1}_{\ell_1}\cdots a^{j_q}_{\ell_q}b^{k_1}_{i_1}\cdots b^{k_p}_{i_p}T'^{\ell_1,...,\ell_q}_{k_1,...,k_p}$.

Dó là công thức đổi toạ độ của tenxo.

Sau đây là các ví dụ về một vài tenxo quan trọng.

(a) Ma trận và ánh xạ tuyến tính: Theo Ví dụ 2.7, không gian các

Ví du 3.5

ánh xạ tuyến tính $\mathcal{L}(L$, L) được đồng nhất với tích tenxo $L^* \otimes$ L $= T_1^1(L)$.

Mỗi phần tử f của nó với biểu thức toạ độ

f $= a_i^i e^j \otimes e_i$

được đồng nhất với ánh xạ tuyến tính f: L $\to$ L xác định bởi

$f(e_j) = a_i^i e_i$.

Nói cách khác, ma trận A $= (a_j^i)$ với phần tử $a_j^i$ nằm ở hàng i cột j chính là

ma trận của ánh xạ f trong cơ sở $(e_1$, ..., $e_n)$.



Tenxo mêtríc: Theo Hệ quả 1.3 và Ví dụ 2.6, tích tenxo $T_2^0(L) = L^* \otimes L^*$

(b)

được đồng nhất với không gian(L $\otimes L)^* \equiv \mathcal{L}(L$, L; $\mathbf{K})các$ ánh xạ song tuyến

tính từ L $\times$ L vào K. Mỗi phần tử của nó

g $= g_{ij}e^i \otimes e^j$

được đồng nhất với dạng song tuyến tínhg: L $\times$ L $\rightarrow \mathbf{K}xác$ định bởi

$g(e_i$, $e_j) = g_{ij}$.

Hàm g là đối xứng nếu và chỉ nếu $g_{ij} = g_{ji}$ với mọi i, j. Giả sử $\mathbf{K} = \mathbf{R}$, hàm

g đối xứng và ma trận Gram-Shmidt G $= (g_{ij})$ có các định thức con chính

đều dương. Khi đó, tenxo g là một tích vô hướng trên L. Nó được gọi là

một tenxo mêtríc.

Tenxo cấu trúc đại số: Theo Hệ quả 1.3 cùng các Ví dụ 2.6 và 2.7, tích

(c)

tenxo $T_2^1(L) = L^* \otimes L^* \otimes$ L được đồng nhất với không gian các ánh xạ

$\mathcal{L}(L\otimes L,L)\equiv \mathcal{L}(L,L;L)$. Mỗi phần tử của tích tenxo đó

m $= m_{ij}^t e^i \otimes e^j \otimes e_t$

được đồng nhất với một ánh xạ tuyến tính m: L $\otimes$ L $\rightarrow$ Lxác định bởi

$m(e_i \otimes e_j) = m_{ij}^t e_i$.

Ánh xạ này trang bị cho L một cấu trúc đại số nếu và chỉ nếu nó có tính kết

hợp, nghĩa là:

$m(m(e_i \otimes e_j) \otimes e_k) = m(e_i \otimes m(e_j \otimes e_k))$,

với mọi i, j, k. Đẳng thức này tương đương với

$m_{ij}^{t}m_{tk}^{\ell}=m_{it}^{\ell}m_{jk}^{t}$,

với mọi i, j, k, $\ell$. Nói cách khác, mỗi tenxo m thoả mãn hệ thức trên được

đồng nhất với một cấu trúc đại số trên không gian vécto L. Nó được gọi là

một tenxo cấu trúc đại số trên L.



Dại số đối xứng

$\boldsymbol{4}$

Trong các cách định nghĩa khác nhau của khái niệm tenxo đối xứng và đại số đối

xứng, chúng ta chọn cách không phụ thuộc vào đặc số của trường K.

Ta vân giả sử L là một không gian vécto trên trường $\mathbf{K}$.

$GọiA_qlà$ không gian véctor con của $T^q(L):=T^q_0(L)sinh$ bởi các véctor có dạng

$\alpha_1 \otimes \cdots \otimes \alpha_q$ - $\alpha_{\sigma(1)} \otimes \cdots \otimes \alpha_{\sigma(q)}$,

trong đó $\alpha_1$, ..., $\alpha_q \in$ L, $\sigma \in S_q$ (nhóm đối xứng trên q phần tử).

Dinh nghĩa 4.1 Không gian thương

$S^{q}(L) := T^{q}(L)/A_{q}$

được gọi là luỹ thừa đối xứng cấp q của L. Mỗi phần tử của $S^q(L)$ được gọi là một

tenxo $\$, $d\tilde{o}i$ xứng trên L.

Để cho gọn, ta ký hiệu $L^{(q)} :=$ L $\times \cdots \otimes$ L (q lần).

### Dịnh nghĩa 4.2 Giả sử M là một K-không gian vécto. Anh xạ đa tuyến tính

$\psi: L^{(q)} \to$ M được gọi là đối xúng nếu

$\psi(\alpha_1,...,\alpha_q)=\psi(\alpha_{\sigma(1)},...,\alpha_{\sigma(q)})$,

với mọi $\alpha_1$, ..., $\alpha_q \in$ L, $\sigma \in S_q$.

Hợp thành của ánh xạ đa tuyến tính chính tắc

t $= t_q$ : $L^{(q)} \rightarrow T^q(L)$,

$t(\alpha_1$, ..., $\alpha_q) = \alpha_1 \otimes \cdots \otimes \alpha_q$

và phép chiếu tuyến tính $\pi = \pi_q$ : $T^q(L) \to S^q(L)$ là ánh xạ đa tuyến tính

$\varphi = \varphi_a$ : $L^{(q)} \rightarrow S^q(L)$,

$\varphi(\alpha_1$, ..., $\alpha_q) = \pi(\alpha_1 \otimes \cdots \otimes \alpha_q)$.



Theo định nghĩa của luỹ thừa đối xứng $S^q(L)$, ánh xạ $\varphi$ có tính đối xứng.

Hơn nữa, cặp $(\varphi$, $S^q(L))$ có tính chất phổ dụng sau đây: Với mọi ánh xạ đa

tuyến tính đối xứng $\psi: L^{(q)} \to$ M trong đó M là một K-không gian vécto bất kỳ,

tồn tại duy nhất một ánh xạ tuyến tính h: $S^q(L) \to$ M làm giao hoán biểu đồ

$L^{(q)} \longleftrightarrow S^{q}(L) \downarrow \downarrow \downarrow$

M,

tức là $\psi =$ h $\circ \varphi$.

Dễ kiểm tra lại rằng A $= \bigoplus_{q=0}^{\infty} A_q$ là một iđêan của đại số $T^*(L) = \bigoplus_{q=0}^{\infty} T^q(L)$.

Do $\mathrm{d}\acute{o}$,

S(L) $:= T^*(L)/A = \bigoplus_{q=0}^{\infty} T^q(L)/A_q = \bigoplus_{q=0}^{\infty} S^q(L)$

là một đại số trên K.

### Định nghĩa 4.3 S(L) được gọi là đại số đối xứng của không gian vécto L.

Tích của hai phần tử x $\in S^q(L)$ và y $\in S^r(L)$ được ký hiệu bởi x $\cdot$ y, hoặc đơn

giản bởi xy $\in S^{q+r}(L)$.

Mệnh đề 4.4

$\varphi(\alpha_1$, ..., $\alpha_q) \cdot \varphi(\alpha_{q+1}$, ..., $\alpha_{q+r}) = \varphi(\alpha_1$, ..., $\alpha_q$, $\alpha_{q+1}$, ..., $\alpha_{q+r})$,

với mọi $\alpha_1$, ..., $\alpha_q$, $\alpha_{q+1}$, ..., $\alpha_{q+r} \in$ L.

Chứng minh: Goi $\times$ : $L^{(q)} \times L^{(r)} \rightarrow L^{(q+r)}$ là ánh xa tư nhiên

$\times ((\alpha_1$, ..., $\alpha_q)$, $(\alpha_{q+1}$, ..., $\alpha_{q+r})) = (\alpha_1$, ..., $\alpha_q$, $\alpha_{q+1}$, ..., $\alpha_{q+r})$.

Ta có biểu đồ giao hoán sau đây:



$L^{(q)} \times L^{(r)} \longrightarrow L^{(q+r)}t_q \times t_r \downarrow t_{q+r}$

$T^q(L) \times T^r(L) \xrightarrow{\otimes} T^{q+r}(L)$

$\pi_q \times \pi_r \Bigg\vert_{\pi_{q+r}}$

$S^q(L) \times S^r(L) \longrightarrow S^{q+r}(L)$,

trong đó $"\otimes"$ là tích của đại số $T^*(L)$, "·" là tích của đại số S(L). Như thế

$\cdot (\pi_q \times \pi_r)(t_q \times t_r) = \pi_{q+r} t_{q+r} \times$.

Một mặt, ta có

$\cdot (\pi_a \times \pi_r)(t_a \times t_r)((\alpha_1$, ..., $\alpha_a)$, $(\alpha_{a+1}$, ..., $\alpha_{a+r}))$

$= \cdot(\pi_a \times \pi_r)(\alpha_1 \otimes \cdots \otimes \alpha_q$, $\alpha_{q+1} \otimes \cdots \otimes \alpha_{q+r})$

$= \cdot(\varphi(\alpha_1$, ..., $\alpha_q)$, $\varphi(\alpha_{q+1}$, ..., $\alpha_{q+r}))$

$= \varphi(\alpha_1$, ..., $\alpha_q) \cdot \varphi(\alpha_{q+1}$, ..., $\alpha_{q+r})$.

Mặt khác

$\pi_{q+r} t_{q+r} \times ((\alpha_1$, ..., $\alpha_q)$, $\ (\alpha_{q+1}$, ..., $\alpha_{q+r}))$

$= \pi_{q+r} t_{q+r}(\alpha_1$, ..., $\alpha_q$, $\alpha_{q+1}$, ..., $\alpha_{q+r})$

$= \pi_{q+r}(\alpha_1 \otimes \cdots \otimes \alpha_q \otimes \alpha_{q+1} \otimes \cdots \otimes \alpha_{q+r})$

$= \varphi(\alpha_1$, ..., $\alpha_q$, $\alpha_{q+1}$, ..., $\alpha_{q+r})$.

Mệnh đề được chứng minh.

$\Box$

Hệ quả 4.5

$\varphi(\alpha_1$, ..., $\alpha_q) := \pi(\alpha_1 \otimes \cdots \otimes \alpha_q) = \alpha_1 \cdots \alpha_q$,

$v\acute{o}i$ mọi $\alpha_1$, ..., $\alpha_q \in$ L.

Chứng minh: Hệ quả được chứng minh bằng quy nạp theo q.



Với q $=$ 1, đẳng thức $\varphi(\alpha_1) := \pi(\alpha_1) = \alpha_1$ được suy trực tiếp từ định nghĩa

của $\varphi$. Giả sử hệ quả đã được chứng minh cho q-1. Theo mệnh đề trên ta có

$\varphi(\alpha_1$, ..., $\alpha_q) = \varphi(\alpha_1$, ..., $\alpha_{q-1}) \cdot \varphi(\alpha_q)$

$= (\alpha_1 \cdots \alpha_{q-1}) \cdot \alpha_q$

$= \alpha_1 \cdots \alpha_q$.

Như vây, hê quả cũng đúng đối với q.

$\Box$

Mệnh đề 4.6 xy $=$ yx với mọi x $\in$ Sq(L), y $\in$ Sr(L).

Chứng minh: Trước hết xét trường hợp x $= \alpha \in S^1(L) =$ L, y $= \beta \in S^1(L) =$ L.

Theo định nghĩa, $\alpha \otimes \beta$ - $\beta \otimes \alpha \in A_2$. Do đó

$\alpha\beta$ - $\beta\alpha = \varphi((\alpha,\beta)$ - $(\beta,\alpha)) = \pi t((\alpha,\beta)$ - $(\beta,\alpha))$

$= \pi(\alpha \otimes \beta$ - $\beta \otimes \alpha) =$ 0 $\in S^2(L)$.

Để chứng minh xy $=$ yx ta chỉ cần chứng tỏ rằng

$(\alpha_1 \cdots \alpha_n)(\beta_1 \cdots \beta_r) = (\beta_1 \cdots \beta_r)(\alpha_1 \cdots \alpha_n)$,

với mọi $\alpha_1$, ..., $\alpha_q$, $\beta_1$, ..., $\beta_r \in$ L. Theo Mệnh đề 4.4 và phần đầu của chứng minh

mệnh đề này, ta có thể tráo đổi thứ tự từng $\alpha_i$ với từng $\beta_i$ mà tích không thay

đổi. Mệnh đề được chứng minh.

$\Box$

### Dịnh lý 4.7 Giả sử (e_1,...,e_n) là một cơ sở của K-không gian vécto L. Khi đó hệ

véctor sau đây lập nên một cơ sở của không gian véctor S(L):

$(e_1^{i_1} \cdots e_n^{i_n}$ : $i_1$, ..., $i_n \geq$ 0).

Hơn nữa, đại số S(L) đẳng cấu với đại số đa thức trên n phần tử $e_1,...,e_n$, nghĩa

$l\hat{a}$ S(L) $\cong \mathbf{K}[e_1$, ..., $e_n]$.



Chứng minh: Gọi $\mathbf{K}[X_1$, ..., $X_n]$ là đại số đa thức của n ẩn, và $(\mathbf{K}[X_1$, ..., $X_n])_q$

là không gian con các đa thức thuần nhất bậc q. Ta xét ánh xạ đa tuyến tính

$\eta: L^{(q)} \to (\mathbf{K}[X_1$, ..., $X_n])_q$ xác định bởi hệ thức $\eta(e_{j_1}$, ..., $e_{j_q}) = X_{j_1} \cdots X_{j_q}$. Vì đại

số $\mathbf{K}[X_1$, ..., $X_n]$ giao hoán, nên $\eta$ đối xứng. Do tính phổ dụng của $S^{(q)}$, tồn tại ánh

xạ tuyến tính $h_q: S^{(q)} \to (\mathbf{K}[X_1$, ..., $X_n])_q$ sao cho

$h_q(e_{j_1}\cdots e_{j_q})=X_{j_1}\cdots X_{j_q}$.

Vì các đại sốS(L)và $\mathbf{K}[X_1,...,X_n]đều$ giao hoán, nên hệ thức trên có thể viết lại

thành

$h_q(e_1^{i_1}\cdots e_n^{i_n})=X_1^{i_1}\cdots X_n^{i_n}$,

trong đó $i_1$ + $\cdots$ + $i_n =$ q.

$h_q$ là một toàn cấu, bởi vì theo công thức trên mọi đơn thức bậc q của các

biến $X_1$, ..., $X_n$ đều thuộc ảnh của $h_q$. Mặt khác, theo Hệ quả 2.5 và Mệnh đề 4.6,

không gian $S^{(q)}(L)$ được sinh bởi hệ vécto $(e_1^{i_1} \cdots e_n^{i_n}$ : $i_1$ + $\cdots$ + $i_n =$ q). Do đó,

dim $S^{(q)}(L) \leq \dim(\mathbf{K}[X_1$, ..., $X_n])_q$. Vì thế, toàn cấu $h_q$ là một đẳng cấu.

Hệ quả là h $= \bigoplus h_q$ : S(L) $\to \mathbf{K}[X_1$, ..., $X_n]$ cũng là một đẳng cấu tuyến tính.

Từ Mệnh đề 4.4 suy ra rằng h(xy) $=$ h(x)h(y). Vậy h là một đẳng cấu đại số.

Dinh lý được chứng minh.

$\Box$

Mỗi ánh xạ tuyến tínhf: L $\rightarrow$ Mcảm sinh một đồng cấu đại sốS(f): S(L) $\rightarrow$

S(M). Đó là tổng trực tiếp của các đồng cấu thành phần $S^q(f)$ : $S^q(L) \to S^q(M)$,

(0 $\leq$ q $< \infty)$, được định nghĩa như sau. Xét ánh xạ đa tuyến tính đối xứng

$\tilde{S}^q(f)$ : $L^{(q)} \rightarrow S^q(M)$,

$\tilde{S}^q(f)(\alpha_1$, ..., $\alpha_q) = f(\alpha_1) \cdots f(\alpha_q)$.

Do tính phổ dụng $củaS^q(L),tồn$ tại duy nhất ánh xạ tuyến $tínhS^q(f)$ : $S^q(L) \rightarrow$

$S^q(M)$ sao cho $\tilde{S}^q(f) = S^q(f) \circ \varphi$, trong đó $\varphi$ : $L^{(q)} \to S^q(L)$ là ánh xạ đa tuyến

tính đối xứng chính tắc. Ta thu được biểu thức tường minh cho Sq(f):

$S^q(f)(\alpha_1\cdots\alpha_q) = S^q(f)(\varphi(\alpha_1,\ldots,\alpha_q)) = \tilde{S}^q(f)(\alpha_1,\ldots,\alpha_q)$



$= f(\alpha_1) \cdots f(\alpha_q)$,

với mọi $\alpha_1$, ..., $\alpha_q \in$ L.

Dễ dàng kiểm tra lại rằng S(gf) $=$ S(g)S(f), với mọi cặp ánh xạ tuyến tính

f: L $\to$ M, g: M $\to$ N. Hon nữa $S(id_L) = id_{S(L)}$.

Nhận xét 4.8 Nếu $Char(\mathbf{K}) =$ 0, người ta có một cách khác để định nghĩa luỹ

thừa đối xứng $S^q(L)$ như sau.

Toán tử đối xứng hoá

S: $T^q(L) \to T^q(L)$

là ánh xạ tuyến tính được định nghĩa bởi hệ thức

$S(\alpha_1 \otimes \cdots \otimes \alpha_q) := \frac{1}{q!} \sum_{\sigma \in S_q} \alpha_{\sigma(1)} \otimes \cdots \otimes \alpha_{\sigma(q)}$.

Vì Char(K) $=$ 0 cho nên q! khả nghịch trong trường K, với mọi q $\in \mathbb{N}$. Dễ dàng

chứng minh rằng $S^2 =$ S. Xét không gian ảnh của toán tử thay phiên hoá

$\tilde{S}^q(L) := \text{Im}(S) \subset T^q(L)$.

Như vậy, x $\in T^q(L)$ là một phần tử của $\tilde{S}^q(L)$ nếu và chỉ nếu x $=$ S(x).

Người ta chứng minh được rằng, nếu Char(K) $=$ 0 thì phép hợp thành

$\tilde{S}^q(L) \subset T^q(L) \stackrel{\pi}{\rightarrow} S^q(L) = T^q(L)/A_q$

là một đẳng cấu tuyến tính. Đẳng cấu này chuyển $S(\alpha_1 \otimes \cdots \otimes \alpha_q)$ thành $\alpha_1 \cdots \alpha_q$.

Do đó, trong những lĩnh vực mà trường K luôn luôn là trường số thực hoặc

trường số phức, người ta thường dùng định nghĩa sau đây:

$S^q(L) := \text{Im}(S) \subset T^q(L)$,

$\alpha_1 \cdots \alpha_q \ := \ S(\alpha_1 \otimes \cdots \otimes \alpha_q)$.



Dại số ngoài

$5<sup>5</sup>$

Cũng giống như ở tiết trước, trong các cách định nghĩa khác nhau của khái niệm

lũy thừa ngoài và đại số ngoài, chúng ta chọn cách không phụ thuộc vào đặc số của

trường K.

Gọi $B_q$ là không gian véctor con của $T^q(L)$ sinh bởi các phần tử có dạng $\alpha_1 \otimes$

$\cdots \otimes \alpha_q$ trong đó $\alpha_i = \alpha_j$ với các chỉ số i $\neq$ j nào đó.

Dinh nghĩa 5.1 Không gian thương

$\Lambda^{q}(L) := T^{q}(L)/B_{q}$

được gọi là luỹ thừa ngoài bậc q của L.

### Định nghĩa 5.2 Giả sử M là một K-không gian vécto. Ánh xạ đa tuyến tính

$\eta: L^{(q)} \to$ M được gọi là thay phiên nếu

$\eta(\alpha_1,...,\alpha_q)=0$,

với mọi $\alpha_1$, ..., $\alpha_q \in$ L trong đó $\alpha_i = \alpha_j$ với các chỉ số i $\neq$ j nào đó.

Hợp thành của ánh xạ đa tuyến tính chính tắc

t $= t_q$ : $L^{(q)} \rightarrow T^q(L)$,

$t(\alpha_1$, ..., $\alpha_q) = \alpha_1 \otimes \cdots \otimes \alpha_q$

và phép chiếu tuyến tính $\pi = \pi_q$ : $T^q(L) \to \Lambda^q(L)$ là ánh xạ đa tuyến tính

$\xi = \xi_q$ : $L^{(q)} \rightarrow \Lambda^q(L)$,

$\xi(\alpha_1$, ..., $\alpha_q) = \pi(\alpha_1 \otimes \cdots \otimes \alpha_q)$.

Theo định nghĩa của luỹ thừa ngoài, $\xi$ là một ánh xạ thay phiên.

Hơn nữa, cặp $(\xi$, $\Lambda^q(L))$ có tính phổ dụng sau đây: Với mọi ánh xạ đa tuyến

tính thay phiên $\eta: L^{(q)} \to$ M, trong đó M là một K-không gian vécto bất kỳ, tồn

tại duy nhất một ánh xạ tuyến tính h: $\Lambda^{q}(L) \to$ M làm giao hoán biểu đồ



$\frac{\xi}{\frac{1}{\xi}}$

$\Lambda^{q}(L)$

$L^{(q)}$

h

M,

tức là $\eta =$ h $\circ \xi$.

Dễ thấy rằng B $= \bigoplus_{q=0}^{\infty} B_q$ là một iđêan của đại số $T^*(L)$. Do đó

$\Lambda(L) := T^*(L)/B = \bigoplus_{q=0}^{\infty} T^q(L)/B_q = \bigoplus_{q=0}^{\infty} \Lambda^q(L)$

là một đại số trên K.

### Định nghĩa 5.3 \Lambda(L) được gọi là đại số ngoài của không gian vécto L.

Tích trong $\Lambda(L)$ của $\omega \in \Lambda^{q}(L)$ và $\eta \in \Lambda^{r}(L)$ được ký hiệu là $\omega \wedge \eta \in \Lambda^{q+r}(L)$,

và được gọi là tích ngoài của $\omega$ và $\eta$.

Mệnh đề 5.4

$\xi(\alpha_1$, ..., $\alpha_q) \wedge \xi(\alpha_{q+1}$, ..., $\alpha_{q+r}) = \xi(\alpha_1$, ..., $\alpha_q$, $\alpha_{q+1}$, ..., $\alpha_{q+r})$,

với mọi $\alpha_1$, ..., $\alpha_q$, $\alpha_{q+1}$, ..., $\alpha_{q+r} \in$ L.

Chứng minh: Gọi $\wedge$ : $\Lambda^{q}(L) \times \Lambda^{r}(L) \to \Lambda^{q+r}(L)$ là (hạn chế của) tích trong đại

số $\Lambda(L)$. Ta có biểu đồ giao hoán

$L^{(q)} \times L^{(r)} \longrightarrow L^{(q+r)}$

$t_{q}\times t_{r} \text{ } \Bigg| \text{ } \Bigg| \text{ } t_{q+r}$

$T^q(L) \times T^r(L) \xrightarrow{\otimes} T^{q+r}(L)$

$\pi_q \times \pi_r$

$\Lambda^{q}(L) \times \Lambda^{r}(L) \longrightarrow \Lambda^{q+r}(L)$,



Từ đó

$\wedge (\pi_a \times \pi_r)(t_a \times t_r) = \pi_{a+r} t_{a+r} \times$.

Một mặt, ta có

$\wedge (\pi_a \times \pi_r)(t_a \times t_r)((\alpha_1$, ..., $\alpha_a)$, $(\alpha_{a+1}$, ..., $\alpha_{a+r}))$

$= \wedge (\pi_a \times \pi_r)(\alpha_1 \otimes \cdots \otimes \alpha_q$, $\alpha_{q+1} \otimes \cdots \otimes \alpha_{q+r})$

$= \wedge (\xi(\alpha_1$, ..., $\alpha_q)$, $\xi(\alpha_{q+1}$, ..., $\alpha_{q+r}))$

$= \xi(\alpha_1$, ..., $\alpha_q) \wedge \xi(\alpha_{q+1}$, ..., $\alpha_{q+r})$.

Mặt khác

$\pi_{a+r} t_{a+r} \times ((\alpha_1$, ..., $\alpha_q)$, $\ (\alpha_{a+1}$, ..., $\alpha_{q+r}))$

$= \pi_{q+r} t_{q+r}(\alpha_1$, ..., $\alpha_q$, $\alpha_{q+1}$, ..., $\alpha_{q+r})$

$= \pi_{q+r}(\alpha_1 \otimes \cdots \otimes \alpha_q \otimes \alpha_{q+1} \otimes \cdots \otimes \alpha_{q+r})$

$= \xi(\alpha_1$, ..., $\alpha_q$, $\alpha_{q+1}$, ..., $\alpha_{q+r})$.

Mệnh đề được chứng minh.

$\Box$

Hệ quả 5.5

$\xi(\alpha_1$, ..., $\alpha_q) := \pi(\alpha_1 \otimes \cdots \otimes \alpha_q) = \alpha_1 \wedge \cdots \wedge \alpha_q$,

với mọi $\alpha_1$, ..., $\alpha_q \in$ L.

Chứng minh: Hệ quả được chứng minh bằng quy nạp theo q.

Với q $=$ 1, đẳng thức $\xi(\alpha_1) := \pi(\alpha_1) = \alpha_1$ được suy trực tiếp từ định nghĩa của

$\xi.Giả$ sử hệ quả đã được chứng minh $cho<br/>$ q-1. Theo mệnh đề trên ta có

$\xi(\alpha_1$, ..., $\alpha_q) = \xi(\alpha_1$, ..., $\alpha_{q-1}) \wedge \xi(\alpha_q)$

$= (\alpha_1 \wedge \cdots \wedge \alpha_{q-1}) \wedge \alpha_q$

$= \alpha_1 \wedge \cdots \wedge \alpha_q$.

Như thế, hệ quả cũng đúng đối với q.

$\Box$



Mệnh đề 5.6 $\omega \wedge \eta = (-1)^{qr} \eta \wedge \omega$ với mọi $\omega \in \Lambda^{q}(L)$, $\eta \in \Lambda^{r}(L)$.

Chứng minh: Trước hết xét trường hợp $\omega = \alpha \in \Lambda^1(L) =$ L, $\eta = \beta \in \Lambda^1(L) =$ L.

Ta sẽ chứng minh rằng

$\alpha \wedge \beta = -\beta \wedge \alpha$,

Thật vậy, theo định nghĩa của $\Lambda^2(L)$ ta có $\alpha \wedge \alpha = \beta \wedge \beta =$ 0. Do đó

0 $= (\alpha$ + $\beta) \wedge (\alpha$ + $\beta) = \alpha \wedge \alpha$ + $\alpha \wedge \beta$ + $\beta \wedge \alpha$ + $\beta \wedge \beta$

$= \alpha \wedge \beta$ + $\beta \wedge \alpha$.

Để chứng minh $\omega \wedge \eta = (-1)^{qr} \eta \wedge \omega$ ta chỉ cần chứng tỏ rằng

$(\alpha_1 \wedge \cdots \wedge \alpha_n) \wedge (\beta_1 \wedge \cdots \wedge \beta_r) = (-1)^{qr} (\beta_1 \wedge \cdots \wedge \beta_r) \wedge (\alpha_1 \wedge \cdots \wedge \alpha_q)$,

với mọi $\alpha_1$, ..., $\alpha_q$, $\beta_1$, ..., $\beta_r \in$ L. Theo Mệnh đề 5.4 và phần đầu của chứng minh

mệnh đề này, mỗi lần tráo đổi thứ tự từng $\alpha_i$ với từng $\beta_i$ đứng sát nó thì tích ngoài

đổi dấu. Để biến đổi $\alpha_1 \wedge \cdots \wedge \alpha_q \wedge \beta_1 \wedge \cdots \wedge \beta_r$ thành $\beta_1 \wedge \cdots \wedge \beta_r \wedge \alpha_1 \wedge \cdots \wedge \alpha_q$

ta cần thực hiện qr lần tráo đổi như thế. Mệnh đề được chứng minh.

$\Box$

Một hệ quả hiển nhiên của mệnh đề trên là

$\alpha_{\sigma(1)} \wedge \cdots \wedge \alpha_{\sigma(q)} = \text{sgn}(\sigma) \alpha_1 \wedge \cdots \wedge \alpha_q$,

với mọi $\alpha_1$, ..., $\alpha_q \in$ L, $\sigma \in S_q$. Trên cơ sở đó, ta có định lý sau đây.

Dinh lý 5.7 (i) $\Lambda^{q}(L) =$ 0 với mọi q $>$ n $= \dim_{K}$ L.

(ii) Giả sử $(e_1,...,e_n)$ là một cơ sở của không gian véctơ L. Khi đó, với 0 $\leq$ q $\leq$ n,

hệ véctơ sau đây lập thành một cơ sở của không gian véctơ $\Lambda^{q}(L):$

$(e_{i_1} \wedge \cdots \wedge e_{i_q}$ : 1 $\leq i_1 < \cdots < i_q \leq$ n).

$ Nói riêng, \dim_K \Lambda^q(L) = \begin{pmatrix} n \\ q \end{pmatrix}. $



Chứng minh: Do tính đa tuyến tính của tích $\wedge$, không gian vécto $\Lambda^{q}(L)$ được

sinh bởi các vécto $e_{i_1} \wedge \cdots \wedge e_{i_q}$, với 1 $\leq i_1$, ..., $i_q \leq$ n.

(i) Nếu q $>$ n thì trong mỗi phần tử như vậy có ít nhất hai chỉ số nào đó bằng

nhau: $i_s = i_t$ với s $\neq$ t. Vì thế, tất cả các phần tử nói trên đều bằng 0. Do đó

$\Lambda^{q}(L)=0$.

(ii) Nếu q $=$ n, theo lý thuyết định thức, có duy nhất một ánh xạ đa tuyến tính,

thay phiên det : $L^{(q)} \to \mathbf{K}$ sao cho $det(e_1$, ..., $e_n) =$ 1. Do đó, tồn tại duy nhất ánh

xạ tuyến tính

$\overline{\det}: \Lambda^q(L) \longrightarrow \mathbf{K}$

sao cho $\overline{\det}(e_1 \wedge \cdots \wedge e_n) =$ 1. Từ đó suy ra hệ chỉ gồm một vécto $e_1 \wedge \cdots \wedge e_n$ là

một cở sở của không gian véctor $\Lambda^{q}(L)$. Như thế dim $\Lambda^{q}(L) =$ 1.

Bây giờ xét trường hợp 1 $\le$ q $\le$ n. Giả sử có một ràng buộc tuyến tính

$\sum_{(i)} a_{(i)} e_{i_1} \wedge \cdots \wedge e_{i_q} =$ 0,

trong đó (i) $= (i_1$, ..., $i_q)$, 1 $\leq i_1 < \cdots < i_q \leq$ n, $a_{(i)} \in \mathbf{K}$. Với mỗi bộ chỉ

số cố định (j) $= (j_1$, ..., $j_q)$ thoã mãn $j_1 < \cdots < j_q$, ta chọn $j_{q+1}$, ..., $j_n$ sao cho

$(j_1$, ..., $j_q$, $j_{q+1}$, ..., $j_n)$ là một hoán vị nào đó của (1, 2, ..., n). Nhân ngoài hai vế của

đẳng thức trên với $e_{j_{q+1}} \wedge \cdots \wedge e_{j_n}$ ta thu được một tổng với hầu hết các số hạng

$e_{i_1} \wedge \cdots \wedge e_{i_q} \wedge e_{j_{q+1}} \wedge \cdots \wedge e_{j_n}$ bằng 0, vì có các chỉ số trùng lặp, loại trừ một số

hạng duy nhất với các chỉ số không trùng lặp

$a_{(j)}e_{j_1}\wedge\cdots\wedge e_{j_q}\wedge e_{j_{q+1}}\wedge\cdots\wedge e_{j_n}=0$.

Hay là $\pm a_{(i)}e_1 \wedge \cdots \wedge e_n =$ 0. Do đó $a_{(i)} =$ 0.

Như vậy, hệ vécto $(e_{i_1} \wedge \cdots \wedge e_{i_q}$ : 1 $\leq i_1 < \cdots < i_q \leq$ n) độc lập tuyến tính

trong $\Lambda^{q}(L)$. Định lý được chứng minh.

$\Box$

Mỗi ánh xạ tuyến tínhf: L $\to$ Mcảm sinh một đồng cấu đại $số\Lambda(f): \Lambda(L) \to$

$\Lambda(M)$. Đó là tổng trực tiếp của các đồng cấu thành phần $\Lambda^q(f):\Lambda^q(L)\to\Lambda^q(M)$,



$(0\leq q<\infty)$, được định nghĩa như sau. Xét ánh xạ đa tuyến tính thay phiên

$\tilde{\Lambda}^q(f)$ : $L^{(q)} \rightarrow \Lambda^q(M)$,

$\tilde{\Lambda}^q(f)(\alpha_1,...,\alpha_q) = f(\alpha_1) \wedge \cdots \wedge f(\alpha_q)$.

Do tính phổ dụng của $\Lambda^{q}(L)$, tồn tại duy nhất ánh xạ tuyến tính $\Lambda^{q}(f)$ : $\Lambda^{q}(L) \to$

$\Lambda^{q}(M)$ sao cho $\tilde{\Lambda}^{q}(f) = \Lambda^{q}(f) \circ \xi$, trong đó $\xi$ : $L^{(q)} \to \Lambda^{q}(L)$ là ánh xạ đa tuyến

tính thay phiên chính tắc. Ta thu được biểu thức tường minh cho $\Lambda^{q}(f):$

$\Lambda^{q}(f)(\alpha_{1} \wedge \cdots \wedge \alpha_{q}) = \Lambda^{q}(f)(\xi(\alpha_{1},...,\alpha_{q}))$

$= \tilde{\Lambda}^q(f)(\alpha_1,...,\alpha_q)$

$= f(\alpha_1) \wedge \cdots \wedge f(\alpha_q)$,

với mọi $\alpha_1$, ..., $\alpha_q \in$ L.

Dễ kiểm tra lại rằng $\Lambda(gf) = \Lambda(g)\Lambda(f)$, với mọi cặp ánh xạ tuyến tính f: L $\to$

M, g: M $\to$ N. Hon nữa $\Lambda(id_L) = id_{\Lambda(L)}$.

Nhận xét 5.8 Nếu $Char(\mathbf{K}) =$ 0, người ta có một cách khác để định nghĩa luỹ

thừa ngoài $\Lambda^{q}(L)$ như trình bày dưới đây. Cách này thường được các nhà giải tích

và hình học vi phân wa dùng.

Toán tử thay phiên hoá

Alt : $T^q(L) \to T^q(L)$

là ánh xạ tuyến tính được định nghĩa bởi hệ thức

$\mathrm{Alt}(\alpha_1 \otimes \cdots \otimes \alpha_q) := \frac{1}{q!} \sum_{\sigma \in S_q} (\mathrm{sgn} \sigma) \alpha_{\sigma(1)} \otimes \cdots \otimes \alpha_{\sigma(q)}$.

Diều kiện Char(K) $=$ 0 đảm bảo cho q! khả nghịch trong trường K. Dễ dàng thử

lai rằng $Alt^2 =$ Alt. Xét không gian ảnh của toán tử thay phiên hoá

$\tilde{\Lambda}^q(L) := \text{Im}(\text{Alt}) \subset T^q(L)$.



Như thế, $\omega \in T^q(L)$ là một phần tử của $\tilde{\Lambda}^q(L)$ nếu và chỉ nếu $\omega = \text{Alt}(\omega)$.

Người ta chứng minh được rằng, nếu Char(K) $=$ 0 thì phép hợp thành

$\tilde{\Lambda}^q(L) \subset T^q(L) \stackrel{\pi}{\rightarrow} \Lambda^q(L) = T^q(L)/B_q$

là một đẳng cấu tuyến tính. Đẳng cấu này chuyển $\mathrm{Alt}(\alpha_1 \otimes \cdots \otimes \alpha_q)$ thành $\alpha_1 \wedge \cdots$

$\cdots \wedge \alpha_q$.

Vì thế, trong Giải tích hoặc Hình học vi phân (là lĩnh vực mà trường $\bf{K}$ luôn

luôn là $\bf{R}$ hoặc $\bf{C})$, người ta thường dùng định nghĩa sau đây:

$\Lambda^{q}(L) := \text{Im}(\text{Alt}) \subset T^{q}(L)$,

$\alpha_1 \wedge \cdots \wedge \alpha_q := \text{Alt}(\alpha_1 \otimes \cdots \otimes \alpha_q)$.

### Định nghĩa 5.9 Gọi L<sup>*</sup> là không gian đối ngẫu của L. Khi đó mỗi phần tử của

$\Lambda^{q}(L^{*})$ được gọi là một q-dạng (ngoài) trên L.

Mệnh đề sau đây giải thích cấu trúc của không gian các q-dạng ngoài.

Mệnh đề 5.10 Nếu L là một K-không gian vécto hữu hạn chiều thì

$\Lambda^{q}(L^{*}) \cong \Lambda^{q}(L)^{*}$,

trong đó về phải là không gian đối ngẫu của $\Lambda^{q}(L)$.

Chứng minh: Nhận xét rằng ánh xạ

$L^q \times (L^*)^q \rightarrow \mathbf{K}$

$((\alpha_1$, ..., $\alpha_q)$, $(\varphi_1$, ..., $\varphi_q) \mapsto \det(\langle \alpha_i$, $\varphi_i \rangle)$

là đa tuyến tính thay phiên đối với các biến $\alpha_1$, ..., $\alpha_q$, đồng thời cũng đa tuyến

tính thay phiên đối với các biến $\varphi_1$, ..., $\varphi_q$. (Ó đây $\langle \alpha_i$, $\varphi_j \rangle$ là giá trị của $\varphi_j$ trên

véctor $\alpha_i.)$ Vì thế, nó cảm sinh ánh xạ song tuyến tính

$\Lambda^{q}(L) \times \Lambda^{q}(L^{*}) \rightarrow \mathbf{K}$

$(\alpha_1 \wedge \cdots \wedge \alpha_q$, $\varphi_1 \wedge \cdots \wedge \varphi_q) \mapsto \det(\langle \alpha_i$, $\varphi_i \rangle)$.



Anh xạ này cho phép xem mỗi phần tử của $\Lambda^{q}(L^{*})$ như một dạng tuyến tính trên

$\Lambda^{q}(L)$, tức là như một phần tử của $\Lambda^{q}(L)^{*}$.

Gọi $e_1$, ..., $e_n$ là một cơ sở của L và $e^1$, ..., $e^n$ là cơ sở đối ngẫu của $L<sup>*</sup>$. Sử dụng

phép đồng nhất nói trên ta thấy cơ sở $(e^{j_1} \wedge \cdots \wedge e^{j_q}$ | $j_1 < \cdots < j_q)$ chính là đối

ngẫu của cơ sở $(e_{i_1} \wedge \cdots \wedge e_{i_q}$ | $i_1 < \cdots < i_q)$. Thật vậy,

$(e_{i_1} \wedge \cdots \wedge e_{i_q}$, $e^{j_1} \wedge \cdots \wedge e^{j_q}) \mapsto \det(\langle e_{i_k}$, $e^{j_\ell} \rangle)$.

Vế phải bằng 1 khi và chỉ khi $i_1 = j_1$, ..., $i_q = j_q$ và bằng 0 trong các trường hợp

khác. Như thế $\Lambda^{q}(L^{*}) \cong \Lambda^{q}(L)^{*}$.

$\Box$

Ví dụ 5.11 Xét không gian vécto thực L $= \mathbb{R}^n$ với cơ sở chính tắc $(e_1$, ..., $e_n):$

$ \left\{ \begin{array}{rcl} e_1 &=& (1,0,...,0)^t, \\[1mm] e_2 &=& (0,1,...,0)^t, \\[1mm] \ddots & \dots & \dots \\[1mm] e_n &=& (0,0,...,1)^t. \end{array} \right. $

$\sim \sim \sim \sim$

Gọi $(dx^1$, ..., $dx^n)$ là cơ sở đối ngẫu của $(\mathbf{R}^n)^*$ được xác định bởi hệ điều kiện sau

$dx^{i}(e_{j}) = \delta^{i}_{j}$, $\$ (1 $\leq$ i, j $\leq$ n).

(Cách ký hiệu này có cơ sở từ Lý thuyết vi phân của hàm nhiều biến.)

Ta xét không gian $\Lambda^{q}(\mathbf{R}^{n*}) \cong \Lambda^{q}(\mathbf{R}^{n})^*$ các q-dạng trên $\mathbf{R}^{n}$. Nó có một cơ sở là

hệ vécto sau đây

$(dx^{i_1} \wedge \cdots \wedge dx^{i_q}$ | 1 $\leq i_1 < \ldots < i_q \leq$ n).

Mỗi vécto $\omega \in \Lambda^q(\mathbf{R}^{n*})$ có biểu thị tuyến tính duy nhất qua cơ sở đó:

$\omega = \sum a_{i_1,\dots,i_q} dx^{i_1} \wedge \dots \wedge dx^{i_q}$,

1 $\leq i_1 <$ ... $< i_q \leq$ n

$\dot{\sigma}$ đây $a_{i_1,...,i_q} \in \mathbf{R}$.

Trường hợp đặc biệt khi q $=$ n, không gian $\Lambda^n(\mathbf{R}^{n*})$ có số chiều bằng 1, với cơ

sở gồm phần tử duy nhất

$dx^1 \wedge dx^2 \wedge \cdots \wedge dx^n$.



Theo đẳng cấu chính tắc $\Lambda^n(\mathbf{R}^{n*}) \cong \Lambda^n(\mathbf{R}^n)^*$ nêu trong chứng minh Mệnh đề 5.10,

n-dạng $dx^1 \wedge \cdots \wedge dx^n$ được đồng nhất với ánh xạ tuyến tính $\Lambda^n(\mathbf{R}^n) \to \mathbf{R}$ xác

định bởi điều kiện chuẩn hoá

$(dx^1 \wedge \cdots \wedge dx^n)(e_1 \wedge \cdots \wedge e_n) = \det(dx^j(e_i)) =$ 1.

Ta định nghĩa ánh xạ đa tuyến tính thay phiên duy nhất $(\mathbf{R}^n)^{(n)} \to \mathbf{R}$, cũng được

ký hiệu là $dx^1 \wedge \cdots \wedge dx^n$, bằng công thức sau đây

$(dx^1 \wedge \cdots \wedge dx^n)(\alpha_1$, ..., $\alpha_n) = (dx^1 \wedge \cdots \wedge dx^n)(\alpha_1 \wedge \cdots \wedge \alpha_n)$.

Theo lý thuyết định thức

$dx^1 \wedge \cdots \wedge dx^n = \det$.

Thật vậy, cả hai vế đều là ánh xạ đa tuyến tính thay phiên duy nhất $(\mathbf{R}^n)^{(n)} \to \mathbf{R}$

thoả mãn điều kiện chuẩn hoá.

Do tính đa tuyến tính thay phiên, mỗi phần tử $\omega \in \Lambda^n(\mathbf{R}^n)^*$ có thể xem như

một thước đo thể tích định hướng n chiều trên $\mathbf{R}^n$ mà giá trị $\omega(\alpha_1 \wedge \cdots \wedge \alpha_n)$ là

thể tích của hình hộp n chiều có hướng tựa trên các vécto $\alpha_1$, ..., $\alpha_n$.

Giả sử U là một tập mở trong $\mathbb{R}^n$. Mỗi hàm khả vi vô hạn từ U vào $\Lambda^q(\mathbb{R}^n)^*$

được gọi là một q-dạng vi phân trên U. Như thế, mỗi q-dạng vi phân trên U được

biểu thị duy nhất dưới dạng

$\omega(x) = \sum_{1 \leq i_1 < \ldots < i_q \leq n} a_{i_1,\ldots,i_q}(x) dx^{i_1} \wedge \cdots \wedge dx^{i_q}$,

trong đó $a_{i_1,\dots,i_q}(x)$ là các hàm khả vi vô hạn theo biến x $\in$ U.

Không gian các q-dạng vi phân trên U dược ký hiệu là $\Omega^{q}(U)$. Nói cách khác

$\Omega^{q}(U) = C^{\infty}(U$, $\Lambda^{q}(\mathbf{R}^{n})^{*})$.



Bài tâp

1. Chứng minh chi tiết các khẳng định về tích tenxo trong các Ví dụ 2.6, 2.7 và

## 2.8. 1. Chứng minh chi tiết các khẳng định về tích tenxo trong các Ví dụ 2.6, 2.7 và

2. Cho $e_1$, ..., $e_n$ là một cơ sở của L và $e^1$, ..., $e^n$ là cơ sở đối ngẫu của $L<sup>*</sup>$. Mỗi

tenxo kiểu (1, 1) có dạng toạ độ như sau

f $= a_i^i e^j \otimes e_i$.

Gọi A $= (a_i^i)$ là ma trận với phần tử $a_i^i$ nằm ở hàng i cột j. Hãy tìm công

thức mô tả sự thay đổi của A khi đổi cơ sở.

3. Với giả thiết như bài trên, mỗi tenxơ kiểu(2,0) có dạng toạ độ như sau

g $= g_{ij}e^i \otimes e^j$

Gọi G $= (g_{ij})$ là ma trận với phần tử $g_{ij}$ nằm ở hàng i cột j. Hãy tìm công

thức mô tả sự thay đổi của G khi đổi cơ sở.

4. Giải quyết vấn đề tương tự với bài tập trên cho các tenxơ kiểu (0,2).

5. Giả sử tenxo hai lần thuận biến g có ma trận G $= (g_{ij})$ trong cơ sở $(e^1$, ..., $e^n)$

là một ma trận khả nghịch. Xét tenxo hai lần phản biến $g^{-1}$ xác định như

sau $g^{-1} = g^{ij} e_i \otimes e_j$, trong đó $g^{ij}$ là phần tử của ma trận $G^{-1}$. Chứng minh

rằng ma trận của hai tenxo nói trên trong hai cơ sở đối ngẫu bất kỳ đều là

các ma trận nghịch đảo của nhau.

6. Cho tự đồng cấu f: L $\to$ L của K-không gian vécto hữu hạn chiều L. Hãy

diễn đạt hàmF: L $\times L^* \to \mathbf{K}xác$ định bởi công thức $F(\alpha$, $\ell) = \ell(f(\alpha))như$

một tenxo. So sánh các toạ độ của tenxo này trong một cơ sở với ma trận

của f trong cùng cơ sở ấy.

7. Tìm số chiều của tích đối xứng $S^q(L)$ biết rằng dim L $=$ n.



8. Giả sử f: L $\to$ L là một tự đồng cấu của không gian vécto n chiều L. Khi đó

$\Lambda^{n}(f): \Lambda^{n}(L) \longrightarrow \Lambda^{n}(L)$ là phép nhân với một vô hướng. Chứng minh rằng

$\Lambda^{n}(f) = \det(f)$.

9. Giả sửLlà một không gian $véct<br/>ơnchiều$ trên trường ${\bf K} và<br/> f:L\rightarrow$ Llà một

tự đồng cấu. Gọi $\alpha_r(f) =$ Tr $\Lambda^r(f)$ là vết của tự đồng cấu $\Lambda^r(f)$ : $\Lambda^r(L) \to$

$\Lambda^r(L)$ (xem bài tập 40 Chương II). Chứng minh rằng

$\det(id$ + f) $= \sum_{r \geq 0} \alpha_r(f)$.

Nói riêng, ta có $\alpha_0(f) =$ 1, $\alpha_1(f) =$ Tr(f), $\alpha_n(f) = \det(f)$, $\alpha_r(f) =$ 0 (với

r $>$ n). Hãy diễn đạt $\alpha_r(f)$ theo các hệ số của đa thức đặc trưng của f.

10. Giả sử f: L $\to$ M là một đồng cấu giữa các không gian vécto hữu hạn chiều

trên trường K. Sử dụng phép đối ngẫu trong chứng minh Mệnh đề 5.10 giữa

các không gian $\Lambda^r(L)$, $\Lambda^r(M)$ và $\Lambda^r(L^*)$, $\Lambda^r(M^*)$, hãy chứng minh rằng đồng

cấu $\Lambda^r(f^*): \Lambda^r(M^*) \to \Lambda^r(L^*)$ là đối ngẫu của đồng cấu $\Lambda^r(f): \Lambda^r(L) \to$

$\Lambda^r(M)$.

$\cap$



TÀI LIỆU THAM KHẢO

1. G. Birkhoff và S. MacLane, Tổng quan về Đại số hiện đại (Bản dịch tiếng

Việt), NXB ĐH và THCN, Hà Nội, 1979.

2. I. M. Gelfand, Bài giảng Đại số tuyến tính, NXB Nauka, Moskva, 1971 (Tiếng

Nga).

3. Nguyễn Hữu Việt Hưng, Dai số đại cương, NXB Giáo dục, Hà Nội, 1999 (tái

$b\dot{a}n)$.

4. A. I. Kostrikin và YU. I. Manin, Dai số và Hình học tuyến tính, NXB Đại học

Moskva, Moskva, 1980.

5. A. I. Kostrikin, Nhập môn đại số, NXB Nauka, Moskva, 1977 (Tiếng Nga).

6. A. G. Kurosh, Giáo trình Đại số cao cấp, NXB Nauka, Moskva, 1971 (Tiếng

Nga).

7. S. Lang, Algebra, Addison - Wesley publishing company, Massachusetts, 1965.

8. I. V. Proskuryakov, Problems in Linear Algebra, Mir publishers, Moscow, 1978.

9. Đoàn Quỳnh (chủ biên), Giáo trình Đại số tuyến tính và Hình học giải tích,

NXB Đại học Quốc gia Hà Nội, (không ghi năm xuất bản).

10. M. Spivak, Calculus on Manifolds, Benjamin Inc., New York - Amsterdam,

1965.



