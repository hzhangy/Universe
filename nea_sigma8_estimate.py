#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. σ_8 估算
从 CMB δT/T 标度到 8 Mpc/h 球内物质密度涨落幅度
"""
from math import pi, sqrt, exp

# N.E.A. 参数
delta_TT_nea = 6.07e-6       # 来自 N.E.A.
Omega_m_nea = 0.322930
Omega_b_nea = 0.050957
Omega_c_nea = 0.271973
h_nea = 0.680398
T_CMB_nea = 2.7287
n_s_nea = 0.965000

# Planck 2018 参考值
delta_TT_planck = 6.0e-6
Omega_m_planck = 0.315
Omega_b_planck = 0.049
h_planck = 0.6736
T_CMB_planck = 2.7255
n_s_planck = 0.9649
sigma8_planck = 0.811

# 标度关系：σ_8 ∝ (δT/T) × Ω_m^(-0.3) × h^(-0.5) × n_s^(0.5) × T^(-1)
sigma8_nea = sigma8_planck * (delta_TT_nea / delta_TT_planck) \
           * (Omega_m_nea / Omega_m_planck)**(-0.3) \
           * (h_nea / h_planck)**(-0.5) \
           * (n_s_nea / n_s_planck)**(0.5) \
           * (T_CMB_nea / T_CMB_planck)**(-1)

print("="*80)
print("  N.E.A. σ_8 估算")
print("="*80)
print(f"  δT/T(nea) = {delta_TT_nea:.2e}")
print(f"  Ω_m_nea   = {Omega_m_nea:.6f}")
print(f"  h_nea     = {h_nea:.6f}")
print(f"  n_s_nea   = {n_s_nea:.6f}")
print(f"  T_CMB_nea = {T_CMB_nea:.4f} K")
print()
print(f"  σ_8(nea) = {sigma8_nea:.4f}")
print(f"  σ_8(obs) = {sigma8_planck:.4f}")
print(f"  偏差 = {abs(sigma8_nea/sigma8_planck - 1)*100:.2f}%")
print("="*80)