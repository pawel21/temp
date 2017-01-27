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
plt.rcParams.update({'font.size': 22})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'
plt.rcParams['figure.figsize'] = 16, 11


eff_635_current = PlotLaserEfficiency("L635_temp_25.txt")
#eff_635_current.plot_slope_efficiency_via_current(28)
#eff_635_current.plot_slope_efficiency_via_power(60)

eff_850_vcsel_current = PlotLaserEfficiency("L850_VCSEL_temp_25.txt")
#eff_850_vcsel_current.plot_slope_efficiency_via_current(2)
#eff_850_vcsel_current.plot_slope_efficiency_via_power(2.7)

eff_980_current = PlotLaserEfficiency("L980_temp_25.txt")
#eff_980_current.plot_slope_efficiency_via_current(1.5)
#eff_980_current.plot_slope_efficiency_via_power(2)

eff_850_edge_current = PlotLaserEfficiency("L850P010_temp_25.txt")
#eff_850_edge_current.plot_slope_efficiency_via_current(12)
#eff_850_edge_current.plot_slope_efficiency_via_power(20)

a_635_current, b_635_current, _ = eff_635_current.fit_via_current_poly_2(28)
l635_current_25, _ = eff_635_current.get_data_to_fit_via_current(28)
dP_635_current = 2 * a_635_current * l635_current_25 + b_635_current

a_635_power, b_635_power, _ = eff_635_current.fit_via_power_poly_2(60)
input_power_635, _ = eff_635_current.get_data_to_fit_via_power(60)
dP_635_power = 2*a_635_power*input_power_635 + b_635_power


a_850_vcsel_current, b_850_vcsel_current, _ = eff_850_vcsel_current.fit_via_current_poly_2(2)
l850_vcsel_current_25, _ = eff_850_vcsel_current.get_data_to_fit_via_current(2)
dP_850_vcsel_current = 2 * a_850_vcsel_current * l850_vcsel_current_25 + b_850_vcsel_current

a_850_vcsel_power, b_850_vcsel_power, _ = eff_850_vcsel_current.fit_via_power_poly_2(2.7)
input_power_850_vcsel, _ = eff_850_vcsel_current.get_data_to_fit_via_power(2.7)
dP_850_vcsel_power = 2*a_850_vcsel_power*input_power_850_vcsel + b_850_vcsel_power


a_980_current, b_980_current, _ = eff_980_current.fit_via_current_poly_2(1.5)
l980_current, _  = eff_980_current.get_data_to_fit_via_current(1.5)
dP_980_vcsel_current = 2 * a_980_current * l980_current + b_980_current

a_980_vcsel_power, b_980_vcsel_power, _ = eff_980_current.fit_via_power_poly_2(2)
input_power_980_vcsel, _ = eff_980_current.get_data_to_fit_via_power(2)
dP_980_vcsel_power = 2*a_980_vcsel_power*input_power_980_vcsel + b_980_vcsel_power

a_850_edge_current, b_850_edge_current, _ = eff_850_edge_current.fit_via_current_poly_2(12)
l850_edge_current_25, _ = eff_850_edge_current.get_data_to_fit_via_current(12)
dP_850_edge_current = 2 * a_850_edge_current * l850_edge_current_25 + b_850_edge_current

a_850_edge_power, b_850_edge_power, _ = eff_850_edge_current.fit_via_power_poly_2(20)
input_power_850_edge, _ = eff_850_edge_current.get_data_to_fit_via_power(20)
dP_850_edge_power = 2 * a_850_edge_power * input_power_850_edge + b_850_edge_power


ax1= plt.subplot(221)
ax1.plot(l635_current_25, dP_635_current, 'b-', label="krawędziówka 635\,nm")
ax1.plot(l850_edge_current_25, dP_850_edge_current, 'g-', label="krawędziówka 850\,nm")
ax1.set_xlabel("prąd [mA]")
ax1.set_ylabel(r"sprawność różniczkowa [W/A]")
plt.legend(loc='upper right',prop={'size':16})
plt.grid(True)

ax3 = plt.subplot(223)
ax3.plot(l980_current, dP_980_vcsel_current, 'b-', label="VCSEL 980\,nm")
ax3.plot(l850_vcsel_current_25, dP_850_vcsel_current, 'g-', label="VCSEL 850\,nm")
ax3.set_xlabel("prąd [mA]")
ax3.set_ylabel(r"sprawność różniczkowa [W/A]")
plt.legend(loc='upper right',prop={'size':16})
plt.grid(True)

ax2 = plt.subplot(222)
ax2.plot(input_power_635, dP_635_power, 'b-', label="krawędziówka 635\,nm")
ax2.plot(input_power_850_edge, dP_850_edge_power, 'g-', label="krawędziówka 635\,nm")
ax2.set_xlabel("moc wejściowa [mA]")
ax2.set_ylabel(r"sprawność różniczkowa ")
plt.legend(loc='upper right',prop={'size':16})
plt.grid(True)

ax4 = plt.subplot(224)
ax4.plot(input_power_980_vcsel, dP_980_vcsel_power, 'b-', label="VCSEL 980\,nm")
ax4.plot(input_power_850_vcsel, dP_850_vcsel_power, 'g-',label="VCSEL 850\,nm")
ax4.set_xlabel("moc wejściowa [mA]")
ax4.set_ylabel(r"sprawność różniczkowa ")
plt.legend(loc='upper right',prop={'size':16})
plt.grid(True)

plt.show()