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

  
#### Chú ý: 
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

  
#### Chú ý
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


#### ví dụ (Ngụy biện toán học). 
Chứng minh rằng $0 = 2$.

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


#### Chú ý
Các phép toán trên giới hạn sau không thực hiện được (dạng vô định): $\,\infty - \infty,\; 0 \times \infty,\; \dfrac{\infty}{\infty},\; \dfrac{0}{0}\,.$

### 4.2 Các tiêu chuẩn tồn tại giới hạn


#### Định lý 1.4 (Tiêu chuẩn kẹp)

Giả sử:

i) $a_n \le b_n \le c_n$ với mọi $n \in \mathbb{N}$, hoặc với mọi $n \ge K$ nào đó, với $K \in \mathbb{N}$.

ii) $\lim_{n\to+\infty} a_n = \lim_{n\to+\infty} c_n = L$.

Khi đó, $\lim_{n\to+\infty} b_n = L$.


#### Định lý 1.5 (Tiêu chuẩn đơn điệu bị chặn)

Mọi dãy số đơn điệu tăng và bị chặn trên (tương ứng, đơn điệu giảm và bị chặn dưới) đều hội tụ.


#### ví dụ

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


#### Chú ý

Giới hạn $\lim_{n\to+\infty}\left(1+\frac{1}{n}\right)^n$ là một số vô tỉ, được kí hiệu là $e$. Nó có giá trị xấp xỉ $2.71$.


#### ví dụ

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

#### Chú ý
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

#### Mối liên hệ giữa giới hạn và VCB:  
$\lim_{x \to a} f(x) = \ell \iff f(x) = \ell + \alpha(x)$,  
trong đó $\alpha(x)$ là VCB khi $x \to a$.

#### Tính chất VCB:  
1. Tổng hai VCB là một VCB.  
2. Tích của VCB với hàm bị chặn là VCB.  
3. Tích các VCB là VCB.  

#### Chú ý 
Thương hai VCB là dạng vô định $\frac{0}{0}$.

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

#### Chú ý 
Không được thay tương đương cho **hiệu** hai VCB tương đương.  
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

#### Chú ý 
Một số dạng vô định (như $\lim_{x \to 0} \frac{x - \sin x}{x^3}$, $\lim_{x \to 0^+} x^{\sin x}$) cần dùng quy tắc L'Hospital hoặc khai triển Maclaurin.  

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


#### Chú ý

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

#### Chú ý
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

#### Chú ý 
Khái niệm "có đạo hàm" và khái niệm "có vi phân" (hay khả vi) là hai khái
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
   $$f'(x) := \frac{dy}{dx}$$
   Kí hiệu $\frac{dy}{dx}$ này là kí hiệu của Leibniz cho đạo hàm của hàm số $f(x)$. Mặc dù có nhiều chỉ trích, nó vẫn được dùng đến ngày nay. Chú ý rằng kí hiệu $f'(x)$ là của d'Alambert.

2) **Cải tiến của Cauchy**:  
   Cauchy cải tiến ý tưởng của Leibniz như sau. Ông định nghĩa đạo hàm:  
   $$f'(x) := \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}$$
   là giới hạn của tỉ số giữa số gia hàm số và số gia đối số. Sau đó, ông định nghĩa vi phân:  
   $$dy = f'(x)dx$$
   như một hàm số của hai biến $x$ và $dx$, trong đó $dx$ là một biến số mới có thể nhận giá trị tùy ý (không bắt buộc là vô cùng bé).

3) **Tiếp cận hiện đại**:  

#### Định nghĩa 1.24  
Cho hàm số $f(x)$ có đạo hàm tại $x_0$. Ánh xạ $d_{x_0}f$, kí hiệu:  
$$d_{x_0}f: \mathbb{R} \to \mathbb{R},$$
$$h \mapsto f'(x_0)h$$
được gọi là **vi phân của $f$ tại $x_0$**.  

i) Vi phân là một hàm số $df$ của hai biến $x_0$ và $h$:  
$d_{x_0}f(h) = f'(x_0)h$,  
trong đó $h$ là biến số mới nhận giá trị tùy ý.  

ii) Kí hiệu $\text{Id}$ là ánh xạ đồng nhất, ta có:  $d_{x_0}(\text{Id})(h) = h$ hay $d_{x_0}(\text{Id}) = \text{Id}$.  

iii) Lạm dụng kí hiệu: Đặt $x := \text{Id}$ (ánh xạ đồng nhất). Khi đó:  
$d_{x_0}x = \text{Id}$ (không phụ thuộc $x_0$) nên kí hiệu $dx$. Suy ra: $d_{x_0}f = f'(x_0)dx$.  Bỏ $x_0$ và thay $f'(x_0)$ bởi $f'(x)$, ta có biểu thức cô đọng:  
$$df = f'(x)dx$$

Mình đã chuẩn hóa lại văn bản: sửa lỗi chính tả, dấu tiếng Việt, ký hiệu, và các công thức; giữ nguyên logic. Tất cả công thức đều đặt trong dấu $ $ và chèn xuống dòng đôi để hiển thị markdown đẹp.



## §9. CÁC ĐỊNH LÝ VỀ HÀM KHẢ VI VÀ ỨNG DỤNG

### 9.1 Các định lý về hàm khả vi

#### Định nghĩa 1.25 (Cực trị của hàm số)

Cho hàm số $f(x)$ liên tục trên $(a,b)$. Ta nói hàm số đạt cực trị tại điểm $x_0\in (a,b)$ nếu tồn tại lân cận $U(x_0)\subset (a,b)$ sao cho $f(x)-f(x_0)$ không đổi dấu với mọi $x\in U(x_0)\setminus \{x_0\}$.

- Nếu $f(x)-f(x_0)>0$ thì ta nói hàm số đạt cực tiểu tại $x_0$.

- Nếu $f(x)-f(x_0)<0$ thì ta nói hàm số đạt cực đại tại $x_0$.



#### Định lý 1.31 (Định lý Fermat)

Cho $f(x)$ liên tục trên khoảng $(a,b)$. Nếu hàm số đạt cực trị tại điểm $x_0\in (a,b)$ và có đạo hàm tại $x_0$ thì $f'(x_0)=0$.

Chứng minh.

Nếu hàm số đạt cực đại tại $x_0$ thì theo định nghĩa tồn tại lân cận $U(x_0)$ sao cho $f(x)-f(x_0)<0$ với mọi $x\in U(x_0)$. Do đó, với $h$ đủ nhỏ sao cho $x_0+h\in U(x_0)$ ta có $f(x_0+h)-f(x_0)<0$.

- $f'_+(x_0)=\lim_{h\to 0^+}\frac{f(x_0+h)-f(x_0)}{h}\le 0$.

- $f'_-(x_0)=\lim_{h\to 0^-}\frac{f(x_0+h)-f(x_0)}{h}\ge 0$.

Do giả thiết tồn tại $f'(x_0)$ nên $f'_+(x_0)=f'_-(x_0)$, điều này chỉ xảy ra khi $f'_+(x_0)=f'_-(x_0)=0$. Trường hợp cực tiểu là tương tự.


#### Ví dụ
Cho $f$ là hàm khả vi trên $\mathbb{R}$ và thỏa $f'(2)<\lambda<f'(3)$. Chứng minh tồn tại $x_0\in (2,3)$ sao cho $f'(x_0)=\lambda$.

**[Lời giải]**

Xét $g(x)=f(x)-\lambda x$.

i) $g'(2)=f'(2)-\lambda<0$, do đó tồn tại $x_1\in (2,3)$ sao cho $g(x_1)<g(2)$. Nếu không thì $g'_+(2)=\lim_{x\to 2^+}\frac{g(x)-g(2)}{x-2}\ge 0$.

ii) $g'(3)=f'(3)-\lambda>0$, do đó tồn tại $x_2\in (2,3)$ sao cho $g(x_2)<g(3)$. Nếu không thì $g'_-(3)=\lim_{x\to 3^-}\frac{g(x)-g(3)}{x-3}\le 0$.

iii) Vậy $g(x)$ đạt cực tiểu tại một điểm $x_0\in (2,3)$, suy ra $g'(x_0)=0\Rightarrow f'(x_0)=\lambda$.



#### Định lý 1.32 (Định lý Rolle)

Nếu hàm số $f(x)$:

i) Liên tục trên $[a,b]$,

ii) Có đạo hàm trên $(a,b)$,

iii) Thỏa $f(a)=f(b)$,

thì tồn tại ít nhất một điểm $c\in (a,b)$ sao cho $f'(c)=0$.

Chứng minh.

