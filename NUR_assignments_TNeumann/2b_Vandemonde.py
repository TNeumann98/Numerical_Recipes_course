# # Numerical recipies
# Assignment I, exercise 2 (09.03.23)
# 
# Tina Neumann

# In[1]:
import numpy as np
import sys
import os
import matplotlib.pyplot as plt

# copied vandermonde.py #script of van Daalen
data=np.genfromtxt(os.path.join(sys.path[0],"vandermonde.txt"),comments='#',dtype=np.float64)
x=data[:,0]
y=data[:,1]
xx=np.linspace(x[0],x[-1],1001) #x values to interpolate at


# In[7]:
# approximate values via Nevilles algorithm (Ex 2,2) on the basis of bi-section
from nevilles_algo import *

# plotting given data
plt.plot(x,y, '+', label = 'Measured data')

y_nev = []
err_nev = []
for a in xx:
    y2, derr = nevilles_algo(a,x,y)
    y_nev.append(y2)
    err_nev.append(derr)
    

plt.plot(xx,y_nev, '-', alpha = 0.6, label = 'Interpolation with Nevilles algo')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-400,400)
plt.title('Interpolation of Lagrangian polynom via Nevilles algorithm')
plt.legend()
plt.savefig('./plots/2b_NevillesAlgo.pdf')
plt.show()

# vizualize the error produced through nevilles algo
# check diffence in y-value between given values and of nevilles algo produced
for i in range(len(x)):
    # write workaround (for .index()-to find the closest index) through smallest difference
    ind = np.abs(xx-x[i]).argmin()
    dy_nev = abs(y[i]-y_nev[ind])
    plt.plot(x[i],dy_nev, marker = '+', color = 'blue') #, label = 'Error of Nevilles algo')
plt.plot(x[-1],dy_nev, marker = '+', color = 'blue', label = 'Error of Nevilles algo') #to obtain label
    
    
plt.xlabel('x')
plt.ylabel(r'|$\Delta$ y|')
plt.title('Error comparison of Lagrangian polynom')
plt.legend()
plt.savefig('./plots/2b_NevillesAlgo_error.pdf')
plt.show()
