from numpy import *
import time

# C = MatMatDot(A, B)
# Calculates the matrix product by optimizing the innermost loop of
# matrix_direct.py

def MatMatDot(A, B):
    start = time.time()
    (m,p) = A.shape
    (p,n) = B.shape

    C = zeros((m,n))
    for j in range(n):
        for i in range(m):
            C[i,j] = dot(A[i,:],B[:,j])
            if time.time() - start > 300:
                    return C, 10*60

    return C, time.time() - start