Do $f$ liên tục trên $[a,b]$ nên đạt GTLN và GTNN trên $[a,b]$.

- Nếu $f$ là hằng trên $[a,b]$ thì $f'(x)=0$ với mọi $x\in (a,b)$.

- Nếu tồn tại $x\in (a,b)$ sao cho $f(x)>f(a)=f(b)$ thì GTLN đạt tại một $c\in (a,b)$, theo Định lý Fermat suy ra $f'(c)=0$.

- Nếu tồn tại $x\in (a,b)$ sao cho $f(x)<f(a)=f(b)$ thì GTNN đạt tại một $c\in (a,b)$, theo Định lý Fermat suy ra $f'(c)=0$.



#### Ví dụ 
Cho $f(x)=(x-1)(x^2-2)(x^2-3)$. Phương trình $f'(x)=0$ có bao nhiêu nghiệm thực? Giải thích.

**[Lời giải]**

Phương trình $f(x)=0$ có 5 nghiệm $x=-\sqrt 3,\,-\sqrt 2,\,1,\,\sqrt 2,\,\sqrt 3$.

i) Vì $f(-\sqrt 3)=f(-\sqrt 2)=0$ nên theo Rolle tồn tại $x_1\in (-\sqrt 3,-\sqrt 2)$ sao cho $f'(x_1)=0$.

ii) Vì $f(-\sqrt 2)=f(1)=0$ nên tồn tại $x_2\in (-\sqrt 2,1)$ sao cho $f'(x_2)=0$.

iii) Vì $f(1)=f(\sqrt 2)=0$ nên tồn tại $x_3\in (1,\sqrt 2)$ sao cho $f'(x_3)=0$.

iv) Vì $f(\sqrt 2)=f(\sqrt 3)=0$ nên tồn tại $x_4\in (\sqrt 2,\sqrt 3)$ sao cho $f'(x_4)=0$.

Vậy $f'(x)=0$ có ít nhất 4 nghiệm. Mặt khác $f'(x)$ là đa thức bậc 4 nên có nhiều nhất 4 nghiệm. Kết luận: có đúng 4 nghiệm phân biệt.



#### Ví dụ
Cho $a,b,c\in \mathbb{R}$ thỏa $a+b+c=0$. Chứng minh rằng:

a) Phương trình $3ax^2+4bx+5c=0$ có ít nhất một nghiệm thuộc $(1,+\infty)$.

b) Phương trình $2ax^2+3bx+4c=0$ có ít nhất một nghiệm thuộc $(1,+\infty)$.

**[Lời giải]**

a) Xét $f(x)=c x^5+b x^4+a x^3$ thỏa điều kiện Rolle trên $[0,1]$ vì $f(0)=0$ và $f(1)=a+b+c=0$. Do đó tồn tại $x_0\in (0,1)$ sao cho $f'(x_0)=5c x_0^4+4b x_0^3+3a x_0^2=0$. Suy ra $3a(1/x_0)^2+4b(1/x_0)+5c=0$. Vậy phương trình $3ax^2+4bx+5c=0$ có nghiệm $x=1/x_0\in (1,+\infty)$.

b) Xét $f(x)=c x^4+b x^3+a x^2$ thỏa điều kiện Rolle trên $[0,1]$ vì $f(0)=0$ và $f(1)=a+b+c=0$. Do đó tồn tại $x_0\in (0,1)$ sao cho $f'(x_0)=4c x_0^3+3b x_0^2+2a x_0=0$. Suy ra $2a(1/x_0)^2+3b(1/x_0)+4c=0$. Vậy phương trình $2ax^2+3bx+4c=0$ có nghiệm $x=1/x_0\in (1,+\infty)$.



#### Ví dụ 
Cho $f$ liên tục trên $[a,b]$ và thỏa $ \int_a^b f(x)\,dx=0$. Chứng minh rằng tồn tại $c\in (a,b)$ sao cho $2017\int_a^c f(x)\,dx=f(c)$.

**[Lời giải]**

Đặt $g(x)=\int_a^x f(t)\,dt$. Khi đó $g$ liên tục trên $[a,b]$, khả vi trên $(a,b)$ và $g(a)=g(b)=0$. Xét $h(x)=e^{-2017x}g(x)$, $h$ liên tục trên $[a,b]$, khả vi trên $(a,b)$ và $h(a)=h(b)=0$. Áp dụng Rolle cho $h$ trên $[a,b]$, tồn tại $c\in (a,b)$ sao cho $h'(c)=0$, tức $g'(c)e^{-2017c}-2017 e^{-2017c}g(c)=0$. Suy ra $g'(c)-2017 g(c)=0$, hay $f(c)=2017\int_a^c f(x)\,dx$.



#### Ví dụ
Giả sử $f:[0,1]\to \mathbb{R}$ khả vi và $ \int_0^1 f(x)\,dx=\int_0^1 x f(x)\,dx$. Chứng minh rằng tồn tại $c\in (0,1)$ sao cho $f(c)=2018\int_0^c f(x)\,dx$.

**Chứng minh**

i) Xét $F(x)=x\int_0^x f(t)\,dt-\int_0^x t f(t)\,dt$. Khi đó $F$ khả vi trên $[0,1]$ và $F(0)=F(1)=0$. Theo Rolle, tồn tại $x_0\in (0,1)$ sao cho $F'(x_0)=0$. Ta có $F'(x)=\int_0^x f(t)\,dt$, nên $\int_0^{x_0} f(t)\,dt=0$.

ii) Đặt $G(x)=e^{-2018x}\int_0^x f(t)\,dt$. Khi đó $G(0)=G(x_0)=0$. Áp dụng Rolle trên $[0,x_0]$ suy ra tồn tại $c\in (0,x_0)$ sao cho $G'(c)=0$, tức $f(c)-2018\int_0^c f(t)\,dt=0$. Vậy $f(c)=2018\int_0^c f(x)\,dx$.



#### Ví dụ
Giả sử $f:[0,1]\to \mathbb{R}$ khả vi và $ \int_0^1 f(x)\,dx=\int_0^1 x f(x)\,dx$. Chứng minh rằng tồn tại $c\in (0,1)$ sao cho $f(c)=2018 f'(c)\int_0^c f(x)\,dx$.

**Chứng minh**

i) Như trên, tồn tại $x_0\in (0,1)$ sao cho $\int_0^{x_0} f(t)\,dt=0$.

ii) Đặt $F(x)=\int_0^x f(t)\,dt$ và $H(x)=e^{-2018 f(x)}F(x)$. Khi đó $H(0)=H(x_0)=0$. Áp dụng Rolle trên $[0,x_0]$, tồn tại $c\in (0,x_0)$ sao cho $H'(c)=0$. Tính $H'(x)=e^{-2018 f(x)}\big(f(x)-2018 f'(x)F(x)\big)$, do đó $H'(c)=0\Rightarrow f(c)=2018 f'(c)\int_0^c f(t)\,dt$.



#### Định lý 1.33 (Định lý Lagrange)

Nếu hàm số $f(x)$:

i) Liên tục trên $[a,b]$,

ii) Có đạo hàm trên $(a,b)$,

thì tồn tại ít nhất một điểm $c\in (a,b)$ sao cho $f'(c)=\frac{f(b)-f(a)}{b-a}$.

Chứng minh.

Xét $h(x)=f(x)-f(a)-\frac{f(b)-f(a)}{b-a}(x-a)$. Khi đó $h$ thỏa các điều kiện của Rolle, nên tồn tại $c\in (a,b)$ sao cho $h'(c)=0$, tức $f'(c)=\frac{f(b)-f(a)}{b-a}$.



#### Ví dụ
Chứng minh các bất đẳng thức sau với $0<a<b$:

a) $\frac{a-b}{1+a^2}<\operatorname{arccot} b-\operatorname{arccot} a<\frac{a-b}{1+b^2}$.

b) $\frac{b-a}{1+b^2}<\operatorname{arctan} b-\operatorname{arctan} a<\frac{b-a}{1+a^2}$.

**[Lời giải]**

a) Áp dụng Lagrange cho $f(x)=\operatorname{arccot} x$ trên $[a,b]$ có $\frac{\operatorname{arccot} b-\operatorname{arccot} a}{b-a}=f'(c)=-\frac{1}{1+c^2}$ với $c\in (a,b)$. Do đó $-\frac{1}{1+a^2}<-\frac{1}{1+c^2}<-\frac{1}{1+b^2}$, suy ra bất đẳng thức đã nêu.

b) Tương tự với $f(x)=\operatorname{arctan} x$ vì $f'(x)=\frac{1}{1+x^2}$.



