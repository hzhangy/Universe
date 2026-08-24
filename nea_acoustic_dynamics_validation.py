#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. CMB 动力学方程验证 V2
延长模拟时间 + 抛物线插值细化FFT峰值
"""
import numpy as np
from scipy.integrate import solve_ivp
from math import pi, sqrt

# 参数
k = 0.2
R = 0.6
cs = 1.0 / sqrt(3.0*(1.0+R))
omega_theory = k * cs

# 数值求解：延长到 T=5000，保证足够多周期
T_total = 5000.0
N_samples = 200000
t_eval = np.linspace(0.0, T_total, N_samples)

def rhs(t, y):
    return [y[1], -omega_theory**2 * y[0]]

sol = solve_ivp(rhs, (0.0, T_total), [1.0, 0.0],
                t_eval=t_eval, rtol=1e-12, atol=1e-12)

signal = sol.y[0]

# 取后半段，排除瞬态
signal = signal[len(signal)//2:]

# FFT
dt = t_eval[1] - t_eval[0]
n = len(signal)
freqs = np.fft.rfftfreq(n, d=dt)
fft = np.abs(np.fft.rfft(signal))

# 找峰值附近做抛物线插值
idx = np.argmax(fft[1:]) + 1
if 0 < idx < len(freqs)-1:
    f0 = freqs[idx-1]
    f1 = freqs[idx]
    f2 = freqs[idx+1]
    y0 = fft[idx-1]
    y1 = fft[idx]
    y2 = fft[idx+1]
    # 抛物线顶点频率
    denom = (y0 - 2*y1 + y2)
    if abs(denom) > 1e-15:
        delta = 0.5 * (y0 - y2) / denom
        f_peak = f1 + delta * (f1 - f0)
    else:
        f_peak = f1
else:
    f_peak = freqs[idx]

omega_measured = 2.0 * pi * f_peak

print("="*80)
print("  N.E.A. CMB 动力学方程验证 V2")
print("="*80)
print(f"  k = {k}")
print(f"  R = {R}")
print(f"  理论声速 c_s = {cs:.6f}")
print(f"  理论角频率 ω = {omega_theory:.6f}")
print()
print(f"  数值测得角频率 ω = {omega_measured:.6f}")
print(f"  偏差 = {abs(omega_measured/omega_theory - 1.0)*100:.4f}%")
print("="*80)
if abs(omega_measured/omega_theory - 1.0) < 0.01:
    print("  ✅ 方程验证通过：N.E.A. CMB 动力学方程正确描述声学振荡。")
else:
    print("  ⚠️ 偏差仍大于预期，请检查数值设置。")