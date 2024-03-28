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

task = 20

# --- Master ---
if rank == 0:
    # Loop over all tasks waiting for result
    data = []
    final_Result = []
    for i in range(1, task+1):
        worker_rank = (task-1) % (size-1) + 1
        n = i
        x = [0.0] * n
        w = [0.0] * n
        x1, x2 = -1.0, 1.0
        gauleg(x1, x2, x, w, n)
        
        data.append(x + w)
        comm.send(data[i-1], dest=worker_rank)
        final_Result.append(comm.recv(source=worker_rank))

    # Send signal that no more tasks are remaining
    for i in range(1, size):
        comm.send(None, dest=i)

    # Print all results
    print(tabulate(final_Result, headers=['Quadrature no.', 'Integration Result', 'Percent error (%)', 'Run time (s)'], floatfmt=(None, '', '', '',)))

# --- Worker ---
else:
    while True:
        start = time.perf_counter()
        data = comm.recv(source=0)
        
        # Stop when no more tasks are receive
        if data is None:
            break
        
        t = int(len(data)/2)
        x = [data[i] for i in range(t)]
        w = [data[i+t] for i in range(t)]
        sum = 0.0
        for i in range(0,t):
            sum = sum + w[i]*f(x[i])

        finish = time.perf_counter()
        exact = 2/math.exp(1)
    
        result = (t, sum, 100*abs(sum-exact)/exact, finish-start)

        # Send results back to Master (rank = 0)
        comm.send(result, dest=0)
