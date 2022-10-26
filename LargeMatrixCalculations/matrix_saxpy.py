from numpy import *
import time

# C = MatMatSaxpy(A,B)
# Computes matrix multiplication by noting that the jth column of C equals
# A times the jth column of B.  This known as saxpy operation.

def MatMatSaxpy(A,B):
    start = time.time()
    (m,p) = A.shape
    (p,n) = B.shape

    C = zeros((m,n))
    for j in range(n):
        for k in range(m):
            C[:,j] = C[:,j] + A[:,k] * B[k,j]
            if time.time() - start > 300:
                    return C, 10*60
        
    return C, time.time() - start