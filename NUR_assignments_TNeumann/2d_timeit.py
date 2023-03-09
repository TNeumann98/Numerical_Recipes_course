# # Numerical recipies
# Assignment I, exercise 2 (09.03.23)
# 
# Tina Neumann

# In[1]:
import timeit
import os
import matplotlib.pyplot as plt
import numpy as np
import sys

## Exercise 2.d) time routines with appropiate 'parameters`
repeat = int(1e2) #default 1e7: choose so that code runs below <1min

## Exercise 2.a) solve matrix via LU-decomposition
# create vandemonde-matrix as polynomial
print('The following time is needed to apply LU-decomposition and solve with the vandemonde-matrix the equation for c takes [sec]:')
print(timeit.timeit('lmat, umat, a_matrix = LU_decomp(vdM);xsol, ysol = solve_LU(y,lmat,umat,len(y))', setup = 'from readin_data import x,y,vdM,LU_decomp,solve_LU',number = repeat))


## Exercise 2.b) interpolation with nevilles algorithm
print('The time required to interpolate the matrix with Nevilles algorithm is [sec]:')
print(timeit.timeit('y_nev=[];err_nev=[];[nevilles_algo(a,x,y) for a in xx]', setup = 'from readin_data import nevilles_algo,xx,x,y',number = repeat))

## Exercise 2.c) solve matrix via 10xLU-decomposition
print('The time required to interpolate via 10-times LU-decomposition solving [sec]:')
print(timeit.timeit('xsol10 = y;[xsol10 = np.subtract(y, solve_LU(xsol10,lmat,umat,len(xsol10)[0])) for l in range(10)]', setup = 'from readin_data import xx,x,y,vdM,LU_decomp,solve_LU',number = repeat))
