CHƯƠNG

HÀM SỐ MỘT BIẾN SỐ (13LT+13BT)

§1. SƠ LƯỢC VỀ CÁC YẾU TỔ LÔGIC; CÁC TẬP SỐ:

$\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$

1. Phần Lôgic không dạy trực tiếp (phần này Đại số đã dạy) mà chỉ nhắc lại những

phép suy luận cơ bản thông qua bài giảng các nội dung khác nếu thấy cần thiết.

2. Giới thiệu các tập số; cần nói rõ tập $\mathbb{Q}$ tuy đã rộng hơn $\mathbb{Z}$ nhưng vẫn chưa lấp đầy

trục số còn tập $\mathbb{R}$ đã lấp đầy trục số và chứa tất cả các giới hạn của các dãy số hội tu,

ta có bao hàm thức

$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$.

$\S2$. TRỊ TUYỆT ĐỔI VÀ TÍNH CHẤT

Nhắc lại định nghĩa và nêu các tính chất sau

• |x| $\ge$ 0, |x| $=$ 0 $\iff$ x $=$ 0, |x + y| $\le$ |x| + |y|;

• |x-y| $\ge$ ||x|-|y||, |x| $\ge$ A $\iff$ x $\ge$ A hoặc x $\le$ -A

$\bullet \$ |x| $\leq$ B $\Longleftrightarrow$ -B $\leq$ x $\leq$ B.



CHƯƠNG

HÀM SỐ MỘT BIẾN SỐ (13LT+13BT)

§1. SƠ LƯỢC VỀ CÁC YẾU TỔ LÔGIC; CÁC TẬP SỐ:

$\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$

1. Phần Lôgic không dạy trực tiếp (phần này Đại số đã dạy) mà chỉ nhắc lại những

phép suy luận cơ bản thông qua bài giảng các nội dung khác nếu thấy cần thiết.

2. Giới thiệu các tập số; cần nói rõ tập $\mathbb{Q}$ tuy đã rộng hơn $\mathbb{Z}$ nhưng vẫn chưa lấp đầy

trục số còn tập $\mathbb{R}$ đã lấp đầy trục số và chứa tất cả các giới hạn của các dãy số hội tu,

ta có bao hàm thức

$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$.

$\S2$. TRỊ TUYỆT ĐỔI VÀ TÍNH CHẤT

Nhắc lại định nghĩa và nêu các tính chất sau

• |x| $\ge$ 0, |x| $=$ 0 $\iff$ x $=$ 0, |x + y| $\le$ |x| + |y|;

• |x-y| $\ge$ ||x|-|y||, |x| $\ge$ A $\iff$ x $\ge$ A hoặc x $\le$ -A

$\bullet \$ |x| $\leq$ B $\Longleftrightarrow$ -B $\leq$ x $\leq$ B.



$\S$ 3. $\mathbf{H} \mathbf{\hat{A}} \mathbf{M} \mathbf{S} \mathbf{\hat{O}}$

## 3.1 Đinh nghĩa hàm số <math display="block">\S 3. \mathbf{H} \mathbf{\hat{A}} \mathbf{M} \mathbf{S} \mathbf{\hat{O}}</math>

### Định nghĩa 1.1. Một hàm số đi từ tập X vào tập Y là một quy tắc cho tương ứng mỗi

phần tử x $\in$ X với một và chỉ một phần tử y $\in$ Y.

Một hàm số có thể được cho dưới dạng biểu thức giải tích y $=$ f(x), chẳng hạn như hàm số

y $= x^2$. Khi đó, cần phải xác định rõ miền xác định (hay tập xác định), tập hợp tất cả các

phần tử x $\in$ X sao cho biểu thức f(x) được xác định, của hàm số.

Tập giá trị của hàm số: là tập tất cả các phần tử y $\in$ Y sao cho tồn tại x $\in$ X, f(x) $=$ y.

Ví dụ 3.1 (Giữa kì, K61). Tìm tập xác định và tập giá trị của hàm số

a) y $= \arcsin(\cos$ 2x).

d) y $= \arccos(2 \sin$ x).

b) y $= \arcsin(2 \cos$ x).

e) y $= \sin(\pi \cos$ 3x).

f) y $= \cos(\pi \sin$ 3x).

c) y $= \arccos(\sin$ 2x).

## 3.2 Hàm số đơn điêu c) <math>y = \arccos(\sin 2x)</math>.

• Một hàm số f(x) được gọi là đơn điệu tăng trên khoảng (a, b) nếu:

$\forall x_1$, $x_2 \in$ (a, b), $x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$.

• Một hàm số f(x) được gọi là đơn điệu giảm trên khoảng (a, b) nếu

$\forall x_1$, $x_2 \in$ (a, b), $x_1 < x_2 \Rightarrow f(x_1) > f(x_2)$.

Chú ý 1.1. Trong Bài giảng này chúng ta chỉ quan tâm đến tính đơn điệu của hàm số

trên mỗi khoảng mà hàm số đó xác định. Chẳng hạn như, hàm số f(x) $= \frac{1}{x}$ có f'(x) $=$

$-\frac{1}{x^2} <$ 0 $\ \forall$ x $\in \text{TXD} = \mathbb{R} \setminus \{0\}$ nhưng nếu nói f(x) đơn điệu giảm trên $\mathbb{R} \setminus \{0\}$ thì sẽ dẫn

đến nghịch lý là -1 $<$ 1 nhưng -1 $=$ f(-1) $<$ f(1) $=$ 1. Thay vì đó, ta nói hàm số f(x)

đơn điệu giảm trên mỗi khoảng $(-\infty,0)$ và $(0,+\infty)$.

## 3.3 Hàm số bị chặn đơn điệu giảm trên mỗi khoảng <math>(-\infty,0)</math> và <math>(0,+\infty)</math>.

• Một hàm số f(x) được gọi là bị chặn trên nếu tồn tại số M $\in \mathbb{R}$ sao cho f(x) $\leq$ M với

moi x $\in$ TXĐ.



• Một hàm số f(x) được gọi là bị chặn dưới nếu tồn tại số m $\in \mathbb{R}$ sao cho f(x) $\geq$ M với

moi x $\in$ TXĐ.

• Một hàm số f(x) được gọi là bị chặn nếu nó vừa bị chặn trên, vừa bị chặn dưới.

## 3.4 Hàm số chẵn, hàm số lẻ • Một hàm số <math>f(x)</math> được gọi là bị chặn nếu nó vừa bị chặn trên, vừa bị chặn dưới.

$ • Một hàm số f(x) được gọi là chẵn nếu \begin{cases} x \in \text{TXD} \Rightarrow -x \in \text{TXD} \\ f(-x) = f(x). \end{cases} $

Đồ thị của hàm số chẵn nhận trục tung làm trục đối xứng.

$ • Một hàm số f(x) được gọi là lẻ nếu \begin{cases} x \in \text{TXD} \Rightarrow -x \in \text{TXD} \\ f(-x) = -f(x). \end{cases} $

Đồ thị của hàm số lẻ nhận gốc tọa độ làm tâm đối xứng.

Ví dụ 3.2. Chứng minh rằng bất kì hàm số f(x) nào xác định trong một khoảng đối xứng

(-a, a) cũng đều biểu diễn được duy nhất dưới dạng tổng của một hàm số chẵn và một

hàm số lẻ.

[Gợi ý] Với mỗi f(x) bất kì ta luôn có

f(x) $= \frac{1}{2}[f(x)$ + f(-x)] + $\frac{1}{2}[f(x)$ - f(-x)]

h(x)

g(x)

trong đó g(x) là một hàm số chẵn, còn h(x) là một hàm số lẻ. Các bạn độc giả được khuyến

khích tự chứng minh tính duy nhất của phân tích này.

## 3.5 Hàm số tuần hoàn khích tự chứng minh tính duy nhất của phân tích này.

Định nghĩa 1.2. Một hàm số f(x) được gọi là tuần hoàn nếu như tồn tại số thực T $>$ 0

sao cho

f(x) $=$ f(x + T) $\ \forall$ x $\in \textit{TXD}$.

Ví du như các hàm số lượng giác y $= \sin$ x, y $= \cos$ x, y $= \tan$ x, y $= \cot$ x đã học ở phổ thông

là các hàm số tuần hoàn. Trong phạm vi Bài giảng này, chúng ta quan tâm chủ yếu là

xem có số T $>$ 0 nào đó thỏa mãn f(x + T) $=$ f(x) mà không đi sâu vào việc tìm chu kỳ

(số T $>$ 0 bé nhất).

Các câu hỏi sau đây tuy phát biểu đơn giản (và tưởng chừng như dễ trả lời) nhưng câu

trả lời sẽ rất thú vị:



• Tổng (hiệu) của hai hàm số tuần hoàn có tuần hoàn không?

• Tích của hai hàm số tuần hoàn có tuần hoàn không?

• Thương của hai hàm số tuần hoàn có tuần hoàn không?

• Đạo hàm của hàm số tuần hoàn (nếu có) có tuần hoàn không?

• Nếu hàm số F(x) có đạo hàm trên $\mathbb{R}$ và F'(x) là một hàm số tuần hoàn thì F(x) có tuần

hoàn không? Nói cách khác, nếu f(x) là một hàm số tuần hoàn thì F(x) $= \int_{0}^{x}$ f(t) dt

có tuần hoàn không?

3.6 Hàm hợp

Cho hai hàm số f, g. Hàm hợp của f và g, kí hiệu là f $\circ$ g, là hàm số được định nghĩa

bởi

(f $\circ$ g)(x) $=$ f[g(x)].

3.7 Ham ngươc

Định nghĩa 1.3. Một hàm số f : X $\rightarrow$ Y được gọi là ánh xạ 1 - 1 (hay còn gọi là đơn ánh)

nếu:

$x_1 \neq x_2 \Rightarrow f(x_1) \neq f(x_2)$.

### Định nghĩa 1.4. <i>Cho f là một đơn ánh với miền xác định A và miền giá trị B. Khi đó hàm</i>

ngược $f^{-1}$, có miền xác định B và miền giá trị A, được định nghĩa bởi

$f^{-1}(y) =$ x $\Leftrightarrow$ f(x) $=$ y.

Miền xác định của f $=$ Miền giá trị của $f^{-1}$

Miền giá trị của f $=$ Miền xác định của $f^{-1}$

Chú ý 1.2. $\overrightarrow{D}$ thị của hàm ngược đối xứng với đồ thị của hàm y $=$ f(x) qua đường phân

giác của góc phần tư thứ nhất.

Để tìm hàm số ngược của hàm số y $=$ f(x) ta làm như sau:

• Viết y $=$ f(x),

• Từ phương trình này giải x theo y, giả sử được x $=$ g(y),

• Đổi vai trò của x và y để được hàm số ngược $f^{-1}(x) =$ g(x).



Ví dụ, tìm hàm ngược của hàm số y $=$ 2x + 3, ta rút x theo y thì được x $= \frac{y-3}{2}$, sau đó

đổi vai trò của x và y để được hàm ngược là y $= \frac{x-3}{2}$. Tuy nhiên, cũng có nhiều khi hàm

số không phải là đơn ánh trên toàn trục số $\mathbb{R}$, khi đó chúng ta phải xét hàm số trên các

khoảng mà hàm số đó là đơn ánh và tìm hàm ngược trên các khoảng tương ứng.

Định lý 1.1. Nếu hàm số f(x) đơn điệu tăng (hoặc giảm) trên khoảng (a,b) thì tồn tại

hàm số ngược $f^{-1}$ của f trên khoảng đó.

## 3.8 Hàm số sơ cấp hàm số ngược <math>f^{-1}</math> của <math>f</math> trên khoảng đó.

Năm loại hàm số sơ cấp cơ bản

1. Hàm lũy thừa y $= x^{\alpha}$. TXĐ của hàm số này phụ thuộc vào $\alpha$.

• Nếu $\alpha$ nguyên dương, ví dụ hàm y $= x^2$, hàm số xác định với mọi x $\in \mathbb{R}$,

• Nếu $\alpha$ nguyên âm, ví dụ hàm y $= x^{-2} = \frac{1}{x^2}$, hàm số y $= y^{\alpha} = \frac{1}{x^{-\alpha}}$ xác định với

moi x $\in \mathbb{R} \setminus \{0\},\$

• Nếu $\alpha = \frac{1}{p}$, p nguyên dương chẵn, ví dụ y $= x^{1/2} = \sqrt{x}$, thì hàm số xác định trên

$\mathbb{R}_{>0}$,

• Nếu $\alpha = \frac{1}{v}$, nguyên dương lẻ, ví dụ y $= x^{1/3} = \sqrt[3]{x}$, thì hàm số xác định trên $\mathbb{R}$,

• Nếu $\alpha$ là số vô tỉ thì quy ước chỉ xét hàm số tại x $>$ 0.

2. Hàm số mũ y $= a^x$ (0 $<$ a $\neq$ 1) có tập xác định là $\mathbb{R}$ và tập giá trị là $\mathbb{R}_{>0}$. Hàm này

đồng biến nếu a $>$ 1 và nghịch biến nếu 0 $<$ a $<$ 1.

3. Làm số logarit y $= \log_a(x)$ (0 $<$ a $\neq$ 1), ngược với hàm số mũ, hàm số này có TXĐ

là $\mathbb{R}_{>0}$ và tập giá trị là $\mathbb{R}$. Hàm số này đồng biến nếu a $>$ 1 và nghịch biến nếu

0 $<$ a $<$ 1. Nó là hàm số ngược của hàm số mũ, do đó đồ thị của nó đối xứng với đồ

thị của hàm số y $= a^x$ qua đường phân giác của góc phần tư thứ nhất. Logarit cơ số

10 của x được kí hiệu là lg x. Logarit cơ số e của x được kí hiệu là ln x.

4. Các hàm lượng giác:

• Hàm số y $= \sin$ x xác định $\forall$ x $\in \mathbb{R}$, là hàm số lẻ, tuần hoàn chu kì $2\pi$.



![](graphs/graph_10_0.png)



• Hàm số y $= \cos$ x xác định $\forall$ x $\in \mathbb{R}$, là hàm số chẵn, tuần hoàn chu kì $2\pi$.

y $= \cos$ x, 0 $\le$ x $\le \pi$

$\overleftarrow{\mathcal{X}}$

$\bigcap$

• Hàm số y $= \tan$ x xác định $\forall$ x $\in \mathbb{R} \setminus \{(2k+1)\frac{\pi}{2}$, k $\in \mathbb{Z}\}$, $\text{$ là hàm số lẻ, tuần $hoàn}$



![](graphs/graph_11_1.png)



![](graphs/graph_11_0.png)



![](graphs/graph_11_2.png)

chu kì $\pi$.

$\mathop{\mathcal{X}_{}}\nolimits$

• Hàm số y $= \cot$ x xác định $\forall$ x $\in \mathbb{R} \setminus \{k\pi$, k $\in \mathbb{Z}\}$, là hàm số lẻ, tuần hoàn chu kì

$\pi$.



![](graphs/graph_11_5.png)



![](graphs/graph_11_3.png)



![](graphs/graph_11_4.png)



Ví dụ 3.3 (Nguy biện toán học). Chứng minh rằng 0 $=$ 2.

Chúng minh. Ta có

$\cos^2$ x $=$ 1 - $\sin^2$ x $\Rightarrow \cos$ x $= \sqrt{1$ - $\sin^2 x} \Rightarrow$ 1 + $\cos$ x $=$ 1 + $\sqrt{1$ - $\sin^2 x}$.

Thay x $= \pi$ vào đẳng thức 1 + $\cos$ x $=$ 1 + $\sqrt{1$ - $\sin^2 x}$ ta được 0 $=$ 2.

$\qquad \qquad \blacksquare$

5. Các hàm lượng giác ngược:

Muốn tìm hàm ngược của một hàm số, một yêu cầu đặt ra là hàm số đó phải là đơn

ánh. Tuy nhiên, các hàm lượng giác đều là các hàm số tuần hoàn (do đó, không phải

là đơn ánh). Chẳng hạn như, hàm số y $= \sin$ x không phải là đơn ánh trên $\mathbb{R}$. Để

vượt qua khó khăn này, người ta hạn chế các hàm số lượng giác trên các khoảng mà

nó là đơn ánh. Chẳng hạn như, hàm số f(x) $= \sin$ x, $-\frac{\pi}{2} \le$ x $\le \frac{\pi}{2}$ là một đơn ánh.

y $= \sin$ x, $-\frac{\pi}{2} \le$ x $\le \frac{\pi}{2}$

$-\frac{\pi}{2}$

$rac{\pi}{2}$

• Hàm số ngược của hàm số y $= \sin$ x, kí hiệu là arcsin x, xác định như sau:

arcsin : [0,1] $\rightarrow \left[-\frac{\pi}{2},\frac{\pi}{2}\right]$

x $\mapsto$ y $= \arcsin$ x $\Leftrightarrow$ x $= \sin$ y

Hàm số y $= \arcsin$ x xác định trên [-1,1], nhận giá trị trên $\left[-\frac{\pi}{2}$, $\frac{\pi}{2}\right]$ và là một

hàm số đơn điệu tăng.

$rac{\pi}{2}$

$\sin$ x

$\arcsin$ x

$\mathop{\mathcal{X}_{}}\nolimits$



• Hàm số ngược của hàm số y $= \cos$ x, kí hiệu là y $= \arccos$ x, được xác định như

sau:

arccos: [0,1] $\rightarrow [0,\pi]$

x $\mapsto$ y $= \arccos$ x $\Leftrightarrow$ x $= \cos$ y

Hàm số y $= \arccos$ x xác định trên [-1, 1], nhận giá trị trên [0, $\pi]$ và là một hàm

số đơn điệu giảm.

$rac{\pi}{2}$

arccos x

$\pi$

O

$\cos$ x

$\mathop{\mathcal{X}_{}}\nolimits$

$\frac{\pi}{2}$

• Hàm số ngược của hàm số y $= \tan$ x, kí hiệu là y $= \arctan$ x, được xác định như

sau:

arctan : $(-\infty$, $+\infty) \rightarrow \left(-\frac{\pi}{2}$, $\frac{\pi}{2}\right)$

x $\mapsto$ y $= \arctan$ x $\Leftrightarrow$ x $= \tan$ y

Hàm số y $= \arctan$ x xác định trên $\mathbb{R}$, nhận giá trị trên $\left(-\frac{\pi}{2}$, $\frac{\pi}{2}\right)$ và là một hàm

số đơn điệu tăng.

$rac{\pi}{2}$

tan x

arctan x

$\mathop{\mathcal{X}_{}}$

$-\frac{\pi}{2}$

• Hàm số ngược của hàm số y $= \cot$ x, kí hiệu là y $= \operatorname{arccot}$ x, được xác định như

sau:

arccot : $(-\infty$, $+\infty) \rightarrow$ (0, $\pi)$

x $\mapsto$ y $= \operatorname{arccot}$ x $\Leftrightarrow$ x $= \cot$ y



Hàm số y $= \operatorname{arccot}$ x xác định trên $\mathbb{R}$, nhận giá trị trên (0, $\pi)$ và là một hàm số

đơn điệu giảm.

$rac{\pi}{2}$

$\cot$ x

$\mathop \chi \nolimits$

$\operatorname{arccot}$ x

$\pi$

$-\frac{\pi}{2}$

Hàm số sơ cấp

Người ta gọi hàm số sơ cấp là hàm số được tạo thành bởi một số hữu hạn các phép toán

cộng, trừ, nhân, chia, phép lập hàm số đối với các hàm số sơ cấp cơ bản. Các hàm số sơ cấp

được chia thành hai loại.

• Hàm số đại số: là những hàm số mà khi tính giá trị của nó ta chỉ phải làm một số

hữu hạn các phép toán cộng, trừ, nhân, chia và lũy thừa với số mũ hữu tỉ. Ví dụ: các

đa thức, phân thức hữu tỉ, ...

• Hàm số siêu việt: là những hàm số sơ cấp nhưng không phải là hàm số đại số, như

y $= \ln$ x, y $= \sin$ x, $\dots$

## 3.9 Bài tập <math display="block">y = \ln x, y = \sin x, \dots</math>

Tìm TXĐ, MGT của hàm số

Bài tập 1.1. Tìm TXĐ của hàm số

a) y $= \sqrt[4]{\lg(\tan x)}$,

c) y $= \frac{\sqrt{x}}{\sin \pi x}$,

b) y $= \arcsin \frac{2x}{1+x}$,

d) y $= \arccos(2\sin$ x).

$[\text{Đáp}\text{ số}]$

c) $\{x \ge$ 0, x $\notin \mathbb{Z}\},\$

a) $\{\pi/4$ + $k\pi <$ x $< \pi/2$ + $k\pi$, k $\in \mathbb{Z}\},\$

b) $\{-1/3 \leq$ x $\leq 1\}$,

d) $\{-\frac{\pi}{6}$ + $k\pi \leq$ x $\leq \frac{\pi}{6}$ + $k\pi$, k $\in \mathbb{Z}\}$.

Bài tập 1.2. Tìm miền giá trị của hàm số



b) y $= \arcsin\left(\lg \frac{x}{10}\right)$

a) y $= \lg(1$ - $2\cos$ x)

$[\text{Đáp}\text{ số}]$

a) $\{-\infty <$ y $\leq \lg 3\}$

b) $\{-\pi/2 \leq$ y $\leq \pi/2\}$

Tìm hàm ngược.

Bài tập 1.3. Tìm hàm ngược của hàm số (trên miền mà hàm số có hàm ngược)

b) y $= \frac{1-x}{1+x}$,

c) y $= \frac{1}{2}(e^x$ + $e^{-x})$.

a) y $=$ 2x + 3,

$[\text{Đáp}\text{ s}\hat{\text{o}}]$

a) y $= \frac{1}{2}x$ - $\frac{3}{2}$.

b) y $=$ y $= \frac{1-x}{1+x}$.

c) Ta có y' $= \frac{1}{2}(e^x$ - $e^{-x})$ không xác dịnh dấu, nên hàm số đã cho có thể không phải là

một đơn ánh. Trước hết,

y $= \frac{1}{2}(e^x$ + $e^{-x}) \Leftrightarrow e^x =$ y $\pm \sqrt{y^2$ - $1} \Leftrightarrow$ x $= \ln(y \pm \sqrt{y^2$ - $1})$.

Ta phải xét trên 2 miền:

• Trên miền x $>$ 0, ta có song ánh:

$(0,+\infty)\to(1,+\infty)$

x $\mapsto$ y $= \frac{1}{2}(e^x$ + $e^{-x})$

$\ln(y$ + $\sqrt{y^2$ - $1}) \leftarrow$ y

Vậy hàm ngược trên miền x $>$ 0 là y $= \ln(x$ + $\sqrt{x^2$ - $1})$, x $>$ 1.

• Trên miền x $<$ 0, tương tự ta có hàm ngược là y $= \ln(x$ - $\sqrt{x^2$ - $1})$, x $>$ 1.

Ví du 3.4 (Giữa kì, K61). Tìm hàm ngược của hàm số sau

a) y $= \frac{x+1}{2x+1}$.

b) y $= \frac{x-1}{2x-1}$.

Xét tính chẵn lẻ của hàm số

Bài tập 1.4. Xét tính chẵn lẻ của hàm số



a) f(x) $= a^x$ + $a^{-x}$ (a $>$ 0) b) f(x) $= \ln(x$ + $\sqrt{1$ - $x^2})$ c) f(x) $= \sin$ x + $\cos$ x

$[\text{Đáp}\text{ số}]$

a) Hàm số đã cho là hàm số chẵn.

b) Hàm số đã cho là hàm số lẻ.

c) Hàm số đã cho không chẵn, không lẻ.

Ví dụ 3.5 (Giữa kì, K61). Xét tính chẵn lẻ của hàm số

b) y $= \sin(\tan$ x).

a) y $= \tan(\sin$ x).

Ví dụ 3.6. Cho hàm số f(x) xác định và có đạo hàm trên $\mathbb{R}$. Chứng minh rằng

a) nếu f(x) là một hàm số lẻ thì f'(x) là một hàm số chẵn.

b) nếu f(x) là một hàm số chẵn thì f'(x) là một hàm số lẻ.

Xét tính tuần hoàn của hàm số

Bài tập 1.5. Xét tính tuần hoàn và chu kì của hàm số sau (nếu có)

c) f(x) $= \sin^2$ x,

a) f(x) $=$ A $\cos \lambda$ x + B $\sin \lambda$ x,

b) f(x) $= \sin$ x + $\frac{1}{2} \sin$ 2x + $\frac{1}{3} \sin$ 3x,

d) f(x) $= \sin(x^2)$.

a) Giả sử T $>$ 0 là một chu kì của hàm số đã cho. Khi đó

Chứng minh.

f(x+T) $= f(x)\forall$ x $\in \mathbb{R}$

$\Leftrightarrow A\cos\lambda(x+T)$ + $B\sin\lambda(x+T) = A\cos\lambda$ x + $B\sin\lambda$ x $\quad \forall$ x $\in \mathbb{R}$

$\Leftrightarrow A[\cos \lambda$ x - $\cos \lambda$ (x + T)] + $B[\sin \lambda$ x - $\sin \lambda$ (x + T)] $=$ 0 $\quad \forall$ x $\in \mathbb{R}$

$\Leftrightarrow 2\sin\frac{-\lambda T}{2}[A\sin(\lambda$ x + $\frac{\lambda T}{2})$ + $B\cos(\lambda$ x + $\frac{\lambda T}{2})] =$ 0 $\quad \forall$ x $\in \mathbb{R}$

$\Leftrightarrow \sin \frac{\lambda T}{2} =$ 0

$\Leftrightarrow$ T $= \left| \frac{2k\pi}{\lambda} \right|$.

Vậy hàm số đã cho tuần hoàn với chu kì T $= \frac{2\pi}{|\lambda|}$.

b) Theo câu a) thì hàm số sin x tuần hoàn với chu kì $2\pi$, hàm số sin 2x tuần hoàn với chu kì $\pi$, hàm số sin 3x tuần hoàn với chu kì $\frac{2\pi}{3}$. Vậy f(x) $= \sin$ x + $\frac{1}{2} \sin$ 2x + $\frac{1}{3} \sin$ 3x

tuần hoàn với chu kì T $= 2\pi$



c) f(x) $= \sin^2$ x $= \frac{1$ - $\cos 2x}{2}$ tuần hoàn với chu kì T $= \pi$

d) Giả sử hàm số đã cho tuần hoàn với chu kì T $>$ 0.Khi đó

$\sin(x+T)^2 = \sin(x^2)\forall$ x.

(a) Cho x $=$ 0 $\Rightarrow$ T $= \sqrt{k\pi}$, k $\in \mathbb{Z}$, k $>$ 0.

(b) Cho x $= \sqrt{\pi} \Rightarrow$ k là số chính phương. Giả sử k $= l^2$, l $\in \mathbb{Z}$, l $>$ 0.

(c) Cho x $= \sqrt{\frac{\pi}{2}}$ ta suy ra điều mâu thuẫn.

Vậy hàm số đã cho không tuần hoàn.



Nhận xét: Muốn chứng minh một hàm số không tuần hoàn, chúng ta có thể sử dụng

phương pháp phản chứng như đã trình bày ở trên. Giả sử hàm số đó tuần hoàn với chu kì

p $>$ 0 sau đó cho một vài giá trị đặc biệt của x để suy ra điều mâu thuẫn. Ngoài phương

pháp phản chứng thì chúng ta cũng có thể sử dụng một số tính chất của hàm số tuần hoàn

để chứng minh. Chẳng hạn như:

• một hàm số tuần hoàn và liên tục thì bị chặn (tại sao?),

• một hàm số tuần hoàn và không phải là hàm hằng thì không tồn tại $\lim_{x\to\infty}$ f(x) (tại

sao?),

• đạo hàm của một hàm số tuần hoàn (nếu có) thì cũng tuần hoàn (tại sao?).

Bài tập 1.6. Chứng minh các hàm số sau không tuần hoàn

(a) y $= \cos$ x + $\cos$ x $\sqrt{2}$,

(d) y $= \cos x^2$,

(b) y $= \sin$ x + $\sin$ x $\sqrt{2}$,

(e) y $= \sin \sqrt{x}$,

(c) y $= \sin x^2$,

(f) y $= \cos \sqrt{x}$.

a) Giả sử hàm số y $= \cos$ x + $\cos x\sqrt{2}$ tuần hoàn với chu kì T $>$ 0. Khi đó,

Chứng minh.

$\cos$ x + $\cos x\sqrt{2} = \cos(x+T)$ + $\cos(x+T)\sqrt{2} \ \forall$ x $\in \mathbb{R}$.

Cho x $=$ 0 ta được 2 $= \cos$ T + $\cos$ T $\sqrt{2}$. Vì cos T $\le$ 1, cos $T\sqrt{2} \le$ 1 nên

$ 2 = \cos T + \cos T\sqrt{2} \Leftrightarrow \begin{cases} \cos T = 1, \\ \cos T\sqrt{2} = 1. \end{cases} \Rightarrow \begin{cases} T = k2\pi, 0 \neq k \in \mathbb{N} \\ T\sqrt{2} = l2\pi, 0 \neq l \in \mathbb{N}. \end{cases} $

Khi $đó\sqrt{2} = \frac{l}{k} \in \mathbb{Q}$, điều này là vô lý $vì\sqrt{2}$ là một số vô tỉ. Như vậy, chúng ta đã trả lời

một câu hỏi trong Mục 3.5, rằng tổng của hai hàm số tuần hoàn có thể không phải là



một hàm số tuần hoàn. Hàm số f(x) $= \cos$ x + $\cos x\sqrt{2}$ là một hàm số hầu tuần hoàn

(almost periodic). Tương tự như vậy, tích của hai hàm số tuần hoàn cũng không phải

là một hàm số tuần hoàn, vì

$2\cos\frac{1+\sqrt{2}}{2}x\cos\frac{1-\sqrt{2}}{2}x = \cos$ x + $\cos x\sqrt{2}$.

$\blacksquare$

Bài tập 1.7. [Giữa kì, K61] Cho f(x), g(x) là các hàm số xác định trên $\mathbb{R}$ và tuần hoàn

với chu kì lần lượt là $T_1 >$ 0, $T_2 >$ 0. Biết tỉ số $\frac{T_1}{T_2}$ là một số hữu tỉ. Chứng minh rằng

f(x) + g(x) và f(x)g(x) cũng là các hàm số tuần hoàn.

Các dạng toán khác

Bài tập 1.8. Tìm f(x) biết

a) $f\left(x$ + $\frac{1}{x}\right) = x^2$ + $\frac{1}{x^2}$,

b) $f\left(\frac{x}{1+x}\right) = x^2$.

$[\text{Đáp}\text{ số}]$

a) f(x) $= x^2$ - 2 $\text{ v\'{o}i }$ |x| $>$ 2.

b) f(x) $= \left(\frac{x}{1-x}\right)^2 \forall$ x $\neq$ 1.

Bài tập 1.9. Cho f(x) $=$ ax + b, f(0) $=$ -2, f(3) $=$ -5. Tìm f(x).

[Đáp số] f(x) $= \frac{7}{3}x$ - 2.

Bài tập 1.10. Cho f(x) $= ax^2$ + bx + c, f(-2) $=$ 0, f(0) $=$ 1, f(1) $=$ 5. Tìm f(x).

[Đáp số] f(x) $= \frac{7}{6}x^2$ + $\frac{17}{6}x$ + 1.

Bài tập 1.11. Cho f(x) $= \frac{1}{2}(a^x$ + $a^{-x})$, a $>$ 0. Chứng minh rằng :

f(x + y) + f(x - y) $=$ 2f(x)f(y).

Bài tập 1.12. Giả sử f(x) + f(y) $=$ f(z). Xác định z nếu:

a) f(x) $=$ ax, a $\neq$ 0,

c) f(x) $= \frac{1}{x}$,

d) f(x) $= \lg \frac{1+x}{1-x}$.

b) f(x) $= \arctan$ x,

$[\text{Đáp}\text{ số}]$



c) z $= \frac{xy}{x$ + $y},d)$ z $= \frac{x$ + $y}{1$ + $xy}$.

a) z $=$ x + y,

b) z $= \frac{x+y}{1-xy}$,



$\S4$. DÃY SỐ

## 4.1 Dãy số và giới han của dãy số <math>\S</math><b>4.</b> DÃY SỐ

Định nghĩa 1.5. Một dãy số là một hàm số $\mathbb{N} \to \mathbb{R}$, n $\mapsto a_n$. Kí hiệu $\{a_n\}_{n \in \mathbb{N}}$.

Một dãy số được gọi là:

• đơn điệu tăng nếu $a_n < a_{n+1} \forall$ n, đơn điệu giảm nếu $a_n > a_{n+1} \forall$ n.

• bị chặn trên nếu tồn tại số M sao cho $a_n \leq$ M $\forall$ n, bị chặn dưới nếu tồn tại số m sao

cho $a_n \geq$ m $\ \forall$ n.

Định nghĩa 1.6. Một dãy số $\{a_n\}$ được gọi là có giới hạn là L và viết

$\lim_{n\to\infty} a_n =$ L $\; \textit{hay } a_n \to$ L $\; \textit{khi }$ n $\to \infty$,

nếu

• (nói một cách nôm na) có thể làm cho các số hạng $a<sub>n</sub>$ gần L với một giá trị tùy ý bằng

cách chọn n đủ lớn.

• (nói một cách chính xác) với mọi $\epsilon >$ 0, tồn tại số tự nhiên N sao cho

$n\hat{e}u$ n $>$ N thì $|a_n$ - L| $< \epsilon$.

Hình dung rằng $\lim_{n\to+\infty} a_n =$ L nghĩa là với mọi $\epsilon >$ 0 thì từ một lúc nào đó toàn bộ số hạng

của dãy $\{a_n\}_{n>N}$ sẽ chui vào trong khoảng (L - $\epsilon$, L + $\epsilon)$.

$a_n$, $\forall$ n $>$ N

Hình 1.6

Một dãy số $\{a_n\}$ có $\lim_{n\to+\infty} a_n =$ L hữu hạn được gọi là hội tụ. Ngược lại, nó được gọi là phân

kì (nghĩa là lim $a_n = \infty$ hoặc là không tồn tại).

Định nghĩa 1.7 (Giới hạn vô cùng). Ta nói $\lim_{n\to\infty} a_n = +\infty$ nếu với mọi số thực dương M,

$t\hat{0}n$ tại số tự nhiên N sao cho

$n\acute{e}u$ n $>$ N thì $a_n >$ M.

Hãy phát biểu cho trường hợp $\lim_{n\to\infty} a_n = -\infty$



Đinh lý 1.2 (Các tính chất của giới han của dãy số).

• Giới hạn của một dãy số, nếu tồn tại, là duy nhất.

• Mọi dãy số hội tụ đều bị chặn.

Định lý 1.3 (Các phép toán trên giới hạn). Giả sử $\lim_{n\to+\infty} a_n =$ A, $\lim_{n\to+\infty} b_n =$ b, ở đó a, b

là các số thực hữu hạn. Khi đó:

• Tổng: $\lim_{n\to+\infty}(a_n+b_n)=A+B$,

• Hiệu: $\lim_{n\to+\infty}(a_n-b_n)=A-B$,

• Tích: $\lim_{n\to+\infty}(a_n.b_n)=AB$,

• Thương: $\lim_{n\to+\infty} \frac{a_n}{b_n} = \frac{A}{B}$ n $\hat{e}$ u B $\neq$ 0.

Chú ý 1.3. Các phép toán trên giới hạn sau không thực hiện được, chúng còn được gọi là

các dạng vô định:

$\infty$ - $\infty$, 0 $\times \infty$, $\frac{\infty}{\infty}$, $\frac{0}{0}$.

## 4.2 Các tiêu chuẩn tồn tại giới hạn <math>\infty - \infty, 0 \times \infty, \frac{\infty}{\infty}, \frac{0}{0}.</math>

### Định lý 1.4 (Tiêu chuẩn kẹp). Giả sử

i) $a_n \le b_n \le c_n$ với mọi n $\in \mathbb{N}$ hoặc với mọi n $\ge$ K nào đó,

ii) $\lim_{n\to+\infty} a_n = \lim_{n\to+\infty} c_n =$ L.

Khi đó, $\lim_{n\to+\infty} b_n =$ L.

Đinh lý 1.5 (Tiêu chuẩn đơn điệu bị chặn). Mọi dãy số đơn điệu tăng (đơn điệu giảm)

và bị chặn trên (tương ứng, bị chặn dưới) đều hội tụ.

Ví dụ 4.1. Xét $u_n = \left(1$ + $\frac{1}{n}\right)^n$. Chứng minh rằng $\{u_n\}$ là một dãy số tăng và bị chặn.

Chứng minh. Áp dụng bất đẳng thức Cauchy ta có :

$1+\left(1+\frac{1}{n}\right)+\ldots+\left(1+\frac{1}{n}\right)\geq (n+1)\sqrt[n+1]{\left(1+\frac{1}{n}\right)^n}$.

n số hang



$\Rightarrow \left(1+\frac{1}{n+1}\right)^{n+1} \ge \left(1+\frac{1}{n}\right)^n$.

Hơn nữa ta có

$u_n = \left(1$ + $\frac{1}{n}\right)^n = \sum_{k=0}^n C_n^k \cdot \frac{1}{n^k}$

k! $=$ 1.2 $\ldots$ k $> 2^{k-1} \forall$ k $>$ 2

$\Rightarrow C_n^k \cdot \frac{1}{n^k} = \frac{n.(n-1)...(n-k+1)}{k!} \cdot \frac{1}{n^k} < \frac{1}{k!} \leq \frac{1}{2^{k-1}}$

$\Rightarrow u_n <$ 1 + 1 + $\frac{1}{2}$ + $\frac{1}{2^2}$ + $\ldots$ + $\frac{1}{2^{k-1}} <$ 3.

Chú ý 1.4. Giới hạn $\lim_{n\to+\infty} \left(1+\frac{1}{n}\right)^n$ là một số vô tỉ, được kí hiệu là e. Nó có giá trị xấp xỉ

2.71.

Ví du 4.2 (Giữa kì, 20173). Xét sự hội tụ và tìm giới hạn (nếu có) của dãy số

$\{x_n\}: x_1 >$ 0, $x_{n+1} = \frac{1}{2} \left( x_n$ + $\frac{1}{x_n} \right)$, n $\ge$ 1.

[Lời giải] Từ $x_1 >$ 0 ta có $x_n >$ 0 với mọi n.

$x_n = \frac{1}{2} \left( x_{n-1}$ + $\frac{1}{x_{n-1}} \right) \ge$ 1.

Do đó, $x_{n+1} = \frac{1}{2} \left( x_n$ + $\frac{1}{x_n} \right) \leq x_n$ với mọi n. Như vậy, $\{x_n\}$ là một dãy số giảm và bị chặn

dưới nên tồn tại $\lim_{n \to +\infty} x_n =$ a.

$x_{n+1} = \frac{1}{2} \left( x_n$ + $\frac{1}{x_n} \right) \Rightarrow$ a $= \frac{1}{2} \left($ a + $\frac{1}{a} \right) \Rightarrow$ a $=$ 1.

$\text{Vây } \lim_{n \to +\infty} x_n =$ 1.

Định nghĩa 1.8. Dãy số $\{a_n\}$ được gọi là dãy số Cauchy nếu với mọi $\epsilon >$ 0, tồn tại số tự

nhiên N sao cho $|a_n$ - $a_m| < \epsilon$ với mọi m, n $>$ N.

### Định lý 1.6 (Tiêu chuẩn Cauchy). Dãy số <math>\{a_n\}</math> là hội tụ khi và chỉ khi nó là dãy số

Cauchy.

Ví dụ 4.3. Chứng minh rằng dãy số $\{a_n\}$ với

$a_n =$ 1 + $\frac{1}{2}$ + $\frac{1}{3}$ + $\cdots$ + $\frac{1}{n}$

là một dãy số phân kỳ.



Ví dụ 4.4 (Ngụy biện toán học). Cho x là một số thực và L $= \lim_{n \to +\infty} x^n$. Đổi biến số

n $=$ m + 1 $\text{$ ta $c} \acute{o}$

L $= \lim_{m+1 \to +\infty} x^{m+1} = \lim_{m \to +\infty} x.x^m =$ x. $\lim_{m \to +\infty} x^m =$ xL.

$V_{\hat{a}y}$ L $=$ xL $\Rightarrow$ L(x-1) $=$ 0. Nếu x $\neq$ 1 thì L $=$ 0. Nói cách khác,

$\n\lim_{n \to +\infty} x^n =$ 0 $\ \forall$ x $\neq 1.\n$

Điều này dẫn đến, chẳng hạn,

$\lim_{n\to+\infty} 2^n =$ 0 thật vô lý!.

Giải thích tại sao lại dẫn đến mâu thuẫn trên?

## 4.3 Bài tâp Giải thích tại sao lại dẫn đến mâu thuẫn trên?

Về bài tập tìm giới hạn của dãy số, về cơ bản cho đến thời điểm hiện tại chúng ta chưa

có nhiều công cụ để xử lý. Chủ yếu vẫn là các phương pháp nhân liên hợp để khử dạng

vô định ở phổ thông, sử dụng tiêu chuẩn đơn điệu bị chặn, tiêu chuẩn kẹp và tiêu chuẩn

Cauchy. Sau này, khi học đến giới hạn của hàm số, các công cụ sẽ phong phú hơn. Khi đó

các bài toán về giới hạn của dãy số có thể đưa về giới hạn của hàm số và tính toán dễ dàng.

Bài tập 1.13. Tìm giới hạn của các dãy số sau:

a) $x_n =$ n - $\sqrt{n^2$ - $n}$, c) $x_n =$ n + $\sqrt[3]{1$ - $n^3}$,

e) $x_n = \frac{\sin^2$ n - $\cos^3 n}{n}$.

b) $x_n = \sqrt{n(n+a)}$ - n, d) $x_n = \frac{n}{2} \sin \frac{n\pi}{2}$,

$[\text{Đáp}\ \text{s}\hat{\text{o}}]$

b) $\frac{u}{2}$

a) $\frac{1}{2}$

$\mathbf{c}) \ \$ 0

d) phân kì

e) 0

Bài tập 1.14. Xét dãy số $x_n = x_{n-1}$ + $\frac{1}{x_{n-1}}$, $x_0 =$ 1.

a) Chứng minh rằng dãy $\{x_n\}$ không có giới hạn hữu hạn.

b) Chứng minh rằng $\lim_{n\to\infty} x_n = +\infty$.

Bài tập 1.15. Cho $s_n =$ 1 + $\frac{1}{1!}$ + ... + $\frac{1}{n!}$. Chứng minh rằng $\{s_n\}$ tăng và bị chặn.

Chú ý: $\lim_{n\to+\infty} s_n =$ e.



Bài tập 1.16. Tính $\lim_{n\to+\infty} \frac{1+a+\ldots+a^n}{1+b+\ldots+b^n}$, |a| $<$ 1, |b| $<$ 1.

Chứng minh.

$\n\lim_{n \to +\infty} \frac{1$ + a + $\ldots$ + $a^n}{1$ + b + $\ldots$ + $b^n} = \lim_{n \to +\infty} \frac{1$ - $a^{n+1}}{1$ - $a} \cdot \frac{1$ - $b}{1$ - $b^{n+1}} = \frac{1$ - $b}{1$ - $a}\n$

Bài tập 1.17. Tính $\lim_{n \to +\infty} \sqrt{2$ + $\sqrt{2$ + $\ldots$ + $\sqrt{2}}}$ (n dấu căn).

Chứng minh. Đặt $u_n = \sqrt{2$ + $\sqrt{2$ + $\ldots$ + $\sqrt{2}}}$ ta có $u_{n+1}^2 =$ 2 + $u_n$. Trước hết chứng minh

$\{u_n\}$ là một dãy số tăng và bị chặn, 0 $\le u_n \le$ 2. Theo tiêu chuẩn đơn điệu bị chặn, $\{u_n\}$

là một dãy số hội tụ. Giả sử $\lim_{n \to \infty} u_n =$ a, 0 $<$ a $<$ 2 thì từ phương trình $u_{n+1}^2 =$ 2 + $u_n$, cho

n $\rightarrow \infty$ ta có

$a^2 =$ a + 2

Vậy a $=$ 2 hay $\lim_{n \to +\infty} \sqrt{2$ + $\sqrt{2$ + ... + $\sqrt{2}}} =$ 2

Bài tập 1.18. Tính $\lim_{n\to+\infty}(n-\sqrt{n^2-1})\sin$ n.

[Gợi ý] $\lim_{n \to +\infty}$ (n - $\sqrt{n^2$ - $1}) \sin$ n $= \lim_{n \to +\infty} \frac{\sin n}{n$ + $\sqrt{n^2$ - $1}} =$ 0 (theo tiêu chuẩn kẹp)

Bài tập 1.19. Tính $\lim_{n\to+\infty} [\cos(\ln$ n) - $\cos(\ln(n+1))]$.

Chúng minh. Ta có

$\cos(\ln$ n) - $\cos(\ln(n+1)) = -2\sin\left(\frac{\ln$ n + $\ln(n+1)}{2}\right) \cdot \sin\left(\frac{\ln$ n - $\ln(n+1)}{2}\right)$

$\blacksquare$

$= -2\sin\frac{\ln n(n+1)}{2}\sin\frac{\ln\frac{n}{n+1}}{2}$

$n\hat{e}n$

0 $\leq |\cos(\ln$ n) - $\cos(\ln(n+1))| \leq$ 2 $\left| \sin \frac{\ln \frac{n}{n+1}}{2} \right|$

Mặt khác $\lim_{n\to\infty} \sin\frac{\ln\frac{n}{n+1}}{2}=0nên$ theo nguyên lý giới hạn kẹp

$\lim_{n \to +\infty} [\cos(\ln$ n) - $\cos(\ln(n+1))] =$ 0

Bài tập 1.20. Chứng minh rằng $\lim_{n\to+\infty}\frac{n}{2^n}=0$.



[Gợi ý]

$2^{n} = (1+1)^{n} > \frac{n(n-1)}{2} \Rightarrow$ 0 $< \frac{n}{2^{n}} < \frac{2}{n-1}$.

Dùng nguyên lý kẹp ta có điều phải chứng minh.

Bài tập 1.21. Chứng minh rằng $\lim_{n\to+\infty}\frac{2^n}{n!}=0$.

[Gơi $\circ]$ Ta có

0 $< \frac{2^n}{n!} = \frac{2}{1} \cdot \frac{2}{2} \cdot \frac{2}{3} \dots \frac{2}{n} <$ 2 $\cdot \frac{2}{n} \ \forall$ n $\ge$ 2.

Bài tập 1.22. Tính

a) $\lim_{n \to +\infty} \left( \frac{1}{2}$ + $\frac{1}{2^2}$ + $\cdots$ + $\frac{n}{2^n} \right)$

b) $\lim_{n \to +\infty} \left( \frac{1}{3}$ + $\frac{1}{3^2}$ + $\cdots$ + $\frac{n}{3^n} \right)$

[Gợi ý]

a. Tính $S_n$ - $\frac{1}{2}S_n \Rightarrow \lim_{n \to +\infty} S_n =$ 2.

b. Tính $S_n$ - $\frac{1}{3}S_n \Rightarrow \lim_{n \to +\infty} S_n = \frac{3}{4}$.

Bài tập 1.23. Chứng minh rằng $\lim_{n\to+\infty} \sqrt[n]{n} =$ 1, $\lim_{n\to+\infty} \sqrt[n]{a} =$ 1 với mọi a $>$ 0.

$[G\phi$ i $\acute{y}]$

a) Đặt $\alpha_n = \sqrt[n]{n}$ - 1 $\Rightarrow$ n $=$ (1 + $\alpha_n)^n > \frac{n(n-1)}{2} \alpha_n^2 \Rightarrow \alpha_n^2 < \frac{2}{n-1}$. Áp dụng nguyên lý giới

hạn kẹp ta có $\lim_{n\to\infty} \alpha_n =$ 0. Vậy $\lim_{n\to\infty} \sqrt[n]{n} =$ 1.

b) Xét $\lim_{n\to+\infty} \sqrt[n]{a}$.

• Nếu a $=$ 1, xong.

• Nếu a $>$ 1, 1 $\leq \sqrt[n]{a} \leq \sqrt[n]{n} \ \forall$ n $>$ a $\Rightarrow \lim_{n \to +\infty} \sqrt[n]{a} =$ 1

• Nếu a $<$ 1, đặt a' $= \frac{1}{a} \Rightarrow \lim \sqrt[n]{a'} =$ 1 $\Rightarrow \lim_{n \to +\infty} \sqrt[n]{a} =$ 1.

Bài tập 1.24. Tính $\lim_{n \to +\infty} x_n$, ở đó $x_n = \frac{1}{2$ + $\frac{1}{2$ + $\dots$ + $\frac{1}{2}}}$ (n phép chia).

[Lời giải]



1) Trước hết ta chứng minh 0 $< x_{2n} <$ -1 + $\sqrt{2}$ và $x_{2n+1} >$ -1 + $\sqrt{2}$. Thật vậy,

Nếu $x_n >$ -1 + $\sqrt{2}$ thì $x_{n+1} = \frac{1}{2$ + $x_n} < \frac{1}{2$ + (-1 + $\sqrt{2})} = \frac{1}{1$ + $\sqrt{2}} =$ -1 + $\sqrt{2}$.

Nếu $x_n <$ -1 + $\sqrt{2}$ thì $x_{n+1} = \frac{1}{2$ + $x_n} > \frac{1}{2$ + (-1 + $\sqrt{2})} = \frac{1}{1$ + $\sqrt{2}} =$ -1 + $\sqrt{2}$.

Như vậy, dãy $\{x_n\}$ này có quy luật là, cứ một số hạng nào đó nhỏ hơn -1 + $\sqrt{2}$ thì số

hạng đứng ngay sau nó lớn hơn $-1+\sqrt{2}$, và ngược lại. Do đó,

$x_1 = \frac{1}{2} >$ -1 + $\sqrt{2} \Rightarrow x_2 <$ -1 + $\sqrt{2} \Rightarrow x_3 >$ -1 + $\sqrt{2} \Rightarrow \cdots$

$ dẫn đến việc \begin{cases} 0 < x_{2n} < -1 + \sqrt{2}, \\ x_{2n+1} > -1 + \sqrt{2}. \end{cases} $

2) Tiếp theo, ta đi chứng minh dãy $\{x_{2n}\}\$ là một dãy số tăng, thật vậy,

$x_{2n+2}=\frac{1}{2+x_{2n+1}}=\frac{1}{2+\frac{1}{2+\cdots}}=\frac{2+x_{2n}}{5+2x_{2n}}$.

$x_{2n+2} > x_{2n} \Leftrightarrow \frac{z$ + $x_{2n}}{5$ + $2x_{2n}} > x_{2n} \Leftrightarrow 2x_{2n}^2$ + $4x_{2n}$ - 2 $<$ 0 $\Leftrightarrow$ -1 - $\sqrt{2} < x_{2n} <$ -1 + $\sqrt{2}$

Điều này luôn đúng, vì ta đã chứng minh ở trên, rằng dãy các số hạng chẵn thỏa

mãn $x_{2n} <$ -1 + $\sqrt{2}$.

Dãy số này tăng và bị chặn trên bởi -1 + $\sqrt{2}$ nên tồn tại $\lim_{n \to \infty} x_{2n} =$ a. Phương trình

$x_{2n+2} = \frac{2+x_{2n}}{5+2x_{2n}}$ dẫn đến a $= \frac{2+a}{5+a} \Rightarrow$ a $=$ -1 + $\sqrt{2}$.

3) Tương tự như vậy, dãy $\{x_{2n+1}\}$ sẽ là một dãy số giảm. Thật vậy,

$x_{2n+3} = \frac{1}{2$ + $x_{2n+2}} = \frac{1}{2$ + $\frac{1}{2$ + $\cdots}} = \frac{2$ + $x_{2n+1}}{5$ + $2x_{2n+1}}$.

$x_{2n+3} < x_{2n+1} \Leftrightarrow 2x_{2n+1}^2$ + $4x_{2n+1}$ - 2 $>$ 0 $\Leftrightarrow x_{2n+1} >$ -1 + $\sqrt{2}$ hoặc $x_{2n+1} <$ -1 - $\sqrt{2}$

Điều này luôn đúng, vì ta đã chứng minh ở trên, rằng dãy các số hạng lẻ thỏa mãn

$x_{2n+1} >$ -1 + $\sqrt{2}$.

Dãy số này giảm và bị chặn dưới, nên tồn tại giới hạn $\lim_{n\to+\infty} x_{2n+1} =$ b. Phương trình

$x_{2n+3} = \frac{2+x_{2n+1}}{5+2x_{2n+1}}$ dẫn đến b $= \frac{2+b}{5+2b} \Rightarrow$ b $=$ -1 + $\sqrt{2}$.

Kết luận: $\lim_{n \to +\infty} x_n =$ -1 + $\sqrt{2}$.



Bài tập 1.25. Dùng tiêu chuẩn Cauchy chứng minh rằng dãy số $u_n =$ 1 + $\frac{1}{2}$ + $\cdots$ + $\frac{1}{n}$

phân kì.

Bài tập 1.26. Chứng minh rằng nếu $\lim_{n\to+\infty} a_n =$ a thì $\lim_{n\to+\infty} \frac{a_1$ + $a_2$ + $\cdots$ + $a_n}{n} =$ a.

Bài tập 1.27. Chứng minh rằng nếu $\lim_{n\to+\infty} a_n =$ a, $a_n >$ 0 $\forall$ n thì $\lim_{n\to+\infty} \sqrt[n]{a_1 a_2 \dots a_n} =$ a.



$\S$ 5. $\ \textbf{GI\^OI} \ \textbf{HAN} \ \textbf{H\^A} \ \textbf{S\^O}$

## 5.1 Đinh nghĩa <math display="block">\S 5. \ \textbf{GI\^OI} \ \textbf{HAN} \ \textbf{H\^A} \ \textbf{S\^O}</math>

Định nghĩa 1.9. Giả sử rằng hàm số f(x) được xác định tại mọi điểm x $\in$ (a, b) $\setminus \{x_0\}$. Ta

nói giới hạn của hàm số f(x) khi x tiến đến $x_0$ bằng L và viết

$\n\lim_{x \to x_0}$ f(x) $= L\n$

• (nói một cách nôm na) nếu ta có thể làm cho giá trị của hàm số f(x) gần L với một

giá trị tùy ý bằng cách chọn x đủ gần $x_0$.

• (nói một cách chính xác) nếu với mọi $\epsilon >$ 0, tồn tại số thực $\delta >$ 0 sao cho

$\|\hat{u}x$ - $x_0\| < \delta \text{thi}$ |f(x) - L| $< \epsilon$.

Hình dung rằng $\lim_{x\to x_0}f(x)=Lnghĩa$ là với $mọi\epsilon>0,tồn$ tại $số\delta>0sao$ cho đồ thị của

hàm số trong khoảng $(x_0$ - $\delta$, $x_0$ + $\delta)$ sẽ nằm hoàn toàn trong dải (L - $\epsilon$, L + $\epsilon)$.

$L+\epsilon$

$-L-\epsilon$

$x_0 \\$

$\chi_{\parallel}$

$\mathcal{O}$

Hình 1.9

Các giới hạn một phía $\lim_{x\to x_0^+} =$ L, $\lim_{x\to x_0^-} =$ L và giới hạn $\lim_{x\to\infty}$ f(x) $=$ L được định nghĩa một

cách tương tự.

### Định lý 1.7 (Tính duy nhất của giới hạn). <i>Giới hạn của hàm số</i> <math>\lim_{x\to x_0} f(x)</math>, nếu tồn tại,

là duy nhất.

## 5.2 Các phép toán trên giới han là duy nhất.

### Định lý 1.8 (Các phép toán trên giới hạn). <i>Giả sử</i> <math>\lim_{x\to x_0} f(x) = a</math>, <math>\lim_{x\to x_0} g(x) = b</math>, <i>ở đó</i>

a, b là các số thực hữu hạn. Khi đó,

• Tống: $\lim_{x \to x_0}$ [f(x) + g(x)] $=$ a + b,



• Hiệu: $\lim_{x \to x_0}$ [f(x) - g(x)] $=$ a - b,

• Tích: $\lim_{x\to x_0}[f(x)g(x)] =$ ab,

• Thương: $\lim_{x\to x_0} \frac{f(x)}{g(x)} = \frac{a}{b}$, nếu b $\neq$ 0.

Chú ý 1.5. Các phép toán trên giới hạn sau không thực hiện được, chúng còn được gọi là

các dạng vô định:

$\infty$ - $\infty$, 0 $\times \infty$, $\frac{\infty}{\infty}$, $\frac{0}{0}$.

## 5.3 Giới han của hàm hợp <math>\infty - \infty, 0 \times \infty, \frac{\infty}{\infty}, \frac{0}{0}.</math>

Nếu có $\lim_{x\to x_0}$ u(x) $= u_0$, $\lim_{u\to u_0}$ f(u) $= f(u_0)$ và có hàm hợp f(u(x)) thì

$\n\lim_{x \to x_0}$ f(u(x)) $= f(u_0).\n$

Áp dụng $\lim_{x\to x_0} A(x)^{B(x)} = e^{\lim_{x\to x_0}$ B(x) $\ln A(x)}$.

## 5.4 Giới han vô cùng Áp dụng <math>\lim_{x\to x_0} A(x)^{B(x)} = e^{\lim_{x\to x_0} B(x) \ln A(x)}</math>.

Định nghĩa 1.10. Giả sử rằng hàm số f(x) được xác định tại mọi điểm x $\in$ (a, b) $\setminus \{x_0\}$.

Ta nói giới hạn của hàm số f(x) khi x tiến đến $x_0$ bằng vô cùng và viết

$\n\lim_{x \to x_0}$ f(x) $= \infty\n$

nếu với mọi số M $>$ 0, tồn tại số thực $\delta >$ 0 sao cho

$n\hat{e}u$ |x - $x_0| < \delta$ thi |f(x)| $>$ M.

Các giới hạn một phía $\lim_{x\to x_0^+} = \infty$, $\lim_{x\to x_0^-} = \infty$ và giới hạn $\lim_{x\to\infty}$ f(x) $= \infty$ được định nghĩa một

cách tương tự.

## 5.5 Các tiêu chuẩn tồn tại giới hạn cách tương tự.

Định lý 1.9. Nếu f(x) $\le$ g(x) với mọi x trong một lân cận nào đó của a, và tồn tại các giới

hạn $\lim_{x\to a}$ f(x), $\lim_{x\to a}$ g(x) thì

$\n\lim_{x \to a}$ f(x) $\le \lim_{x \to a} g(x).\n$

Hệ quả 1.1 (Tiêu chuẩn kẹp). Nếu f(x) $\le$ g(x) $\le$ h(x) trong một lân cận nào đó của a,

và tồn tại các giới hạn $\lim_{x\to a}$ f(x) $= \lim_{x\to a}$ h(x). Khi đó tồn tại $\lim_{x\to a}$ g(x), và

$\n\lim_{x \to a}$ f(x) $= \lim_{x \to a} g(x).\n$



## 5.6 Mối liên hệ giữa giới hạn của dãy số và giới han None

của hàm số

Nhiều bài toán giới hạn của dãy số có thể được chuyển về giới hạn của hàm số và lợi

dụng các công cụ của giới hạn của hàm số để tính toán một cách dễ dàng. Chúng thể hiện

qua mối liên hê sau.

Định lý 1.10. $\lim_{x\to x_0}$ f(x) $=$ L khi và chỉ khi với mọi dãy số $\{x_n\}$ sao cho $\lim_{n\to+\infty} x_n = x_0$ thì

$\lim_{n\to+\infty} f(x_n) =$ L, ở đó (chỉ riêng trong Định lý này) $x_0$ và L có thể là một số thực hữu hạn

hoặc bằng vô cùng.

Chẳng hạn như, muốn chứng minh $\lim_{n \to +\infty} \frac{\ln n}{n} =$ 0 ta có thể đưa về $\lim_{x \to \infty} \frac{\ln x}{x} =$ 0.

## 5.7 Bài tâp Chẳng hạn như, muốn chứng minh <math>\lim_{n \to +\infty} \frac{\ln n}{n} = 0</math> ta có thể đưa về <math>\lim_{x \to \infty} \frac{\ln x}{x} = 0</math>.

Bài tập 1.28. Tính

a) $\lim_{x \to 1} \frac{x^{100}$ - 2x + $1}{x^{50}$ - 2x + $1} \left(\frac{0}{0}\right)$

b) $\lim_{x \to a} \frac{(x^n$ - $a^n)$ - $na^{n-1}(x$ - $a)}{(x$ - $a)^2} \left(\frac{0}{0}\right)$

Phương pháp phân tích đa thức thành nhân tử. Nếu $P_n(x_0) = Q_m(x_0) =$ 0 thì

$\n\lim_{x \to x_0} \frac{P_n(x)}{O_m(x)} = \lim_{x \to x_0} \frac{(x$ - $x_0) \cdot P_{n-1}(x)}{(x$ - $x_0) \cdot O_{m-1}(x)} = \lim_{x \to x_0} \frac{P_{n-1}(x)}{O_{m-1}(x)}.\n$

$[\text{Đáp}\text{ s\^0}]$

a) $\frac{49}{24}$

b) $\frac{n(n-1)}{2}a^{n-2}$

Bài tập 1.29. Tìm giới hạn

b) $\lim_{x \to +\infty} (\sqrt[3]{x^3$ + $x^2$ - $1}$ - x) $(\infty$ - $\infty)$.

a) $\lim_{x \to +\infty} \frac{\sqrt{x$ + $\sqrt{x$ + $\sqrt{x}}}}{\sqrt{x$ + $1}} \left(\frac{\infty}{\sim}\right)$.

Chứng minh. a) Chia cả tử và mẫu cho $\sqrt{x}$ ta được

$\n\lim_{x \to +\infty} \frac{\sqrt{x$ + $\sqrt{x$ + $\sqrt{x}}}}{\sqrt{x$ + $1}} = \lim_{x \to \infty} \frac{\sqrt{1$ + $\sqrt{1/x$ + $\sqrt{1/x^3}}}}{\sqrt{1$ + $1/x}} = 1.\n$

b) Sử dụng phương pháp nhân liên hợp ta được

$\n\lim_{x \to +\infty} (\sqrt[3]{x^3$ + $x^2$ - $1}$ - x) $= \lim_{x \to \infty} \frac{x^2$ - $1}{\sqrt[3]{(x^3$ + $x^2$ - $1)^2}$ + $x\sqrt[3]{x^3$ + $x^2$ - $1}$ + $x^2} = \frac{1}{3}.\n$



§6. VÔ CÙNG LỚN, VÔ CÙNG BÉ

## 6.1 Vô cùng bé (VCB) §6. VÔ CÙNG LỚN, VÔ CÙNG BÉ

Định nghĩa 1.11. Hàm số f(x) được gọi là một vô cùng bé (viết tắt là VCB) khi x $\rightarrow$ a

$n\hat{e}u$

$\n\lim_{x \to a}$ f(x) $= 0.\n$

Mối liên hệ giữa giới hạn và VCB

$\n\lim_{x \to a}$ f(x) $= \ell \Longleftrightarrow$ f(x) $= \ell$ + $\alpha(x);\n$

trong đó $\alpha(x)$ là một VCB trong quá trình x $\rightarrow$ a.

Môt số tính chất của VCB

1. Tổng hai VCB (đối với một VCB người ta không quan tâm đến dấu của nó) là một

VCB.

2. Tích của VCB với một đại lượng bị chặn là một VCB.

3. Tích các VCB là một VCB.

Chú ý: Thương của hai VCB là một dạng vô định $\frac{0}{0}$.

So sánh các VCB

### Định nghĩa 1.12 (VCB cùng bậc, tương đương). Giả sử <math>\alpha(x)</math> và <math>\beta(x)</math> là các VCB khi

x $\rightarrow$ a.

i) Nếu $\lim_{x \to a} \frac{\alpha(x)}{\beta(x)} =$ A $\neq$ 0, ta nói rằng $\alpha(x)$, $\beta(x)$ là các VCB cùng bậc.

ii) Đặc biệt, nếu $\lim_{x\to a} \frac{\alpha(x)}{\beta(x)} =$ 1 thì ta nói $\alpha(x)$ và $\beta(x)$ là các VCB tương đương và viết

$\alpha(x) \sim \beta(x)$.

Môt số VCB tương đương hay dùng trong quá trình x $\rightarrow$ 0

• x $\sim \sin$ x $\sim \tan$ x $\sim \arcsin$ x $\sim \arctan$ x $\sim e^x$ - 1 $\sim \frac{a^x$ - $1}{\ln a} \sim \ln(1$ + x),

• $(1+x)^a$ - 1 $\sim$ ax. Đặc biệt, $\sqrt[m]{1$ + $\alpha x}$ - 1 $\sim \frac{\alpha x}{m}$,



• 1 - $\cos$ x $\sim \frac{x^2}{2}$.

### Định nghĩa 1.13 (VCB bậc cao). Nếu <math>\lim_{x\to a} \frac{\alpha(x)}{\beta(x)} = 0</math>, ta nói rằng <math>\alpha(x)</math> là VCB bậc cao hơn

$\beta(x)$ và kí hiệu $\alpha(x) = o(\beta(x))$.

Định lý 1.11.

a) Hiệu hai VCB tương đương là một VCB bậc cao hơn VCB đó.

b) Tích hai VCB là một VCB bậc cao hơn cả hai VCB đó.

Ứng dụng của VCB để tìm giới hạn

### Định lý 1.12 (Quy tắc thay tương đương). <i>Nếu</i> <math>\alpha_1(x) \sim \alpha_2(x)</math>, <math>\beta_1(x) \sim \beta_2(x)</math> khi <math>x \to a</math>

thì

$\n\lim_{x \to a} \frac{\alpha_1(x)}{\beta_1(x)} = \lim_{x \to a} \frac{\alpha_2(x)}{\beta_2(x)}$, $\quad \lim_{x \to a} \alpha_1(x)\gamma(x) = \lim_{x \to a} \alpha_2(x)\gamma(x).\n$

### Định lý 1.13 (Quy tắc ngắt bỏ VCB bậc cao). Nếu <math>\alpha_1(x) = o(\alpha_2(x))</math>, <math>\beta_1(x) = o(\beta_2(x))</math>

khi x $\rightarrow$ a thì

$\alpha_1(x)$ + $\alpha_2(x) \sim \alpha_2(x)$ và $\lim_{x \to a} \frac{\alpha_1(x)$ + $\alpha_2(x)}{\beta_1(x)$ + $\beta_2(x)} = \lim_{x \to a} \frac{\alpha_2(x)}{\beta_2(x)}$.

Chú ý 1.6. Sai lầm hay mắc: Thay tương đương khi có hiệu hai VCB. Chẳng hạn như, với

VCB $\alpha(x) = \sin$ x - $\tan$ x + $x^3$ khi x $\rightarrow$ 0 ta có

ii) Thực tế, $\alpha(x) \sim \frac{x^3}{2}$.

i) Thay tương đương $\alpha(x) \sim x^3$,

Thật vậy,

$\lim_{x\to 0} \frac{\sin$ x - $\tan$ x + $x^3}{x^3} =$ 1 + $\lim_{x\to 0} \frac{\sin$ x $\left(1$ - $\frac{1}{\cos x}\right)}{x^3} =$ 1 + $\lim_{x\to 0} \frac{-\sin$ x (1 - $\cos x)}{x^3 \cos x} = \frac{1}{2}$.

Ví du 6.1 (Giữa kì, K61). So sánh cặp vô cùng bé sau đây khi x $\rightarrow$ 0

a) $\alpha(x) = \sqrt[3]{x^2$ + $x^3}$, $\beta(x) = e^{\sin x}$ - 1.

b) $\alpha(x) = \sqrt[5]{x^4$ + $x^5}$, $\beta(x) = e^{\tan x}$ - 1.

c) $\alpha(x) = \sqrt[5]{x^4$ - $x^5}$, $\beta(x) = \ln(1$ + $\tan$ x).

d) $\alpha(x) = \sqrt[3]{x^2$ - $x^3}$, $\beta(x) = \ln(1$ + $\sin$ x).

e) $\alpha(x) = e^{\sqrt{x}}$ - 1, $\beta(x) = \sqrt{x$ + $x^2}$.

f) $\alpha(x) = e^{x^2}$ - 1, $\beta(x) = x^2$ + $x^3$.



6.2 Vô cùng lớn (VCL)

Định nghĩa 1.14. Hàm số f(x) được gọi là một vô cùng lớn (viết tắt là VCL) khi x $\rightarrow$ a

$n\hat{e}u$

$\n\lim_{x \to a}$ |f(x)| $= \infty.\n$

Nghich đảo của một VCB là một VCL, và ngược lại.

So sánh các VCL

### Định nghĩa 1.15 (VCL cùng bậc, tương đương). Giả sử <math>\alpha(x)</math> và <math>\beta(x)</math> là các VCL khi

x $\rightarrow$ a.

i) Nếu $\lim_{x\to a} \frac{\alpha(x)}{\beta(x)} =$ A $\neq$ 0, ta nói rằng $\alpha(x)$, $\beta(x)$ là các VCL cùng bậc.

ii) Đặc biệt, nếu $\lim_{x\to a} \frac{\alpha(x)}{\beta(x)} =$ 1 thì ta nói $\alpha(x)$ và $\beta(x)$ là các VCL tương đương và viết

$\alpha(x) \sim \beta(x)$.

Định nghĩa 1.16 (VCL bậc cao). Nếu $\lim_{x\to a} \frac{\alpha(x)}{\beta(x)} = \infty$, ta nói rằng $\alpha(x)$ là VCL bậc cao hơn

$\beta(x)$.

Ứng dụng VCL khử dạng $\left(\frac{\infty}{\infty}\right)$

Định lý 1.14 (Quy tắc thay tương đương). Nếu $\alpha_1(x) \sim \alpha_2(x)$, $\beta_1(x) \sim \beta_2(x)$ là các

VCL khi x $\rightarrow$ a thì

$\n\lim_{x \to a} \frac{\alpha_1(x)}{\beta_1(x)} = \lim_{x \to a} \frac{\alpha_2(x)}{\beta_2(x)}$, $\quad \lim_{x \to a} \alpha_1(x) \gamma(x) = \lim_{x \to a} \alpha_2(x) \gamma(x).\n$

Đinh lý 1.15 (Quy tắc ngắt bỏ VCL bậc thấp). Nếu $\alpha_1(x)$ là VCL bậc cao hơn $\alpha_2(x)$ và

$\beta_1(x)$ là VCL bậc cao hơn $\beta_2(x)$ khi x $\rightarrow$ a thì

$\alpha_1(x)$ + $\alpha_2(x) \sim \alpha_1(x)$ và $\lim_{x \to a} \frac{\alpha_1(x)$ + $\alpha_2(x)}{\beta_1(x)$ + $\beta_2(x)} = \lim_{x \to a} \frac{\alpha_1(x)}{\beta_1(x)}$.

Chú ý 1.7. Còn tồn đọng một số dạng vô định mà phương pháp sử dụng các VCB-VCL

chua xử lý được, ví du

$\n\lim_{x\to 0}\frac{x-\sin x}{x^3},\quad \lim_{x\to 0^+}x^{\sin x},\ldots\n$

Các giới hạn này sẽ được xử lý khi chúng ta học đến công thức L'Hospital và khai triển

Maclaurin.

Ví dụ 6.2 (Giữa kì, K61). Tính giới hạn



a) $\lim_{x\to 0^+} \frac{e^{x^2}-1}{x^2+x^3}$.

c) $\lim_{x\to 0} \frac{1-\cos x}{\ln(1+x^2)}$.

b) $\lim_{x\to 0^+} \frac{e^{\sqrt{x}}-1}{\sqrt{x+x^2}}$.

d) $\lim_{x\to 0} \frac{e^{2x}-1}{\ln(1-3x)}$.

## 6.3 Bài tập <i>d</i>) <math display="block">\lim_{x\to 0} \frac{e^{2x}-1}{\ln(1-3x)}</math>.

Như vậy ngoài các phương pháp phân tích đa thức thành nhân tử và nhân liên

hợp đã trình bày ở trên, bài học hôm nay cung cấp cho chúng ta một công cụ mới để tìm

giới hạn, đó là các quy tắc thay tương đương và ngắt bỏ các VCB bậc cao. Đây có lẽ là một

trong những công cụ rất tốt của Giải tích để tính giới hạn.

Bài tập 1.30. Tìm giới hạn

b. $\lim_{x \to 0} \frac{\sqrt[n]{1$ + $\alpha x} \cdot \sqrt[n]{1$ + $\beta$ x - $1}}{x} \left( \frac{0}{0} \right)$

a. $\lim_{x\to 0} \frac{\sqrt[m]{1+\alpha x}$ - $\sqrt[n]{1+\beta x}}{x} \left(\frac{0}{0}\right)$

Chứng minh.

a.

$\frac{\sqrt[m]{1+\alpha x}$ - $\sqrt[n]{1+\beta x}}{\sqrt[m]{1+\alpha x}$ - $1} = \frac{\sqrt[m]{1+\alpha x}$ - $1}{\sqrt[n]{1+\beta x}$ - $1}$

Vì $\sqrt[m]{1+\alpha x}-1 \sim \frac{\alpha}{m}x$, $\sqrt[n]{1+\beta x}-1 \sim \frac{\beta}{n}x$, nên

$\n\lim_{x\to 0}\frac{\sqrt[m]{1+\alpha x}-\sqrt[n]{1+\beta x}}{x}=\frac{\alpha}{m}-\frac{\beta}{n}\n$

$\mathbf{b}$.

$\n\lim_{x\to 0}\frac{\sqrt[m]{1+\alpha x}.\sqrt[n]{1+\beta x-1}}{x}=\lim_{x\to 0}\left(\sqrt[m]{1+\alpha x}.\frac{\sqrt[n]{1+\beta x}-1}{x}+\frac{\sqrt[m]{1+\alpha x}-1}{x}\right)=\frac{\alpha}{m}+\frac{\beta}{n}.\n$

Chú ý 1.8.

i) Lưu ý kĩ thuật thêm bớt 1 ở trong các biểu thức có chứa cos $\alpha(x)$, $e^{\alpha(x)}$ và $\ln(\alpha(x))$, $\sqrt[m]{1$ + $\alpha(x)}$.

ii) Với nhiều bài toán nhìn qua tưởng rất phức tạp vì công thức rất cồng kềnh, thực chất

nếu dùng quy tắc thay tương đương và ngắt bỏ các VCB bậc cao thì sẽ thấy rất đơn

giản. Ví dụ, tính

$\lim_{x \to 0} \frac{\sin$ 2x + $\arcsin^2$ x - $\arctan^2 x}{3x}$.

Với tử số ta có sin 2x ~ 2x, $arcsin<sup>2</sup>$ x ~ $x<sup>2</sup>$, $arctan<sup>2</sup>$ x ~ $x<sup>2</sup>$. Như vậy giới hạn đã cho

bằng $\frac{2}{3}$. Hoặc ví dụ như tính

$\lim_{x \to 0} \frac{1$ - $\cos$ x + $2\sin$ x - $\sin^3$ x - $x^2$ + $3x^4}{\tan^3$ x - $6\sin^2$ x + x - $5x^3}$.



Trông biểu thức này rất phức tạp nhưng thực chất chúng ta có thể nhìn thấy ngay

giới hạn này bằng $\lim_{x\to 0} \frac{2\sin x}{x} =$ 2 với nhận xét là $2\sin$ x $\sim$ 2x là VCB bậc thấp nhất ở

tử số và x là VCB bậc thấp nhất ở mẫu số.

Bài tập 1.31. Tìm giới hạn

a) $\lim_{x \to a} \frac{\sin$ x - $\sin a}{x$ - $a} \left(\frac{0}{0}\right)$

c) $\lim_{x \to 0} \frac{\sqrt{\cos x}$ - $\sqrt[3]{\cos x}}{\sin^2 x} \left(\frac{0}{0}\right)$

d) $\lim_{x \to 0} \frac{1$ - $\cos$ x $\cos$ 2x $\cos 3x}{1$ - $\cos x} \left(\frac{0}{0}\right)$.

b) $\lim_{x \to +\infty} (\sin \sqrt{x+1}$ - $\sin \sqrt{x})$

$[\text{Đáp}\text{ số}]$

b) 0

d) 14

a) $\cos$ a

c) $\frac{1}{12}$

Bài tập 1.32. Tìm giới han

c) $\lim_{x \to \infty} [\sin(\ln(x+1))$ - $\sin(\ln$ x)]

a) $\lim_{x \to \infty} \left( \frac{x^2$ - $1}{x^2$ + $1} \right)^{\frac{x$ - $1}{x$ + $1}}$

b) $\lim_{x \to 0^+} (\cos \sqrt{x})^{\frac{1}{x}} (1^{\infty})$

d) $\lim_{n\to\infty} n^2(\sqrt[n]{x}$ - $\sqrt[n+1]{x})$, x $>$ 0.

Chứng minh. a) Đây không phải là dạng vô định, $\lim_{x\to\infty} \left(\frac{x^2-1}{x^2+1}\right)^{\frac{x-1}{x+1}} =$ 1.

b) Áp dụng công thức $\left| \lim_{x \to x_0} A(x)^{B(x)} \right| = e^{\lim_{x \to x_0}$ B(x) $\ln A(x)}$. Vì

$\lim_{x \to 0^+} \ln \left( \cos \sqrt{x} \right)^{\frac{1}{x}} = \lim_{x \to 0^+} \frac{\ln \cos \sqrt{x}}{x} = \lim_{x \to 0^+} \frac{-\sin \sqrt{x}}{2\sqrt{x}} = -\frac{1}{2}$

nên

$\lim_{x \to 0^+} \ln \left( \cos \sqrt{x} \right)^{\frac{1}{x}} = e^{-\frac{1}{2}}$.

c) Đáp số: 0.



d)

$\lim_{n\to\infty} n^2(\sqrt[n]{x}$ - $\sqrt[n+1]{x})$, x $>$ 0

$= \lim_{n \to \infty} n^2 (x^{\frac{1}{n}}$ - $x^{\frac{1}{n+1}})$

$= \lim_{n \to \infty} n^2 x^{\frac{1}{n+1}} \left( x^{\frac{1}{n(n+1)}}$ - 1 $\right)$

$= \lim_{n \to \infty} n^2 x^{\frac{1}{n+1}} \cdot \frac{x^{\frac{1}{n(n+1)}}$ - $1}{\frac{1}{n(n+1)}} \cdot \frac{1}{n(n+1)}$

$\qquad \qquad \blacksquare$

$= \lim_{n \to \infty} \frac{n}{n+1} x^{\frac{1}{n+1}} \frac{x^{\frac{1}{n(n+1)}}$ - $1}{1}$

$\frac{\overline{n(n+1)}}{n(n+1)}$

$=$ ln x

So sánh các VCB-VCL.

Chú ý 1.9.

i) So sánh 2 VCB: Nếu $\lim_{x\to a} \frac{\alpha(x)}{\beta(x)} =$ 0 thì ta nói $\alpha(x)$ là VCB bậc cao hơn $\beta(x)$, nhưng

ii) So sánh 2 VCL: Nếu $\lim_{x\to a} \frac{\alpha(x)}{\beta(x)} = \infty$ thì ta nói $\alpha(x)$ là VCL bậc cao hơn $\beta(x)$.

iii) Cùng một biểu thức $\alpha(x) = \sqrt{x}$ + $\sqrt{x}$ chẳng hạn, thì nếu trong quá trình x $\to 0^+$

thì nó là VCB nên theo quy tắc ngắt bỏ VCB bậc cao, $\alpha(x) \sim \sqrt{\sqrt{x}} = x^{1/4}$, còn nếu

xét trong quá trình x $\rightarrow \infty$ thì nó là VCL nên theo quy tắc ngắt bỏ VCL bậc thấp,

$\alpha(x) \sim \sqrt{x}$.

Bài tập 1.33. Khi $x\rightarrow$ 0 cặp VCB sau có tương đương không ?

$\alpha(x) = \sqrt{x$ + $\sqrt{x}} \text{$ và $} \beta(x) = e^{\sin x}$ - $\cos$ x

[Đáp số] $\beta(x) = o(\alpha(x))$

Bài tập 1.34. Tìm giới hạn

a) $\lim_{x\to 0^+} (1-2x)^{\frac{1}{x}} (1^{\infty})$,

c) $\lim_{x\to 0} \left(\frac{1+\tan x}{1+\sin x}\right)^{\frac{1}{\sin x}} (1^{\infty})$,

d) $\lim_{x\to 0} \left(\frac{\sin x}{x}\right)^{\frac{\sin x}{x-\sin x}} (1^{\infty})$,

b) $\lim_{x \to \frac{\pi}{2}} (\sin x)^{\tan x} (1^{\infty})$,



[Gợi ý] Áp dụng $\left| \lim_{x \to x_0} A(x)^{B(x)} \right| = e^{\lim_{x \to x_0}$ B(x) $\ln A(x)}$

$[\text{Đáp}\ \text{s}\text{\^{o}}]$

a) $e^{-2}$

b) 1

d) e

c) 1

Bài tập 1.35. Tìm giới hạn

a) $\lim_{x\to 0} \frac{e^{\alpha x}$ - $e^{\beta x}}{x} \left(\frac{0}{0}\right)$, b) $\lim_{x\to 0} \frac{e^{\alpha x}$ - $e^{\beta x}}{\sin \alpha$ x - $\sin \beta x} \left(\frac{0}{0}\right)$, c) $\lim_{x\to a} \frac{a^x$ - $x^a}{x$ - $a} \left(\frac{0}{0}\right)$.

[Gợi $\acute{y}]$ Sử dụng phương pháp thay tương đương.

$[\text{Đáp}\ \text{s}\hat{\text{o}}]$

a) $\alpha$ - $\beta$

b) 1

c) $a^a(\ln$ a - 1)



$\S7$. HÀM SỐ LIÊN TỤC

## 7.1 Đinh nghĩa <math>\S</math><b>7. HÀM SỐ LIÊN TỤC</b>

Định nghĩa 1.17. Cho hàm số f(x) xác định trong một lân cận nào đó của $x_0$. Nó được

gọi là

i) liên tục phải tại $x_0$ nếu $\lim_{x \to x_0^+} f(x_0)$,

ii) liên tục trái tại $x_0$ nếu $\lim_{x\to x_0^-} f(x_0)$,

iii) liên tục tại $x_0$ nếu $\lim_{x\to x_0} = f(x_0)$. Nói cách khác,

$\forall \varepsilon >$ 0, $\exists \delta(\varepsilon$, $x_0) >$ 0 : $\forall$ x, |x - $x_0| < \delta$ ta có|f(x) - $f(x_0)| < \varepsilon$.

Từ định nghĩa suy ra hàm số f(x) liên tục tại $x_0$ khi và chỉ khi nó liên tục phải và liên tục

trái tại $x_0$.

Ví dụ 7.1. Tất cả các hàm số sơ cấp đều liên tục trên tập xác định của chúng.

Ví du 7.2 (Giữa kì, K61). Tìm m để hàm số sau liên tục tại x $=$ 1:

$ a) f(x) = \begin{cases} (x - m)(x^2 + x + 1), & \text{n\'{e}}u \ x \neq 1, \\ 1 + m, & \text{n\'{e}}u \ x = 1. \end{cases} $

$ b) f(x) = \begin{cases} (x+m)(x^2+x+1), & n \neq 1, \\ 1-m, & n \neq 1. \end{cases} $

Định nghĩa 1.18. Hàm số f(x) được gọi là liên tục trên khoảng (a, b) nếu nó liên tục tại

mọi điểm $x_0 \in$ (a, b). Nó được gọi là liên tục trên đoạn [a, b] nếu nó liên tục tại mọi điểm

$x_0 \in$ (a,b), đồng thời liên tục phải tại a và liên tục trái tại b.

## 7.2 Các phép toán số học đối với hàm số liên tục <math>x_0 \in (a,b)</math>, đồng thời liên tục phải tại a và liên tục trái tại b.

Định lý 1.16. Giả thiết các hàm số f(x) và g(x) liên tục tại $x_0$ nào đó. Khi đó các hàm số

f(x) $\pm$ g(x), f(x)g(x) cũng liên tục tại $x_0$. Hàm số $\frac{f(x)}{g(x)}$ cũng liên tục tại $x_0$ nếu $g(x_0) \neq$ 0.

Điều tương tự cũng đúng đối với các hàm số liên tục trái (phải) tại $x_0$.



## 7.3 Sự liên tục của hàm ngược None

Định lý 1.17. (Sự liên tục của hàm ngược)

Nếu X là một khoảng, y $=$ f(x) đồng biến (nghịch biến) liên tục trên X. Khi đó có hàm

ngược y $=$ g(x) cũng đồng biến (nghịch biến) và liên tục trên f(X).

Ví du: Các hàm số lượng giác ngược là liên tục trên tập xác định của chúng.

## 7.4 Sự liên tục của hàm hợp <b>Ví du</b>: Các hàm số lượng giác ngược là liên tục trên tập xác định của chúng.

Định lý 1.18. Nếu hàm số f(x) liên tục tại b và $\lim_{x\to a}$ g(x) $=$ b thì $\lim_{x\to a}$ f(g(x)) $=$ b. Nói cách

khác,

$\n\lim_{x \to a}$ f(g(x)) $= f(\lim_{x \to a} g(x))\n$

Hệ quả 1.2. Nếu g(x) liên tục tại a và f(x) liên tục tại g(a) thì hàm số f $\circ$ g liên tục tại a.

## 7.5 Các định lý về hàm liên tục <b>Hệ quả 1.2.</b> <i>Nếu</i> <math>g(x)</math> <i>liên tục tại a và</i> <math>f(x)</math> <i>liên tục tại</i> <math>g(a)</math> <i>thì hàm số</i> <math>f \circ g</math> <i>liên tục tại a.</i>

Đinh lý 1.19. Nếu f(x) liên tục trên khoảng (a,b) mà giá trị $f(x_0)$, $x_0 \in$ (a,b) dương (hay

âm) thì tồn tại một lân cận $U(x_0)$ sao cho $\forall$ x $\in U(x_0)$, f(x) cũng dương hay âm. Hình ảnh

hình học.

Đinh lý 1.20. Nếu f(x) liên tục trên đoạn [a,b] thì nó bị chặn trên đoạn đó. Hình ảnh

hình hoc.

Định lý 1.21. Nếu f(x) liên tục trên đoạn [a, b] thì nó đạt được GTLN, NN trên đoạn này.

Hình ảnh hình học.

* Liên tục đều, hình ảnh hình học của liên tục đều.

Định lý 1.22. (Định lý Cantor)

Nếu f(x) liên tục trên [a, b] thì nó liên tục đều trên đó (thay [a, b] bằng khoảng (a, b) thì

định lý không còn đúng). Mô tả hình học.

Định lý 1.23. (Định lý Cauchy)

Nếu f(x) liên tục trên đoạn [a,b] và có f(a). f(b) $<$ 0 thì $\exists \alpha \in$ (a,b) để $f(\alpha) =$ 0.

Ví dụ 7.3 (Giữa kì, 20173). Cho hàm số f : [1,3] $\rightarrow$ [1,3] liên tục. Chứng minh rằng tồn

tai $x_0 \in$ [1,3] sao cho $f(x_0) = x_0$.



[Lời giải] Xét g(x) $=$ f(x) - x $\Rightarrow$ g(1) $=$ f(1) - 1 $\ge$ 0, g(3) $=$ f(3) - 3 $\le$ 0. Theo Định lý

Cauchy, phương trình g(x) $=$ 0 có nghiệm $x_0$ nào đó trong khoảng [1,3] $\Rightarrow f(x_0) = x_0$.

Hệ quả 1.3. Nếu f(x) liên tục trên đoạn [a,b], A $=$ f(a) $\neq$ B $=$ f(b) thì nó nhận mọi giá

tri trung gian giữa A và B.

Hệ quả 1.4. Cho f(x) liên tục trên [a, b], m, M lần lượt là các GTNN, LN của hàm số trên

đoạn này thì [m; M] là tập giá trị của hàm số.

## 7.6 Điểm gián đoạn và phân loại điểm gián đoạn của đoạn này thì <math>[m; M]</math> là tập giá trị của hàm số.

hàm số

Định nghĩa 1.19. Nếu hàm số không liên tục tại điểm $x_0$ thì ta nói nó gián đoạn tại $x_0$.

Hình ảnh hình học: đồ thị không liền nét tại điểm gián đoạn.

Theo định nghĩa, hàm số f(x) liên tục tại $x_0$ nếu ba điều kiện sau được thỏa mãn:

• f(x) xác định tại $x_0$,

• tồn tại $\lim_{x\to x_0}$ f(x),

$\bullet \lim_{x \to x_0}$ f(x) $= f(x_0)$.

Như vậy nếu $x_0$ là điểm gián đoạn của f(x) thì

• hoặc $x_0 \notin$ TXĐ,

• hoặc $x_0 \in \text{TXD}$ và $\exists \lim_{x \to x_0}$ f(x),

• hoặc $x_0 \in \text{TXD}$ và $\exists \lim_{x \to x_0}$ f(x) nhưng $\lim_{x \to x_0}$ f(x) $\neq f(x_0)$, ở đây x $\to x_0$ theo nghĩa cả

hai phía hay một phía.

Nếu $x_0 \notin$ TXĐ của f(x) thì có thể có rất nhiều điểm gián đoạn, nên ta chỉ quan tâm

đến những điểm gián đoạn thuộc tập xác định hay là những điểm đầu mút của khoảng

xác định.

Phân loại điểm gián đoạn

Giả sử $x_0$ là điểm gián đoạn của f(x).



1. Điểm gián đoạn loại 1:

Nếu $\exists \lim_{x \to x_0^+}$ f(x) $= f(x_0^+)$ và $\lim_{x \to x_0^-}$ f(x) $= f(x_0^-)$ thì $x_0$ được gọi là điểm gián đoạn

loại 1 của hàm số f(x). Khi đó, có thể xảy ra hai trường hợp:

• Nếu $f(x_0^+) \neq f(x_0^-)$ thì giá trị $|f(x_0^+)$ - $f(x_0^-)|$ gọi là bước nhảy của hàm số.

• Đặc biệt: nếu $f(x_0^+) = f(x_0^-)$ thì $x_0$ được gọi là điểm gián đoạn bỏ được của

hàm số. Khi đó nếu hàm số chưa xác định tại $x_0$ thì ta có thể bổ sung thêm giá

trị của hàm số tại $x_0$ để hàm số liên tục tại điểm $x_0$. Còn nếu hàm số xác định

tại điểm $x_0$ thì ta có thể thay đổi giá trị của hàm số tại điểm này để hàm số liên

tục tại $x_0$.

2. Điểm gián đoạn loại 2:

Nếu $x_0$ không là điểm gián đoạn loại 1 thì ta nói nó là điểm gián đoạn loại 2.

Chú ý 1.10. Với quan điểm xem điểm gián đoạn bỏ được là trường hợp đặc biệt của điểm

gián đoạn loại 1, nếu $x_0$ là điểm đầu mút của khoảng hay đoạn xác định của f(x), mà có

lim f(x) hoặc lim f(x) hữu hạn thì ta cũng xem $x_0$ là điểm gián đoạn bỏ được của hàm

x $\rightarrow x_0^+$

x $\rightarrow x_0^-$

$S\acute{\hat{O}}$.

Ví du 7.4 (Giữa kì, K61).

a) Điểm x $= \frac{\pi}{2}$ là điểm gián đoạn loại gì của hàm số f(x) $= \frac{1}{1-2^{\tan x}}$.

b) Điểm x $= -\frac{\pi}{2}$ là điểm gián đoạn loại gì của hàm số f(x) $= \frac{1}{1-2^{\tan x}}$.

Ví du 7.5 (Cuối kì, K61-Viện ĐTQT). Điểm x $=$ 0 là điểm gián đoạn loại gì của hàm số

a) y $= e^{\frac{\pi}{2}$ - $\arctan \frac{1}{x}}$.

b) y $= e^{\frac{\pi}{2}$ - $\operatorname{arccot} \frac{1}{x}}$.

## 7.7 Bài tập <b>b)</b> <math>y = e^{\frac{\pi}{2} - \operatorname{arccot} \frac{1}{x}}</math>.

Xét tính liên tục của hàm số. Muốn kiểm tra xem f(x) có liên tục tại $x_0$ hay không

chúng ta đi kiểm tra $\lim_{x\to x_0}$ f(x) có bằng $f(x_0)$ hay không? Đôi khi phải xét $\lim_{x\to x_0^+}$ f(x) và

lim f(x) nếu biểu thức của f(x) ở hai phía của $x_0$ được cho dưới các công thức khác nhau.

x $\rightarrow x_0^-$

Thậm chí cũng có khi biểu thức của f(x) ở hai phía của $x_0$ được cho cùng một công thức

nhưng giới hạn trái và giới hạn phải của f(x) tại $x_0$ vẫn khác nhau. Ví dụ, xét sự liên tục

$ của hàm số f(x) = \begin{cases} \frac{1}{1-2^{\cot x}}, & x \neq 0, \\ 1, & x = 0 \end{cases}. Hàm số này có \lim_{x \to 0^+} f(x) = 0 và \lim_{x \to 0^-} f(x) = 1 (tại $

sao?). Do đó nó liên tục trái tại 0 và không liên tục phải tại 0.

Bài tập 1.36. Tìm a để hàm số liên tục tại x $=$ 0



$ a) f(x) = \begin{cases} \frac{1-\cos x}{x}, & \text{n\'{e}u } x \neq 0 \\ a, & \text{n\'{e}u } x = 0. \end{cases} $

$ b) g(x) = \begin{cases} ax^2 + bx + 1, & \text{n\'{e}u } x \ge 0 \\ a \cos x + b \sin x, & \text{n\'{e}u } x < 0. \end{cases} $

$[\text{Đáp}\text{ số}]$

a) a $= \frac{1}{2}$

b) a $=$ 1

Bài tập 1.37. Điểm x $=$ 0 là điểm gián đoạn loại gì của hàm số

a) y $= \frac{8}{1$ - $2^{\cot x}}$, b) y $= \frac{\sin \frac{1}{x}}{\frac{1}{1$ - $1}}$,

c) y $= \frac{e^{ax}$ - $e^{bx}}{x}$ (a $\neq$ b).

$[\text{Đáp}\text{ s}\hat{\text{o}}]$

c) $B<sub>o</sub>$ duoc

a) Loai I

b) Loai II

Bài tập 1.38. Xét sự liên tục của các hàm số sau

$ a) f(x) = \begin{cases} x \sin \frac{1}{x}, & \text{n\'{e}u } x \neq 0 \\ 0, & \text{n\'{e}u } x = 0 \end{cases} $

$ c) f(x) = \begin{cases} \sin \pi x, & \text{néu x vô ti} \\ 0, & \text{néu x hŭu ti} \end{cases} $

$ b) f(x) = \begin{cases} e^{-\frac{1}{x^2}}, & \text{n\'{e}u } x \neq 0 \\ 0, & \text{n\'{e}u } x = 0 \end{cases} $

$[\text{Đáp}\text{ s}\hat{\text{o}}]$

a) liên tuc

b) liên tuc

c) gián đoạn

Bài tập 1.39. Chứng minh rằng nếu f, g là các hàm số liên tục trên đoạn [a, b] và f(x) $=$

g(x) với mọi x là số hữu tỉ trong đoạn [a, b] thì f(x) $=$ g(x) $\forall$ x $\in$ [a, b].

Bài tập 1.40. Chứng minh rằng phương trình $x^5$ - 3x - 1 có ít nhất một nghiệm trong

khoảng (1,2).

Bài tập 1.41. Cho f(x) $= ax^2$ + bx + c, biết 2a + 3b + 6c $=$ 0. Chứng minh rằng f(x) có ít

nhất một nghiệm trong khoảng (0, 1).

Bài tập 1.42. Chứng minh rằng nếu f : [0,1] $\rightarrow$ [0,1] liên tục thì tồn tại $x_0 \in$ [0,1] sao cho

$f(x_0) = x_0$.

Bài tập 1.43. Chứng minh rằng mọi đa thức bậc lẻ với hệ số thực đều có ít nhất một

nghiêm thực.



$\S8$. ĐAO HÀM VÀ VI PHÂN

## 8.1 Đinh nghĩa <math>\S</math><b>8.</b> <b>Đ</b>AO HÀM VÀ VI PHÂN

Đinh nghĩa 1.20. Giới hạn, nếu có, của tỉ số

$\lim_{\Delta$ x $\to 0} \frac{f(x_0$ + $\Delta$ x) - $f(x_0)}{\Delta x}$

được gọi là đạo hàm của hàm số f(x) tại $x_0$ và được kí hiệu là $f'(x_0)$. Khi đó ta nói hàm số

f(x) có đạo hàm tại $x_0$.

Nếu quá trình $\Delta$ x $\rightarrow$ 0 trong định nghĩa trên được thay bằng

• $\Delta$ x $\rightarrow 0^+$ thì giới hạn đó được gọi là đạo hàm phải của hàm số f(x) tại $x_0$, kí hiệu là

$f'(x_0^+)$.

• $\Delta$ x $\rightarrow 0^-$ thì giới hạn đó được gọi là đạo hàm trái của hàm số f(x) tại $x_0$, kí hiệu là

$f'(x_0^-)$.

Đương nhiên, một hàm số có đạo hàm tại $x_0$ khi và chỉ khi nó có đạo hàm trái và đạo hàm

phải tại $x_0$.

Nếu tồn tại $f'(x_0)$ thì f(x) liên tục tại $x_0$. Tuy nhiên, điều ngược lại không đúng, chẳng

hạn như hàm số f(x) $=$ |x| liên tục tại 0 nhưng không có đạo hàm tại đó.

Ví dụ 8.1 (Giữa kì, K61). Tính f'(0), biết

$ a) f(x) = \begin{cases} \sin x, & n \hat{e}u \ x \ge 0, \\ x^2 + x, & n \hat{e}u \ x < 0. \end{cases} $

$ b) f(x) = \begin{cases} \tan x, & n\hat{e}u \ge 0, \\ -x^2 + x, & n\hat{e}u \le 0. \end{cases} $

Ví dụ 8.2 (Giữa kì, K61). Hãy chỉ ra một hàm số f(x) xác định trên $\mathbb{R}$, liên tục tại các

điểm $x_0 =$ 1, $x_1 =$ 2 nhưng không có đạo hàm tại các điểm này.

Ví dụ 8.3 (Giữa kì, K59). Cho hàm số f(x) khả vi tại 1 và biết rằng

$\n\lim_{x \to 0} \frac{f(1$ + 7x) - f(1 + $2x)}{x} = 2.\n$

Tính f'(1).

[Lời giải] Ta có

$\n\lim_{x \to 0} \frac{f(1+7x)$ - $f(1+2x)}{x} = \lim_{x \to 0} \left[$ 7 $\cdot \frac{f(1+7x)$ - $f(1)}{7x}$ - 2 $\cdot \frac{f(1+2x)$ - $f(1)}{2x} \right]\n$

$=$ 7f'(1) - 2f'(1) $\Rightarrow$ f'(1) $= \frac{2}{5}$.



$ Ví dụ 8.4 (Giữa kì, 20173). Cho hàm số f(x) = \begin{cases} e^{-\frac{1}{x}}, & \text{nếu } x > 0, \\ 0, & \text{nếu } x = 0. \end{cases} $

Tính $f'_{+}(0)$.

[Lời giải] Ta có

$f'_{+}(0) = \lim_{x \to 0^{+}} \frac{f(x)$ - $f(0)}{x$ - $0} = \lim_{x \to 0^{+}} \frac{e^{-\frac{1}{x}}}{x}$.

$\text{Đặt }$ t $= \frac{1}{x} \Rightarrow f'_{+}(0) = \lim_{t \to +\infty} \frac{t}{e^t} = \lim_{t \to +\infty} \frac{1}{e^t} =$ 0 $\quad \text{(L'Hospital)}$

## 8.2 Các phép toán trên đao hàm <math display="block">\text{Đặt } t = \frac{1}{x} \Rightarrow f'_{+}(0) = \lim_{t \to +\infty} \frac{t}{e^t} = \lim_{t \to +\infty} \frac{1}{e^t} = 0 \quad \text{(L'Hospital)}</math>

Định lý 1.24. Cho u(x) và v(x) là các hàm số có đạo hàm tại $x_0$. Khi đó,

i) (u $\pm v)'(x_0) = u'(x_0) \pm v'(x_0)$,

ii) $(uv)'(x_0) = u'(x_0)v(x_0)$ + $u(x_0)v'(x_0)$,

iii) $\left(\frac{u}{v}\right)(x_0) = \frac{u'(x_0)v(x_0)-u(x_0)v'(x_0)}{v^2(x_0)} n\hat{e}u v(x_0) \neq$ 0.

Ví du 8.5 (Giữa kì, K61-Viện ĐTQT). Tính đạo hàm của hàm số

a) f(x) $= x^{\sin x}$, 0 $<$ x $< \frac{\pi}{2}$.

d) f(x) $= (\cos x)^x$, 0 $<$ x $< \frac{\pi}{2}$.

e) f(x) $= (\cos x)^{\sin x}$, 0 $<$ x $< \frac{\pi}{2}$.

b) f(x) $= (\sin x)^x$, 0 $<$ x $< \frac{\pi}{2}$.

f) f(x) $= (\sin x)^{\cos x}$, 0 $<$ x $< \frac{\pi}{2}$.

c) f(x) $= x^{\cos x}$, 0 $<$ x $< \frac{\pi}{2}$.

## 8.3 Đao hàm của hàm hợp c) <math>f(x) = x^{\cos x}, 0 < x < \frac{\pi}{2}</math>.

Định lý 1.25. Nếu u có đạo hàm tại x và f có đạo hàm tại u(x) thì hàm số hợp F $=$ f $\circ$ u

có đạo hàm tại x và

F'(x) $=$ f'(u(x)).u'(x).

$\acute{Y}$ tưởng chứng minh: ta có

$u(x_0$ + $\Delta$ x) $= u(x_0)$ + $u'(x_0) \Delta$ x + $o(\Delta$ x)

$f[u(x_0$ + $\Delta$ x)] - $f[u(x_0)] = f\left[u_0$ + $\underbrace{u'(x_0)\Delta$ x + $o(\Delta x)}_{\delta_u}\right]$ - $f(x_0) = f'_u(u_0).\delta_y$ + $o(\delta_y)$

$\implies \lim_{\Delta$ x $\to 0} \frac{f[u(x_0$ + $\Delta$ x)] - $f[u(x_0)]}{\Delta x}$



## 8.4 Đao hàm của hàm ngược None

Định lý 1.26. $Gi\acute{a}$ thiết

i) x $= \varphi(y)$ có đạo hàm tại $y_0$ và $\varphi'(y_0) \neq$ 0,

ii) x $= \varphi(y)$ có hàm ngược y $=$ f(x) liên tục tại $x_0 = \varphi(y_0)$.

Khi đó hàm ngược này có đạo hàm tại điểm $x_0$ và $f'(x_0) = \frac{1}{\varphi'(y_0)}$.

Định lý 1.27. $Gi\acute{a}$ thiết

i) x $= \varphi(y)$ có đạo hàm tại $y_0$ và $\varphi'(y_0) \neq$ 0,

ii) x $= \varphi(y)$ biến thiên đơn điệu trong lân cận điểm $y_0$.

Khi đó nó tồn tại hàm ngược y $=$ f(x), hàm ngược này cũng có đạo hàm tại điểm $x_0$ và

$f'(x_0) = \frac{1}{\varphi'(y_0)}$.

Từ đó xây dựng công thức đạo hàm của các hàm số lượng giác ngược.

## 8.5 Đạo hàm của các hàm số sơ cấp cơ bản Từ đó xây dựng công thức đạo hàm của các hàm số lượng giác ngược.

1. $(x^{\alpha})' = \alpha x^{\alpha-1}$

7. $(\tan$ x)' $= \frac{1}{\cos^2 x}$

8. $(\cot$ x)' $= -\frac{1}{\sin^2 x}$

2. $(a^x)' = a^x \ln$ a

9. $(\arcsin$ x)' $= \frac{1}{\sqrt{1-x^2}}$

3. $(\log_a$ x)' $= \frac{1}{x \ln a}$

10. $(\arccos$ x)' $= -\frac{1}{\sqrt{1-x^2}}$

4. $(\ln$ x)' $= \frac{1}{x}$

5. $(\sin$ x)' $= \cos$ x

11. $(\arctan$ x)' $= \frac{1}{1+x^2}$

12. $(\operatorname{arccot}$ x)' $= -\frac{1}{1+r^2}$

6. $(\cos$ x)' $= -\sin$ x

## 8.6 Vi phân của hàm số 6. <math>(\cos x)' = -\sin x</math>

Cho hàm số y $=$ f(x) có đạo hàm tại x. Theo định nghĩa của đạo hàm,

f'(x) $= \lim_{\Delta$ x $\to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta$ x $\to 0} \frac{f(x$ + $\Delta$ x) - $f(x)}{\Delta x}$.



Do đó, $\frac{\Delta y}{\Delta x} =$ f'(x) + $\alpha(\Delta$ x), trong đó $\alpha(\Delta$ x) là một VCB khi $\Delta$ x $\to$ 0. Vậy

$\Delta$ y $=$ f(x + $\Delta$ x) - f(x) $= f'(x)\Delta$ x + $\alpha \Delta$ x.

Số hạng $\alpha.\Delta$ x là một VCB bậc cao hơn $\Delta$ x. Do đó, $\Delta$ y và $f'(x)\Delta$ x là hai VCB tương đương.

Định nghĩa 1.21. Cho hàm số f(x) xác định trong một lân cận $U_{\epsilon}(x_0)$. Nếu có

$\Delta$ f $=$ A $\Delta$ x + $o(\Delta$ x),

$\partial$ đó A chỉ phụ thuộc vào $x<sub>0</sub>$ chứ không phụ thuộc vào $\Delta$ x thì ta nói hàm số f(x) khả vi tại

$x_0$ và biểu thức

df $= A\Delta$ x

được gọi là vi phân của hàm số f(x) tại điểm $x_0$.

Mối liên hệ giữa đạo hàm và vi phân

Định lý 1.28. Hàm số f(x) có đạo hàm tại $x_0$ khi và chỉ khi nó khả vi tại $x_0$ và

$df(x_0) = f'(x_0) \Delta$ x.

Chú ý 1.11. Khái niệm "có đạo hàm" và khái niệm "có vi phân" (hay khả vi) là hai khái

niệm khác nhau. Tuy nhiên, vì tính tương đương giữa hai khái niệm này đối với hàm số

một biến số mà nhiều người hiểu nhầm rằng chúng là một. Trong chương 3 của học phần

Giải tích I này, chúng ta sẽ thấy hai khái niệm này là khác nhau đối với hàm số nhiều

biến số.

Xét hàm số y $=$ f(x) $=$ x có df(x) $=$ dx $= 1.\Delta$ x. Vì thế với biến số độc lập x ta quy ước viết

dx $= \Delta$ x và dy $=$ df(x) $=$ f'(x)dx.

Tính bất biến của dạng thức vi phân (cấp 1)

Cho y $=$ f(x) là một hàm số khả vi. Khi đó, ta đã biết nếu x là biến số độc lập thì

df(x) $=$ f'(x)dx.

Định lý 1.29. Nếu x không phải là một biến số độc lập mà x $=$ x(t) là một hàm số phụ

thuộc vào biến số t thì công thức

df(x) $=$ f'(x)dx

vẫn còn đúng.



Chứng minh. Đặt F(t) $=$ f(x(t)), khi đó F'(t) $=$ f'(x(t))x'(t) và

df(x(t)) $=$ f'(x(t))x'(t)dt.

Mặt khác, dx $=$ x'(t)dt nên df(x) $=$ f'(x)dx.

Chính vì vậy, tính chất này còn được gọi là tính bất biến của dạng thức vi phân cấp

một. Chú ý rằng tính chất này không còn đúng đối với các dạng thức vi phân cấp cao.

Ví dụ 8.6. Tính $\frac{d}{d(x^3)}(x^3-2x^6-x^9)$.



![](graphs/graph_47_0.png)

Ý nghĩa hình học của vi phân

$df(x_0) = \overline{MT}$

$x_0$ + $\Delta$ x $\overrightarrow{x}$

$x_0$

$\mathcal{O}$

Khi x thay đổi từ $x_0$ đến $x_0$ + $\Delta$ x thì

i) $df(x_0) = \overline{MT}$ thể hiện sự thay đổi của đường thẳng tiếp tuyến,

ii) $\Delta$ y $= f(x_0$ + $\Delta$ x) - $f(x_0)$ thể hiện sự thay đổi của đường cong y $=$ f(x).

Vi phân của tổng, hiệu, tích, thương

d(u $\pm$ v) $=$ du $\pm$ dv, $\quad$ d(u.v) $=$ udv + vdu, $\quad d\left(\frac{u}{v}\right) = \frac{vdu$ - $udv}{v^2}$.

Ví dụ 8.7 (Giữa kì, K61). Tìm f'(x) nếu biết

a) $\frac{d}{dx}[f(2016x)] = x^2$.

b) $\frac{d}{dx}[f(2017x)] = x^2$.



Ứng dụng vi phân tính gần đúng

Xuất phát từ công thức $\Delta$ y $=$ f(x + $\Delta$ x) - f(x) $= f'(x)\Delta$ x + $o(\Delta$ x) ta ngắt bỏ phần VCB

bậc cao $o(\Delta$ x) để được công thức tính gần đúng sau:

$f(x_0$ + $\Delta$ x) $\approx f(x_0)$ + $f'(x_0) \Delta$ x.

Ví dụ 8.8 (Giữa kì, K61). Sử dụng vi phân, tính gần đúng

a) $\sqrt[3]{7,97}$.

b) $\sqrt[3]{8,03}$.

## 8.7 Đạo hàm cấp cao b) <math>\sqrt[3]{8,03}</math>.

Định nghĩa 1.22. Nếu hàm số y $=$ f(x) có đạo hàm thì $y<sup>'</sup> =$ f'(x) gọi là đạo hàm cấp một

$c\n\mathbf{u}\mathbf{a}$ f(x).

i) Đạo hàm, nếu có, của đạo hàm cấp một được gọi là đạo hàm cấp hai, kí hiệu là f''(x).

ii) Đạo hàm, nếu có, của đạo hàm cấp n - 1 được gọi là đạo hàm cấp n, kí hiệu là $f^{(n)}(x)$.

Các phép toán trên đạo hàm cấp cao

### Định lý 1.30. Cho u, v là các hàm số khả vi đến cấp n. Khi đó,

i) (u $\pm v)^{(n)} = u^{(n)} \pm v^{(n)}$,

ii) (Công thức Leibniz) $(u.v)^{(n)} = \sum_{k=0}^{n} C_n^k u^{(n-k)} v^{(k)}$.

Ví dụ 8.9. Tính đạo hàm cấp cao của các hàm số sau

y $= x^{\alpha}$, y $= \frac{1}{x$ + $a}$, y $= \sin(ax$ + b),

y $= \cos(ax$ + b), y $= e^{ax}$, y $= (x^2$ + 1) $e^x$, y $= e^x \sin$ x.

Đạo hàm cấp cao của một số hàm số cơ bản

1. $(x^{\alpha})^{(n)} = \alpha(\alpha$ - 1) $\dots (\alpha$ - n + 1) $x^{\alpha$ - $n}$

2. $[(1+x)^{\alpha}]^{(n)} = \alpha(\alpha-1)...(\alpha-n+1).(1+x)^{\alpha-n}$

3. $\left(\frac{1}{1+x}\right)^{(n)} = (-1)^{(n)} \cdot \frac{n!}{(1+x)^{n+1}}$

4. $\left(\frac{1}{1-x}\right)^{(n)} = \frac{n!}{(1-x)^{n+1}}$



5. $(\sin x)^{(n)} = \sin$ (x + $\frac{n\pi}{2})$

6. $(\cos x)^{(n)} = \cos$ (x + $\frac{n\pi}{2})$

7. $(a^x)^{(n)} = a^x \cdot (\ln a)^n$

8. $(\ln x)^{(n)} = (-1)^{n-1} \cdot \frac{(n-1)!}{n!}$

Ví dụ 8.10 (Giữa kì, K61). Tính đạo hàm cấp cao $y^{(10)}(0)$ với

a) y(x) $= e^{x^2}$.

c) y(x) $= \arctan$ x.

b) y(x) $= e^{-x^2}$.

d) y(x) $= \operatorname{arccot}$ x.

[Lời giải]

a) Ta có y'(x) $= 2xe^{x^2} =$ 2xy. Lấy đạo hàm cấp n hai về ta được

$y^{(n+1)}(x) = (2xy)^{(n)} = 2xy^{(n)}(x)$ + $2ny^{(n-1)}(x)$. (Công thức Leibniz)

Thay x $=$ 0 ta được có công thức truy hồi

$y^{(n+1)}(0) = 2ny^{(n-1)}(0)$.

Do đó,

$y^{(10)}(0) = 2.9y^{(8)}(0) = (2.9)(2.7)y^{(6)}(0) = \cdots = (2.9)(2.7)(2.5)(2.3)(2.1)y^{(0)}(0) =$ 30240.

b) Tương tự câu a).

c) Ta có y' $= \frac{1}{1+x^2} \Rightarrow (1+x^2)y' =$ 1. Lấy đạo hàm cấp n hai về ta được

$(1+x^2)y^{(n+1)}(x)$ + $n.2x.y^{(n)}(x)$ + $\frac{n(n-1)}{2}.2.y^{(n-1)}(x) =$ 0. (Công thức Leibniz)

Thay x $=$ 0 vào ta được công thức truy hồi

$y^{(n+1)}(0) = -n(n-1)y^{(n-1)}(0)$.

Do đó,

$y^{(10)}(0) = -9.8y^{(8)}(0) = (-9.8)(-7.6)y^{(6)}(0) = \cdots =$ (-9.8)(-7.6)(-5.4)(-3.2)y''(0) $=$ 0

bởi vì, y' $= \frac{1}{1+x^2} \Rightarrow$ y''(x) $= \frac{-2x}{(1+x^2)^2} \Rightarrow$ y''(0) $=$ 0.

d) Tương tự câu c).

Ví dụ 8.11 (Giữa kì, K59). Tính đạo hàm cấp cao $y^{(19)}(0)$ với



a) y $= \arcsin$ x,

b) y $= \arccos$ x.

[Lời giải]

a) Ta có

y' $= \frac{1}{\sqrt{1-x^2}} \Rightarrow (1-x^2)y' = \sqrt{1-x^2} \Rightarrow (1-x^2)y''$ - 2xy' $= \frac{-x}{\sqrt{1-x^2}} \Rightarrow (1-x^2)y''$ - xy' $=$ 0.

Đạo hàm cấp n hai về ta được

$[(1-x^2)y''$ - $xy']^{(n)} =$ 0 $\Rightarrow (1-x^2)y^{(n+2)}$ - $2nxy^{(n+1)}$ - $n(n-1)y^{(n)}$ - $xy^{(n+1)}$ - $ny^{(n)} =$ 0.

Thay x $=$ 0 vào ta được công thức truy hồi

$y^{(n+2)}(0) = n^2 y^{(n)}(0) \Rightarrow y^{(19)}(0) = 17^2 y^{(17)}(0) = \cdots = (17!!)^2$ y'(0) $= (17!!)^2$.

b) Tương tự câu a).

Ví dụ 8.12 (Cuối kì, K60). Tính $f^{(10)}(1)$ với f(x) $= x^9 \ln$ x.

[Lời giải] Ta xét bài toán tổng quát hơn: tính $g^{(n+1)}(x)$ với g(x) $= x^n \ln$ x. Nhận xét

i) g'(x) $= nx^{n-1} \ln$ x + $x^{n-1} = nx^{n-1} \left( \ln$ x + $\frac{1}{n} \right)$

ii) g''(x) $= n(n-1)x^{n-1} \left( \ln$ x + $\frac{1}{n-1}$ + $\frac{1}{n} \right)$

Do đó,

$g^{(n)}(x) =$ n! $\left( \ln$ x + $\frac{1}{1}$ + $\frac{1}{2}$ + $\cdots$ + $\frac{1}{n} \right)$

$g^{(n+1)}(x) = \frac{n!}{x} \Rightarrow f^{(10)}(x) = \frac{10!}{x} \Rightarrow f^{(10)}(1) =$ 10!.

Ví dụ 8.13 (Cuối kì, 20152). Cho hàm số f(x) $= \frac{x}{1+x^3}$. Tính $d^{10}f(0)$.

[Lời giải] Ta có (1 + $x^3)f(x) =$ x. Lấy đạo hàm cấp n hai về ta được

$(1+x^3)f^{(n)}(x)$ + $n.3x^2 \cdot f^{(n-1)}(x)$ + $\frac{n(n-1)}{2} \cdot$ 6x $\cdot f^{(n-2)}(x)$ + $\frac{n(n-1)(n-2)}{6} \cdot$ 6x $\cdot f^{(n-3)}(x) =$ 0.

Cho x $=$ 0 ta được công thức truy hồi

$f^{(n)}(0) = -n(n-1)(n-2)f^{n-3}(0)$.

Do đó,

$f^{(10)}(0) =$ -10.9.8, $f^{(7)}(0) = (-10.9.8)(-7.6.5)(-4.3.2)f^{(1)}(0) =$ -10! $\Rightarrow d^{10}f(0) = -10!dx^{10}$.

Ví du 8.14 (Giữa kì, K61). Tính đạo hàm cấp cao



a) $\left(\frac{1}{x^2-x}\right)^{(60)}$.

c) $(x^2 \sin 2x)^{(50)}$.

b) $\left(\frac{1}{x^2+x}\right)^{(50)}$.

d) $(x^2 \cos 2x)^{(60)}$.

## 8.8 Vi phân cấp cao <i>d)</i> <math>(x^2 \cos 2x)^{(60)}</math>.

Định nghĩa 1.23. Nếu hàm số y $=$ f(x) khả vi thì dy $=$ f'(x)dx gọi là vi phân cấp một

$c\n\mathring{a}$ f(x).

i) Vi phân, nếu có, của vi phân cấp một được gọi là vi phân cấp hai, kí hiệu là $d^2$ f(x).

ii) Vi phân, nếu có, của vi phân cấp n-1 được gọi là vi phân cấp n, kí hiệu là $d^n$ f(x).

Biểu thức của vi phân cấp cao

Nếu x là biến số độc lập thì

$d^n$ f(x) $= f^{(n)}(x) dx^n$.

Vi phân cấp cao không có tính chất bất biến đối với hàm hợp

Ta có df(x) $=$ f'(x)dx nên

$d^2$ f(x) $=$ df'(x)dx + $f'(x)d^2x = f''(x)dx^2$ + $f'(x)d^2x$.

Ví dụ 8.15. Chứng minh rằng nếu y $= x^3$, x $= t^2$ thì

$d^2y \neq y^{(2)}dx^2$.

## 8.9 Bài tâp <math display="block">d^2y \neq y^{(2)}dx^2.</math>

Bài tập 1.44. Tìm đạo hàm của hàm số

$\int$ 1-x,

khi x $<$ 1

$ f(x) = \begin{cases} (1-x)(2-x), & \text{khi } 1 \le x \le 2 \\ x-2, & \text{khi } x > 2. \end{cases} $

$ Bài tập 1.45. Với điều kiện nào thì hàm số f(x) = \begin{cases} x^n \sin \frac{1}{x}, & \text{ khi } x \neq 0 \\ 0, & \text{ khi } x = 0 \end{cases} $



a) liên tục tại x $=$ 0, b) khả vi tại x $=$ 0,

c) có đạo hàm liên tục tại

x $=$ 0.

$[\text{Đáp}\text{ s}\hat{\text{o}}]$

b) n $>$ 1,

a) n $>$ 0,

c) n $>$ 2.

Bài tập 1.46. Chứng minh rằng hàm số f(x) $=$ |x - a| $\cdot \varphi(x)$, trong đó $\varphi(x)$ là một hàm số

liên tục và $\varphi(a) \neq$ 0, không khả vi tại điểm x $=$ a.

[Gợi $\acute{y}]$

$f'_{+}(a) = \varphi(a) \neq f'_{-}(a) = -\varphi(a)$

Bài tập 1.47. Tìm vi phân của hàm số

a) y $= \frac{1}{a} \arctan \frac{x}{a} \mid$ (a $\neq$ 0)

c) y $= \frac{1}{2a} \ln \left| \frac{x$ - $a}{x$ + $a} \right|$ (a $\neq$ 0)

d) y $= \ln$ |x + $\sqrt{x^2$ + $a}|$

b) y $= \arcsin \frac{x}{a}$ (a $\neq$ 0)

$[\text{Đáp}\text{ s}\hat{\text{o}}]$

a) dy $= \frac{dx}{a^2$ + $x^2}$

c) dy $= \frac{dx}{x^2$ - $a^2}$

d) dy $= \frac{dx}{\sqrt{x^2$ + $a}}$

b) dy $= \frac{dx}{\sqrt{a^2$ - $x^2}}.(sign$ a)

Bài tập 1.48. Tìm

a) I $= \frac{d}{d(x^3)}(x^3$ - $2x^6$ - $x^9)$,

c) K $= \frac{d(\sin x)}{d(\cos x)}$.

b) J $= \frac{d}{d(x^2)}(\frac{\sin x}{x})$,

$[\text{Đáp}\text{ số}]$

a) I $= -3x^6$ - $4x^3$ + 1, x $\neq$ 0,

c) K $= -\cot$ x, x $\neq k\pi$, k $\in \mathbb{Z}$.

b) J $= \frac{1}{2x^2} \left( \cos$ x - $\frac{\sin x}{x} \right)$, x $\neq$ 0,

Bài tập 1.49. Tính gần đúng giá trị của biểu thức



b) $\sqrt[7]{\frac{2-0.02}{2+0.02}}$

a) $\lg$ 11

[Goi $\dot{y}]$

a) Xét f(x) $= \lg$ x, $x_0 =$ 10, $\triangle$ x $=$ 1, ta có $\lg$ 11 $\approx \lg$ 10 + $\frac{1}{10 \ln 10} =$ 1,043

b) Cách 1. $\sqrt[7]{\frac{2-0.02}{2+0.02}} = \sqrt[7]{\frac{4}{2+0.02}}$ - 1. Xét f(x) $= \sqrt[7]{\frac{4}{x}}$ - 1, $x_0 =$ 2, $\triangle$ x $=$ 0.02

Ta có

f(x + $\triangle$ x) $= \sqrt[7]{\frac{4}{2}}$ - 1 + 0.02 $\cdot \frac{1}{7} \cdot (\frac{4}{2}$ - $1)^{\frac{-6}{7}} \cdot \frac{-4}{2} =$ 1 - 0.02 $\cdot \frac{1}{7}$.

Cách 2. Xét hàm số f(x) $= \sqrt[7]{\frac{2-x}{2+x}}$, với $x_0 =$ 0, $\Delta$ x $=$ 0, 02.

Bài tập 1.50. Tìm đạo hàm cấp cao của các hàm số

(c) y $= x^2 e^{2x}$, tinh $y^{(10)}$.

(a) y $= \frac{x^2}{1-x}$, tinh $y^{(8)}$.

(b) y $= \frac{1+x}{\sqrt{1-x}}$, tinh $y^{(100)}$.

(d) y $= x^2 \sin$ x, tinh $y^{(50)}$.

$[\text{Đáp}\text{ s}\hat{\text{o}}]$

(a) $y^{(8)} = \frac{8!}{(1-x)^9}$, x $\neq$ 1.

(b) $y^{(100)} = \frac{197!}{2^{100}(1-x)^{100}\sqrt{1-x}}(399-x)$, x $<$ 1.

(c) $y^{(10)} = 2^{10}e^{2x} \left(x^2$ + 10x + $\frac{45}{2}\right)$.

(d) $y^{(50)} = -x^2 \sin$ x + 100x $\cos$ x + 2450 $\sin$ x.

Bài tập 1.51. Tính đạo hàm cấp n của các hàm số

c) y $= \frac{x}{\sqrt[3]{1$ + $x}}$

a) y $= \frac{x}{x^2$ - $1}$,

b) y $= \frac{1}{x^2$ - 3x + $2}$

d) y $= e^{ax} \sin(bx$ + c).

$[\text{Đáp}\text{ s}\hat{\text{o}}]$

a) $y^{(n)} = \frac{(-1)^n}{2}$ n! $\left[ \frac{1}{(x-1)^{n+1}}$ + $\frac{1}{(x+1)^{n+1}} \right]$.

b) $y^{(n)} =$ n! $\left| \frac{1}{(1-x)^{n+1}}$ - $\frac{1}{(2-x)^{n+1}} \right|$.



c) $y^{(n)} = \frac{(-1)^{n-1}}{3^n}$ (1.4 $\dots$ (3n-5)) $\frac{3n+2x}{(1+x)^{n+\frac{1}{3}}}$, n $\ge$ 2, x $\ne$ 1.

d) Tính y' rồi dự đoán và chứng minh bằng quy nạp

$y^{(n)} = (a^2$ + $b^2)^{\frac{n}{2}} e^{ax} \sin(bx$ + c + $n\varphi)$, $\delta \sin \varphi = \frac{b}{\sqrt{a^2$ + $b^2}}$, $\cos \varphi = \frac{a}{\sqrt{a^2$ + $b^2}}$.

Bài tập 1.52. Tính đạo hàm cấp n của các hàm số

e) y $= \sin^2$ x,

a) y $= \frac{1}{a$ + $h\gamma}$,

j) y $=$ x $\cos$ ax,

f) y $= \sin^3$ x,

b) y $= \frac{1}{\sqrt{a$ + $h\gamma}}$,

k) y $= x^2 \cos$ ax,

g) y $= \sin$ ax $\cdot \sin$ bx,

c) y $= \frac{1}{x^2$ - $a^2}$,

1) y $= x^2 \sin$ ax,

h) y $= \sin^2$ ax $\cdot \cos$ bx,

d) y $= \frac{ax$ + $b}{cx$ + $a}$,

m) y $= \ln \frac{a$ + $bx}{a$ + $bx}$.

i) y $= \sin^4$ x + $\cos^4$ x,

$[\text{Đáp}\ \text{s}\text{\^{o}}]$

a) $y^{(n)} = \frac{(-1)^n \cdot$ n! $b^n}{(a$ + $bx)^{n+1}}$.

b) $y^{(n)} = \frac{(-1)^n (2n-1)!!b^n}{2^n \sqrt[n]{a+bx}}$.

c) y $= \frac{1}{x^2$ - $a^2} = \frac{1}{2a} \left( \frac{1}{x$ - $a}$ - $\frac{1}{x$ + $a} \right)$ nên $y^{(n)} = \frac{(-1)^n \cdot n!}{2a} \left| \left( \frac{1}{x$ - $a} \right)^{n+1}$ - $\left( \frac{1}{x$ + $a} \right)^{n+1} \right|$.

d) y $= \frac{ax$ + $b}{cx$ + $d} = \frac{a}{c}$ + $\frac{1}{c} \left($ b - $\frac{ad}{c} \right) \frac{1}{x$ + $\frac{d}{c}}$ nên $y^{(n)} = \frac{1}{c} \left($ b - $\frac{ad}{c} \right) \frac{(-1)^n \cdot n!}{\left($ x + $\frac{d}{c} \right)^{n+1}}$.

e) y $= \sin^2$ x $= \frac{1}{2}$ - $\frac{1}{2} \cos$ 2x nên $y^{(n)} = -2^{n-1} \cos$ (2x + $\frac{n\pi}{2})$.

f) y $= \sin^3$ x $= \frac{3}{4} \sin$ x - $\frac{1}{4} \sin$ 3x nên $y^{(n)} = \frac{3}{4} \sin$ (x + $\frac{n\pi}{2})$ - $\frac{1}{4} 3^n \sin$ (3x + $\frac{n\pi}{2})$.

g) y $= \sin$ ax $\cdot \sin$ bx $= \frac{1}{2} [\cos(a$ - b)x - $\cos(a$ + b)x] nên

$y^{(n)} = \frac{1}{2}(a-b)^n \cos\left[$ (a-b)x + $\frac{n\pi}{2} \right]$ - $\frac{1}{2}(a+b)^n \cos\left[$ (a+b)x + $\frac{n\pi}{2} \right]$.

h) y $= \sin^2$ ax $\cdot \cos$ bx $= \frac{\cos bx}{2}$ - $\frac{1}{4}[\cos(2a+b)x$ + $\cos(2a-b)x]$ nên

$y^{(n)} = \frac{1}{2}b^n \cos \left(bx$ + $\frac{n\pi}{2}\right)$ - $\frac{1}{4}(2a$ + $b)^n \cos \left[(2a$ + b)x + $\frac{n\pi}{2}\right]$

$-\frac{1}{4}(2a-b)^n\cos\left[(2a-b)x+\frac{n\pi}{2}\right]$.



i) y $= \sin^4$ x + $\cos^4$ x $= \frac{3}{4}$ + $\frac{1}{4} \cos$ 4x nên $y^{(n)} = 4^{n-1} \cos$ (4x + $\frac{n\pi}{2})$.

j) $y^{(n)} = a^n$ x $\cos \left(ax$ + $\frac{n\pi}{2}\right)$ + $na^{n-1} \cos \left(ax$ + $\frac{(n-1)\pi}{2}\right)$.

k) $y^{(n)} = a^n x^2 \sin \left(ax$ + $\frac{n\pi}{2}\right)$ + $2na^{n-1}x \sin \left(ax$ + $\frac{(n-1)\pi}{2}\right)$ + $n(n-1)a^{n-2} \sin \left(ax$ + $\frac{(n-2)\pi}{2}\right)$.

1) $y^{(n)} = a^n x^2 \cos \left(ax$ + $\frac{n\pi}{2}\right)$ + $2na^{n-1}x \cos \left(ax$ + $\frac{(n-1)\pi}{2}\right)$ + $n(n-1)a^{n-2} \cos \left(ax$ + $\frac{(n-2)\pi}{2}\right)$.

m) $y^{(n)} = \frac{(n-1)!b^n}{(a^2$ - $b^2x^2)^n} \cdot$ [(a + $bx)^n$ + $(-1)^n(a$ - $bx)^n]$.

## 8.10 Đọc thêm: Về khái niệm vi phân m) <math>y^{(n)} = \frac{(n-1)!b^n}{(a^2 - b^2x^2)^n} \cdot [(a + bx)^n + (-1)^n(a - bx)^n].</math>

Vi phân có lẽ là một khái niệm trừu tượng và dễ gây hiểu nhầm nhất trong môn Giải

tích I. Theo sự hiểu biết của tác giả thì có nhiều cách tiếp cận khác nhau đối với phép tính

vi phân.

1) Người đầu tiên đưa ra khái niệm vi phân có lẽ là Leibniz, khi ông coi dy là một đại

lượng vô cùng bé thể hiện sự thay đổi của hàm số y $=$ f(x) tương ứng với sự thay đổi

vô cùng bé dx của biến số x, nghĩa là ông định nghĩa

f'(x) $:= \frac{dy}{dx}$.

Kí hiệu $\frac{dy}{dx}$ này là kí hiệu của Leibniz cho đạo hàm của hàm số f(x). Mặc dù có nhiều

chỉ trích cho kí hiệu này, nó vẫn được dùng cho đến ngày nay. Cũng chú ý thêm rằng,

kí hiệu f'(x) trên là kí hiệu của d'Alambert.

2) Cauchy là người đã cải tiến ý tưởng của Leibniz và những người đi trước như sau.

Trước hết, ông định nghĩa phép toán đạo hàm

f'(x) $:= \lim_{\Delta$ x $\to 0} \frac{f(x$ + $\Delta$ x) - $f(x)}{\Delta x}$

là giới hạn của tỉ số giữa số gia của hàm số và số gia của đối số khi số gia của đối số

tiến về 0. Sau đó ông định nghĩa vi phân

dy $=$ f'(x)dx,

như một hàm số của hai biến số x và dx, ở đó dx là một biến số mới, có thể lấy giá tri

tùy ý, không nhất thiết phải là một đại lượng VCB như trong kí hiệu của Leibniz.

3) Ngày nay, vi phân được định nghĩa theo lối tiếp cận hiện đại như sau:



Định nghĩa 1.24. Cho hàm số f(x) có đạo hàm tại $x_0$. Ta gọi ánh xạ, kí hiệu là $d_{x_0}f$,

xác định bởi

$d_{x_0}f:\mathbb{R}\to\mathbb{R}$,

h $\mapsto f'(x_0)h$

là vi phân của f tại $x_0$.

Vậy vi phân của f tại $x_0$ là một ánh xạ tuyến tính.

i) Như vậy, vi phân của hàm số một biến số f(x) là một hàm số df của hai biến số

$x_0$ và h cho bởi

$d_{x_0}f(h) = f'(x_0)h$,

$\mathring{\sigma}$ đó h là một biến số mới có thể nhận giá trị tùy ý.

ii) Kí hiệu Id là ánh xạ đồng nhất, khi đó, $d_{x_0}(Id)(h) =$ h, hay là $d_{x_0}(Id) =$ Id.

iii) Một cách lạm dụng kí hiệu, ta kí hiệu x là ánh xạ đồng nhất x $:= \text{Id}$. Khi đó,

$d_{x_0}x = \text{Id}$ là ánh xạ đồng nhất và không phụ thuộc vào $x_0$ nên ta kí hiệu nó là

dx. Điều này dẫn đến $d_{x_0}f = f'(x_0)dx$. Đôi khi, người ta bỏ $x_0$ trong $d_{x_0}f$ và, một

cách lạm dụng, thay $x_0$ bởi x trong $f'(x_0)$ để có biểu thức cô đọng

df $=$ f'(x)dx.



§9. CÁC ĐỊNH LÝ VỀ HÀM KHẢ VI VÀ ỨNG DỤNG

## 9.1 Các định lý về hàm khả vi §9. CÁC ĐỊNH LÝ VỀ HÀM KHẢ VI VÀ ỨNG DỤNG

Định nghĩa 1.25 (Cực trị của hàm số). Cho hàm số f(x) liên tục trên (a, b), ta nói hàm

số đạt cực trị tại điểm $x_0 \in$ (a, b) nếu $\exists U(x_0) \subset$ (a, b) sao cho f(x) - $f(x_0)$ không đổi dấu

$\forall$ x $\in U(x_0) \setminus \{x_0\}$.

• Nếu f(x) - $f(x_0) >$ 0 thì ta nói hàm số đạt cực tiểu tại $x_0$.

• Nếu f(x) - $f(x_0) <$ 0 thì ta nói hàm số đạt cực đại tại $x_0$.

Định lý 1.31 (Định lý Fermat). Cho f(x) liên tục trên khoảng (a,b), nếu hàm số đạt cực

trị tại điểm $x_0 \in$ (a, b) và có đạo hàm tại $x_0$ thì $f'(x_0) =$ 0.

Chứng minh. Nếu hàm số đạt cực đại tại $x_0$ thì theo định nghĩa tồn tại một lân cận $U(x_0)$

sao cho f(x) - $f(x_0) <$ 0 $\forall$ x $\in U(x_0)$. Do đó, với h đủ nhỏ sao cho $f(x_0$ + h) $\in U(x_0)$ thì

$f(x_0$ + h) - $f(x_0) <$ 0.

• $f'(x_0^+) = \lim_{h \to 0^+} \frac{f(x_0+h)$ - $f(x_0)}{h} \le$ 0.

• $f'(x_0^-) = \lim_{h \to 0^-} \frac{f(x_0+h)-f(x_0)}{h} \ge$ 0.

$\mathbf{r}$

Do giả thiết tồn tại $f'(x_0)$ nên $f'(x_0^+) = f'(x_0^-)$. Điều này chỉ xảy ra khi

$f'(x_0^+) = f'(x_0^-) =$ 0.

Ví dụ 9.1 (Giữa kì, K61). Tìm các cực trị của các hàm số

a) y $= \frac{\cos x}{2$ + $\sin x}$ trong khoảng (0, $2\pi).b)$ y $= \frac{\sin x}{2$ + $\cos x}$ trong khoảng (0, $2\pi)$.

Ví dụ 9.2 (Cuối kì, K61-Viện ĐTQT). Cho f(x) là một hàm số khả vi trên $\mathbb{R}$ và thỏa

mãn f'(2) $< \lambda <$ f'(3). Chứng minh rằng tồn tại $x_0 \in$ (2,3) sao cho $f'(x_0) = \lambda$.

[Lời giải] Xét hàm số g(x) $=$ f(x) - $\lambda$ x. Khi đó,

i) g'(2) $=$ f'(2) - $\lambda <$ 0, do đó tồn tại $x_1 \in$ (2,3) nào đó sao cho $g(x_1) <$ g(2), nếu không

thì

$g'_{+}(2) = \lim_{x \to 2^{+}} \frac{g(x)$ - $g(2)}{x$ - $2} \ge$ 0.

ii) g'(3) $=$ f'(3) - $\lambda >$ 0, do đó tồn tại $x_2 \in$ (2,3) sao cho $g(x_2) <$ g(3), nếu không thì

$g'_{-}(3) = \lim_{x \to 3^{-}} \frac{g(x)$ - $g(2)}{x$ - $3} \le$ 0.



iii) Do đó, g(x) đạt cực tiểu tại điểm $x_0 \in$ (2,3) $\Rightarrow g'(x_0) =$ 0 $\Rightarrow f'(x_0) = \lambda$.

Định lý 1.32 (Định lý Rolle). Nếu hàm số f(x) :

i) Liên tục trong khoảng đóng [a, b],

ii) Có đạo hàm trong khoảng mở (a,b),

iii) thỏa mãn điều kiện f(a) $=$ f(b),

thì tồn tại ít nhất một điểm c $\in$ (a, b) sao cho f'(c) $=$ 0.

Chứng minh. Do hàm số f(x) liên tục trên [a, b] nên nó đạt GTLN và GTNN trên [a, b]. Ta

chia làm các trường hợp sau:

• Nếu f(x) là hằng số trên [a, b] thì f'(x) $=$ 0 $\forall$ x $\in$ (a, b).

• Nếu có số x $\in$ (a, b) sao cho f(x) $>$ f(a) $=$ f(b) thì GTLN của f(x) sẽ phải đạt được

tại một điểm c nào đó thuộc (a, b) (do nó không đạt GTLN tại hai đầu mút). Khi đó,

theo Định lý Fermat, f'(c) $=$ 0.

• Nếu có số x $\in$ (a, b) sao cho f(x) $<$ f(a) $=$ f(b) thì GTNN của f(x) sẽ phải đạt được

tại một điểm c nào đó thuộc (a, b) (do nó không đạt GTNN tại hai đầu mút). Khi đó,

theo Định lý Fermat, f'(c) $=$ 0.

$\mathbf{r}^{\prime}$

Ví dụ 9.3 (Học kì 20163). Cho hàm số f(x) $=$ (x - $1)(x^2$ - $2)(x^2$ - 3). Phương trình

f'(x) $=$ 0 có bao nhiều nghiệm thực? Giải thích.

[Lời giải] Phương trình f(x) $=$ 0 có 5 nghiệm là x $= -\sqrt{3}$, x $= -\sqrt{2}$, x $=$ 1, x $= \sqrt{2}$ và

x $= \sqrt{3}$.

i) Vì $f(-\sqrt{3}) = f(-\sqrt{2}) =$ 0 nên theo Định lý Rolle, tồn tại $x_1 \in (-\sqrt{3}$, $-\sqrt{2})$ sao cho

$f'(x_1) =$ 0.

ii) Vì $f(-\sqrt{2}) =$ f(1) $=$ 0 nên theo Định lý Rolle, tồn tại $x_2 \in (-\sqrt{2}$, 1) sao cho $f'(x_2) =$ 0.

iii) Vì f(1) $= f(\sqrt{2}) =$ 0 nên theo Định lý Rolle, tồn tại $x_2 \in (1,\sqrt{2})$ sao cho $f'(x_3) =$ 0.

iv) Vì $f(\sqrt{2}) = f(\sqrt{3}) =$ 0 nên theo Định lý Rolle, tồn tại $x_4 \in (\sqrt{2},\sqrt{2})$ sao cho $f'(x_4) =$ 0.

Vậy phương trình f'(x) $=$ 0 có ít nhất 4 nghiệm. Mặt khác, f'(x) là một đa thức bậc bốn,

nên nó có nhiều nhất là bốn nghiệm. Kết luận: phương trình f'(x) $=$ 0 có đúng 4 nghiệm

phân biệt.

Ví dụ 9.4 (Giữa kì, K62). Cho ba số thực a, b, c thỏa mãn a + b + c $=$ 0. Chứng minh rằng



a) phương trình $3ax^2$ + 4bx + 5c $=$ 0 có ít nhất một nghiệm thuộc khoảng (1, $+\infty)$.

b) phương trình $2ax^2$ + 3bx + 4c $=$ 0 có ít nhất một nghiệm thuộc khoảng (1, $+\infty)$.

[Lời giải]

a) Xét hàm số f(x) $= cx^5$ + $bx^4$ + $ax^3$ thỏa mãn các điều kiện của Định lý Rolle trong

khoảng [0, 1]. Do đó,

$\exists x_0 \in$ (0,1) | $f'(x_0) = 5cx_0^4$ + $4bx_0^3$ + $3ax_0^2 =$ 0 $\Rightarrow 3a\left(\frac{1}{x_0}\right)^2$ + $4b\left(\frac{1}{x_0}\right)$ + 5c $=$ 0.

Vậy phương trình $3ax^2$ + 4bx + 5c $=$ 0 có nghiệm $\frac{1}{x_0} \in$ (1, $+\infty)$.

b) Xét hàm số f(x) $= cx^4$ + $bx^3$ + $ax^3$ thỏa mãn các điều kiện của Định lý Rolle trong

khoảng [0,1]. Do đó,

$\exists x_0 \in$ (0,1) | $f'(x_0) = 4cx_0^3$ + $3bx_0^2$ + $2ax_0 =$ 0 $\Rightarrow 2a\left(\frac{1}{x_0}\right)^2$ + $3b\left(\frac{1}{x_0}\right)$ + 4c $=$ 0.

Vậy phương trình $2ax^2$ + 3bc + 4c $=$ 0 có nghiệm $\frac{1}{x_0} \in$ (1, $+\infty)$.

Ví dụ 9.5 (Cuối kì, K62). Cho f liên tục trên [a,b] và thỏa mãn $\int$ f(x)dx $=$ 0. Chứng

minh rằng $\exists$ c $\in$ (a, b) sao cho 2017 $\int_{c}^{c}$ f(x) dx $=$ f(c).

[Lời giải]

Xét hàm số g(x) $= \int_a^x$ f(t)dt, là một hàm số liên tục trên [a, b], khả vi trên (a, b) và

g(a) $=$ g(b) $=$ 0. Do đó, hàm số h(x) $= e^{-2017x}g(x)$ cũng là một hàm số liên tục trên [a, b],

khả vi trên (a, b) và h(a) $=$ h(b) $=$ 0. Áp dụng Định lý Rolle với hàm số h(x) trong khoảng

[a, b] ta có:

$\exists$ c $\in$ (a,b) : h'(c) $=$ 0 $\Leftrightarrow g'(c)e^{-2017c}$ - $2017e^{-2017c}g(c) =$ 0

$\Leftrightarrow$ g'(c) - 2017g(c) $=$ 0

$\Leftrightarrow$ f(c) $=$ 2017 $\int_{c}^{c}$ f(t)dt $=$ 2017 $\int_{a}^{c}$ f(x)dx.

Ví dụ 9.6 (Olympic Toán học sinh viên Toàn quốc 2018 - Bảng B). $Gi\!{a}$ sử $f:[0,1]\rightarrow$

$\mathbb{R}$ là một hàm số khả vi sao cho $\int_{0}^{1}$ f(x)dx $= \int_{0}^{1}$ xf(x)dx. Chứng minh rằng tồn tại số

c $\in$ (0,1) sao cho

f(c) $=$ 2018 $\int_{0}^{c}$ f(x) dx.



Chứng minh. i) Xét hàm số F(x) $=$ x $\int_{0}^{x}$ f(t)dt - $\int_{0}^{x}$ tf(t)dt khả vi trên [0,1] và F(0) $=$

F(1) $=$ 0. Theo Định lý Rolle, tồn tại $x_0 \in$ (0,1) sao cho $F'(x_0) =$ 0 $\Leftrightarrow \int_{0}^{\infty}$ f(t) dt $=$ 0.

ii) Đặt G(x) $= e^{-2018x} \int_{\hat{G}} \tilde{f}(t)$ dt thì G(x) là một hàm số khả vi trên [0,1] với G(0) $=$

$G(x_0) =$ 0. Theo Định lý Rolle, tồn tại c $\in$ (0, $x_0)$ sao cho

G'(c) $=$ 0 $\Leftrightarrow$ f(c) $=$ 2018 $\int_{c}^{c}$ f(x) dx.

Ví dụ 9.7 (Olympic Toán học sinh viên Toàn quốc 2018 - Bảng A). Giả sử f : [0,1] $\rightarrow$

$\mathbb{R}$ là một hàm số khả vi sao cho $\int_{0}^{1}$ f(x)dx $= \int_{0}^{1}$ xf(x)dx. Chứng minh rằng tồn tại số

c $\in$ (0,1) sao cho

f(c) $=$ 2018f'(c) $\int_{0}^{c}$ f(x)dx.

Chứng minh. i) Xét hàm số F(x) $=$ x $\int_{0}^{x}$ f(t)dt - $\int_{0}^{x}$ tf(t)dt khả vi trên [0,1] và F(0) $=$

F(1) $=$ 0. Theo Định lý Rolle, tồn tại $x_0 \in$ (0,1) sao cho $F'(x_0) =$ 0 $\Leftrightarrow \int_0^{\infty}$ f(t) dt $=$ 0.

ii) Đặt G(x) $= e^{-2018f(x)} \int_{x}^{x}$ f(t)dt thì G(x) là một hàm số khả vi trên [0, 1] với G(0) $=$

$G(x_0) =$ 0. Theo Định lý Rolle, tồn tại c $\in$ (0, $x_0)$ sao cho

G'(c) $=$ 0 $\Leftrightarrow$ f(c) $=$ 2018f'(c) $\int_{c}^{c}$ f(x) dx.

$\mathbf{U}$

Định lý 1.33 (Định lý Lagrange). Nếu hàm số f(x) :

i) Liên tục trong khoảng đóng [a, b],

ii) Có đạo hàm trong khoảng mở (a,b),



thì tồn tại ít nhất một điểm c $\in$ (a, b) sao cho f'(c) $= \frac{f(b)-f(a)}{b-a}$.

Chứng minh. Xét hàm số

h(x) $=$ f(x) - f(a) - $\frac{f(b)$ - $f(a)}{b$ - $a}(x$ - a).

Có thể dễ dàng kiểm chứng h(x) thỏa mãn các điều kiện của Định lý Rolle, do đó tồn tại

c $\in$ (a, b) sao cho h'(c) $=$ f'(c) - $\frac{f(b)-f(a)}{b-a} =$ 0.

$\mathbf{r}$

Ví du 9.8 (Giữa kì, K61). Chứng minh các bất đẳng thức sau với 0 $<$ a $<$ b.

a) $\frac{a-b}{1+a^2} <$ arctan b - arctan a $< \frac{b-a}{1+a^2}$.

[Lời giải]

a) Áp dụng Định lý Lagrange với hàm số f(x) $= \operatorname{arccot}$ x trong khoảng [a, b] ta có

$\frac{\operatorname{arccot}$ b - $\operatorname{arccot} a}{b$ - $a} =$ f'(c) $= -\frac{1}{1$ + $c^2}$

với c $\in$ (a, b) nào đó. Do đó,

$-\frac{1}{1+a^2} < \frac{\operatorname{arccot}$ b - $\operatorname{arccot} a}{b-a} = -\frac{1}{1+c^2} < -\frac{1}{1+b^2}$

dẫn đến điều phải chứng minh.

b) Tương tự câu a).

Ví dụ 9.9 (Giữa kì, K59). Cho hàm số $f:(0,+\infty) \to \mathbb{R}$ thỏa mãn f(x) $\le$ 1 và f''(x) $\ge$ 0

với mọi x $>$ 0. Chứng minh rằng f'(x) $\leq$ 0 với mọi x $>$ 0.

[Lời giải]

Giả sử phản chứng, tồn tại $x_0 >$ 0 sao cho $f'(x_0) >$ 0.

i) Vì f''(x) $\ge$ 0 nên f'(x) $\ge f'(x_0)$ với mọi x $> x_0$.

ii) Áp dụng Định lý Lagrange cho hàm số f(x) trong khoảng $[x_0$, x] ta có: tồn tại c $\in$

$(x_0$, x) sao cho f(x) $= f(x_0)$ + f'(c)(x - $x_0) \ge f(x_0)$ + $f'(x_0)(x$ - $x_0)$.

iii) Mặt khác, vì $f'(x_0) >$ 0 nên $\lim_{x \to +\infty} f(x_0)$ + $f'(x_0)(x$ - $x_0) = +\infty \Rightarrow \lim_{x \to +\infty}$ f(x) $= +\infty$,

trái với giả thiết f(x) $\le$ 1 với mọi x $>$ 0.

Mâu thuẫn này chứng tỏ f'(x) $\leq$ 0 với mọi x $>$ 0.

### Định lý 1.34 (Định lý Cauchy). Nếu các hàm số <math>f(x)</math>, <math>g(x)</math> thỏa mãn các điều kiện:



i) Liên tục trong khoảng đóng [a, b],

ii) Có đạo hàm trong khoảng mở (a,b),

iii) g'(x) không triệt tiêu trong khoảng mở (a, b)

thì tồn tại ít nhất một điểm c $\in$ (a, b) sao cho

$\frac{f(b)-f(a)}{\varphi(b)-\varphi(a)}=\frac{f'(c)}{\varphi'(c)}$.

Chú ý 1.12. a) Định lý Rolle là trường hợp riêng của định lý Lagrange, định lý La-

grange là trường hợp riêng của định lý Cauchy. Các giả thiết trong các định lý này

là cần thiết.

b) Định lý Lagrange còn có một dạng khác, đó là công thức số gia hữu hạn:

$\Delta$ f $= f'(x_0$ + $\theta \Delta$ x), $\ \theta \in$ (0,1).

## 9.2 Các công thức khai triển Taylor, Maclaurin <math>\Delta f = f'(x_0 + \theta \Delta x), \ \theta \in (0,1).</math>

Định lý 1.35. Nếu hàm số f(x)

(i) Có đạo hàm đến cấp n trong khoảng đóng liên tục tại $x_0$,

(ii) Có đạo hàm đến cấp n + 1 trong lân cận $U_{\epsilon}(x_0)$,

thì f(x) có thể biểu diễn dưới dạng

f(x) $= f(x_0)$ + $\frac{f'(x_0)}{1!}(x$ - $x_0)$ + $\cdots$ + $\frac{f^{(n)}(x_0)}{n!}(x$ - $x_0)^n$ + $\frac{f^{(n+1)}(c)}{(n+1)!}(x$ - $x_0)^{n+1}$,

$\partial$ đó c là một số thực nằm giữa x và $x<sub>0</sub>$ nào đó.

Nếu $x_0 =$ 0 thì công thức sau còn được gọi là công thức Maclaurin:

f(x) $=$ f(0) + $\frac{f'(0)}{1!}x$ + $\cdots$ + $\frac{f^{(n)}(0)}{n!}x^{n}$ + $\frac{f^{(n+1)}(c)}{(n+1)!}x^{n+1}$

(1.1)

hay

f(x) $=$ f(0) + $\frac{f'(0)}{1!}x$ + $\cdots$ + $\frac{f^{(n)}(0)}{n!}x^{n}$ + $o(x^{n})$,

(1.2)

ở đó $o(x^n)$ là một VCB bậc cao hơn $x^n$.



Môt số khai triển Maclaurin quan trong

(1) (1 + $x)^{\alpha} =$ 1 + $\alpha$ x + $\frac{\alpha(\alpha$ - $1)}{2}x^2$ + $\cdots$ + $\frac{\alpha(\alpha$ - $1)\cdots(\alpha$ - n + $1)}{n!}x^n$ + $o(x^n)$

(2) $\frac{1}{1+x} =$ 1 - x + $x^2$ - $\cdots$ + $(-1)^n x^n$ + $o(x^n)$

(3) $\frac{1}{1-x} =$ 1 + x + $x^2$ + $\cdots$ + $x^n$ + $o(x^n)$

(4) $e^x =$ 1 + x + $\frac{x^2}{2!}$ + $\cdots$ + $\frac{x^n}{n!}$ + $o(x^n)$

(5) $\sin$ x $=$ x - $\frac{x^3}{3!}$ + $\frac{x^5}{5!}$ + $\cdots$ + $(-1)^n \frac{x^{2n+1}}{(2n+1)!}$ + $o(x^{2n+1})$

(6) $\cos$ x $=$ 1 - $\frac{x^2}{2!}$ + $\frac{x^4}{4!}$ + $\cdots$ + $(-1)^n \frac{x^{2n}}{(2n)!}$ + $o(x^{2n})$

(7) $\ln(1+x) =$ x - $\frac{x^2}{2}$ + $\frac{x^3}{2}$ + $\cdots$ + $(-1)^{n-1} \frac{x^n}{n}$ + $o(x^n)$

Các phép toán trên khai triển Maclaurin

Trên khai triển Maclaurin chúng ta có thể thực hiện các phép toán cơ bản sau: công,

trù, nhân, chia, hàm hợp, đạo hàm và tích phân. Các phép toán cộng, trù, nhân, chia được

thực hiện hệt như cộng, trừ, nhân, chia các đa thức. Cho f(x) $= a_0$ + $a_1x$ + $a_2x^2$ + $a_3x^3$ +

$\cdots$ + $a_n x^n$ + $\cdots$ và g(x) $= b_0$ + $b_1$ x + $b_2 x^2$ + $b_3 x^3$ + $\cdots$ + $b_n x^n$ + $\cdots$ là các chuỗi Maclaurin

hình thức. Khi đó

1. Phép cộng $(tr\grave{u})$

f(x) $\pm$ g(x) $= (a_0 \pm b_0)$ + $(a_1 \pm b_1)x$ + $(a_2 \pm b_2)x^2$ + $(a_3 \pm b_3)x^3$ + $\cdots$ + $(a_n \pm b_n)x^n$ + $\cdots$

2. Phép nhân

f(x)g(x) $= c_0$ + $c_1x$ + $c_2x^2$ + $c_3x^3$ + $\cdots$ + $c_nx^n$ + $\cdots$,

ở đó $c_n = \sum_{i=0}^n a_i b_{n-i}$. Chuỗi $\sum_{n=0}^{+\infty} c_n x^n$ còn được gọi là tích chập của hai chuỗi $\sum_{n=0}^{+\infty} a_n x^n$ và

$\sum_{n=1}^{+\infty} b_n x^n$.

$n=0$

Ví dụ 9.10. Tìm khai triển Maclaurin của hàm số f(x) $= e^x \sin$ x.

[Lời giải] Xuất phát từ khai triển Maclaurin của hàm số g(x) $= e^x$

$e^x =$ 1 + x + $\frac{x^2}{2!}$ + $\cdots$ + $\frac{x^n}{n!}$ + $o(x^n)$

$\mathrm{v\grave{a}}\,h(x)=\sin$ x

$\sin$ x $=$ x - $\frac{x^3}{3!}$ + $\frac{x^5}{5!}$ + $\cdots$ + $(-1)^n \frac{x^{2n+1}}{(2n+1)!}$ + $o(x^{2n+1})$



ta có

$e^x \sin$ x $=$ x + $x^2$ + $\left(\frac{1}{2!}$ - $\frac{1}{3!}\right)x^3$ + $\cdots$

Ví dụ 9.11 (Giữa kì, 20173). Cho y $= e^x \sin$ x. Tính đạo hàm cấp cao $y<sup>(6)</sup>(0)$.

[Lời giải] Số hạng chứa $x^6$ trong khai triển Maclaurin của y $= e^x \sin$ x là

$x.(-1)^2 \frac{x^5}{5!}$ + $\frac{x^3}{3!}(-1)^1 \frac{x^3}{3!}$ + $\frac{x^5}{5!}x = -\frac{1}{90}x^6$.

Do đó,

$\frac{y^{(6)}(0)}{6!} = -\frac{1}{90} \Rightarrow y^{(6)}(0) =$ -8.

• Như vậy, nếu chỉ cần tìm một số số hạng đầu tiên trong khai triển Maclarin của

hàm số $e^x$ sin x thì có thể dùng phương pháp thực hiện phép nhân này.

• Tuy nhiên, để tìm được số hạng tổng quát thì phương pháp này lại không hiệu

quả. Thay vào đó, ta sẽ đi tính $f^{(n)}(x)$ bằng phương pháp quy nạp như trong Bài

tập 1.51d. Từ công thức

f'(x) $= e^x(\sin$ x + $\cos$ x) $= \sqrt{2}e^x \sin$ (x + $\frac{\pi}{4})$,

và

f''(x) $= \sqrt{2}e^x \left[\sin\left(x$ + $\frac{\pi}{4}\right)$ + $\cos\left(x$ + $\frac{\pi}{4}\right)\right] = (\sqrt{2})^2 e^x \sin\left(x$ + 2 $\cdot \frac{\pi}{4}\right)$

suy ra

$f^{(n)}(x) = (\sqrt{2})^n e^x \sin\left(x$ + $n\frac{\pi}{4}\right)$.

Do đó,

$e^x \sin$ x $= \sum_{n=1}^{\infty} \frac{(\sqrt{2})^n \sin \frac{n\pi}{4}}{n!} x^n$.

3. Phép chia cũng thực hiện như phép chia đa thức một cách bình thường.

4. Phép lấy hàm hợp. Chúng ta bắt đầu bằng một ví dụ đơn giản sau. Tìm chuỗi Maclau-

rin của hàm số f(x) $= \sin x^2$. Muốn tìm chuỗi Maclaurin một cách trực tiếp, ta cần

tính các đạo hàm cấp cao của hàm số f(x) $= \sin x^2$ rồi thay vào công thức

f(x) $=$ f(0) + $\frac{f'(0)}{1!}x$ + $\cdots$ + $\frac{f^{(n)}(0)}{n!}x^{n}$ + $o(x^{n})$.

Bằng cách tính các đạo hàm cấp một và cấp hai của f(x):

• f'(x) $=$ 2x $\cos x^2$,



• f''(x) $= -4x^2 \sin x^2$ + 2 $\cos x^2$,

chúng ta thấy rằng quá trình này sẽ rất phức tạp. Chúng ta có một phương pháp

khác. Đó là thực hiện phép đổi biến số, thay x bằng $x^2$ trong khai triển Maclaurin

của hàm số

$\sin$ x $=$ x - $\frac{x^3}{3!}$ + $\frac{x^5}{5!}$ + $\cdots$ + $(-1)^n \frac{x^{2n+1}}{(2n+1)!}$ + $\cdots$

$\mathbf{d}\mathbf{\hat{e}} \mathbf{d} \mathbf{u} \mathbf{c}$

$\sin x^2 = x^2$ - $\frac{x^6}{3!}$ + $\frac{x^{10}}{5!}$ + $\cdots$ + $(-1)^n \frac{x^{2(2n+1)}}{(2n+1)!}$ + $\cdots$

Bản chất của vấn đề ở đây là chúng ta cần đi tìm khai triển Maclaurin của hàm

số hợp (f $\circ$ g)(x) $=$ f(g(x)). Để tìm hiểu sâu thêm về vấn đề này, công thức Faà di

Bruno sau đây giúp chúng ta tính đạo hàm cấp cao của hàm hợp.

Đinh lý 1.36 (Công thức Faà di Bruno).

$f(g(x))^{(n)} = \sum \frac{n!}{m_1! \$, $1!^{m_1} \$, $m_2! \$, $2!^{m_2} \cdots m_n! \$, $n!^{m_n}} \cdot f^{(m_1$ + $\cdots$ + $m_n)}(g(x)) \cdot \prod_{j=1}^n \left( g^{(j)}(x) \right)^{m_j}$,

$i=1$

ở đó tổng được lấy trên tất cả các bộ số không âm $(m_1$, $\ldots$, $m_n)$ thỏa mãn

1 $\cdot m_1$ + 2 $\cdot m_2$ + 3 $\cdot m_3$ + $\cdots$ + n $\cdot m_n =$ n.

Hệ quả 1.5. Cho f(x) $= \sum_{n=0}^{\infty} a_n x^n$ và g(x) $= \sum_{n=0}^{\infty} b_n x^n$ là các chuỗi Maclaurin hình thức và $b_0 =$ 0. Khi đó, hàm số (f $\circ$ g)(x) có chuỗi Maclaurin hình thức là

$\sum_{n=0}^{\infty} c_n x^n$,

$\partial$ do $c_0 = a_0$ và

$c_n = \sum_{\mathbf{i} \in C_n} a_k b_{i_1} b_{i_2} \cdots b_{i_k}$

và

$C_n = \{(i_1$, $i_2$, $\ldots$, $i_k)$ : 1 $\leq$ k $\leq$ n, $i_1$ + $i_2$ + $\cdots$ + $i_k = n\}$.

Trường hợp đơn giản nhất, g(x) $= x^k$ thì chỉ việc thay x bằng $x^k$ trong khai triển

Maclaurin của f(x) để ra khai triển Maclaurin của $f(x^k)$ như trong ví dụ hàm số

f(x) $= \sin(x^2)$ đã nêu ở trên.

5. Phép lấy đạo hàm. Giả sử hàm số f(x) có khai triển Maclaurin là

f(x) $= a_0$ + $a_1$ x + $a_2 x^2$ + $a_3 x^3$ + $\cdots$ + $a_n x^n$ + $\cdots$



Khi đó hàm số $f^{\prime}(x)có$ khai triển Maclaurin là

f'(x) $= a_1$ + $2a_2x$ + $3a_3x^2$ + $\cdots$ + $na_nx^{n-1}$ + $\cdots$

được thực hiện bằng cách lấy đạo hàm của từng thành phần của chuỗi Maclaurin

của hàm f(x). Bạn đọc có thể tự kiểm tra bằng cách lấy đạo hàm chuỗi Maclaurin

của hàm sin x để ra chuỗi Maclaurin của hàm số cos x, hoặc lấy đạo hàm của chuỗi

Maclaurin của hàm số ln(1 + x) để ra chuỗi Maclaurin của hàm số $\frac{1}{1+x}$.

6. Phép lấy tích phân. Cũng tương tự như vậy, giả sử hàm số f(x) có khai triển Maclau-

rin là

f(x) $= a_0$ + $a_1$ x + $a_2 x^2$ + $a_3 x^3$ + $\cdots$ + $a_n x^n$

Khi đó hàm số $\int_0^x$ f(t)dt có khai triển Maclaurin là

$\int_{0}^{x}$ f(t)dt $= a_0x$ + $a_1\frac{x^2}{2}$ + $a_2\frac{x^3}{3}$ + $\dots$ + $a_n\frac{x^{n+1}}{n+1}$ + $\dots$

được thực hiện bằng cách lấy tích phân của từng thành phần của chuỗi Maclau-

rin của hàm f(x). Chẳng hạn, muốn tìm khai triển Maclaurin của hàm số f(x) $=$

arctan x, đầu tiên ta tìm chuỗi Maclaurin của hàm số

$\frac{1}{1+x^2}=1-x^2+x^4-\cdots+(-1)^nx^{2n}+\cdots$,

sau đó ta lấy tích phân hai về thì được

$\arctan$ x $= \int \frac{1}{1+t^2}$ dt $=$ x - $\frac{x^3}{3}$ + $\frac{x^5}{5}$ + $\dots$ + $(-1)^n \frac{x^{2n+1}}{2n+1}$ + $\dots$

Ứng dụng của khai triển Maclaurin

1. Tính gần đúng

Ví dụ 9.12. Tính gần đúng số e với sai số nhỏ hơn 0,0001.

Ta có $e^x =$ 1 + x + $\frac{x^2}{2!}$ + $\cdots$ + $\frac{x^n}{n!}$ + $\frac{c^{n+1}}{(n+1)!}$ với c là một số thực nào đó nằm giữa 0 và x.

Do đó ta xấp xỉ số e bằng

e $\approx$ 1 + 1 + $\frac{1}{2!}$ + $\cdots$ + $\frac{1}{n!}$

với sai số mong muốn $\frac{c^{n+1}}{(n+1)!} < \frac{1}{(n+1)!} <$ 0,0001. Điều này xảy ra nếu (n+1)! $>$ 1000 $\Leftrightarrow$

n $>$ 6. Nói cách khác,

e $\approx$ 1 + 1 + $\frac{1}{2!}$ + $\frac{1}{3!}$ + $\frac{1}{4!}$ + $\frac{1}{5!}$ + $\frac{1}{6!}$



2. Tính giới hạn

Ví dụ 9.13. Tính

$\lim_{x\to 0}\frac{x-\sin x}{x^3}$.

Chứng minh. Dựa vào khai triên Maclaurin của hàm f(x) $= \sin$ x ta có

$\sin$ x $=$ x - $\frac{x^3}{3!}$ + $o(x^3)$

nên

x - $\sin$ x $= \frac{x^3}{6}$ + $o(x^3) \sim \frac{x^3}{6}$ + $o(x^3)$

(theo quy tắc ngắt bỏ VCB bậc cao).

Do đó

$\n\lim_{x \to 0} \frac{x$ - $\sin x}{x^3} = \frac{1}{2}.\n$



Chú ý 1.13. Khi sử dụng khai triển Maclaurin để tính giới hạn, có thể khai triển

hàm số đến số hạng thích hợp. Chẳng hạn như ở Ví dụ bên trên, mẫu số là $x^3$ nên ta

chỉ khai triển tử số đến số hạng $x^3$, còn phần VCB bậc cao ở phía sau sẽ được ngắt

$b\r{o}$.

Ví dụ 9.14 (Giữa kì, K61). Tính giới hạn

b) $\lim_{x\to 0}\frac{e^x-\sin x-\cos x}{x^2}$.

a) $\lim_{x\to 0}\frac{e^{x}-\frac{1}{1-x}}{x^{2}}$.

Ví du 9.15 (Giữa kì, K62). Tìm a, b $\in \mathbb{R}$ sao cho

a) $\lim_{x\to 0} \frac{ax^2$ + b $\ln(\cos x)}{x^4} =$ 1.

b) $\lim_{x \to 0} \frac{ax$ + b $\sin(\sin x)}{x^3} =$ 1.

[Lời giải]

a) Ta có

$\ln(\cos$ x) $= \ln\left(1$ - $\frac{x^2}{2}$ + $\frac{x^4}{24}$ + $o(x^4)\right)$

$= \left(-\frac{x^2}{2}$ + $\frac{x^4}{24}\right)$ - $\frac{1}{2}\left(-\frac{x^2}{2}$ + $\frac{x^4}{24}$ + $o(x^4)\right)^2$ + $o(x^4)$

$= -\frac{x^2}{2}$ - $\frac{x^4}{12}$ + $o(x^4)$.

Do đó,

1 $= \lim_{x \to 0} \frac{ax^2$ + b $\ln(\cos x)}{x^4} = \lim_{x \to 0} \frac{\left(a$ - $\frac{b}{2}\right) x^2$ - $\frac{b}{12} x^4$ + $o(x^4)}{x^4} \Rightarrow$ a $=$ -6, b $=$ -12.



b)

$\sin(\sin$ x) $= \sin\left(x$ - $\frac{x^3}{6}$ + $o(x^4)\right)$

$=$ x - $\frac{x^3}{6}$ - $\frac{1}{6} \left($ x - $\frac{x^3}{6}$ + $o(x^4) \right)^3$ + $o(x^4)$

$=$ x - $\frac{x^3}{2}$ + $o(x^4)$.

Do đó,

1 $= \lim_{x \to 0} \frac{ax$ + b $\sin(\sin x)}{x^3} = \lim_{x \to 0} \frac{(a+b)x$ - $b\frac{x^3}{3}$ + $o(x^4)}{x^3} \Rightarrow$ a $=$ 3, b $=$ -3.

3. Tính đạo hàm cấp cao $f^{(n)}(0)$.

Ví dụ 9.16 (Giữa kì, K61). Tính đạo hàm cấp cao $y^{(10)}(0)$ với

a) y(x) $= e^{x^2}$,

c) y(x) $= \arctan$ x,

b) y(x) $= e^{-x^2}$,

d) y(x) $= \operatorname{arccot}$ x.

[Lời giải] Ngoài phương pháp dựa vào công thức truy hồi như ở Ví dụ 8.10, ta có thể

dựa vào khai triển Maclaurin.

a) Thay x bởi $x^2$ trong công thức khai triển Maclaurin của $e^x$ ta có

$e^{x^2} =$ 1 + $x^2$ + $\frac{(x^2)^2}{2!}$ + $\frac{(x^2)^3}{3!}$ + $\cdots$ + $\frac{(x^2)^n}{n!}$ + $\cdots = \sum_{n=1}^{+\infty} \frac{y^{(n)}(0)}{n!} x^n$.

So sánh hệ số của $x^{10}$ ta được

$\frac{y^{(10)}(0)}{10!} = \frac{1}{5!} \Rightarrow y^{(10)}(0) = \frac{10!}{5!} =$ 30240.

b) Tương tự câu a).

c) Thay x bằng $x^2$ trong khai triển Maclaurin của hàm số f(x) $= \frac{1}{1+x}$ ta được khai

triển Maclaurin của hàm số f(x) $= \frac{1}{1+x^2}$ như sau:

$\frac{1}{1+x^2}=1-x^2+x^4-\cdots+(-1)^nx^{2n}+\cdots$,

Lấy tích phân hai về ta được

$\arctan$ x $= \int_{0}^{t} \frac{1}{1+t^2}$ dt $=$ x - $\frac{x^3}{3}$ + $\frac{x^5}{5}$ + $\dots$ + $(-1)^n \frac{x^{2n+1}}{2n+1}$ + $\dots = \sum_{n=0}^{+\infty} \frac{y^{(n)}(0)}{n!} x^n$

So sánh hệ số của $x^{10}$ hai vế ta được $y^{(10)}(0) =$ 0.

Ví dụ 9.17 (Cuối kì, K62). Tính đạo hàm cấp cao $y^{(10)}(0)$ với



a) y(x) $= \sin(x^2)$.

b) y(x) $= cos(x^2)$.

[Lời giải]

a) Thay x bằng $x^2$ trong khai triển Maclaurin của sin x

$\sin$ x $= \sum_{n=0}^{+\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}$

ta dược

$\sin(x^2) = \sum_{n=0}^{+\infty} (-1)^n \frac{x^{2(2n+1)}}{(2n+1)!} = \sum_{n=0}^{+\infty} \frac{y^{(n)}(0)}{n!} x^n$.

So sánh hệ số của $x^{10}$ hai về ta được

$\frac{y^{(10)}(0)}{10!} = (-1)^2 \cdot \frac{1}{5!} \Rightarrow y^{(10)}(0) = \frac{10!}{5!} =$ 30240.

b) Tương tự câu a).

Ví dụ 9.18 (Giữa kì, K62). Tính đạo hàm cấp cao $y^{(9)}(0)$ với

b) g(x) $= \ln(1$ + x + $x^2)$.

a) f(x) $= \ln(1$ - x + $x^2)$.

[Lời giải]

a) Ta có

f(x) $= \ln(1$ - x + $x^2) = \ln(1$ + $x^3)$ - $\ln(1$ + x) $= x^3$ - $\frac{x^6}{2}$ + $\frac{x^9}{3}$ - $\sum_{n=1}^{9} \frac{(-1)^{n-1}x^n}{n}$ + $o(x^9)$

Hệ số của $x^9$ trong khai triển Maclaurin của f(x) bằng

$\frac{f^{(9)}(0)}{9!} = \frac{1}{3}$ - $\frac{1}{9} = \frac{2}{9}$.

Do đó,

$f^{(9)}(0) =$ 2.8! $=$ 80640

b) Tương tự câu a).

Ví dụ 9.19. a) Tìm khai triển Maclaurin của hàm số f(x) $= \arcsin$ x.

b) Tính đạo hàm cấp cao $arcsin<sup>(n)</sup>(0)$ (Giữa kì, K59).

[Lời giải]



a) Nhận xét (arcsin x)' $= \frac{1}{\sqrt{1-x^2}}$. Trong trường hợp này có lẽ "không có" hoặc "rất

khó" để tìm ra công thức tính đạo hàm cấp cao của hàm số arcsin x. Vì vậy, ta

xuất phát từ công thức khai triển Maclaurin của hàm số (1 + $x)^{\alpha}$

$(1+x)^{\alpha} = \sum_{n=1}^{\infty} \frac{\alpha(\alpha-1)\dots(\alpha-n+1)}{n!}x^n$.

Thay $\alpha = -\frac{1}{2}$ ta được

$\frac{1}{\sqrt{1+x}} = \sum_{n=0}^{\infty} \frac{-\frac{1}{2} \left(-\frac{1}{2}$ - $1\right) \cdots \left(-\frac{1}{2}$ - $(n-1)\right)}{n!} x^n = \sum_{n=0}^{\infty} \frac{(-1)^n (2n-1)!!}{2^n n!} x^n$.

Thay x bằng $-x^2$ ta được

$(\arcsin$ x)' $= \frac{1}{\sqrt{1-x^2}} = \sum_{n=0}^{\infty} \frac{(-1)^n (2n-1)!!}{2^n n!} (-x^2)^n = \sum_{n=0}^{\infty} \frac{(2n-1)!!}{(2n)!!} x^{2n}$

Do đó

$\arcsin$ x $= \int_{0}^{\infty} \sum_{n=0}^{\infty} \frac{(2n-1)!!}{(2n)!!} t^{2n}$ dt $= \sum_{n=0}^{\infty} \frac{(2n-1)!!}{(2n)!!} \int_{0}^{x} t^{2n}$ dt $= \sum_{n=0}^{\infty} \frac{(2n-1)!!}{(2n)!!} \frac{x^{2n+1}}{2n+1}$.

b) Dựa vào công thức khai triển Maclaurin của hàm số arcsin x suy ra

$ \begin{cases} \arcsin^{(2n)}(0) = 0, \\ \arcsin^{(2n+1)}(0) = [(2n-1)!!]^2. \end{cases} $

Ví dụ 9.20 (Cuối kì, 20152). Cho hàm số f(x) $= \frac{x}{1+x^3}$. Tính $d^{10}f(0)$.

[Lời giải] f(x) $=$ x $\cdot \frac{1}{1+x^3}$, áp dụng công thức Leibniz ta có

$f^{(n)}(x) =$ x $\cdot \left(\frac{1}{1+x^3}\right)^{(n)}$ + n $\cdot \left(\frac{1}{1+x^3}\right)^{(n-1)}$.

Thay x $=$ 0, n $=$ 10 vào ta có $f^{(10)}(0) = 10g^{(9)}(0)$, với g(x) $= \frac{1}{1$ + $x^3}$.

Ta có

$\frac{1}{1+x} =$ 1 - x + $x^2$ - $\dots$ + $(-1)^n x^n$ + $o(x^n) \Rightarrow \frac{1}{1+x^3} =$ 1 - $x^3$ + $(x^3)^2$ - $(x^3)^3$ + $\dots$

Từ đó suy ra hệ số của $x^9$ trong khai triển Maclaurin của g(x) $= \frac{1}{1+x^3}$ bằng

-1 $= \frac{g^{(9)}(0)}{9!} \Rightarrow g^{(9)}(0) =$ -9! $\Rightarrow f^{(10)}(0) =$ -10! $\Rightarrow d^{10}f(0) = -10!dx^{10}$

Bài tập 1.53. Tìm khai triển Maclaurin của hàm số f(x) $= \arccos$ x.

[Gợi ý] Có thể dựa vào đẳng thức arcsin x + $\arccos$ x $= \frac{\pi}{2}$ để suy ra khai triển Maclau-

rin của hàm số f(x) $= \arccos$ x.



## 9.3 Quy tắc L'Hospital None

### Định lý 1.37 (Quy tắc L'Hospital). Giả thiết

i) Các hàm số f(x), g(x) khả vi trong một lân cận nào đó của điểm $x_0$ (có thể trừ tại

điểm $x_0)$ đồng thời g'(x) $\neq$ 0 trong lân cân ấy,

ii) $\lim_{x \to x_0}$ f(x) $= \lim_{x \to x_0}$ g(x) $=$ 0 $\left($ kh $\dot{u} \$, $\text{dang} \$, $\frac{0}{0} \right)$.

Khi đó nếu tồn tại $\lim_{x \to x_0} \frac{f'(x)}{g'(x)} =$ A (có thể hữu hạn hoặc vô hạn) thì $\lim_{x \to x_0} \frac{f(x)}{g(x)} =$ A.

Chú ý 1.14. Quy tắc L'Hospital trên vẫn đúng nếu

• thay quá trình x $\rightarrow x_0$ bởi một trong các quá trình

x $\to x_0^+$, x $\to x_0^-$, x $\to +\infty$ hoặc x $\to -\infty$.

• thay điều kiện $\lim_{x \to x_0}$ f(x) $= \lim_{x \to x_0}$ g(x) $=$ 0 bởi

$\lim_{x \to x_0}$ f(x) $= \infty$, $\lim_{x \to x_0}$ g(x) $= \infty \left($ kh $\mathring{u} \$, $\operatorname{dang} \frac{\infty}{\infty} \right)$

$\acute{Y}$ tưởng chứng minh: Chúng ta chứng minh quy tắc L'Hospital cho trường hợp đơn giản,

$g'(x_0) \neq$ 0.

1. Nếu $f(x_0) = g(x_0) =$ 0 thì Với x $\neq x_0$ ta có

$\frac{f(x)}{g(x)} = \frac{f(x)$ - $f(x_0)}{g(x)$ - $g(x_0)} \stackrel{(Cauchy)}{=} \frac{f'(c)}{g'(c)}$,

c nằm giữa x và $x_0$.

Khi x $\to x_0$ thì c $\to x_0$. Do $\lim_{x \to x_0} \frac{f'(x)}{g'(x)} =$ A, suy ra

$\n\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{c \to x_0} \frac{f'(c)}{g'(c)} = A.\n$

2. Nếu chỉ có $\lim_{x\to x_0}$ f(x) $= \lim_{x\to x_0}$ g(x) $=$ 0 mà các hàm số chưa chắc đã xác định tại $x_0$. Ta

xây dựng

$ F(x) = \begin{cases} 0, & x = x_0 \\ f(x), & x \neq x_0, \end{cases} \quad G(x) = \begin{cases} 0, & x = x_0 \\ g(x), & x \neq x_0. \end{cases} $

3. Nếu x $\to \infty$, đặt y $= \frac{1}{x}$.

Ví du 9.21 (Giữa kì, K61). Tính giới hạn



a) $\lim_{x\to 0} \frac{\ln(1+x)$ - $\sin x}{x^2}$.

b) $\lim_{x\to 0} \frac{e^{2x}$ - $\sin 2x}{x^2}$.

Ví du 9.22. Tính các giới hạn sau:

a) $\lim_{x\to 0} \frac{x$ - $\sin x}{\arcsin^3 x}$,

c) $\lim_{x\to 0^+} x^{\alpha} \ln$ x,

d) $\lim_{x\to\infty}\frac{a^x}{x}$.

b) $\lim_{x\to 0^+} x^x$,

Chú ý 1.15.

• Hai qui tắc trên chỉ là điều kiện đủ để tìm lim $\frac{f(x)}{g(x)}$.

$x^2 \sin \frac{1}{x}$

Ví dụ như $\lim_{x\to 0} \frac{x}{\sin x} =$ 0 theo nguyên lý giới hạn kẹp, nhưng nếu áp dụng quy tắc

L'Hospital thì sẽ dẫn đến kết quả sai.

• Trong quá trình tìm giới hạn có dạng vô định, nên kết hợp cả thay tương đương với

dùng qui tắc L'Hospital để đạt được hiệu quả tốt nhất.

• Có thể dùng qui tắc L'Hospital nhiều lần.

Chú ý 1.16. Công thức L'Hospital được công bố lần đầu vào năm 1696 trong cuốn sách

Analyse des Infiniment Petits, pour intelligence des lignes courbes của nhà toán học người

Pháp Marquis de l'Hospital (1661-1704), nhưng nó lại được khám phá vào năm 1694 bởi

nhà toán học người Thụy Sỹ John (Johann) Bernoulli (1667-1748). Điều này được giải

thích vì hai nhà toán học có một thỏa thuận lạ kì, rằng Marquis de l'Hospital mua quyền

sở hữu các phát minh của Bernoulli trong một khoảng thời gian nhất định. Bức thư sau

đây của l'Hopital vào ngày 17 tháng 3 năm 1694 đã đề xuất một trong những thỏa thuận

khác thường nhất trong lịch sử khoa học.

"I will be happy to give you a retainer of 300 pounds, beginning with the first of Jan-

uary of this year ... I promise shortly to increase this retainer, which I know is very mod-

est, as soon as my affairs are somewhat straightened out ... I am not so unreasonable as

to demand in return all of your time, but I will ask you to give me at intervals some hours

of your time to work on what I request and also to communicate to me your discoveries, at

the same time asking you not to disclose any of them to others. I ask you even not to send

here to Mr. Varignon or to others any copies of the writings you have left with me; if they

are published, I will not be at all pleased. Answer me regarding all this ..."

## 9.4 Về một số dạng vô định are published, I will not be at all pleased. Answer me regarding all this ..."

Quy tắc L'Hospital, ngoài việc được áp dụng để khử dạng vô định $\frac{0}{0}$, $\frac{\infty}{\infty}$, còn có thể được

dùng để khử các dang vô định sau:



1. Dạng vô định 0 $\times \infty$. Chẳng hạn như muốn tính giới hạn $\lim_{x\to x_0}$ f(x)g(x) ta có thể viết

nó dưới dạng

$\n\lim_{x \to x_0} \frac{f(x)}{1/\varphi(x)}\n$

để áp dụng công thức L'Hospital.

Ví dụ 9.23. Tính $\lim_{x\to 0^+}$ x $\ln$ x.

2. Dạng vô định $\infty$ - $\infty$. Để tính các giới hạn này chúng ta đưa phép trừ về dạng phép

thương, chẳng hạn như quy đồng mẫu số, đặt nhân tử chung.

Ví dụ 9.24. Tính $\lim_{x\to 0} \left(\frac{1}{x}$ - $\frac{1}{\sin x}\right)$.

3. Tính các giới hạn có dạng $\lim_{x\to x_0} A(x)^{B(x)}$. Đặt f(x) $= A(x)^{B(x)}$ và đi tính

$\lim_{x \to x_0} \ln$ f(x) $= \lim_{x \to x_0}$ B(x) $\ln$ A(x) $= \lim_{x \to x_0} \frac{\ln A(x)}{1/B(x)}$

bằng cách áp dụng công thức L'Hospital.

• Nếu $\lim_{x\to x_0} \frac{\ln A(x)}{1/B(x)}$ có dạng $\frac{0}{0}$, nghĩa là

$\n\lim_{x \to x_0} \ln$ A(x) $=$ 0, $\lim_{x \to x_0}$ 1/B(x) $= 0.\n$

Khi đó, $\lim_{x\to x_0}$ A(x) $=$ 1, $\lim_{x\to x_0}$ B(x) $= \infty$ ta có dạng vô định $1^{\infty}$.

• Nếu $\lim_{x\to x_0} \frac{\ln A(x)}{1/B(x)}$ có dạng $\frac{\infty}{\infty}$, nghĩa là

$\n\lim_{x \to x_0} \ln$ A(x) $= \infty$, $\lim_{x \to x_0}$ 1/B(x) $= \infty.\n$

Khi đó,

- hoặc $\lim_{x\to x_0}$ A(x) $=$ 0, $\lim_{x\to x_0}$ B(x) $=$ 0 ta có dạng vô định $0^0$,

- hoặc là $\lim_{x\to x_0}$ A(x) $= \infty$, $\lim_{x\to x_0}$ B(x) $=$ 0 ta có dạng vô định $\infty^0$.

Chú ý rằng chỉ có ba dạng vô định $0^0$, $1^{\infty}$, $\infty^0$ cho các giới hạn có dạng $\lim_{x\to x_0} A(x)^{B(x)}$.

Các trường hợp khác hay bị nhầm lẫn sau đây đều không phải là dạng vô định

và có thể tính trực tiếp dựa vào các quy tắc tính giới hạn:

$0^1 =$ 0, $0^{+\infty} =$ 0, $0^{-\infty} = +\infty$, $1^0 =$ 1, $1^1 =$ 1, $\infty^1 = \infty$, $\infty^{\infty} = \infty$.



## 9.5 Thay tương đương khi có hiệu hai VCB? None

Đây có lẽ là một câu hỏi thú vị và được rất nhiều ban đọc quan tâm. Chúng ta bắt đầu

với một ví du sau đây.

Ví du 9.25 (Câu 6, Đề 4, Giữa kì K61). Tính

$\n\lim_{x\to 0}\frac{e^x-\sin x-\cos x}{r^2}.\n$

[Lời giải]

Cách 2: Dùng quy tắc L'Hospital

Cách 1: Thay tương đương

$\lim_{x \to 0} \frac{e^x$ - $\sin$ x - $\cos x}{x^2}$

$\n\lim_{x \to 0} \frac{e^x$ - $\sin$ x - $\cos x}{x^2}\n$

$= \lim_{x \to 0} \frac{(e^x$ - 1) - $\sin$ x + (1 - $\cos x)}{x^2}$

$= \lim_{x \to 0} \frac{e^x$ - $\cos$ x + $\sin x}{2x}$

$= \lim \frac{x$ - x + $\frac{x^2}{2}}{2}$

$= \lim_{x \to 0} \frac{e^x$ + $\sin$ x + $\cos x}{2}$

$\chi^2$

$x\rightarrow$ 0

$x\rightarrow$ 0

$=\frac{1}{2}$

$=1$.

Trong hai cách giải trên chắc chắn có một cách giải sai, và sai lầm ở đâu? Đây là sai lầm

nhiều người hay mắc phải khi thay tương đương trong các biểu thức có chứa dấu $\pm$.

Chú ý 1.17. Nếu $\alpha_1(x)$, $\alpha_2(x)$, $\beta_1(x)$, $\beta_2(x)$ là các VCB khi x $\rightarrow x_0$ và $\alpha_1(x) \sim \alpha_2(x)$, $\beta_1(x) \sim$

$\beta_2(x)$ thì

• $\alpha_1(x)\beta_1(x) \sim \alpha_2(x)\beta_2(x)$

• $\lim_{x \to r_0} \frac{\alpha_1(x)}{\beta_1(x)} = \lim_{x \to r_0} \frac{\alpha_2(x)}{\beta_2(x)}$

nhưng chưa chắc $\alpha_1(x) \pm \beta_1(x) \sim \alpha_2(x) \pm \beta_2(x)$. Chẳng hạn, sin x $\sim$ x, tan x $\sim$ x khi x $\to$ 0,

nhưng tan x - $\sin$ x $\sim \frac{1}{2}x^3$.

Vậy có thay tương $đượ<br/>c$ trong biểu thức có dấu $\pm$ hay không không? Đây là một

câu hỏi rất thú vị. Muốn biết biểu thức $\alpha_1(x)$ - $\beta_1(x)$ có tương đương với $\alpha_2(x)$ - $\beta_2(x)$ hay

không thì chúng ta quay về Định nghĩa, đi tính $\lim_{x\to a} \frac{\alpha_1(x)-\beta_1(x)}{\alpha_2(x)-\beta_2(x)}$. Ta chia làm 4 trường hợp

như sau:

1. Nếu $\alpha_1(x)$ là VCB bậc cao hơn $\beta_1(x)$ thì $\lim_{x\to a} \frac{\alpha_1(x)}{\beta_1(x)} = \lim_{x\to a} \frac{\alpha_2(x)}{\beta_2(x)} =$ 0 (theo định nghĩa của VCB bậc cao). Khi đó $\lim_{x\to a} \frac{\alpha_1(x)$ - $\beta_1(x)}{\alpha_2(x)$ - $\beta_2(x)} = \lim_{x\to a} \frac{\frac{\alpha_1(x)}{\beta_1(x)}$ - $1}{\frac{\alpha_2(x)}{\beta_2(x)}$

tương đương với $\alpha_2(x)$ - $\beta_2(x)$.



2. Nếu $\beta_1(x)$ là VCB bậc cao hơn $\alpha_1(x)$ thì $\lim_{x\to a} \frac{\beta_1(x)}{\alpha_1(x)} = \lim_{x\to a} \frac{\beta_2(x)}{\alpha_2(x)} =$ 0 (theo định nghĩa của

VCB bậc cao). Khi đó $\lim_{x\to a} \frac{\alpha_1(x)-\beta_1(x)}{\alpha_2(x)-\beta_2(x)} = \lim_{x\to a} \frac{\frac{\beta_1(x)}{\alpha_1(x)}-1}{\frac{\beta_2(x)}{\alpha_2(x)}-1} \cdot \frac{\alpha_1(x)}{\alpha_2(x)} = \frac{0-1}{0-1} =$ 1. Vậy $\alpha_1(x)$ - $\beta_1(x)$

tương đương với $\alpha_2(x)$ - $\beta_2(x)$.

3. Nếu $\alpha_1(x)$ và $\beta_1(x)$ là các VCB cùng bậc nhưng không tương đương thì $\lim_{x\to a} \frac{\alpha_1(x)}{\beta_1(x)} =$

A $\neq$ 1. Khi đó $\lim_{x \to a} \frac{\alpha_1(x)$ - $\beta_1(x)}{\alpha_2(x)$ - $\beta_2(x)} = \lim_{x \to a} \frac{\frac{\alpha_1(x)}{\beta_1(x)}$ - $1}{\frac{\alpha_2(x)}{\beta_2(x)}$ - $1} \cdot \frac{\beta_1(x)}{\beta_2(x)} = \frac{A-1}{A-1} =$ 1. Vậy $\alpha_1(x)$ - $\beta_1(x)$ tương

đương với $\alpha_2(x)$ - $\beta_2(x)$.

4. Nếu $\alpha_1(x)$ và $\beta_1(x)$ là các VCB tương đương thì $\lim_{x \to a} \frac{\alpha_1(x)}{\beta_1(x)} =$ 1. Khi đó $\lim_{x \to a} \frac{\alpha_1(x)$ - $\beta_1(x)}{\alpha_2(x)$ - $\beta_2(x)} =$

$\lim_{x\to a} \frac{\frac{\alpha_1(x)}{\beta_1(x)}-1}{\frac{\alpha_2(x)}{\beta_2(x)}-1} \cdot \frac{\beta_1(x)}{\beta_2(x)} = \frac{1-1}{1-1}$ là dạng vô định $\frac{0}{0}$ nên không xác định được giới hạn của nó.

5. Nếu $\alpha_1(x)$ và $\beta_1(x)$ là các VCB không so sánh được với nhau, thì $\alpha_1(x)$ - $\beta_1(x)$ và

$\alpha_2(x)$ - $\beta_2(x)$ có thể không so sánh được với nhau.

Kết luận: Nếu $\alpha_1(x)$, $\alpha_2(x)$, $\beta_1(x)$, $\beta_2(x)$ là các VCB khi x $\to x_0$ và $\alpha_1(x) \sim \alpha_2(x)$, $\beta_1(x) \sim$

$\beta_2(x)$ thì $\alpha_1(x)$ - $\beta_1(x) \sim \alpha_2(x)$ - $\beta_2(x)$ ngoại trừ trường hợp $\alpha_1(x)$ và $\beta_1(x)$ là các

VCB tương đương hoặc không so sánh được với nhau. Ví dụ, không thay tương

đương được trong biểu thức tan x - $\sin$ x vì tan x $\sim \sin$ x, nhưng vẫn thay tương đương

được trong biểu thức tan 2x - $\sin$ x $\sim$ 2x - x $=$ x hoặc sin x - $\tan^2$ x $\sim$ x - $x^2 \sim$ x. Bạn đọc

cần nắm vững điều này, và trong trường hợp không chắc chắn thì tốt nhất nên

tránh thay tương đương trong các biểu thức có chứa dấu cộng và dấu trừ.

Trường hợp $\alpha_1(x)$ + $\beta_1(x)$ có tương đương với $\alpha_2(x)$ + $\beta_2(x)$ hay không chúng ta lập luận

tương tự. Vẫn thay tương đượng được bình thường ngoại trừ trường hợp $\alpha_1(x)$ và $-\beta_1(x)$

là các VCB tương đương hoặc không so sánh được với nhau.

Quay trở lại Ví dụ 9.25 nêu trên thì sai lầm là ở chỗ chúng ta đã thay tương tương

$(e^x$ - 1) - $\sin$ x $\sim$ x - x $=$ 0 để dẫn đến $(e^x$ - 1) - $\sin$ x + (1 - $\cos$ x) $\sim \frac{x^2}{2}$. Chúng ta không

thực hiện được điều này bởi vì $e^x$ - 1 $\sim \sin$ x. Thực tế thì $(e^x$ - 1) - $\sin$ x là một VCB khi

x $\rightarrow$ 0 và nếu nhìn vào khai triển Maclaurin của các hàm số $e^x$ và sin x thì ta thấy

• $e^x =$ 1 + x + $\frac{x^2}{2}$ + $o(x^2)$

• $\sin$ x $=$ x + $o(x^2)$ (số hạng tiếp theo trong khai triển này là $-\frac{x^3}{3!} = o(x^2))$

nên

$(e^x$ - 1) - $\sin$ x $= \frac{x^2}{2}$ + $o(x^2) \sim \frac{x^2}{2}$.

Cho nên khi thay $(e^x$ - 1) - $\sin$ x $\sim$ x - x $=$ 0 nghiễm nhiên chúng ta đã làm mất đi số

hạng $\frac{x^2}{2}$.



Ví dụ 9.26 (Câu 5, Đề 1, Giữa kì K61). Tính

$\n\lim_{x\to 0}\frac{e^x-\cos x-\ln(1+x)}{r^2}.\n$

[Gợi ý] Một cách tương tự, hãy chỉ ra rằng với bài tập trên nếu

• thay tương đương ta được kết quả bằng $\frac{1}{2}$ (SAI)

• dùng công thức L'Hospital hoặc khai triển Maclaurin ta được kết quả bằng $\frac{3}{2}$ (ĐÚNG).

## 9.6 Hiêu hai VCB tương đương • dùng công thức L'Hospital hoặc khai triển Maclaurin ta được kết quả bằng <math>\frac{3}{2}</math> (<b>ĐÚNG</b>).

Trong mục trước, chúng ta biết rằng không thay tương đượng được trong biểu thức

$\alpha(x)$ - $\beta(x)$ nếu $\alpha(x)$ và $\beta(x)$ là các VCB tương đương. Vậy hiệu của hai VCB tương đương

là gì?

Bổ đề 1.1. Hiệu của hai VCB tương đương là một VCB bậc cao hơn cả hai VCB đó.

Chứng minh. Giả sử $\alpha(x) \sim \beta(x)$ khi x $\rightarrow x_0$. Khi đó,

$\n\lim_{x \to x_0} \frac{\alpha(x)$ - $\beta(x)}{\alpha(x)} =$ 1 - $\lim_{x \to x_0} \frac{\beta(x)}{\alpha(x)} =$ 1 - 1 $= 0.\n$

Vậy theo định nghĩa, $\alpha(x)$ - $\beta(x)$ là một VCB bậc cao hơn $\alpha(x)$.

$\blacksquare$

Ví dụ 9.27 (Một số ví dụ về hiệu hai VCB tương đương).

h) tan x - $\arcsin$ x $\sim \frac{x^3}{6}$

a) x - $\sin$ x $\sim \frac{x^3}{6}$

b) x - $\tan$ x $\sim -\frac{x^3}{3}$

i) tan x – arctan x $\sim \frac{2x^3}{3}$

c) x - $\arcsin$ x $\sim -\frac{x^3}{6}$

j) arcsin x – arctan x $\sim \frac{x^3}{2}$

d) x - $\arctan$ x $\sim \frac{x^3}{3}$

k) x - $(e^x$ - 1) $\sim -\frac{x^2}{2}$

e) $\sin$ x - $\tan$ x $\sim -\frac{x^3}{2}$

1) x - $\ln(1+x) \sim \frac{x^2}{2}$

f) sin x – arcsin x ~ $-\frac{x^3}{3}$

g) sin x – arctan x $\sim \frac{x^3}{6}$

m) (1 - $\cos$ x) - $\frac{x^2}{2} \sim -\frac{x^4}{24}$

Hiệu hai VCB cùng bậc là một VCB bậc cao hơn cả hai VCB đó, vậy cụ thể, cao hơn là

bậc bằng bao nhiêu? Lấy, chẳng hạn, $\alpha(x) =$ x, ở ví dụ trên ta đã chỉ ra một số hiệu của

hai VCB tương đương "trong tự nhiên", như là x - $\sin$ x $\sim \frac{x^3}{6}$ cùng bậc với VCB $\alpha(x) = x^3$,

còn x - $(e^x$ - 1) $\sim -\frac{x^2}{2}$ cùng bậc với VCB $\beta(x) = x^2$ khi x $\to$ 0. Với các VCB tương đương

"nhân tạo" sau đây thì x - $\beta(x)$ có thể cùng bậc với $x^a$ (a $>$ 1) bất kì. Chẳng hạn như muốn

x - $\beta(x) \sim x^{2017}$ thì chỉ cần chọn $\beta(x) =$ x - $x^{2017}$. Khi đó,

x $\sim$ x - $x^{2017}$ (ngắt bỏ VCB bâc cao), và x - (x - $x^{2017}) = x^{2017}$



## 9.7 Ba phương pháp (mới) để tính giới hạn None

Như vậy đến thời điểm hiện tại chúng ta đã học được ba phương pháp mới để tính giới

hạn, đó là

• Phương pháp sử dụng VCB-VCL (thay tương đương, ngắt bỏ),

• Phương pháp dùng khai triển Maclaurin,

• Phương pháp dùng quy tắc L'Hospital.

Mỗi một phương pháp đều có các ưu, nhược điểm riêng và tương ứng với các bài toán đặc

thù. Để so sánh các phương pháp này với nhau, ta minh họa bằng vẽ và 6 Ví dụ sau đây.



![](graphs/graph_77_1.png)



![](graphs/graph_77_2.png)



![](graphs/graph_77_0.png)

VCB

Maclaurin

Ví dụ 1 (Cả ba phương pháp đều áp dụng được).

$\n\lim_{x \to 0} \frac{1$ - $\cos x}{\ln(1$ + $x^2)}\n$

Ví du 2 (Sử dụng VCB hoặc khai triển Maclaurin. Không nên dùng L'Hospital).

$\lim_{x \to 0} \frac{1$ - $\cos$ x + $x^2$ - $\sin x}{x$ + $\sin^2$ x + $\arcsin^3$ x + $\arctan^4 x}$

Ví du 3 (Sử dụng khai triển Maclaurin hoặc L'Hospital. Không thay tương đương).

$\n\lim_{x \to 0} \frac{x$ - $\sin$ x + $x^3}{x^3}.\n$



Ví du 4 (Khai triển Maclaurin. Không thay tương đương (tử số) và L'Hospital).

$\n\lim_{x\to 0} \frac{x$ - $\sin$ x - $x^3}{\arcsin(\arctan^3 x)}.\n$

Ví du 5 (Sử dụng L'Hospital. Không dùng VCB, Maclaurin).

$\lim_{x\to 0^+}\frac{\ln x}{x},\ \text{ho\n\check{a}c}\ \lim_{x\to 0^+}x^x$.

Ví du 6 (Không dùng cả ba phương pháp trên).

$\n\lim_{x \to +\infty} \frac{x$ - $\sin x}{x$ + $\cos x}.\n$

[Lời giải]

$\n\lim_{x \to \infty} \frac{x$ - $\sin x}{x$ + $\cos x} = \lim_{x \to \infty} \frac{1$ - $\frac{\sin x}{x}}{1$ + $\frac{\cos x}{x}} = 1.\n$

Chú ý 1.18. Trong quá trình tìm giới hạn của các dạng vô định, nên linh hoạt trong cách

xử lý, có thể kết hợp nhiều phương pháp với nhau để đạt hiệu quả tốt nhất. Chẳng hạn

như trong Ví dụ (4) nêu trên,

$\n\lim_{x\to 0} \frac{x$ - $\sin$ x - $x^3}{\arcsin(\arctan^3 x)}\n$

nên sử dụng khai triển Maclaurin ở tử số và thay tương đương ở mẫu số.

## 9.8 Về các VCL tiêu biểu nên sử dụng khai triển Maclaurin ở tử số và thay tương đương ở mẫu số.

Chúng ta đã học về các VCB, VCL, các quy tắc thay tương đương, các quy tắc ngắt bỏ

VCB bậc cao, ngắt bỏ VCL bậc thấp. Tuy nhiên, các bài tập về VCL thường hay bị lãng

quên vì một lý do nào đó. Chúng ta đã học các VCB tương tương hay dùng, nhưng chưa có

nhiều ví dụ về các VCL. Chính vì vậy, mục này sẽ dành riêng để nói về ba VCL tiêu biểu

(khi x $\to +\infty)$, đó là

• Các hàm số mũ với cơ số lớn hơn 1, ví dụ $a^x$ (a $>$ 1),

• Các hàm số đa thức, các hàm số là lũy thừa của x, chẳng hạn $x^n$, $x^{\alpha}$, $(\alpha >$ 0),

• Các hàm số logarit với cơ số lớn hơn 1, như $\ln$ x, $\log_a$ x (a $>$ 1).

Cả ba hàm số này đều tiến ra vô cùng khi x $\to +\infty$, tuy nhiên với tốc độ khác nhau. Trong

ba hàm số này thì hàm số mũ (với cơ số lớn hơn 1) là VCL có bậc cao nhất (tiến ra vô cùng

với tốc độ nhanh nhất), sau đó đến các hàm số đa thức, và cuối cùng là các hàm số logarit

(với cơ số lớn hơn 1).



Hàm số mũ $\succ$ Hàm số đa thức $\succ$

$\overline{\mathbf{H}}àm$ số logarit

Cụ thể, bạn đọc có thể tự chứng minh dễ dàng hai giới hạn sau (bằng cách dùng quy

tắc L'Hospital):

$\n\lim_{x \to +\infty} \frac{a^x}{x^a} = \infty$, $\lim_{x \to +\infty} \frac{x^a}{\log_{\alpha} x} = \infty$, $\ \forall$ a $>$ 1, $\alpha > 0.\n$

Ví du 9.28. Tính

$\lim_{x \to +\infty} \frac{\ln$ x + $x^{2016}$ + $e^x}{\log_2$ x + $x^{2017}$ + $2e^x}$.

$ Áp dụng quy tắc ngắt bỏ VCL bậc thấp ta được, \begin{cases} \ln x + x^{2016} + e^x \sim e^x, \\ \log_2 x + x^{2017} + 2e^x \sim 2e^x \end{cases} khi x \to +\infty. $

Do $d\acute{o}$,

$\lim_{x \to +\infty} \frac{\ln$ x + $x^{2016}$ + $e^x}{\log_2$ x + $x^{2017}$ + $2e^x} = \frac{1}{2}$.

Bạn đọc sẽ thường xuyên gặp lại các VCL này khi học về Tích phân suy rộng (trong học

phần Giải tích I này) và Chuỗi số (trong học phần Giải tích III, học kì 2).

## 9.9 Bài tập ôn tập phần Giải tích I này) và Chuỗi số (trong học phần Giải tích III, học kì 2).

Bài tập 1.54. Chứng minh rằng phương trình $x^n$ + px + q với n nguyên dương không thể

có quá 2 nghiệm thực nếu n chẵn và không thể có quá 3 nghiệm thực nếu n lẻ.

Chứng minh. Xét n chẵn, giả sử phương trình có 3 nghiệm thực $x_1 < x_2 < x_3$, khi đó tồn

tại $c_1 \in (x_1$, $x_2)$, $c_2 \in (x_2$, $x_3)$ sao cho $f'(c_1) = f'(c_2) =$ 0. Tức là phương trình $x^{n-1} = -\frac{p}{n}$ có

2 nghiệm thực, điều này mâu thuẫn do n chẵn.

Xét n lẻ, giả sử phương trình có 4 nghiệm thực $x_1 < x_2 < x_3 < x_4$, khi đó theo định lý

Rolle, phương trình $x^{n-1}$ + $\frac{p}{n} =$ 0 có 3 nghiệm thực, trong khi theo trên ta vừa chứng minh

thì nó không thể có quá 2 nghiệm thực do n-1 chẵn.



Bài tập 1.55. Giải thích tại sao công thức Cauchy dạng $\frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(c)}{g'(c)}$ không áp

dụng được với các hàm số f(x) $= x^2$, g(x) $= x^3$, -1 $\le$ x $\le$ 1

Bài tập 1.56. Chứng minh các bất đẳng thức

b) $\frac{a-b}{a} < \ln \frac{a}{b} < \frac{a-b}{b}$, 0 $\le$ b $\le$ a.

a) $|\sin$ x - $\sin$ y| $\le$ |x - y|



a) Xét hàm số f(t) $= \sin$ t, thoả mãn điều kiện của định lý Lagrange

Chứng minh.

trong khoảng [x, y] bất kì. Khi đó $\exists$ c $\in$ [x, y] sao cho

$\sin$ x - $\sin$ y $=$ f'(c)(x - y) $= \cos$ c(x - y) $\Rightarrow |\sin$ x - $\sin$ y| $\le$ |x - y|

b) Xét hàm số f(x) $= \ln$ x, thoả mãn điều kiện của định lý Lagrange trong khoảng [b, a]

$n\hat{e}n$

$\ln$ a - $\ln$ b $=$ f'(c)(a - b) $\Rightarrow \ln \frac{b}{a} = \frac{1}{c}(b$ - a) $\Rightarrow \ln \frac{a}{b} = \frac{a$ - $b}{c}$

Vậy

$\frac{a-b}{a} < \ln \frac{a}{b} < \frac{a-b}{b}$, $\text{$ do $}$ b $<$ c $<$ a.

Bài tập 1.57. Tìm giới hạn

(a) $\lim_{x \to +\infty} \sqrt{x$ + $\sqrt{x}$ + $\sqrt{x}}$ - x $\ (\infty$ - $\infty)$,

(f) $\lim_{x\to 1^-} \frac{\tan \frac{\pi x}{2}}{\ln(1-x)} \left(\frac{\infty}{\infty}\right)$

(b) $\lim_{x\to 1}\left(\frac{x}{x-1}-\frac{1}{\ln x}\right) \;(\infty-\infty)$,

(g) $\lim_{x\to 0^+} x^{\sin x} (0<sup>0</sup>)$,

(c) $\lim_{x \to \infty} \frac{e^{\frac{1}{x}}$ - $\cos \frac{1}{x}}{1$ - $\sqrt{1$ - $\frac{1}{x^2}}} \left( \frac{0}{0} \right)$,

(h) $\lim_{x\to 0}$ (1 - a $\tan^2 x)^{\frac{1}{x \sin x}} (1^{\infty})$,

(i) $\lim_{x\to 0}$ (1 - $\cos x)^{\tan x} (0^0)$,

(d) $\lim_{x\to 0} \frac{e^x \sin$ x - $x(1+x)}{x^3} \left(\frac{0}{0}\right)$,

(j) $\lim_{x \to \frac{\pi}{2}} (\sin x)^{\tan x} (1^{\infty})$.

(e) $\lim_{x\to 1} \tan \frac{\pi x}{2} \ln(2-x) (\infty.0)$,

[Gợi $\acute{y}]$

(a) Sử dụng phương pháp nhân liên hợp, đáp số: $\frac{1}{2}$.

(b) Quy đồng mẫu số rồi sử dụng công thức L'Hospital, đáp số: $\frac{1}{2}$.

(c) Đặt t $= \frac{1}{x}$, sau đó độc giả có thể dùng khai triển Maclaurin hoặc công thức L'Hospital,

đáp số: $\infty$.

(d) Sử dụng khai triển Maclaurin hoặc công thức L'Hospital, đáp số: $\frac{1}{3}$.

(e) Sử dụng trực tiếp công thức L'Hospital (đưa tan $\frac{\pi x}{2}$ xuống mẫu số), hoặc đặt t $=$ 1 - x

và dùng công thức thay tương đương. đáp số: $\frac{2}{\pi}$.

(f) Sử dụng công thức L'Hospital, đáp số: $-\infty$.

(g) Sử dụng công thức lim $A(x)^{B(x)} = e^{\lim$ B(x) $\ln A(x)}$, đáp số: 1.



(h) Sử dụng công thức lim $A(x)^{B(x)} = e^{\lim$ B(x) $\ln A(x)}$, đáp số: $e^{-a}$.

(i) Sử dụng công thức lim $A(x)^{B(x)} = e^{\lim$ B(x) $\ln A(x)}$, đáp số: 1.

(j) Sử dụng công thức lim $A(x)^{B(x)} = e^{\lim$ B(x) $\ln A(x)}$, đáp số: 1.

Bài tập 1.58. Tính các giới hạn sau

(a) $\lim_{x\to\infty} \left|$ x - $x^2 \ln \left($ 1 + $\frac{1}{x} \right) \right|$,

(i) $\lim_{x\to 0} \left( \frac{1-\cos^2 x}{x \sin 2x} \right)$,

(b) $\lim_{x \to 0} \frac{1}{x} \left( \frac{1}{x}$ - $\cot$ x $\right) = \frac{\sin$ x - x $\cos x}{x^2 \sin x}$,

(j) $\lim_{x\to 0} \left( \frac{1}{x}$ - $\frac{1}{e^x$ - $1} \right)$,

(c) $\lim_{x\to 0} x^{-5} [\sin(\sin$ x) - x $\sqrt[3]{1$ - $x^2}]$,

(k) $\lim_{x \to +\infty} (\frac{2}{\pi} \arctan x)^x$,

(d) $\lim_{x\to 0} [\ln(1+x)^{\frac{1}{x^2}}$ - $\frac{e^x}{x}]$,

(l) $\lim_{x\to 0} \frac{\arctan x}{\sin$ x - $x}$,

(e) $\lim_{x \to 0} \frac{\cos$ x - $e^{-\frac{x^2}{2}}}{x^4}$,

(m) $\lim_{x\to 0^+} \frac{\ln x}{1$ + 2 $\ln(\sin x)}$,

(f) $\lim_{x \to 0} \frac{x$ - $\ln(1$ + $x)}{x^2}$,

(n) $\lim_{x\to 0} \frac{\sin$ x - x $\cos x}{x^3}$,

(o) $\lim_{x \to 0} \frac{x^2}{\sqrt{1$ + x $\sin x}$ - $\sqrt{\cos x}}$,

(g) $\lim_{x\to 0} \left( \frac{1}{x}$ - $\frac{1}{\sin x} \right) = \frac{\sin$ x - $x}{x \sin x}$,

(p) $\lim_{x\to 0} \frac{\ln(\cos ax)}{\ln(\cos bx)}$, a $\neq$ 0, b $\neq$ 0.

(h) $\lim_{x\to 0} \left( \frac{\tan$ x - $x}{x$ - $\sin x} \right)$,

[Goi $\hat{y}]$

(a) Đáp số: $\frac{1}{2}$.

(h) L'Hospital, đáp số: 2.

(i) L'Hospital, đáp số: $\frac{1}{2}$.

(b) Khai triển Taylor, đáp số: $\frac{1}{3}$.

(j) Quy đồng mẫu số và L'Hospital, đáp

(c) DS: $\frac{7}{45}$.

$\hat{\text{so}}: \frac{1}{2}$.

(d) Khai triển Taylor, đáp số: $-\frac{3}{2}$.

(k) BS: $e^{-\frac{2}{\pi}}$.

(e) Khai triển Taylor, đáp số: $-\frac{1}{12}$.

(l) L'Hospital, đáp số: $\infty$.

(f) Khai triển Taylor hoặc L'Hospital, đáp

(m) L'Hospital, đáp số: $\frac{1}{2}$.

$\hat{\text{so}}: \frac{1}{2}$.

(n) L'Hospital, đáp số: $\frac{1}{3}$.

(g) Khai triển Taylor hoặc L'Hospital, đáp

(o) Nhân liên hợp, đáp số: $\frac{4}{3}$.

$\hat{\textbf{so}}:$ 0.



$rac{a^2}{h^2}$.

(p) L'Hospital, thay tương đương, đáp số:

Bài tập 1.59. Chứng minh rằng $\lim_{x\to\infty} \frac{x-\sin x}{x+\cos x}$ tồn tại và bằng 1 nhưng không tính được

bằng quy tắc L'Hospital.

Chứng minh.

$\n\lim_{x \to \infty} \frac{x$ - $\sin x}{x$ + $\cos x} = \lim_{x \to \infty} \frac{1$ - $\frac{\sin x}{x}}{1$ + $\frac{\cos x}{x}} = 1.\n$

Nếu áp dụng quy tắc L'Hospital một cách hình thức thì ta có

$\n\lim_{x \to \infty} \frac{x$ - $\sin x}{x$ + $\cos x} = \lim_{x \to \infty} \frac{1$ - $\cos x}{1$ - $\sin x}\n$

Tuy nhiên giới hạn ở về phải không tồn tại, có thể kiểm tra bằng cách chọn 2 dãy $x_k =$

$2k\pi \text{$ và $} y_k = \frac{\pi}{2} = 2k\pi$

$\blacksquare$

Bài tập 1.60. Tính các giới hạn sau:

a) $\lim_{x \to \infty} \left( \frac{2}{\pi} \arctan$ x $\right)^x$,

b) $\lim_{x \to \infty} \left( \frac{a^{1/x}$ + $b^{1/x}}{2} \right)^x$, a, b $>$ 0.

Bài tập 1.61. Dùng khai triển Maclaurin để tính các giới hạn sau:

b) $\lim_{x \to 0} \frac{(\cosh$ x - 1) $\ln(1$ + x) - $x^3/2}{x(\sin$ x - $\arcsin x)}$. (2)

a) $\lim_{x \to 0} \frac{1$ - $\sqrt{1$ + $x^2 \cos x}}{x(\tan$ x - $\sinh x)}$, (1)

Bài tập 1.62. Xác định a, b sao cho biểu thức sau đây có giới hạn hữu hạn khi $x\rightarrow$ 0

f(x) $= \frac{1}{\sin^3 x}$ - $\frac{1}{x^3}$ - $\frac{a}{x^2}$ - $\frac{b}{x} = \frac{x^3$ - $\sin^3$ x (1 + ax + $bx^2)}{x^3 \sin^3 x}$

Chứng minh. Tại lân cận của x $=$ 0, ta có thể viết

$\sin$ x $=$ x - $\frac{x^3}{3!}$ + $o(x^3)$

do đó

Mẫu số $= x^3[x$ - $\frac{x^3}{3!}$ + $o(x^3)]^3 = x^6$ + $o(x^6)$

và

Tử số $= x^3$ - $\sin^3$ x(1 + ax + $bx^2) = x^3$ - $[x^3$ + $ax^4$ + (b - $\frac{1}{2})x^5$ + $cx^6$ + $o(x^6)]$

$\Rightarrow$ f(x) $= -\frac{ax^4$ + (b - $\frac{1}{2})x^5$ + $cx^6$ + $o(x^6)}{x^6$ + $o(x^6)}$

Do đó để tồn tại giới hạn hữu hạn của f(x) khi $x\rightarrow$ 0, ta phải có a $=$ 0, b $= \frac{1}{2}$

$\qquad \qquad \blacksquare$

(1) sinh x $= \frac{e^x$ - $e^{-x}}{2}$

(2) cosh x $= \frac{e^x$ + $e^{-x}}{2}$



Bài tập 1.63. Cho f là một hàm số thực, khả vi trên [a, b] và có đạo hàm f''(x) trên (a, b),

chứng minh rằng $\forall$ x $\in$ (a, b) có thể tìm được ít nhất 1 điểm c $\in$ (a, b) sao cho

f(x) - f(a) - $\frac{f(b)$ - $f(a)}{h}$ (x - a) $= \frac{(x$ - a)(x - $b)}{2}$ f''(c)

Chứng minh. Lấy $x_0 \in$ (a, b) bất kì.

$\mathbf{D} \mathbf{\check{a}} \mathbf{t} \ \varphi(x) :=$ f(x) - f(a) - $\frac{f(b)$ - $f(a)}{b-a}(x-a)$ - $\frac{(x-a)(x-b)}{2}.\lambda$

Trong đó $\lambda$ được xác định bởi điều kiên :

$\varphi(x_0) = f(x_0)$ - f(a) - $\frac{f(b)$ - $f(a)}{h} (x_0$ - a) - $\frac{(x_0$ - $a)(x_0$ - $b)}{h} \cdot \lambda =$ 0

Khi đó ta có $\varphi(x_0) = \varphi(a) = \varphi(b) =$ 0

Ta có hàm $\varphi$ liên tục, khả vi trên [a, $x_0]$, đo đó $\varphi$ thoả mãn các điều kiện trong định lý

Rolle, suy ra tồn tại $c_1 \in$ (a, $x_0)$ sao cho $\varphi'(c_1) =$ 0. Tương tự như thế, tồn tại $c_2 \in (x_0$, b)

sao cho $\varphi'(c_2) =$ 0. Mặt khác,

$\varphi'(x) =$ f'(x) - $\frac{f(b)$ - $f(a)}{b$ - $a}$ - $\lambda(x$ - $\frac{a$ + $b}{2})$

Theo giả thiết, f có đạo hàm cấp 2, do đó $\varphi$ cũng có đạo hàm cấp 2, và $\varphi''(c_1) = \varphi''(c_2) =$ 0,

nên theo định lý Rolle ta có tồn tại c $\in (c_1$, $c_2)$ sao cho $\varphi''(c) =$ f''(c) - $\lambda =$ 0 $\Rightarrow \lambda =$ f''(c),

và ta có :

f(x) - f(a) - $\frac{f(b)$ - $f(a)}{b$ - $a}(x$ - a) $= \frac{(x$ - a)(x - $b)}{2}f''(c)$



$\S$ 10. CÁC LƯỢC ĐỒ KHẢO SÁT HÀM SỐ

## 10.1 Khảo sát và vẽ đồ thị của hàm số <math>y = f(x)</math> <math display="inline">\S 10.</math> CÁC LƯỢC ĐỒ KHẢO SÁT HÀM SỐ

Mục này học sinh đã được nghiên cứu tương đối kĩ trong chương trình phổ thông nên

chỉ nhấn mạnh cho sinh viên những điểm cần chú ý trong quá trình khảo sát hàm số và

khảo sát một số hàm số khác với chương trình phổ thông như hàm số có chứa căn thức, ...

Sơ đồ khảo sát

1. Tìm TXĐ của hàm số, nhận xét tính chẵn, lẻ, tuần hoàn của hàm số (nếu có).

2. Xác định chiều biến thiên: tìm các khoảng tăng, giảm của hàm số.

3. Tìm cực trị (nếu có).

4. Xét tính lồi, lõm (nếu cần thiết), điểm uốn (nếu có).

5. Tìm các tiêm cân của hàm số (nếu có).

6. Lập bảng biến thiên.

7. Tìm một số điểm đặc biệt mà hàm số đi qua (ví dụ như giao điểm với các trục toạ độ,

....) và vẽ đồ thi của hàm số.

Ví du 10.1 (Giữa kì, K61). Tìm các cực trị của hàm số sau

a) y $= \frac{2x}{x^2+2}$.

b) y $= \frac{2x}{x^2+1}$.

Ví dụ 10.2 (Giữa kì, K59). Tìm các đường tiệm cận của đường cong y $= x^2 \sin \frac{1}{x}$.

[Lời giải] TXĐ $= \mathbb{R} \setminus \{0\}$.

0 $\le \left| x^2 \sin \frac{1}{x} \right| \le x^2 \Rightarrow \lim_{x \to 0} x^2 \sin \frac{1}{x} =$ 0 $\quad \text{(gi\'oi$ hạn $kep)}$.

Đường cong không có tiệm cận đứng.

$\n\lim_{x \to \infty} x^2 \sin \frac{1}{x} = \lim_{x \to \infty}$ x $\cdot \frac{\sin \frac{1}{x}}{1} = \infty\n$

Đường cong không có tiệm cận ngang.

$\n\lim_{x \to \infty} \frac{y}{x} = \lim_{x \to \infty} \frac{\sin \frac{1}{x}}{\frac{1}{x}} = 1.\n$

$\n\lim_{x \to \infty}$ (y - x) $= \lim_{x \to \infty}$ x $\left($ x $\sin \frac{1}{x}$ - 1 $\right) = \lim_{t \to 0} \frac{1}{t} \left( \frac{\sin t}{t}$ - 1 $\right) = \lim_{t \to 0} \frac{\sin$ t - $t}{t^2} =$ 0 $\quad \left($ d $\geq$ t $= \frac{1}{x} \right).\n$

Đường cong có một tiệm cận xiên là y $=$ x.



Ví dụ 10.3. Tìm các tiệm cận xiên của đường cong y $= \ln(1$ + $e^{-2x})$.

[Lời giải] Ta có

$\n\lim_{x \to +\infty} \frac{y}{x} =$ 0, $\quad$ a $= \lim_{x \to -\infty} \frac{y}{x} = \lim_{x \to -\infty} \frac{\ln(1$ + $e^{-2x})}{x} = \lim_{x \to -\infty} \frac{-2e^{-2x}}{1$ + $e^{-2x}} =$ -2, $\quad \text{(L'Hospital)}.\n$

b $= \lim_{x \to -\infty}$ (y + 2x) $= \lim_{x \to -\infty} \ln(1$ + $e^{-2x})$ + 2x $= \lim_{x \to -\infty} \ln[(1$ + $e^{-2x})e^{2x}] = \lim_{x \to -\infty} \ln(1$ + $e^{2x}) =$ 0.

Kết luận: y $=$ -2x là tiệm cận xiên của đường cong.

Bài tập 1.64. Khảo sát và vẽ đường cong y $= \frac{2-x^2}{1+x^4}$.



![](graphs/graph_85_0.png)

Hình 1.64



![](graphs/graph_85_1.png)

Hình 1.65

Bài tập 1.66. Khảo sát và vẽ đường cong y $= \frac{x-2}{\sqrt{x^2+1}}$.



Y



![](graphs/graph_86_0.png)

Hình 1.66

## 10.2 Khảo sát và vẽ đường cong cho dưới dạng tham sô Hình 1.66

$ Giả sử cần khảo sát và vẽ đường cong cho dưới dạng tham số \begin{cases} x = x(t) \\ y = y(t) \end{cases} $

1. Tìm TXĐ, nhận xét tính chẵn, lẻ, tuần hoàn của các hàm số x(t), y(t) (nếu có).

2. Xác định chiều biến thiên của các hàm số x(t), y(t) theo biến t bằng cách xét dấu các

đạo hàm của nó.

3. Tìm các tiệm cận của đường cong

(a) Tiệm cận đứng: Nếu $\lim_{t\to t_0(\infty)}$ y(t) $= \infty$ và $\lim_{t\to t_0(\infty)}$ x(t) $= x_0$ thì x $= x_0$ là một tiệm

cận đứng của đường cong.

(b) Tiệm cận ngang: Nếu $\lim_{t\to t_0(\infty)}$ x(t) $= \infty$ và $\lim_{t\to t_0(\infty)}$ y(t) $= y_0$ thì y $= y_0$ là một tiệm

cận ngang của đường cong.

(c) Tiệm cận xiên: Nếu $\lim_{t\to t_0(\infty)}$ y(t) $= \infty$ và $\lim_{t\to t_0(\infty)}$ x(t) $= \infty$ thì đường cong có thể có

tiệm cận xiên. Nếu

a $= \lim_{t \to t_0(\infty)} \frac{y(t)}{x(t)}$, $\quad$ b $= \lim_{t \to t_0(\infty)}$ [y(t) - ax(t)]

thì y $=$ ax + b là một tiệm cận xiên của đồ thị hàm số.

4. Để vẽ đường cong được chính xác hơn, ta xác định tiếp tuyến của đường cong tại các

điểm đặc biệt. Hệ số góc của tiếp tuyến của đường cong tai mỗi điểm bằng

$\frac{dy}{dx} = \frac{y'_t}{x'_t}$



Ngoài ra có thể khảo sát tính lồi lõm và điểm uốn (nếu cần thiết) bằng cách tính các

đạo hàm cấp hai

$\frac{d^2y}{dx^2} = \frac{d\left(\frac{y'_t}{x'_t}\right)}{dx} = \frac{y_{tt}"x'_t$ - $y'_t x_{t}"}{\gamma'^3}$

5. Xác định một số điểm đặc biệt mà đồ thị hàm số đi qua và vẽ đồ thị hàm số.

Ví dụ 10.4 (Giữa kì, K61). Tìm các tiệm cận của đường cong cho bởi phương trình tham

$S\acute{\hat{O}}$

$ b) \begin{cases} x = \frac{2016t}{1+t^3} \\ y = \frac{2016t^2}{1+t^3} \end{cases} $

$ a) \begin{cases} x = \frac{2016t}{1-t^3} \\ y = \frac{2016t^2}{1-t^3} \end{cases} $

$ \begin{cases} x = 2t - t^2 \\ y = 3t - t^3. \end{cases} $

Bài tập 1.67. Khảo sát và vẽ đường cong



![](graphs/graph_87_0.png)

$\mathop{\mathcal{X}_{}}\nolimits$

## 10.3 Khảo sát và vẽ đường cong trong hệ toạ độ cực <math display="block">\mathop{\mathcal{X}_{}}\nolimits</math>

Bài tập 1.68. Khảo sát và vẽ đường cong r $=$ a + b $\cos \varphi$, (0 $<$ a $\le$ b).





![](graphs/graph_88_0.png)

$Hình\$ 1.68

Bài tập 1.69. Khảo sát và vẽ đường cong r $=$ a (1 + $\cos \varphi)$ (a $>$ 0), (đường Cardioid hay

đường hình tim, trường hợp đặc biệt của đường cong trong Bài tập 1.68 với a $=$ b)

$\mathbf{A}^{\mathcal{Y}}$

$\mathcal{A}$

$\mathcal{X}$

2a

-u

Hình 1.69

Bài tập 1.70. Khảo sát và vẽ đường cong r $= \frac{a}{\sqrt{\cos 3\varphi}}$, (a $>$ 0).



$\sqrt{\cos 3\varphi}$

O

$\mathop{\mathcal{X}_{}}\nolimits$

Hình 1.70

Bài tập 1.71. Khảo sát và vẽ đường cong Lemniscate

(x2 + y2)2 $=$ 2a2(x2 - y2) (a $>$ 0).

Phương trình của đường Lemniscate trong tọa độ cực là r $= a\sqrt{2 \cos 2\varphi}$.

$\int^{y}$ r $=$ a $\sqrt{2 \cos 2\varphi}$

$\mathop{\mathcal{X}_{}}\nolimits$

Hình 1.71

Bài tập 1.72. Khảo sát và vẽ đường cong $(x^2$ + $y^2)^2 = 2a^2xy$ (a $>$ 0).

$ Tham số hoá đường cong đã cho, đặt \begin{cases} x = r \cos \varphi \\ y = r \sin \varphi \end{cases}, phương trình đường cong tương đương $

với $r^2 = a^2 \sin 2\varphi$.



r $= a\sqrt{\sin 2\varphi}$

O

$\chi$

Hình 1.72

Bài tập 1.73. Khảo sát và vẽ đường cong $x^3$ + $y^3 =$ axy (a $>$ 0)

(Lá Descartes)

$ Tham số hoá đường cong đã cho, đặt \begin{cases} x = r \cos \varphi \\ \vdots \end{cases}, phương trình đường cong tương đương $

y $=$ r $\sin \varphi$

với

r $= \frac{a \sin \varphi \cos \varphi}{\sin^3 \varphi$ + $\cos^3 \varphi}$



![](graphs/graph_90_0.png)

## 10.4 Bài tập <math display="block">r = \frac{a \sin \varphi \cos \varphi}{\sin^3 \varphi + \cos^3 \varphi}</math>

Bài tập 1.74. Khảo sát tính đơn điệu của hàm số



a. y $= x^3$ + x

b. y $= \arctan$ x - x

$[\text{Đáp}\text{ số}]$

a) hàm số tăng với mọi x

b) hàm số giảm với mọi x

Bài tập 1.75. Chứng minh các bất đẳng thức

a. 2x $\arctan$ x $\ge \ln(1$ + $x^2) \forall$ x $\in \mathbb{R}$ b. x - $\frac{x^2}{2} \le \ln(1$ + x) $<$ x $\quad \forall$ x $>$ 0

Chứng minh. a) Xét hàm số f(x) $=$ 2x arctan x - $\ln(1$ + $x^2) \Rightarrow$ f'(x) $=$ 2 arctan x.

• Nếu x $\ge$ 0, f'(x) $\ge$ 0 $\Rightarrow$ f(x) $\ge$ f(0) $=$ 0

• Nếu x $<$ 0, f'(x) $<$ 0 $\Rightarrow$ f(x) $<$ f(0) $=$ 0

$\blacksquare$

b) Tương tự, xét g(x) $=$ x - $\frac{x^2}{2}$ - $\ln(1+x)$, h(x) $= \ln(1+x)$ - x

g'(x) $= -\frac{x^2}{1+x} <$ 0, h'(x) $= -\frac{x}{1+x} <$ 0 $\Rightarrow$ g(x) $\le$ g(0) $=$ 0, h(x) $\le$ h(0) $=$ 0.

Bài tập 1.76. Tìm cực tri của hàm số

a) y $= \frac{3x^2$ + 4x + $4}{x^2$ + x + $1}b)$ y $=$ x - $\ln(1$ + x)c) y $= \sqrt[3]{(1$ - x)(x - $2)^2}$

Chứng minh. a) y' $= \frac{-x(x+2)}{(x^2+x+1)^2}$, $y_{\text{min}} =$ y(-2) $= \frac{8}{3}$, $y_{\text{max}} =$ y(0) $=$ 4.

b) y' $= \frac{x}{1+x}$, $y_{\min} =$ y(0) $=$ 0.

c) y' $= -\frac{1}{3} \frac{\sqrt[3]{(x-2)^2}}{\sqrt[3]{(1-x)^2}}$ + $\frac{2}{3} \frac{\sqrt[3]{1-x}}{\sqrt[3]{x-2}} = \frac{\frac{4}{3}-x}{\sqrt[3]{(1-x)^2(x-2)}}$.

• Xét $x_1 = \frac{4}{3}$, ta có $y_{\text{min}} = y(\frac{4}{3}) = -\frac{\sqrt[3]{4}}{3}$

• Xét $x_2 =$ 1, y' không đổi dấu, hàm số không đạt cực trị tại $x_2 =$ 1

• Xét $x_3 =$ 2, ta có $y_{\text{max}} =$ y(2) $=$ 0

$\blacksquare$

Bài tập 1.77. Chứng minh các bất đẳng thức sau

c) $\tan$ x $>$ x + $\frac{x^3}{3} \forall$ 0 $<$ x $< \frac{\pi}{2}$

a) $e^x >$ 1 + x $\quad \forall$ x $\neq$ 0

b) x - $\frac{x^3}{6} < \sin$ x $<$ x $\quad \forall$ x $>$ 0

Bài tập 1.78. Chứng minh rằng với mọi x $>$ 0 ta có

$\left(1+\frac{1}{x}\right)^x <$ e $< \left(1+\frac{1}{x}\right)^{x+1}$

Bài tập 1.79. Tính các giới hạn sau



(c) $\lim_{x\to 0} x^{-5} \left[ \sin(\sin$ x) - x $\sqrt[3]{1$ - $x^2} \right]$,

(a) $\lim_{x\to\infty} \left[x$ - $x^2 \ln(1+\frac{1}{x})\right]$,

(d) $\lim_{x\to 0} \left[ \ln(1+x)^{\frac{1}{x^2}}$ - $\frac{e^x}{x} \right]$.

(b) $\lim_{x\to 0}\frac{1}{x}\left(\frac{1}{x}-\cot x\right)$,





CHƯƠNG Z

PHÉP TÍNH TÍCH PHÂN MỘT BIÊN SÔ

$\S1$. TÍCH PHÂN BẤT ĐỊNH

## 1.1 Nguyên hàm của hàm số <math>\S</math>1. TÍCH PHÂN BẤT ĐỊNH

# Chương này trình bày về phép tính tích phân, đây là phép toán ngược của phép tính

đạo hàm (vi phân) của hàm số. Nếu ta cho trước một hàm số f(x) thì có tồn tại hay không

một hàm số F(x) có đạo hàm bằng f(x)? Nếu tồn tại, hãy tìm tất cả các hàm số F(x) như

vậy.

Định nghĩa 2.26. Hàm số F(x) được gọi là một nguyên hàm của hàm số f(x) trên khoảng

D $\$, $n\hat{e}u$ F'(x) $=$ f(x), $\forall$ x $\in$ D $\$, hay dF(x) $=$ f(x)dx.

### Định lý sau đây nói rằng nguyên hàm của một hàm số cho trước không phải là duy nhất,

nếu biết một nguyên hàm thì ta có thể miêu tả được tất cả các nguyên hàm khác của hàm

số đó.

Đinh lý 2.38. Nếu F(x) là một nguyên hàm của hàm số f(x) trên khoảng D, thì:

• Hàm số F(x) + C cũng là một nguyên hàm của hàm số f(x), với C là một hằng số bất

$k\hat{y}$.

• Ngược lại, mọi nguyên hàm của hàm số f(x) đều viết được dưới dạng F(x) + C, trong

đó C là một hằng số.

Như vậy biểu thức F(x) + C biểu diễn tất cả các nguyên hàm của hàm số f(x), mỗi hằng

số C tương ứng cho ta một nguyên hàm.



Định nghĩa 2.27. Tích phân bất định của một hàm số f(x) là họ các nguyên hàm F(x) +

C, với x $\in$ D, trong đó C là một nguyên hàm của hàm số f(x) và C là một hằng số bất

kỳ. Tích phân bất định của f(x)dx được ký hiệu là $\int$ f(x)dx. Biểu thức f(x)dx được gọi là

biểu thức dưới dấu tích phân và hàm số f(x) được gọi là hàm số dưới dấu tích phân.

Vậy $\int$ f(x)dx $=$ F(x) + C, với F(x) là nguyên hàm của f(x).

Các tính chất của tích phân bất định

• $\left[ \int$ f(x) dx $\right]' =$ f(x) hay d $\int$ f(x) dx $=$ f(x) dx

• $\int$ F'(x)dx $=$ F(x) + C $\text{$ hay $} \int$ dF(x) $=$ F(x) + C

• $\int$ af(x)dx $=$ a $\int$ f(x)dx (a là hằng số khác 0)

• $\int$ [f(x) $\pm$ g(x)] dx $= \int$ f(x) dx $\pm \int$ g(x) dx

Hai tính chất cuối cùng là tính chất tuyến tính của tích phân bất định, ta có thể viết

chung

$\int [\alpha$ f(x) + $\beta$ g(x)] dx $= \alpha \int$ f(x) dx + $\beta \int$ g(x) dx

trong đó $\alpha$, $\beta$ là các hằng số không đồng thời bằng 0.

Các công thức tích phân dạng đơn giản

1) $\int x^{\alpha}$ dx $= \frac{x^{\alpha+1}}{\alpha+1}$ + C, $(\alpha \neq$ -1)

7) $\int e^x$ dx $= e^x$ + C

2) $\int \frac{dx}{x} = \ln$ |x| + C

8) $\int \frac{dx}{a^2-x^2} = \frac{1}{2a} \ln \left| \frac{a+x}{a-x} \right|$ + C

3) $\int \sin$ x dx $= -\cos$ x + C $\int \cos$ x dx

9) $\int \frac{dx}{x^2$ + $a^2} = \frac{1}{a} \arctan \frac{x}{a}$ + C

$\sin$ x + C

4) $\int \frac{dx}{\sin^2 x} = -\cot$ x + C

10) $\int \frac{dx}{\sqrt{x^2$ + $\alpha}} = \ln$ |x + $\sqrt{x^2$ + $\alpha}|$ + C

5) $\int \frac{dx}{\cos^2 x} = \tan$ x + C

6) $\int a^x$ dx $= \frac{a^x}{\ln a}$ + C, (a $>$ 0, a $\neq$ 1)11) $\int \frac{dx}{\sqrt{a^2$ - $x^2}} = \arcsin \frac{x}{a}$ + C

12) $\int \sqrt{a^2$ - $x^2}$ dx $= \frac{1}{2}x\sqrt{a^2$ - $x^2}$ + $\frac{a^2}{2} \arcsin \frac{x}{a}$ + C

13) $\int \sqrt{x^2$ + $a}$ dx $= \frac{1}{2} \left[$ x $\sqrt{x^2$ + $a}$ + a $\ln \left|$ x + $\sqrt{x^2$ + $a} \right| \right]$ + C



## 1.2 Các phương pháp tính tích phân bất định None

1. Phương pháp khai triển

Để tính một tích phân bất kỳ, ta cần sử dụng các phương pháp thích hợp để đưa về

các tích phân đã có trong bảng các công thức tích phân đơn giản ở trên. Một phương

pháp đơn giản là phương pháp khai triển. Phương pháp này dựa trên tính chất tuyến

tính của tích phân bất định:

$\int [\alpha$ f(x) + $\beta$ g(x)] dx $= \alpha \int$ f(x) dx + $\beta \int$ g(x) dx

Ta phân tích hàm số dưới dấu tích phân thành tổng (hiệu) của các hàm số đơn giản

mà đã biết được nguyên hàm của chúng, các hằng số được đưa ra bên ngoài dấu tích

phân.

Ví dụ 1.1. • $\int (2x\sqrt{x}$ - $3x^2)dx =$ 2 $\int x^{\frac{3}{2}}$ dx - 3 $\int x^2$ dx $= \frac{4}{5}x^{\frac{5}{2}}$ - $x^3$ + C

• $\int \left(2\sin$ x + $x^3$ - $\frac{1}{x}\right)$ dx $=$ 2 $\int \sin$ x dx + $\int x^3$ dx - $\int \frac{dx}{x} = -2\cos$ x + $\frac{x^4}{4}$ - $\ln|x|$ + C

• $\int \frac{dx}{x^2(1+x^2)} = \int \left(\frac{1}{x^2}$ - $\frac{1}{1+x^2}\right)$ dx $= -\frac{1}{x}$ + $\arctan$ x + C

2. Phương pháp biến đổi biểu thức vi phân

Nhận xét: nếu $\int$ f(x)dx $=$ F(x) + C thì $\int$ f(u)du $=$ F(u) + C, trong đó u $=$ u(x) là

một hàm số khả vi liên tục. Ta có thể kiểm tra lại bằng cách đạo hàm hai về theo x.

Sử dụng tính chất này, ta biến đổi biểu thức dưới dấu tích phân g(x)dx về dạng

g(x)dx $=$ f(u(x))u'(x)dx,

trong đó f(x) là một hàm số mà ta dễ dàng tìm được nguyên hàm F(x). Khi đó tích

phân cần tính trở thành

$\int$ g(x)dx $= \int$ f(u(x))u'(x)dx $= \int$ f(u(x))du $=$ F(u(x)) + C

Trong trường hợp đơn giản u(x) $=$ ax + b thì du $=$ adx, do đó nếu $\int$ f(x)dx $=$ F(x) + C

ta suy ra

$\int$ f(ax+b)dx $= \frac{1}{a}F(ax+b)$ + C

Ví dụ 1.2. (a) $\int \sin$ ax dx $= -\frac{1}{a} \cos$ ax + C

(b) $\int e^{ax}$ dx $= \frac{e^{ax}}{a}$ + C



(c) $\int e^{\sin x} \cos$ x dx $= \int e^{\sin x} d(\sin$ x) $= e^{\sin x}$ + C

(d) $\int \frac{dx}{\cos^4 x} = \int$ (1 + $\tan^2$ x) $d(\tan$ x) $= \frac{\tan^3 x}{3}$ + $\tan$ x + C

(e) $\int x\sqrt{1+3x^2}dx = \frac{1}{6}\int \sqrt{1+3x^2}d(1+3x^2) = \frac{1}{9}(\sqrt{1+3x^2})^3$ + C

(f)

I $= \int \frac{\arccos$ x $\arcsin x}{\sqrt{1-x^2}}$ dx $= \int \left(\frac{\pi}{2}$ - $\arcsin x\right) \arcsin$ x $d(\arcsin$ x)

nên

$\Rightarrow$ I $= \frac{\pi}{4} \arcsin^2$ x - $\frac{1}{3} \arcsin^3$ x + C

3. Phương pháp đổi biến

Xét tích phân I $= \int$ f(x)dx, trong đó f(x)là một hàm số liên tục. Để tính tích phân

này, ta tìm cách chuyển sang tính tích phân khác của một hàm số khác bằng một

phép đổi biến x $= \varphi(t)$, sao cho biểu thức dưới dấu tích phân đối với biến t có thể tìm

được nguyên hàm một cách đơn giản hơn.

Phép đổi biến thứ nhất:

Đặt x $= \varphi(t)$, trong đó $\varphi(t)$ là một hàm số đơn điệu, và có đạo hàm liên tục. Khi đó

ta có

I $= \int$ f(x)dx $= \int f[\varphi(t)] \varphi'(t)dt$

Giả sử hàm số g(t) $= f[\varphi(t)] \varphi'(t)$ có nguyên hàm là hàm G(t), và t $=$ h(x) là hàm

số ngược của hàm số x $= \varphi(t)$, ta có

$\int$ g(t)dt $=$ G(t) + C $\Rightarrow$ I $=$ G[h(x)] + C

Phép đổi biến thứ hai:

Đặt t $= \psi(x)$, trong đó $\psi(x)$ là một hàm số có đạo hàm liên tục, và ta viết được hàm

f(x) $= g[\psi(x)] \psi'(x)$. Khi đó ta có

I $= \int$ f(x)dx $= \int g[\psi(x)]\psi'(x)dx$

Giả sử hàm số g(t) có nguyên hàm là hàm số G(t), ta có

I $= G[\psi(x)]$ + C

Chú ý: Khi tính tích phân bất định bằng phương pháp đổi biến số, sau khi tìm được

nguyên hàm theo biến số mới, phải đổi lai thành hàm số của biến số cũ.



Ví dụ 1.3. (a) Tính tích phân $I_1 = \int \sqrt{\frac{x}{2-x}}$ dx

$D\check{a}t$ x $= 2\sin^2$ t, t $\in$ [0, $\frac{\pi}{2}]$, ta $\$ tinh $\$ ducoc

dx $=$ 4 $\sin$ t $\cos$ t dt, $\sqrt{\frac{x}{2-x}} = \sqrt{\frac{2 \sin^2 t}{2(1$ - $\sin^2 t)}} = \tan$ t

Suy ra

$I_1 = \int \sqrt{\frac{x}{2-x}}$ dx $=$ 4 $\int \sin^2$ t dt $=$ 2t - $\sin$ 2t + C

Đổi lại biến x, với t $=$ arcsin $\sqrt{\frac{x}{2}}$, ta thu được

$I_1 = \int \sqrt{\frac{x}{2-x}}$ dx $=$ 2 $\arcsin \sqrt{\frac{x}{2}$ - $\sqrt{2x$ - $x^2}}$ + C

(b) Tính tích phân $I_2 = \int \frac{e^{2x}}{e^x$ + $1}$ dx

$\mathbf{D}\breve{\mathbf{a}}\mathbf{t} e^x =$ t $\Rightarrow e^x$ dx $=$ dt, ta có

$I_2 = \int \frac{t}{t+1}$ dt $= \int \left(1$ - $\frac{1}{t+1}\right)$ dt $=$ t - $\ln|t+1|$ + C

Đổi lại biến x, ta được $I_2 = e^x$ - $\ln(e^x$ + 1) + C.

(c) Tính tích phân $I_3 = \int \frac{dx}{\sqrt{1+4x}}$

$\mathbf{D}\mathbf{a}t$ t $= 2^{-x} \Rightarrow$ dt $= -2^{-x} \ln$ 2dx, tích phân trở thành

$I_3 = \int \frac{-at}{t \ln 2\sqrt{1+t^{-2}}} = -\frac{1}{\ln 2} \int \frac{dt}{\sqrt{t^2+1}} = -\frac{1}{\ln 2} \ln(t$ + $\sqrt{t^2+1})$ + C

Đổi lại biến x, ta có:

$I_3 = -\frac{1}{\ln 2} \ln(2^{-x}$ + $\sqrt{4^{-x}$ + $1})$ + C

Ví dụ 1.4 (Giữa kì, K61). Tính tích phân

a) $\int x^{x+1} \left(1$ + $\frac{1}{x}$ + $\ln x\right)$ dx.

b) $\int x^{x-1} \left(1$ - $\frac{1}{x}$ + $\ln x\right)$ dx.

4. Phương pháp tích phân từng phần

Giả sử u $=$ u(x) và v $=$ v(x) là các hàm số có đạo hàm liên tục. Theo quy tắc lấy vi

phân

d(uv) $=$ udv + vdu $\Rightarrow$ uv $= \int$ d(uv) $= \int$ udv + $\int$ vdu

Suy ra

$\int$ udv $=$ uv - $\int$ vdu



Xét tích phân I $= \int$ f(x) dx. Ta cần biểu diễn

f(x)dx $=$ [g(x)h(x)] dx $=$ g(x) [h(x)dx $=$ udv

và áp dụng công thức tích phân từng phần với các hàm số u $=$ g(x), v $= \int$ h(x) dx. Ta

thường sử dụng phương pháp này khi biểu thức dưới dấu tích phân chứa một trong

các hàm số sau đây: $\ln$ x, $a^x$, hàm số lượng giác, hàm số lượng giác ngược. Cụ thể:

• Trong các tích phân $\int x^n e^{kx}$ dx; $\int x^n \sin$ kx dx; $\int x^n \cos$ kx dx, n nguyên dương, ta

thường chọn u $= x^n$.

• Trong các tích phân $\int x^{\alpha} \ln^{n}$ x dx, $\alpha \neq$ -1 và n nguyên dương, ta thường chọn

$u=\ln^n$ x.

• Trong tích phân $\int x^n$ arctan kxdx; $\int x^n$ arcsin kxdx, n nguyên dương, ta thường

chọn u $= \arctan$ kx hoặc u $= \arcsin$ kx; dv $= x^n$ dx.

Ví dụ 1.5. Tính các tích phân bất định

(a) $I_1 = \int \ln$ x dx $=$ x $\ln$ x - $\int$ dx $=$ x $\ln$ x - x + C

(b) $I_2 = \int x^2 \sin$ x dx

$\mathbf{D}\mathbf{a}t$ u $= x^2$, dv $= \sin$ x dx $\Rightarrow$ v $= -\cos$ x, ta duoc

$I_2 = -x^2 \cos$ x + 2 $\int$ x $\cos$ x dx

$\mathbf{D}\breve{\mathbf{a}}\mathbf{t}$ u $=$ x, dv $= \cos$ x dx $\Rightarrow$ v $= \sin$ x, $\mathbf{t}\mathbf{a} \mathbf{d} \mathbf{u} \mathbf{c}$

$I_2 = -x^2 \cos$ x + 2(x $\sin$ x - $\int \sin$ x dx) $= -x^2 \cos$ x + 2x $\sin$ x + 2 $\cos$ x + C

(c) $I_3 = \int \frac{xe^x dx}{(x+1)^2}$

$\mathbf{D}\mathbf{a}$ t u $= xe^{x};$ dv $= \frac{dx}{(x+1)^{2}} \Rightarrow$ v $= -\frac{1}{x+1};$ du $= (x+1)e^{x}$ dx, ta dugc

$I_3 = -\frac{xe^x}{x+1}$ + $\int e^x$ dx $= -\frac{xe^x}{x+1}$ + $e^x$ + C $= \frac{e^x}{x+1}$ + C

(d) $I_4 = \int \frac{xe^x dx}{\sqrt{1+e^x}}$

$D\check{a}t \sqrt{1+e^x} =$ t $\Rightarrow \frac{e^x dx}{\sqrt{1+e^x}} =$ 2dt, ta có $I_4 =$ 2 $\int$ [ln(t-1) + ln(t+1)] dt $=$ 2(t-1)

1) $\ln(t-1)$ + $2(t+1)\ln(t+1)$ - 4t + C Đổi lại biến x ta có

$\int \frac{xe^{x} dx}{\sqrt{1+e^{x}}} = 2(x-2)\sqrt{1+e^{x}}$ + $4\ln\left(1+\sqrt{1+e^{x}}\right)$ - 2x + C



(e) $I_5 = \int \frac{x \arcsin x}{\sqrt{1-x^2}}$ dx

$\mathbf{D}\mathbf{a}$ t u $= \arcsin$ x; dv $= \frac{xdx}{\sqrt{1-x^2}} \Rightarrow$ du $= \frac{dx}{\sqrt{1-x^2}};$ v $= -\sqrt{1-x^2}$, ta duc

$I_5 = -\sqrt{1-x^2} \arcsin$ x + $\int$ dx $= -\sqrt{1-x^2} \arcsin$ x + x + C

(f) $I_6 = \int e^x \cos$ 2x dx

$\mathbf{D}\mathbf{a}$ t u $= \cos$ 2x; dv $= e^x$ dx $\Rightarrow$ v $= e^x;$ du $=$ -2 $\sin$ 2x dx, ta duoc

$I_6 = e^x \cos$ 2x + 2 $\int e^x \sin$ 2x dx

$\mathbf{D}\mathbf{a}$ t u $= \sin$ 2x; dv $= e^x$ dx $\Rightarrow$ v $= e^x;$ du $=$ 2 $\cos$ 2x dx, ta duoc

$I_6 = e^x \cos$ 2x + 2 $\left( e^x \sin$ 2x - 2 $\int e^x \cos$ 2x dx $\right) = e^x \cos$ 2x + $2e^x \sin$ 2x - $4I_6$ + 5C

$V_{\hat{a}y} I_6 = \frac{e^x}{5} (\cos$ 2x + 2 $\sin$ 2x) + C.

Ví dụ 1.6 (Giữa kì, K61). Tính tích phân

a) $\int x^3 \arctan$ x dx.

c) $\int x^2 \sin$ 2x dx.

d) $\int x^2 \cos$ 2x dx.

b) $\int x^3 \operatorname{arccot}$ x dx.

Ví dụ 1.7 (Ngụy biện toán học). Chứng minh rằng 0 $=$ 1.

Chứng minh. Xét tích phân

I $= \int \frac{dx}{x \ln x} = \int \frac{1}{\ln x}$ d $\ln$ x

$= \frac{1}{\ln x} \cdot \ln$ x - $\int \ln$ x $d\left(\frac{1}{\ln x}\right)$ (tích phân từng phần)

$=$ 1 - $\int \ln$ x $\cdot \frac{-1}{\ln^2 x} \cdot \frac{1}{x}$ dx

$=$ 1 - $\int \frac{dx}{x \ln x}$

$=$ 1 + I.

Phương trình I $=$ 1 + I dẫn đến 0 $=$ 1. Sai lầm ở đâu?

$\qquad \qquad \blacksquare$

Trong các mục sau đây chúng ta sẽ xét tích phân bất định của một số dạng hàm cơ

bản: hàm phân thức hữu tỷ, hàm lượng giác, hàm chứa căn thức; và trình bày một

số phương pháp giải chung đối với tích phân các hàm này.



## 1.3 Tích phân hàm phân thức hữu tỷ None

Định nghĩa 2.28. Một hàm phân thức hữu tỷ là một hàm số có dạng f(x) $= \frac{P(x)}{O(x)}$, trong

đó P(x), Q(x) là các đa thức của x. Một phân thức hữu tỷ có bậc của đa thức ở tử số nhỏ

hơn bậc của đa thức ở mẫu số là một phân thức hữu tỷ thực sự.

Bằng phép chia đa thức, chia P(x) cho Q(x) ta luôn đưa được một hàm phân thức hữu tỷ

về dạng

f(x) $=$ H(x) + $\frac{r(x)}{O(x)}$

trong đó H(x) là đa thức thương, r(x) là phần dư trong phép chia. Khi đó $\frac{r(x)}{O(x)}$ là một phân

thức hữu tỷ thực sự. Nguyên hàm của đa thức được tìm bởi công thức tích phân cơ bản.

Ta sẽ xét việc tìm nguyên hàm của phân thức hữu tỷ còn lại $\frac{r(x)}{O(x)}$ trong hai trường hợp đặc

biệt: mẫu số của phân thức là đa thức bậc nhất hoặc đa thức bậc hai. Trong những trường

hợp mẫu số phức tạp hơn, chúng ta sử dụng phương pháp hệ số bất định để đưa về hai

trường hợp trên.

Phương pháp hệ số bất định

Giả sử chúng ta muốn phân tích một phân thức hữu tỷ thực sự $\frac{P(x)}{O(x)}$ thành tổng (hiệu)

của các phân thức hữu tỷ thực sự có mẫu số là đa thức bậc nhất hoặc bậc hai. Trước hết

ta phân tích đa thức ở mẫu số Q(x) thành tích của các đa thức bậc nhất hoặc bậc hai vô

nghiệm

Q(x) $=$ (x - $\alpha_1)^{a_1}...(x$ - $\alpha_m)^{a_m}(x^2$ + $p_1x$ + $q_1)^{b_1}...(x^2$ + $p_nx$ + $q_n)^{b_n}$

trong đó $\alpha_i$, $p_j$, $q_j$ là các hằng số, $a_i$, $b_j$ là các số nguyên dương, 1 $\le$ i $\le$ m; 1 $\le$ j $\le$ n.

• Nếu trong phân tích của Q(x) xuất hiện đơn thức (x - $\alpha)^a$, a là số nguyên dương thì

trong phân tích của phân thức $\frac{P(x)}{Q(x)}$ xuất hiện các hạng tử dạng $\frac{A_i}{(x-\alpha)^i}$, trong đó $A_i$ là

hằng số và 1 $\le$ i $\le$ a.

• Nếu trong phân tích của Q(x) xuất hiện biểu thức $(x^2$ + px + $q)^b$, b là số nguyên

dương thì trong phân tích của phân thức $\frac{P(x)}{Q(x)}$ xuất hiện các hạng tử dạng $\frac{B_jx+C_j}{(x^2+nx+a)^j}$,

trong đó $B_j$, $C_j$ là các hằng số và 1 $\le$ j $\le$ b.

Sau khi viết được phân tích của $\frac{P(x)}{O(x)}$, ta tìm các hằng số $A_i$, $B_j$, $C_j$ bằng cách quy đồng mẫu

số ở hai vế, rồi đồng nhất hệ số của $x^n$, n $\in \mathbb{R}$ ở hai vế. Như vậy việc dùng phương pháp hệ

số bất định dẫn chúng ta tới việc tính bốn loại tích phân hữu tỷ cơ bản sau:

I. $\int \frac{A dx}{x-a}$

II. $\int \frac{Adx}{(x-a)^k} \$ (k $\ge$ 2)

III. $\int \frac{(Mx$ + $N)dx}{x^2$ + nx + $a}$

IV. $\int \frac{(Mx$ + $N)dx}{(x^2$ + px + $a)^m} \$ (m $\ge$ 2)

trong đó



1. $\int \frac{Adx}{x-a} =$ A $\ln$ |x-a| + C

2. $\int \frac{A dx}{(x-a)^k} = \int A(x-a)^{-k}$ dx $= \frac{-A}{(k-1)(x-a)^{k-1}}$ + C

3.

$\int \frac{(Mx$ + $N)dx}{x^2$ + px + $a} = \int \frac{Mt$ + (N - $Mp/2)}{t^2$ + $a^2}$ dt $\quad$ (a $= \sqrt{q$ - $p^2/4}$, $\text{$ đối biến $}$ t $=$ x + p/2)

$=\int \frac{Mtdt}{t^2$ + $a^2}$ + $\int \frac{(N$ - $Mp/2)dt}{t^2$ + $a^2}$

$=\frac{M}{2}\ln(t^2+a^2)+\frac{1}{2}(N-Mp/2)\arctan\frac{t}{a}+C$

$= \frac{M}{2}\ln(x^2$ + px + q) + $\frac{2N$ - $Mp}{\sqrt{4a$ - $p^2}} \arctan \frac{2x$ + $p}{\sqrt{4a$ - $p^2}}$ + C.

4.

$\int \frac{(Mx+N)dx}{(x^2+px+q)^m} = \int \frac{Mt$ + $(N-Mp/2)}{(t^2+a^2)^m}$ dt $\quad$ (a $= \sqrt{q-p^2/4}$, $\text{ d\text{o}i bi\text{\'en }$ t $= x+p/2})$

$= \int \frac{Mt dt}{(t^2$ + $a^2)^m}$ + $\int \frac{(N$ - $Mp/2)dt}{(t^2$ + $a^2)^m}$

• Tích phân thứ nhất $\int \frac{Mtdt}{(t^2+a^2)^m} = -\frac{M}{2(m-1)(t^2+a^2)^{m-1}}$ + C.

• Muốn xử lý tích phân thứ hai ta thực hiện phép đổi biến số lượng giác t $=$ a $\tan$ z,

$ khi đó \begin{cases} t^2 + a^2 = \frac{a^2}{\cos^2 z}, \\ dt = \frac{a}{\cos^2 z} dz. \end{cases} $

Ta có

$\int \frac{dt}{(t^2 \pm a^2)^m} = a^{2m-1} \int \cos^{2m-2}$ z dz.

Tích phân của hàm lượng giác này sẽ được nghiên cứu kĩ ở phần sau.

Ví du 1.8. Tính các tích phân bất định

a. $I_1 = \int \frac{x^4$ - $x^3$ + $2x^2$ - 2x + $1}{(x^2$ + 2)(x - $1)}$ dx

Ta có

$\frac{x^4$ - $x^3$ + $2x^2$ - 2x + $1}{(x^2$ + 2)(x - $1)} =$ x + $\frac{1}{(x^2$ + 2)(x - $1)} =$ x + $\frac{A}{x$ - $1}$ + $\frac{Bx$ + $C}{x^2$ + $2}$

Quy đồng mẫu số ở hai vế

3 $=$ (A + $B)x^{2}$ + (C - B + 2)x - C



$ Đồng nhất hệ số của x<sup>2</sup>, x và hệ số tự do, ta được \begin{cases} A + B = 0 \\ C - B + 2 = 0 \end{cases} \Rightarrow \begin{cases} A = 1 \\ B = -1 \\ C = -1 \end{cases} $

Suy ra

$\frac{x^4$ - $x^3$ + $2x^2$ - 2x + $3}{(x^2$ + 2)(x - $1)} =$ x + $\frac{1}{x$ - $1}$ - $\frac{1}{2} \frac{2x}{x^2$ + $2}$ - $\frac{1}{x^2$ + $2}$

Vây tích phân bằng

I $= \frac{x^2}{2}$ + $\ln|x$ - 1| - $\frac{\ln(x^2$ + $2)}{2}$ - $\frac{1}{\sqrt{2}} \arctan \frac{x}{\sqrt{2}}$ + C

b. $I_2 = \int \frac{2x^4$ + $10x^3$ + $17x^2$ + 16x + $5}{(x+1)^2(x^2+2x+3)}$ dx

Ta viết

$\frac{2x^4$ + $10x^3$ + $17x^2$ + 16x + $5}{(x+1)^2(x^2$ + 2x + $3)} =$ 2 + $\frac{2}{x+1}$ - $\frac{1}{(x+1)^2}$ - $\frac{4}{x^2$ + 2x + $3}$

Suy ra

I $=$ 2x + $2\ln|x+1|$ + $\frac{1}{x+1}$ - $2\sqrt{2}\arctan\frac{x+1}{\sqrt{2}}$ + C

Ví dụ 1.9 (Giữa kì, K61). Tính các tích phân sau

a) $\int \frac{1}{x^2+2016x}$ dx.

c) $\int \frac{xdx}{(x^2+1)(x^2+2)}$.

d) $\int \frac{xdx}{(x^2+2)(x^2+3)}$.

b) $\int \frac{1}{x^2-2016x}$ dx.

Ví dụ 1.10 (Giữa kì, K61). Tính tích phân

a) $\int$ x $\ln(x^2$ + x + 1) dx.

b) $\int$ x $\ln(x^2$ - x + 1) dx.

## 1.4 Tích phân hàm lượng giác b) <math display="block">\int x \ln(x^2 - x + 1) dx.</math>

1. Phương pháp chung

Xét tích phân $\int R(\sin$ x, $\cos$ x) dx, trong đó hàm dưới dấu tích phân là một biểu thức

hữu tỷ đối với sin x, cos x. Ta có thể sử dụng phép đổi biến tổng quát t $= \tan \frac{t}{2}$, khi đó

$\sin$ x $= \frac{2t}{1+t^2}; \cos$ x $= \frac{1-t^2}{1+t^2}; \tan$ x $= \frac{2t}{1-t^2};$ dx $= \frac{2dt}{1+t^2}$

tích phân đang xét được đưa về tích phân của phân thức hữu tỉ của biến t.



Ví dụ 1.11. Tính tích phân $\int \frac{\sin$ x - $\cos$ x + $2}{1$ + $\sin$ x + $\cos x}$ dx

Ta viết

$\int \frac{\sin$ x - $\cos$ x + $2}{1$ + $\sin$ x + $\cos x}$ dx $= -\int \frac{d(1$ + $\sin$ x + $\cos x)}{1$ + $\sin$ x + $\cos x}$ + $2\int \frac{dx}{1$ + $\sin$ x + $\cos x}$

$\tilde{B}at$ t $= \tan \frac{x}{2}$, suy ra

$\int \frac{dx}{1$ + $\sin$ x + $\cos x} = \int \frac{dt}{1$ + $t} = \ln|1$ + t| + C

Thay lai biến cũ, ta được

$\int \frac{\sin$ x - $\cos$ x + $2}{1$ + $\sin$ x + $\cos x}$ dx $= -\ln|1$ + $\sin$ x + $\cos$ x| + $\ln|1$ + $\tan \frac{x}{2}|$ + C

2. Tích phân dạng $\int \sin^m$ x $\cos^n$ x dx, trong đó m, n là các số nguyên

• Nếu m là số nguyên dương lẻ, ta đặt t $= \cos$ x.

• Nếu n là số nguyên dương lẻ, ta đặt t $= \sin$ x.

• Nếu m, n là các số nguyên dương chẵn, ta sử dụng công thức hạ bậc:

$\sin^2$ x $= \frac{1$ - $\cos 2x}{2}; \cos^2$ x $= \frac{1$ + $\cos 2x}{2}$

rồi đưa về tích phân dạng $\int \sin^k$ 2x $\cos^l$ 2x dx.

Ví dụ 1.12. Tính các tích phân bất định

$I_1 = \int \sin^3$ x $\cos^2$ x dx

$D\breve{a}t\cos$ x $=$ t $\Rightarrow -\sin$ x dx $=$ dt ta có

$\int \sin^3$ x $\cos^2$ x dx $= \int$ (1 - $t^2)t^2(-dt) = \frac{t^5}{5}$ - $\frac{t^3}{3}$ + C $= \frac{\cos^5 x}{5}$ - $\frac{\cos^3 x}{3}$ + C

$I_2 = \int \sin^4$ x $\cos^2$ x dx

Sử dụng công thức hạ bậc ta có

$I_2 = \int \frac{(1$ - $\cos 2x)^2}{4} \frac{1$ + $\cos 2x}{2}$ dx $= \frac{1}{8} \int \left(1$ - $\cos$ 2x - $\cos^2$ 2x + $\cos^3 2x\right)$ dx

$\Rightarrow I_2 = \frac{1}{8} \left($ x - $\frac{\sin 2x}{2}$ - $\int \frac{1$ + $\cos 4x}{2}$ dx + $\frac{1}{2} \int$ (1 - $\sin^2$ 2x) $d(\sin$ 2x) $\right)$

Vây

$\Rightarrow I_2 = \frac{1}{8} \left( \frac{x}{2}$ - $\frac{\sin 2x}{2}$ - $\frac{\sin 4x}{8}$ + $\frac{\sin 2x}{2}$ - $\frac{\sin^3 2x}{6} \right)$ + C



$\hat{D}ói$ với tích phân $I_2$ sau khi sử dụng công thức hạ bậc lần thứ nhất ta cũng có

thể tiếp tục hạ bậc của biểu thức lượng giác dưới dấu tích phân bởi công thức

$\sin^3$ x $= \frac{3 \sin$ x - $\sin 3x}{4}; \cos^3$ x $= \frac{3 \cos$ x + $\cos 3x}{4}$

$\acute{A}p$ dụng vào tích phân $I_2$, ta có:

$I_2 = \frac{1}{8} \int \left($ 1 - $\cos$ 2x - $\frac{1$ + $\cos 4x}{2}$ + $\frac{3 \cos$ 2x + $\cos 6x}{4} \right)$ dx

$=\frac{1}{8}\left(\frac{x}{2}-\frac{\sin 2x}{8}-\frac{\sin 4x}{8}+\frac{\sin 6x}{24}\right)+C$

3. Tích phân $\int R(\sin$ x, $\cos$ x) dx có dạng đặc biệt

• Đặt t $= \cos$ x nếu $R(-\sin$ x, $\cos$ x) $= -R(\sin$ x, $\cos$ x).

• Đặt t $= \sin$ x nếu $R(\sin$ x, $-\cos$ x) $= -R(\sin$ x, $\cos$ x).

• Đặt t $= \tan$ x nếu $R(-\sin$ x, $-\cos$ x) $= R(\sin$ x, $\cos$ x).

Ví dụ 1.13. Tính tích phân $\int \frac{dx}{\sin$ x $\cos^4 x}$

$\mathbf{D}\mathbf{\breve{a}}t$ t $= \cos$ x $\Rightarrow$ dt $= -\sin$ x dx, $\mathbf{t}\mathbf{a} \mathbf{c}\mathbf{\breve{o}}$

$\int \frac{dx}{\sin$ x $\cos^4 x} = \int \frac{-dt}{(1-t^2)t^4} = \int \left| \frac{1}{t^4}$ + $\frac{1}{t^2}$ + $\frac{1}{2(t-1)}$ - $\frac{1}{2(t+1)} \right|$ dt

$= -\frac{1}{3t^3}$ - $\frac{1}{t}$ + $\frac{1}{2} \ln \left| \frac{t-1}{t+1} \right|$ + C

nên

$\int \frac{dx}{\sin$ x $\cos^4 x} = -\frac{1}{3 \cos x^3}$ - $\frac{1}{\cos x}$ + $\frac{1}{2} \ln \frac{1$ - $\cos x}{1$ + $\cos x}$ + C

## 1.5 Tích phân các biểu thức vô tỷ <math display="block">\int \frac{dx}{\sin x \cos^4 x} = -\frac{1}{3 \cos x^3} - \frac{1}{\cos x} + \frac{1}{2} \ln \frac{1 - \cos x}{1 + \cos x} + C</math>

Xét các tích phân có dang

$\bullet \int R(x,\sqrt{x^2+\alpha^2})dx$,

$\bullet \int R(x,\sqrt{x^2-\alpha^2})dx$,

$\bullet \int R(x,\sqrt{\alpha^2-x^2})dx$,

trong đó R(u, v) là các hàm số hữu tỷ.

Có hai phương pháp xử lý tích phân các biểu thức hữu tỉ là Phép thế lương giác và

Phép thế Euler. Ý tưởng của cả hai phương pháp này đều là khử các biểu thức vô tỉ bằng

cách:



1. đưa về tích phân của các hàm lượng giác bằng qua phép thế lượng giác,

2. đưa về tích phân của các hàm phân thức hữu tỉ bằng phép thế Euler.

Phép thế lượng giác

• Đặt x $= \alpha \tan$ t đối với tích phân $\int$ R(x, $\sqrt{x^2$ + $\alpha^2})$ dx.

• Đặt x $= \frac{\alpha}{\cos t}$ hoặc x $= \frac{\alpha}{\sin t}$ đối với tích phân $\int$ R(x, $\sqrt{x^2$ - $\alpha^2})$ dx.

• Đặt x $= \alpha \sin$ t hoặc x $= \alpha \cos$ t đối với tích phân $\int$ R(x, $\sqrt{\alpha^2$ - $x^2})$ dx.

Ví dụ 1.14. Tính $\int \frac{dx}{\sqrt{a^2-x^2}}$.

$ [Lời giải] Đặt x = \alpha \sin t, -\frac{\pi}{2} < t < \frac{\pi}{2} ta có \begin{cases} t = \arcsin \frac{x}{\alpha}, \\ dx = \alpha \cos t dt, \\ \frac{1}{\sqrt{\alpha^2 - x^2}} = \frac{1}{\alpha \cos t}. \end{cases} $

I $= \int$ dt $=$ t + C $= \arcsin \frac{x}{\alpha}$ + C

Ví dụ 1.15. Tính $\int \sqrt{\alpha^2$ - $x^2}$ dx.

$ [Lời giải] Đặt x = \alpha \sin t, -\frac{\pi}{2} \le t \le \frac{\pi}{2} ta có \begin{cases} t = \arcsin \frac{x}{\alpha}, \\ dx = \alpha \cos t dt, \\ \sqrt{\alpha^2 - x^2} = \alpha \cos t. \end{cases} $

I $= \alpha^2 \int \cos^2$ t dt $= \alpha^2 \int \frac{1$ + $\cos 2t}{2}$ dt $= \frac{\alpha^2}{2}$ t + $\frac{\alpha^2}{4} \sin$ 2t $= \frac{1}{2}$ x $\sqrt{\alpha^2$ - $x^2}$ + $\frac{\alpha^2}{2} \arcsin \frac{x}{\alpha}$ + C.

Phép thế Euler

• Đặt t $=$ x + $\sqrt{x^2$ + $a}$ đối với tích phân $\int$ R(x, $\sqrt{x^2$ + $a})$ dx, ở đây a có thể âm hoặc dương,

nghĩa là a $= \pm \alpha^2$ đều áp dụng được. Khi đó,

dt $=$ 1 + $\frac{x}{\sqrt{x^2$ + $a}} = \frac{x$ + $\sqrt{x^2$ + $a}}{\sqrt{x^2$ + $a}}$ dx $\Rightarrow \frac{dt}{t} = \frac{dx}{\sqrt{x^2$ + $a}}$

và tích phân đã cho được đưa về tích phân của phân thức hữu tỉ.



• $Đặt\sqrt{\alpha^2$ - $x^2} =$ xt + $\alpha$ đối với tích phân $\int R(x,\sqrt{\alpha^2$ - $x^2})dx$. Khi đó,

$\alpha^2$ - $x^2 =$ (xt + $\alpha)^2 \Leftrightarrow \alpha^2$ - $x^2 = x^2t^2$ + $2\alpha$ xt + $\alpha^2 \Leftrightarrow$ x $= -\frac{2\alpha t}{1$ + $t^2}$,

và tích phân đã cho được đưa về tích phân của phân thức hữu tỉ.

Ví dụ 1.16. Tính $\int \frac{dx}{\sqrt{x^2+a}}$.

[Lời giải] Đặt t $=$ x + $\sqrt{x^2$ + $a}$, khi đó $\frac{dt}{t} = \frac{dx}{\sqrt{x^2$ + $a}}$ và

I $= \int \frac{dt}{t} = \ln|t|$ + C $= \ln|x$ + $\sqrt{x^2$ + $a}|$ + C.

Ví dụ 1.17. Tính $\int \sqrt{x^2$ + $a}$ dx.

[Lời giải] Sử dụng công thức tích phân từng phần ta có

I $= x\sqrt{x^2$ + $a}$ - $\int \frac{x^2}{\sqrt{x^2$ + $a}}$ dx

$= x\sqrt{x^2$ + $a}$ - $\int \frac{(x^2$ + a) - $a}{\sqrt{x^2$ + $a}}$ dx

(2.1)

$= x\sqrt{x^2$ + $a}$ + a $\int \frac{1}{\sqrt{x^2$ + $a}}$ dx - I.

Do đó,

I $= \frac{1}{2} \left[$ x $\sqrt{x^2$ + $a}$ + a $\ln \left|$ x + $\sqrt{x^2$ + $a} \right| \right]$ + C.

Nói chung việc tính tích phân của các biểu thức vô tỷ thông thường được đưa về việc

tính bốn loại tích phân cơ bản sau

1. $\int \frac{dx}{\sqrt{\alpha^2$ - $x^2}} = \arcsin \frac{x}{\alpha}$ + C.

2. $\int \sqrt{\alpha^2$ - $x^2}$ dx $= \frac{1}{2}x\sqrt{\alpha^2$ - $x^2}$ + $\frac{\alpha^2}{2} \arcsin \frac{x}{\alpha}$ + C.

3. $\int \frac{dx}{\sqrt{x^2+a}} = \ln$ |x + $\sqrt{x^2+a}|$ + C.

4. $\int \sqrt{x^2$ + $a}$ dx $= \frac{1}{2} \left[$ x $\sqrt{x^2$ + $a}$ + a $\ln \left|$ x + $\sqrt{x^2$ + $a} \right| \right]$ + C.

Ví du 1.18. Tính các tích phân sau

a) $\int (1-x^2)^{-\frac{3}{2}}$ dx

$\tilde{B} \tilde{a} \tilde{t}$ x $= \sin$ t, t $\in \left[-\frac{\pi}{2}$, $\frac{\pi}{2}\right] \Rightarrow$ dx $= \cos$ t dt, $\sqrt{1$ - $x^2} = \cos$ t, thi

$\int$ (1 - $x^2)^{-\frac{3}{2}}$ dx $= \int \frac{dt}{\cos^2 t} = \tan$ t + C $= \tan(\arcsin$ x) + C



b) $\int \frac{dx}{x^2 \sqrt{1+x^2}}$

$D\check{a}t$ x $= \tan$ t $\Rightarrow$ dx $= \frac{dt}{\cos^2 t}$, ta có

$\int \frac{dx}{x^2 \sqrt{1$ + $x^2}} = \int \frac{\cos$ t $dt}{\sin^2 t} = -\frac{1}{\sin t}$ + C $= -\frac{1}{\sin(\arctan x)}$ + C.

c) $\int \frac{dx}{\sqrt{x^2+x+1}}$.

Ta $\ c\acute{o}$

I $= \int \frac{d\left(x$ + $\frac{1}{2}\right)}{\sqrt{\left(x$ + $\frac{1}{2}\right)^2$ + $\frac{3}{4}}} = \ln\left|x$ + $\frac{1}{2}$ + $\sqrt{x^2$ + x + $1}\right|$ + C.

Tích phân có dạng $\int \frac{px+q}{\sqrt{ax^2+bx+c}}$ dx

Viết

$\int \frac{px+q}{\sqrt{ax^2+bx+c}}dx = \frac{p}{2a}\int \frac{d(ax^2+bx+c)}{\sqrt{ax^2+bx+c}}$ + $\left(q-\frac{pb}{2a}\right)\int \frac{1}{\sqrt{ax^2+bx+c}}dx$

để đưa về việc tính tích phân của hàm vô tỉ cơ bản.

Ví dụ 1.19. Tính $\int \frac{4x-1}{\sqrt{5-4x-x^2}}$ dx.

Tích phân có dạng $\int \frac{dx}{(px+a)\sqrt{ax^2+bx+c}}$

Đặt u $= \frac{1}{px+q}$ để đưa về việc tính tích phân của hàm vô tỉ cơ bản.

Ví dụ 1.20. Tính $\int \frac{dx}{(1+x)\sqrt{3+6x+x^2}}$.

Tính các tích phân có dạng $\int R\left(x$, $\left(\frac{ax+b}{cx+d}\right)^{m_1/n_1}$, ..., $\left(\frac{ax+b}{cx+d}\right)^{m_p/n_p}\right)$ dx

Đặt $\sqrt[k]{\frac{ax+b}{cx+d}} =$ t, với k là bội chung nhỏ nhất của $n_1$, $n_2$, ..., $n_p$, để đưa tích phân đã

cho về tích phân của phân thức hữu tỉ với biến t.

Ví dụ 1.21. Tính $\int \sqrt{\frac{x+1}{x+2}}$ dx.



[Lời giải] Đặt t $= \sqrt{\frac{x+1}{x+2}}$ ta có x $= -\frac{2t^2-1}{t^2-1}$, dx $= \frac{2t}{(t^2-1)^2}dt$ và

$I=2\int \frac{t^2}{(t^2-1)^2}dt$

$= \frac{1}{2} \int \left| \frac{1}{t-1}$ - $\frac{1}{t+1}$ + $\frac{1}{(t-1)^2}$ + $\frac{1}{(t+1)^2} \right|$ dt

(2.2)

$=\frac{1}{2}\ln\frac{t-1}{t+1}-\frac{1}{2}\left(\frac{1}{t-1}-\frac{1}{t+1}\right)+C$

$= \frac{1}{2} \ln \frac{\sqrt{\frac{x+1}{x+2}}$ - $1}{\sqrt{\frac{x+1}{x+2}}$ + $1}$ + x + 2 + C.

Ví dụ 1.22. Tính $\int \frac{dx}{\sqrt{x}$ + $\sqrt[3]{x}}$.

[Gợi ý] Đặt $\sqrt[6]{x} =$ t, đáp số I $= 2\sqrt{x}$ - $3\sqrt[3]{x}$ + $6\sqrt[6]{x}$ - $6\ln(1$ + $\sqrt[6]{x})$ + C.

Bài tập 2.1. Tính các tích phân sau

a) $\int \frac{\sqrt{x+9}}{x}$ dx,

g) $\ \bigg/ \sqrt{e^x+1}$ dx,

d) $\frac{dx}{\sqrt[5]{x}-1}$,

h) $\int \frac{dx}{\sqrt{x}$ + $\sqrt[3]{x}}$,

e) $\frac{dx}{\sqrt[3]{x}$ - $\sqrt[4]{x}}$,

b) $\int \frac{\sqrt{x}-1}{\sqrt{x}+1}$ dx,

f) $\int \frac{dx}{\sqrt{\sqrt{x}-2}}$,

c) $\int \frac{dx}{x+\sqrt[3]{x}}$,

i) $\int \frac{3x+2}{\sqrt{x-9}}$ dx.

$[\text{Đáp}\text{ s}\hat{\text{o}}]$

a) Đặt u $= \sqrt{x+9}$, I $= 2\sqrt{x+9}$ + 3 $\ln \left| \frac{\sqrt{x+9}-3}{\sqrt{x+9}+3} \right|$ + C.

b) Đặt u $= \sqrt{x}$, I $=$ x - $4\sqrt{x}$ + $4\ln(\sqrt{x}$ + 1) + C.

c) Đặt u $= \sqrt[3]{x}$, I $= \frac{3}{2} \ln(\sqrt[3]{x^2}$ + 1) + C.

d) Đặt $\sqrt[5]{x} =$ u, I $= 5\left(\frac{\sqrt[5]{x^4}}{4}$ + $\frac{\sqrt[5]{x^3}}{3}$ + $\frac{\sqrt[5]{x^2}}{2}$ + $\sqrt[5]{x}$ + $\ln|\sqrt[5]{x}$ - $1|\right)$ + C.

e) Đặt $\sqrt[12]{x} =$ u,

I $= \frac{3}{2}\sqrt[3]{x^2}$ + $\frac{12}{7}\sqrt[12]{x^7}$ + $2\sqrt{x}$ + $\frac{12}{5}\sqrt[12]{x^5}$ + $3\sqrt[3]{x}$ + $4\sqrt[4]{x}$ + $6\sqrt[6]{x}$ + $12\sqrt[12]{x}$ + $12\ln|\sqrt[12]{x} \cdot$ 1| + C.

f) $\text{Đặt}\sqrt{\sqrt{x}-2} =$ u, I $= \frac{4}{3}\sqrt{(\sqrt{x^2})^3$ + $8\sqrt{\sqrt{x^2}}$ + $C}$.

g) $\text{Đặt}\sqrt{e^x+1} =$ u, I $= 2\sqrt{e^x+1}$ - $\ln\left|\frac{1+\sqrt{e^x+1}}{1\sqrt{e^x+1}}\right|$ + C.

h) Đặt $\sqrt[6]{x} =$ t, I $= 2\sqrt{x}$ - $3\sqrt[3]{x}$ + $6\sqrt[6]{x}$ - $6\ln(1$ + $\sqrt[6]{x})$ + C.

i) $\text{Đặt}\sqrt{x-9} =$ u, I $= 2(x-9)^{3/2}$ + $58\sqrt{x-9}$ + C



$\S2$. TÍCH PHÂN XÁC ĐINH

## 2.1 Đinh nghĩa tích phân xác định <math>\S</math><b>2.</b> TÍCH PHÂN XÁC ĐINH

Định nghĩa 2.29. Giả sử hàm số f(x) xác định và bị chặn trên [a,b]. Chia [a,b] thành n

khoảng nhỏ $[x_i$, $x_{i+1}]$ bởi phân hoạch a $= x_0 < x_1 <$ ... $< x_n =$ b. Trong mỗi đoạn $[x_i$, $x_{i+1}]$

ta chọn điểm $\xi_i \in [x_i$, $x_{i+1}]$ và thành lập biểu thức

$S_n = \sum_{i=0}^{n-1} f(\xi_i) \triangle x_i \text{ v\'{o}i } \triangle x_i = x_{i+1}$ - $x_i$

(2.3)

Biểu thức $S_n$ được gọi là tổng tích phân. Gọi $\lambda = \max_{1 \leq$ i $\leq n} \triangle x_i$. Nếu tồn tại giới hạn hữu

hạn I $= \lim_{\lambda \to 0} S_n$ không phụ thuộc vào cách chia đoạn [a, b] và không phụ thuộc vào cách

chọn điểm $\xi_i$ thì I được gọi là tích phân xác định của hàm số f(x) trên [a,b] và kí hiệu là

$\int_a^b$ f(x)dx. Trong trường hợp đó ta nói hàm số f(x) khả tích trên [a, b].

Chú ý 2.19. Trong định nghĩa trên ta đã xét hàm số f(x) trong khoảng đóng [a, b] tức là

đã giả thiết a $<$ b. Bây giờ nếu b $<$ a ta định nghĩa $\int_a^b$ f(x)dx $:=$ - $\int_a^a$ f(x)dx và khi a $=$ b

ta định nghĩa $\int_{a}^{b}$ f(x)dx $=$ 0.

## 2.2 Các tiêu chuẩn khả tích ta định nghĩa <math>\int_{a}^{b} f(x)dx = 0.</math>

Định lý 2.39. Điều kiện cần và đủ để hàm số bị chặn f(x) khả tích trên [a,b] là $\lim_{\lambda \to 0}$ (S -

s) $=$ 0, trong đó:

S $= \sum_{i=1}^{n+1} M_i \triangle x_i$, s $= \sum_{i=1}^{n+1} m_i \triangle x_i$

$M_i = \sup_{x \in [x_i$, $x_{i+1}]}$ f(x), $m_i = \inf_{x \in [x_i$, $x_{i+1}]}$ f(x)

Áp dụng định lý 2.39 chúng ta có thể chứng minh được các định lý sau:

Đinh lý 2.40. Nếu f(x) liên tục trên [a,b] thì f(x) khả tích trên [a,b].

Định lý 2.41. Nếu f(x) bị chặn trên [a, b] và có một số điểm gián đoạn trên [a, b] thì f(x)

khả tích trên [a, b].

Định lý 2.42. Nếu f(x) bị chặn và đơn điệu trên [a, b] thì f(x) khả tích trên [a, b].



## 2.3 Các tính chất của tích phân xác định None

Trong các phần tiếp theo sau đây, nếu không có chú thích gì thì khi viết $\int_{v}^{v}$ f(x) dx ta

hiểu là f(x) được giả thiết là khả tích trên [a, b].

• Tinh chất 1.

$\int_{a}^{b} [\alpha$ f(x) + $\beta$ g(x)] dx $= \alpha \int_{a}^{b}$ f(x) dx + $\beta \int_{a}^{b}$ g(x) dx

• Tinh chất 2.

Cho 3 khoảng đóng [a, b], [a, c], [b, c], nếu f(x) khả tích trên khoảng có độ dài lớn nhất

thì cũng khả tích trên 2 đoạn còn lại, và

$\int_{a}^{b}$ f(x)dx $= \int_{a}^{c}$ f(x)dx + $\int_{a}^{b}$ f(x)dx

• Tính chất 3. Giả thiết a $<$ b. Khi đó:

(i) Nếu f(x) $\ge$ 0, $\forall$ x $\in$ [a, b] thì $\int_a^b$ f(x) dx $\ge$ 0

(ii) Nếu f(x) $\ge$ g(x) $\forall$ x $\in$ [a, b] thì $\int_a^b$ f(x) dx $\ge \int_a^b$ g(x) dx

(iii) Nếu f(x) khả tích trên [a, b] thì |f(x)| khả tích trên [a, b] và:

$\left|\int_{a}^{b} f(x)dx\right| \leq \int_{a}^{b}$ |f(x)|dx

(iv) Nếu m $\le$ f(x) $\le$ M, $\forall$ x $\in$ [a, b] thì

m(b-a) $\le \int_{a}^{b}$ f(x) dx $\le$ M(b-a)

• Tinh $\$, $ch\hat{at}$ 4.(Định lý trung bình thứ nhất)

Giả sử f(x) khả tích trên [a, b] và m $\le$ f(x) $\le$ M, $\forall$ x $\in$ [a, b], khi đó tồn tại $\mu$ sao cho:

$\int_{a}$ f(x)dx $= \mu(b-a)$, m $\le \mu \le$ M.

Đặc biệt, nếu f(x) liên tục trên [a, b] thì tồn tại c $\in$ [a, b] sao cho:

$\int_{a}^{b}$ f(x)dx $=$ f(c)(b - a).



• Tính chất 5.(Định lý trung bình thứ hai)

Giả thiết

(i) f(x) và f(x)g(x) khả tích trên [a, b].

(ii) m $\le$ f(x) $\le$ M, $\forall$ x $\in$ [a, b].

(iii) g(x) không đổi dấu trên [a, b].

Khi đó

$\int_{0}^{b}$ f(x)g(x)dx $= \mu \int_{0}^{b}$ g(x)dx, m $\leq \mu \leq$ M.

Đặc biệt nếu f(x) liên tục trên [a, b] thì tồn tại c $\in$ [a, b] sao cho:

$\int_{a}^{b}$ f(x)g(x)dx $=$ f(c) $\int_{a}^{b}$ g(x)dx.

Ví dụ 2.1 (Cuối kì, K61-Viện ĐTQT). Chứng minh rằng nếu f(x) là một hàm số liên

tục trên [3,4] sao cho f(x) $\ge$ 0 với mọi x $\in$ [3,4] và $\int_{2}^{4}$ f(x)dx $=$ 0 thì f(x) $=$ 0 với mọi

x $\in$ [3, 4].

## 2.4 Tích phân với cận trên thay đổi (hàm tích phân) <math display="inline">x \in [3, 4]</math>.

Giả sử f(x) là một hàm khả tích trên [a, b], khi đó với mỗi x $\in$ [a, b] thì f cũng khả tích

trên [a, x]. Ta xác định hàm số F(x) $= \int_{x}^{x}$ f(t) dt.

Định lý 2.43. (1) Nếu f(t) khả tích trên [a, b] thì F(x) liên tục trên [a, b].

(2) Nếu f liên tục tại $x_0 \in$ [a, b] thì F(x) có đạo hàm tại $x_0$ và $F'(x_0) = f(x_0)$.

Định lý 2.44 (Công thức Newton-Leibniz). Nếu f(x) liên tục trong khoảng đóng [a, b]

và F(x) là một nguyên hàm của f(x) thì

$\int_{a}^{b}$ f(x)dx $=$ F(b) - F(a).



## 2.5 Các phương pháp tính tích phân xác đinh None

1. Sử dụng công thức tích phân từng phần.

Giả sử u(x), v(x) là các hàm số có đạo hàm liên tục trong [a, b]. Khi đó:

$\int_{a}^{b}$ u dv $=$ uv $\Big|_{a}^{b}$ - $\int_{a}^{b}$ v du

2. Sử dụng các phép đổi biến số.

Định lý 2.45 (Đổi biến x $:= \varphi(t))$. Xét I $= \int_{a}^{b}$ f(x)dx với f(x) liên tục trong [a, b]. Thực hiện phép đổi biến x $= \varphi(t)$ thoả

mãn 3 điều kiên sau:

(1) $\varphi(t)$ có đạo hàm liên tục trong [a, b].

(2) $\varphi(a) = \alpha; \varphi(b) = \beta$.

(3) Khi t biến thiên trong $[\alpha$, $\beta]$ từ $\alpha$ đến $\beta$ thì x $= \varphi(t)$ biến thiên liên tục từ $\alpha$ đến

b.

Khi đó ta có công thức:

$\int_{0}^{b}$ f(x)dx $= \int_{0}^{b} f[\varphi(t)]\varphi'(t)dt$.

Định lý 2.46 (Đổi biến t $:= \varphi(x)).Giả$ sử tích phân cần tính có dạng I $= \int_{b}^{b} f[\varphi(x)].\varphi'(x)dx$. Trong đó $\varphi(x)$ biến thiên

đơn điệu ngặt và có đạo hàm liên tục trên [a, b]. Khi đó:

$\varphi(b)$

$\int_{a}^{b} f[\varphi(x)].\varphi'(x)dx = \int_{\varphi(a)}$ f(t)dt.

3. Sử dụng các phép truy hồi, quy nạp.



## 2.6 Hệ thống bài tập None

Dạng 1. Tính đạo hàm của hàm tích phân.

Chúng ta có các công thức sau:

$\left| \left( \int$ f(t) dt $\right)_{x} =$ f(x) $\right|$

(2.4)

$\left| \left( \int_{x}^{g(x)}$ f(t) dt $\right) \right|_{x} =$ f(g(x)).g'(x)

(2.5)

Công thức 2.4 chúng ta đã biết trong Định lý 2.43, còn công thức 2.5 được suy ra từ công

thức đao hàm của hàm hợp.

Bài tập 2.1. Tính các đao hàm:

b) $\frac{d}{dy} \int_{x}^{y} e^{t^2}$ dt

a) $\frac{d}{dx}\int_{a}^{y}e^{t^{2}}dt$

c) $\frac{d}{dx} \int_{x^2}^{x^3} \frac{dt}{\sqrt{1+x^4}}$

Chứng minh. a) $\frac{d}{dx} \int_{0}^{y} e^{t^2}$ dt $= -\frac{d}{dx} \int_{0}^{x} e^{t^2}$ dt $= -e^{x^2} (\text{$ do $}$ y $\text{$ là hằng $số})$

b) $\frac{d}{dy} \int^{y} e^{t^2}$ dt $= e^{y^2} (\text{$ do $}$ x $\text{$ là hằng $số})$

c) $\frac{d}{dx} \int_{1}^{x^3} \frac{dt}{\sqrt{1+x^4}} = -\frac{d}{dx} \int_{1}^{x^2} \frac{dt}{\sqrt{1+x^4}}$ + $\frac{d}{dx} \int_{1}^{x^3} \frac{dt}{\sqrt{1+x^4}} = \frac{-2x}{\sqrt{1+x^8}}$ + $\frac{3x^2}{\sqrt{1+12x^2}}$

$\qquad \qquad \blacksquare$

Dạng 2. Tính giới hạn của hàm số dựa vào công thức L'Hospital và đạo hàm của

hàm tích phân.

Bài tập 2.2. Tìm giới han:

a) A $= \lim_{x \to 0^+} \frac{\int_{\tan x}^{\sin x} \sqrt{\tan t} dt}{\int_{0}^{\tan x} \sqrt{\sin t} dt}$

b) B $= \lim_{x \to +\infty} \frac{\int (\arctan t)^2 dt}{\sqrt{x^2$ + $1}}$



Chứng minh. a) Nhận xét: $\lim_{x\to 0^+} \int_{0}^{\sin x} \sqrt{\tan t}$ dt $= \lim_{x\to 0^+} \int_{0}^{\tan t} \sqrt{\sin t}$ dt $=$ 0 nên áp dụng quy

tắc L'Hospital ta có:

$\lim_{x \to 0^+} \frac{\left(\int_0^{\sin x} \sqrt{\tan t} dt\right)}{\left(\int_0^{\tan x} \sqrt{\sin t} dt\right)} = \lim_{x \to 0^+} \frac{\sqrt{\tan(\sin x)} \cdot \cos x}{\sqrt{\sin(\tan x)} \cdot \frac{1}{\cos^2 x}} =$ 1 $\Rightarrow$ A $=$ 1

b) Nhận xét: $\lim_{x \to +\infty} \int_{0}^{\infty} (\arctan t)^2$ dt $= \lim_{x \to +\infty} \sqrt{x^2$ + $1} = \infty$ nên áp dụng quy tắc L'Hospital

ta có:

$\lim_{x \to +\infty} \frac{\left(\int_0^x (\arctan t)^2 dt\right)'}{\left(\sqrt{x^2$ + $1}\right)'} = \lim_{x \to +\infty} \frac{(\arctan x)^2}{\frac{x}{\sqrt{x^2$ + $1}}} = \frac{\pi^2}{4} \Rightarrow$ B $= \frac{\pi^2}{4}$

Dạng 3. Sử dụng công thức tổng tích phân để tính giới han của một số dãy số

đặc biệt.

Xuất phát từ công thức tính tổng tích phân 2.3

$S_n = \sum_{i=0}^{n-1} f(\xi_i) \triangle x_i \text{ v\'oi } \triangle x_i = x_{i+1}$ - $x_i$

Nếu chúng ta chia đoạn [a, b] thành n khoảng có độ dài bằng nhau bởi phân hoạch a $=$

$x_0 < x_1 < \ldots < x_n =$ b, trong đó $x_i =$ a + (b - $a)^{\frac{i}{n}}$ thì:

$S_n = \frac{b-a}{n} \sum_{i=0}^{n-1} f(\xi_i) \text{$ với $} \xi_i \in [x_i$, $x_{i+1}]$

Khi đó nếu hàm f(x) khả tích trên [a, b], và chọn $\xi_i = x_i$ ta được công thức:

$\left|\lim_{n\to\infty}\frac{b-a}{n}\right|\sum_{i=0}^{n-1}f\left(a+\frac{b-a}{n}.i\right)\right|=\int_{0}^{b}f(x)dx$

(2.6)

Còn nếu chọn $\xi_i = x_{i+1}$ ta được công thức:

$\left|\lim_{n\to\infty}\frac{b-a}{n}\left[\sum_{i=1}^n f\left(a+\frac{b-a}{n}.\overline{i}\right)\right]\right|=\int_0^b$ f(x)dx

(2.7)



Bài tập 2.3. Dùng định nghĩa và cách tính tích phân xác định, tìm các giới hạn:

a) A $= \lim_{n \to \infty} \left| \frac{1}{n\alpha}$ + $\frac{1}{n\alpha$ + $\beta}$ + $\frac{1}{n\alpha$ + $2\beta}$ + $\cdots$ + $\frac{1}{n\alpha$ + $(n-1)\beta} \right|$

b) B $= \lim_{n \to \infty} \frac{1}{n} \left( \sqrt{1$ + $\frac{1}{n}}$ + $\sqrt{1$ + $\frac{2}{n}}$ + $\cdots$ + $\sqrt{1$ + $\frac{n}{n}} \right)$

a) Viết

Chứng minh.

A $= \lim_{n \to \infty} \frac{1}{n} \left| \frac{1}{\alpha}$ + $\frac{1}{\alpha$ + $\frac{\beta}{\alpha$ + $\frac{2\beta}{\alpha$ + $\frac{2\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{\alpha$ + $\frac{(n-1)\beta}{$

Áp dụng công thức 2.6 với a $=$ 0, b $=$ 1, f(x) $= \frac{1}{\alpha$ + $\beta x}$ ta được:

A $= \int_{\alpha}^{1} \frac{1}{\alpha$ + $\beta x}$ dx $= \frac{1}{\beta} \ln \frac{\alpha$ + $\beta}{\alpha}$

Nếu áp dụng công thức 2.7 với a $=$ 0, b $=$ 1, f(x) $= \frac{1}{\alpha$ + $\beta x}$ ta được:

A' $= \lim_{n \to \infty} \left[ \frac{1}{n\alpha$ + $\beta}$ + $\frac{1}{n\alpha$ + $2\beta}$ + $\cdots$ + $\frac{1}{n\alpha$ + $n\beta} \right] =$ A $= \frac{1}{\beta} \ln \frac{\alpha$ + $\beta}{\alpha}$

b) Áp dụng công thức 2.7 với a $=$ 0, b $=$ 1, f(x) $= \sqrt{1$ + $x}$ ta được:

B $= \int_{1}^{1} \sqrt{1$ + $x}$ dx $= \frac{2}{3} (2\sqrt{2}$ - 1)

Nếu áp dụng công thức 2.6 với a $=$ 0, b $=$ 1, f(x) $= \sqrt{1$ + $x}$ ta được:

B' $= \lim_{n \to \infty} \frac{1}{n} \left($ 1 + $\sqrt{1$ + $\frac{1}{n}}$ + $\cdots$ + $\sqrt{1$ + $\frac{n-1}{n}} \right) =$ B $= \frac{2}{3} (2\sqrt{2}$ - 1)

Bài tập 2.4. Tính $\lim_{n\to\infty} \left(\frac{1}{n} \sqrt[n]{\frac{(2n)!}{n!}}\right)$

[Gợi ý] Tính $\lim_{n\to\infty} \ln\left(\frac{1}{n}\sqrt[n]{\frac{(2n)!}{n!}}\right)$ bằng cách viết biểu thức trong giới hạn dưới dạng tổng

tích phân.

Dang 4. Tính tích phân xác định (xem mục 2.5)

Bài tập 2.5. Tính các tích phân



a) $\int_{1}^{e} |\ln$ x| (x+1) dx

d) $\int_0^2 \frac{\sin^2$ x $\cos x}{(1$ + $\tan^2 x)^2}$ dx

e) $\int_0^3 \arcsin \sqrt{\frac{x}{1+x}}$ dx

b) $\int_{1}^{e}$ (x $\ln x)^{2}$ dx

f) $\int_0^{\frac{\pi}{2}} \cos^n$ x $\cos$ nx dx

c) $\int_0^1 (x^3$ - 2x + $5)e^{-\frac{x}{2}}$ dx

[Gợi $\acute{y}]$

a) $I_a = \frac{e^2$ + $5}{4}$

b) $I_b = \frac{5e^3-2}{27}$

c) $I_c =$ 98 - $\frac{144}{\sqrt{e}}$

d)

$I_d = \int\limits_0^2 \frac{\sin^2$ x $\cos x}{(1$ + $\tan^2 x)^2}$ dx

$= \int_{0}^{2} \sin^2$ x $\cdot \cos$ x $\cdot \cos^4$ x dx

$= \int_{0}^{2} \sin^{2}$ x $\cdot$ (1 - $\sin^{2}$ x) $d(\sin x)= \frac{\sin^{3}(2)}{3}$ - $\frac{2 \sin^{5}(2)}{5}$ + $\frac{\sin^{7}(2)}{7}$



e)

$I_e = \int_{0}^{3} \arcsin \sqrt{\frac{x}{1+x}}$ dx

$=$ x $\arcsin \sqrt{\frac{x}{1+x}} \bigg|_0^3$ - $\int_0^3$ x $\cdot \frac{1}{\sqrt{1-\frac{x}{1+x}}} \cdot \frac{1}{2\sqrt{\frac{x}{x+1}}} \cdot \frac{1}{(x+1)^2}$ dx

$= \pi$ - $\frac{1}{2} \int_{0}^{3} \frac{\sqrt{x}}{x+1}$ dx

$= \pi$ - $\frac{1}{2} \int_{0}^{\sqrt{3}} \frac{t}{t^2$ + $1}$ .2t dt $\$, $(d\ddot{a}t \sqrt{x} =$ t)

$= \pi$ - $\int_{0}^{\sqrt{3}} \left(1$ - $\frac{1}{t^2$ + $1}\right)$ dt

$= \pi$ - $\left[$ (t - $\arctan$ t) $\Big|_0^{\sqrt{3}} \right]= \frac{4\pi}{3}$ - $\sqrt{3}$

$\mathbf{f})$

$I_n = \int_{0}^{\frac{\pi}{2}} \cos^n$ x $\cos$ nx dx

$= \frac{1}{n} \int_{1}^{\frac{\pi}{2}} \cos^n$ x d $\sin$ nx

$= \frac{1}{n} \cos^{n}$ x $\sin$ nx $\Big|_{0}^{\frac{\pi}{2}}$ + $\frac{1}{n} \int_{0}^{\frac{\pi}{2}} \sin$ nx $\cdot$ n $\cdot \cos^{n-1}$ x $\cdot \sin$ x dx

$=\int_{0}^{\frac{\pi}{2}}\sin nx.\cos^{n-1}x.\sin$ xdx.



Suy ra

$2I_n = \int_{0}^{\frac{\pi}{2}} \cos^n$ x $\cos$ nx dx + $\int_{0}^{\frac{\pi}{2}} \sin$ nx $\cdot \cos^{n-1}$ x $\cdot \sin$ x dx

$=\int_{0}^{\frac{\pi}{2}}\cos^{n-1}x\cos(n-1)xdx$

$= I_{n-1}$

Vậy theo phép truy hồi ta có $I_n = \left(\frac{1}{2}\right)^n I_0 = \frac{\pi}{2^{n+1}}$.

Bài tập 2.6. Tính

a) $I_n = \int_{1}^{\frac{\pi}{2}} \sin^n$ x dx

b) $J_n = \int_{\frac{1}{2}}^{\frac{1}{2}} \cos^n$ x dx

Dạng 5. Chứng minh các đẳng thức tích phân

Bài tập 2.7. Chứng minh rằng nếu f(x) liên tục trên [0,1] thì:

a) $\int_0^{\frac{\pi}{2}} f(\sin$ x) dx $= \int_0^{\frac{\pi}{2}} f(\sin$ x) dx b) $\int_0^{\pi}$ x $f(\sin$ x) dx $= \frac{\pi}{2} \int_0^{\pi} f(\cos$ x) dx.

[Gợi ý] Đây là bài tập dễ, câu a) đặt t $= \frac{\pi}{2}$ - x, còn câu b) đặt t $= \pi$ - x.

Bài tập 2.8. Áp dụng kết quả của bài tập 2.7 hãy chứng minh

$\int_{1}^{2} \frac{\sqrt{\sin x}}{\sqrt{\sin x}$ + $\sqrt{\cos x}}$ dx $= \int_{1}^{2} \frac{\sqrt{\cos x}}{\sqrt{\sin x}$ + $\sqrt{\cos x}}$ dx $= \frac{\pi}{4}$

Bài tập 2.9. Giả sử f(x) liên tục trên [-a, a](a $>$ 0), hãy chứng minh

$ I = \int_{-a}^{a} f(x)dx = \begin{cases} 0 & \text{n\'{e}u } f(x) \text{ là hàm số lẻ trên } [-a, a] \\ 2 \int_{0}^{a} f(x)dx & \text{n\'{e}u } f(x) \text{ là hàm số chẵn trên } [-a, a] \end{cases} $

Bài tập 2.10. Cho f(x) liên tục, chẵn trên [-a, a], chứng minh

$\int_{-a}^{a} \frac{f(x)dx}{1+b^x} = \int_{0}^{a}$ f(x)dx $\text{ } \text{v\'oi }$ 0 $\leq$ b $\neq$ 1

Áp dụng tính

$I_1 = \int_{-1}^{1} \frac{1}{(x^2+1)(e^x+1)}$ dx, $\quad I_2 = \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \frac{2^x \cos 2x}{2002^x+2^x}$ dx, $\quad I_3 = \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \frac{x^2 |\sin x|}{1+2^x}$ dx



Bài tập 2.11. Chứng minh $\int_{a}^{b} x^{m}(a+b-x)^{n}$ dx $= \int_{a}^{b} x^{n}(a+b-x)^{m}$ dx

Áp dụng tính $I_n = \int_1^1 x^2 (1-x)^n$ dx và chứng minh

$\sum_{k=0}^{n}(-1)^{k}C_{n}^{k}\cdot\frac{1}{k+3}=\frac{1}{n+1}-\frac{2}{n+2}+\frac{1}{n+3}$

Dang 6. Chứng minh các bất đẳng thức tích phân

Bài tập 2.12. Cho f(x), g(x) là hai hàm số khả tích trên [a, b]. Khi đó $f^2(x)$, $g^2(x)$ cũng

khả tích trên [a, b]. Chứng minh bất đẳng thức sau (a $<$ b)

$\left(\int_{a}^{b} f(x)g(x)dx\right)^{2} \leq \left(\int_{a}^{b} f^{2}(x)dx\right)\left(\int_{a}^{b} g^{2}(x)dx\right)$

(Bất đẳng thức Cauchy-Schwarzt)

Chúng minh. Xét 2 trường hợp:

TH1. Nếu $\int_{b}^{b} f^{2}(x)$ dx $= \int_{b}^{b} g^{2}(x)$ dx $=$ 0 thì:

0 $\leq \Big| \int_{b}^{b}$ f(x)g(x) dx $\Big| \leq \int_{a}^{b}$ |f(x)g(x)| dx $\leq \int_{a}^{b} \frac{f^{2}(x)$ + $g^{2}(x)}{2}$ dx $=$ 0

Khi đó ta có dấu " $=$ " xảy ra.

TH2. Nếu ít nhất một trong hai tích phân $\int_{0}^{b} f^{2}(x)dx$, $\int g^{2}(x)dx$ khác 0, không mất tính

tổng quát ta giả sử $\int_{0}^{v} f^{2}(x)$ dx $\neq$ 0

Khi đó $[\alpha$ f(x) + $g(x)]^2 \ge$ 0 $\Rightarrow \int_a^b [\alpha$ f(x) + $g(x)]^2 \ge$ 0. Suy ra

$\left(\int_{0}^{b} f^{2}(x)dx\right).\alpha^{2}$ + $\left(2\int_{0}^{b} f(x)g(x)dx\right).\alpha$ + $\int_{0}^{b} g^{2}(x)dx \geq$ 0 $\forall \alpha \in \mathbb{R}$

(2.8)



Biểu thức ở về trái là tam thức bậc 2 đối với $\alpha$ nên 2.8 đúng với mọi $\alpha \in \mathbb{R}$ khi và chỉ

khi

$\triangle' = \left( \int_{a}^{b}$ f(x)g(x)dx $\right)^2$ - $\left( \int_{a}^{b} f^2(x)dx \right) \cdot \left( \int_{a}^{b} g^2(x)dx \right) \leq$ 0.

$\blacksquare$

Bài tập 2.13 (Cuối kì, K62). Cho hàm số f(x) khả vi liên tục đến cấp hai trên [a,b] và

f(a) $=$ f(b) $=$ 0. Chứng minh rằng

$\left(\int_{a}^{b} [f'(x)]^2 dx\right)^2 \leq \int_{a}^{b} [f(x)]^2$ dx $\int_{a}^{b} [f''(x)]^2$ dx.

Chúng minh. Ta có

$\int_{a}^{b} [f'(x)]^{2}$ dx $= \int_{a}^{b}$ f'(x) df(x) $=$ f(x) f'(x) $\Big|_{a}^{b}$ - $\int_{a}^{b}$ f(x) f''(x) dx $=$ - $\int_{a}^{b}$ f(x) f''(x) dx.

Áp dụng bất đẳng thức Cauchy - Schwartz ta có

$\left(\int_a^b [f'(x)]^2 dx\right)^2 = \left(-\int_a^b f(x)f''(x)dx\right)^2 \leq \int_a^b [f(x)]^2$ dx $\int_a^b [f''(x)]^2$ dx.

$\blacksquare$

Bài tập 2.14 (Cuối kì, K60). Cho hàm số f(x) khả vi liên tục trên [0,1] và f(0) $=$ 0.

Chứng minh rằng $\int [f(x)]^2$ dx $\leq \frac{1}{2} \int [f'(x)]^2$ dx.

Chúng minh. Ta có

$f(x)^{2} =$ [f(x) - $f(0)]^{2} = \left(\int_{0}^{x} f'(t)dt\right)^{2} \leq \int_{0}^{x} [f'(t)]^{2}$ dt $\cdot \int_{0}^{x} 1^{2}$ dt

$=$ x $\int_{0}^{x} [f'(t)]^{2}$ dt $\leq$ x $\int_{0}^{1} [f'(t)]^{2}$ dt $=$ x $\int_{0}^{1} [f'(x)]^{2}$ dx.

Do đó,

$\int_{0}^{1} [f(x)]^{2}$ dx $\leq \int_{0}^{1} [f'(x)]^{2}$ dx $\cdot \int_{0}^{1}$ x dx $= \frac{1}{2} \int_{0}^{1} [f'(x)]^{2}$ dx.

Bài tập 2.14 có thể được mở rộng như sau (với chứng minh hoàn toàn tương tự).



Bài tập 2.15. Cho f là một hàm số khả vi liên tục trên [a, b]. Chứng minh rằng

$\int_a^b [f(x)-f(a)]^2$ dx $\leq \frac{b-a}{2} \int_a^b [f'(x)]^2$ dx.

Cũng với ý tưởng viết f(x) - f(a) $= \int_{a}^{b}$ f'(t) dt, bạn đọc có thể chứng minh các kết quả sau.

Bài tập 2.16. Cho f là một hàm số khả vi liên tục trên [a,b] và f(a) $=$ 0. Chứng minh

rằng

$\frac{1}{b-a}\int_{0}^{b}|f(x)|dx\leq \int_{0}^{b}|f'(x)|dx$.

[Lời giải] Thật vậy,

$|f(x)|=|f(x)-f(a)|=\left|\int\limits_a^xf'(t)dt\right|\leq \int\limits_a^x|f'(t)|dt\leq \int\limits_a^b|f(t)|dt$.

Do đó,

$\int_{a}^{b}$ |f(x)| dx $\leq \int_{a}^{b} \left( \int_{a}^{b}$ |f(t)| dt $\right)$ dx $=$ (b-a) $\int_{a}^{b}$ |f(t)| dt $=$ (b-a) $\int_{a}^{b}$ |f(x)| dx.

Bài tập 2.17. Cho f là một hàm số khả vi liên tục trên [a,b] và f(a) $=$ 0. Chứng minh

rằng

$\int_{b}^{b}$ |f(x)f'(x)| dx $\leq \frac{b-a}{2} \int_{b}^{b} [f'(x)]^2$ dx.

[Lời giải] Ta có f(x) $=$ f(x) - f(a) $= \int$ f(t)dt nên

|f(x)f'(x)| $\leq$ |f'(x)| $\int$ |f'(t)dt|.

Suy ra

$\int_{a}^{b}$ |f(x)f'(x)| dx $\leq \int_{a}^{b} \left($ |f'(x)| $\int_{a}^{x}$ |f'(t)| dt $\right)$ dx

(2.9)



$\text{Vi}\left(\int\limits_a^x |f'(t)|dt\right)' =$ |f'(x)| $\text{$ nên $}\left|\left(\int\limits_a^x |f'(t)|dt\right)^2\right| =$ 2|f'(x)| $\int\limits_a^x$ |f'(t)|dt|. $\text{$ Do $đó,}$

$\int_{a}^{b} \left($ |f'(x)| $\int_{a}^{x}$ |f'(t)dt| $\right)$ dx $= \frac{1}{2} \left( \int_{a}^{x}$ |f'(t)| dt $\right)^{2} \Big|_{x=a}^{x=b}$

(2.10)

$=\frac{1}{2}\left(\int\limits_{a}^{b}|f'(x)|dx\right)^{2}\leq\frac{b-a}{2}\int\limits_{a}^{b}|f'(x)|^{2}dx$.

Từ (2.9) và (2.10) ta có điều phải chứng minh.

Bài tập 2.18. Cho f là một hàm số khả vi liên tục trên [a, b], f(a) $=$ 0 và 0 $\le$ f'(x) $\le$ 1 với

mọi x $\in$ [a, b]. Chứng minh rằng

a) $\int_{v}^{b}$ f(x) dx $\geq \frac{1}{2} [f(b)^2$ - $f(a)^2]$,

b) $\int_{a}^{b} [f(x)]^3$ dx $\leq \left( \int_{a}^{b}$ f(x) dx $\right)^2$.

a) Từ giả thiết ta có f(x) là một hàm số đơn điệu không giảm và f(x) $\ge$

Chứng minh.

f(a) $=$ 0, $\forall$ x $\in$ [a, b]. Do đó,

f(x) $>$ f(x)f'(x), $\forall$ x $\in$ [a, b].

Suy ra

$\int_{0}^{b}$ f(x)dx $\ge \int_{0}^{b}$ f(x)f'(x)dx $= \frac{1}{2}[f(x)]^{2}\Big|_{a}^{b} = \frac{1}{2}[f(b)^{2}$ - $f(a)^{2}]$.

b) Xét hàm số

F(x) $= \left(\int_{a}^{x} f(t)dt\right)^{2}$ - $\int_{a}^{x} [f(t)]^{3}$ dt, $\quad$ x $\in$ [a, b].

Ta có

F'(x) $=$ 2f(x) $\int_{-x}^{x}$ f(t)dt - $f(x)^3 =$ f(x) $\left[$ 2 $\int_{-x}^{x}$ f(t)dt - $[f(x)]^2 \right]$.

Đặt G(x) $=$ 2 $\int_{a}^{x}$ f(t)dt - $[f(x)]^2$, ta có

G'(x) $=$ 2f(x) - 2f(x)f'(x) $=$ 2f(x)(1 - f'(x)) $\ge$ 0, $\forall$ x $\in$ [a, b]

$\Rightarrow$ G(x) $\geq$ G(a) $=$ 0, $\forall$ x $\in$ [a, b].

Từ đó suy ra F'(x) $\ge$ 0, $\forall$ x $\in$ [a, b] $\Rightarrow$ F(b) $\ge$ F(a) $=$ 0 $\Rightarrow \int_a^b [f(x)]^3$ dx $\le \left(\int_a^b$ f(x) $dx\right)^{-1}$.

$\blacksquare$



Bài tập 2.19 (Olympic Toán học Sinh viên Toàn quốc 2018 -Bảng A). Cho f : [a, b] $\rightarrow$

$\mathbb{R}$ là một hàm số khả vi liên tục sao cho $\int$ f(x)dx $=$ 0. Chứng minh rằng

$\max_{x\in[a,b]}\left|\int\limits_{a}^{x}f(t)dt\right|\leq\frac{(b-a)^{2}}{8}\max_{x\in[a,b]}|f'(x)|$.

[Lời giải] Do f'(x) liên tục nên tồn tại M $= \max_{x \in [a,b]}$ f'(x).

$\bullet$ Đặt

F(x) $= \int$ f(t)dt + M $\frac{(x-a)(x-b)}{2}$, $\quad$ x $\in$ [a,b].

(2.11)

Ta có F(a) $=$ F(b) $=$ 0 và F''(x) $=$ f'(x) + M $\ge$ 0, $\forall$ x $\in$ [a, b].

• Vì F''(x) $\ge$ 0 nên F(x) là hàm lồi trên [a, b], hơn nữa F(a) $=$ F(b) $=$ 0 nên F(x) $\le$

0, $\forall$ x $\in$ [a, b]. Từ (2.11) ta có

$\int_{a}^{x}$ f(t)dt $\leq$ M $\frac{(x-a)(b-x)}{2} \leq \frac{M}{2} \left( \frac{(x-a)+(b-x)}{2} \right)^2 = \frac{(b-a)^2}{8}$ M, $\forall$ x $\in$ [a,b].

• Một cách tương tự, đặt

G(x) $= \int_{a}^{x}$ f(t)dt - M $\frac{(x-a)(x-b)}{2}$, $\quad$ x $\in$ [a,b]

(2.12)

sẽ dẫn đến G là một hàm lõm trên [a, b] và bất đẳng thức

$\int_{a}^{x}$ f(t)dt $\geq -\frac{(b-a)^2}{8}M$, $\forall$ x $\in$ [a, b].

Kết luận:

$\max_{x\in[a,b]} \left| \int_a^x$ f(t)dt $\right| \leq \frac{(b-a)^2}{8} \max_{x\in[a,b]}$ |f'(x)|.



§3. TÍCH PHÂN SUY RÔNG

Khi định nghĩa tích phân xác định, chúng ta đã xét các hàm số xác định trên một đoạn

hữu hạn [a, b] và bị chặn trên đoạn đó. Trong phần này chúng ta sẽ mở rộng khái niệm

tích phân, từ đó đưa vào khái niệm tích phân suy rộng với cận vô hạn và tích phân của

hàm số không bị chặn.

## 3.1 Tích phân suy rộng với cận vô hạn hàm số không bị chặn.

Giả sử f(x) là hàm số xác định trên khoảng [a, $+\infty)]$ và khả tích trên mọi đoạn hữu

han [a, A], (a $\leq$ A $< +\infty)$.

Định nghĩa 2.30. Giới hạn của tích phân $\int_{a}^{\infty}$ f(x) dx khi A $\rightarrow +\infty$ được gọi là tích phân

suy rộng của hàm số f(x) trên khoảng [a, $+\infty)$ và ký hiệu như sau

$+\infty$

$\int$ f(x)dx $= \lim_{A \to +\infty} \int$ f(x)dx

Nếu giới hạn này tồn tại hữu hạn ta nói tích phân suy rộng $\int$ f(x)dx hội tụ. Ngược lại,

nếu không tồn tại giới hạn này hoặc giới hạn bằng vô cùng ta nói tích phân đó phân kỳ.

Tương tự ta định nghĩa tích phân của một hàm số f(x) trên các khoảng $(-\infty$, a] và

$(-\infty$, $+\infty)$ bởi các công thức sau

$\int_{a}^{u}$ f(x)dx $= \lim_{A \to -\infty} \int_{A}^{u}$ f(x)dx $\text{$ và $} \int_{a}^{+\infty}$ f(x)dx $= \lim_{A \to +\infty$, A' $\to -\infty} \int_{A}^{A}$ f(x)dx

Ta có thể viết

$\int_{-\infty}^{+\infty}$ f(x)dx $= \int_{-\infty}^{+\infty}$ f(x)dx + $\int_{-\infty}^{u}$ f(x)dx

khi hai trong ba tích phân nói trên hội tụ.

Qua các định nghĩa trên ta thấy rằng tích phân suy rộng là giới hạn của tích phân xác

định (hiểu theo nghĩa thông thường) khi cho cận tích phân dần tới vô cùng. Do đó có thể

dùng công thức Leibniz để tính tích phân, sau đó cho cận tiến ra vô cùng.

$\int_{a}^{A}$ f(x)dx $=$ F(A) - F(a)



kí hiệu

$F(+\infty) = \lim_{A \to \infty}$ F(A)

thì có thể viết

$\int_{a}$ f(x)dx $= F(+\infty)$ - F(a) $= F(x)|_{a}^{+\infty}$

Ví dụ 3.1. a) Tính tích phân $\int_{a^2}^{b^2} \frac{dx}{x \ln$ x $(\ln \ln x)^2}$

Ta có

$\int_{a^{2}}^{A} \frac{dx}{x \ln$ x $(\ln \ln x)^{2}} = -\frac{1}{\ln \ln x}\Big|_{e^{2}}^{A} = \frac{1}{\ln 2}$ - $\frac{1}{\ln \ln A} \frac{n \hat{e} n}{n \hat{e} n} \Rightarrow \lim_{A \to +\infty} \int_{a^{2}}^{A} \frac{dx}{x \ln$ x $(\ln \ln x)^{2}} = \frac{1}{\ln 2}$

Vây

$\int \frac{dx}{x \ln$ x $(\ln \ln x)^2} = \frac{1}{\ln 2}$

b) Tính tích phân $\int \frac{dx}{(x^2+1)^2}$

Trước hết ta tính $\int_1^A \frac{dx}{(x^2+1)^2}$, đặt x $= \tan$ t $\Rightarrow \frac{dx}{(1+x^2)^2} = \frac{dt}{1+\tan^2 t} = \cos^2$ t dt,

$\int_{A'}^{A} \frac{dx}{(x^2+1)^2} = \int_{\arctan A'}^{\arctan A} \frac{1+\cos 2t}{2}$ dt $= \left(\frac{t}{2}$ + $\frac{\sin 2t}{4}\right) \Big|_{\arctan A'}^{\arctan A'}$

Khi A $\to +\infty$, A' $\to -\infty$ thì arctan A $\to \frac{\pi}{2};$ arctan A' $\to -\frac{\pi}{2}$, suy ra

$\int \frac{dx}{(x^2+1)^2} = \left(\frac{t}{2}$ + $\frac{\sin 2t}{4}\right)\bigg|_{-\frac{\pi}{2}}^{\frac{\pi}{2}} = \frac{\pi}{2}$

c) $\int_{-\infty}^{0}$ x $\sin$ x dx $= \lim_{A \to -\infty} \int_{A}^{0}$ x $\sin$ x dx $= \lim_{A \to -\infty}$ (-x $\cos$ x + $\sin x)|_{A}^{0} = \lim_{A \to -\infty}$ (A $\cos$ A - $\sin$ A)

Giới hạn này không tồn tại, do đó tích phân phân kỳ.

d) Xét sự hội tụ của tích phân

I $= \int_{1}^{\infty} \frac{dx}{x^{\alpha}}$

Tích phân suy rộng I hội tụ khi và chỉ khi $\alpha >$ 1, và phân kỳ khi và chỉ khi $\alpha \leq$ 1.



## 3.2 Tích phân suy rộng của hàm số không bị chăn None

Giả sử f(x) là hàm số xác định trên khoảng [a, b) và khả tích trên mọi đoạn [a, t], (t $<$ b)

bất kỳ), và $\lim_{x\to b}$ f(x) $= \infty$. Điểm x $=$ b được gọi là điểm bất thường (điểm kỳ dị) của hàm số

f(x).

Định nghĩa 2.31. Giới hạn của tích phân $\int_{t}^{t}$ f(x) dx khi t $\rightarrow b^{-}$, được gọi là tích phân suy

rộng của hàm số f(x) trên khoảng [a,b) và được ký hiệu như sau:

$\int_{0}^{b}$ f(x)dx $= \lim_{t \to b^{-}} \int_{0}^{t}$ f(x)dx

Nếu giới hạn ở về phải tồn tại, ta nói tích phân suy rộng hội tụ. Ngược lại nếu không tồn

tại giới hạn này hoặc giới hạn bằng vô cùng, ta nói tích phân phân kỳ.

Tương tự ta định nghĩa tích phân suy rộng của hàm số f(x) không bị chặn trên khoảng

(a, b] và (a, b) lần lượt nhận x $=$ a và x $=$ b làm điểm bất thường.

$\int_{a}^{b}$ f(x)dx $= \lim_{t \to a^{+}} \int_{a}^{b}$ f(x)dx $\text{$ và $} \int_{a}^{b}$ f(x)dx $= \lim_{t \to a^{+}$, t' $\to b^{-}} \int_{a}^{b}$ f(x)dx

Đối với tích phân có hai điểm bất thường x $=$ a, x $=$ b, ta có thể viết

$\int_{c}^{b}$ f(x)dx $= \int_{c}^{c}$ f(x)dx + $\int_{c}^{b}$ f(x)dx

khi hai trong ba tích phân nói trên hội tụ.

Ví dụ 3.2. a) Xét sự hội tụ của tích phân $\int_{1}^{1} \frac{dx}{\sqrt{1-x^2}}$

$\int_{-1}^{0} \frac{dx}{\sqrt{1-x^2}} = \lim_{t \to -1} \int_{t}^{0} \frac{dx}{\sqrt{1-x^2}} = \lim_{t \to -1} \arcsin$ x $\Big|_{0}^{0} = \lim_{t \to -1} (-\arcsin$ t) $= \frac{\pi}{2}$

$\int_{0}^{1} \frac{dx}{\sqrt{1-x^2}} = \lim_{t \to 1} \int_{0}^{1} \frac{dx}{\sqrt{1-x^2}} = \lim_{t \to 1} \arcsin$ x $\bigg|_{0}^{1} = \lim_{t \to 1} \arcsin$ t $= \frac{\pi}{2}$

nên

$\int_{1}^{1} \frac{dx}{\sqrt{1-x^2}} = \int_{1}^{0} \frac{dx}{\sqrt{1-x^2}}$ + $\int_{0}^{1} \frac{dx}{\sqrt{1-x^2}} = \pi$



b) Xét sự hội tụ của tích phân I $= \int_{0}^{1} \frac{dx}{x^{\alpha}}$

Tích phân suy rộng I hội tụ khi và chỉ khi $\alpha <$ 1, phân kỳ khi và chỉ khi $\alpha \ge$ 1.

## 3.3 Các tiêu chuẩn hội tu <i>Tích phân suy rộng I hội tụ khi và chỉ khi</i> <math>\alpha</math> < 1, <i>phân kỳ khi và chỉ khi</i> <math>\alpha \ge 1</math>.

### Định lý 2.47 (Tiêu chuẩn so sánh).

1. Cho hai hàm số f(x) và g(x) khả tích trên mọi khoảng hữu hạn [a, A](a $\leq$ A) và

0 $\le$ f(x) $\le$ g(x), x $\ge$ a.

Khi đó

i) Nếu $\int_{a}^{+\infty}$ g(x)dx hội tụ thì $\int_{a}^{+\infty}$ f(x)dx hội tụ

ii) Nếu $\int_{-\infty}^{+\infty}$ f(x)dx phân kỳ thì $\int_{-\infty}^{+\infty}$ g(x)dx phân kỳ.

2. Giả sử f(x) và g(x) là hai hàm số khả tích trên mọi đoạn hữu hạn [a, A](a $\leq$ A) và

$\lim_{x \to +\infty} \frac{f(x)}{g(x)} =$ k(0 $<$ k $< +\infty)$. Khi đó các tích phân $\int_{0}^{\infty}$ f(x) dx và $\int_{0}^{\infty}$ g(x) dx hoặc cùng

hội tụ, hoặc cùng phân kỳ.

Hệ quả 2.6. Cho f và g là hai hàm số dương khả tích trên [a, $+\infty)$. Khi đó

1. Nếu $\lim_{x \to +\infty} \frac{f(x)}{g(x)} =$ 0 và nếu $\int_{-\infty}^{+\infty}$ g(x) dx hội tụ thì $\int_{-\infty}^{+\infty}$ f(x) dx hội tụ.

2. Nếu $\lim_{x \to +\infty} \frac{f(x)}{g(x)} = +\infty$ và nếu $\int_{-\infty}^{+\infty}$ g(x) dx phân kì thì $\int_{-\infty}^{+\infty}$ f(x) dx phân kì.

Tương tự chúng ta cũng có các tiêu chuẩn hội tụ cho trường hợp tích phân suy rộng của

hàm số không bị chặn.

### Định lý 2.48 (Tiêu chuẩn so sánh).

1. Cho hai hàm số f(x) và g(x) khả tích trên (a, b] và có cùng điểm bất thường là x $=$ a

sao cho

0 $\le$ f(x) $\le$ g(x), $\forall$ x $\in$ (a, b]

Khi đó



i) Nếu $\int_{b}^{b}$ g(x) dx hội tụ thì $\int_{b}^{b}$ f(x) dx hội tụ

ii) Nếu $\int_{a}^{b}$ f(x)dx phân kỳ thì $\int_{a}^{b}$ g(x)dx phân kỳ

2. Giả sử f(x) và g(x) là hai hàm số dương khả tích trên (a, b] và có cùng điểm bất

thường x $=$ a. Nếu tồn tại giới hạn

$\n\lim_{x \to a^+} \frac{f(x)}{g(x)} =$ k(0 $<$ k $< +\infty)\n$

Khi đó các tích phân $\int_{0}^{b}$ f(x)dx và $\int_{0}^{b}$ g(x)dx hoặc cùng hội tụ, hoặc cùng phân kỳ.

Hệ quả 2.7. Cho f và g là hai hàm số dương khả tích trên (a,b] và có cùng điểm bất

thường x $=$ a. Khi đó

1. Nếu $\lim_{x\to a^+} \frac{f(x)}{g(x)} =$ 0 và nếu $\int_{a}^{b}$ g(x) dx hội tụ thì $\int_{a}^{b}$ f(x) dx hội tụ.

2. Nếu $\lim_{x\to a^+} \frac{f(x)}{g(x)} = +\infty$ và nếu $\int_a^b$ g(x) dx phân kì thì $\int_a^b$ f(x) dx phân kì.

Chú ý:

• Khi xét đến tính chất hội tụ hay phân kì của một tích phân suy rộng, nói chung

chúng ta chỉ "quan tâm" tới dáng điệu của hàm số tại các điểm bất thường.

• Khi sử dụng tiêu chuẩn so sánh chúng ta thường hay so sánh các tích phân suy rộng

đã cho với hai loại tích phân suy rộng sau:

$ a) I_1 = \int_a^{+\infty} \frac{dx}{x^{\alpha}} \begin{cases} \text{hội tụ nếu} & \alpha > 1 \\ \text{phân kì nếu} & \alpha \leq 1 \end{cases} $

$\mathbf{b})$

$ I_2 = \int_{a}^{b} \frac{dx}{(x-a)^{\alpha}} \begin{cases} \text{hội tụ nếu } \alpha < 1 \\ \text{phân kì nếu } \alpha \ge 1 \end{cases}, I'_2 = \int_{a}^{b} \frac{dx}{(b-x)^{\alpha}} \begin{cases} \text{hội tụ nếu } \alpha < 1 \\ \text{phân kì nếu } \alpha \ge 1 \end{cases} $

Ví du 3.3 (Cuối kì, K61 Viện ĐTQT). Xét sự hội tụ, phân kỳ của tích phân



a) $\int \frac{(1-\cos 2x)dx}{x^2 \ln(1+3\sqrt{x})}$.

b) $\int \frac{(1-\cos 3x)dx}{x^2 \ln(1+2\sqrt{x})}$.

## 3.4 Tích phân suy rộng hội tụ tuyệt đối và bán hội tụ b) <math display="block">\int \frac{(1-\cos 3x)dx}{x^2 \ln(1+2\sqrt{x})}.</math>

Định lý 2.49. 1. Nếu $\int_{-\infty}^{+\infty}$ |f(x)| dx hội tụ thì $\int_{-\infty}^{+\infty}$ f(x) dx hội tụ

2. Nếu $\int_{a}^{b}$ |f(x)| dx (có điểm bất thường là a hoặc b) hội tụ thì $\int_{a}^{+\infty}$ f(x) dx cũng hội tụ

### Định nghĩa 2.32.

1. Nếu $\int_{a}^{+\infty}$ |f(x)| dx hội tụ thì ta nói $\int_{a}^{+\infty}$ f(x) dx hội tụ tuyệt đối, còn nếu $\int_{a}^{+\infty}$ f(x) dx hội tụ

nhưng $\int_{-\infty}^{+\infty}$ |f(x)| dx phân kì thì ta nói $\int_{-\infty}^{+\infty}$ |f(x)| dx bán hội tụ.

2. Nếu $\int_{a}^{b}$ |f(x)| dx (có điểm bất thường là a hoặc b) hội tụ thì ta nói $\int_{a}^{b}$ f(x) dx hội tụ

tuyệt đối, còn nếu $\int_{a}^{b}$ f(x)dx hội tụ nhưng $\int_{a}^{b}$ |f(x)|dx phân kì thì ta nói $\int_{a}^{b}$ |f(x)|dx

bán hội tụ.

Ví dụ 3.4. Chứng minh rằng $\int_{1}^{+\infty} \frac{\cos x}{x^2} h\hat{\varphi}i t\mu tuy\hat{\varphi}t d\hat{\varphi}i$.

Chứng minh. Ta có

$\left|\frac{\cos x}{x^2}\right| \leq \frac{1}{x^2}$

mà $\int_{1}^{+\infty} \frac{1}{x^2}$ hội tụ nên $\int_{1}^{+\infty} \frac{\cos x}{x^2}$ hội tụ tuyệt đối.

$\blacksquare$

Ví dụ 3.5 (Tích phân Dirichlet). Chứng minh rằng $\int_{0}^{+\infty} \frac{\sin x}{x}$ là bán hội tụ.

Chứng minh. Ta có

$\int_{-\infty}^{+\infty} \frac{\sin x}{x} = \int_{-\infty}^{1} \frac{\sin x}{x}$ + $\int_{-\infty}^{+\infty} \frac{\sin x}{x}$.



$\int_0^1 \frac{\sin x}{x}$ thực chất là tích phân xác định vì $\lim_{x\to 0^+} \frac{\sin x}{x} =$ 1, do đó $\int_0^1 \frac{\sin x}{x} \in$ R. Vì vậy chỉ cần

chỉ ra rằng $\int_{1}^{+\infty} \frac{\sin x}{x}$ là hội tụ. Theo công thức tích phân từng phần,

$\int_{1}^{M} \frac{\sin x}{x}$ dx $= -\frac{\cos x}{x} \Big|_{1}^{M}$ + $\int_{1}^{M} \frac{\cos x}{x^2}$ dx $= \cos$ 1 - $\frac{\cos M}{M}$ + $\int_{1}^{M} \frac{\cos x}{x^2}$ dx.

Cho M $\to +\infty$ ta có

$\int \frac{\sin x}{x}$ dx $= \cos$ 1 + $\int \frac{\cos x}{x^2}$ dx.

Mà $\int_{1}^{+\infty} \frac{\cos x}{x^2}$ dx là hội tụ nên $\int_{1}^{+\infty} \frac{\sin x}{x}$ cũng hội tụ. Việc tiếp theo là chỉ ra $\int_{0}^{+\infty} \left|\frac{\sin x}{x}\right|$ dx

là phần kì. Thật vậy,

$\int_{-\infty}^{+\infty} \left| \frac{\sin x}{x} \right|$ dx $= \sum_{n=0}^{+\infty} \int_{-\infty}^{(n+1)\pi} \left| \frac{\sin x}{x} \right|$ dx $= \sum_{n=0}^{+\infty} \int_{-\infty}^{\pi} \frac{\sin v}{v$ + $n\pi}$ dv.

$\text{Vi } \frac{1}{v+n\pi} \geq \frac{1}{(n+1)\pi} \text{$ với $}$ 0 $\leq$ v $\leq \pi \text{ nên}$

$\int_{0}^{\pi} \frac{\sin v}{v$ + $n\pi}$ dv $\ge \frac{1}{(n+1)\pi} \int_{0}^{\pi} \sin$ v dv $= \frac{2}{(n+1)\pi}$.

Mà $\sum_{n=0}^{+\infty} \frac{2}{(n+1)\pi}$ là phân kì nên $\int_{0}^{+\infty} \left| \frac{\sin x}{x} \right|$ dx là phân kì theo tiêu chuẩn so sánh.

## 3.5 Bài tập Mà <math>\sum_{n=0}^{+\infty} \frac{2}{(n+1)\pi}</math> là phân kì nên <math>\int_{0}^{+\infty} \left| \frac{\sin x}{x} \right| dx</math> là phân kì theo tiêu chuẩn so sánh.

Bài tập 2.1. Xét sự hội tụ và tính (trong trường hợp hội tụ) các tích phân sau:

a) $\int_{-\infty}^{0} xe^{x}$ dx

c) $\int_{-\infty}^{+\infty} \frac{dx}{(x^2+1)^2}$

d) $\int_0^1 \frac{dx}{\sqrt{x(1-x)}}$

b) $\int_0^{+\infty} \cos$ x dx

Chứng minh. a) $\int_{-\infty}^{\infty} xe^{x}$ dx $= e^{x}(x-1)\Big|_{-\infty} =$ 1

b) $\int_{0}^{+\infty} \cos$ x dx $= \sin$ x $\Big|_{0}^{+\infty}$. Do không tồn tại giới hạn $\lim_{x \to +\infty} \sin$ x nên tích phân đã cho

phân kì.



c) $\int_{-\infty}^{\infty} \frac{dx}{(x^2+1)^2} =$ 2 $\int_{0}^{+\infty} \frac{dx}{(x^2+1)^2}$. Đặt x $= \tan$ t thì I $=$ 2 $\int_{0}^{\frac{\pi}{2}} \cos^2$ t dt $= \frac{\pi}{2}$

d) $\int_{0}^{1} \frac{dx}{\sqrt{x(1-x)}} = \int_{0}^{\frac{\pi}{2}} \frac{dx}{\sqrt{x(1-x)}}$ + $\int_{\frac{\pi}{2}}^{1} \frac{dx}{\sqrt{x(1-x)}}$

• Xét tích phân $I_1$ có điểm bất thường là x $=$ 0. Khi x $\to$ 0, $\frac{1}{\sqrt{x(1-x)}} \sim \frac{1}{\sqrt{x}}$. Mặt

khác tích phân $\int_{1}^{1} \frac{dx}{\sqrt{x}}$ hội tụ nên $I_1$ hội tụ.

• Xét tích phân $I_2$ có điểm bất thường là x $=$ 1. Khi x $\to$ 1, $\frac{1}{\sqrt{x(1-x)}} \sim \frac{1}{\sqrt{1-x}}$.

Mặt khác tích phân $\int_{0}^{1} \frac{dx}{\sqrt{1-x}}$ hội tụ nên $I_2$ hội tụ.

Vây I $= I_1$ + $I_2$ hôi tu.

Trong trường hợp tổng quát, muốn tính I $= \int_{0}^{b} \frac{dx}{\sqrt{(x-a)(b-x)}}$ ta thực hiện phép đổi

biến

x $= a\cos^2\varphi$ + $b\sin^2\varphi$

sẽ chuyển I về tích phân xác định

$I=2\int_{0}^{\frac{\pi}{2}}d\varphi=\pi$

Bài tập 2.2. Xét sự hội tụ của các tích phân suy rộng sau

c) $\int_{1}^{1} \frac{\sqrt{x} dx}{\sqrt{1-x^4}}$

e) $\int_{-\infty}^{+\infty} \frac{e^{-x^2}}{x^2}$ dx

a) $\int_{0}^{1} \frac{dx}{\tan$ x - $x}$

d) $\int_{-\infty}^{+\infty} \frac{\ln(1+x)dx}{x}$

f) $\int \frac{x^2 dx}{x^4$ - $x^2$ + $1}$

b) $\int \frac{\sqrt{x} dx}{e^{\sin x}$ - $1}$

a) Tích phân đã cho có điểm bất thường là x $=$ 0 và

Chứng minh.

$\n\lim_{x \to 0} \frac{1}{\tan$ x - $x}$ : $\frac{1}{x^3} = \frac{1}{3}\n$



Mặc khác $\int \frac{dx}{x^3}$ phân kì nên $\int \frac{dx}{\tan$ x - $x}$ cũng phân kì.

b) Tích phân đã cho có điểm bất thường là x $=$ 0 và khi x $\to$ 0, $e^{\sin x}$ - 1 $\sim \sin$ x $\sim$ x nên

$\frac{\sqrt{x}}{e^{\sin x}$ - $1} \sim \frac{1}{\sqrt{x}}$. Do $\int_1^1 \frac{dx}{\sqrt{x}}$ hội tụ nên $\int_1^1 \frac{\sqrt{x} dx}{e^{\sin x}$ - $1}$ cũng hội tụ.

c) Tích phân đã cho có điểm bất thường là x $=$ và khi x $\rightarrow$ 1 thì

$\frac{\sqrt{x}}{\sqrt{1-x^4}} = \frac{\sqrt{x}}{\sqrt{(1-x)(1+x+x^2+x^3)}} \sim \frac{1}{2\sqrt{1-x}}$

Do $\int \frac{dx}{\sqrt{1-x}}$ hội tụ nên $\int \frac{\sqrt{x} dx}{\sqrt{1-x^4}}$ cũng hội tụ.

d) Ta có $\frac{\ln(1+x)}{x} > \frac{1}{x}$ với mọi x $>$ e - 1. Mà $\int_{1}^{+\infty} \frac{dx}{x}$ phân kì nên $\int_{1}^{\infty} \frac{\ln(1+x)dx}{x}$ cũng

phân kì.

e) Ta có $e^{-x^2} <$ 1 với mọi x $>$ 0 nên $\frac{e^{-x^2}}{x^2} < \frac{1}{x^2}$ với mọi x $>$ 0. Mặt khác $\int_{0}^{\infty} \frac{dx}{x^2}$ hội tụ nên

$\int_{-\infty}^{+\infty} \frac{e^{-x^2}}{x^2}$ dx cũng hội tụ.

f) Khi x $\to +\infty$ thì $\frac{x^2}{x^4$ - $x^2$ + $1} \sim \frac{1}{x^2}$ nên tích phân đã cho hội tụ.

$\blacksquare$

Bài tập 2.3. Nếu $\int$ f(x)dx hội tụ thì có suy ra được f(x) $\rightarrow$ 0 khi x $\rightarrow +\infty$ không?

[Gợi ý] $\int_a$ f(x)dx hội tụ không suy ra được f(x) $\to$ 0 khi x $\to +\infty$.

Ví dụ như $\int_{0}^{\infty} \sin(x^2)$ dx hội tụ (xem bài tập 2.5) nhưng không tồn tại giới hạn $\lim_{x \to +\infty} \sin(x^2)$.

Bài tập 2.4. Cho hàm số f(x) liên tục trên [a, $+\infty)$ và $\lim_{x \to +\infty}$ f(x) $=$ A $\neq$ 0. Hỏi $\int_{a}^{b}$ f(x) dx

có hội tụ không?



[Gợi ý] Theo giả thiết $\lim_{x \to +\infty} \frac{f(x)}{A} =$ 1, mà $\int$ A dx phân kì nên $\int$ f(x) dx cũng phân

$k\grave{\textit{\i}}$.

Bài tập 2.5. Xét sự hội tụ của các tích phân suy rộng sau

g) $\int_{-\infty}^{+\infty} x^{p-1} e^{-x}$ dx

d) $\int_{1}^{1} \frac{x^2 dx}{\sqrt[3]{(1-x^2)^5}}$

a) $\int_{0}^{\infty} \sin(x^2)$ dx

b) $\int_0^{+\infty} e^{-x^2}$ dx

e) $\int_0^{\frac{\pi}{2}} (\tan x)^p$ dx

h) $\int \frac{f(x)dx}{\sqrt{1-x^2}}$, (f liên tục)

f) $\int_{0}^{1} x^{p-1} (1-x)^{q-1}$ dx

c) $\int_{-\infty}^{+\infty} \left(1$ - $\cos \frac{2}{x}\right)$ dx

a) Thực hiện phép đổi biến x $= \sqrt{t}$, dx $= \frac{dt}{2\sqrt{t}}$, đưa tích phân đã cho về

Chứng minh.

dang

I $= \frac{1}{2} \int_{-\infty}^{+\infty} \frac{\sin$ t $dt}{\sqrt{t}}$

Ta có thể viết

$\int_{0}^{+\infty} \frac{\sin$ t $dt}{\sqrt{t}} = \int_{0}^{\frac{\pi}{2}} \frac{\sin$ t $dt}{\sqrt{t}}$ + $\int_{\frac{\pi}{2}}^{+\infty} \frac{\sin$ t $dt}{\sqrt{t}}$

Vì lim $\frac{\sin t}{t \to 0} =$ 0 nên tích phân $I_1$ thực chất là tích phân xác định nên hội tụ, do đó chỉ

cần xét $I_2$.

$I_2 = \int_{-\pi}^{+\infty} \frac{\sin t}{\sqrt{t}}$ dt $= -\int_{\pi}^{+\infty} \frac{d(\cos t)}{\sqrt{t}} = -\frac{\cos t}{\sqrt{t}} \Big|_{\frac{\pi}{2}}^{+\infty}$ - $\frac{1}{2} \int_{\pi}^{+\infty} \frac{\cos t}{t^{3/2}}$ dt $= -\frac{1}{2} \int_{\pi}^{+\infty} \frac{\cos t}{t^{3/2}}$ dt

Vì $\left|\frac{\cos t}{t^{3/2}}\right| \le \frac{1}{t^{3/2}}$ nên $\int_{\underline{\cdot}}^{\infty} \frac{\cos t}{t^{3/2}}$ dt hội tụ. Vậy ta có $I_2$ cũng hội tụ và tích phân đã cho

hội tụ.

b) Ta có với x $>$ 1 thì $e^{-x^2} < e^{-x}$ mà $\int_{1}^{+\infty} e^{-x}$ dx $= e^{-1}$ hội tụ nên $\int_{1}^{+\infty} e^{-x^2}$ dx cũng hội tụ.

c) Khi x $\to +\infty$, 1 - $\cos \frac{2}{x} =$ 2 $\sin^2 \frac{1}{x} \sim \frac{2}{x^2}$ nên $\int_0^{\infty} \left(1$ - $\cos \frac{2}{x}\right)$ dx hội tụ.



d) Khi x $\to$ 1, $\frac{x^2}{\sqrt[3]{(1-x^2)^5}} = \frac{x^2}{\sqrt[3]{[(1-x)(1+x)]^5}} \sim \frac{1}{\sqrt[3]{32} \cdot \sqrt[3]{(1-x)^5}}$ nên $\int_0^1 \frac{x^2 dx}{\sqrt[3]{(1-x^2)^5}}$

hội tu.

e) Trước hết ta có nhận xét rằng I $= \int_{0}^{\frac{\pi}{2}} (\tan x)^p$ dx có điểm bất thường là x $=$ 0 khi

p $<$ 0 và x $= \frac{\pi}{2}$ khi p $>$ 0.

• Nếu p $<$ 0 thì khi x $\to$ 0, $(\tan x)^p = \left(\frac{\cos x}{\sin x}\right)^{-p} \sim \frac{1}{x^{-p}}$ nên I hội tụ nếu -1 $<$

p $<$ 0 và phân kì nếu p $\le$ -1.

• Nếu p $>$ 0 thì khi x $\to \frac{\pi}{2}$, $(\tan x)^p = \left(\frac{\sin x}{\cos x}\right)^p = \left(\frac{\sin x}{\sin \left(\frac{\pi}{2}$ - $x\right)}\right)^r \sim \frac{1}{\left(\frac{\pi}{2}$ - $x\right)^p}$

nên I hội tụ nếu 0 $<$ p $<$ 1 và phân kì nếu p $\ge$ 1.

Kết luận: $\int_0^{\frac{\pi}{2}} (\tan x)^p$ dx hội tụ khi |p| $<$ 1 và phân kì khi |p| $\ge$ 1.

f) Trước hết ta có nhận xét rằng nếu p $<$ 1 thì x $=$ 0 là điểm bất thường, còn nếu q $<$ 1

thì x $=$ 1 là điểm bất thường. Phân tích

I $= \int_{0}^{1} x^{p-1} (1-x)^{q-1}$ dx $= \int_{0}^{\frac{1}{2}} x^{p-1} (1-x)^{q-1}$ dx + $\int_{\frac{1}{2}}^{1} x^{p-1} (1-x)^{q-1}$ dx

$I_1$ chỉ hội tụ khi 1 - p $<$ 1, nghĩa là p $>$ 0; còn $I_2$ chỉ hội tụ khi 1 - q $<$ 1, nghĩa là

q $>$ 0. Vậy I chỉ hội tụ khi p $>$ 0, q $>$ 0.

g) Nếu p $\ge$ 1 thì tích phân đã cho chỉ có điểm bất thường tại $+\infty$ và

$\n\lim_{x \to +\infty} [x^{p-1}e^{-x}]$ : $\frac{1}{x^2} = \lim_{x \to +\infty} \frac{x^{p+1}}{e^x} = 0\n$

nên $\int x^{p-1}e^{-x}dx$ hội tụ.

x $\rightarrow +\infty$

Nếu p $<$ 1 thì x $=$ 0 cũng là một điểm bất thường. Ta có

$\int_{0}^{+\infty} x^{p-1}e^{-x}dx = \int_{0}^{1} x^{p-1}e^{-x}dx$ + $\int_{1}^{+\infty} x^{p-1}e^{-x}dx$



Tích phân $I_1$ hội tụ khi p $>$ 0 và $I_2$ hội tụ với p bất kì.

Vậy $\int_{0}^{1} x^{p-1}e^{-x}dx$ hội tụ nếu p $>$ 0.

h) Mặc dù tích phân đã cho là tích phân suy rộng có điểm bất thường là x $=$ 1 nhưng ta

có thể đưa I về tích phân thường bằng cách đổi biến. Đặt x $= \sin \theta$, trên [0, c] ta có

$\int_{0}^{1} \frac{f(x)dx}{\sqrt{1-x^2}} = \lim_{c \to 1^{-}} \int_{0}^{c} \frac{f(x)dx}{\sqrt{1-x^2}} = \lim_{c \to 1^{-}} \int_{0}^{\arcsin c} f(\sin \theta) d\theta = \int_{0}^{\frac{\pi}{2}} f(\sin \theta) d\theta$

Vì f là một hàm số liên tục trên [0, 1] nên hàm hợp f(sin $\theta)$ là một hàm số liên tục và

bị chặn trên $\left[0$, $\frac{\pi}{2}\right]$ và tích phân đã cho là tích phân xác định nên hội tụ.

$\blacksquare$

Bài tập 2.6. Tính các tích phân suy rộng sau

a) $\int_{-\infty}^{+\infty} e^{-ax} \sin$ bx dx b) $\int_{-\infty}^{+\infty} e^{-ax} \cos$ bx dx c) $\int_{-\infty}^{+\infty} \frac{dx}{1+x^4}$

Chứng minh. a) $\int e^{-ax} \sin$ bx dx $= -\frac{a \sin$ bx + b $\cos bx}{a^2$ + $b^2} e^{-ax} \Big|_0^{+\infty} = \frac{b}{a^2$ + $b^2}$

b) $\int e^{-ax} \cos$ bx dx $= \frac{b \sin$ bx - a $\cos bx}{a^2$ + $b^2} e^{-ax} \Big|_0^{+\infty} = \frac{b}{a^2$ + $b^2}$

c) Thực hiện phép đổi biến x $= \frac{1}{t}$ ta có

I $= \int_{-\infty}^{+\infty} \frac{dx}{1+x^4} = \int_{-\infty}^{+\infty} \frac{t^2 dt}{1+t^4} = \int_{-\infty}^{+\infty} \frac{x^2 dx}{1+x^4}$

Do đó

2I $= \int_{0}^{+\infty} \frac{dx}{1+x^4}$ + $\int_{0}^{+\infty} \frac{x^2 dx}{1+x^4} = \int_{0}^{+\infty} \frac{(1+x^2) dx}{1+x^4} = \int_{0}^{+\infty} \frac{\left(1+\frac{1}{x^2}\right) dx}{x^2+\frac{1}{x^2}}$

Lại đặt z $=$ x - $\frac{1}{x}$ ta được

I $= \frac{1}{2} \int_{-\infty}^{\infty} \frac{z}{z^2$ + $2} = \frac{1}{2\sqrt{2}} \arctan \frac{z}{\sqrt{2}} \Big|_{-\infty}^{+\infty} = \frac{\pi}{2\sqrt{2}}$



§4. CÁC ỨNG DỤNG CỦA TÍCH PHẦN XÁC ĐỊNH

## 4.1 Tính diên tích hình phẳng <b>§4. CÁC ỨNG DỤNG CỦA TÍCH PHẦN XÁC ĐỊNH</b>

1. Trường hợp biên của hình phẳng cho trong hệ toạ độ Descartes (tính diện tích "hình

thang cong")

$ Nếu S giới hạn bởi \begin{cases} a \le x \le b \\ y = f(x) \\ y = g(x) \\ f, g \in C[a, b] \end{cases} thì S = \int_{a}^{b} |f(x) - g(x)| dx (2.13) $

$ Nếu S giới hạn bởi \begin{cases} c \le y \le d \\ x = \varphi(y) \\ x = \psi(y) \end{cases} thì S = \int_{c}^{d} |\varphi(y) - \psi(y)| dy (2.14) $

$\varphi$, $\psi \in$ [c, d]

$ Nếu S giới hạn bởi \begin{cases} a \le x \le b \\ y = 0 \\ x = \varphi(t) \\ y = \psi(t) \end{cases} thì S = \int_{t_1}^{t_2} |\psi(t)\varphi'(t)| dt $

(2.15)

Trong đó giả thiết rằng phương trình $\varphi(t) =$ a, $\psi(t) =$ b có nghiệm duy nhất là $t_1$, $t_2$ và

$\varphi$, $\psi$, $\varphi' \in C[t_1$, $t_2]$.

Ví dụ 4.1 (Cuối kì, K61-Viện ĐTQT). Tính diện tích của miền

$ b) D: \begin{cases} x - y \geq 2 \\ x^2 + y^2 \leq 2x. \end{cases} $

$ a) D: \begin{cases} x + y \geq 2 \\ x^2 + y^2 < 2x. \end{cases} $

Bài tập 2.1. Tính diện tích hình phẳng giới hạn bởi:

a) Dường parabol y $= x^2$ + 4 và đường thẳng x - y + 4 $=$ 0.

b) Parabol bậc ba y $= x^3$ và các đường y $=$ x, y $=$ 2x.

c) Dường tròn $x^2$ + $y^2 =$ 2x và parabol $y^2 =$ x

d) Duờng $y^2 = x^2$ - $x^4$



[Gợi $\acute{y}]$

Các câu a), b), c) có thể vẽ hình và tính toán dễ dàng như sau:

a) S $= \int_{0}^{1}$ [(x+4) - $(x^2+4)]$ dx $= \frac{1}{6}$

b) S $= \int_{0}^{1}$ (2x - $x^2)$ dx + $\int_{2}^{\sqrt{2}}$ (2x - $x^3)$ dx $= \frac{3}{4}$

c) S $=$ 2 $\int_{0}^{2} (\sqrt{4x$ - $x^2})$ - $\sqrt{2x}$ dx $= 2\pi$ - $\frac{16}{3}$

d) Trước hết ta có điều kiện 0 $\le$ x $\le$ 1, và nhận xét rằng nếu M(x, y) $\in$ C thì $M'(\pm$ x, $\pm$ y) $\in$

$ C. Do đó S = 4S(D), trong đó D là miền giới hạn bởi: \begin{cases} 0 \le x \le 1 \\ y = \sqrt{x^2 - x^4} \end{cases} $

Do miền D nằm hoàn toàn trong hình vuông 0 $\le$ x $\le$ 1, 0 $\le$ y $\le$ 1, hơn nữa hàm số

y $= \sqrt{x^2$ - $x^4}$ liên tục, y(0) $=$ y(1) $=$ 0 nên đồ thị của nó trong [0,1] có hình dáng

như hình vẽ dưới đây:

$\mathop{\mathcal{X}_{}}\nolimits$

Áp dụng công thức 2.13 ta có S(D) $= \int_{0}^{1} \sqrt{x^2$ - $x^4}$ dx $= \frac{1}{3} \Rightarrow$ S $= \frac{4}{3}$.

2. Trường hợp biên của hình phẳng cho trong hệ toạ độ cực (tính diện tích của miền có

dạng hình quạt)

$ Nếu S giới hạn bởi \begin{cases} \varphi = \alpha \\ \varphi = \beta \\ r = r(\varphi) \\ r(\varphi) \in C[\alpha, \beta] \end{cases} thì S = \frac{1}{2} \int_{\alpha}^{\beta} r^{2}(\varphi) d\varphi $

(2.16)



Bài tập 2.2. Tính diện tích hình phẳng giới hạn bởi đường hình tim $r^2 = a^2 \cos 2\varphi$

[Gợi $\acute{y}]$

$\int_{-\infty}^{g}$ r $=$ a $\sqrt{\cos 2\varphi}$

$\mathop{\mathcal{X}_{}}\nolimits$

Hình 2.2

Khảo sát và vẽ đồ thị của đường cong trong toạ độ cực và nhận xét tính đối xứng của

hình vẽ ta có:

S $=$ 4S(D) $= 4.\frac{1}{2} \int_{0}^{\frac{\pi}{4}} r^{2}(\varphi) d\varphi = a^{2}$.

## 4.2 Tính độ dài đường cong phẳng <math display="block">S = 4S(D) = 4.\frac{1}{2} \int_{0}^{\frac{\pi}{4}} r^{2}(\varphi) d\varphi = a^{2}.</math>

Trường hợp đường cong AB cho bởi phương trình y $=$ f(x)

$ AB\begin{cases}y = f(x) \\ a \le x \le b \\ f \in C^{1}[a, b]\end{cases} thi s = \int_{a}^{b} \sqrt{1 + [f'(x)]^{2}} $

(2.17)

Trường hợp đường cong AB cho bởi phương trình tham số:

$ AB\begin{cases} x = x(t) \\ y = y(t) \\ \alpha \le t \le \beta \\ x(t), y(t) \in C^{1}[a, b] \\ x'^{2}(t) + y'^{2}(t) > 0 \forall t \in [\alpha, \beta] \end{cases} $

$\text{thi}\left|s=\int\limits_{\alpha}^{t}\sqrt{[x'(t)]^2+[y'(t)]^2}dt\right|$

(2.18)

Trường hợp đường cong AB cho bởi phương trình trong toạ độ cực:

$ AB\begin{cases} r = r(\varphi) \\ \alpha \leq \varphi \leq \beta \\ r(\varphi) \in C^{1}[\alpha, \beta] \end{cases} \text{thi} \begin{cases} s = \int_{\alpha}^{\beta} \sqrt{r^{2}(\varphi) + r'^{2}(\varphi)} d\varphi \end{cases} $

(2.19)



Bài tập 2.1. Tính độ dài đường cong

a) y $= \ln \frac{e^x+1}{e^x-1}$ khi x biến thiên từ 1 đến 2.

$ b) \begin{cases} x = a(\cos t + \ln \tan \frac{t}{2}) \\ y = a \sin t \end{cases} khi t biến thiên từ \frac{\pi}{3} đến \frac{\pi}{2}. $

$Ch\núng$ minh. a) Ta có

1 + $y'^2(x) =$ 1 + $\left(\frac{e^x}{e^x$ + $1}$ - $\frac{e^x}{e^x$ - $1}\right)^2 = \left(\frac{e^{2x}$ + $1}{e^{2x}$ - $1}\right)^2$

Nên áp dụng công thức 2.17 ta được:

s $= \int_{1}^{2} \frac{e^{2x}$ + $1}{e^{2x}$ - $1}$ dx $\stackrel{(t=e^{2x})}{=} \int_{2}^{e^{2x}} \frac{t+1}{2t(t-1)} = \ln \frac{e^{2}$ + $1}{e^{2}}$

b) Ap dung công thức 2.18 ta có

$x^{2}(t)$ + $y^{2}(t) = a^{2} \cdot \frac{\cos^{2} t}{\sin^{2} t} \Rightarrow$ s $=$ a $\int_{\frac{\pi}{2}}^{\frac{\pi}{2}} \sqrt{\frac{\cos^{2} t}{\sin^{2} t}}$ dt $=$ a $\ln \sqrt{\frac{2}{\sqrt{3}}}$

## 4.3 Tính thể tích vật thể <math display="block">x^{2}(t) + y^{2}(t) = a^{2} \cdot \frac{\cos^{2} t}{\sin^{2} t} \Rightarrow s = a \int_{\frac{\pi}{2}}^{\frac{\pi}{2}} \sqrt{\frac{\cos^{2} t}{\sin^{2} t}} dt = a \ln \sqrt{\frac{2}{\sqrt{3}}}</math>

Trường hợp vật thể được giới hạn bởi một mặt cong và hai mặt phẳng x $=$ a, x $=$ b. Giả

thiết ta biết rằng diện tích S của thiết diện của vật thể khi cắt bởi mặt phẳn x $= x_0$ là

$S(x_0)$, và S(x) là hàm số xác định, khả tích trên [a, b]. Khi đó

V $= \int_{a}^{b}$ S(x) dx

(2.20)

Bài tập 2.1. Tính thể tích của vật thể là phần chung của hai hình trụ $x^2$ + $y^2 = a^2$ và

$y^2$ + $z^2 = a^2$ (a $>$ 0).

Lời giải: Do tính đối xứng nên V $=$ 8V' trong đó V' $=$ V $\cap \{x \ge$ 0, y $\ge$ 0, z $\ge 0\}$. Một

điểm M(x,0,0) $\in$ Ox, qua M ta dựng thiết diện của V' vuông góc với Ox thì được một hình

vuông có cạnh là $\sqrt{a^2$ - $x^2}$, do đó S(x) $= a^2$ - $x^2$. Áp dụng công thức 2.20 ta được

V $=$ 8 $\int_{0}^{u} (a^{2}$ - $x^{2})$ dx $= \frac{16}{3}a^{3}$



Bài tập 2.2. Tìm thể tích vật thể giới hạn bởi mặt paraboloit z $=$ 4 - $y^2$, các mặt phẳng

toạ độ và mặt phẳng x $=$ a.

Chứng minh. Sau khi vẽ hình và áp dụng công thức 2.20 ta có:

V $= \int_{0}^{a}$ S(x)dx $\text{$ mà $}$ S(x) $= \int_{0}^{2}$ (4 - $y^{2})dy = \frac{16}{3} \text{$ nên $}$ V $= \frac{16}{3}a$

Tính thể tích vật thể tròn xoay

$ \n\begin{cases}\na \leq x \leq b \\
y = 0 \quad \text{quanh truc } Ox, \text{ trong } d\acute{o} f \in C[a, b] \text{ thì} \\
y = f(x)\n\end{cases}\n $

Trường hợp vật thể là vật thể tròn xoay được tạo thành khi quay hình thang cong

V $= \pi \int_{0}^{x} f^{2}(x)$ dx

(2.21)

$\mathcal{A}$

Tương tự, nêú vật thể là vật thể tròn xoay được tạo thành khi quay hình thang cong

$ \n\begin{cases}\nc \le y \le d \\
x = 0 \quad \text{quanh truc } Oy, \text{ trong đó } \varphi \in C[c, d] \text{ thì} \\
x = \varphi(y)\n\end{cases}\n $

V $= \pi \int_{c}^{\pi} \varphi^{2}(y)$ dy

(2.22)

Bài tập 2.3. Tính thể tích khối tròn xoay tạo nên khi quay hình giới hạn bởi các đường

y $=$ 2x - $x^2 \dot{u} \dot{u} =$ 0

a) quanh truc Ox một vòng

b) quanh truc Oy một vòng.

[Gơi ý]

a) Áp dụng công thức 2.21:

V $= \pi \int$ (2x - $x^2)$ dx $=$

b) Ap dụng công thức 2.22:

V $= \pi \int$ (1 + $\sqrt{1$ - $y})^2$ dy - $\pi \int$ (1 - $\sqrt{1$ - $y})^2$ dy



## 4.4 Tính diên tích mặt tròn xoay None

$ Cho hình thang cong giới hạn bởi \begin{cases} a \leq x \leq b \\ y = 0 \\ y = f(x) \end{cases} với f \in C^1[a, b]. Quay hình thang cong $

này quanh trục Ox thì ta được một vật thể tròn xoay. Khi đó diện tích xung quanh của vật

thể được tính theo công thức:

S $= 2\pi \int_{a}^{b}$ |f(x)| $\sqrt{1$ + $f'^2(x)}$ dx

(2.23)

$ Tương tự nếu quay hình thang cong \begin{cases} c \le y \le d \\ x = 0 \\ x = \varphi(y) \end{cases} với \varphi \in C^1[c, d], quanh trục Oy thì: $

S $= 2\pi \int_{c}^{u} |\varphi(y)| \sqrt{1$ + $\varphi'^{2}(y)}$ dy

(2.24)

Bài tập 2.1. Tính diện tích mặt tròn xoay tạo nên khi quay các đường sau

a) y $= \tan$ x, 0 $<$ x $\leq \frac{\pi}{4}$ quanh trục Ox.

b) $\frac{x^2}{a^2}$ + $\frac{y^2}{b^2} =$ 1 quanh trục Oy(a $>$ b)

c) $9y^2 = x(3-x)^2$, 0 $\le$ x $\le$ 3 quanh truc Ox.



a) Áp dụng công thức 2.23 ta có:

Chứng minh.

S $= 2\pi \int_{0}^{\frac{\pi}{4}} \tan$ x $\sqrt{1$ + (1 + $\tan^2 x)}$ dx

$= 2\pi \int_{0}^{1}$ t $\sqrt{1$ + (1 + $t^{2})^{2}} \cdot \frac{dt}{1$ + $t^{2}} \quad (d\check{a}t \;$ t $= \tan$ x)

$= \pi \int_{1}^{1} \frac{\sqrt{1$ + (1 + $t^2)^2}}{1$ + $t^2} d(t^2$ + 1)

$= \pi \int_{-\infty}^{\infty} \frac{\sqrt{1+s^2}}{s}$ ds $\quad (d\check{a}t \$ s $=$ 1 + $t^2)$

$= \pi \int_{0}^{\sqrt{5}} \left(1$ + $\frac{1}{u^2$ - $1}\right)$ du

$= \pi \cdot \left\{ \sqrt{5}$ - $\sqrt{2}$ + $\frac{1}{2} \left[ \ln \frac{\sqrt{5}$ - $1}{\sqrt{2}$ - $1}$ - $\ln \frac{\sqrt{5}$ + $1}{\sqrt{2}$ + $1} \right] \right\}$

b) Nhận xét tính đối xứng của miền và áp dụng công thức 2.24 ta có:

S $= 2.2\pi \int_{0}^{b} \frac{a}{b} \sqrt{b^2$ - $y^2} \cdot \sqrt{1$ + $\left(\frac{a}{b} \cdot \frac{y}{\sqrt{b^2$ - $y^2}}\right)^2}$ dy

$= 4\pi \frac{a}{b} \int_{0}^{b} \sqrt{b^4$ + $(a^2$ - $b^2)y^2}$ dy

$=4\pi \frac{a}{b}\sqrt{a^2-b^2}\int_{b}^{b}\sqrt{y^2+\frac{b^4}{a^2-b^2}}dy$

$= 4\pi \frac{a}{b} \sqrt{a^2$ - $b^2} \int_{0}^{b} \sqrt{y^2$ + $\beta}$ dy $(\text{ d\#t } \beta = \frac{b^4}{a^2$ - $b^2})$

$= 4\pi \frac{a}{b} \sqrt{a^2$ - $b^2} \cdot \frac{1}{2} \left[$ y $\sqrt{y^2$ + $\beta}$ + $\beta \ln$ |y + $\sqrt{y^2$ + $\beta}| \right] \bigg|^{b}$

$\left(\int \sqrt{y^2$ + $\beta}$ dy $= \frac{1}{2} \left[$ y $\sqrt{y^2$ + $\beta}$ + $\beta \ln$ |y + $\sqrt{y^2$ + $\beta}| \right] \right)$

$\blacksquare$

c) Trước hết

$9y^2 = x(3-x)^2 \Rightarrow$ 18yy' $=$ 3(3-x)(1-x) $\Rightarrow$ y' $= \frac{(3-x)(1-x)}{6y} \Rightarrow y'^2 = \frac{(1-x)^2}{4x}$



a) Áp dụng công thức 2.23 ta có:

Chứng minh.

S $= 2\pi \int_{0}^{\frac{\pi}{4}} \tan$ x $\sqrt{1$ + (1 + $\tan^2 x)}$ dx

$= 2\pi \int_{0}^{1}$ t $\sqrt{1$ + (1 + $t^{2})^{2}} \cdot \frac{dt}{1$ + $t^{2}} \quad (d\check{a}t \;$ t $= \tan$ x)

$= \pi \int_{1}^{1} \frac{\sqrt{1$ + (1 + $t^2)^2}}{1$ + $t^2} d(t^2$ + 1)

$= \pi \int_{-\infty}^{\infty} \frac{\sqrt{1+s^2}}{s}$ ds $\quad (d\check{a}t \$ s $=$ 1 + $t^2)$

$= \pi \int_{0}^{\sqrt{5}} \left(1$ + $\frac{1}{u^2$ - $1}\right)$ du

$= \pi \cdot \left\{ \sqrt{5}$ - $\sqrt{2}$ + $\frac{1}{2} \left[ \ln \frac{\sqrt{5}$ - $1}{\sqrt{2}$ - $1}$ - $\ln \frac{\sqrt{5}$ + $1}{\sqrt{2}$ + $1} \right] \right\}$

b) Nhận xét tính đối xứng của miền và áp dụng công thức 2.24 ta có:

S $= 2.2\pi \int_{0}^{b} \frac{a}{b} \sqrt{b^2$ - $y^2} \cdot \sqrt{1$ + $\left(\frac{a}{b} \cdot \frac{y}{\sqrt{b^2$ - $y^2}}\right)^2}$ dy

$= 4\pi \frac{a}{b} \int_{0}^{b} \sqrt{b^4$ + $(a^2$ - $b^2)y^2}$ dy

$=4\pi \frac{a}{b}\sqrt{a^2-b^2}\int_{b}^{b}\sqrt{y^2+\frac{b^4}{a^2-b^2}}dy$

$= 4\pi \frac{a}{b} \sqrt{a^2$ - $b^2} \int_{0}^{b} \sqrt{y^2$ + $\beta}$ dy $(\text{ d\#t } \beta = \frac{b^4}{a^2$ - $b^2})$

$= 4\pi \frac{a}{b} \sqrt{a^2$ - $b^2} \cdot \frac{1}{2} \left[$ y $\sqrt{y^2$ + $\beta}$ + $\beta \ln$ |y + $\sqrt{y^2$ + $\beta}| \right] \bigg|^{b}$

$\left(\int \sqrt{y^2$ + $\beta}$ dy $= \frac{1}{2} \left[$ y $\sqrt{y^2$ + $\beta}$ + $\beta \ln$ |y + $\sqrt{y^2$ + $\beta}| \right] \right)$

$\blacksquare$

c) Trước hết

$9y^2 = x(3-x)^2 \Rightarrow$ 18yy' $=$ 3(3-x)(1-x) $\Rightarrow$ y' $= \frac{(3-x)(1-x)}{6y} \Rightarrow y'^2 = \frac{(1-x)^2}{4x}$



Nên áp dụng công thức 2.23 ta có:

S $= 2\pi \int_{0}^{3} \frac{\sqrt{x(3-x)}}{3} \cdot \sqrt{1$ + $\frac{(1-x)^2}{4x}}$ dx $= 2\pi \cdot \frac{1}{6} \int_{0}^{3}$ (3-x)(1+x) dx $= 3\pi$.

"Nghịch lý sừng Gabriel"

$ Cho một vật thể tròn xoay tạo bởi khi xoay miền giới hạn bởi \begin{cases} 1 \leq x, \\ y = 0, \\ y = \frac{1}{x} \end{cases} quanh trục Ox. $

Tính thể tích và diện tích mặt của nó.



![](graphs/img_144_0.png)

[Lời giải] Ta có

V $= \pi \int_{-\infty}^{+\infty} \left(\frac{1}{x}\right)^2$ dx $= \pi$

và

S $= 2\pi \int_{-\infty}^{+\infty} \frac{1}{x} \sqrt{1$ + $\left(-\frac{1}{x^2}\right)^2}$ dx $\ge 2\pi \int_{1}^{+\infty} \frac{1}{x}$ dx $= +\infty$.

Như vậy, đây là một vật thể có diện tích mặt bằng $+\infty$, trong khi đó lại có thể tích hữu

hạn. Giả sử bạn có một vật thể như vậy và cần sơn nó.

i) Một mặt, vì diện tích mặt là $+\infty$, bạn cần một lượng vô hạn sơn để sơn nó.

ii) Mặt khác, vì miền giới hạn bởi vật đó có thể tích hữu hạn, bạn có thể đổ đầy nó bằng

một lượng hữu hạn sơn (ở đây là $\pi$ đơn vị thể tích), và khi đó toàn bộ mặt trong của

nó sẽ được sơn.

Một nghịch lý phải không?





$\frac{3}{\text{CHƯƠNG}}$

HÀM SỐ NHIỀU BIẾN SỐ

$\S1$. GIỚI HẠN CỦA HÀM SỐ NHIỀU BIẾN SỐ

## 1.1 Giới hạn của hàm số nhiều biến số <math display="inline">\S1.</math> GIỚI HẠN CỦA HÀM SỐ NHIỀU BIẾN SỐ

Ta nói rằng dãy điểm $\{M_n(x_n$, $y_n)\}\dần$ tới điểm $M_0(x_0$, $y_0)$ trong $\mathbb{R}^2$ và viết $M_n \to M_0$

khi n $\to +\infty$ nếu $\lim_{n \to +\infty} d(M_n$, $M_0) =$ 0 hay nếu $x_n \to x_0$, $y_n \to y_0$.

Định nghĩa 3.33. Cho hàm số z $=$ f(M) $=$ f(x, y) xác định trong một lân cận V nào đó

của điểm $M_0(x_0$, $y_0)$, có thể trừ tại điểm $M_0$. Ta nói rằng hàm số f(x, y) có giới hạn là L

khi M dần đến $M_0$ nếu

$\forall \epsilon >$ 0, $\exists \delta >$ 0 : $\text{ n\'{e}u }$ d(M, $M_0) < \delta \text{ th\'{i}}$ | f(M) - L | $< \epsilon$.

Một cách tương đương, với mọi dãy điểm $M_n(x_n$, $y_n)$ thuộc lân cận V dần đến $M_0$ ta đều có

$\n\lim_{n\to+\infty}f(x_n,y_n)=L.\n$

Khi đó ta viết

$\lim_{(x,y)\to(x_0,y_0)}$ f(x,y) $=$ L $\; \text{hay} \; \lim_{M\to M_0}$ f(M) $=$ L.

• Khái niệm giới hạn vô hạn cũng được định nghĩa tương tự như đối với hàm số một

biến số.

• Các định lý về giới hạn của tổng, hiệu, tích, thương đối với hàm số một biến số cũng

đúng cho hàm số nhiều biến số và được chứng minh tương tự.

Nhận xét:



• Theo định nghĩa trên, muốn chứng minh sự tồn tại của giới hạn của hàm số nhiều

biến số là việc không dễ vì phải chỉ ra $\lim_{n\to+\infty} f(x_n$, $y_n) =$ l với mọi dãy số $\{x_n \to$

$x_0$, $\{y_n \rightarrow y_0\}$. Trong thực hành, muốn tìm giới hạn của hàm số nhiều biến số,

phương pháp chứng minh chủ yếu là đánh giá hàm số, dùng nguyên lý giới hạn kẹp

để đưa về giới hạn của hàm số một biến số.

• Với chiều ngược lại, muốn chứng minh sự không tồn tại giới hạn của hàm số nhiều

biến số, ta chỉ cần chỉ ra tồn tại hai dãy $\{x_n \to x_0$, $y_n \to y_0\}$ và $\{x'_n \to x_0$, $y'_n \to y_0\}$

sao cho

$\lim_{n\to+\infty} f(x_n,y_n) \neq \lim_{n\to+\infty} f(x'_n,y'_n)$

hoặc chỉ ra tồn tại hai quá trình (x,y) $\rightarrow (x_0$, $y_0)$ khác nhau mà f(x, y) tiến tới hai

giới hạn khác nhau.

## 1.2 Tính liên tục của hàm số nhiều biến số giới hạn khác nhau.

• Giả sử hàm số f(M) xác định trong miền D, $M_0$ là một điểm thuộc D. Ta nói rằng

hàm số f(M) liên tục tại điểm $M_0$ nếu

$\n\lim_{M \to M_0}$ f(M) $= f(M_0)\n$

Nếu miền D đóng và $M_0$ là điểm biên của D thì $\lim_{M\to M_0}$ f(M) được hiểu là giới hạn

của f(M) khi M dần tới $M_0$ ở bên trong của D.

• Hàm số f(M) được gọi là liên tục trong miền D nếu nó liên tục tại mọi điểm thuộc

D.

• Hàm số nhiều biến số liên tục cũng có những tính chất như hàm số một biến số liên

tục. Chẳng hạn, nếu hàm số nhiều biến số liên tục trong một miền đóng, bị chặn thì

nó liên tục đều, bị chặn trong miền ấy, đạt giá trị lớn nhất và giá trị nhỏ nhất trong

miền đó.

## 1.3 Bài tập miền đó.

Bài tập 3.1. Tìm miền xác định của các hàm số sau

a) z $= \frac{1}{\sqrt{x^2$ + $y^2$ - $1}}$

c) z $= \arcsin \frac{y-1}{x}$

b) z $= \sqrt{(x^2$ + $y^2$ - 1)(4 - $x^2$ - $y^2)}$

d) z $= \sqrt{x \sin y}$

Bài tập 3.2. Tìm giới hạn (nếu có) của các hàm số sau



b) f(x,y) $= \sin \frac{\pi x}{2x$ + $y}$ (x $\to \infty$, y $\to \infty)$

a) f(x,y) $= \frac{x^2$ - $y^2}{x^2$ + $y^2}$ (x $\to$ 0, y $\to$ 0)

a) Nếu cho (x, y) $\rightarrow$ (0, 0) theo phương của đường thẳng y $=$ kx thì ta có

Chứng minh.

f(x,kx) $= \frac{x^2$ - $k^2x^2}{x^2$ + $k^2x^2} = \frac{1$ - $k^2}{1$ + $k^2} \rightarrow \frac{1$ - $k^2}{1$ + $k^2}$ khi x $\rightarrow$ 0

Vậy khi (x, y) $\rightarrow$ (0, 0 theo những phương khác nhau thì f(x, y) dần tới những giới

hạn khác nhau. Do đó không tồn tại $\lim_{(x,y)\to(0,0)}$ f(x,y).

b) Nếu cho (x, y) $\rightarrow (\infty$, $\infty)$ theo phương của đường thẳng y $=$ kx thì ta có

f(x,kx) $= \sin \frac{\pi x}{2x$ + $kx} = \sin \frac{\pi}{2$ + $k} \rightarrow \sin \frac{\pi}{2$ + $k}$ khi x $\rightarrow$ 0

Vậy khi (x,y) $\rightarrow$ (0,0 theo những phương khác nhau thì f(x,y) dần tới những giới

hạn khác nhau. Do đó không tồn tại $\lim_{(x,y)\to(0,0)}$ f(x,y).

$\blacksquare$

Bài tập 3.3. [Cuối kì, K62, GT2, Nhóm ngành 2] Tính các giới hạn

b) $\lim_{(x,y)\to(0,0)} \frac{x^4$ + $2y^4}{2x^2$ + $1/2}$.

a) $\lim_{(x,y)\to(0,0)} \frac{2x^4$ + $y^4}{x^2$ + $2y^2}$.

[Lời giải] Ta có

$\mathbf{a})$

$\n\lim_{(x,y)\to(0,0)}\frac{2x^2+y^2}{x^2+2y^2}=\lim_{(x,y)\to(0,0)}\frac{2x^4}{x^2+2y^2}+\lim_{(x,y)\to(0,0)}\frac{y^4}{x^2+2y^2}=0+0=0,\n$

do 0 $\le \frac{2x^4}{x^2$ + $2y^2} \le 2x^2$, 0 $\le \frac{y^4}{x^2$ + $2y^2} \le \frac{1}{2}y^2$ và nguyên lý giới hạn kẹp.

b)

$\lim_{(x,y)\to(0,0)}\frac{x^4+2y^4}{2x^2+y^2}=\lim_{(x,y)\to(0,0)}\frac{x^4}{2x^2+y^2}+\lim_{(x,y)\to(0,0)}\frac{2y^4}{2x^2+y^2}=0+0=0$,

do 0 $\le \frac{x^4}{2x^2$ + $y^2} \le \frac{1}{2}x^2$, 0 $\le \frac{2y^4}{2x^2$ + $y^2} \le 2y^2$ và nguyên lý giới hạn kẹp.

Chú ý 3.20. Không nhầm lẫn $\lim_{(x,y)\to(x_0,y_0)}$ f(x,y) với các giới hạn lặp $\lim_{x\to x_0} \lim_{y\to y_0}$ f(x,y) và

$\lim_{y\to y_0}\lim_{x\to x_0}$ f(x,y). Chẳng hạn như, bạn đọc có thể kiểm tra với hàm số f(x,y) $= \frac{x^2}{x^2$ + $y^2}$ ta có

i) $\lim_{(x,y)\to(0,0)} \frac{x^2}{x^2+y^2}$ không tồn tại.

ii) $\lim_{x\to 0} \lim_{y\to 0}$ f(x,y) $\frac{x^2}{x^2+y^2} =$ 1,

iii) $\lim_{y \to 0} \lim_{x \to 0} \frac{x^2}{x^2$ + $y^2} =$ 0.



$\S2$. ĐAO HÀM VÀ VI PHẦN

## 2.1 Đao hàm riêng <math>\S</math><b>2.</b> <b>Đ</b>AO HÀM VÀ VI PHẦN

• Cho hàm số f(x, y) xác định trong một miền D, điểm $M(x_0$, $y_0) \in$ D. Nếu cho y $= y_0$,

hàm số một biến số x $\mapsto$ f(x, $y_0)$ có đạo hàm tại điểm x $= x_0$ thì đạo hàm đó gọi là

đạo hàm riêng của f với biến x tại $M_0$ và được kí hiệu là $\frac{\partial f}{\partial x}$ hay $\frac{\partial}{\partial x}$ f(x, y).

$\frac{\partial f}{\partial x} = \lim_{\Delta$ x $\to 0} \frac{f(x_0$ + $\Delta$ x, $y_0)$ - $f(x_0$, $y_0)}{\Delta x}$

• Cho hàm số f(x, y) xác định trong một miền D, điểm $M(x_0$, $y_0) \in$ D. Nếu cho x $= x_0$,

hàm số một biến số x $\mapsto f(x_0$, y) có đạo hàm tại điểm y $= y_0$ thì đạo hàm đó gọi là

đạo hàm riêng của f với biến x tại $M_0$ và được kí hiệu là $\frac{\partial f}{\partial u}$ hay $\frac{\partial}{\partial u}$ f(x, y).

$\frac{\partial f}{\partial y} = \lim_{\triangle$ y $\to 0} \frac{f(x_0$, $y_0$ + $\triangle$ y) - $f(x_0$, $y_0)}{\triangle y}$

Chú ý: Các đạo hàm riêng của các hàm số n biến số (với n $\ge$ 3) được định nghĩa tương tự.

Khi cần tính đạo hàm riêng của hàm số theo biến số nào, xem như hàm số chỉ phụ thuộc

vào biến đó, còn các biến còn lại là các hằng số và áp dụng các quy tắc tính đạo hàm như

hàm số một biến số.

## 2.2 Vi phân toàn phần hàm số một biến số.

• Cho hàm số z $=$ f(x, y) xác định trong miền D. Lấy các điểm $M_0(x_0$, $y_0) \in$ D, $M(x_0$ +

$\Delta x_0$, $y_0$ + $\Delta y_0 \in$ D. Biểu thức $\Delta$ f $= f(x_0$ + $\Delta x_0$, $y_0$ + $\Delta y_0)$ - $f(x_0$, $y_0)(x_0$, $y_0)$ được

gọi là số gia toàn phần của f tại $M_0$. Nếu như có thể biểu diễn số gia toàn phần dưới

dạng

$\triangle$ f $=$ A. $\triangle$ x + B $\triangle$ y + $\alpha \triangle$ y + $\beta \triangle$ y

trong đó A, B là các hằng số chỉ phụ thuộc $x_0$, $y_0$ còn $\alpha$, $\beta \rightarrow$ 0 khi M $\rightarrow M_0$, thì ta nói

hàm số z khả vi tại $M_0$, còn biểu thức A. $\triangle$ x + B $\triangle$ y + $\alpha \triangle$ y được gọi là vi phân toàn

phần của z $=$ f(x, y) tại $M_0$ và được kí hiệu là dz.

Hàm số z $=$ f(x, y) được gọi là khả vi trên miền D nếu nó khả vi tại mọi điểm của

miền ấy.

• Đối với hàm số một biến số, sự tồn tại đạo hàm tại điểm $x_0$ tương đương với sự khả

vi của nó tại $x_0$. Đối với hàm số nhiều biến số, sự tồn tại của các đạo hàm riêng tại

$M_0(x_0$, $y_0)$ chưa đủ để nó khả vi tại $M_0$ (xem bài tập 3.4). Định lý sau đây cho ta điều

kiện đủ để hàm số z $=$ f(x, y) khả vi tại $M_0$.



Định lý 3.50. Nếu hàm số f(x,y) có các đạo hàm riêng trong lân cận của $M_0$ và nếu các

đạo hàm riêng đó liên tục tại $M_0$ thì f(x, y) khả vi tại $M_0$ và

dz $= f'_x \triangle$ x + $f'_y \triangle$ y

Ví du 2.1 (Cuối kì, K61 Viện ĐTQT). Sử dụng vi phân, tính gần đúng

b) $\sqrt{(6,05)^2$ + $(7,96)^2}$.

a) $\sqrt{(8,05)^2$ + $(5,96)^2}$.

## 2.3 Đao hàm của hàm số hợp a) <math>\sqrt{(8,05)^2 + (5,96)^2}</math>.

Cho D là một tập hợp trong $\mathbb{R}^2$ và các hàm số

D $\stackrel{\varphi}{\to} \varphi(D) \subset \mathbb{R}^2 \stackrel{f}{\to} \mathbb{R}$

và F $=$ f $\circ \varphi$ là hàm số hợp của hai hàm số f và $\varphi:$

F(x,y) $=$ f(u(x,y), v(x,y))

Định lý 3.51. Nếu f có các đạo hàm riêng $\frac{\partial f}{\partial x}$, $\frac{\partial f}{\partial y}$ liên tục trong $\varphi(D)$ và nếu u, v có các

đạo hàm riêng $\frac{\partial u}{\partial x}$, $\frac{\partial u}{\partial y}$, $\frac{\partial v}{\partial y}$, $\frac{\partial v}{\partial y}$ trong D thì tồn tại các đạo hàm riêng $\frac{\partial F}{\partial x}$, $\frac{\partial F}{\partial y}$ và

$ \n\begin{cases}\n\frac{\partial F}{\partial x} = \frac{\partial f}{\partial u} \frac{\partial u}{\partial x} + \frac{\partial f}{\partial v} \frac{\partial v}{\partial x} \\
\frac{\partial F}{\partial y} = \frac{\partial f}{\partial y} \frac{\partial u}{\partial y} + \frac{\partial f}{\partial z} \frac{\partial v}{\partial y}\n\end{cases}\n $

(3.1)

Công thức 3.1 có thể được viết dưới dạng ma trận như sau

$ \begin{pmatrix} \frac{\partial F}{\partial x} & \frac{\partial F}{\partial y} \end{pmatrix} = \begin{pmatrix} \frac{\partial f}{\partial u} & \frac{\partial f}{\partial v} \end{pmatrix} \begin{pmatrix} \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\ \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y} \end{pmatrix} $

trong đó ma trận

$ \begin{pmatrix} \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\ \frac{\partial v}{\partial y} & \frac{\partial v}{\partial z} \end{pmatrix} $

được gọi là ma trận Jacobi của ánh xạ $\varphi$, định thức của ma trận ấy được gọi là định thức

Jacobi của u, v với x, y và được kí hiệu là $\frac{D(u,v)}{D(x-u)}$.



## 2.4 Đạo hàm và vi phân cấp cao None

• Cho hàm số hai biến số z $=$ f(x, y). Các đạo hàm riêng $f'_x$, $f'_y$ là những đạo hàm riêng

cấp một. Các đạo hàm riêng của các đạo hàm riêng cấp một nếu tồn tai được gọi là

những đạo hàm riêng cấp hai. Có bốn đạo hàm riêng cấp hai được kí hiệu như sau:

$ \n\begin{cases}\n(f'_x)'_x = f''_{xx} = \frac{\partial}{\partial x} \left( \frac{\partial f}{\partial x} \right) = \frac{\partial^2 f}{\partial x^2} \\
(f'_x)'_y = f''_{xy} = \frac{\partial}{\partial y} \left( \frac{\partial f}{\partial x} \right) = \frac{\partial^2 f}{\partial y \partial x} \\
(f'_y)'_x = f''_{yx} = \frac{\partial}{\partial x} \left( \frac{\partial f}{\partial y} \right) = \frac{\partial^2 f}{\partial x \partial y} \\
(f'_y)'_y = f''_{yy} = \frac{\partial}{\partial y} \left( \frac{\partial f}{\partial y} \right) = \frac{\partial^2 f}{\partial $

Các đạo hàm riêng của các đạo hàm riêng cấp hai, nếu tồn tại, được gọi là các đạo

hàm riêng cấp ba, ...

Định lý 3.52 (Schwarz). Nếu trong một lân cận U nào đó của điểm $M_0(x_0$, $y_0)$ hàm

$s\hat{o}$ z $=$ f(x,y) có các đạo hàm riêng $f''_{xy}$, $f''_{yx}$ và nếu các đạo hàm riêng ấy liên tục tại

$M_0$ thì $f''_{xy} = f''_{yx}$ tại $M_0$.

• Xét hàm số z $=$ f(x, y), vi phân toàn phần của nó dz $= f'_x$ dx + $f'_y$ dy, nếu tồn tại, cũng

là một hàm số với hai biến số x, y. Vi phân toàn phần của dz, nếu tồn tại, được gọi là

vi phân toàn phần cấp hai của z và được kí hiệu là $d^2z$. Ta có công thức

$d^{2}z = f''_{xx}dx^{2}$ + $2f''_{xy}dxdy$ + $f''_{yy}dy^{2}$

Ví dụ 2.2 (Cuối kì, K62, GT2, Nhóm ngành 2). Cho hàm số z $=$ z(x, y) có các đạo hàm

$ riêng cấp một liên tục, ở đó \begin{cases} x = r \cos \varphi, \\ y = r \sin \varphi. \end{cases} $

Chứng minh rằng

$\left(\frac{\partial z}{\partial x}\right)^2$ + $\left(\frac{\partial z}{\partial y}\right)^2 = \left(\frac{\partial z}{\partial r}\right)^2$ + $\frac{1}{r^2}\left(\frac{\partial z}{\partial \varphi}\right)^2$.

## 2.5 Đao hàm theo hướng - Gradient <math display="block">\left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2 = \left(\frac{\partial z}{\partial r}\right)^2 + \frac{1}{r^2}\left(\frac{\partial z}{\partial \varphi}\right)^2.</math>

Định nghĩa 3.34. Cho f(x,y,z) là một hàm số xác định trong một miền D $\in \mathbb{R}^3$ và $\vec{l} =$

$(l_1$, $l_2$, $l_3)$ là một vécto đơn vị bất kì trong $\mathbb{R}^3$. Giới hạn, nếu có,

$\n\lim_{t\to 0}\frac{f(M_0+t\vec{l})-f(M)}{t}\n$

(3.2)



được gọi là đạo hàm của hàm số f theo hướng $\vec{l}$ tại $M_0$ và được kí hiệu là $\frac{\partial f}{\partial \vec{l}}(M_0)$.

• Nếu $\vec{l}$ không phải là véc tơ đơn vị thì giới hạn trong công thức 3.2 có thể được thay

bằng

$\lim_{t\to 0}\frac{u(x_0+t\cos\alpha,y_0+t\cos\beta,z_0+t\cos\gamma)-u(x_0,y_0,z_0)}{t}$,

trong đó cos $\alpha$, cos $\beta$, cos $\gamma$ là các cosin chỉ phương của $\vec{l}$.

• Nếu $\vec{l}$ trùng với véctơ đơn vị i của trục Ox thì đạo hàm theo hướng $\vec{l}$ chính là đạo hàm

riêng theo biến x của hàm f

$\frac{\partial f}{\partial \vec{l}}(M_0) = \frac{\partial f}{\partial x}(M_0)$

• Vậy đạo hàm riêng theo biến x chính là đạo hàm theo hướng của trục Ox, cũng như

vậy, $\frac{\partial f}{\partial y}$, $\frac{\partial f}{\partial z}$ là các đạo hàm của f theo hướng của trục Oy và Oz. Định lý sau đây cho

ta mối liên hệ giữa đạo hàm theo hướng và đạo hàm riêng:

Định lý 3.53. Nếu hàm số f(x,y,z) khả vi tại điểm $M_0(x_0,y_0,z_0)$ thì tại $M_0$ có đạo hàm

theo mọi hướng $\vec{l}$ và ta có

$\frac{\partial f}{\partial \vec{l}}(M_0) = \frac{\partial f}{\partial \tau}(M_0) \cos \alpha$ + $\frac{\partial f}{\partial \mu}(M_0) \cos \beta$ + $\frac{\partial f}{\partial \tau}(M_0) \cos \gamma$

trong đó (cos $\alpha$, cos $\beta$, cos $\gamma)$ là cosin chỉ phương của $\vec{l}$.

Cho f(x, y, z) là hàm số có các đạo hàm riêng tại $M_0(x_0$, $y_0$, $z_0)$. Người ta gọi gradient của

f tại $M_0$ là véctơ

$\left(\frac{\partial f}{\partial x}(M_0)$, $\frac{\partial f}{\partial y}(M_0)$, $\frac{\partial f}{\partial z}(M_0)\right)$

và được kí hiệu là $\overrightarrow{\text{grad}} f(M_0)$.

Định lý 3.54. Nếu $\overrightarrow{l}$ là một véctơ đơn vị và hàm số f(x,y,z) khả vi tại $M_0$ thì tại đó ta có

$\frac{\partial f}{\partial \vec{l}}(M_0) = \overrightarrow{\text{grad}} f.\vec{l}$

Chú ý: $\frac{\partial f}{\partial \vec{l}}(M_0)$ thể hiện tốc độ biến thiên của hàm số f tại $M_0$ theo hướng $\vec{l}$. Từ công

thức $\frac{\partial f}{\partial \vec{l}}(M_0) = \overrightarrow{\text{grad}} f.\vec{l} = |\overrightarrow{\text{grad}}$ f| $|\vec{l}| \cdot \cos(\overrightarrow{\text{grad}} f.\vec{l})$ ta có $|\frac{\partial f}{\partial \vec{l}}(M_0)|$ đạt giá trị lớn nhất

bằng $|\overrightarrow{\text{grad}}$ f| $|\vec{l}|$ nếu $\vec{l}$ có cùng phương với $\overrightarrow{\text{grad } f}$. Cụ thể

• Theo hướng $\vec{l}$, hàm số f tăng nhanh nhất tại $M_0$ nếu $\vec{l}$ có cùng phương, cùng hướng

với grad $\hat{f}$.

• Theo hướng $\vec{l}$, hàm số f giảm nhanh nhất tại $M_0$ nếu $\vec{l}$ có cùng phương, ngược hướng

với grad $\hat{f}$.



## 2.6 Hàm ẩn - Đạo hàm của hàm số ẩn None

• Cho phương trình F(x, y) $=$ 0 trong đó F : U $\to \mathbb{R}$ là một hàm số có các đạo hàm

riêng liên tục trên tập mở U $\subset \mathbb{R}^2$ và $F'_y(x_0$, $y_0) \neq$ 0. Khi đó phương trình F(x, y) $=$ 0

xác định một hàm số ẩn y $=$ y(x) trong một lân cận nào đó của $x_0$ và có đạo hàm

y'(x) $= -\frac{F'_x}{F'_y}$

• Tương tự, cho phương trình F(x,y,z) $=$ 0 trong đó F : U $\to \mathbb{R}$ là một hàm số có các

đạo hàm riêng liên tục trên tập mở U $\subset \mathbb{R}^3$ và $F'_z(x_0$, $y_0$, $z_0) \neq$ 0. Khi đó phương trình

F(x, y, z) $=$ 0 xác định một hàm số ẩn z $=$ z(x, y) trong một lân cận nào đó của $(x_0$, $y_0)$

và có đạo hàm

$z'_x=-\frac{F'_x}{F'_z}$, $z'_y=-\frac{F'_y}{F'}$

## 2.7 Bài tập <math display="block">z'_x=-\frac{F'_x}{F'_z}, z'_y=-\frac{F'_y}{F'}</math>

Bài tập 3.4. Chứng minh rằng hàm số

$ f(x,y) = \begin{cases} \frac{xy}{x^2 + y^2} & \text{n\'{e}u } (x,y) \neq (0,0) \\ 0 & \text{n\'{e}u } (x,y) = (0,0) \end{cases} $

có các đạo hàm riêng tại (0,0) nhưng không liên tục tại (0,0) và do đó không khả vi tại

(0,0).

Bài tập 3.5. Tính các đạo hàm riêng của hàm số sau

a) z $= \ln$ (x + $\sqrt{x^2$ + $y^2})$ c) z $= x^{y^3}$

e) u $= x^{y^z}$, (x, y, z $>$ 0)

d) z $= \arctan \sqrt{\frac{x^2$ - $y^2}{x^2$ + $y^2}}f)$ u $= e^{\frac{1}{x^2$ + $y^2$ + $z^2}}$, (x, y, z $>$ 0)

b) z $= y^2 \sin \frac{x}{y}$

$Ch\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n$

$z'_x = \frac{1$ + $\frac{x}{\sqrt{x^2$ + $y^2}}}{x$ + $\sqrt{x^2$ + $y^2}} = \frac{1}{\sqrt{x^2$ + $y^2}}; z'_y = \frac{\frac{y}{\sqrt{x^2$ + $y^2}}}{x$ + $\sqrt{x^2$ + $y^2}}$

b)

$z'_x =$ y $\cos \frac{x}{y}; z'_y =$ 2y $\sin \frac{x}{y}$ - x $\cos \frac{x}{y}$.



$\mathbf{c})$

$z'_x = y^3 x^{y^3-1}; z'_y = 3y^2 \ln$ x $\cdot x^{y^3}$

d)

$z'_x = \frac{1}{\frac{x^2$ - $y^2}{2$ + $2}$ + $1} \frac{\partial}{\partial x} \left( \sqrt{\frac{x^2$ - $y^2}{x^2$ + $y^2}} \right) = \frac{y^2}{x \sqrt{x^4$ - $y^4}}$

$z'_y = \frac{1}{\frac{x^2$ - $y^2}{x^2$ + $1} \frac{\partial}{\partial y}} \left( \sqrt{\frac{x^2$ - $y^2}{x^2$ + $y^2}} \right) = \frac{-y}{\sqrt{x^4$ - $y^4}}$

e)

$u'_x = y^z x^{y^z-1}; u'_y = x^{y^z}$ z $y^{z-1} \cdot \ln$ x; $u'_z = x^{y^z} y^z \ln$ y $\ln$ x

f)

$u'_{x} = e^{\frac{1}{x^{2}+y^{2}+z^{2}}} \cdot \frac{-2x}{(x^{2}+u^{2}+z^{2})^{2}}; u'_{y} = e^{\frac{1}{x^{2}+y^{2}+z^{2}}} \frac{-2y}{(x^{2}+u^{2}+z^{2})^{2}}; u'_{z} = e^{\frac{1}{x^{2}+y^{2}+z^{2}}} \frac{-2z}{(x^{2}+u^{2}+z^{2})^{2}}$.

Bài tập 3.6. Khảo sát sự liên tục và sự tồn tại, liên tục của các đạo hàm riêng của các

hàm số f(x, y) sau

$ a) f(x,y) = \begin{cases} x \arctan\left(\frac{y}{x}\right)^2 & \text{n\'{e}u } x \neq 0 \\ 0 & \text{n\'{e}u } x = 0 \end{cases} $

$ b) f(x,y) = \begin{cases} \frac{x \sin y - y \sin x}{x^2 + y^2} & \text{n\'{e}u } (x,y) \neq (0,0) \\ 0 & \text{n\'{e}u } (x,y) = (0,0). \end{cases} $

Chứng minh. a) Dễ thấy hàm số liên tục với mọi (x, y) $\neq$ (0, y).Xét x $=$ 0, vì $\left|$ x $\arctan \left( \frac{y}{x} \right)^2 \right| \leq \frac{\pi}{2}$ |x| nên $\lim_{x \to 0}$ x arctan $\left( \frac{y}{x} \right)^2 =$ 0 $=$ f(0, y). Vậy f(x, y)

liên tục trên $\mathbb{R}^2$.

Với x $\neq$ 0 các đạo hàm riêng tồn tại và liên tục:

$z'_x = \arctan\left(\frac{y}{x}\right)^2$ - $\frac{2x^2y^2}{x^4$ + $1t^4}$, $z'_y = \frac{2x^3y}{x^4$ + $1t^4}$

Xét tai x $=$ 0,

$ \begin{cases} f'_x(0,y) = \lim_{h \to 0} \frac{f(h,y) - f(0,y)}{h} = \arctan\left(\frac{h}{y}\right)^2 = \begin{bmatrix} 0, y = 0\\ \frac{\pi}{2}, y \neq 0 \end{bmatrix} \\ f'_y(0,y) = \lim_{k \to 0} \frac{f(0, y + k) - f(0, y)}{k} = \lim_{k \to 0} 0 = 0 \end{cases} $

Vậy ta thấy $f'_x(x$, y) liên tục trên $\mathbb{R}^2 \setminus$ (0, 0); $f'_y(x$, y) liên tục trên $\mathbb{R}^2$.



b) Hàm số liên tục trên $\mathbb{R}^2 \setminus$ (0,0), còn tại (0,0) thì

0 $\le \left| \frac{x \sin$ y - y $\sin x}{x^2$ + $y^2} \right| = \left| \frac{xy}{x^2$ + $y^2} \left( \frac{\sin y}{y}$ - $\frac{\sin x}{x} \right) \right| \le \frac{1}{2} \left| \frac{\sin y}{y}$ - $\frac{\sin x}{x} \right|$

nên

$\n\lim_{\substack{x \to$ 0 $\\$ y $\to 0}} \left| \frac{x \sin$ y - y $\sin x}{x^2$ + $y^2} \right| = 0\n$

Vậy f(x, y) liên tục trên $\mathbb{R}^2$.

$\mathbf{r}$

Bài tập 3.7. Giả sử z $=$ yf $(x^2$ - $y^2)$, ở đó f là hàm số khả vi. Chứng minh rằng đối với

hàm số z hệ thức sau luôn thoả mãn

$\frac{1}{x}z'_x$ + $\frac{1}{u}z'_y = \frac{z}{u^2}$

Chúng minh. Ta có

$z'_x = yf(x^2$ - $y^2) \cdot$ 2x, $z'_y = f(x^2$ - $y^2)$ + y $\cdot f(x^2$ - $y^2) \cdot$ (-2y)

$n\hat{e}n$

$\frac{1}{x}z'_x$ + $\frac{1}{1}z'_y = \frac{f(x^2$ - $y^2)}{1} = \frac{z}{1^2}$

$\blacksquare$

Bài tập 3.8. Tìm đao hàm của hàm số hợp sau đây

a) z $= e^{u^2$ - $2v^2}$, u $= \cos$ x, v $= \sqrt{x^2$ + $y^2}$.

b) z $= \ln (u^2$ + $v^2)$, u $=$ xy, v $= \frac{x}{y}$.

c) z $= \arcsin(x$ - y), x $=$ 3t, y $= 4t^3$.

Chứng minh.

a) Ta có

$ \begin{cases} u'_x = -\sin x \\ u'_y = 0 \end{cases} ; \begin{cases} v'_x = \frac{x}{\sqrt{x^2 + y^2}} \\ v'_y = \frac{y}{\sqrt{x^2 + y^2}} \end{cases} ; $

nên

$ \begin{cases} z'_x = e^{\cos x^2 - 2(x^2 + y^2)} [-\sin 2x - 4x]. \\ z'_y = e^{\cos x^2 - 2(x^2 + y^2)} [-4y]. \end{cases} $

b) Ta có

$ \begin{cases} u'_x = y \\ u'_y = x \end{cases} ; \begin{cases} v'_x = \frac{1}{y} \\ v'_y = \frac{-x}{y^2} \end{cases} $

nên

$z'_x = \frac{2}{x}$, $z'_y = \frac{2(y^4-1)}{y(y^4+1)}$



c) Ta có

$ \n\begin{cases}\n  x'_t = 3 \\
  y'_t = 12t^2\n\end{cases}\n $

nên

$z'_{t} = \frac{1}{\sqrt{1$ - (x - $y)^{2}}} \left(3$ - $12t^{2}\right)$

$\blacksquare$

Bài tập 3.9. Tìm vi phân toàn phần của các hàm số

a) z $= \sin(x^2$ + $y^2)$

c) z $= \arctan \frac{x+y}{x-y}$

d) u $= x^{y^2 z}$

b) z $= \ln \tan \frac{y}{r}$

Chứng minh.

a

dz $= \cos\left(x^2$ + $y^2\right)(2xdx$ + 2ydy)

$\mathbf{b})$

dz $= \frac{2}{\sin \frac{2y}{x}} \cdot \left( \frac{x$ dy - y $dx}{x^2} \right)$.

$\mathbf{c})$

dz $= \frac{(x$ - y) dx + (x + y) $dy}{(x$ - $y)^2$ + (x + $y)^2}$.

d)

du $= x^{y^2 z} \left( \frac{y^2 z}{x}$ dx + 2yz $\ln$ x dy + $y^2 \ln$ x dz $\right)$.

$\blacksquare$

Bài tập 3.10. Tính gần đúng

b) B $= \ln(\sqrt[3]{1.03}$ + $\sqrt[4]{0.98}$ - 1)

a) A $= \sqrt[3]{(1,02)^2$ + $(0,05)^2}$

Chứng minh. a) Xét hàm f(x, y) $= \sqrt[3]{x^2$ + $y^2}$, $\Delta$ x $=$ 0.02; $\Delta$ y $=$ 0.05; x $=$ 1; y $=$ 0. Ta có

$f'_x = \frac{1}{3(x^2$ + $y^2)^{2/3}}$ 2x; $f'_y = \frac{1}{3(x^2$ + $y^2)^{2/3}}$ 2y

Khi đó

f(1 + $\Delta$ x, 0 + $\Delta$ y) $\approx$ f(1,0) + $f'_x(1,0) \Delta$ x + $f'_y(1,0) \Delta$ y $=$ 1 + $\frac{2}{3} \cdot$ 0,02 + 0.0,05 $=$ 1,013.



b) Xét hàm

f(x, y) $= \ln(\sqrt[3]{x}$ + $\sqrt[4]{y}$ - 1); x $=$ 1; y $=$ 1; $\Delta$ x $=$ 0, 03; $\Delta$ y $=$ 0, 02

Ta có

$f'_x = \frac{1}{\sqrt[3]{x}$ + $\sqrt[4]{y}$ - $1} \cdot \frac{1}{3\gamma^{\frac{2}{3}}}; f'_y = \frac{1}{\sqrt[3]{x}$ + $\sqrt[4]{y}$ - $1} \cdot \frac{1}{3y^{\frac{3}{4}}}$

Khi đó

f(1 + $\Delta$ x, 1 + $\Delta$ y) $\approx$ f(1, 1) + $f'_x(1$, 1) $\Delta$ x + $f'_y(1$, 1) $\Delta$ y

$\mathbf{r} \in \mathbb{R}^{n \times n}$

$=$ 0 + $\frac{1}{3} \cdot$ 0.03 + $\frac{1}{4}$ (-0.02) $=$ 0.005.

Bài tập 3.11. Tìm đạo hàm của các hàm số ẩn xác định bởi các phương trình sau

a) $x^3y$ - $y^3x = a^4;$ tính y'

c) x + y + z $= e^z;$ tính $z'_x$, $z'_y$

b) arctan $\frac{x+y}{a} = \frac{y}{a};$ tinh y'

d) $x^3$ + $y^3$ + $z^3$ - 3xyz $=$ 0, tinh $z'_x$, $z'_y$

a) Xét hàm số ẩn F(x, y) $= x^3y$ - $y^3x$ - $a^4 =$ 0, có $F'_x = 3x^2y$ - $y^3; F'_y =$

Chứng minh.

$x^3$ - $3y^2x$. Vây

y' $= \frac{-F'_x}{F'_x} = -\frac{3x^2y$ - $y^3}{x^3$ - $3y^2x}$

$ b) Xét hàm số ẩn F(x, y) = \arctan \frac{x+y}{a} - \frac{y}{a} có \begin{cases} F'_x = \frac{\frac{1}{a}}{1 + (\frac{x+y}{a})^2} = \frac{a}{a^2 + (x+y)^2} \\ F'_y = \frac{a}{a^2 + (x+y)^2} - \frac{1}{a} = \frac{a^2 - a^2 - (x+y)^2}{a(a^2 + (x+y)^2)} \end{cases}nên $

y' $= \frac{u}{(x$ + $u)^2}$.

c) Xét hàm số ẩn F(x, y, z) $=$ x + y + z - $e^z$ có $F'_x =$ 1; $F'_y =$ 1; $F'_z =$ 1 - $e^z$ nên

$z'_x = \frac{-1}{1-z^z}; z'_y = \frac{-1}{1-z^z}$

d) Xét hàm số ẩn F(x, y) $= x^3$ + $y^3$ + $z^3$ - 3xyz $=$ 0 có $F'_x = 3x^2$ - 3yz; $F'_y = 3y^2$ - 3xz; $F'_z =$

$3z^2$ - 3xy nên

$z'_x = \frac{3yz$ - $3x^2}{3z^2$ - $3xy}; z'_x = \frac{3xz$ - $3y^2}{3z^2$ - $3xy}$



Bài tập 3.12. Cho u $= \frac{x+z}{y+z}$, tính $u'_x$, $u'_y$ biết rằng z là hàm số ẩn của x, y xác định bởi

phương trình $z.e^z = x.e^x$ + $y.e^y$



$ Chứng minh. Xét hàm số F(x, y, z) = ze^{z} - xe^{x} - ye^{y} = 0 có \begin{cases} F'_{x} = -(e^{x} + xe^{x}) \\ F'_{y} = -(e^{y} + ye^{y}) \\ F'_{z} = e^{z} + ze^{z} \end{cases} nên $

$ \n\begin{cases}\n u'_{x} = \frac{(1 + z'_{x}) \cdot (y + z) - (x + z) (z'_{x})}{(y + z)^{2}} = \frac{\left(1 + \frac{e^{x} + xe^{x}}{e^{z} + ze^{z}}\right) - (x + z) \frac{e^{x} + xe^{x}}{e^{z} + ze^{z}}}{(y + z)^{2}} \\
 u'_{y} = \frac{(x + z) \cdot (1 + z'_{y}) - (y + z) (z'_{y})}{(y + z)^{2}} = \frac{(x + z) \cdot \left(1 + \frac{e^{y} + ye^{y}}{e^{z} + ze^{z}}\right) - (y + z) \left(\frac{e^{y $

$\qquad \qquad \blacksquare$

Bài tập 3.13. Tìm đạo hàm của các hàm số ẩn y(x), z(x) xác định bởi hệ

$ \begin{cases} x + y + z = 0 \\ x^2 + y^2 + z^2 = 1 \end{cases} $

Chứng minh. Lấy đạo hàm hai về của các phương trình của hệ ta có

$ \n\begin{cases}\n1 + y'_x + z'_x = 0 \\
2x + 2yy'_x + 2zz'_x = 0\n\end{cases}\n $

$n\hat{e}n$

$ \n\begin{cases}\ny'_x = \frac{z - x}{y - z} \\
z'_x = \frac{x - y}{y - z}\n\end{cases}\n $

$\blacksquare$

Bài tập 3.14. Phương trình $z^2$ + $\frac{2}{x} = \sqrt{y^2$ - $z^2}$, xác định hàm ẩn z $=$ z(x, y). Chứng minh

$\mathring{\text{rand}} x^2 z'_x$ + $\frac{1}{y} z'_y = \frac{1}{z}$

$ \text{ing } x \leq_{x} y \leq_{z}Chứng minh. Xét hàm số F(x, y, z) = z^{2} + \frac{2}{x} - \sqrt{y^{2} - z^{2}} có \begin{cases} F'_{x} = -\frac{2}{x^{2}} \\ F'_{y} = \frac{-y}{\sqrt{y^{2} - z^{2}}} \\ F'_{z} = 2z + \frac{z}{\sqrt{y^{2} - z^{2}}} \end{cases}nên $

$z'_x = \frac{\frac{z}{x^2}}{2z$ + $\frac{z}{\sqrt{y^2$ - $z^2}}}$

$\int z'_y = \frac{\sqrt{y^2$ - $z^2}}{2z$ + $\frac{z}{\sqrt{y^2$ - $z^2}}}$

Từ đó suy ra $x^2z'_x$ + $\frac{z'_y}{y} = \frac{1}{z}$.

$\qquad \qquad \blacksquare$

Bài tập 3.15. Tính các đạo hàm riêng cấp hai của các hàm số sau



b) z $= x^2 \ln (x^2$ + $y^2)$ c) z $= \arctan \frac{y}{x}$

a) z $= \frac{1}{3} \sqrt{(x^2$ + $y^2)^3}$

Chứng minh.

a) Ta có

$ \begin{cases}\nz'_{x} = x\sqrt{x^{2} + y^{2}} \\
z'_{y} = y\sqrt{x^{2} + y^{2}}\n\end{cases} \Rightarrow \begin{cases}\nz''_{xx} = \sqrt{x^{2} + y^{2}} + x\frac{2x}{2\sqrt{x^{2} + y^{2}}} = \frac{2x^{2} + y^{2}}{\sqrt{x^{2} + y^{2}}} \\
z''_{yy} = \sqrt{x^{2} + y^{2}} + y\frac{2y}{2\sqrt{x^{2} + y^{2}}} = \frac{x^{2} + 2y^{2}}{\sqrt{x^{2} + y^{2}}} \\
z''_{xy} = \frac{2xy}{2\sqrt{x^{2} + y^{2}}} = \frac{xy}{\sqrt{x^{2} + y $

b) Ta có

$ \begin{cases}\nz'_{x} = 2x \ln (x + y) + \frac{x^{2}}{x + y} \\
z'_{y} = \frac{x^{2}}{x + y}\n\end{cases} \Rightarrow \begin{cases}\nz''_{xx} = 2 \ln (x + y) + \frac{2x}{x + y} + \frac{2x (x + y) - x^{2}}{(x + y)^{2}} \\
z''_{xy} = \frac{2x}{x + y} + \frac{-x^{2}}{(x + y)^{2}}\n\end{cases} $

$z_{yy} = \frac{1}{(x+y)^2}$

c) Ta có

$ \begin{cases}\nz'_x = \frac{1}{1 + \left(\frac{y}{x}\right)^2} \cdot \frac{-y}{x^2} = \frac{-y}{x^2 + y^2} \\
z'_y = \frac{1}{1 + \left(\frac{y}{x}\right)^2} \cdot \frac{1}{x} = \frac{x}{x^2 + y^2}\n\end{cases} \Rightarrow \begin{cases}\nz''_{xx} = \frac{2xy}{(x^2 + y^2)^2} \\
z''_{xy} = \frac{-(x^2 + y^2) + y \cdot 2y}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2} \\
z''_{yy} = \frac{-2xy}{(x^2 + y^2)^ $

Bài tập 3.16. Tính vi phân cấp hai của các hàm số sau

a) z $= xy^2$ - $x^2y$

b) z $= \frac{1}{2(x^2$ + $y^2)}$

Chứng minh. a) Ta có dz $= (y^2$ - 2xy) dx + (2xy - $x^2)$ dy nên

$d^{2}z =$ -2y $(dx)^{2}$ + 4 (y - x) dxdy + (2y) $(dy)^{2}$

b) Ta có dz $= \frac{x}{2(x^2+y^2)^2}dx$ + $\frac{y}{2(x^2+y^2)^2}dy$ nên

$d^{2}z = \frac{y^{2}$ - $3x^{2}}{(x^{2}$ + $y^{2})^{3}} (dx)^{2}$ - $\frac{4xy}{(x^{2}$ + $y^{2})^{3}}$ dxdy + $\frac{x^{2}$ - $3y^{2}}{(x^{2}$ + $y^{2})^{3}} (dy)^{2}$



§3. CỤC TRỊ CỦA HÀM SỐ NHIỀU BIẾN SỐ

## 3.1 Cuc tri tu do §3. CỤC TRỊ CỦA HÀM SỐ NHIỀU BIẾN SỐ

Định nghĩa 3.35. Cho hàm số z $=$ f(x, y) xác định trong một miền D và $M_0(x_0$, $y_0) \in$ D.

Ts nói rằng hàm số f(x, y) đạt cực trị tại $M_0$ nếu với mọi điểm M trong lân cận nào đó của

$M_0$ nhưng khác $M_0$, hiệu số f(M) - $f(M_0)$ có dấu không đổi.

• Nếu f(M) - $f(M_0) >$ 0 trong một lân cận nào đó của $M_0$ thì $M_0$ được gọi là cực tiểu

của hàm số f tai $M_0$.

• Nếu f(M) - $f(M_0) <$ 0 trong một lân cận nào đó của $M_0$ thì $M_0$ được gọi là cực đại

của hàm số f tại $M_0$.

Trong phần tiếp theo chúng ta sử dụng các kí hiệu sau:

p $= f'_x(M)$, q $= f_y(M)$, r $= f_{xx}"(M)$, s $= f_{xy}"(M)$, t $= f_{yy}"(M)$

Định lý 3.55. Nếu hàm số f(x,y) đạt cực trị tại M và tại đó các đạo hàm riêng p $=$

$f'_x(M)$, q $= f_y(M)$ tồn tại thì các đạo hàm riêng ấy bằng không.

Định lý 3.56. Giả sử hàm số z $=$ f(x, y) có các đạo hàm riêng đến cấp hai liên tục trong

một lân cận nào đó của $M_0(x_0$, $y_0)$. Giả sử tại $M_0$ ta có p $=$ q $=$ 0, khi đó

1. Nếu $s^2$ - rt $<$ 0 thì f(x, y) đạt cực trị tại $M_0$. Đó là cực tiểu nếu r $>$ 0, là cực đại nếu

r $<$ 0.

2. Nếu $s^2$ - rt $>$ 0 thì f(x, y) không đạt cực trị tại $M_0$.

Chú ý: Nếu $s^2$ - rt $=$ 0 thì chưa kết luận được điều gì về điểm $M_0$, nó có thể là cực trị,

cũng có thể không. Trong trường hợp đó ta sẽ dùng định nghĩa để xét xem $M_0$ có phải là

cực trị hay không bằng cách xét hiệu f(M) - $f(M_0)$, nếu nó xác định dấu trong một lân

cận nào đó của $M_0$ thì nó là cực trị và ngược lai.

Ví dụ 3.1 (Cuối kì, K61 Viện ĐTQT). Tìm các cực trị của hàm số

a) z $= x^2$ - 2x + $\arctan(y^2)$.

b) z $= y^2$ - 2y + $\arctan(x^2)$.

Bài tập 3.17. Tìm cực trị của các hàm số sau



c) z $= 2x^4$ + $y^4$ - $x^2$ - $2y^2$

a) z $= x^2$ + xy + $y^2$ + x - y + 1

d) z $= x^2$ + $y^2$ - $e^{-(x^2+y^2)}$

b) z $=$ x + y - $x.e^y$

$ Chúng minh. a) Xét hệ phương trình \begin{cases} p = z'_x = 2x + y + 1 = 0 \\ q = z'_y = x + 2y - 1 = 0 \end{cases} \Leftrightarrow \begin{cases} x = -1 \\ y = 1 \end{cases}. Vậy $

ta có M(-1,1) là điểm tới hạn duy nhất.

Ta có A $= z''_{xx}(M) =$ 2; B $= z''_{xy}(M) =$ 1; C $= z''_{yy}(M) =$ 2 nên $B^2$ - AC $=$ 1 - 4 $=$ -3 $<$

0. Vậy hàm số đạt cực trị tại M và do A $>$ 0 nên M là điểm cực tiểu.

b) Xét hê phương trình

$ \begin{cases} p = 1 - e^y = 0 \\ q = 1 - xe^y = 0 \end{cases} \Leftrightarrow \begin{cases} x = 1 \\ y = 0 \end{cases} $

Vậy hàm số có điểm tới hạn duy nhất M(1,0). Ta có A $= z''_{xx}(M) =$ 0; B $= z''_{xy}(M) =$ 0

z $=$ 1; C $= z''_{yy}(M) =$ -1 nên $B^2$ - AC $=$ 1 $>$ 0. Hàm số đã cho không có cực trị.

c) Xét hệ phương trình

$ \begin{cases}\nz'_{x} = 8x^{3} - 2x \\
z'_{y} = 4y^{3} - 4y\n\end{cases} \Leftrightarrow \begin{cases}\nx (4x^{2} - 1) = 0 \\
y (y^{2} - 1) = 0\n\end{cases} \Leftrightarrow \begin{cases}\nx = 0 \lor x = \frac{1}{2} \lor x = -\frac{1}{2} \\
y = 0 \lor y = 1 \lor y = -1\n\end{cases} $

Vậy các điểm tới hạn của hàm số là

$M_1(0,0); M_2(0,1); M_3(0,-1); M_4(\frac{1}{2},0); M_5(\frac{1}{2},1)$

$M_6\left(\frac{1}{2},-1\right); M_7\left(-\frac{1}{2},0\right); M_8\left(-\frac{1}{2},1\right); M_9\left(-\frac{1}{2},-1\right);$

Ta có $z''_{xx} = 24x^2$ - 2; $z''_{xy} =$ 0; $z''_{yy} = 12y^2$ - 4.

• Tai $M_1(0,0)$, A $=$ -2; B $=$ 0; C $=$ -4; $B^2$ - AC $=$ -8 $<$ 0 nên $M_1$ là điểm cực đại

với z $=$ 0.

• Tai $M_2(0,1); M_3(0,-1);$ A $=$ -2; B $=$ 0; C $=$ 8; $B^2$ - AC $=$ 16 $>$ 0 nên $M_2$, $M_3$

không phải là điểm cực đại với z $=$ 0.

• Tại $M_4\left(\frac{1}{2},0\right); M_7\left(\frac{-1}{2},0\right);$ A $=$ 4; B $=$ 0; C $=$ -4; $B^2$ - AC $=$ 16 $>$ 0 nên $M_4$, $M_7$

không phải là điểm cực đại với z $=$ 0.

• Tại $M_5\left(\frac{1}{2},1\right); M_6\left(\frac{1}{2},-1\right); M_8\left(-\frac{1}{2},1\right); M_9\left(-\frac{1}{2},-1\right);$ A $=$ 4; B $=$ 0; C $=$ 8; $B^2$ -

AC $=$ -32 $<$ 0 nên $M_5$, $M_6$, $M_8$, $M_9$ là các điểm cực tiểu với giá trị tại đó là

$z=-\frac{9}{8}$.

$ d) Xét hệ phương trình \begin{cases} p = z'_x = 2x + e^{-(x^2 + y^2)} . 2x = 0 \\ q = z'_y = 2y + e^{-(x^2 + y^2)} . 2y = 0 \end{cases} \Leftrightarrow \begin{cases} x = 0 \\ y = 0 \end{cases} $



Vậy M(0,0) là điểm tới hạn duy nhất. Xét

$z_{xx}'' =$ 2 + 2 $\cdot e^{-(x^2$ + $y^2)}$ - $4x^2 \cdot e^{-(x^2$ + $y^2)}$

$z''_{xy} =$ -4xy $\cdot e^{-(x^2+y^2)}$

$z''_{yy} =$ 2 + 2 $\cdot e^{-(x^2$ + $y^2)}$ - $4y^2 \cdot e^{-(x^2$ + $y^2)}$

Tại M(0,0) có A $=$ 4; B $=$ 0; C $=$ 4; $B^2$ - AC $=$ -16 $<$ 0; A $>$ 0 nên tại M hàm số đạt

cực tiểu.

$\blacksquare$

## 3.2 Cực trị có điều kiên <math display="block">\blacksquare</math>

Cho tập mở U $\subset \mathbb{R}^2$ và hàm số f: U $\to \mathbb{R}$. Xét bài toán tìm cực trị của hàm số f(x, y)

khi các biến x, y thoả mãn phương trình

$\varphi(x,y)=0$

Ta nói rằng tại điểm $(x_0$, $y_0) \in$ U thoả mãn điều kiện $\varphi(x_0$, $y_0) =$ 0 hàm f có cực đại tương

$\hat{d}\delta$ i (tương ứng cực tiểu tương $\hat{d}\delta$ i) nếu tồn tại một lân cận V $\subset$ U sao cho f(x, y) $\leq f(x_0$, $y_0)$

(tương ứng f(x, y) $\ge f(x_0$, $y_0))$ với mọi (x, y) $\in$ V thoả mãn điều kiện $\varphi(x$, y) $=$ 0. Điểm

$(x_0$, $y_0)$ được gọi là cực trị có điều kiện của hàm số f(x, y), còn điều kiện $\varphi(x$, y) $=$ 0 được

gọi là điều kiện ràng buộc của bài toán. Nếu trong một lân cận của $(x_0$, $y_0)$ từ hệ thức

$\varphi(x,y) =$ 0 ta xác định được hàm số y $=$ y(x) thì rõ ràng $(x_0$, $y(x_0))$ là cực trị địa phương

của hàm số một biến số g(x) $=$ f(x, y(x)). Như vậy, trong trường hợp này bài toán tìm cực

trị ràng buộc được đưa về bài toán tìm cực trị tự do của hàm số một biến số. Ta xét bài

toán sau đây

Bài tập 3.18. Tìm cực trị có điều kiện

a) z $= \frac{1}{x}$ + $\frac{1}{y}$ với điều kiện $\frac{1}{x^2}$ + $\frac{1}{y^2} = \frac{1}{a^2}$

b) z $=$ x $\cdot$ y với điều kiện x + y $=$ 1

Chứng minh. a) Đặt x $= \frac{a}{\sin t};$ y $= \frac{a}{\cos t}$, ta có $\frac{1}{x^2}$ + $\frac{1}{y^2} = \frac{1}{a^2}$. Khi đó

z $= \frac{1}{x}$ + $\frac{1}{y} = \frac{\sin t}{a}$ + $\frac{\cos t}{a}$.

Ta có

$z'_t = \frac{\cos t}{a}$ - $\frac{\sin t}{a} = \frac{\sqrt{2}}{a} \sin \left( \frac{\pi}{4}$ - t $\right) =$ 0 $\Leftrightarrow$ t $= \frac{\pi}{4} \vee$ t $= \frac{5\pi}{4}$

Với t $= \frac{\pi}{4}$ ta có x $= \sqrt{2}a;$ y $= \sqrt{2}a$, hàm số đạt cực tiểu và $z_{CT} = -\frac{\sqrt{2}}{a}$.

Với t $= \frac{5\pi}{4}$ ta có x $= -\sqrt{2}a;$ y $= -\sqrt{2}a$, hàm số đạt cực đại và $z_{\text{CD}} = \frac{\sqrt{2}}{a}$.



b) Từ điều kiện x + y $=$ 1 ta suy ra y $=$ 1 - x. Vậy z $=$ xy $=$ x(1 - x). Dễ dàng nhận

thấy hàm số x $=$ x(1-x) đạt cực đại tại x $= \frac{1}{2}$ và $z_{\text{CD}} = \frac{1}{4}$.

$\blacksquare$

Tuy nhiên không phải lúc nào cũng tìm được hàm số y $=$ y(x) từ điều kiện $\varphi(x$, y) $=$ 0. Do

đó bài toán tìm cực trị điều kiện không phải lúc nào cũng đưa được về bài toán tìm cực trị

tự do. Trong trường hợp đó ta dùng phương pháp Lagrange được trình bày dưới đây.

Đinh lý 3.57 (Điều kiện cần để hàm số đạt cực trị điều kiện). Giả sử U là một tập

mở trong $\mathbb{R}^2$, f: U $\to \mathbb{R}$ và $(x_0$, $y_0)$ là điểm cực trị của hàm f với điều kiện $\varphi(x$, y) $=$ 0.

Hơn nữa giả thiết rằng:

a. Các hàm f(x,y), $\varphi(x,y)$ có các đạo hàm riêng liên tục trong một lân cận của $(x_0$, $y_0)$.

b. $\frac{\partial \varphi}{\partial y}(x_0$, $y_0) \neq$ 0.

Khi đó tồn tại một số $\lambda_0$ cùng với $x_0$, $y_0$ tạo thành nghiệm của hệ phương trình sau (đối với

$\lambda$, x, y)

$\frac{\partial \phi}{\partial x} =$ 0 $\qquad \qquad \left( \frac{\partial f}{\partial x}(x$, y) + $\lambda \frac{\partial \varphi}{\partial x}(x$, y) $=$ 0 $\right)$

$ \begin{cases} \frac{\partial \phi}{\partial y} = 0 \\ \frac{\partial \phi}{\partial y} = 0 \end{cases} \Leftrightarrow \begin{cases} \frac{\partial f}{\partial y}(x, y) + \lambda \frac{\partial \phi}{\partial y}(x, y) = 0 \\ \varphi(x, y) = 0 \end{cases} $

(3.3)

$v\acute{o}i \phi(x,y,\lambda) =$ f(x,y) + $\lambda \phi(x,y)$ được gọi là hàm Lagrange.

### Định lý trên chính là điều kiện cần của cực trị có ràng buộc. Giải hệ phương trình 3.3 ta

sẽ thu được các điểm tới hạn. Giả sử $M(x_0$, $y_0)$ là một điểm tới hạn ứng với giá trị $\lambda_0$. Ta

$c\acute{o}$

$\phi(x$, y, $\lambda_0)$ - $\phi(x_0$, $y_0$, $\lambda_0) =$ f(x, y) + $\lambda_0 \varphi(x$, y) - $f(x_0$, $y_0)$ - $\lambda_0 \varphi(x_0$, $y_0) =$ f(x, y) - $f(x_0$, $y_0)$

nên nếu M là một điểm cực trị của hàm số $\phi(x$, y, $\lambda_0)$ thì M cũng là điểm cực trị của hàm

số f(x,y) với điều kiện $\varphi(x,y) =$ 0. Muốn xét xem M có phải là điểm cực trị của hàm số

$\phi(x$, y, $\lambda_0)$ hay không ta có thể quay lại sử dụng định lý 3.56 hoặc đi tính vi phân cấp hai

$d^2\phi(x_0$, $y_0$, $\lambda_0) = \frac{\partial^2 \phi}{\partial x^2}(x_0$, $y_0$, $\lambda_0)dx^2$ + $2\frac{\partial^2 \phi}{\partial$ x $\partial y}(x_0$, $y_0$, $\lambda_0)dxdy$ + $\frac{\partial^2 \phi}{\partial y^2}(x_0$, $y_0$, $\lambda_0)dy^2$

trong đó dx và dy liên hệ với nhau bởi hệ thức

$\frac{\partial \varphi}{\partial x}(x_0$, $y_0)dx$ + $\frac{\partial \varphi}{\partial y}(x_0$, $y_0)dy =$ 0

hay

dy $= -\frac{\frac{\partial \varphi}{\partial x}(x_0$, $y_0)}{\frac{\partial \varphi}{\partial y}(x_0$, $y_0)}$ dx



Thay biểu thức này của dy vào $d^2\phi(x_0$, $y_0$, $\lambda_0)$ ta có

$d^2\phi(x_0$, $y_0$, $\lambda_0) = G(x_0$, $y_0$, $\lambda_0)dx^2$

Từ đó suy ra

• Nếu $G(x_0$, $y_0$, $\lambda_0) >$ 0 thì $(x_0$, $y_0)$ là điểm cực tiểu có điều kiện.

• Nếu $G(x_0$, $y_0$, $\lambda_0) <$ 0 thì $(x_0$, $y_0)$ là điểm cực đại có điều kiện.

Bài tập 3.19. Tìm cực trị có điều kiện của hàm số z $= \frac{1}{x}$ + $\frac{1}{y}$ với điều kiện $\frac{1}{x^2}$ + $\frac{1}{y^2} = \frac{1}{a^2}$

Chứng minh. Xét hàm số Lagrange $\phi(x$, y, $\lambda) = \frac{1}{x}$ + $\frac{1}{y}$ + $\lambda(\frac{1}{x^2}$ + $\frac{1}{y^2}$ - $\frac{1}{a^2})$. Từ hệ phương

trình

$ \begin{cases} \frac{\partial \phi}{\partial x} = -\frac{1}{x^2} - \frac{2\lambda}{x^3} \\ \frac{\partial \phi}{\partial y} = -\frac{1}{y^2} - \frac{2\lambda}{y^3} \\ \frac{\partial \phi}{\partial \lambda} = \frac{1}{x^2} + \frac{1}{y^2} - \frac{1}{a^2} = 0 \end{cases} $

ta thu được các điểm tới hạn là $M_1(a\sqrt{2}$, $a\sqrt{2})$ ứng với $\lambda_1 = -\frac{a}{\sqrt{2}}$, $M_2(-a\sqrt{2}$, $-a\sqrt{2})$ ứng

với $\lambda_2 = \frac{u}{\sqrt{2}}$. Ta có

$d^2\phi = \frac{\partial^2 \phi}{\partial x^2} dx^2$ + 2 $\frac{\partial^2 \phi}{\partial$ x $\partial y}$ dxdy + $\frac{\partial^2 \phi}{\partial y^2} dy^2 = \left(\frac{2}{x^3}$ + $\frac{6\lambda}{x^4}\right) dx^2$ + $\left(\frac{2}{y^3}$ + $\frac{6\lambda}{y^4}\right) dy^2$

Từ điều kiện $\frac{1}{x^2}$ + $\frac{1}{y^2}$ - $\frac{1}{a^2} =$ 0 suy ra $-\frac{2}{x^3}dx$ - $\frac{2}{y^3}dy =$ 0 nên dy $= -\frac{y^3}{x^3}dx$, thay vào biểu thức

$d^2\phi$ ta có

• Tại $M_1$, $d^2\phi(M_1) = -\frac{\sqrt{2}}{4a^3}(dx^2$ + $dy^2) = -\frac{2\sqrt{2}}{4a^3}(dx^2) <$ 0 nên $M_1$ là điểm cực đại có điều

kiện.

• Tại $M_2$, $d^2\phi(M_2) = \frac{\sqrt{2}}{4a^3}(dx^2$ + $dy^2) = \frac{2\sqrt{2}}{4a^3}(dx^2) >$ 0 nên $M_2$ là điểm cực tiểu có điều

kiện.

$\blacksquare$

## 3.3 Giá trị lớn nhất - Giá trị nhỏ nhất <math display="block">\blacksquare</math>

Giả sử f : A $\to \mathbb{R}$ là hàm số liên tục trên tập hợp đóng A của $\mathbb{R}^2$. Khi đó, f đạt giá trị

lớn nhất và giá trị nhỏ nhất trên A. Để tìm các giá trị này ta hãy tìm giá trị của hàm số

tại tất cả các điểm dừng trong miền A cũng như tại các điểm đạo hàm riêng không tồn tại,

sau đó so sánh các giá trị này với các giá trị của hàm trên biên $\partial$ A của A (tức là ta phải

xét cực trị có điều kiện).

Bài tập 3.20. Tìm giá trị lớn nhất và giá trị nhỏ nhất của các hàm số:



a) z $= x^2y(4$ - x - y) trong hình tam giác giới hạn bởi các đường x $=$ 0, y $=$ 0, x + y $=$ 6.

b) z $= \sin$ x + $\sin$ y + $\sin(x$ + y) trong hình chữ nhật giới hạn bởi các đường x $=$ 0, x $=$

$\frac{\pi}{2}$, y $=$ 0, y $= \frac{\pi}{2}$.



