# CHƯƠNG 1: HÀM SỐ MỘT BIẾN SỐ

## §1. SƠ LƯỢC VỀ CÁC YẾU TỐ LÔGIC; CÁC TẬP SỐ: $ \mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R} $

1. Phần lôgic không dạy trực tiếp (phần này Đại số đã dạy) mà chỉ nhắc lại những phép suy luận cơ bản thông qua bài giảng các nội dung khác nếu thấy cần thiết.

  
2. Giới thiệu các tập số; cần nói rõ tập $ \mathbb{Q} $ tuy đã rộng hơn $ \mathbb{Z} $ nhưng vẫn chưa lấp đầy trục số, còn tập $ \mathbb{R} $ đã lấp đầy trục số và chứa tất cả các giới hạn của các dãy số hội tụ; ta có chuỗi bao hàm 
$$ \mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} $$

## §2. TRỊ TUYỆT ĐỐI VÀ TÍNH CHẤT

#### Định nghĩa: Với mọi $ x \in \mathbb{R} $, $ |x| = x $ nếu $ x \ge 0 $ và $ |x| = -x $ nếu $ x < 0 $.

#### Tính chất:
- $ |x| \ge 0 $, $ |x| = 0 \iff x = 0 $, $ |x + y| \le |x| + |y| $.

  
- $ |x - y| \ge ||x| - |y|| $, $ |x| \ge A \iff x \ge A $ hoặc $ x \le -A $ với $ A \ge 0 $.

  
- $ |x| \le B \Longleftrightarrow -B \le x \le B $ với $ B \ge 0 $.


## §3. HÀM SỐ

### 3.1 Định nghĩa hàm số

#### Định nghĩa 1.1
Một hàm số đi từ tập $ X $ vào tập $ Y $ là một quy tắc cho tương ứng mỗi phần tử $ x \in X $ với một và chỉ một phần tử $ y \in Y $.

Một hàm số có thể được cho dưới dạng biểu thức giải tích $ y = f(x) $, chẳng hạn như hàm số $ y = x^2 $. Khi đó, cần phải xác định rõ miền xác định (hay tập xác định) của hàm số, tức là tập hợp tất cả các phần tử $ x \in X $ sao cho biểu thức $ f(x) $ được xác định.

  
Tập giá trị của hàm số: là tập tất cả các phần tử $ y \in Y $ sao cho tồn tại $ x \in X $ với $ f(x) = y $.

### 3.2 Hàm số đơn điệu

• Một hàm số $f(x)$ được gọi là đơn điệu tăng trên khoảng $(a,b)$ nếu $ \forall x_1, x_2 \in (a,b),\ x_1 < x_2 \Rightarrow f(x_1) < f(x_2) $.

  
• Một hàm số $f(x)$ được gọi là đơn điệu giảm trên khoảng $(a,b)$ nếu $ \forall x_1, x_2 \in (a,b),\ x_1 < x_2 \Rightarrow f(x_1) > f(x_2) $.

  
**Chú ý 1.1**: 
Trong bài giảng này, ta chỉ xét tính đơn điệu của hàm số trên mỗi khoảng mà hàm số đó xác định. Chẳng hạn, hàm số $f(x) = \frac{1}{x}$ có $f'(x) = -\frac{1}{x^2} < 0$ với mọi $x \in \text{TXĐ} = \mathbb{R} \setminus \{0\}$, nhưng nếu nói $f(x)$ đơn điệu giảm trên $\mathbb{R} \setminus \{0\}$ thì mâu thuẫn với việc $-1 < 1$ nhưng $f(-1) = -1 < f(1) = 1$. Thay vào đó, ta nói $f(x)$ đơn điệu giảm trên mỗi khoảng $(-\infty,0)$ và $(0,+\infty)$.



### 3.3 Hàm số bị chặn

• Một hàm số $f(x)$ được gọi là bị chặn trên nếu tồn tại số $M \in \mathbb{R}$ sao cho $f(x) \le M$ với mọi $x \in \text{TXĐ}$.

  
• Một hàm số $f(x)$ được gọi là bị chặn dưới nếu tồn tại số $m \in \mathbb{R}$ sao cho $f(x) \ge m$ với mọi $x \in \text{TXĐ}$.

  
• Một hàm số $f(x)$ được gọi là bị chặn nếu nó vừa bị chặn trên, vừa bị chặn dưới.

### 3.4 Hàm số chẵn, hàm số lẻ

• Một hàm số $f(x)$ được gọi là chẵn nếu $x \in \text{TXĐ} \Rightarrow -x \in \text{TXĐ}$ và $f(-x) = f(x)$. Đồ thị của hàm số chẵn nhận trục tung làm trục đối xứng.

  
• Một hàm số $f(x)$ được gọi là lẻ nếu $x \in \text{TXĐ} \Rightarrow -x \in \text{TXĐ}$ và $f(-x) = -f(x)$. Đồ thị của hàm số lẻ nhận gốc tọa độ làm tâm đối xứng.

### 3.5 Hàm số tuần hoàn

#### Định nghĩa 1.2: Một hàm số $f(x)$ được gọi là tuần hoàn nếu tồn tại số thực $T > 0$ sao cho $f(x) = f(x + T)$ với mọi $x \in \text{TXĐ}$.

Ví dụ quen thuộc: các hàm lượng giác $y = \sin x$, $y = \cos x$, $y = \tan x$, $y = \cot x$ đều là các hàm số tuần hoàn. Trong phạm vi bài giảng này, ta chủ yếu quan tâm đến việc có tồn tại $T > 0$ sao cho $f(x + T) = f(x)$, còn việc tìm chu kì nhỏ nhất không phải là trọng tâm.

Các câu hỏi gợi mở:

- Tổng (hoặc hiệu) của hai hàm số tuần hoàn có tuần hoàn không?

  
- Tích của hai hàm số tuần hoàn có tuần hoàn không?

  
- Thương của hai hàm số tuần hoàn có tuần hoàn không?

  
- Đạo hàm của một hàm số tuần hoàn (nếu tồn tại) có tuần hoàn không?

  
- Nếu hàm số $F(x)$ có đạo hàm trên $\mathbb{R}$ và $F'(x)$ là một hàm số tuần hoàn thì $F(x)$ có tuần hoàn không? Nói cách khác, nếu $f(x)$ là một hàm số tuần hoàn thì $F(x) = \int_{0}^{x} f(t)\,dt$ có tuần hoàn không?



### 3.6 Hàm hợp

Cho hai hàm số $f, g$. Hàm hợp của $f$ và $g$, kí hiệu $f \circ g$, được định nghĩa bởi $ (f \circ g)(x) = f(g(x)) $.



### 3.7 Hàm ngược

#### Định nghĩa 1.3
Một hàm số $f: X \to Y$ được gọi là ánh xạ 1-1 (đơn ánh) nếu $x_1 \ne x_2 \Rightarrow f(x_1) \ne f(x_2)$.

  
#### Định nghĩa 1.4
Cho $f$ là một đơn ánh với miền xác định $A$ và miền giá trị $B$. Hàm ngược $f^{-1}$ có miền xác định $B$ và miền giá trị $A$, được định nghĩa bởi $ f^{-1}(y) = x \Leftrightarrow f(x) = y $.

- $ \text{TXĐ}(f) = \text{Tập giá trị}(f^{-1}) $

  
- $ \text{Tập giá trị}(f) = \text{TXĐ}(f^{-1}) $

  
**Chú ý 1.2**
Đồ thị của hàm ngược đối xứng với đồ thị của $y = f(x)$ qua đường thẳng $y = x$ (đường phân giác của góc phần tư thứ nhất).

Cách tìm hàm số ngược của $y = f(x)$:

- Viết $y = f(x)$.

  
- Giải phương trình này theo $x$ theo biến $y$, giả sử được $x = g(y)$.

  
- Đổi vai trò của $x$ và $y$ để được hàm số ngược $f^{-1}(x) = g(x)$.
  
