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
from lu_decomposition import *

# plotting given data
plt.plot(x,y, '+', label = 'Given data points')

## Exercise 2.a) solve matrix via LU-decomposition
# create vandemonde-matrix as polynomial
vdM = []
for i in range(len(x)): #create rows
    row_x = []
    for j in range(len(x)): #create columns
        row_x.append(x[j]**j) #define polynomial for vandemonde-matrix

    vdM.append(row_x) #append polynomial for row elements, of same x value
        
lmat, umat, a_matrix = LU_decomp(vdM) #use code from Tut3
xsol, ysol = solve_LU(y,lmat,umat,len(y))
plt.plot(x, xsol, ':', alpha = 0.6, label = 'Interpolation with LU-decomposition')

## Exercise 2.b) interpolation with nevilles algorithm
y_nev = []
err_nev = []
for a in xx:
    y2, derr = nevilles_algo(a,x,y) #cal create function of Tut2
    y_nev.append(y2)
    err_nev.append(derr)
    
plt.plot(xx, y_nev, '-', alpha = 0.6, label = 'Interpolation with Nevilles algo')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-400,400)
plt.title('Interpolation of Lagrangian polynom')
plt.legend()
plt.savefig('./plots/2_Interpolation_Algos.pdf')
plt.show()

### calculate the y-error produced (variance from given values) by
# 2.a) LU-decomposition
err_lu = []
for m in range(len(xsol)):
    err_lu.append(abs(y[i]-xsol[i]))
print(err_lu)
plt.plot(x, err_lu, marker = '*', color = 'orange', label = 'Error of LU-decomposition')
# 2.b) through nevilles algo
# check diffence in y-value between given values and of nevilles algo produced
for i in range(len(x)):
    # write workaround (for .index()-to find the closest index) through smallest difference
    ind = np.abs(xx-x[i]).argmin()
    dy_nev = abs(y[i]-y_nev[ind])
    plt.plot(x[i],dy_nev, marker = '+', color = 'blue') #, label = 'Error of Nevilles algo')
plt.plot(x[-1],dy_nev, marker = '+', color = 'blue', label = 'Error of Nevilles algo') #to obtain label
    
plt.xlabel('x')
plt.ylabel(r'|$\Delta$ y|')
plt.yscale('log')
plt.title('Error comparison of Lagrangian polynom')
plt.legend()
plt.savefig('./plots/2_interpolation_error.pdf')
plt.show()
