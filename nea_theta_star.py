#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. CMB 角尺度 θ_* = r_d / D_A(z_*)
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
H0_nea = 100 * h_nea

# 辐射参数
Omega_gamma_h2 = 2.469e-5
Omega_nu_h2 = 1.711e-5
Omega_r_h2 = Omega_gamma_h2 + Omega_nu_h2
Omega_r_nea = Omega_r_h2 / h_nea**2

# 拖拽红移与最后散射面红移
theta = 2.7287 / 2.7
b1 = 0.313 * (Omega_m_nea*h_nea**2)**(-0.419) * (1 + 0.607*(Omega_m_nea*h_nea**2)**0.674)
b2 = 0.238 * (Omega_m_nea*h_nea**2)**0.223
z_d = 1291 * (Omega_m_nea*h_nea**2)**0.251 / (1 + 0.659*(Omega_m_nea*h_nea**2)**0.828) * (1 + b1*(Omega_b_nea*h_nea**2)**b2)

# z_* 拟合 (Hu & White 1997)
g1 = 0.0783 * (Omega_m_nea*h_nea**2)**(-0.238) / (1 + 39.5*(Omega_b_nea*h_nea**2)**0.763)
g2 = 0.560 / (1 + 21.1*(Omega_b_nea*h_nea**2)**1.81)
z_star = 1048 * (1 + 0.00124*(Omega_b_nea*h_nea**2)**(-0.738)) * (1 + g1*(Omega_m_nea*h_nea**2)**g2)

# 声速
def R_func(z):
    R0 = 3 * Omega_b_nea * h_nea**2 / (4 * Omega_gamma_h2)
    return R0 / (1 + z)

def cs(z):
    R = R_func(z)
    return c / sqrt(3*(1+R))

def H(z):
    return H0_nea * sqrt(Omega_m_nea*(1+z)**3 + Omega_r_nea*(1+z)**4 + Omega_Lambda_nea)

# 声学视界 r_d
def integrand_rd(t):
    z = 1/t - 1
    return cs(z) / H(z) / t**2

t_high = 1/(1+z_d)
rd, _ = quad(integrand_rd, 0, t_high, limit=200)

# 角直径距离 D_A(z_star)
def integrand_da(z):
    return c / H(z)

DA_comoving, _ = quad(integrand_da, 0, z_star, limit=200)

# 角尺度 θ_* = r_d / D_A
theta_star = rd / DA_comoving  # 弧度

print("="*80)
print("  N.E.A. CMB 角尺度 θ_* = r_d / D_A(z_*)")
print("="*80)
print(f"  拖拽红移 z_d = {z_d:.2f}")
print(f"  最后散射面红移 z_* = {z_star:.2f}")
print(f"  声学视界 r_d = {rd:.2f} Mpc")
print(f"  角直径距离 D_A = {DA_comoving:.2f} Mpc")
print(f"  θ_* = {theta_star:.6f} rad")
print(f"  θ_* (Planck 2018) ≈ 0.010409 rad")
print(f"  偏差 = {abs(theta_star/0.010409 - 1)*100:.2f}%")
print("="*80)