#### Định lý 1.1
Nếu hàm số $f(x)$ đơn điệu tăng hoặc đơn điệu giảm trên khoảng $(a,b)$ thì tồn tại hàm số ngược $f^{-1}$ của $f$ trên khoảng đó.

### 3.8 Hàm số sơ cấp

Năm loại hàm số sơ cấp cơ bản:

#### Hàm lũy thừa 
$y = x^{\alpha}$, TXĐ phụ thuộc vào $\alpha$.

- Nếu $\alpha$ nguyên dương, ví dụ $y = x^2$, thì xác định với mọi $x \in \mathbb{R}$.

  
- Nếu $\alpha$ nguyên âm, ví dụ $y = x^{-2} = \frac{1}{x^2}$, thì xác định với mọi $x \in \mathbb{R} \setminus \{0\}$, và nói chung $y = x^{\alpha} = \frac{1}{x^{-\alpha}}$.

  
- Nếu $\alpha = \frac{1}{p}$ với $p$ nguyên dương chẵn, ví dụ $y = x^{1/2} = \sqrt{x}$, thì xác định trên $\mathbb{R}_{\ge 0}$.

  
- Nếu $\alpha = \frac{1}{v}$ với $v$ nguyên dương lẻ, ví dụ $y = x^{1/3} = \sqrt[3]{x}$, thì xác định trên $\mathbb{R}$.

  
- Nếu $\alpha$ vô tỉ thì quy ước chỉ xét với $x > 0$.

  
#### Hàm số mũ 
$y = a^x$ với $0 < a \ne 1$: TXĐ là $\mathbb{R}$, tập giá trị là $\mathbb{R}_{>0}$. Hàm đồng biến nếu $a > 1$, nghịch biến nếu $0 < a < 1$.

  
#### Hàm số logarit 
$y = \log_a x$ với $0 < a \ne 1$: TXĐ là $\mathbb{R}_{>0}$, tập giá trị là $\mathbb{R}$. Hàm đồng biến nếu $a > 1$, nghịch biến nếu $0 < a < 1$. Đây là hàm ngược của $y = a^x$, nên đồ thị đối xứng với đồ thị $y = a^x$ qua đường $y = x$. Kí hiệu: $\lg x$ là logarit cơ số 10, $\ln x$ là logarit cơ số $e$.

  
#### Hàm số lượng giác cơ bản
• Hàm số $y = \sin x$ xác định $\forall x \in \mathbb{R}$, là hàm số lẻ, tuần hoàn chu kì $2\pi$.

![](../extracted/graphs/graph_10_0.png)

• Hàm số $y = \cos x$ xác định $\forall x \in \mathbb{R}$, là hàm số chẵn, tuần hoàn chu kì $2\pi$.

![](../extracted/graphs/graph_11_0.png)


• Hàm số $y = \tan x$ xác định $\forall x \in \mathbb{R} \setminus \left\{\left(2k+1\right)\frac{\pi}{2} \mid k \in \mathbb{Z}\right\}$, là hàm số lẻ, tuần hoàn chu kì $\pi$.

![](../extracted/graphs/graph_11_1.png)

• Hàm số $y = \cot x$ xác định $\forall x \in \mathbb{R} \setminus \left\{k\pi \mid k \in \mathbb{Z}\right\}$, là hàm số lẻ, tuần hoàn chu kì $\pi$.

![](../extracted/graphs/graph_11_2.png)


**ví dụ** (Ngụy biện toán học). Chứng minh rằng $0 = 2$.

Chứng minh. Ta có $ \cos^2 x = 1 - \sin^2 x \Rightarrow \cos x = \pm \sqrt{1 - \sin^2 x} \Rightarrow 1 + \cos x = 1 \pm \sqrt{1 - \sin^2 x} $. Thay $ x = \pi $ vào, vế trái bằng $0$, còn vế phải bằng $1 \pm 1$, không thể suy ra $0 = 2$.
  
#### Hàm số lượng giác ngược

Muốn tìm hàm ngược của một hàm số, điều kiện cần là hàm số đó phải đơn ánh. Tuy nhiên, các hàm lượng giác đều tuần hoàn nên không đơn ánh trên toàn bộ tập số thực.

Để khắc phục, ta hạn chế miền xác định của các hàm lượng giác về những khoảng mà chúng đơn ánh. Chẳng hạn, hàm $f(x)=\sin x$ là đơn ánh trên khoảng $-\pi/2 \le x \le \pi/2$.

- Hàm số ngược của $y=\sin x$, kí hiệu $\arcsin x$, được xác định bởi:
$x \mapsto y=\arcsin x \Leftrightarrow x=\sin y$

Với qui ước chuẩn, $\arcsin: [-1,1] \to [-\pi/2,\pi/2]$. Hàm $y=\arcsin x$ xác định trên $[-1,1]$, nhận giá trị trong $[-\pi/2,\pi/2]$ và là hàm đơn điệu tăng.

![](../extracted/graphs/graph_12_1.png)

- Hàm số ngược của $y=\cos x$, kí hiệu $\arccos x$, được xác định bởi:
$x \mapsto y=\arccos x \Leftrightarrow x=\cos y$

Với qui ước chuẩn, $\arccos: [-1,1] \to [0,\pi]$. Hàm $y=\arccos x$ xác định trên $[-1,1]$, nhận giá trị trong $[0,\pi]$ và là hàm đơn điệu giảm.

![](../extracted/graphs/graph_13_0.png)

- Hàm số ngược của $y=\tan x$, kí hiệu $\arctan x$, được xác định bởi:
$x \mapsto y=\arctan x \Leftrightarrow x=\tan y$

Ta có $\arctan: (-\infty,+\infty) \to (-\pi/2,\pi/2)$. Hàm $y=\arctan x$ xác định trên toàn bộ $\mathbb R$, nhận giá trị trong $(-\pi/2,\pi/2)$ và là hàm đơn điệu tăng.

![](../extracted/graphs/graph_13_1.png)

- Hàm số ngược của $y=\cot x$, kí hiệu $\operatorname{arccot} x$, được xác định bởi:
$x \mapsto y=\operatorname{arccot} x \Leftrightarrow x=\cot y$

Theo qui ước này, $\operatorname{arccot}: (-\infty,+\infty) \to (0,\pi)$. Hàm $y=\operatorname{arccot} x$ xác định trên toàn bộ $\mathbb R$, nhận giá trị trong $(0,\pi)$ và là hàm đơn điệu giảm.

![](../extracted/graphs/graph_14_0.png)

#### Hàm số sơ cấp

Người ta gọi hàm số sơ cấp là hàm số được tạo thành bởi một số hữu hạn các phép toán cộng, trừ, nhân, chia và phép hợp hàm từ các hàm số sơ cấp cơ bản. Các hàm số sơ cấp được chia thành hai loại:

- Hàm số đại số: là những hàm số mà khi tính giá trị của nó ta chỉ sử dụng một số hữu hạn phép cộng, trừ, nhân, chia và lũy thừa với số mũ hữu tỉ. Ví dụ: đa thức, phân thức hữu tỉ, ...

- Hàm số siêu việt: là những hàm số sơ cấp nhưng không phải là hàm số đại số, như $y=\ln x$, $y=\sin x$, ...

## §4. Dãy số


### 4.1 Dãy số và giới hạn của dãy số


#### Định nghĩa 1.5
Một dãy số là một hàm số $\,\mathbb{N} \to \mathbb{R},\; n \mapsto a_n\,$. Kí hiệu $\,\{a_n\}_{n \in \mathbb{N}}\,$.

Một dãy số được gọi là:

- đơn điệu tăng nếu $\,a_n < a_{n+1}\; \forall n\,$; đơn điệu giảm nếu $\,a_n > a_{n+1}\; \forall n\,$.

