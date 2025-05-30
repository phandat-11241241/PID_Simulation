import numpy as np
import matplotlib.pyplot as plt

angle_planet_list = []
omega_planet_list = []
omega_wheel_list = []
tau_list = []

#Giả sử ảnh hưởng của moment quán tính 
I_planet = float(input("Nhập Moment quán tính của vệ tinh: "))
I_wheel = float(input("Nhập Moment quán tính của reaction wheel: "))

# Tham số PID
Kp = float(input("Nhập Proportional gain Kp: ")) # Proportional gain
Ki = float(input("Nhập Integral gain Ki: "))  # Integral gain
Kd = float(input("Nhập Derivative gain Kd: "))    # Derivative gain

# Thời gian mô phỏng
dt = 0.01           # bước thời gian 
t_end = 10        #  thời gian mô phỏng 
time = np.arange(0, t_end, dt)

# Góc mục tiêu
target_angle = float(input("Nhập góc mục tiêu: "))
target_angle_1 = target_angle 
target_angle = np.deg2rad(target_angle) 

# Trạng thái ban đầu
angle_planet = 0.0       # Góc vệ tinh [rad]
omega_planet = 0.0       # Vận tốc góc vệ tinh
omega_wheel = 0.0       # Vận tốc góc bánh xe

# Biến PID
integral = 0
pre_error = 0

for t in time:
    # Tính sai số và PID
    error = angle_planet - target_angle  
    integral += error * dt
    derivative = (error - pre_error) / dt
    tau = Kp * error + Ki * integral + Kd * derivative

    # Phương trình động lực học
    alpha_wheel = tau / I_wheel 
    omega_wheel += alpha_wheel * dt  
    alpha_planet = -I_wheel * alpha_wheel / I_planet
    omega_planet += alpha_planet * dt
    angle_planet += omega_planet * dt

    # ghi lại các thông số tại thời điểm t 
    angle_planet_list.append(np.rad2deg(angle_planet))
    omega_planet_list.append(np.rad2deg(omega_planet))
    omega_wheel_list.append(np.rad2deg(omega_wheel))
    tau_list.append(tau)

    # Cập nhật sai số 
    pre_error = error
Input_data = (
    f"I_planet = {I_planet}, I_wheel = {I_wheel}  |  "
    "Thông số hiệu chỉnh PID: " + f"Kp = {Kp}, Ki = {Ki}, Kd = {Kd}  |  "
    f"Target angle = {target_angle_1} deg"
) 
plt.figure(figsize=(14, 8))
plt.suptitle("Mô phỏng PID điều khiển vệ tinh\n" + Input_data , fontsize=15)
plt.subplot(3, 1, 1)
plt.plot(time, angle_planet_list)
plt.ylabel("Góc vệ tinh (deg)")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(time, omega_planet_list, label='Vệ tinh')
plt.plot(time, omega_wheel_list, label='Reaction Wheel')
plt.ylabel("Vận tốc góc (deg/s)")
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(time, tau_list)
plt.ylabel("Moment điều khiển (Nm)")
plt.xlabel("Thời gian (s)")
plt.grid(True)

plt.tight_layout()
plt.show()
