#!/usr/bin/env python3

# ===================================================== #
# ITEM 3


# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez

# Last modification date: 02/15/2024
# Version: 1.0
# ===================================================== #

# Import libraries
import numpy as np
import math as mt
import numexpr as nexp
import time

# Definition of variables
N = 10**9
deltax = 2/N

# 3.2. Using a For loop
# ===================== #
F1 = 0
start_t_32 = time.time() 
for i in range(1,N+1):
    xi = (2 * i / N) - 1
    fxi = mt.sqrt(4 - 4 * xi**2)
    F1 = F1 + fxi * deltax
end_t_32 = time.time()
F1_time = end_t_32 - start_t_32
print('---------')
print('ITEM 3.2.')
print('---------')
print('Time to compute F1: ','{:.6f}'.format(F1_time),' [s].')
print('The value of F1 is: ','{:.16f}'.format(F1))

# 3.3. Using numpy's vectorized functions
# ======================================= #
start_t_33 = time.time()
i_vec = np.arange(1,N+1)
x_vec = (2 * i_vec / N) - 1
F_vec = np.sqrt(4 - 4 * x_vec**2) * deltax
F2 = np.sum(F_vec)
end_t_33 = time.time()
F2_time = end_t_33 - start_t_33
print('---------')
print('ITEM 3.3.')
print('---------')
print('Time to compute F2: ','{:.6f}'.format(F2_time),' [s].')
print('The value of F2 is: ','{:.16f}'.format(F2))

# 3.4. Using numexpr evaluations
# ============================== #
start_t_34 = time.time()
i_vec = np.arange(1,N+1)
x_vec = nexp.evaluate('(2 * i_vec / N) - 1')
F_vec = nexp.evaluate('sqrt(4 - 4 * x_vec**2) * deltax')
F3 = nexp.evaluate('sum(F_vec)') 
end_t_34 = time.time()
F3_time = end_t_34 - start_t_34
print('---------')
print('ITEM 3.4.')
print('---------')
print('Time to compute F3: ','{:.6f}'.format(F3_time),' [s].')
print('The value of F3 is: ','{:.16f}'.format(F3))























