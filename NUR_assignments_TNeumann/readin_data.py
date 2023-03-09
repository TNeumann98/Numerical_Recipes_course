# small script to predefine all needed parameters and packages for timeit

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

## Exercise 2.a) solve matrix via LU-decomposition
# create vandemonde-matrix as polynomial
vdM = []
for i in range(len(x)): #create rows
    row_x = []
    for j in range(len(x)): #create columns
        row_x.append(x[j]**j) #define polynomial for vandemonde-matrix

    vdM.append(row_x) #append polynomial for row elements, of same x value
lmat, umat, a_matrix = LU_decomp(vdM) #use code from Tut3