- bị chặn trên nếu tồn tại số $M$ sao cho $\,a_n \le M\; \forall n\,$; bị chặn dưới nếu tồn tại số $m$ sao cho $\,a_n \ge m\; \forall n\,$.


#### Định nghĩa 1.6
Một dãy số $\,\{a_n\}\,$ được gọi là có giới hạn là $L$ và viết $\,\lim_{n\to\infty} a_n = L\,$ (hay $\,a_n \to L\,$ khi $\,n \to \infty$) nếu:

- (trực giác) có thể làm cho các số hạng $a_n$ gần $L$ đến mức tùy ý bằng cách chọn $n$ đủ lớn.

- (chính xác) với mọi $\,\epsilon > 0\,$, tồn tại $\,N \in \mathbb{N}\,$ sao cho nếu $\,n > N\,$ thì $\,|a_n - L| < \epsilon\,$.

Hình dung rằng $\,\lim_{n\to+\infty} a_n = L\,$ nghĩa là với mọi $\,\epsilon > 0\,$ thì từ một chỉ số đủ lớn trở đi, toàn bộ các số hạng của dãy $\,\{a_n\}_{n > N}\,$ đều nằm trong khoảng $\,\big(L-\epsilon,\; L+\epsilon\big)\,$.

Một dãy số $\,\{a_n\}\,$ có $\,\lim_{n\to+\infty} a_n = L\,$ hữu hạn được gọi là hội tụ. Ngược lại, nó được gọi là phân kì (nghĩa là $\,\lim_{n\to+\infty} a_n = \pm\infty\,$ hoặc giới hạn không tồn tại).


#### Định nghĩa 1.7 (Giới hạn vô cùng)
Ta nói $\,\lim_{n\to+\infty} a_n = +\infty\,$ nếu với mọi $\,M > 0\,$, tồn tại $\,N \in \mathbb{N}\,$ sao cho nếu $\,n > N\,$ thì $\,a_n > M\,$.

Trường hợp $\,\lim_{n\to+\infty} a_n = -\infty\,$ được phát biểu tương tự: với mọi $\,M > 0\,$, tồn tại $\,N \in \mathbb{N}\,$ sao cho nếu $\,n > N\,$ thì $\,a_n < -M\,$.


#### Định lý 1.2 (Các tính chất của giới hạn của dãy số)
- Giới hạn của một dãy số, nếu tồn tại, là duy nhất.

- Mọi dãy số hội tụ đều bị chặn.


#### Định lý 1.3 (Các phép toán trên giới hạn)
Giả sử $\,\lim_{n\to+\infty} a_n = A,\; \lim_{n\to+\infty} b_n = B\,$, ở đó $\,A, B \in \mathbb{R}\,$ (hữu hạn). Khi đó:

- Tổng: $\,\lim_{n\to+\infty} (a_n + b_n) = A + B\,$.

- Hiệu: $\,\lim_{n\to+\infty} (a_n - b_n) = A - B\,$.

- Tích: $\,\lim_{n\to+\infty} (a_n\, b_n) = A B\,$.

- Thương: $\,\lim_{n\to+\infty} \dfrac{a_n}{b_n} = \dfrac{A}{B}\,$ nếu $\,B \ne 0\,$.


**Chú ý 1.3**
Các phép toán trên giới hạn sau không thực hiện được (dạng vô định): $\,\infty - \infty,\; 0 \times \infty,\; \dfrac{\infty}{\infty},\; \dfrac{0}{0}\,.$

### 4.2 Các tiêu chuẩn tồn tại giới hạn


#### Định lý 1.4 (Tiêu chuẩn kẹp)

Giả sử:

i) $a_n \le b_n \le c_n$ với mọi $n \in \mathbb{N}$, hoặc với mọi $n \ge K$ nào đó, với $K \in \mathbb{N}$.

ii) $\lim_{n\to+\infty} a_n = \lim_{n\to+\infty} c_n = L$.

Khi đó, $\lim_{n\to+\infty} b_n = L$.


#### Định lý 1.5 (Tiêu chuẩn đơn điệu bị chặn)

Mọi dãy số đơn điệu tăng và bị chặn trên (tương ứng, đơn điệu giảm và bị chặn dưới) đều hội tụ.


**ví dụ**

Xét $u_n = \left(1 + \frac{1}{n}\right)^n$. Chứng minh rằng $\{u_n\}$ là một dãy số tăng và bị chặn.

**bài làm**

- Tăng: Áp dụng AM-GM cho $n+1$ số dương $1,\; \underbrace{1+\tfrac{1}{n},\ldots,1+\tfrac{1}{n}}_{n\ \text{số}}$:
  
  $1 + \left(1+\frac{1}{n}\right) + \cdots + \left(1+\frac{1}{n}\right) \ge (n+1)\sqrt[n+1]{\left(1 \cdot \left(1+\frac{1}{n}\right)^n\right)}$.
  
  Vì vế trái bằng $n+2$, ta được $1 + \frac{1}{n+1} \ge \left(1+\frac{1}{n}\right)^{\frac{n}{n+1}}$. Nâng lũy thừa $(n+1)$ hai vế suy ra:
  
  $\left(1+\frac{1}{n+1}\right)^{n+1} \ge \left(1+\frac{1}{n}\right)^n$, tức $u_{n+1} \ge u_n$.

- Bị chặn trên: Khai triển nhị thức
  
  $u_n = \left(1+\frac{1}{n}\right)^n = \sum_{k=0}^n \binom{n}{k}\frac{1}{n^k} = 1 + 1 + \sum_{k=2}^n \binom{n}{k}\frac{1}{n^k}$.
  
  Với $k \ge 2$,
  
  $\binom{n}{k}\frac{1}{n^k} = \frac{n(n-1)\cdots(n-k+1)}{k!\,n^k} < \frac{1}{k!} \le \frac{1}{2^{\,k-1}}$.
  
  Do đó
  
  $u_n < 1 + 1 + \sum_{k=2}^{\infty} \frac{1}{2^{\,k-1}} = 2 + 1 = 3$.
  
  Vậy $\{u_n\}$ tăng và bị chặn trên bởi $3$ nên hội tụ.


**Chú ý 1.4**

Giới hạn $\lim_{n\to+\infty}\left(1+\frac{1}{n}\right)^n$ là một số vô tỉ, được kí hiệu là $e$. Nó có giá trị xấp xỉ $2.71$.


**ví dụ**

Xét sự hội tụ và tìm giới hạn (nếu có) của dãy số $\{x_n\}$ xác định bởi $x_1 > 0$, $x_{n+1} = \frac{1}{2}\left(x_n + \frac{1}{x_n}\right)$, $n \ge 1$.

**bài làm**

- Từ $x_1 > 0$ suy ra bằng quy nạp $x_n > 0$ với mọi $n$.

- Với $n \ge 2$, ta có $x_n = \frac{1}{2}\left(x_{n-1} + \frac{1}{x_{n-1}}\right) \ge 1$ (do AM-GM: $\frac{x + 1/x}{2} \ge 1$ với mọi $x>0$). Vì $x_n \ge 1$ nên
  
  $x_{n+1} = \frac{1}{2}\left(x_n + \frac{1}{x_n}\right) \le \frac{1}{2}(x_n + x_n) = x_n$.
  
  Do đó $\{x_n\}$ là dãy giảm và bị chặn dưới bởi $1$.

- Bởi định lý đơn điệu bị chặn, tồn tại $\lim_{n\to+\infty} x_n = a \ge 1$. Chuyển giới hạn trong hệ thức truy hồi:
  
  $a = \frac{1}{2}\left(a + \frac{1}{a}\right) \Rightarrow a^2 = 1$.
  
  Do $a>0$ nên $a=1$.

Kết luận: $\lim_{n\to+\infty} x_n = 1$.


#### Định nghĩa 1.8

