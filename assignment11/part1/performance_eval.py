# ----------------------------------------------------- #
# HPC - HOMEWORK 11 - PART 1 
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez
# Date: 04/25/2024
# ----------------------------------------------------- #

import numpy as np
import searchUtilsTeam07 as search
import time

num_elem = 10**7

sort_arr = np.linspace(-10, 10, num_elem, dtype = np.float64)
unsort_arr = np.linspace(-10, 10, num_elem, dtype = np.float64)
np.random.shuffle(unsort_arr)

x_sort = sort_arr[-2]
x_unsort = unsort_arr[-2]

print('----------------------------------------')
print('Search Algorithms Performance Evaluation')
print('----------------------------------------')
print('The second to last element will be searched in all arrays.')
print('\n')
print('Value sought in sorted array: ', x_sort)
print('Value sought in unsorted array: ', x_unsort)
print('\n')

print('---------------------------')
print('Fortran Linear Search Test:')
print('---------------------------')
ts_1 = time.time()
idx1 = search.searchutils.linearsearch(sort_arr,x_sort,num_elem)
te_1 = time.time()
t_1 = te_1 - ts_1
print('For the sorted array, the value was found at index: ', idx1)
print('CPU time [s]: ', t_1)  
print('\n')

ts_2 = time.time()
idx2 = search.searchutils.linearsearch(unsort_arr,x_unsort,num_elem)
te_2 = time.time()
t_2 = te_2 - ts_2
print('For the unsorted array, the value was found at index: ', idx2)
print('CPU time [s]: ', t_2)  
print('\n')

print('---------------------------')
print('Fortran Binary Search Test:')
print('---------------------------')
ts_3 = time.time()
idx3 = search.searchutils.binarysearch(sort_arr,x_sort,num_elem)
te_3 = time.time()
t_3 = te_3 - ts_3
print('For the sorted array, the value was found at index: ', idx3)
print('CPU time [s]: ', t_3)  
print('\n')

print('------------------------')
print('Numpy SearchSorted Test:')
print('------------------------')
ts_4 = time.time()
idx4 = np.searchsorted(sort_arr,x_sort)
te_4 = time.time()
t_4 = te_4 - ts_4
print('For the sorted array, the value was found at index: ', idx4)
print('CPU time [s]: ', t_4)  
print('\n')

print('-----------------')
print('Numpy Where Test:')
print('-----------------')
ts_5 = time.time()
idx5 = np.where(sort_arr == x_sort)
te_5 = time.time()
t_5 = te_5 - ts_5
print('For the sorted array, the value was found at index: ', idx5)
print('CPU time [s]: ', t_5)  
print('\n')

ts_6 = time.time()
idx6 = np.where(unsort_arr == x_unsort)
te_6 = time.time()
t_6 = te_6 - ts_6
print('For the unsorted array, the value was found at index: ', idx6)
print('CPU time [s]: ', t_6)  
