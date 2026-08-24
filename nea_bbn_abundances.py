#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. 原初核合成丰度：Y_p 和 D/H
"""
from math import log

# N.E.A. η
eta_nea = 6.427287e-10

# 观测值
Yp_obs = 0.2449
Yp_err = 0.0040
DH_obs = 2.55e-5
DH_err = 0.03e-5

# 标准 BBN 近似
# Y_p = 0.2485 + 0.0016 ln(η/6e-10)
Yp_nea = 0.2485 + 0.0016 * log(eta_nea / 6.0e-10)

# D/H = 2.6e-5 * (η/6e-10)^(-1.6)
DH_nea = 2.6e-5 * (eta_nea / 6.0e-10)**(-1.6)

print("="*80)
print("  N.E.A. 原初核合成丰度")
print("="*80)
print(f"  η_nea = {eta_nea:.6e}")
print()
print(f"  Y_p(nea) = {Yp_nea:.4f}")
print(f"  Y_p(obs) = {Yp_obs:.4f} ± {Yp_err:.4f}")
print(f"  偏差 = {abs(Yp_nea/Yp_obs - 1)*100:.2f}%")
print()
print(f"  D/H(nea) = {DH_nea:.5e}")
print(f"  D/H(obs) = {DH_obs:.5e} ± {DH_err:.5e}")
print(f"  偏差 = {abs(DH_nea/DH_obs - 1)*100:.2f}%")
print("="*80)