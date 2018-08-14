# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

temp = [.3, 4.1, 7.1, 10.5, 14.5, 23.3]
freq = [404.39, 404.61, 404.90, 405.03, 405.33, 405.97]

fit = np.polyfit(temp, freq, 1)
fit = np.poly1d(fit)

ax.plot( temp, fit(temp), linestyle='--', alpha=.5, color='b', label='fit: 0.068 * Temperature + 404.3')
ax.plot( temp, freq, linestyle='none', color='b', marker='o')
ax.legend()
ax.set_xlabel(r'Diode Temperature ($\degree$C)')
ax.set_ylabel('Wavelength (nm)')

fig.show()