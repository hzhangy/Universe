#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. 物质-辐射相等红移 z_eq
"""
from math import pi, sqrt, exp

# N.E.A. 参数
Omega_b_nea = 0.050957
Omega_c_nea = 0.271973
Omega_m_nea = Omega_b_nea + Omega_c_nea
h_nea = 0.680398

Omega_gamma_h2 = 2.469e-5
Omega_nu_h2 = 1.711e-5
Omega_r_h2 = Omega_gamma_h2 + Omega_nu_h2
Omega_r_nea = Omega_r_h2 / h_nea**2

z_eq = Omega_m_nea / Omega_r_nea - 1

print("="*80)
print("  N.E.A. 物质-辐射相等红移 z_eq")
print("="*80)
print(f"  Ω_m_nea = {Omega_m_nea:.6f}")
print(f"  Ω_r_nea = {Omega_r_nea:.6e}")
print(f"  z_eq_nea = {z_eq:.2f}")
print(f"  观测 z_eq ≈ 3402 (Planck 2018)")
print(f"  偏差 = {abs(z_eq/3402 - 1)*100:.2f}%")
print("="*80)