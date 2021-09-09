import numpy as np
import matplotlib.pyplot as plt

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X1 = np.arange(-5, 5, 0.5)
Y1 = np.arange(-5, 5, 0.5)
X1, Y1 = np.meshgrid(X1, Y1)
Z1 = 2*X1 + 5*Y1
ax.plot_wireframe(X1, Y1, Z1)
ax.plot_wireframe(X1, Y1, Z1 + 10)


show()