#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 00:48:06 2017

@author: pawel
"""

import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 20})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'
plt.rcParams['figure.figsize'] = 23, 16

def f(x, a, b):
    return a*x + b
    
def exp(t, i_0, t_0):
    return i_0*np.exp(t/t_0)
    
def get_t_0(a, da):
      t0 = 1 / a
      dt = abs(-1 / a ** 2) * da
      return t0, dt

def get_i_0(b, db):
      i_th = np.e ** b
      di_th = abs(np.e ** b) * db
      return i_th, di_th    

temp_850 = np.linspace(10, 80, 15) + 273
I_th_850 = [10.48, 10.86, 11.05, 11.33, 11.65, 11.98, 12.34, 12.71, 13.11, 13.57, 14.08, 14.58, 15.18, 15.74, 16.55]
error_I_th_850 = [0.090, 0.10, 0.100, 0.050, 0.060, 0.070, 0.070, 0.080, 0.090, 0.070, 0.100, 0.100, 0.110, 0.130, 0.160]

ax1 = plt.subplot(131)
ax1.errorbar(temp_850, I_th_850, yerr=error_I_th_850, fmt='o')
ax1.set_xlabel("temperatura, $T$ [K]")
ax1.set_ylabel("prąd progowy, $I_{\mathrm{th}}$ [mA]")
plt.grid(True)

ax2 = plt.subplot(132)
ax2.plot(temp_850, np.log(I_th_850), 'ro')
ax2.set_xlabel("temperatura, $T$ [K]")
ax2.set_ylabel("$\ln(I_{\mathrm{th}})$")
ax2.text(280, 2.76, r"$\ln(I_{\mathrm{th}}) = \frac{T}{T_{0}} + \ln I_{0}$")
ax2.text(280, 2.72, "$T_0 = (157 \pm 4)$\,K")
ax2.text(280, 2.68, "$I_0 = (1.7 \pm 0.1)$\,mA")
plt.grid(True)

popt, pcov = curve_fit(f, temp_850, np.log(I_th_850))
a = popt[0]
b = popt[1]
error = np.abs(np.diag(pcov)**0.5)
da = error[0]
db = error[1]

t_0, dt_0 = get_t_0(a,da)
i_0, di_0 = get_i_0(b, db)
print("t_0 = %s +- %s" %(t_0, dt_0))
print("i_0 = %s +- %s" %(i_0, di_0)) 

x = np.linspace(5, 85, 100) + 273
y = a*x + b
ax2.plot(x, y, 'b--') 

ax3 = plt.subplot(133)
ax3.set_xlabel("temperatura, $T$ [K]")
ax3.set_ylabel("prąd progowy, $I_{\mathrm{th}}$ [mA]")
ax3.errorbar(temp_850, I_th_850, yerr=error_I_th_850, fmt='o')
f_exp = exp(x, i_0, t_0)
ax3.text(280, 14, r"$y=1.7 \cdot \exp (\frac{T}{157})$", color='green')
ax3.plot(x, f_exp, 'g-')
plt.grid(True)

plt.subplots_adjust(left=0.08, right=0.95, top=0.93, bottom=0.1, hspace=0.34, wspace=0.320)
plt.show()