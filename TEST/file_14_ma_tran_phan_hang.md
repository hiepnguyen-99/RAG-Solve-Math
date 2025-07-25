# Ma trận phân hạng (Rank Matrix)

## Định nghĩa
**Hạng của ma trận** là số lượng vector độc lập tuyến tính tối đa trong tập hàng hoặc cột của ma trận đó.

\[ \text{rank}(A) = \dim(\text{Col}(A)) = \dim(\text{Row}(A)) \]

## Cách tìm hạng
- Dùng phép khử Gauss để đưa về dạng bậc thang
- Đếm số hàng khác 0 sau khi rút gọn

## Tính chất
- \( \text{rank}(A) \leq \min(m, n) \)
- \( \text{rank}(A) = \text{rank}(A^T) \)
- \( \text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B)) \)

## Hạng và nghiệm hệ phương trình
- Nếu \( \, \text{rank}(A) = \text{rank}([A | B]) = n \), hệ có nghiệm duy nhất
- Nếu \( \, \text{rank}(A) = \text{rank}([A | B]) < n \), hệ có vô số nghiệm
- Nếu \( \, \text{rank}(A) < \text{rank}([A | B]) \), hệ vô nghiệm

## Ứng dụng
- Phân tích số chiều dữ liệu
- Phát hiện dữ liệu trùng lặp trong học máy

