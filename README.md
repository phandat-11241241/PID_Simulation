## Description

Chương trình mô phỏng quá trình **điều khiển quay một vệ tinh quanh một trục (1 DOF)** dưới ảnh hưởng của moment quán tính và moment phản lực từ **bánh xe phản lực (reaction wheel)** .

**Mục tiêu của mô hình hoá**:

- Thể hiện quá trình quay của vệ tinh thông qua **moment phản lực sinh ra từ bánh xe**
- Áp dụng **điều khiển PID** để điều chỉnh hướng quay vệ tinh đến đúng **góc mục tiêu (target angle)**
- Mô phỏng ảnh hưởng của:
  - Moment quán tính của vệ tinh (`I_planet`)
  - Moment quán tính của bánh xe (`I_wheel`)
  - Tham số điều khiển PID (`Kp`, `Ki`, `Kd`)
- Hiển thị các thông số vật lý theo thời gian:
  - Góc quay của vệ tinh
  - Vận tốc quay của vệ tinh và bánh xe
  - Moment lực điều khiển
- Tất cả quá trình được thực hiện trong môi trường mô phỏng rời rạc theo bước thời gian `dt`, và kết quả được trực quan hóa bằng biểu đồ.

## Các bước thực hiện mô phỏng

### 1. Tính moment điều khiển (τ)
Từ sai số giữa góc quay hiện tại và góc mục tiêu, bộ điều khiển PID tính được moment lực τ cần thiết để điều chỉnh reaction wheel tại mỗi bước thời gian `dt`.

### 2. Tính động học bánh xe phản lực
Từ moment lực τ, tính được:
- Gia tốc góc: α_wheel = τ / I_wheel
- Vận tốc góc: ω_wheel(t + Δt) = ω_wheel(t) + α_wheel · dt

### 3. Tính trạng thái của vệ tinh (bảo toàn moment động lượng)
Áp dụng định luật bảo toàn moment động lượng :
  
          I_planet · ω_planet + I_wheel · ω_wheel = const

→ Gia tốc vệ tinh: α_planet = – (I_wheel / I_planet) · α_wheel  
→ Vận tốc góc vệ tinh: ω_planet(t + Δt) = ω_planet(t) + α_planet·dt

 ### 4. Hiển thị đồ thị của các trạng thái của vệ tinh và reaction wheel tại các khoảng thời gian
## Kết quả mô phỏng PID
![Kết quả mô phỏng](https://github.com/phandat-11241241/PID_Simulation/blob/master/Report.png?raw=true)
