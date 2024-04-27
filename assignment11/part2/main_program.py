import module as md
import numpy as np
import time


matrixSize = [10, 100, 1000, 5000, 10000, 50000]

for N in matrixSize:
  print(" ==================== ")
  print('N = %d' % N)
  
  # Create the matrix K
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
  
  A = K.copy()
  b = f.copy()
  C = K.copy()
  d = f.copy()
  P = K.copy()
  q = f.copy()
  
  # Solve using dgesv using the mkl_solver function
  print("Solve using dgesv using the mkl_solver function")
  #print(A)
  #print(b)
  
  t_start = time.time()
  res = md.mkl_solver( A,b )
  t_end = time.time()
  
  #print(A)
  #print(b)
  print('Time spent: {0:.6f} s'.format(t_end-t_start))
  
  # Solve using dsysv with the mkl_solver_symm function
  print("Solve using dsysv with the mkl_solver_symm function")
  #print(C)
  #print(d)
  
  t_start = time.time()
  res = md.mkl_solver_symm( C,d )
  t_end = time.time()
  
  #print(C)
  #print(d)
  print('Time spent: {0:.6f} s'.format(t_end-t_start))


  # Solve using dsysv_work with the mkl_solver_symm_work function
  print("Solve using dsysv_work with the mkl_solver_symm_work function with lwork = 1")
  #print(P)
  #print(q)
  
  t_start = time.time()
  res = md.mkl_solver_symm_work( P,q )
  t_end = time.time()
  
  #print(P)
  #print(q)
  print('Time spent: {0:.6f} s'.format(t_end-t_start))
