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
C1 = MatMatDirect(A,B)
C2 = MatMatDot(A,B)
C3 = MatMatOuter(A,B)
C4 = MatMatSaxpy(A,B)
C5 = MatMatVec(A,B)

# Find tha maximum absolute value in C
maxval = fabs(C).max()

# Find the maximum relative errors of our implementations
print(fabs(C - C1).max() / maxval)
print(fabs(C - C2).max() / maxval)
print(fabs(C - C3).max() / maxval)
print(fabs(C - C4).max() / maxval)
print(fabs(C - C5).max() / maxval)