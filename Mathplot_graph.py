import matplotlib.pyplot as plt 
import numpy as np
from math import pi

#u=
#v=0.5
a=3
b=1.5

ax1=np.linspace(0,2*pi, 100)
#plt.plot(a,b)
plt.plot(a*np.cos(ax1),b*np.sin(ax1), c = 'hotpink')
plt.plot(ls='dotted')
plt.title("Ellipse Figure")
plt.grid()
plt.show()