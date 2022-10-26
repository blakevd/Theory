from numpy import *
import time

# C = MatMatDirect(A,B)
# This is what Matlab uses to compute the matrix product C = A*B

def MatMatDirect(A,B):
    start = time.time()
    (m,p) = A.shape
    (p,n) = B.shape

    C = zeros((m,n))
    for j in range(n):
        for i in range(m):
            for k in range(p):
                C[i,j] = C[i,j] + A[i,k] * B[k,j]
                if time.time() - start > 300:
                    return C, 10*60

    return C, time.time() - start