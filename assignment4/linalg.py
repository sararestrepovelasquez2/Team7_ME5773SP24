#
# =================
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez
#
# Last modification: 02/16/2024
# Version 1.0
# =================
#
import numpy as np
import time

N=10**4
print('N = %d' % N)

t_mStart = time.time()

# Create the matrix 𝐊
K = np.zeros((N,N))
for i in range (N):
    if i<N-1:
        K[i,i]=2
        if i==0:
            K[i,i+1]=-1
        else:
            K[i,i-1]=-1
            K[i,i+1]=-1
    else:
        K[i,i]=1
        K[i,i-1]=-1
    i+=1

# Create the matrix f
f = np.zeros((N,1))
f[N-1,0]=1/N

t_mEnd = time.time()
T_createMatrix = t_mEnd-t_mStart
print('Time create matrix K and f: %.9f' % T_createMatrix)

t_sStart = time.time()

# Solving for 𝐮
u = np.matmul(np.linalg.inv(K),f)

t_sEnd = time.time()

T_solveU = t_sEnd-t_sStart
print('Time solve u: %.9f' % T_solveU)

print('u[N] = ',end="")
print(u[N-1])

