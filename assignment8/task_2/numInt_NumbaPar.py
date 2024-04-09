# ================================================== #
# HPC - Homework 8
#
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez
# Date: 04/08/2024
# ================================================== #

import numpy as np
import time
import numba
from numba import jit, prange

@jit(nopython=True)
def myfunct(x):
    """
    Defines the function to be integrated.

    INPUTS:
    - x: double, evaluation point.

    OUTPUTS:
    - double, evaluated function.
    
    """

    return np.sin(x*x)+x/2

# end function

@jit(nopython=True, parallel=True)
def integral_riemann(a,b,N):
    """
    Implements the Riemann integration for the function
    myfunct(x).

    INPUTS:
    - a: double, Lower integration limit.
    - b: double, Upper integration limit.
    - N: Int, Number of integration regions.

    OUTPUTS:
    - double, evaluated integral.
    
    """
    dx = (b-a)/N
    F = 0
    
    for i in prange(N):
        x = a + i*dx
        F += myfunct(x)*dx
    # end for 

    return F

# end function

if __name__ == '__main__':

        numba.set_num_threads(1)
        # Dummy call
        print('-----------------')
        print('DUMMY CALL')
        print('-----------------')
        # If needed, add dummy call to the integral_riemann
        # function here

        # Evaluate the CPU time and integration here.

        t_start = time.time()
        a = 0
        b = 2
        N = 100 # 100_000_000 # 10**8 
        F = integral_riemann(a,b,N)
        t_end = time.time()


        print('Integral {0:f}'.format(F))
        print('CPU time:{0:.6f}s'.format(t_end-t_start))
    
        p_arr = np.array([1, 2, 4, 8, 16, 20])

        for j in p_arr:
            print(':::::::::::::::::::::::::::::::::::::::::')
            print('PROCESSORS: {0:f}'.format(j))
            print(':::::::::::::::::::::::::::::::::::::::::')
        
            numba.set_num_threads(j)

            # Real call
            print('-----------------')
            print('REAL CALL')
            print('-----------------')


            t_start = time.time()
            a = 0
            b = 2
            N = 100_000_000 # 10**8 
            F = integral_riemann(a,b,N)
            t_end = time.time()


            print('Integral {0:f}'.format(F))
            print('CPU time:{0:.6f}s'.format(t_end-t_start))

            # end for. 

# end if