#### Ví dụ 
Cho $f:(0,+\infty)\to \mathbb{R}$ thỏa $f(x)\le 1$ và $f''(x)\ge 0$ với mọi $x>0$. Chứng minh $f'(x)\le 0$ với mọi $x>0$.

**[Lời giải]**

Giả sử phản chứng, tồn tại $x_0>0$ sao cho $f'(x_0)>0$.

i) Vì $f''(x)\ge 0$ nên $f'$ không giảm, do đó $f'(x)\ge f'(x_0)$ với mọi $x>x_0$.

ii) Áp dụng Lagrange cho $f$ trên $[x_0,x]$ có $f(x)=f(x_0)+f'(c)(x-x_0)\ge f(x_0)+f'(x_0)(x-x_0)$ với $c\in (x_0,x)$.

iii) Vì $f'(x_0)>0$ nên $\lim_{x\to +\infty}\big(f(x_0)+f'(x_0)(x-x_0)\big)=+\infty$, suy ra $\lim_{x\to +\infty} f(x)=+\infty$, mâu thuẫn với $f(x)\le 1$.

Suy ra $f'(x)\le 0$ với mọi $x>0$.



#### Định lý 1.34 (Định lý Cauchy)

Nếu các hàm số $f(x),g(x)$:

i) Liên tục trên $[a,b]$,

ii) Có đạo hàm trên $(a,b)$,

iii) $g'(x)$ không triệt tiêu trên $(a,b)$,

thì tồn tại ít nhất một điểm $c\in (a,b)$ sao cho $\frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f'(c)}{g'(c)}$.

#### Chú ý

a) Định lý Rolle là trường hợp riêng của định lý Lagrange; định lý Lagrange là trường hợp riêng của định lý Cauchy. Các giả thiết trong các định lý này là cần thiết.

b) Dạng khác của định lý Lagrange (công thức số gia hữu hạn): $\Delta f=f'(x_0+\theta\,\Delta x)\,\Delta x$, với $\theta\in (0,1)$.

### 9.2 Các công thức khai triển Taylor, Maclaurin


#### Định lý 1.35 (Công thức Taylor)

Giả sử hàm số $f(x)$:

(i) Có đạo hàm đến cấp $n$ tại $x_0$,

(ii) Có đạo hàm đến cấp $n+1$ trong một lân cận $U_\varepsilon(x_0)$,

khi đó với mọi $x$ đủ gần $x_0$ ta có
$f(x)=f(x_0)+\frac{f'(x_0)}{1!}(x-x_0)+\dots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n+\frac{f^{(n+1)}(c)}{(n+1)!}(x-x_0)^{n+1}$,

trong đó $c$ là một số nằm giữa $x$ và $x_0$.

Nếu $x_0=0$ thì ta có công thức Maclaurin:
$f(x)=f(0)+\frac{f'(0)}{1!}x+\dots+\frac{f^{(n)}(0)}{n!}x^n+\frac{f^{(n+1)}(c)}{(n+1)!}x^{n+1}$  (1.1)

hay
$f(x)=f(0)+\frac{f'(0)}{1!}x+\dots+\frac{f^{(n)}(0)}{n!}x^n+o(x^n)$  (1.2)

ở đó $o(x^n)$ là một vô cùng bé bậc cao hơn $x^n$.



#### Một số khai triển Maclaurin quan trọng

(1) $(1+x)^\alpha=1+\alpha x+\frac{\alpha(\alpha-1)}{2}x^2+\cdots+\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^n+o(x^n)$

(2) $\frac{1}{1+x}=1-x+x^2-\cdots+(-1)^n x^n+o(x^n)$

(3) $\frac{1}{1-x}=1+x+x^2+\cdots+x^n+o(x^n)$

(4) $e^x=1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}+o(x^n)$

(5) $\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}+\cdots+(-1)^n\frac{x^{2n+1}}{(2n+1)!}+o(x^{2n+1})$

(6) $\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}+\cdots+(-1)^n\frac{x^{2n}}{(2n)!}+o(x^{2n})$

(7) $\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots+(-1)^{n-1}\frac{x^n}{n}+o(x^n)$


#### Các phép toán trên khai triển Maclaurin

Giả sử $f(x)=\sum_{n=0}^{+\infty} a_n x^n$ và $g(x)=\sum_{n=0}^{+\infty} b_n x^n$ là các chuỗi Maclaurin hình thức. Khi đó:

1) Phép cộng, trừ:
$f(x)\pm g(x)=\sum_{n=0}^{+\infty}(a_n\pm b_n)x^n$

2) Phép nhân (tích chập):
$f(x)g(x)=\sum_{n=0}^{+\infty} c_n x^n$, với $c_n=\sum_{i=0}^n a_i b_{n-i}$

3) Phép chia: thực hiện tương tự phép chia đa thức.

4) Phép lấy hàm hợp: nếu $g(x)=\sum_{n=1}^{+\infty} b_n x^n$ (với $b_0=0$) và $f(x)=\sum_{k=0}^{+\infty} a_k x^k$ thì
$(f\circ g)(x)=\sum_{n=0}^{+\infty} c_n x^n$, trong đó $c_0=a_0$ và
$c_n=\sum_{k=1}^n a_k \sum_{i_1+\cdots+i_k=n} b_{i_1}\cdots b_{i_k}$



#### Ví dụ 9.10

Tìm khai triển Maclaurin của $f(x)=e^x\sin x$.

**Lời giải**

Dùng phép nhân chuỗi:
$e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$, $\quad \sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots$.

Nhân hai chuỗi và gom hệ số:
$e^x\sin x=x+x^2+\left(\frac{1}{2!}-\frac{1}{3!}\right)x^3+\left(\frac{1}{3!}-\frac{1}{4!}\right)x^4+\cdots$

Ngoài ra, có công thức tổng quát (chứng minh bằng quy nạp/đạo hàm):
$f^{(n)}(x)=(\sqrt{2})^n e^x \sin\!\left(x+\frac{n\pi}{4}\right)$, nên
$e^x\sin x=\sum_{n=0}^{+\infty}\frac{(\sqrt{2})^n\sin\!\left(\frac{n\pi}{4}\right)}{n!}\,x^n$.



#### Ví dụ 9.11

Cho $y=e^x\sin x$. Tính $y^{(6)}(0)$.

**Lời giải**

Dùng công thức tổng quát ở trên: $y^{(6)}(0)=(\sqrt{2})^6\sin\!\left(\frac{6\pi}{4}\right)=8\cdot(-1)=-8$.

Có thể kiểm tra bằng hệ số $x^6$ trong $e^x\sin x$, là $-\frac{1}{90}$, nên $\frac{y^{(6)}(0)}{6!}=-\frac{1}{90}\Rightarrow y^{(6)}(0)=-8$.

#### Định lý 1.36 (Công thức Faà di Bruno)

Với $n\in\mathbb{N}$:
$\frac{d^n}{dx^n}\,f(g(x))=\sum \frac{n!}{m_1!\cdots m_n!}\,f^{(m_1+\cdots+m_n)}(g(x))\prod_{j=1}^n\left(\frac{g^{(j)}(x)}{j!}\right)^{m_j}$,

trong đó tổng lấy trên mọi bộ $(m_1,\ldots,m_n)$ số nguyên không âm thỏa $\sum_{j=1}^n j\,m_j=n$.



#### Hệ quả 1.5 (Chuỗi của hàm hợp)

Nếu $f(x)=\sum_{k=0}^{+\infty} a_k x^k$, $g(x)=\sum_{n=0}^{+\infty} b_n x^n$ và $b_0=0$, thì chuỗi Maclaurin hình thức của $(f\circ g)(x)$ là $\sum_{n=0}^{+\infty} c_n x^n$, với
$c_0=a_0$ và $c_n=\sum_{k=1}^n a_k \sum_{i_1+\cdots+i_k=n} b_{i_1}\cdots b_{i_k}$.



5) Phép lấy đạo hàm

Nếu $f(x)=\sum_{n=0}^{+\infty} a_n x^n$ thì
$f'(x)=\sum_{n=1}^{+\infty} n a_n x^{n-1}=a_1+2a_2 x+3a_3 x^2+\cdots$

#### Ví dụ
đạo hàm chuỗi của $\sin x$ cho $\cos x$; đạo hàm chuỗi của $\ln(1+x)$ cho $\frac{1}{1+x}$.



6) Phép lấy tích phân

Nếu $f(x)=\sum_{n=0}^{+\infty} a_n x^n$ thì
$\int_0^x f(t)\,dt=\sum_{n=0}^{+\infty} a_n \frac{x^{n+1}}{n+1}=a_0 x+a_1\frac{x^2}{2}+a_2\frac{x^3}{3}+\cdots$

