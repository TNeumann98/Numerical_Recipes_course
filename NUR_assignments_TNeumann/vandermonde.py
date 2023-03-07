#This script is to get you started with reading the data and plotting it
#You are free to change whatever you like/do it completely differently

import numpy as np
import sys
import os
import matplotlib.pyplot as plt

data=np.genfromtxt(os.path.join(sys.path[0],"Vandermonde.txt"),comments='#',dtype=np.float64)
x=data[:,0]
y=data[:,1]
xx=np.linspace(x[0],x[-1],1001) #x values to interpolate at

fig,ax=plt.subplots()
ax.plot(x,y,marker='o',linewidth=0)
plt.xlim(-1,101)
plt.ylim(-400,400)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.show()
