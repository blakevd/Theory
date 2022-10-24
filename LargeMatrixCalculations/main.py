from numpy import *
from matrix_direct import *
from matrix_dot import *
from matrix_outer import *
from matrix_saxpy import *
from matrix_vector import *

# Size of matrices
m = 100
n = 100
p = 100

# Initialize A and B with random numbers
A = random.random((m,p))   # A is m x p
B = random.random((p,n))   # B is p x n

# Matrix Multiplication with Python impelementation
C = dot(A,B)    # C is m x n

# Matrix Multiplication with our implementations
C1, C1_runtime = MatMatDirect(A,B)
C2, C2_runtime = MatMatDot(A,B)
C3, C3_runtime = MatMatOuter(A,B)
C4, C4_runtime = MatMatSaxpy(A,B)
C5, C5_runtime = MatMatVec(A,B)

# Find tha maximum absolute value in C
maxval = fabs(C).max()

# Find the maximum relative errors of our implementations
#print(fabs(C - C1).max() / maxval)
#print(fabs(C - C2).max() / maxval)
#print(fabs(C - C3).max() / maxval)
#print(fabs(C - C4).max() / maxval)
#print(fabs(C - C5).max() / maxval)

print(C1_runtime)
print(C2_runtime)
print(C3_runtime)
print(C4_runtime)
print(C5_runtime)