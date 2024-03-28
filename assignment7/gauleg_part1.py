import math
from mpi4py import MPI
import time
from tabulate import tabulate

# Start timer
start = time.perf_counter()

# Start the MPI process
comm = MPI.COMM_WORLD

# Determine total number of tasks
size = comm.Get_size()

# Determine id of "this" task
rank = comm.Get_rank()


def f(x):
    return x*math.exp(x)

def gauleg(x1, x2, x, w, n):
    EPS = 3.0e-16
    m = (n + 1) // 2
    xm = 0.50 * (x2 + x1)
    xl = 0.50 * (x2 - x1)
    
    for i in range(1, m + 1):
        z = math.cos(math.pi * (i - 0.25) / (n + 0.50))
        while True:
            p1 = 1.0
            p2 = 0.0
            for j in range(1, n + 1):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
            
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            
            if abs(z - z1) > EPS:
                continue
            
            x[i - 1] = xm - xl * z
            x[n - i] = xm + xl * z
            w[i - 1] = 2.0 * xl / ((1.0 - z * z) * pp * pp)
            w[n - i] = w[i - 1]
            break


# --- Master ---
if rank == 0:
    # Loop over all tasks waiting for result
    for i in range(1, size):
        n = i
        x = [0.0] * n
        w = [0.0] * n
        x1, x2 = -1.0, 1.0
        gauleg(x1, x2, x, w, n)
        
        output = x + w
        comm.send(output, dest=i)
    
    final_Result = [comm.recv(source=i) for i in range(1,size)]
    
    # Print all results
    print(tabulate(final_Result, headers=['Quadrature no.', 'Integration Result', 'Percent error (%)', 'Run time (s)'], floatfmt=(None, '', '', '',)))
    
# --- Worker ---
else:
    start = time.perf_counter()
    
    output = comm.recv(source=0)
    x = [output[i] for i in range(rank)]
    w = [output[i+rank] for i in range(rank)]
    sum = 0.0
    for i in range(0,rank):
        sum = sum + w[i]*f(x[i])

    finish = time.perf_counter()
    exact = 2/math.exp(1)
    
    result = (rank, sum, 100*abs(sum-exact)/exact, finish-start)

    # Send results back to Master (rank = 0)
    comm.send(result, dest=0)