#### Ví dụ
từ $\frac{1}{1+x^2}=1-x^2+x^4-\cdots+(-1)^n x^{2n}+\cdots$ suy ra
$\arctan x=\int_0^x \frac{1}{1+t^2}\,dt=x-\frac{x^3}{3}+\frac{x^5}{5}-\cdots+(-1)^n\frac{x^{2n+1}}{2n+1}+\cdots$



#### Ứng dụng của khai triển Maclaurin


1) Tính gần đúng

#### Ví dụ 9.12

Tính gần đúng số $e$ với sai số nhỏ hơn $0{,}0001$.

Lời giải.

Với $x=1$, phần dư Lagrange của $e^x$ thỏa $R_n=\frac{e^c}{(n+1)!}$ với $c\in(0,1)$, nên $R_n<\frac{e}{(n+1)!}$. Cần $\frac{e}{(n+1)!}<10^{-4}\Rightarrow (n+1)!> \frac{e}{10^{-4}}\approx 27183$. Do $8!=40320>27183$, chọn $n=7$.

Vậy $e\approx 1+1+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}+\frac{1}{5!}+\frac{1}{6!}+\frac{1}{7!}$, sai số $<1\cdot 10^{-4}$.



2) Tính giới hạn

#### Ví dụ 9.13

Tính $\lim_{x\to 0}\frac{x-\sin x}{x^3}$.

Lời giải.

$\sin x=x-\frac{x^3}{3!}+o(x^3)\ \Rightarrow\ x-\sin x=\frac{x^3}{6}+o(x^3)$.

Do đó $\lim_{x\to 0}\frac{x-\sin x}{x^3}=\frac{1}{6}$.



#### Ví dụ 9.14 

a) $\lim_{x\to 0}\frac{e^x-\frac{1}{1-x}}{x^2}$.

b) $\lim_{x\to 0}\frac{e^x-\sin x-\cos x}{x^2}$.

**Lời giải**

a) $e^x=1+x+\frac{x^2}{2}+\frac{x^3}{6}+o(x^3)$, $\ \frac{1}{1-x}=1+x+x^2+x^3+o(x^3)$.

Suy ra $e^x-\frac{1}{1-x}=-\frac{x^2}{2}-\frac{5}{6}x^3+o(x^3)$, nên giới hạn bằng $-\frac{1}{2}$.

b) $\sin x+\cos x=1+x-\frac{x^2}{2}-\frac{x^3}{6}+\frac{x^4}{24}+o(x^4)$.

Suy ra $e^x-(\sin x+\cos x)=x^2+\frac{x^3}{3}+o(x^3)$, nên giới hạn bằng $1$.



#### Ví dụ 9.15

Tìm $a,b\in\mathbb{R}$ sao cho:

a) $\lim_{x\to 0}\frac{a x^2+b\ln(\cos x)}{x^4}=1$.

b) $\lim_{x\to 0}\frac{a x+b\sin(\sin x)}{x^3}=1$.

**Lời giải**

a) $\cos x=1-\frac{x^2}{2}+\frac{x^4}{24}+o(x^4)\Rightarrow \ln(\cos x)=-\frac{x^2}{2}-\frac{x^4}{12}+o(x^4)$.

Suy ra $\frac{a x^2+b\ln(\cos x)}{x^4}=\frac{(a-\frac{b}{2})x^2-\frac{b}{12}x^4+o(x^4)}{x^4}$.

Để giới hạn hữu hạn cần $a-\frac{b}{2}=0\Rightarrow a=\frac{b}{2}$. Khi đó giới hạn $=-\frac{b}{12}=1\Rightarrow b=-12$, $a=-6$.

b) $\sin x=x-\frac{x^3}{6}+o(x^3)\Rightarrow \sin(\sin x)=\sin\!\big(x-\frac{x^3}{6}+o(x^3)\big)=x-\frac{x^3}{3}+o(x^3)$.

Suy ra $\frac{a x+b\sin(\sin x)}{x^3}=\frac{(a+b)x-\frac{b}{3}x^3+o(x^3)}{x^3}$.

Cần $a+b=0\Rightarrow a=-b$, và $-\frac{b}{3}=1\Rightarrow b=-3$, do đó $a=3$.



3) Tính đạo hàm cấp cao $f^{(n)}(0)$

#### Ví dụ 9.16

Tính $y^{(10)}(0)$ với:

a) $y(x)=e^{x^2}$.

b) $y(x)=e^{-x^2}$.

c) $y(x)=\arctan x$.

d) $y(x)=\operatorname{arccot} x$.

**Lời giải**

a) $e^{x^2}=1+x^2+\frac{x^4}{2!}+\frac{x^6}{3!}+\frac{x^8}{4!}+\frac{x^{10}}{5!}+\cdots$, nên $\frac{y^{(10)}(0)}{10!}=\frac{1}{5!}\Rightarrow y^{(10)}(0)=\frac{10!}{5!}=30240$.

b) $e^{-x^2}=1-x^2+\frac{x^4}{2!}-\frac{x^6}{3!}+\frac{x^8}{4!}-\frac{x^{10}}{5!}+\cdots$, nên $\frac{y^{(10)}(0)}{10!}=-\frac{1}{5!}\Rightarrow y^{(10)}(0)=-30240$.

c) $\arctan x=x-\frac{x^3}{3}+\frac{x^5}{5}-\cdots$, chỉ có lũy thừa lẻ nên $y^{(10)}(0)=0$.

d) Chọn nhánh $\operatorname{arccot} x=\frac{\pi}{2}-\arctan x$. Khi đó khai triển quanh $0$: $\operatorname{arccot} x=\frac{\pi}{2}-\big(x-\frac{x^3}{3}+\frac{x^5}{5}-\cdots\big)$, chỉ có lũy thừa lẻ (bỏ hằng), nên $y^{(10)}(0)=0$.



#### Ví dụ 9.17

Tính $y^{(10)}(0)$ với:

a) $y(x)=\sin(x^2)$.

b) $y(x)=\cos(x^2)$.

**Lời giải**

a) $\sin(x^2)=\sum_{n=0}^{+\infty}(-1)^n\frac{x^{2(2n+1)}}{(2n+1)!}$, hệ số $x^{10}$ ứng với $2(2n+1)=10\Rightarrow n=2$, nên $\frac{y^{(10)}(0)}{10!}=\frac{1}{5!}\Rightarrow y^{(10)}(0)=30240$.

b) $\cos(x^2)=\sum_{n=0}^{+\infty}(-1)^n\frac{x^{4n}}{(2n)!}$, không có số hạng $x^{10}$ (vì $4n=10$ vô nghiệm nguyên), nên $y^{(10)}(0)=0$.



#### Ví dụ 9.18

Tính $y^{(9)}(0)$ với:

a) $f(x)=\ln(1-x+x^2)$.

b) $g(x)=\ln(1+x+x^2)$.

**Lời giải**

a) $(1-x+x^2)=\frac{1+x^3}{1+x}\Rightarrow \ln(1-x+x^2)=\ln(1+x^3)-\ln(1+x)$.

Hệ số $x^9$: từ $\ln(1+x^3)$ là $\frac{1}{3}$; từ $-\ln(1+x)$ là $-\frac{1}{9}$. Vậy hệ số $x^9$ là $\frac{2}{9}$, nên $\frac{f^{(9)}(0)}{9!}=\frac{2}{9}\Rightarrow f^{(9)}(0)=2\cdot 8!=80640$.

b) $(1+x+x^2)=\frac{1-x^3}{1-x}\Rightarrow \ln(1+x+x^2)=\ln(1-x^3)-\ln(1-x)$.

Hệ số $x^9$: từ $\ln(1-x^3)$ là $-\frac{1}{3}$; từ $-\ln(1-x)$ là $+\frac{1}{9}$. Vậy hệ số $x^9$ là $-\frac{2}{9}$, nên $g^{(9)}(0)=-2\cdot 8!=-80640$.



#### Ví dụ 9.19

a) Tìm khai triển Maclaurin của $f(x)=\arcsin x$.

b) Tính $\arcsin^{(n)}(0)$ (Giữa kì, K59).

**Lời giải**

a) $(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}$. Dùng khai triển nhị thức:
$(1+u)^\alpha=\sum_{n=0}^{+\infty}\binom{\alpha}{n}u^n$.

Với $\alpha=-\tfrac12$ và $u=-x^2$:
$\frac{1}{\sqrt{1-x^2}}=\sum_{n=0}^{+\infty}\frac{(2n-1)!!}{(2n)!!}\,x^{2n}$.

