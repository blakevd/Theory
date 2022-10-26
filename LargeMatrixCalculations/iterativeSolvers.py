import numpy as np
from scipy.special import logsumexp

# reads in sparse matrix and stores as a 2D array
def readMatrixFile(file, matrix_size):
    f = open(file)
    M = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    for line in f:
        values = line.split(" ")
        M[int(values[0]) - 1][int(values[1]) - 1] = float(values[2])
    return M

def readRHSFile(file, b_size):
    f = open(file)
    b = [0 for i in range(b_size)]
    for line in f:
        values = line.split(" ")
        b[int(values[0]) - 1] = float(values[1])

    return b

# solves Ax = b jacobis method
def jacobi(A, b):
    iterations = 5000
    tolerance = 1e-10
    n = len(b)
    # make x same matrix as b with all zeros
    x = np.zeros_like(b, np.double) # inital guess

    for k in range(iterations): # mat iterations
        x_copy = x.copy()
        for i in range(n):
            sum = 0.0
            for j in range(n):
                if j != i:
                    sum += A[i][j] * x[j]
            # x_k+1 set to new guess value
            x[i] = np.exp(logsumexp((b[i]-sum))) / logsumexp(A[i][j])
        # check convergence
        error = np.linalg.norm(x-x_copy,ord=np.inf)/np.linalg.norm(x,ord=np.inf)
        if error < tolerance:
            break
            
    return x

def jacobi2(A, b, tolerance=1e-6, max_iterations=5000):
    
    x = np.zeros_like(b, dtype=np.double)
    
    T = A - np.diag(np.diagonal(A))
    
    for k in range(max_iterations):
        
        x_old  = x.copy()
        
        x[:] = (b - np.dot(T, x)) / np.diagonal(A)

        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
            break
            
    return x

def guassSeidel():
    return

def SuccesiveOverRelaxation():
    w = 1.05

def main():
    A = readMatrixFile("A1.matrix", 793)
    b = readRHSFile("b1.rhs", 793)

    print(jacobi2(A, b))
    
main()