Dãy số $\{a_n\}$ được gọi là dãy số Cauchy nếu với mọi $\epsilon > 0$, tồn tại $N \in \mathbb{N}$ sao cho $|a_n - a_m| < \epsilon$ với mọi $m,n > N$.


#### Định lý 1.6 (Tiêu chuẩn Cauchy)

Dãy số $\{a_n\}$ hội tụ khi và chỉ khi nó là dãy số Cauchy.

## §5. GIỚI HẠN HÀM SỐ
### 5.1 Định nghĩa
#### Định nghĩa 1.9
Giả sử hàm số $f(x)$ được xác định tại mọi điểm $x \in (a,b) \setminus {x_0}$. Ta nói giới hạn của hàm số $f(x)$ khi $x$ tiến đến $x_0$ bằng $L$ và viết
$\lim_{x \to x_0} f(x) = L$

- (Nói một cách nôm na) nếu ta có thể làm cho giá trị $f(x)$ gần $L$ tùy ý bằng cách chọn $x$ đủ gần $x_0$.

- (Nói một cách chính xác) nếu $\forall \epsilon > 0$, $\exists \delta > 0$ sao cho $$ \text{nếu } |x - x_0| < \delta \text{ thì } |f(x) - L| < \epsilon$$

Hình dung: $\lim_{x \to x_0} f(x) = L$ nghĩa là $\forall \epsilon > 0$, $\exists \delta > 0$ sao cho đồ thị hàm số trong $(x_0 - \delta, x_0 + \delta)$ nằm hoàn toàn trong dải $(L - \epsilon, L + \epsilon)$.

![](../extracted/graphs/graph_28_0.png)

Các giới hạn một phía $\lim_{x \to x_0^+} f(x) = L$, $\lim_{x \to x_0^-} f(x) = L$ và $\lim_{x \to \infty} f(x) = L$ được định nghĩa tương tự.

#### Định lý 1.7 (Tính duy nhất của giới hạn)
Giới hạn $\lim_{x \to x_0} f(x)$, nếu tồn tại, là duy nhất.

### 5.2 Các phép toán trên giới hạn
#### Định lý 1.8 (Các phép toán trên giới hạn)
Giả sử $\lim_{x \to x_0} f(x) = a$, $\lim_{x \to x_0} g(x) = b$ với $a, b$ hữu hạn. Khi đó:

Tổng: $\lim_{x \to x_0} [f(x) + g(x)] = a + b$

Hiệu: $\lim_{x \to x_0} [f(x) - g(x)] = a - b$

Tích: $\lim_{x \to x_0} [f(x) \cdot g(x)] = a \cdot b$

Thương: $\lim_{x \to x_0} \frac{f(x)}{g(x)} = \frac{a}{b}$ (nếu $b \neq 0$)

**Chú ý 1.5**
Các phép toán sau không thực hiện được (dạng vô định):
$\infty - \infty$, $0 \cdot \infty$, $\frac{\infty}{\infty}$, $\frac{0}{0}$.

### 5.3 Giới hạn của hàm hợp
Nếu $\lim_{x \to x_0} u(x) = u_0$, $\lim_{u \to u_0} f(u) = f(u_0)$ và tồn tại hàm hợp $f(u(x))$ thì:
$\lim_{x \to x_0} f(u(x)) = f(u_0)$.

Áp dụng:
$\lim_{x \to x_0} A(x)^{B(x)} = e^{\lim_{x \to x_0} B(x) \ln A(x)}$.

### 5.4 Giới hạn vô cùng
#### Định nghĩa 1.10
Giả sử $f(x)$ xác định tại mọi $x \in (a,b) \setminus {x_0}$. Ta nói:
$\lim_{x \to x_0} f(x) = \infty$
nếu $\forall M > 0$, $\exists \delta > 0$ sao cho nếu $|x - x_0| < \delta$ thì $|f(x)| > M$.

Các giới hạn $\lim_{x \to x_0^+} f(x) = \infty$, $\lim_{x \to x_0^-} f(x) = \infty$ và $\lim_{x \to \infty} f(x) = \infty$ định nghĩa tương tự.

### 5.5 Các tiêu chuẩn tồn tại giới hạn
#### Định lý 1.9
Nếu $f(x) \leq g(x)$ trong lân cận của $a$, và tồn tại $\lim_{x \to a} f(x)$, $\lim_{x \to a} g(x)$, thì:
$\lim_{x \to a} f(x) \leq \lim_{x \to a} g(x)$.

#### Hệ quả 1.1 (Tiêu chuẩn kẹp)
Nếu $f(x) \leq g(x) \leq h(x)$ trong lân cận của $a$, và $\lim_{x \to a} f(x) = \lim_{x \to a} h(x) = L$. Khi đó:
$\lim_{x \to a} g(x) = L$.

### 5.6 Mối liên hệ giữa giới hạn dãy số và giới hạn hàm số
Nhiều bài toán giới hạn dãy số có thể chuyển về giới hạn hàm số và sử dụng các công cụ tính giới hạn hàm số để giải quyết dễ dàng. Mối liên hệ này được thể hiện qua định lý sau:

#### Định lý 1.10
$\lim_{x\to x_0} f(x) = L$ khi và chỉ khi với mọi dãy số ${x_n}$ thỏa mãn:

$\lim_{n\to+\infty} x_n = x_0$

$x_n \neq x_0$ (với mọi $n$ đủ lớn)
thì $\lim_{n\to+\infty} f(x_n) = L$.

(Trong định lý này, $x_0$ và $L$ có thể là số thực hoặc $\pm\infty$)

Ứng dụng:
Để tính $\lim_{n \to +\infty} \frac{\ln n}{n}$, ta chuyển về giới hạn hàm số:
$\lim_{x \to +\infty} \frac{\ln x}{x} = 0$
Suy ra $\lim_{n \to +\infty} \frac{\ln n}{n} = 0$.

## §6. VÔ CÙNG LỚN, VÔ CÙNG BÉ

### 6.1 Vô cùng bé (VCB)

#### Định nghĩa 1.11  
Hàm số $f(x)$ được gọi là **vô cùng bé (VCB)** khi $x \to a$ nếu:  
$\lim_{x \to a} f(x) = 0$.

**Mối liên hệ giữa giới hạn và VCB**:  
$\lim_{x \to a} f(x) = \ell \iff f(x) = \ell + \alpha(x)$,  
trong đó $\alpha(x)$ là VCB khi $x \to a$.

**Tính chất VCB**:  
1. Tổng hai VCB là một VCB.  
2. Tích của VCB với hàm bị chặn là VCB.  
3. Tích các VCB là VCB.  
**Chú ý**: Thương hai VCB là dạng vô định $\frac{0}{0}$.

#### Định nghĩa 1.12 (So sánh VCB)  
Giả sử $\alpha(x)$, $\beta(x)$ là VCB khi $x \to a$:  
- **Cùng bậc** nếu $\lim_{x \to a} \frac{\alpha(x)}{\beta(x)} = A \neq 0$.  
- **Tương đương** ($\alpha(x) \sim \beta(x)$) nếu $\lim_{x \to a} \frac{\alpha(x)}{\beta(x)} = 1$.  

**Các VCB tương đương thường dùng khi $x \to 0$**:  
- $x \sim \sin x \sim \tan x \sim \arcsin x \sim \arctan x \sim e^x - 1 \sim \ln(1 + x)$  
- $(1+x)^a - 1 \sim ax$ (đặc biệt $\sqrt[m]{1+\alpha x} - 1 \sim \frac{\alpha x}{m}$)  
- $1 - \cos x \sim \frac{x^2}{2}$  

#### Định nghĩa 1.13 (VCB bậc cao)  
$\alpha(x)$ là VCB bậc cao hơn $\beta(x)$ nếu $\lim_{x \to a} \frac{\alpha(x)}{\beta(x)} = 0$, kí hiệu $\alpha(x) = o(\beta(x))$.  