Tích phân từ $0$ đến $x$ cho ta
$\arcsin x=\sum_{n=0}^{+\infty}\frac{(2n-1)!!}{(2n)!!}\cdot \frac{x^{2n+1}}{2n+1}=\sum_{n=0}^{+\infty}\frac{(2n)!}{4^n(n!)^2(2n+1)}\,x^{2n+1}$.

b) Từ chuỗi trên:
$\arcsin^{(2n)}(0)=0,\quad \arcsin^{(2n+1)}(0)=\frac{[(2n)!]^2}{4^n(n!)^2}=[(2n-1)!!]^2$.



#### Ví dụ 9.20

Cho $f(x)=\frac{x}{1+x^3}$. Tính $f^{(10)}(0)$.

**Lời giải**

Viết $f(x)=x\,g(x)$ với $g(x)=\frac{1}{1+x^3}$. Quy tắc Leibniz cho $n\ge 1$:
$f^{(n)}(x)=x\,g^{(n)}(x)+n\,g^{(n-1)}(x)$.

Thay $x=0$, được $f^{(n)}(0)=n\,g^{(n-1)}(0)$. Với $n=10$: $f^{(10)}(0)=10\,g^{(9)}(0)$.

Mà $\frac{1}{1+x^3}=1-x^3+x^6-x^9+\cdots$, hệ số $x^9$ là $-1$, nên $g^{(9)}(0)=-9!$.

Suy ra $f^{(10)}(0)=10\cdot(-9!)=-10!$.

### 9.3 Quy tắc L'Hospital

#### Định lý 1.37 (Quy tắc L'Hospital)

Giả thiết:

i) Các hàm số $f(x),g(x)$ khả vi trong một lân cận (có thể bỏ điểm) của $x_0$, và $g'(x)\ne 0$ trong lân cận đó.

ii) $\lim_{x\to x_0}f(x)=\lim_{x\to x_0}g(x)=0$ (dạng $0/0$), hoặc $\lim_{x\to x_0}f(x)=\pm\infty$, $\lim_{x\to x_0}g(x)=\pm\infty$ (dạng $\infty/\infty$).

Khi đó, nếu tồn tại $\lim_{x\to x_0}\frac{f'(x)}{g'(x)}=A$ (có thể hữu hạn hoặc vô hạn) thì $\lim_{x\to x_0}\frac{f(x)}{g(x)}=A$.

#### Chú ý

- Kết luận vẫn đúng khi thay $x\to x_0$ bởi một trong các quá trình $x\to x_0^+$, $x\to x_0^-$, $x\to +\infty$, $x\to -\infty$.

- Có thể thay điều kiện $\lim_{x\to x_0}f(x)=\lim_{x\to x_0}g(x)=0$ bởi $\lim_{x\to x_0}f(x)=\pm\infty$, $\lim_{x\to x_0}g(x)=\pm\infty$.



Ý tưởng chứng minh

Xét trường hợp đơn giản $g'(x_0)\ne 0$.

1) Nếu $f(x_0)=g(x_0)=0$, với $x\ne x_0$ áp dụng định lý giá trị trung bình dạng Cauchy cho $f$ và $g$ trên đoạn nối $x$ và $x_0$ ta có $\frac{f(x)-f(x_0)}{g(x)-g(x_0)}=\frac{f'(c)}{g'(c)}$ với $c$ nằm giữa $x$ và $x_0$. Khi $x\to x_0$ thì $c\to x_0$, do đó $\lim_{x\to x_0}\frac{f(x)}{g(x)}=\lim_{c\to x_0}\frac{f'(c)}{g'(c)}=A$.

2) Nếu chỉ biết $\lim_{x\to x_0}f(x)=\lim_{x\to x_0}g(x)=0$ (chưa chắc xác định tại $x_0$), đặt $F(x)=0$ nếu $x=x_0$, $F(x)=f(x)$ nếu $x\ne x_0$; tương tự $G(x)=0$ nếu $x=x_0$, $G(x)=g(x)$ nếu $x\ne x_0$. Áp dụng bước 1) cho $F,G$.

3) Trường hợp $x\to \infty$, đặt $y=1/x$ rồi chuyển về $y\to 0$.



#### Ví dụ 9.21

Tính các giới hạn:

a) $\lim_{x\to 0}\frac{\ln(1+x)-\sin x}{x^2}$.

b) $\lim_{x\to 0}\frac{e^{2x}-\sin 2x}{x^2}$.

Lời giải.

a) Áp dụng L'Hospital hai lần:
$\frac{\ln(1+x)-\sin x}{x^2}\xrightarrow{\text{L'H}} \frac{\frac{1}{1+x}-\cos x}{2x}\xrightarrow{\text{L'H}} \frac{-\frac{1}{(1+x)^2}+\sin x}{2}\to -\frac{1}{2}$.

b) Khi $x\to 0$, tử số $e^{2x}-\sin 2x\to 1$, mẫu số $x^2\to 0^+$, nên giới hạn là $+\infty$.



#### Ví dụ 9.22

Tính các giới hạn sau:

a) $\lim_{x\to 0}\frac{x-\sin x}{(\arcsin x)^3}$.

b) $\lim_{x\to 0^+}x^x$.

c) $\lim_{x\to 0^+}x^\alpha\ln x$.

d) $\lim_{x\to \infty}\frac{a^x}{x}$.

Lời giải.

a) Dùng tương đương gần $0$: $x-\sin x\sim \frac{x^3}{6}$, $\arcsin x\sim x$, nên $\frac{x-\sin x}{(\arcsin x)^3}\to \frac{1}{6}$.

