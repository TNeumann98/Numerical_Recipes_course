#!/usr/bin/env python
# coding: utf-8

# # Numerical recipies
# Assignment (09.03.23)
# 
# Tina Neumann

# In[28]:


import numpy as np
import timeit


# In[40]:


### Exercise 1: Poisson distribution
# define given distribution
def poiss_32(lam, k):
    '''Function determines the poisson distribution P(k) of
    input: a positive mean (lam) and an integer (k)
    output: P(k)'''
    lam = np.float32(lam) #redefine as 32-bit integers
    k = np.int32(k)
    # to decrease the calculation time:
    # multiply by inverse instead of dividing
    # the values are considered to be in log-scale: log(products)--> sums
    # define k!
    f_frac = 1.
    for f in range(1,k): #range leaves out last element
        f_frac += np.log(f)

    log_p = np.int32(k)*np.log(np.float32(lam)) - np.float32(lam) - np.int32(f_frac) #logarithmic P(k)
    p = np.exp(np.float32(log_p)) #revert log-scale
    print('k! = ', f_frac)
    print('log(P(k)) = ', log_p)
    return p


# In[41]:


def poiss_64(lam, k):
    '''Function determines the poisson distribution P(k) of
    input: a positive mean (lam) and an integer (k)
    output: P(k)'''
    lam = np.float64(lam) #redefine as 64-bit integers
    k = np.int64(k)
    # define k!
    f_frac = 1.
    for f in range(1,k): #range leaves out last element
        f_frac *= f

    log_p = k*np.log(lam) - lam - np.log(f_frac) #logarithmic P(k)
    p = np.exp(log_p) #revert log-scale
    print('k! = ', f_frac)
    print('log(P(k)) = ', log_p)
    return p


# In[42]:


from scipy.special import factorial
def poiss(lam, k):
    '''Function determines the poisson distribution P(k) of
    input: a positive mean (lam) and an integer (k)
    output: P(k)'''
    lam = float(lam)
    k = np.int64(k)
    #with numpy functions
    # define k!
    try:
        f_frac = factorial(k)
        p = lam**k*np.exp(-lam)*f_frac**(-1)
    except:
        print('OverflowError (34, Numerical result out of range')
        p = 'nan(OverflowError)'
    return p


# In[43]:
# Save output as a text file
with open("1_PoissonDistribution.txt", "w") as file:
    file.write('# The given lambda, k \n# \t \t results for 32-bit data types for the Poisson-distribution P(k) \n# \t \t \t \t P(k) for 64-bit types \n# \t \t \t \t  \t \t P(k) calculated with scipy \n')
# read-in given values
with open('input_1a.txt') as f:
    lines = f.readlines()[2:]
    for line in lines:
            #define lambda, k
            mean_lam, k_int = line.split('\t')
            print(mean_lam,k_int)

            k_int = k_int[:-1] #str has additional '\n'
            print('The given values are lam & k: '+ mean_lam, ' & '+ k_int)
            
            # add values to output file
            with open("1_PoissonDistribution.txt", "a+") as file:
                file.write(str(mean_lam+'\t'+k_int+'\t'+f'{poiss_32(mean_lam,k_int):.6E}'+'\t'+f'{poiss_64(mean_lam,k_int):.6E}'+'\t'+f'{poiss(mean_lam,k_int):.6E}'+'\n'))
            print('For 32 bits this results in a poisson distribution of P(k) = ', f'{poiss_32(mean_lam,k_int):.6E}') #print 6 relevant digits
            print('For 64 bits this results in a poisson distribution of P(k) = ', f'{poiss_64(mean_lam,k_int):.6E}') #print 6 relevant digits
            print('For numpy-functions this results in a poisson distribution of P(k) = ', f'{poiss(mean_lam,k_int):.6E}') #print 6 relevant digits