#### Định lý 1.11  
a) Hiệu hai VCB tương đương là VCB bậc cao hơn mỗi VCB ban đầu:  
$\alpha \sim \beta \implies \alpha - \beta = o(\alpha)$  
b) Tích hai VCB là VCB bậc cao hơn mỗi VCB:  
$\alpha = o(1), \beta = o(1) \implies \alpha\beta = o(\alpha)$  

#### Định lý 1.12 (Thay tương đương)  
Nếu $\alpha_1 \sim \alpha_2$, $\beta_1 \sim \beta_2$ khi $x \to a$ thì:  
$\lim_{x \to a} \frac{\alpha_1(x)}{\beta_1(x)} = \lim_{x \to a} \frac{\alpha_2(x)}{\beta_2(x)}$,  
$\lim_{x \to a} \alpha_1(x)\gamma(x) = \lim_{x \to a} \alpha_2(x)\gamma(x)$.  

#### Định lý 1.13 (Ngắt bỏ VCB bậc cao)  
Nếu $\alpha_1 = o(\alpha_2)$, $\beta_1 = o(\beta_2)$ khi $x \to a$ thì:  
$\alpha_1 + \alpha_2 \sim \alpha_2$ và  
$\lim_{x \to a} \frac{\alpha_1(x) + \alpha_2(x)}{\beta_1(x) + \beta_2(x)} = \lim_{x \to a} \frac{\alpha_2(x)}{\beta_2(x)}$.  

**Chú ý 1.6**: Không được thay tương đương cho **hiệu** hai VCB tương đương.  
#### Ví dụ: Với $\alpha(x) = \sin x - \tan x + x^3$ khi $x \to 0$:  
- Sai: $\alpha(x) \sim x^3$  
- Đúng: $\alpha(x) \sim \frac{x^3}{2}$ (vì $\lim_{x \to 0} \frac{\sin x - \tan x + x^3}{x^3} = \frac{1}{2}$)  

### 6.2 Vô cùng lớn (VCL)

#### Định nghĩa 1.14  
Hàm số $f(x)$ được gọi là **vô cùng lớn (VCL)** khi $x \to a$ nếu:  
$\lim_{x \to a} |f(x)| = \infty$.  
> **Nhận xét**: Nghịch đảo của VCB là VCL và ngược lại.

#### Định nghĩa 1.15 (So sánh VCL)  
Giả sử $\alpha(x)$, $\beta(x)$ là VCL khi $x \to a$:  
- **Cùng bậc** nếu $\lim_{x \to a} \frac{\alpha(x)}{\beta(x)} = A \neq 0$.  
- **Tương đương** ($\alpha(x) \sim \beta(x)$) nếu $\lim_{x \to a} \frac{\alpha(x)}{\beta(x)} = 1$.  

#### Định nghĩa 1.16 (VCL bậc cao)  
$\alpha(x)$ là VCL bậc cao hơn $\beta(x)$ nếu $\lim_{x \to a} \frac{\alpha(x)}{\beta(x)} = \infty$.  

#### Định lý 1.14 (Thay tương đương)  
Nếu $\alpha_1 \sim \alpha_2$, $\beta_1 \sim \beta_2$ là VCL khi $x \to a$ thì:  
$\lim_{x \to a} \frac{\alpha_1(x)}{\beta_1(x)} = \lim_{x \to a} \frac{\alpha_2(x)}{\beta_2(x)}$.  

#### Định lý 1.15 (Ngắt bỏ VCL bậc thấp)  
Nếu $\alpha_1$ là VCL bậc cao hơn $\alpha_2$, $\beta_1$ là VCL bậc cao hơn $\beta_2$ khi $x \to a$ thì:  
$\alpha_1 + \alpha_2 \sim \alpha_1$ và  
$\lim_{x \to a} \frac{\alpha_1(x) + \alpha_2(x)}{\beta_1(x) + \beta_2(x)} = \lim_{x \to a} \frac{\alpha_1(x)}{\beta_1(x)}$.  

**Chú ý 1.7**: Một số dạng vô định (như $\lim_{x \to 0} \frac{x - \sin x}{x^3}$, $\lim_{x \to 0^+} x^{\sin x}$) cần dùng quy tắc L'Hospital hoặc khai triển Maclaurin.  

## §7. HÀM SỐ LIÊN TỤC

### 7.1 Định nghĩa

#### Định nghĩa 1.17  
Cho hàm số $f(x)$ xác định trong lân cận của $x_0$. Hàm số được gọi là:  
- i) **Liên tục phải** tại $x_0$ nếu $\lim_{x \to x_0^+} f(x) = f(x_0)$.  
- ii) **Liên tục trái** tại $x_0$ nếu $\lim_{x \to x_0^-} f(x) = f(x_0)$.  
- iii) **Liên tục** tại $x_0$ nếu $\lim_{x \to x_0} f(x) = f(x_0)$.  

*Cách phát biểu tương đương:*
$f$ liên tục tại $x_0$ nếu $\forall \varepsilon > 0$, $\exists \delta(\varepsilon, x_0) > 0$ sao cho $\forall x$ thỏa mãn $|x - x_0| < \delta$ thì $|f(x) - f(x_0)| < \varepsilon$.  

**Nhận xét**: $f(x)$ liên tục tại $x_0$ $\iff$ $f$ liên tục phải và liên tục trái tại $x_0$.

#### Ví dụ
Các hàm sơ cấp liên tục trên tập xác định của chúng.

#### Định nghĩa 1.18  
$f(x)$ **liên tục trên khoảng $(a, b)$** nếu liên tục tại mọi $x_0 \in (a, b)$.  
$f(x)$ **liên tục trên đoạn $[a, b]$** nếu:  
- Liên tục trên $(a, b)$,  
- Liên tục phải tại $a$,  
- Liên tục trái tại $b$.  

### 7.2 Phép toán trên hàm liên tục

#### Định lý 1.16  
Nếu $f(x)$, $g(x)$ liên tục tại $x_0$ thì:  
- $f(x) \pm g(x)$ liên tục tại $x_0$  
- $f(x) \cdot g(x)$ liên tục tại $x_0$  
- $\frac{f(x)}{g(x)}$ liên tục tại $x_0$ (nếu $g(x_0) \neq 0$)  

Điều tương tự cũng đúng đối với các hàm số liên tục trái (phải) tại ${x0}$.

### 7.3 Hàm ngược liên tục

#### Định lý 1.17  
Nếu $y = f(x)$ đồng biến (hoặc nghịch biến) và liên tục trên khoảng $X$ thì tồn tại hàm ngược $y = g(x)$ đồng biến (hoặc nghịch biến) và liên tục trên $f(X)$.  

#### Ví dụ: Các hàm lượng giác ngược liên tục trên tập xác định.

### 7.4 Hàm hợp liên tục

#### Định lý 1.18  
Nếu $f(x)$ liên tục tại $b$ và $\lim_{x \to a} g(x) = b$ thì:  
$\lim_{x \to a} f(g(x)) = f(b)$  
hay viết gọn:  
$\lim_{x \to a} f(g(x)) = f\left( \lim_{x \to a} g(x) \right)$.

**Hệ quả 1.2**  
Nếu $g(x)$ liên tục tại $a$ và $f(x)$ liên tục tại $g(a)$ thì hàm hợp $f \circ g$ liên tục tại $a$.

### 7.5 Định lý cơ bản về hàm liên tục

#### Định lý 1.19 (Bảo toàn dấu)  
Nếu $f(x)$ liên tục tại $x_0 \in (a,b)$ và $f(x_0) > 0$ (hoặc $< 0$) thì tồn tại lân cận $U(x_0)$ sao cho $f(x)$ cùng dấu với $f(x_0)$ trên $U(x_0)$.

#### Định lý 1.20 (Bị chặn)  
Nếu $f(x)$ liên tục trên đoạn $[a, b]$ thì $f$ bị chặn trên $[a, b]$.