b) Viết $x^x=e^{x\ln x}$. Ta có $x\ln x=\frac{\ln x}{1/x}\xrightarrow{\text{L'H}} \frac{1/x}{-1/x^2}=-x\to 0$. Do đó $x^x\to e^0=1$.

c) Với $\alpha\in \mathbb{R}$, viết $x^\alpha\ln x=\frac{\ln x}{x^{-\alpha}}$. Áp dụng L'Hospital khi cần:
- Nếu $\alpha>0$: $\frac{\ln x}{x^{-\alpha}}\xrightarrow{\text{L'H}} \frac{1/x}{-\alpha x^{-\alpha-1}}=-\frac{1}{\alpha}x^\alpha\to 0$, nên giới hạn $=0$.
- Nếu $\alpha=0$: $x^0\ln x=\ln x\to -\infty$.
- Nếu $\alpha<0$: đặt $\beta=-\alpha>0$, $x^\alpha\ln x=x^{-\beta}\ln x\to -\infty$.

d) Giả sử $a>0$. Viết $\frac{a^x}{x}=\frac{e^{(\ln a)x}}{x}$.
- Nếu $a>1$ thì là dạng $\infty/\infty$, áp dụng L'Hospital: $\frac{(\ln a)e^{(\ln a)x}}{1}\to +\infty$.
- Nếu $a=1$ thì $\frac{1}{x}\to 0$.
- Nếu $0<a<1$ thì $a^x\to 0$, nên giới hạn $=0$.


#### Chú ý

- L'Hospital và thay tương đương chỉ là các công cụ đủ để tìm giới hạn. Có những giới hạn không thuộc dạng $0/0$ hay $\infty/\infty$ nên không áp dụng được L'Hospital, ví dụ $\lim_{x\to 0} x^2\sin\!\frac{1}{x}=0$ (dùng kẹp).

- Nên kết hợp khéo léo giữa thay tương đương và L'Hospital.

- Có thể dùng L'Hospital nhiều lần nếu sau mỗi lần vẫn còn dạng vô định thích hợp.



#### Chú ý

Công thức L'Hospital được công bố năm 1696 trong cuốn Analyse des Infiniment Petits của Marquis de l'Hospital (1661–1704), nhưng được khám phá vào năm 1694 bởi Johann Bernoulli (1667–1748). Hai người có thỏa thuận rằng l'Hospital trả tiền để được quyền công bố các phát hiện của Bernoulli trong một thời gian. Trích đoạn thư của l'Hospital gửi Bernoulli ngày 17-3-1694:

"I will be happy to give you a retainer of 300 pounds, beginning with the first of January of this year ... I promise shortly to increase this retainer, which I know is very modest, as soon as my affairs are somewhat straightened out ... I am not so unreasonable as to demand in return all of your time, but I will ask you to give me at intervals some hours of your time to work on what I request and also to communicate to me your discoveries, at the same time asking you not to disclose any of them to others. I ask you even not to send here to Mr. Varignon or to others any copies of the writings you have left with me; if they are published, I will not be at all pleased. Answer me regarding all this ..."

### 9.4 Về một số dạng vô định


Quy tắc L'Hospital, ngoài việc áp dụng để khử các dạng vô định $\frac{0}{0}$, $\frac{\infty}{\infty}$, còn có thể dùng để xử lý các dạng sau bằng cách biến đổi phù hợp trước khi áp dụng.



#### Dạng vô định $0\cdot \infty$

Viết tích về dạng thương để áp dụng L'Hospital, chẳng hạn
$\lim_{x\to x_0} f(x)g(x)=\lim_{x\to x_0}\frac{f(x)}{1/g(x)}$.

#### Ví dụ 9.23

Tính $\lim_{x\to 0^+} x\ln x$.

**Lời giải**

Viết $x\ln x=\frac{\ln x}{1/x}$. Áp dụng L'Hospital:
$\lim_{x\to 0^+}\frac{\ln x}{1/x}=\lim_{x\to 0^+}\frac{1/x}{-1/x^2}=\lim_{x\to 0^+}(-x)=0$.



#### Dạng vô định $\infty-\infty$

Đưa phép trừ về dạng một phân số, bằng quy đồng mẫu số hay đặt nhân tử chung, rồi áp dụng L'Hospital hay thay tương đương.

#### Ví dụ 9.24

Tính $\lim_{x\to 0}\left(\frac{1}{x}-\frac{1}{\sin x}\right)$.

**Lời giải**

Quy đồng:
$\frac{1}{x}-\frac{1}{\sin x}=\frac{\sin x-x}{x\sin x}$.

Dùng L'Hospital hai lần cho tỷ số $\frac{\sin x-x}{x\sin x}$:
Lần 1: $\frac{\cos x-1}{\sin x+x\cos x}$; Lần 2: $\frac{-\sin x}{2\cos x - x\sin x}\to \frac{0}{2}=0$.

Vậy giới hạn bằng $0$.



#### Dạng $\lim_{x\to x_0} A(x)^{B(x)}$

Đặt $f(x)=A(x)^{B(x)}$, lấy log:
$\ln f(x)=B(x)\ln A(x)=\frac{\ln A(x)}{1/B(x)}$.

Nếu xuất hiện dạng $\frac{0}{0}$ hoặc $\frac{\infty}{\infty}$, áp dụng L'Hospital để tìm $\lim \ln f(x)$, rồi suy ra $\lim f(x)=\exp\!\left(\lim \ln f(x)\right)$.

- Nếu $\lim \frac{\ln A(x)}{1/B(x)}$ có dạng $\frac{0}{0}$ thì $\lim A(x)=1$, $\lim B(x)=\infty$ nên là dạng vô định $1^\infty$.

- Nếu $\lim \frac{\ln A(x)}{1/B(x)}$ có dạng $\frac{\infty}{\infty}$ thì hoặc $\lim A(x)=0$, $\lim B(x)=0$ (dạng $0^0$), hoặc $\lim A(x)=\infty$, $\lim B(x)=0$ (dạng $\infty^0$).

Chỉ có ba dạng vô định kiểu lũy thừa: $0^0$, $1^\infty$, $\infty^0$.

#### Trường hợp đặc biệt
Các trường hợp sau không phải dạng vô định và tính trực tiếp:
$0^1=0$, $0^{+\infty}=0$, $0^{-\infty}=+\infty$, $1^0=1$, $1^1=1$, $\infty^1=\infty$, $\infty^\infty=\infty$.

### 9.5 Thay tương đương khi có hiệu hai VCB?

Đây có lẽ là một câu hỏi thú vị và được rất nhiều bạn đọc quan tâm. Chúng ta bắt đầu với một ví dụ sau đây.

  
#### Ví dụ 9.25 
Tính $ \lim_{x\to 0}\frac{e^x-\sin x-\cos x}{x^2} $.

**Lời giải 1 (dùng quy tắc L'Hospital)**

Đặt $N(x)=e^x-\sin x-\cos x$, $D(x)=x^2$. Ta có $N(0)=0$, $D(0)=0$.

Áp dụng L'Hospital lần 1:
$ \frac{N'(x)}{D'(x)}=\frac{e^x-\cos x+\sin x}{2x} \xrightarrow[x\to 0]{} \frac{0}{0} $.

Áp dụng L'Hospital lần 2:
$ \lim_{x\to 0}\frac{N''(x)}{D''(x)}=\lim_{x\to 0}\frac{e^x+\sin x+\cos x}{2}=\frac{1+0+1}{2}=1 $.

Vậy $ \lim_{x\to 0}\frac{e^x-\sin x-\cos x}{x^2}=1 $.

  
**Lời giải 2 (dùng khai triển Maclaurin)**

$ e^x=1+x+\frac{x^2}{2}+\frac{x^3}{6}+o(x^3) $  
$ \sin x=x-\frac{x^3}{6}+o(x^3) $  
$ \cos x=1-\frac{x^2}{2}+o(x^2) $

Suy ra
$ e^x-\sin x-\cos x=\big(1+x+\frac{x^2}{2}+\frac{x^3}{6}\big)-\big(x-\frac{x^3}{6}\big)-\big(1-\frac{x^2}{2}\big)+o(x^3)=x^2+\frac{x^3}{3}+o(x^3) $.

Do đó
$ \frac{e^x-\sin x-\cos x}{x^2}=1+\frac{x}{3}+o(x)\xrightarrow[x\to 0]{}1 $.

  
Sai lầm thường gặp khi “thay tương đương” với dấu cộng, trừ

Có bạn thay $(e^x-1)\sim x$ và $\sin x\sim x$ nên viết $(e^x-1)-\sin x\sim x-x=0$, từ đó suy ra tử số $\sim \frac{x^2}{2}$ và giới hạn bằng $ \frac{1}{2} $ (SAI). Thực tế
$ (e^x-1)-\sin x=\frac{x^2}{2}+o(x^2)\sim \frac{x^2}{2} $,
nên nếu thay $x$ cho cả $e^x-1$ và $\sin x$ thì ta đã làm mất số hạng bậc hai quyết định giới hạn.

  
#### Chú ý 1.17

Nếu $\alpha_1(x)$, $\alpha_2(x)$, $\beta_1(x)$, $\beta_2(x)$ là các VCB khi $x\to x_0$ và $\alpha_1(x)\sim \alpha_2(x)$, $\beta_1(x)\sim \beta_2(x)$ thì:

- $ \alpha_1(x)\beta_1(x)\sim \alpha_2(x)\beta_2(x) $.

- $ \lim_{x\to x_0}\frac{\alpha_1(x)}{\beta_1(x)}=\lim_{x\to x_0}\frac{\alpha_2(x)}{\beta_2(x)} $.

- Nhưng chưa chắc $ \alpha_1(x)\pm \beta_1(x)\sim \alpha_2(x)\pm \beta_2(x) $. Chẳng hạn, $\sin x\sim x$, $\tan x\sim x$ khi $x\to 0$, nhưng $ \tan x-\sin x\sim \frac{1}{2}x^3 $.

  
Vậy có thay tương đương được trong biểu thức có dấu $ \pm $ hay không? Muốn biết $ \alpha_1(x)-\beta_1(x) $ có tương đương với $ \alpha_2(x)-\beta_2(x) $ hay không, ta xét
$ \lim_{x\to a}\frac{\alpha_1(x)-\beta_1(x)}{\alpha_2(x)-\beta_2(x)} $.
Chia thành các trường hợp:

1) Nếu $\alpha_1$ là VCB bậc cao hơn $\beta_1$ thì $ \lim\frac{\alpha_1}{\beta_1}=\lim\frac{\alpha_2}{\beta_2}=0 $. Khi đó
$ \frac{\alpha_1-\beta_1}{\alpha_2-\beta_2}=\frac{\frac{\alpha_1}{\beta_1}-1}{\frac{\alpha_2}{\beta_2}-1}\cdot \frac{\beta_1}{\beta_2}\to \frac{0-1}{0-1}\cdot 1=1 $,
nên $ \alpha_1-\beta_1\sim \alpha_2-\beta_2 $.

2) Nếu $\beta_1$ là VCB bậc cao hơn $\alpha_1$ thì tương tự ta cũng được $ \alpha_1-\beta_1\sim \alpha_2-\beta_2 $.

3) Nếu $\alpha_1$ và $\beta_1$ cùng bậc nhưng không tương đương, đặt $ \lim\frac{\alpha_1}{\beta_1}=A\neq 1 $. Khi đó
$ \frac{\alpha_1-\beta_1}{\alpha_2-\beta_2}=\frac{\frac{\alpha_1}{\beta_1}-1}{\frac{\alpha_2}{\beta_2}-1}\cdot \frac{\beta_1}{\beta_2}\to \frac{A-1}{A-1}\cdot 1=1 $,
nên $ \alpha_1-\beta_1\sim \alpha_2-\beta_2 $.

