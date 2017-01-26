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
from scipy.optimize import curve_fit

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


class PlotLaserEfficiency:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        current, voltage, power = np.loadtxt(self.path_to_data, unpack=True, skiprows=1)
        self.current = current*1000
        self.voltage = voltage
        self.output_power = power * 1000

    def get_data(self):
        return self.current, self.voltage, self.output_power

    def get_input_power(self):
        # return value mW
        return self.current*self.voltage

    def get_output_power(self):
        # return value mW
        return self.output_power

    def get_ratio_power(self):
        input_power = self.get_input_power()
        return self.output_power / input_power

    def plot_wall_plug_efficiency(self):
        fig, ax1 = plt.subplots()
        input_power = self.get_input_power()
        ax1.plot(input_power, self.output_power, 'bo')
        ax1.set_xlabel("Moc wejściowa [mW]")
        ax1.set_ylabel("Moc wyjściowa [mW]")
        ax1.set_xlim([0, max(input_power)])
        plt.grid(True)
        plt.show()

    def plot_ratio_power_to_current(self):
        fig, ax1 = plt.subplots()
        input_power = self.current * self.voltage
        ratio_power = self.get_ratio_power()
        ax1.plot(self.current, ratio_power, 'bo')
        ax1.set_xlabel("Prąd [mA]")
        ax1.set_ylabel("Moc wyjściowa / Moc wejściowa")
        ax1.set_xlim([0, max(input_power)])
        plt.grid(True)
        plt.show()

    def plot_slope_efficiency_via_current(self, start_fit):
        fig, ax1 = plt.subplots()
        a, b, c = self.fit_via_current_poly_2(start_fit)
        x = np.linspace(start_fit, max(self.current))
        y = self.poly_2(x, a, b, c)
        ax1.plot(self.current, self.output_power, 'ro', markersize=4)
        ax1.plot(x, y, 'b-', linewidth=2)
        ax1.set_xlabel('Prąd [mA]')
        ax1.set_ylabel('Moc wyjściowa [mW]')
        plt.grid(True)
        plt.show()
        return x, y

    def plot_slope_efficiency_via_power(self, start_fit):
        fig, ax1 = plt.subplots()
        input_power = self.get_input_power()
        a, b, c = self.fit_via_power_poly_2(start_fit)
        x = np.linspace(start_fit, max(input_power))
        y = self.poly_2(x, a, b, c)
        ax1.plot(input_power, self.output_power, 'go', markersize=4)
        ax1.plot(x, y, 'b-', linewidth=2)
        ax1.set_xlim([0, max(input_power)])
        ax1.set_xlabel('Moc wejściowa [mA]')
        ax1.set_ylabel('Moc wyjściowa [mW]')
        plt.grid(True)
        plt.show()
        return x, y

    def fit_via_current_poly_2(self, start_fit):
        x_to_fit, y_to_fit = self.get_data_to_fit_via_current(start_fit)
        popt, pcov = curve_fit(self.poly_2, x_to_fit, y_to_fit)
        a = popt[0]
        b = popt[1]
        c = popt[2]
        error = np.abs(np.diag(pcov) ** 0.5)
        da = error[0]
        db = error[1]
        dc = error[2]
        print(self.path_to_data)
        print(u"a = %s \u00B1 %s" % (a, da))
        print(u"b = %s \u00B1 %s" % (b, db))
        print(u"c = %s \u00B1 %s" % (c, dc))
        return a, b, c

    def fit_via_power_poly_2(self, start_fit):
        x_to_fit, y_to_fit = self.get_data_to_fit_via_power(start_fit)
        popt, pcov = curve_fit(self.poly_2, x_to_fit, y_to_fit)
        a = popt[0]
        b = popt[1]
        c = popt[2]
        error = np.abs(np.diag(pcov) ** 0.5)
        da = error[0]
        db = error[1]
        dc = error[2]
        print(self.path_to_data)
        print(u"a = %s \u00B1 %s" % (a, da))
        print(u"b = %s \u00B1 %s" % (b, db))
        print(u"c = %s \u00B1 %s" % (c, dc))
        return a, b, c

    def fit_via_power_poly_3(self, start_fit):
        x_to_fit, y_to_fit = self.get_data_to_fit_via_power(start_fit)
        popt, pcov = curve_fit(self.poly_3, x_to_fit, y_to_fit)
        a = popt[0]
        b = popt[1]
        c = popt[2]
        d = popt[3]
        error = np.abs(np.diag(pcov) ** 0.5)
        da = error[0]
        db = error[1]
        dc = error[2]
        dd = error[3]
        print(self.path_to_data)
        print(u"a = %s \u00B1 %s" % (a, da))
        print(u"b = %s \u00B1 %s" % (b, db))
        print(u"c = %s \u00B1 %s" % (c, dc))
        print(u"d = %s \u00B1 %s" % (d, dd))
        return a, b, c, d

    def fit_step_by_step(self, start_fit, step):
        x_to_fit, y_to_fit = self.get_data_to_fit_via_power(start_fit)
        x_to_fit = x_to_fit[::3]
        y_to_fit = y_to_fit[::3]
        a = []
        x_a = []
        for i in range(0, len(x_to_fit)):
            try:
                popt, pcov = curve_fit(self.poly_1, x_to_fit[i:i + step], y_to_fit[i:i + step])
                a.append(popt[0])
                x_a.append(np.mean(x_to_fit[i:i+step]))
            except Exception as err:
                break
        fig, ax1 = plt.subplots()
        ax1.plot(x_a, a, 'bo')
        ax1.set_xlabel('Moc wejściowa [mW]')
        ax1.set_ylabel('Sprawność różniczkowa [W/A]')
        plt.grid(True)
        plt.show()
        return x_a, a

    def fit_step_by_step_via_current(self, start_fit, step):
        x_to_fit, y_to_fit = self.get_data_to_fit_via_current(start_fit)
        x_to_fit = x_to_fit[::3]
        y_to_fit = y_to_fit[::3]
        a = []
        x_a = []
        for i in range(0, len(x_to_fit)):
            try:
                popt, pcov = curve_fit(self.poly_1, x_to_fit[i:i + step], y_to_fit[i:i + step])
                a.append(popt[0])
                x_a.append(np.mean(x_to_fit[i:i + step]))
            except Exception as err:
                break
        fig, ax1 = plt.subplots()
        ax1.plot(x_a, a, 'bo')
        ax1.set_xlabel('Moc wejściowa [mW]')
        ax1.set_ylabel('Sprawność różniczkowa [W/A]')
        plt.grid(True)
        plt.show()
        return x_a, a

    @staticmethod
    def poly_1(x, a, b):
        return a*x + b

    @staticmethod
    def poly_2(x, a, b, c):
        return a*x**2 + b*x + c

    @staticmethod
    def poly_3(x, a, b, c, d):
        return a*x**3 + b*x**2 + c*x + d

    def get_data_to_fit_via_current(self, start_to_fit):
        x_to_fit = []
        y_to_fit = []
        for i in range(0, len(self.current)):
            if self.current[i] > start_to_fit:
                x_to_fit.append(self.current[i])
                y_to_fit.append(self.output_power[i])
        return np.array(x_to_fit), np.array(y_to_fit)

    def get_data_to_fit_via_power(self, start_to_fit):
        x_to_fit = []
        y_to_fit = []
        input_power = self.get_input_power()
        for i in range(0, len(input_power)):
            if input_power[i] > start_to_fit:
                 x_to_fit.append(input_power[i])
                 y_to_fit.append(self.output_power[i])
        return np.array(x_to_fit), np.array(y_to_fit)