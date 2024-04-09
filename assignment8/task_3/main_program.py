import module as md
import numpy as np
import math
import time
import numba


# Pure python function
def func_eval(x_arr):
    """
    DESCRIPTION:
        This function evaluates the sin(x)*cos(x) for an array of values.

    INPUTS:
        - x_arr: (Array), input values to evaluate the function.
    """

    res = np.empty_like(x_arr)

    for i in range( x_arr.shape[0] ):
        res[i] = math.sin(x_arr[i])*math.cos(x_arr[i])+3
    # end for

    return res

# end function


A_arr_3 = np.random.rand(3,3)
B_arr_3 = np.random.rand(3,3)

A_arr_10 = np.random.rand(10,10)
B_arr_10 = np.random.rand(10,10)

A_arr_100 = np.random.rand(100,100)
B_arr_100 = np.random.rand(100,100)

A_arr_1000 = np.random.rand(1000,1000)
B_arr_1000 = np.random.rand(1000,1000)

n = 100 #number of iterations

#matrix size 3x3 multiplication
t_start = time.time()
for i in range( n ):
    C_arr_3 = md.func_matx_mult( A_arr_3, B_arr_3)
t_end = time.time()
print('Time spent on matrix 3x3: {0:.6f} s -- Cython'.format((t_end-t_start)/n))

t_start = time.time()
for i in range( n ):
    C_arr_3 = np.dot( A_arr_3, B_arr_3)
t_end = time.time()
print('Time spent on matrix 3x3: {0:.6f} s -- Numpy dot'.format((t_end-t_start)/n))


#matrix size 10x10 multiplication
t_start = time.time()
for i in range( n ):
    C_arr_10 = md.func_matx_mult( A_arr_10, B_arr_10)
t_end = time.time()
print('Time spent on matrix 10x10: {0:.6f} s -- Cython'.format((t_end-t_start)/n))

t_start = time.time()
for i in range( n ):
    C_arr_10 = np.dot( A_arr_10, B_arr_10)
t_end = time.time()
print('Time spent on matrix 10x10: {0:.6f} s -- Numpy dot'.format((t_end-t_start)/n))


#matrix size 100x100 multiplication
t_start = time.time()
for i in range( n ):
    C_arr_100 = md.func_matx_mult( A_arr_100, B_arr_100)
t_end = time.time()
print('Time spent on matrix 100x100: {0:.6f} s -- Cython'.format((t_end-t_start)/n))

t_start = time.time()
for i in range( n ):
    C_arr_100 = np.dot( A_arr_100, B_arr_100)
t_end = time.time()
print('Time spent on matrix 100x100: {0:.6f} s -- Numpy dot'.format((t_end-t_start)/n))


#matrix size 1000x1000 multiplication
t_start = time.time()
for i in range( n ):
    C_arr_1000 = md.func_matx_mult( A_arr_1000, B_arr_1000)
t_end = time.time()
print('Time spent on matrix 1000x1000: {0:.6f} s -- Cython'.format((t_end-t_start)/n))

t_start = time.time()
for i in range( n ):
    C_arr_1000 = np.dot( A_arr_1000, B_arr_1000)
t_end = time.time()
print('Time spent on matrix 1000x1000: {0:.6f} s -- Numpy dot'.format((t_end-t_start)/n))

