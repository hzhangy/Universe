import numpy as np
from math import pi, sqrt, exp
from scipy.integrate import quad

# 已有拓扑参数
Delta = 1 - sqrt(3)/2
R = 1/(1+pi)
N_max = exp(10*sqrt(3))
f_geo = 1 + Delta/(4*pi)

# 物理常数
Z_MeV = 0.406640
Z_J = Z_MeV * 1e6 * 1.602176634e-19
hbar_SI = 1.054571817e-34
c_SI = 299792458.0
m_p_MeV = 938.272

# 观测值
H0_obs_km_s_Mpc = 67.66  # Planck
t0_obs_Gyr = 13.787  # Planck 2018

# 拓扑 H0
t_Tick = hbar_SI / Z_J
alpha_G = R / (N_max**5)
H0_nea_s = (1/t_Tick) * alpha_G * sqrt(R) * (1+R) / f_geo

# 转换为 km/s/Mpc
H0_nea_km_s_Mpc = H0_nea_s * 3.085677581e22 / 1e3
print(f"H0_nea = {H0_nea_km_s_Mpc:.3f} km/s/Mpc")

# Ω参数
Omega_Lambda_nea = 0.677070
Omega_m_nea = 1 - Omega_Lambda_nea
Omega_k = 0  # 平坦

# 宇宙年龄函数
def H(z):
    return H0_nea_s * np.sqrt(Omega_m_nea*(1+z)**3 + Omega_Lambda_nea + Omega_k*(1+z)**2)

# t0 = ∫_0^∞ dz / ((1+z) H(z))
t0_s, _ = quad(lambda z: 1.0/((1+z)*H(z)), 0, np.inf, limit=200)
t0_Gyr = t0_s / (365.25*24*3600*1e9)

print(f"t0_nea = {t0_Gyr:.3f} Gyr")
print(f"t0_obs = {t0_obs_Gyr:.3f} Gyr")
print(f"偏差 = {abs(t0_Gyr/t0_obs_Gyr-1)*100:.2f}%")

# 减速参数
q0 = Omega_m_nea/2 - Omega_Lambda_nea
print(f"q0_nea = {q0:.4f}")
print("q0_obs 约 -0.527 (Planck)")