import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

#- define the data
x = np.linspace(0., 1., 100)
y = np.random.randn(len(x))

#- plot it
ax = plt.gca()
ax.plot(x, y, 'k')

#- define your own locator based on ticker.LinearLocator
class MyLocator(ticker.LinearLocator):
   def tick_values(self, vmin, vmax):
       "vmin and vmax are the axis limits, return the tick locations here"
       return [vmin, 0.5 * (vmin + vmax), vmax]

#- initiate the locator and attach it to the current axis
ML = MyLocator()
ax.yaxis.set_major_locator(ML)

plt.show()
#- now, play with the zoom to see the y-ticks changing