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

  
#### Chú ý 1.1: 
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

  
#### Chú ý 1.2 
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


#### Chú ý 1.3
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


#### Chú ý 1.4

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