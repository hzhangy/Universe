#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. CMB 移位参数 R V2（修正 z_* 拟合公式）
"""
from scipy.integrate import quad
from math import pi, sqrt

c = 299792.458  # km/s

# N.E.A. 参数
Omega_b_nea = 0.050957
Omega_c_nea = 0.271973
Omega_m_nea = Omega_b_nea + Omega_c_nea
Omega_Lambda_nea = 1 - Omega_m_nea
h_nea = 0.680398
H0_nea = 100 * h_nea

Omega_gamma_h2 = 2.469e-5
Omega_nu_h2 = 1.711e-5
Omega_r_h2 = Omega_gamma_h2 + Omega_nu_h2
Omega_r_nea = Omega_r_h2 / h_nea**2

# 正确 z_* 拟合（与 theta_star 脚本一致）
g1 = 0.0783 * (Omega_m_nea*h_nea**2)**(-0.238) / (1 + 39.5*(Omega_b_nea*h_nea**2)**0.763)
g2 = 0.560 / (1 + 21.1*(Omega_b_nea*h_nea**2)**1.81)
z_star = 1048 * (1 + 0.00124*(Omega_b_nea*h_nea**2)**(-0.738)) * (1 + g1*(Omega_m_nea*h_nea**2)**g2)

def H(z):
    return H0_nea * sqrt(Omega_m_nea*(1+z)**3 + Omega_r_nea*(1+z)**4 + Omega_Lambda_nea)

def integrand(z):
    return c / H(z)

D_A, _ = quad(integrand, 0, z_star, limit=200)

R = sqrt(Omega_m_nea) * H0_nea * D_A / c

print("="*80)
print("  N.E.A. CMB 移位参数 R V2")
print("="*80)
print(f"  Ω_m_nea = {Omega_m_nea:.6f}")
print(f"  h_nea = {h_nea:.6f}")
print(f"  最后散射面红移 z_* = {z_star:.2f}")
print(f"  角直径距离 D_A = {D_A:.2f} Mpc")
print(f"  移位参数 R_nea = {R:.4f}")
print(f"  观测 R_obs ≈ 1.7502 (Planck 2018)")
print(f"  偏差 = {abs(R/1.7502 - 1)*100:.2f}%")
print("="*80)