#### Định lý 1.21 (Weierstrass - Đạt min, max)  
Nếu $f(x)$ liên tục trên đoạn $[a, b]$ thì $f$ đạt giá trị lớn nhất và nhỏ nhất trên $[a, b]$.

#### Định lý 1.22 (Cantor - Liên tục đều)  
Nếu $f(x)$ liên tục trên đoạn $[a, b]$ thì $f$ liên tục đều trên $[a, b]$.  
> **Lưu ý**: Định lý không đúng nếu thay đoạn $[a, b]$ bằng khoảng $(a, b)$.

#### Định lý 1.23 (Cauchy)  
Nếu $f(x)$ liên tục trên $[a, b]$ và $f(a) \cdot f(b) < 0$ thì tồn tại $\alpha \in (a, b)$ sao cho $f(\alpha) = 0$.

#### Ví dụ
Cho $f: [1,3] \to [1,3]$ liên tục. Chứng minh tồn tại $x_0 \in [1,3]$ sao cho $f(x_0) = x_0$.  
**Giải**: Xét $g(x) = f(x) - x$.  
- $g(1) = f(1) - 1 \geq 0$ (vì $f(1) \in [1,3]$)  
- $g(3) = f(3) - 3 \leq 0$ (vì $f(3) \in [1,3]$)  

Theo Định lý Cauchy, tồn tại $x_0 \in [1,3]$ sao cho $g(x_0) = 0 \iff f(x_0) = x_0$.

**Hệ quả 1.3**  
Nếu $f$ liên tục trên $[a,b]$, $A = f(a)$, $B = f(b)$ ($A \neq B$) thì $f$ nhận mọi giá trị nằm giữa $A$ và $B$.

**Hệ quả 1.4**  
Nếu $f$ liên tục trên $[a,b]$, $m = \min_{[a,b]} f(x)$, $M = \max_{[a,b]} f(x)$ thì $f([a,b]) = [m, M]$.

### 7.6 Điểm gián đoạn và phân loại

#### Định nghĩa 1.19  
Nếu hàm số không liên tục tại điểm x0thì ta nói nó gián đoạn tại x0

Hình ảnh hình học: đồ thị không liền nét tại điểm gián đoạn.

Theo định nghĩa, hàm số $f(x)$ liên tục tại $x_0$ nếu ba điều kiện sau được thỏa mãn:

- $f(x)$ xác định tại $x_0$,

- tồn tại $\lim_{x \to x_0} f(x)$,

- $\lim_{x \to x_0} f(x) = f(x_0)$.

Như vậy nếu $x_0$ là điểm gián đoạn của $f(x)$ thì

- hoặc $x_0 \notin \text{TXĐ}$,

- hoặc $x_0 \in \text{TXĐ và } \not\exists \lim_{x \to x_0} f(x)$,

- hoặc $x_0 \in \text{TXĐ}$ và $\exists \lim_{x \to x_0} f(x)$ nhưng $\lim_{x \to x_0}  f(x) \neq f(x_0)$, ở đây $x \to x_0$ theo nghĩa cả hai phía hay một phía.

Nếu $x_0 \notin \text{TXD}$ của $f(x)$ thì có thể có rất nhiều điểm gián đoạn, nên ta chỉ quan tâm đến những điểm gián đoạn thuộc tập xác định hay là những điểm đầu mút của khoảngn xác định.


#### Phân loại điểm gián đoạn


Giả sử $x_0$ là điểm gián đoạn của f(x).


1. Điểm gián đoạn loại 1:


Nếu $\exists \lim_{x \to x_0^+} f(x) = f(x_0^+)$ và $\lim_{x \to x_0^-} f(x) = f(x_0^-)$ thì $x_0$ được gọi là điểm gián đoạn loại 1 của hàm số f(x). Khi đó, có thể xảy ra hai trường hợp:


• Nếu $f(x_0^+) \neq f(x_0^-)$ thì giá trị $|f(x_0^+) - f(x_0^-)|$ gọi là bước nhảy của hàm số.


• Đặc biệt: nếu $f(x_0^+) = f(x_0^-)$ thì $x_0$ được gọi là điểm gián đoạn bỏ được của hàm số. Khi đó nếu hàm số chưa xác định tại $x_0$ thì ta có thể bổ sung thêm giá trị của hàm số tại $x_0$ để hàm số liên tục tại điểm $x_0$. Còn nếu hàm số xác định tại điểm $x_0$ thì ta có thể thay đổi giá trị của hàm số tại điểm này để hàm số liên tục tại $x_0$.


2. Điểm gián đoạn loại 2:


Nếu $x_0$ không là điểm gián đoạn loại 1 thì ta nói nó là điểm gián đoạn loại 2.


**Chú ý 1.10**

Với quan điểm xem điểm gián đoạn bỏ được là trường hợp đặc biệt của điểm gián đoạn loại 1, nếu $x_0$ là điểm đầu mút của khoảng hay đoạn xác định của f(x), mà có $\lim_{x \to x_0^+} f(x)$ hoặc $\lim_{x \to x_0^-} f(x)$ hữu hạn thì ta cũng xem $x_0$ là điểm gián đoạn bỏ được của hàm số.

## §8. ĐẠO HÀM VÀ VI PHÂN

### 8.1 Định nghĩa

#### Định nghĩa 1.20  
Giới hạn, nếu có, của tỉ số  

$$ \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} $$

được gọi là **đạo hàm** của hàm số $f(x)$ tại $x_0$ và được kí hiệu là $f'(x_0)$. Khi đó ta nói hàm số $f(x)$ có đạo hàm tại $x_0$.

Nếu quá trình $\Delta x \to 0$ trong định nghĩa trên được thay bằng:  
- $\Delta x \to 0^+$ thì giới hạn đó được gọi là **đạo hàm phải** tại $x_0$, kí hiệu $f'(x_0^+)$.  
- $\Delta x \to 0^-$ thì giới hạn đó được gọi là **đạo hàm trái** tại $x_0$, kí hiệu $f'(x_0^-)$.  

Hàm số có đạo hàm tại $x_0$ khi và chỉ khi nó có đạo hàm trái và đạo hàm phải tại $x_0$ và $f'(x_0^+) = f'(x_0^-)$.

**Chú ý:**  
- Nếu tồn tại $f'(x_0)$ thì $f(x)$ liên tục tại $x_0$.  
- Điều ngược lại không đúng. Ví dụ: $f(x) = |x|$ liên tục tại $0$ nhưng không có đạo hàm tại đó.

#### Ví dụ
Cho hàm số $f(x)$ khả vi tại $1$ và $\lim_{x \to 0} \frac{f(1 + 7x) - f(1 + 2x)}{x} = 2$. Tính $f'(1)$.

**Lời giải:**  
$\begin{aligned} 
\lim_{x \to 0} \frac{f(1+7x) - f(1+2x)}{x} &= \lim_{x \to 0} \left[ 7 \cdot \frac{f(1+7x) - f(1)}{7x} - 2 \cdot \frac{f(1+2x) - f(1)}{2x} \right] \\ 
&= 7f'(1) - 2f'(1) = 5f'(1) 
\end{aligned}$  
Theo giả thiết: $5f'(1) = 2 \Rightarrow f'(1) = \dfrac{2}{5}$.

#### Ví dụ
Cho $f(x) = \begin{cases} e^{-1/x} & \text{nếu } x > 0 \\ 0 & \text{nếu } x = 0 \end{cases}$. Tính $f'_+(0)$.

**Lời giải:**  
$f'_+(0) = \lim_{x \to 0^{+}} \frac{f(x) - f(0)}{x} = \lim_{x \to 0^{+}} \frac{e^{-1/x}}{x}$.  
Đặt $t = \frac{1}{x}$:  
$f'_+(0) = \lim_{t \to +\infty} \frac{t}{e^t} = \lim_{t \to +\infty} \frac{1}{e^t} = 0$ (dùng L'Hospital).

