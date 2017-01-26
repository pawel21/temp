#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:47:14 2017

@author: pawel
"""

import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

from plot_laser_efficiency import PlotLaserEfficiency

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 24})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


eff_635_current = PlotLaserEfficiency("L635_temp_25.txt")
#eff_635_current.plot_slope_efficiency_via_current(28)

eff_850_vcsel_current = PlotLaserEfficiency("L850_VCSEL_temp_25.txt")
#eff_850_vcsel_current.plot_slope_efficiency_via_current(2)

eff_980_current = PlotLaserEfficiency("L980_temp_25.txt")
#eff_980_current.plot_slope_efficiency_via_current(1.5)

eff_850_edge_current = PlotLaserEfficiency("L850P010_temp_25.txt")
#eff_850_edge_current.plot_slope_efficiency_via_current(12)

a_635_current, b_635_current, _ = eff_635_current.fit_via_current_poly_2(28)
l635_current_25, _ = eff_635_current.get_data_to_fit_via_current(28)
dP_635_current = 2 * a_635_current * l635_current_25 + b_635_current

a_850_vcsel_current, b_850_vcsel_current, _ = eff_850_vcsel_current.fit_via_current_poly_2(2)
l850_vcsel_current_25, _ = eff_850_vcsel_current.get_data_to_fit_via_current(2)
dP_850_vcsel_current = 2 * a_850_vcsel_current * l850_vcsel_current_25 + b_850_vcsel_current

a_980_current, b_980_current, _ = eff_980_current.fit_via_current_poly_2(1.5)
l980_current, _  = eff_980_current.get_data_to_fit_via_current(1.5)
dP_980_vcsel_current = 2 * a_980_current * l980_current + b_980_current

a_850_edge_current, b_850_edge_current, _ = eff_850_edge_current.fit_via_current_poly_2(12)
l850_edge_current_25, _ = eff_850_edge_current.get_data_to_fit_via_current(12)
dP_850_edge_current = 2 * a_850_edge_current * l850_edge_current_25 + b_850_edge_current


ax1= plt.subplot(221)

ax1.plot(l635_current_25, dP_635_current, label="krawędziówka 635\,nm")
ax1.plot(l850_edge_current_25, dP_850_edge_current, label="krawędziówka 850\,nm")
ax1.set_xlabel("prąd [mA]")
ax1.set_ylabel(r"sprawność różniczkowa [W/A]")
plt.legend(loc=5,prop={'size':16})
plt.grid(True)

ax3 = plt.subplot(223)
ax3.plot(l850_vcsel_current_25, dP_850_vcsel_current)
ax3.plot(l980_current, dP_980_vcsel_current)
ax3.set_xlabel("prąd [mA]")
ax3.set_ylabel(r"sprawność różniczkowa [W/A]")
plt.grid(True)
plt.show()