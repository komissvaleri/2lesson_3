import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
x = np.arange(-10, 10, 1)
y = np.arange(-10, 10, 1)
x, y = np.meshgrid(x, y)
z = np.sqrt(x**2 + y**2)
ax.plot_surface(x, y, z)
show()