### 8.2 Các phép toán trên đạo hàm

#### Định lý 1.24  
Cho $u(x)$, $v(x)$ có đạo hàm tại $x_0$. Khi đó:  
i) $(u \pm v)'(x_0) = u'(x_0) \pm v'(x_0)$  
ii) $(uv)'(x_0) = u'(x_0)v(x_0) + u(x_0)v'(x_0)$  
iii) $\left( \dfrac{u}{v} \right)'(x_0) = \dfrac{u'(x_0)v(x_0) - u(x_0)v'(x_0)}{v^2(x_0)}$ (nếu $v(x_0) \neq 0$)

### 8.3 Đạo hàm của hàm hợp

#### Định lý 1.25  
Nếu $u$ có đạo hàm tại $x$ và $f$ có đạo hàm tại $u(x)$, thì hàm hợp $F = f \circ u$ có đạo hàm tại $x$ và:  
$F'(x) = f'(u(x)) \cdot u'(x)$

**Ý tưởng chứng minh:**  
Với $\Delta x$ đủ nhỏ:  
$u(x_0 + \Delta x) = u(x_0) + u'(x_0) \Delta x + o(\Delta x)$  
Gọi $\delta_u = u'(x_0) \Delta x + o(\Delta x)$. Khi đó:  
$\begin{aligned} 
f[u(x_0 + \Delta x)] - f[u(x_0)] &= f[u_0 + \delta_u] - f(u_0) \\ 
&= f'(u_0) \cdot \delta_u + o(\delta_u) 
\end{aligned}$  
Suy ra:  
$\lim_{\Delta x \to 0} \frac{F(x_0 + \Delta x) - F(x_0)}{\Delta x} = f'(u_0) \cdot u'(x_0)$


### 8.4 Đạo hàm của hàm ngược

#### Định lý 1.26  
Giả sử:  
i) $x = \varphi(y)$ có đạo hàm tại $y_0$ và $\varphi'(y_0) \neq 0$,  
ii) $x = \varphi(y)$ có hàm ngược $y = f(x)$ liên tục tại $x_0 = \varphi(y_0)$.  
Khi đó $f$ có đạo hàm tại $x_0$ và $f'(x_0) = \dfrac{1}{\varphi'(y_0)}$.

#### Định lý 1.27  
Giả sử:  
i) $x = \varphi(y)$ có đạo hàm tại $y_0$ và $\varphi'(y_0) \neq 0$,  
ii) $x = \varphi(y)$ đơn điệu trong lân cận $y_0$.  
Khi đó tồn tại hàm ngược $y = f(x)$ khả vi tại $x_0$ và $f'(x_0) = \dfrac{1}{\varphi'(y_0)}$.

**Ứng dụng:** Xây dựng công thức đạo hàm cho các hàm lượng giác ngược.

### 8.5 Đạo hàm của các hàm số sơ cấp cơ bản

1. $(x^\alpha)' = \alpha x^{\alpha-1}$  
2. $(a^x)' = a^x \ln a$  
3. $(\log_a x)' = \frac{1}{x \ln a}$  
4. $(\ln x)' = \frac{1}{x}$  
5. $(\sin x)' = \cos x$  
6. $(\cos x)' = -\sin x$  
7. $(\tan x)' = \frac{1}{\cos^2 x} = \sec^2 x$  
8. $(\cot x)' = -\frac{1}{\sin^2 x} = -\csc^2 x$  
9. $(\arcsin x)' = \frac{1}{\sqrt{1-x^2}}$  
10. $(\arccos x)' = -\frac{1}{\sqrt{1-x^2}}$  
11. $(\arctan x)' = \frac{1}{1+x^2}$  
12. $(\operatorname{arccot} x)' = -\frac{1}{1+x^2}$  

### 8.6 Vi phân của hàm số

#### Định nghĩa 1.21  
Cho hàm số $y = f(x)$ xác định trong lân cận $U_\epsilon(x_0)$. Nếu có:  
$$\Delta f = A \Delta x + o(\Delta x)$$
trong đó $A$ chỉ phụ thuộc $x_0$ và không phụ thuộc $\Delta x$, thì $f$ **khả vi** tại $x_0$ và **vi phân** của $f$ tại $x_0$ là:  
$$df = A \Delta x$$
  
#### Định lý 1.28 (Mối liên hệ với đạo hàm)
$f(x)$ có đạo hàm tại $x_0$ $\iff$ $f(x)$ khả vi tại $x_0$ và:  
$$df(x_0) = f'(x_0) \Delta x$$
Với biến độc lập $x$, quy ước $dx = \Delta x$, nên:  
$$dy = f'(x) dx$$

**Chú ý 1.11**: Khái niệm "có đạo hàm" và khái niệm "có vi phân" (hay khả vi) là hai khái
niệm khác nhau. Tuy nhiên, vì tính tương đương giữa hai khái niệm này đối với hàm số
một biến số mà nhiều người hiểu nhầm rằng chúng là một. Trong chương 3 của học phần
Giải tích I này, chúng ta sẽ thấy hai khái niệm này là khác nhau đối với hàm số nhiều
biến số.
  
#### Tính bất biến của vi phân cấp 1

Cho $y = f(x)$ là một hàm số khả vi. Khi đó, ta đã biết nếu $x$ là biến số độc lập thì
$$df = f'(x) dx$$

**Định lý 1.29** Nếu $x$ không phải là một biến số độc lập mà $x = x(t)$ là một hàm số phụ thuộc vào biến số $t$ thì công thức
$$df = f'(x) dx$$
vẫn đúng.

#### Ý nghĩa hình học  

![](../extracted/graphs/graph_47_0.png)

Khi x thay đổi từ $x_0$ đến $x_0$ + $\Delta$ x thì

i) $df(x_0) = \overline{MT}$ thể hiện sự thay đổi của đường thẳng tiếp tuyến

ii) $\Delta y = f(x_0 + \Delta x) - f(x_0)$ thể hiện sự thay đổi của đường cong $y = f(x)$.

#### Công thức vi phân  
- $d(u \pm v) = du \pm dv$  
- $d(uv) = u  dv + v  du$  
- $d\left(\dfrac{u}{v}\right) = \dfrac{v  du - u  dv}{v^2}$

#### Ví dụ
Tìm $f'(x)$ biết:  
$$\dfrac{d}{dx}[f(2016x)] = x^2$$

**Lời giải:**  
Đặt $u = 2016x$. Theo định lý hàm hợp:  
$$\frac{d}{dx}[f(u)] = f'(u) \cdot u' = f'(2016x) \cdot 2016 = x^2 \Rightarrow f'(2016x) = \frac{x^2}{2016}$$

Đặt $t = 2016x \Rightarrow x = \dfrac{t}{2016}$:  
$$

f'(t) = \frac{(t/2016)^2}{2016} = \frac{t^2}{2016^3} \Rightarrow \boxed{f'(x) = \dfrac{x^2}{2016^3}}$$  

#### Ứng dụng tính gần đúng  
$$f(x_0 + \Delta x) \approx f(x_0) + f'(x_0) \Delta x$$

#### Ví dụ 
Tính gần đúng:  
a) $\sqrt[3]{7.97}$
b) $\sqrt[3]{8.03}$

**Lời giải:**  
Xét $f(x) = \sqrt[3]{x}$, $f'(x) = \dfrac{1}{3} x^{-2/3}$.  
a) Chọn $x_0 = 8$, $\Delta x = -0.03$:  
$$f(7.97) \approx f(8) + f'(8) \cdot (-0.03) = 2 + \frac{1}{3} \cdot \frac{1}{4} \cdot (-0.03) = 2 - 0.0025 = \boxed{1.9975}$$

