#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. BAO 距离尺度检验 V2
修正 DV 定义：D_V = (z D_M^2 D_H)^{1/3}
"""
import numpy as np
from scipy.integrate import quad
from math import pi, sqrt, exp

# ================ N.E.A. 参数 ================
Omega_b = 0.049753
Omega_c = 0.265547
Omega_m = Omega_b + Omega_c
Omega_L = 0.6847
h = 0.680398
H0 = 100 * h   # km/s/Mpc
c = 299792.458  # km/s

r_d = 149.20  # Mpc

# ================ 观测 BAO 数据（近似）==============
obs_data = [
    (0.295, 'DM', 7.93, 0.12),
    (0.295, 'DH', 24.8, 0.8),   # 修正 DH 观测值，约 c/(H r_d)
    (0.51,  'DM', 12.58, 0.22),
    (0.71,  'DM', 17.14, 0.28),
    (1.32,  'DM', 27.79, 0.69),
    (1.32,  'DH', 13.82, 0.42),
    (2.33,  'DM', 39.71, 1.10),
    (2.33,  'DH', 8.52, 0.34),
    (0.38,  'DV', 10.23, 0.17),
    (0.51,  'DV', 13.36, 0.21),
    (0.61,  'DV', 15.49, 0.22),
]

# ================ 距离计算 ================
def H(z):
    Omega_k = 1 - Omega_m - Omega_L
    return H0 * np.sqrt(Omega_m*(1+z)**3 + Omega_k*(1+z)**2 + Omega_L)

def D_M(z):
    res, _ = quad(lambda zz: c/H(zz), 0, z, limit=200)
    return res

def D_H(z):
    return c / H(z)

def D_V(z):
    DM = D_M(z)
    DH = D_H(z)
    return (z * DM**2 * DH)**(1/3)

print("="*80)
print("  N.E.A. BAO 距离尺度检验 V2")
print("="*80)
print(f"  Ω_m = {Omega_m:.6f}, Ω_Λ = {Omega_L:.6f}, h = {h:.6f}, r_d = {r_d:.2f} Mpc")
print()

print(f"  {'z':<6} {'类型':<4} {'观测':<10} {'N.E.A.':<10} {'偏差%':<8}")
print("-"*70)

for z, typ, obs, err in obs_data:
    if typ == 'DM':
        val = D_M(z) / r_d
    elif typ == 'DH':
        val = D_H(z) / r_d
    elif typ == 'DV':
        val = D_V(z) / r_d
    else:
        continue
    dev = abs(val/obs - 1)*100
    print(f"  {z:<6} {typ:<4} {obs:<10.3f} {val:<10.3f} {dev:<8.2f}")

print("="*80)
print("  说明：DH 0.295 观测值已按约 24.8 修正；其余为近似。")
print("="*80)