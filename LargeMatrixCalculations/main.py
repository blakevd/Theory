from numpy import *
from matrix_direct import *
from matrix_dot import *
from matrix_outer import *
from matrix_saxpy import *
from matrix_vector import *
from time import time

# Matrix Multiplication with Python impelementation
def pythonMat(A,B):
    start = time()
    C, C_runtime = dot(A,B), time() - start    # C is m x n
    
    print(f"Python implementation: {C_runtime:.8f} seconds")
# Matrix Multiplication with our implementations   
def matLabMat(A,B):
    C1, C1_runtime = MatMatDirect(A,B)
    print(f"Matlab's implementation (matrix_direct.py): {C1_runtime:.8f} seconds")

def innerMat(A,B):
    C2, C2_runtime = MatMatDot(A,B)
    print(f"Optimized inner most loop of Matlab's (matrix_dot.py): {C2_runtime:.8f} seconds")
    
def outerMat(A,B):
    C3, C3_runtime = MatMatOuter(A,B)
    print(f"Outer products method (matrix_outer): {C3_runtime:.8f} seconds")

def saxpyMat(A,B):
    C4, C4_runtime = MatMatSaxpy(A,B)
    print(f"Saxpy operation method (matrix_saxpy.py): {C4_runtime:.8f} seconds")

def vectorMat(A,B):
    C5, C5_runtime = MatMatVec(A,B)
    print(f"Matrix vector products method (matrix_vector.py): {C5_runtime:.8f} seconds")
      
sizes = [128, 512, 1024, 4096]
for current_size in sizes:
    # Size of matrices
    m = current_size
    n = current_size
    p = current_size

    # Initialize A and B with random numbers
    A = random.random((m,p))   # A is m x p
    B = random.random((p,n))   # B is p x n
    
    print("n = ", current_size)
    saxpyMat(A,B)
    
# Find tha maximum absolute current_size in C
# maxval = fabs(C).max()

# Find the maximum relative errors of our implementations
#print(fabs(C - C1).max() / maxval)
#print(fabs(C - C2).max() / maxval)
#print(fabs(C - C3).max() / maxval)
#print(fabs(C - C4).max() / maxval)
#print(fabs(C - C5).max() / maxval)