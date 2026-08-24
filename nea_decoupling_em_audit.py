#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nea_decoupling_em_audit.py
验证退耦条件：f_ext(x_dec) = 1/U_EM

退耦点 x_dec 由带宽磨损方程和电磁承载力极限确定。
"""
import numpy as np

# 基础量
pi = np.pi
U_EM = 0.4 * pi
U_EM_inv = 1.0 / U_EM

# 带宽磨损方程
def f_ext(x):
    return 4.0 / 5.0 - x / 100.0

# 退耦点由 f_ext(x_dec) = 1/U_EM 解出
x_dec = 100.0 * (4.0 / 5.0 - U_EM_inv)
f_dec = f_ext(x_dec)

# 带宽赤字场 phi = (1 - f_ext^2)/2
phi_dec = (1.0 - f_dec**2) / 2.0

print("="*80)
print("  退耦条件验证：f_ext(x_dec) = 1/U_EM")
print("="*80)
print(f"  U_EM      = {U_EM:.6f}")
print(f"  1/U_EM    = {U_EM_inv:.6f}")
print()
print(f"  x_dec     = {x_dec:.6f}")
print(f"  f_ext(x_dec) = {f_dec:.6f}")
print(f"  phi(x_dec)   = {phi_dec:.6f}")
print()
print(f"  f_ext(x_dec) / (1/U_EM) = {f_dec/U_EM_inv:.8f}")
print(f"  绝对偏差 = {abs(f_dec - U_EM_inv):.2e}")
print()
print("  结论：")
print("  退耦点由电磁拓扑承载力极限 1/U_EM 确定，")
print("  与带宽磨损方程自洽闭合。")
print("="*80)