4) Nếu $\alpha_1$ và $\beta_1$ tương đương thì $ \lim\frac{\alpha_1}{\beta_1}=1 $, khi đó
$ \lim\frac{\alpha_1-\beta_1}{\alpha_2-\beta_2}=\lim \frac{\frac{\alpha_1}{\beta_1}-1}{\frac{\alpha_2}{\beta_2}-1}\cdot \frac{\beta_1}{\beta_2} $ là dạng vô định $ \frac{0}{0} $, không kết luận được.

5) Nếu $\alpha_1$ và $\beta_1$ không so sánh được, thì $ \alpha_1-\beta_1 $ và $ \alpha_2-\beta_2 $ có thể cũng không so sánh được.

  
Kết luận: Nếu $\alpha_1$, $\alpha_2$, $\beta_1$, $\beta_2$ là các VCB khi $x\to x_0$ và $\alpha_1\sim \alpha_2$, $\beta_1\sim \beta_2$ thì
$ \alpha_1-\beta_1\sim \alpha_2-\beta_2 $ ngoại trừ trường hợp $\alpha_1$ và $\beta_1$ là các VCB tương đương hoặc không so sánh được với nhau.

Ví dụ, không thay tương đương được trong biểu thức $ \tan x-\sin x $ vì $ \tan x\sim \sin x $, nhưng vẫn thay tương đương được trong $ \tan 2x-\sin x\sim 2x-x=x $ hoặc $ \sin x-\tan^2 x\sim x-x^2\sim x $.

  
Quay trở lại Ví dụ 9.25, sai lầm là ở chỗ đã thay $(e^x-1)-\sin x\sim x-x=0$, dẫn đến $(e^x-1)-\sin x+(1-\cos x)\sim \frac{x^2}{2}$ và tính ra giới hạn $ \frac{1}{2} $ (SAI). Thực tế $ e^x-1\sim \sin x $, nên $(e^x-1)-\sin x$ là một VCB bậc cao hơn và
$ (e^x-1)-\sin x=\frac{x^2}{2}+o(x^2)\sim \frac{x^2}{2} $.
Khi thay $x$ cho cả hai hạng, ta đã làm mất số hạng $ \frac{x^2}{2} $ quyết định.

  
#### Ví dụ 9.26
Tính $ \lim_{x\to 0}\frac{e^x-\cos x-\ln(1+x)}{x^2} $.

Gợi ý: Nếu thay tương đương nông sẽ cho kết quả $ \frac{1}{2} $ (SAI). Dùng L'Hospital hoặc Maclaurin được $ \frac{3}{2} $ (ĐÚNG).

- Maclaurin: $ e^x=1+x+\frac{x^2}{2}+o(x^2) $, $ \cos x=1-\frac{x^2}{2}+o(x^2) $, $ \ln(1+x)=x-\frac{x^2}{2}+o(x^2) $. Suy ra tử số $ = \frac{3}{2}x^2+o(x^2) $, nên giới hạn $ =\frac{3}{2} $.

- L'Hospital: Hai lần đạo hàm cho
$ \lim\frac{e^x+\cos x+\frac{1}{(1+x)^2}}{2}=\frac{1+1+1}{2}=\frac{3}{2} $.

  
### 9.6 Hiệu hai VCB tương đương

Trong mục trước, chúng ta biết rằng không thay tương đương được trong biểu thức $ \alpha(x)-\beta(x) $ nếu $\alpha(x)$ và $\beta(x)$ là các VCB tương đương. Vậy hiệu của hai VCB tương đương là gì?

  
#### Bổ đề 1.1. Hiệu của hai VCB tương đương là một VCB bậc cao hơn cả hai VCB đó.

Chứng minh. Giả sử $ \alpha(x)\sim \beta(x) $ khi $ x\to x_0 $. Khi đó,
$ \lim_{x\to x_0}\frac{\alpha(x)-\beta(x)}{\alpha(x)}=1-\lim_{x\to x_0}\frac{\beta(x)}{\alpha(x)}=1-1=0 $.
Vậy theo định nghĩa, $ \alpha(x)-\beta(x) $ là một VCB bậc cao hơn $ \alpha(x) $ (và tương tự so với $ \beta(x) $).

  
#### Ví dụ 9.27 (Một số ví dụ về hiệu hai VCB tương đương)

- a) $ x-\sin x\sim \frac{x^3}{6} $

- b) $ x-\tan x\sim -\frac{x^3}{3} $

- c) $ x-\arcsin x\sim -\frac{x^3}{6} $

- d) $ x-\arctan x\sim \frac{x^3}{3} $

- e) $ \sin x-\tan x\sim -\frac{x^3}{2} $

- f) $ \sin x-\arcsin x\sim -\frac{x^3}{3} $

- g) $ \sin x-\arctan x\sim \frac{x^3}{6} $

- h) $ \tan x-\arcsin x\sim \frac{x^3}{6} $

- i) $ \tan x-\arctan x\sim \frac{2x^3}{3} $

- j) $ \arcsin x-\arctan x\sim \frac{x^3}{2} $

- k) $ x-(e^x-1)\sim -\frac{x^2}{2} $

- l) $ x-\ln(1+x)\sim \frac{x^2}{2} $

- m) $ (1-\cos x)-\frac{x^2}{2}\sim -\frac{x^4}{24} $

Hiệu hai VCB cùng bậc là một VCB bậc cao hơn cả hai VCB đó, vậy cụ thể “cao hơn” là bao nhiêu? Lấy $\alpha(x)=x$. Ở ví dụ trên ta thấy $ x-\sin x\sim \frac{x^3}{6} $ (cùng bậc với $ x^3 $) còn $ x-(e^x-1)\sim -\frac{x^2}{2} $ (cùng bậc với $ x^2 $) khi $ x\to 0 $.

Với các “VCB tương đương nhân tạo”, muốn $ x-\beta(x)\sim x^a $ với $ a>1 $ bất kì, chỉ cần chọn $ \beta(x)=x-x^a $. Khi đó $ x\sim x-x^a $ (ngắt bỏ VCB bậc cao), và $ x-(x-x^a)=x^a $.

  
### 9.7 Ba phương pháp (mới) để tính giới hạn

Đến thời điểm hiện tại, ta có ba phương pháp “mới” để tính giới hạn:

- Phương pháp sử dụng VCB–VCL (thay tương đương, ngắt bỏ).

- Phương pháp dùng khai triển Maclaurin.

- Phương pháp dùng quy tắc L'Hospital.

Mỗi phương pháp có ưu, nhược điểm riêng và hợp với từng dạng bài. Dưới đây là 6 ví dụ minh họa:

![](../extracted/graphs/graph_77_0.png)
  
#### Ví dụ 1 (Cả ba phương pháp đều áp dụng được)

$ \lim_{x\to 0}\frac{1-\cos x}{\ln(1+x^2)}=\frac{\frac{x^2}{2}+o(x^2)}{x^2+o(x^2)}\to \frac{1}{2} $.

  
#### Ví dụ 2 (Dùng VCB hoặc Maclaurin; không nên dùng L'Hospital)

$ \lim_{x\to 0}\frac{1-\cos x+x^2-\sin x}{x+\sin^2 x+\arcsin^3 x+\arctan^4 x} $.

  
#### Ví dụ 3 (Dùng Maclaurin hoặc L'Hospital; không “thay tương đương” bừa bãi)

$ \lim_{x\to 0}\frac{x-\sin x+x^3}{x^3} $.

Ở đây $ x-\sin x\sim \frac{x^3}{6} $, nên tử số $ \sim \big(\frac{1}{6}+1\big)x^3 $, giới hạn bằng $ \frac{7}{6} $. Nếu thay $ x\sim \sin x $ thì sẽ sai.

  
#### Ví dụ 4 (Khai triển Maclaurin; không thay tương đương ở tử số và không dùng L'Hospital)

$ \lim_{x\to 0}\frac{x-\sin x-x^3}{\arcsin(\arctan^3 x)} $.

Tử số $ x-\sin x-x^3\sim \frac{x^3}{6}-x^3=-\frac{5}{6}x^3 $. Mẫu $ \arcsin(\arctan^3 x)\sim \arcsin(x^3)\sim x^3 $. Do đó giới hạn $ =-\frac{5}{6} $.

  
#### Ví dụ 5 (Dùng L'Hospital; không dùng VCB, Maclaurin)

- $ \lim_{x\to 0^+}\frac{\ln x}{x}=-\infty $.

