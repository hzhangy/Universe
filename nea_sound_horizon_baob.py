#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. 重子声学振荡尺度 r_d 计算 V3
修正：恢复 R 方向 + 加入辐射项
"""
import numpy as np
from scipy.integrate import quad
from math import pi, sqrt

# 物理常数
c = 299792.458  # km/s

# N.E.A. 参数
Omega_b_nea = 0.050957
Omega_c_nea = 0.271973
Omega_m_nea = Omega_b_nea + Omega_c_nea
Omega_Lambda_nea = 1 - Omega_m_nea
h_nea = 0.680398
H0_nea = 100 * h_nea  # km/s/Mpc

# 辐射密度参数
Omega_gamma_h2 = 2.469e-5  # 光子 (T=2.725K 近似)
# 中微子贡献：3.046 种无质量中微子
Omega_nu_h2 = 1.711e-5
Omega_r_h2 = Omega_gamma_h2 + Omega_nu_h2
Omega_r_nea = Omega_r_h2 / h_nea**2

# 拖拽红移近似 (Eisenstein & Hu 1998)
theta = 2.7287/2.7
b1 = 0.313 * (Omega_m_nea*h_nea**2)**(-0.419) * (1 + 0.607*(Omega_m_nea*h_nea**2)**0.674)
b2 = 0.238 * (Omega_m_nea*h_nea**2)**0.223
z_d = 1291 * (Omega_m_nea*h_nea**2)**0.251 / (1 + 0.659*(Omega_m_nea*h_nea**2)**0.828) * (1 + b1*(Omega_b_nea*h_nea**2)**b2)

# 声速中的 R = 3ρ_b / (4ρ_γ)
def R_func(z):
    # R0 = 3Ω_b / (4Ω_γ)
    R0 = 3 * Omega_b_nea * h_nea**2 / (4 * Omega_gamma_h2)
    return R0 / (1 + z)

def cs(z):
    R = R_func(z)
    return c / sqrt(3*(1 + R))

def H(z):
    return H0_nea * sqrt(Omega_m_nea*(1+z)**3 + Omega_r_nea*(1+z)**4 + Omega_Lambda_nea)

# 积分 r_d = ∫_{z_d}^{∞} c_s / H dz
# 变量 t=1/(1+z)，t 从 0 到 1/(1+z_d)
def integrand(t):
    z = 1/t - 1
    return cs(z) / H(z) / t**2

t_low = 0.0
t_high = 1.0/(1.0+z_d)

rd, err = quad(integrand, t_low, t_high, limit=200)

print("="*80)
print("  N.E.A. 重子声学振荡尺度 r_d V3")
print("="*80)
print(f"  Ω_b_nea = {Omega_b_nea:.6f}")
print(f"  Ω_c_nea = {Omega_c_nea:.6f}")
print(f"  Ω_m_nea = {Omega_m_nea:.6f}")
print(f"  Ω_Lambda_nea = {Omega_Lambda_nea:.6f}")
print(f"  h_nea = {h_nea:.6f}")
print(f"  Ω_r_nea = {Omega_r_nea:.6e}")
print(f"  拖拽红移 z_d = {z_d:.2f}")
print(f"  声学视界 r_d = {rd:.2f} Mpc")
print()
print(f"  观测 r_d (Planck 2018) ≈ 147.09 Mpc")
print(f"  偏差 = {abs(rd/147.09 - 1)*100:.2f}%")
print("="*80)