b) Chọn $x_0 = 8$, $\Delta x = 0.03$:  
$$f(8.03) \approx 2 + \frac{1}{12} \cdot 0.03 = 2 + 0.0025 = \boxed{2.0025}$$


### 8.7 Đạo hàm cấp cao

#### Định nghĩa 1.22  
- $f'(x)$: đạo hàm cấp 1.  
- $f''(x) = [f'(x)]'$: đạo hàm cấp 2.  
- $f^{(n)}(x) = \left[f^{(n-1)}(x)\right]'$: đạo hàm cấp $n$.

#### Định lý 1.30 (Các phép toán trên đạo hàm cao cấp)
Cho $u,v$ khả vi đến cấp $n$.  
i) $(u \pm v)^{(n)} = u^{(n)} \pm v^{(n)}$  
ii) **Công thức Leibniz**:  
$$(u \cdot v)^{(n)} = \sum_{k=0}^{n} C_n^k  u^{(n-k)}  v^{(k)}$$

#### Đạo hàm cấp cao của hàm cơ bản  
1. $(x^\alpha)^{(n)} = \alpha(\alpha-1)\cdots(\alpha-n+1) x^{\alpha-n}$  
2. $[(1+x)^\alpha]^{(n)} = \alpha(\alpha-1)\cdots(\alpha-n+1) (1+x)^{\alpha-n}$  
3. $\left( \dfrac{1}{1+x} \right)^{(n)} = (-1)^n \dfrac{n!}{(1+x)^{n+1}}$  
4. $\left( \dfrac{1}{1-x} \right)^{(n)} = \dfrac{n!}{(1-x)^{n+1}}$  
5. $(\sin x)^{(n)} = \sin \left( x + \dfrac{n\pi}{2} \right)$  
6. $(\cos x)^{(n)} = \cos \left( x + \dfrac{n\pi}{2} \right)$  
7. $(a^x)^{(n)} = a^x (\ln a)^n$  
8. $(\ln x)^{(n)} = (-1)^{n-1} \dfrac{(n-1)!}{x^n}$  

#### Ví dụ
Tính $y^{(10)}(0)$:  
a) $y = e^{x^2}$  
b) $y = \arctan x$  

**Lời giải:**  
a) $y' = 2x e^{x^2} = 2x y$. Đạo hàm cấp $n$:  
$$y^{(n+1)} = [2x y]^{(n)} = 2x y^{(n)} + 2n y^{(n-1)}$$
Tại $x=0$: $y^{(n+1)}(0) = 2n y^{(n-1)}(0)$.  
Truy hồi:  
$$y^{(10)}(0) = 2\cdot9\cdot y^{(8)}(0) = \cdots = 2^5 \cdot (9\cdot7\cdot5\cdot3\cdot1) \cdot 1 = \boxed{30240}$$

b) $y' = \dfrac{1}{1+x^2}$. Đạo hàm cấp $n$:  
$$(1+x^2) y^{(n+1)} + 2n x y^{(n)} + n(n-1) y^{(n-1)} = 0$$
Tại $x=0$: $y^{(n+1)}(0) = -n(n-1) y^{(n-1)}(0)$.  
Tính $y''(0) = 0$ nên $\boxed{y^{(10)}(0) = 0}$  

#### Ví dụ
Tính $f^{(10)}(1)$ với $f(x) = x^9 \ln x$.  

**Lời giải:**  
Xét $g(x) = x^n \ln x$. Đạo hàm cấp $n+1$:  
$$g^{(n+1)}(x) = \dfrac{n!}{x}$$
Với $n=9$: $f^{(10)}(x) = \dfrac{9!}{x} \Rightarrow \boxed{f^{(10)}(1) = 9! = 362880}$  


### 8.8 Vi phân cấp cao

#### Định nghĩa 1.23  
- $df = f'(x) dx$: vi phân cấp 1.  
- $d^2 f = d(df)$: vi phân cấp 2.  
- $d^n f = d(d^{n-1} f)$: vi phân cấp $n$.

#### Biểu thức  
Nếu $x$ là biến độc lập:  
$$d^n f = f^{(n)}(x)  dx^n$$

#### Không bất biến  
Nếu $x = x(t)$, thì:  
$$d^2 f = f''(x) (dx)^2 + f'(x) d^2 x \neq f''(x) dx^2$$

#### Ví dụ
Cho $y = x^3$, $x = t^2$. Chứng minh $d^2 y \neq y^{(2)} dx^2$.  

**Lời giải:**  
- Tính trực tiếp: $y = t^6 \Rightarrow dy = 6t^5 dt \Rightarrow d^2 y = 30t^4 (dt)^2 + 6t^5 d^2 t$  
- Tính qua $x$: $y'' dx^2 = 6x (dx)^2 = 6t^2 (2t dt)^2 = 24t^4 (dt)^2$  
Rõ ràng $\boxed{30t^4 (dt)^2 + 6t^5 d^2 t \neq 24t^4 (dt)^2}$ nên $d^2 y \neq y^{(2)} dx^2$.

### 8.10 Đọc thêm: Về khái niệm vi phân

Vi phân có lẽ là một khái niệm trừu tượng và dễ gây hiểu nhầm nhất trong môn Giải tích I. Theo sự hiểu biết của tác giả thì có nhiều cách tiếp cận khác nhau đối với phép tính vi phân.

1) **Cách tiếp cận của Leibniz**:  
   Người đầu tiên đưa ra khái niệm vi phân có lẽ là Leibniz, khi ông coi $dy$ là một đại lượng vô cùng bé thể hiện sự thay đổi của hàm số $y = f(x)$ tương ứng với sự thay đổi vô cùng bé $dx$ của biến số $x$, nghĩa là ông định nghĩa:  
   $f'(x) := \frac{dy}{dx}$.  
   Kí hiệu $\frac{dy}{dx}$ này là kí hiệu của Leibniz cho đạo hàm của hàm số $f(x)$. Mặc dù có nhiều chỉ trích, nó vẫn được dùng đến ngày nay. Chú ý rằng kí hiệu $f'(x)$ là của d'Alambert.

2) **Cải tiến của Cauchy**:  
   Cauchy cải tiến ý tưởng của Leibniz như sau. Ông định nghĩa đạo hàm:  
   $f'(x) := \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}$  
   là giới hạn của tỉ số giữa số gia hàm số và số gia đối số. Sau đó, ông định nghĩa vi phân:  
   $dy = f'(x)dx$,  
   như một hàm số của hai biến $x$ và $dx$, trong đó $dx$ là một biến số mới có thể nhận giá trị tùy ý (không bắt buộc là vô cùng bé).

3) **Tiếp cận hiện đại**:  

#### Định nghĩa 1.24  
Cho hàm số $f(x)$ có đạo hàm tại $x_0$. Ánh xạ $d_{x_0}f$, kí hiệu:  
$d_{x_0}f: \mathbb{R} \to \mathbb{R}$,  
$h \mapsto f'(x_0)h$  
được gọi là **vi phân của $f$ tại $x_0$**.  

i) Vi phân là một hàm số $df$ của hai biến $x_0$ và $h$:  
$d_{x_0}f(h) = f'(x_0)h$,  
trong đó $h$ là biến số mới nhận giá trị tùy ý.  

ii) Kí hiệu $\text{Id}$ là ánh xạ đồng nhất, ta có:  
$d_{x_0}(\text{Id})(h) = h$ hay $d_{x_0}(\text{Id}) = \text{Id}$.  

iii) Lạm dụng kí hiệu: Đặt $x := \text{Id}$ (ánh xạ đồng nhất). Khi đó:  
$d_{x_0}x = \text{Id}$ (không phụ thuộc $x_0$) nên kí hiệu $dx$.  
Suy ra:  
$d_{x_0}f = f'(x_0)dx$.  
Bỏ $x_0$ và thay $f'(x_0)$ bởi $f'(x)$, ta có biểu thức cô đọng:  
$df = f'(x)dx$.  