- $ \lim_{x\to 0^+}x^x=\lim_{x\to 0^+}e^{x\ln x}=e^{\lim x\ln x}=e^0=1 $.

  
#### Ví dụ 6 (Không dùng cả ba phương pháp L'Hospital, VCB, Maclaurin)

$ \lim_{x\to +\infty}\frac{x-\sin x}{x+\cos x}=\lim_{x\to +\infty}\frac{1-\frac{\sin x}{x}}{1+\frac{\cos x}{x}}=1 $.

  
#### Chú ý 1.18

Trong quá trình tìm giới hạn của các dạng vô định, nên linh hoạt, có thể kết hợp nhiều phương pháp với nhau để đạt hiệu quả tốt nhất. Chẳng hạn trong Ví dụ 4, nên dùng Maclaurin ở tử số và thay tương đương ở mẫu số.

  
### 9.8 Về các VCL tiêu biểu

Ta đã học về VCB, VCL, quy tắc thay tương đương, ngắt bỏ VCB bậc cao, ngắt bỏ VCL bậc thấp. Các VCL tiêu biểu khi $ x\to +\infty $ là:

- Hàm số mũ với cơ số lớn hơn 1, ví dụ $ a^x $ (với $ a>1 $).

- Các hàm đa thức, lũy thừa của $ x $, như $ x^n $, $ x^{\alpha} $ ($ \alpha>0 $).

- Các hàm logarit với cơ số lớn hơn 1, như $ \ln x $, $ \log_a x $ ($ a>1 $).

Cả ba đều tiến ra vô cùng khi $ x\to +\infty $, nhưng tốc độ khác nhau: mũ ≻ đa thức ≻ logarit.

Cụ thể, bạn đọc có thể chứng minh (bằng L'Hospital):

$ \lim_{x\to+\infty}\frac{a^x}{x^{\alpha}}=\infty $ với mọi $ a>1 $, $ \alpha>0 $.

$ \lim_{x\to+\infty}\frac{x^{\alpha}}{\log_a x}=\infty $ với mọi $ a>1 $, $ \alpha>0 $.

  
#### Ví dụ 9.28
Tính $ \lim_{x\to +\infty}\frac{\ln x+x^{2016}+e^x}{\log_2 x+x^{2017}+2e^x} $.

Áp dụng quy tắc ngắt bỏ VCL bậc thấp:
$ \ln x+x^{2016}+e^x\sim e^x $,  
$ \log_2 x+x^{2017}+2e^x\sim 2e^x $.

Do đó
$ \lim_{x\to +\infty}\frac{\ln x+x^{2016}+e^x}{\log_2 x+x^{2017}+2e^x}=\frac{1}{2} $.

## §10. CÁC LƯỢC ĐỒ KHẢO SÁT HÀM SỐ

### 10.1 Khảo sát và vẽ đồ thị của hàm số $y = f(x)$

Mục này sinh viên đã được học khá kĩ ở phổ thông, nên chỉ nhấn mạnh các điểm cần chú ý trong quá trình khảo sát hàm số và bổ sung một số dạng khác như hàm có chứa căn thức, ...

Sơ đồ khảo sát

1. Tìm tập xác định (TXĐ) của hàm số, nhận xét tính chẵn, lẻ, tuần hoàn (nếu có).

2. Xác định chiều biến thiên: tìm các khoảng tăng, giảm của hàm số.

3. Tìm cực trị (nếu có).

4. Xét tính lồi, lõm (nếu cần), điểm uốn (nếu có).

5. Tìm các tiệm cận của hàm số (nếu có).

6. Lập bảng biến thiên.

7. Tìm một số điểm đặc biệt mà đồ thị đi qua (ví dụ giao điểm với các trục toạ độ, ...), và vẽ đồ thị của hàm số.

#### Ví dụ 10.2 
Tìm các đường tiệm cận của đường cong $y=x^2\sin\dfrac{1}{x}$.

**Lời giải**

- TXĐ: $ \mathbb{R}\setminus \{0\} $.

- Vì $0\le \left|x^2\sin\dfrac{1}{x}\right|\le x^2$, nên $ \lim_{x\to 0} x^2\sin\dfrac{1}{x}=0 $ (giới hạn kẹp). Suy ra không có tiệm cận đứng tại $x=0$.

- $ \lim_{x\to\infty} x^2\sin\dfrac{1}{x} = \lim_{x\to\infty} x\cdot \frac{\sin(1/x)}{1/x} = \infty $, do đó không có tiệm cận ngang.

- Xét tiệm cận xiên khi $x\to +\infty$:
  
  $ \lim_{x\to\infty}\frac{y}{x} = \lim_{x\to\infty} x\sin\frac{1}{x} = 1 $.
  
  $ \lim_{x\to\infty}(y-x) = \lim_{x\to\infty} x\left(x\sin\frac{1}{x}-1\right) = \lim_{t\to 0} \frac{1}{t}\left(\frac{\sin t}{t}-1\right) = \lim_{t\to 0}\frac{\sin t - t}{t^2}=0 $ (đặt $t=\tfrac{1}{x}$).

Kết luận: Đường cong có một tiệm cận xiên là $y=x$.

  
#### Ví dụ 10.3
Tìm các tiệm cận xiên của đường cong $y=\ln(1+e^{-2x})$.

**Lời giải**

- Khi $x\to +\infty$, $ \lim \dfrac{y}{x}=0 $ nên không có tiệm cận xiên ở $+\infty$.

- Khi $x\to -\infty$, tính hệ số góc và hệ số tự do:
  
  $ a=\lim_{x\to -\infty}\frac{y}{x}=\lim_{x\to -\infty}\frac{\ln(1+e^{-2x})}{x}=\lim_{x\to -\infty}\frac{-2e^{-2x}}{1+e^{-2x}}=-2 $ (L'Hospital).
  
  $ b=\lim_{x\to -\infty}(y-ax)=\lim_{x\to -\infty}\big(\ln(1+e^{-2x})+2x\big)=\lim_{x\to -\infty}\ln\big[(1+e^{-2x})e^{2x}\big]=\lim_{x\to -\infty}\ln(1+e^{2x})=0 $.

Kết luận: $y=-2x$ là tiệm cận xiên của đường cong.

### 10.2 Khảo sát và vẽ đường cong cho dưới dạng tham số

Giả sử cần khảo sát và vẽ đường cong cho dưới dạng tham số
$ \begin{cases}
x=x(t) \\
y=y(t)
\end{cases} $

1. Tìm TXĐ, nhận xét tính chẵn, lẻ, tuần hoàn của $x(t)$, $y(t)$ (nếu có).

2. Xác định chiều biến thiên của $x(t)$, $y(t)$ theo $t$ bằng cách xét dấu các đạo hàm $x'(t)$, $y'(t)$.

3. Tìm các tiệm cận của đường cong:

   (a) Tiệm cận đứng: nếu $ \lim_{t\to t_0(\infty)}y(t)=\infty $ và $ \lim_{t\to t_0(\infty)}x(t)=x_0 $ thì $ x=x_0 $ là tiệm cận đứng.

   (b) Tiệm cận ngang: nếu $ \lim_{t\to t_0(\infty)}x(t)=\infty $ và $ \lim_{t\to t_0(\infty)}y(t)=y_0 $ thì $ y=y_0 $ là tiệm cận ngang.

   (c) Tiệm cận xiên: nếu $ \lim_{t\to t_0(\infty)}y(t)=\infty $ và $ \lim_{t\to t_0(\infty)}x(t)=\infty $ thì có thể có tiệm cận xiên. Khi đó
  
   $ a=\lim_{t\to t_0(\infty)}\frac{y(t)}{x(t)}, \quad b=\lim_{t\to t_0(\infty)}\big(y(t)-a\,x(t)\big) $,
  
   thì $ y=ax+b $ là tiệm cận xiên.

4. Để vẽ chính xác hơn, xác định tiếp tuyến của đường cong tại các điểm đặc biệt. Hệ số góc của tiếp tuyến tại điểm có $x'(t)\ne 0$ là
$ \frac{dy}{dx}=\frac{dy/dt}{dx/dt} $.

Ngoài ra có thể khảo sát tính lồi, lõm và điểm uốn (nếu cần) bằng đạo hàm cấp hai:
$ \frac{d^2y}{dx^2}=\frac{d\left(\frac{dy/dt}{dx/dt}\right)}{dx}=\frac{y''(t)\,x'(t)-y'(t)\,x''(t)}{(x'(t))^3} $.

5. Xác định một số điểm đặc biệt mà đồ thị đi qua và vẽ đồ thị.

### 10.3 Khảo sát và vẽ đường cong trong hệ toạ độ cực