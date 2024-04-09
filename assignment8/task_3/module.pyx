# cython: wraparound=False
# cython: boundscheck=False
# cython: profile=True
# cython: initializedcheck=False
import cython
cimport cython

import  numpy as np
cimport numpy as np

cimport libc.math as cmath # Import c- math libraries.

import math # Math function in python

def func_matx_mult(np.ndarray[double, ndim=2] A_arr, np.ndarray[double, ndim=2] B_arr):
    """
    DESCRIPTION:
        This function performs the matrix multiplication.

    INPUTS:
        - A_arr, B_arr: (Array), input values to evaluate the function.
    """

    cdef int i
    cdef int j
    cdef int k
    
    cdef np.ndarray[double, ndim=2] C_arr = np.zeros((A_arr.shape[0], B_arr.shape[1]))

    for i in range( A_arr.shape[0] ):
        for j in range( B_arr.shape[1] ):
            for k in range( A_arr.shape[1] ):
                C_arr[i,j] = C_arr[i,j] + A_arr[i,k]*B_arr[k,j]
    # end for

    return C_arr

# end function
