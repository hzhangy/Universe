#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. 物质功率谱形状参数 Γ
"""
from math import sqrt, exp

# N.E.A. 参数
Omega_b_nea = 0.050957
Omega_c_nea = 0.271973
Omega_m_nea = Omega_b_nea + Omega_c_nea
h_nea = 0.680398

# 常见形状参数公式 (Efstathiou et al. 1992 / Sugiyama 1995)
Gamma = Omega_m_nea * h_nea * exp(-Omega_b_nea * (1 + sqrt(2*h_nea)/Omega_m_nea))

print("="*80)
print("  N.E.A. 物质功率谱形状参数 Γ")
print("="*80)
print(f"  Ω_b_nea = {Omega_b_nea:.6f}")
print(f"  Ω_c_nea = {Omega_c_nea:.6f}")
print(f"  Ω_m_nea = {Omega_m_nea:.6f}")
print(f"  h_nea = {h_nea:.6f}")
print(f"  Γ_nea = {Gamma:.4f}")
print(f"  观测 Γ ≈ 0.20 (SDSS / 2dF 近似)")
print(f"  偏差 = {abs(Gamma/0.20 - 1)*100:.2f}%")
print("="*80)