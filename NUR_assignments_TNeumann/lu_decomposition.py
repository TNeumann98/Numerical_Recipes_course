# # Numerical recipies
# Tutorial 3 (25.02.23)
# 
# Tina Neumann

# In[21]:
import numpy as np
### LU-decomposition via Crout's algorithm
# as described in lecture 3, slide 10-12
def LU_decomp(matrix):
    '''Function which does LU-decomposition via
    Crout's algorithm 
    input: the to decompose matrix
    output: decomposed L-/U-matrix
        + modified A-matrix
    '''
    lu_mat = matrix.copy()
    n = len(lu_mat)
    #define L-& U- matrix
    l_mat = np.zeros((n, n)) #L-decomposed matrix consisiting of alphas
    u_mat = np.zeros((n, n)) #U-decomposed matrix consisiting of betas

    for i in range(0, n):  # step 1: loop over the rows of A
        # set all alp = 1 for i = j
        l_mat[i][i] = 1.
        for j in range(0, n):  # step 2: loop over columns and
        # step 3: define beta-values for i <= j
            u_mat[0][j] = lu_mat[0][j]
            #slide 12
            sumab = 0 #to initialize sum
            for k in range(0,i): #loops till max-1
                sumab += l_mat[i][k]*u_mat[k][j]
                if  i <= j: 
                    u_mat[i][j] = lu_mat[i][j] - sumab
                else: #i>j : loop over aij
                    l_mat[i][j] = u_mat[j][j]**(-1)* (lu_mat[i][j] - sumab)
    
    a_matrix = l_mat + u_mat 
    return l_mat, u_mat, a_matrix


# In[34]:

### slide 16, solving system
def solve_LU(b,lmat,umat):
	x_sol = b.copy() #step 1: define x
	y_sol = b.copy() #step 1: define y (=Ux)

	for i in range(0,n): #step 2: loop over rows --> solving for y
	    #step 3 forward substituion
	    #slide 11
	    sumab = 0 #to initialize sum
	    for j in range(0,i): #loops till max-1
	    	sumab += lmat[i][j]*y_sol[j]
	    if i == 0:
	    	y_sol[0] = lmat[0][0]**(-1) * b[0]
	    else:
	    	y_sol[i] = lmat[i][i]**(-1) * (b[i] - sumab)
	for i in range(n-1,0+1): #step 4
	    #step 5 back-substituion (without swapping) --> solving for x
	    #slide 11
	    sumab = 0 #to initialize sum
	    for j in range(i+1,n): #loops till max-1
	    	sumab += umat[i][j]*x_sol[j]
	    if i == n-1:
	    	x_sol[n-1] = umat[n-1][n-1]**(-1) * y_sol[n-1]
	    else:
	    	x_sol[i] = umat[i][i]**(-1) * (y_sol[i] - sumab)
	return x_sol, y_sol
