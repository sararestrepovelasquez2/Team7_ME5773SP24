#!/usr/bin/env python3
#
# =====================================================
# ITEM 3
#
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez
#
#
# Last modification date: 02/24/2024
# Version: 1.0
# =====================================================
#
#
# Import libraries
import time
import numpy as np
import h5py


# Create matrix A
A = np.zeros([5000,5000],order='F',dtype='int64')
for i in range(len(A)):
    for j in range(len(A[0])):
        A[i,j] = np.random.randint(2,9)

# Create matrix B
B = np.zeros([5000,5000],order='C',dtype='int8')
for i in range(len(B)):
    for j in range(len(B[0])):
        B[i,j] = np.random.randint(100,127)

# Create matrix C
C = np.zeros([5000,5000],order='C',dtype='float64')
for i in range(len(C)):
    for j in range(len(C[0])):
        C[i,j] = 0.33333

# Create matrix D
D = np.zeros([10,10],order='F',dtype='int16')
d=1001
for i in range(len(D)):
    for j in range(len(D[0])):
        D[i,j] = d
        d=D[i,j]+1

# Create matrix E
E = np.array([[350.0, 350.1],
              [350.2, 350.3]], order='C', dtype='float32')




# Save as csv file.
t1_aStart=time.time()
np.savetxt('A.csv',A,delimiter=',',fmt="%d")
t1_aEnd=time.time()

t1_bStart=time.time()
np.savetxt('B.csv',B,delimiter=',',fmt="%d")
t1_bEnd=time.time()

t1_cStart=time.time()
np.savetxt('C.csv',C,delimiter=',',fmt="%.18e")
t1_cEnd=time.time()

t1_dStart=time.time()
np.savetxt('D.csv',D,delimiter=',',fmt="%d")
t1_dEnd=time.time()

t1_eStart=time.time()
np.savetxt('E.csv',E,delimiter=',',fmt="%.7e")
t1_eEnd=time.time()


# Print CSV file generating time
T1_a = t1_aEnd - t1_aStart
print('Time to generate A.csv: %f' % T1_a)

T1_b = t1_bEnd - t1_bStart
print('Time to generate B.csv: %f' % T1_b)

T1_c = t1_cEnd - t1_cStart
print('Time to generate C.csv: %f' % T1_c)

T1_d = t1_dEnd - t1_dStart
print('Time to generate D.csv: %f' % T1_d)

T1_e = t1_eEnd - t1_eStart
print('Time to generate E.csv: %f' % T1_e)




# Save as numpy array.
t2_aStart=time.time()
np.save('A.npy',A)
t2_aEnd=time.time()

t2_bStart=time.time()
np.save('B.npy',B)
t2_bEnd=time.time()

t2_cStart=time.time()
np.save('C.npy',C)
t2_cEnd=time.time()

t2_dStart=time.time()
np.save('D.npy',D)
t2_dEnd=time.time()

t2_eStart=time.time()
np.save('E.npy',E)
t2_eEnd=time.time()


# Print NPY file generating time
T2_a = t2_aEnd - t2_aStart
print('Time to generate A.npy: %f' % T2_a)

T2_b = t2_bEnd - t2_bStart
print('Time to generate B.npy: %f' % T2_b)

T2_c = t2_cEnd - t2_cStart
print('Time to generate C.npy: %f' % T2_c)

T2_d = t2_dEnd - t2_dStart
print('Time to generate D.npy: %f' % T2_d)

T2_e = t2_eEnd - t2_eStart
print('Time to generate E.npy: %f' % T2_e)




# Generate an HDF5 file:
f = h5py.File("matrix_db.hdf5", "w")


# Generate integer group with description attribute.
integer_g = f.create_group('integer_group')
integer_g.attrs['description'] = 'Stores elements with integer values.'


# Generate datasets for integer elements.
t3_aStart = time.time()
dset_A = integer_g.create_dataset('matrix_A',shape=(5000,5000),
							chunks=(500,500), dtype=np.int64,
							compression='gzip')
dset_A[...] = A
t3_aEnd = time.time()

t3_bStart = time.time()
dset_B = integer_g.create_dataset('matrix_B',shape=(5000,5000),
							chunks=(1000,1000), dtype=np.int8,
							compression='gzip')
dset_B[...] = B
t3_bEnd = time.time()

t3_dStart = time.time()
dset_D = integer_g.create_dataset('matrix_D',shape=(10,10),
							dtype=np.int16)
dset_D[...] = D
t3_dEnd = time.time()



# Generate float group with description attribute.
float_g = f.create_group('float_group')
float_g.attrs['description'] = 'Stores elements with float values.'


# Generate datasets for float elements.
t3_cStart = time.time()
dset_C = float_g.create_dataset('matrix_C',shape=(5000,5000),
							    dtype=np.float64,compression='gzip')
dset_C[...] = C
t3_cEnd = time.time()

t3_eStart = time.time()
dset_E = float_g.create_dataset('matrix_E',shape=(2,2),
							    dtype=np.float32)
dset_E[...] = E
t3_eEnd = time.time()

f.close()


# Print hdf5 file generating time
T3_a = t3_aEnd - t3_aStart
print('Time to create database A: %f' % T3_a)

T3_b = t3_bEnd - t3_bStart
print('Time to create database B: %f' % T3_b)

T3_c = t3_cEnd - t3_cStart
print('Time to create database C: %f' % T3_c)

T3_d = t3_dEnd - t3_dStart
print('Time to create database D: %f' % T3_d)

T3_e = t3_eEnd - t3_eStart
print('Time to create database E: %f' % T3_e)




