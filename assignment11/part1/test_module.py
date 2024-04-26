# ----------------------------------------------------- #
# HPC - HOMEWORK 11 - PART 1 
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez
# Date: 04/25/2024
# ----------------------------------------------------- #

import numpy as np
import searchUtilsTeam07 as search

num_elem = 10

sort_arr = np.linspace(-10, 10, num_elem, dtype = np.float64)
unsort_arr = np.linspace(-10, 10, num_elem, dtype = np.float64)
np.random.shuffle(unsort_arr)

x_sort = sort_arr[-2]
x_unsort = unsort_arr[-2]

print('----------------------')
print('Search Algorithms Test')
print('----------------------')
print('The second to last element will be searched in all arrays.')
print('\n')
print('Sorted array: ',sort_arr)
print('Value sought in this array: ', x_sort)
print('Unsorted array: ',unsort_arr)
print('Value sought in this array: ', x_unsort)
print('\n')
print('----------------------')
print('Linear Search Test:')
print('----------------------')
idx1 = search.searchutils.linearsearch(sort_arr,x_sort,num_elem)
idx2 = search.searchutils.linearsearch(unsort_arr,x_unsort,num_elem)
print('For the sorted array, the value was found at index: ', idx1)
print('For the unsorted array, the value was found at index: ', idx2)
print('\n')
print('----------------------')
print('Binary Search Test:')
print('----------------------')
idx3 = search.searchutils.binarysearch(sort_arr,x_sort,num_elem)
print('For the sorted array, the value was found at index: ', idx3)
