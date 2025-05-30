## Description

Chương trình mô phỏng quá trình **điều khiển quay một vệ tinh quanh một trục (1 DOF)** dưới ảnh hưởng của moment quán tính và moment phản lực từ **bánh xe phản lực (reaction wheel)** .

**Mục tiêu của mô hình hoá**:

- Thể hiện quá trình quay của vệ tinh thông qua **moment phản lực sinh ra từ bánh xe**
- Áp dụng **điều khiển PID** để điều chỉnh hướng quay vệ tinh đến đúng **góc mục tiêu (target angle)**
- Mô phỏng ảnh hưởng của:
  - Moment quán tính của vệ tinh** (`I_planet`)
  - Moment quán tính của bánh xe** (`I_wheel`)
  - Tham số điều khiển PID (`Kp`, `Ki`, `Kd`)
- Hiển thị các thông số vật lý theo thời gian:
  - Góc quay của vệ tinh
  - Vận tốc quay của vệ tinh và bánh xe
  - Moment lực điều khiển
- Tất cả quá trình được thực hiện trong môi trường mô phỏng rời rạc theo bước thời gian `dt`, và kết quả được trực quan hóa bằng biểu đồ.

**Các bước thực hiện**

  1> Từ công thức PID tính được moment lực τ cần để điều chỉnh cho reaction wheel trong khoảng thời gian dt

  2> Từ moment lực τ, tính được gia tốc góc alpha và vận tốc góc omega để điều chỉnh cho reaction wheel

  3> Áp dụng định luật bảo toàn moment động lượng tìm được các thông số gia tốc góc, vận tốc góc của vệ tinh
    
  
 

