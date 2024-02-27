#!/usr/bin/env python3
#
# ======================================================== #
# HOMEWORK 5: ITEM 2
# 
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez
#
#
# Last modification date: 02/25/2024
# Version: 1.0
# ======================================================== #
#
# Import libraries
import time
import numpy as np
import h5py

print('-------------------------------------------')
print('HW5 - ITEM 2 ')
print('-------------------------------------------')

# Load CSV files
st_A_csv = time.time()
A_csv = np.loadtxt('A.csv',delimiter=',',dtype='int64')
et_A_csv = time.time()
t_A_csv = et_A_csv - st_A_csv
print('Time [s] to load A.csv: %f' % t_A_csv)

st_B_csv = time.time()
B_csv = np.loadtxt('B.csv',delimiter=',',dtype='int8')
et_B_csv = time.time()
t_B_csv = et_B_csv - st_B_csv
print('Time [s] to load B.csv: %f' % t_B_csv)

st_C_csv = time.time()
C_csv = np.loadtxt('C.csv',delimiter=',',dtype='float64')
et_C_csv = time.time()
t_C_csv = et_C_csv - st_C_csv
print('Time [s] to load C.csv: %f' % t_C_csv)

st_D_csv = time.time()
D_csv = np.loadtxt('D.csv',delimiter=',',dtype='int16')
et_D_csv = time.time()
t_D_csv = et_D_csv - st_D_csv
print('Time [s] to load D.csv: %f' % t_D_csv)

st_E_csv = time.time()
E_csv = np.loadtxt('E.csv',delimiter=',',dtype='float32')
et_E_csv = time.time()
t_E_csv = et_E_csv - st_E_csv
print('Time [s] to load E.csv: %f' % t_E_csv)

print('-------------------------------------------')

# Load NPY files
st_A_npy = time.time()
A_npy = np.load('A.npy')
et_A_npy = time.time()
t_A_npy = et_A_npy - st_A_npy
print('Time [s] to load A.npy: %f' % t_A_npy)

st_B_npy = time.time()
B_npy = np.load('B.npy')
et_B_npy = time.time()
t_B_npy = et_B_npy - st_B_npy
print('Time [s] to load B.npy: %f' % t_B_npy)

st_C_npy = time.time()
C_npy = np.load('C.npy')
et_C_npy = time.time()
t_C_npy = et_C_npy - st_C_npy
print('Time [s] to load C.npy: %f' % t_C_npy)

st_D_npy = time.time()
D_npy = np.load('D.npy')
et_D_npy = time.time()
t_D_npy = et_D_npy - st_D_npy
print('Time [s] to load D.npy: %f' % t_D_npy)

st_E_npy = time.time()
E_npy = np.load('E.npy')
et_E_npy = time.time()
t_E_npy = et_E_npy - st_E_npy
print('Time [s] to load E.npy: %f' % t_E_npy)

print('-------------------------------------------')

# Load HDF5 matrices
f = h5py.File('matrix_db.hdf5','r+')

A_hdf5 = f['integer_group/matrix_A']
st_A_hdf5 = time.time()
A_arr = A_hdf5[...]
et_A_hdf5 = time.time()
t_A_hdf5 = et_A_hdf5 - st_A_hdf5
print('Time [s] to load A from hdf5: %f' % t_A_hdf5)

B_hdf5 = f['integer_group/matrix_B']
st_B_hdf5 = time.time()
B_arr = B_hdf5[...]
et_B_hdf5 = time.time()
t_B_hdf5 = et_B_hdf5 - st_B_hdf5
print('Time [s] to load B from hdf5: %f' % t_B_hdf5)

C_hdf5 = f['float_group/matrix_C']
st_C_hdf5 = time.time()
C_arr = C_hdf5[...]
et_C_hdf5 = time.time()
t_C_hdf5 = et_C_hdf5 - st_C_hdf5
print('Time [s] to load C from hdf5: %f' % t_C_hdf5)

D_hdf5 = f['integer_group/matrix_D']
st_D_hdf5 = time.time()
D_arr = D_hdf5[...]
et_D_hdf5 = time.time()
t_D_hdf5 = et_D_hdf5 - st_D_hdf5
print('Time [s] to load D from hdf5: %f' % t_D_hdf5)

E_hdf5 = f['float_group/matrix_E']
st_E_hdf5 = time.time()
E_arr = E_hdf5[...]
et_E_hdf5 = time.time()
t_E_hdf5 = et_E_hdf5 - st_E_hdf5
print('Time [s] to load E from hdf5: %f' % t_E_hdf5)

f.close()
