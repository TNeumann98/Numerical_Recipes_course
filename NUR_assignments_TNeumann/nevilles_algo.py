# # Numerical recipies
# from Tutorial 2 (16.02.23)
# 
# Tina Neumann

### Exercise 1
import numpy as np
import matplotlib.pyplot as plt

def linspace(xmin,xmax,step):
    linarr = []
    dstep = (xmax-xmin)/step
    for s in range(step+1):
        linarr.append(xmin+s*dstep)
    return linarr

## 1.a) linear interpolation
def lin_interp(j_low,ind,x,y):
        try:
            dx = x[j_low+1]-x[j_low]
            dy = y[j_low+1]-y[j_low]
        except: #use slope of previous points
            dx = x[j_low]-x[j_low-1]
            dy = y[j_low]-y[j_low-1]
        m = dy/dx
        y_span = m*(ind-x[j_low]) + y[j_low] # equation of lecture II, slide 9 #n = -m*x[j_low]+y[j_low]   
        return y_span

    
def interp_algo(span,x,y):
    '''
    Linear interpolation via 
    bisection algorithm
    span: range within the algo should interpolate
    x: given x data (assuming that this is sorted)
    y: given y data
    ----------------
    return
    pos: x and y value of interpolated point
    '''
    ran = linspace(0,len(span),len(span))
    x_pos =  [] #save x and y position seperate
    y_pos = []
    v = 0
    while v != len(ran)-1: #iterate through all values of given interpolation x-range
        bi1 = 0
        bi2 = int(len(x)/2) #define index of bisection (!for even N +odd N (lower index via int()))
        bi3 = len(x)-1
        
        #bisection algorithm
        #find nearest lower index (jlow)
        while True:
            if x[bi1] <= span[v] < x[bi2]: #first half (bi1 stays)
                bi3 = bi2
                bi2 = int(bi1+(bi2-bi1)/2) 
            elif x[bi2]<= span[v] <= x[bi3]: #second half (bi3 stays)
                bi1 = bi2
                bi2 = int(bi2+(bi3-bi2)/2)
            if bi1 == bi2 or bi3 == bi2:
                break

        j_low = bi1 # j_low == index left of x value in span
        
        #call function for interpolation seperatelye
        y_span = lin_interp(j_low,span[v],x,y) 
        x_pos.append(span[v])
        y_pos.append(y_span)
        v += 1
        
    return x_pos, y_pos

# In[61]:


## 1.b) interpolation with nevilles algorithm 
### lecture 2, slide 10
def nevilles_algo(span,x,y):
    '''
    polynomial interpolation via 
    Neville's algorithm 
    span: points where to evaluate
    x: in bisection pre-determined x-values
    y: in bisection pre-determined y-values
    ----------------
    return
    pos: x and y value of interpolated point
    '''
    yPi = []
    derr = []
    # use recipe on slide 11
    # 1.) use bisection of 1.a) / 2.) set initial Pi as their y-values

    m = len(x) #len(given x-values) number of points (Pi)
    Pi = y.copy() #to avoid overwriting
    #from Tut2, 1.a)
    #for xx in span:
    for k in range(1,m+1):     #step 4
        for i in range(0,m-k): #step 5, current interval [xi,x(i+k)]
            j =  i + k #define j index
            # H(x)
            h = ((x[j]-span)*Pi[i] + (span-x[i])*Pi[i+1])/(x[j]-x[i])
            Pi[i] = h #step 6 (update / overwrite the p-value)

    yPi.append(Pi[0]) #append last remaining P-value
    derr.append(abs(Pi[2]-Pi[1])) # step 7: save error as difference of last values

    return yPi, derr # return y-value and its error
