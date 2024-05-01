# HPC
# HOMEWORK 12
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez. 
# Date: 05/21/2024
# ----------------------------------------------------- #

import cupy as cp
import time as time
import numpy as np


defK_kernel = cp.RawKernel(r'''
extern "C" __global__
void defK( double* K, int ncols, int nrows) {
    /*
    This function defines a square matrix K (row-major format) 
    with all elements in the diagonal as 4 and all elements 
    next to the diagonal as -2. The last element of the diagonal
    is set to 2. All other elements are set to zero.
    
    INPUTS: 
    - K: Pointer to the memory in K. 
    - nrows: Number of rows of the matrix.
    - ncols: Number of columns of the matrix.
    */
    
    // Define global indices of the threads along each direction.
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    int j = blockDim.y * blockIdx.y + threadIdx.y;   
    
    // Check that the i, j location lies within the matrix dimensions.
    if ( ( i < nrows) && ( j < ncols ) ){
        
        // Define the contiguous global index of the matrix.
        // i.e the index to access a single data point from the main 
        // pointer in K 
        // Consider the global indices as follows
        //
        // K_local = [[(0,0),(0,1),(0,2)],  // i,j indices for K.
        //            [(1,0),(1,1),(1,2)],
        //            [(2,0),(2,1),(2,2)]]
        //
        // K_g = [[ 0, 1, 2],  // global contiguous indices for K.
        //        [ 3, 4, 5],
        //        [ 6, 7, 8]]
        //
        // we use long long type (int64) because the 
        // integer value gets very large.
        //

        long long g_indx = i * ncols + j ;    
       
        if (i == j){
            if (j != ncols - 1){
                K[g_indx] = 4.0;
            }
            else{
                K[g_indx] = 2.0; 
            }
        }
        else if ((i == j + 1) || (i == j - 1)){
            K[g_indx] = -2;
        } 
        else{
            K[g_indx] = 0;
        }
    }
}
''', 'defK')

# Create the inputs. Must be defined with corresponding 
# types as in the raw kernel.

t_start = time.time()
N = 30000

K = cp.empty((N,N),dtype = cp.float64)

# Define the execution grid.
block_dim = 16
grid_dim  = N//block_dim+1 # Guarantee we send at least 1 grid.

# We are required to create the holder of the result.
# print("-")
defK_kernel((grid_dim,grid_dim,1), (block_dim,block_dim,1), ( K, K.shape[0],K.shape[1]))  # grid, block and arguments

# Create vector f
f = cp.zeros(N)
f[-1] = 1/N

u = cp.linalg.solve(K,f)
print('==================')
print('CUPY')
print('==================')
print('Solution vector u: ', u)
t_end = time.time()
print(f"Time spent creating the K and f, and solving the system of equations: {t_end-t_start:.6f} s.")
print('\n')

# Implementation in Numpy
ts_np = time.time()
# Create the matrix K
K_np = np.zeros((N,N))
for m in range (N):
    if m<N-1:
        K_np[m,m]=4
        if m==0:
            K_np[m,m+1]=-2
        else:
            K_np[m,m-1]=-2
            K_np[m,m+1]=-2
    else:
        K_np[m,m]=2
        K_np[m,m-1]=-2
    m+=1
  
# Create the matrix f
f_np = np.zeros((N,1))
f_np[N-1,0]=1/N


u_np = np.linalg.solve(K_np,f_np)
print('==================')
print('NUMPY')
print('==================')
print('Solution vector u: ', u_np)
te_np = time.time()
print(f"Time spent creating the K and f, and solving the system of equations: {te_np-ts_np:.6f} s.")
