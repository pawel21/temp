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

E = np.linspace(0, 1.2, 1000)
fermi_10 = fun_fermi(E, 0.0086)
fermi_300 = fun_fermi(E, 0.0259)
fermi_450 = fun_fermi(E, 0.039)

ax1 = plt.subplot(121)
ax1.plot(fermi_10, E,'b-', label="10\,K", linewidth=2)
ax1.plot(fermi_300, E,'g-', label="300\,K", linewidth=2)
ax1.plot(fermi_450, E, 'r-', label="450\,K", linewidth=2)
ax1.plot([-0.1, 1.1], [0.55, 0.55], 'k--', linewidth=3)
ax1.text(0.15, 0.48, "Poziom fermiego")
ax1.set_xlim([-0.1, 1.1])
ax1.set_xlabel("prawdopodobieństwa ")
ax1.set_ylabel("energia [eV]")

plt.legend()
plt.grid(True)

ax1 = plt.subplot(122)
ax1.plot(E, fermi_10, label="10\,K", linewidth=2)
ax1.plot(E, fermi_300, label="300\,K", linewidth=2)
ax1.plot(E, fermi_450, label="450\,K", linewidth=2)
ax1.set_ylabel("prawdopodobieństwa ")
ax1.set_xlabel("energia [eV]")
ax1.set_ylim([-0.1, 1.1])
ax1.text(0.55, 0.6, r"$f(E) = \frac{1}{1 + \exp(\frac{E-E_f}{kT})}$")
plt.grid(True)
plt.show()