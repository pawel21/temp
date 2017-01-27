import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'

kT = 0.00257

def fun_fermi(E, kT):
    E_f = 0.55
    return 1/( 1 + np.exp((E-E_f)/kT))

E = np.linspace(0, 1, 1000)
fermi_10 = fun_fermi(E, 0.0086)
fermi_300 = fun_fermi(E, 0.0259)
fermi_450 = fun_fermi(E, 0.039)

ax1 = plt.subplot()
ax1.plot(E, fermi_10, 'b-', label="10\,K", linewidth=2)
ax1.plot(E, fermi_300, 'g-', label="300\,K", linewidth=2)
ax1.plot(E, fermi_450, 'r-', label="450\,K", linewidth=2)
plt.legend()
plt.grid(True)

plt.show()