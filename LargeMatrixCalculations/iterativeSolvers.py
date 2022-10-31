import numpy as np
import matplotlib as plt

# reads in sparse matrix and stores as a 2D array
def readMatrixFile(file, matrix_size):
    f = open(file)
    M = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    for line in f:
        values = line.split(" ")
        M[int(values[0]) - 1][int(values[1]) - 1] = float(values[2])
    return np.array(M)

def readRHSFile(file, b_size):
    f = open(file)
    b = [0 for i in range(b_size)]
    for line in f:
        values = line.split(" ")
        b[int(values[0]) - 1] = float(values[1])
    
    return np.array(b)

# solves Ax = b jacobis method
def jacobi(A, b, K, tolerance):
    n = len(b)
    x = np.zeros_like(b)
    e = []
    for k in range(K): # very very slow method for large matrix
        prev_x = x.copy()
        for i in range(n):
            sum = 0.0
            for j in range(n):
                if j != i:
                    sum += np.dot(A[i][j], x[j])
            x[i] = (b[i] - sum) / float(A[i][i])
        # check tolerance based on https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_IterativeSolvers.html
        error = np.abs(np.linalg.norm(x)) - np.abs(np.linalg.norm(prev_x))
        e.append(error)
        #print(error)
        if error < tolerance:
            break
    return x, e

def guassSeidel(A, b, K, tolerance):
    n = len(b)
    x = np.zeros_like(b)
    e = []

    for k in range(K):
        prev_x = x.copy()
        for i in range(n):
            sum = 0.0
            for j in range(i - 1):
                sum += np.dot(A[i][j], x[j])
            for j in range(i+1, n):
                sum += np.dot(A[i][j], x[j])
                
            x[i] = (b[i]-sum) / float(A[i][i])
        error = np.abs(np.linalg.norm(x)) - np.abs(np.linalg.norm(prev_x))
        e.append(error)
        #print(error)
        if error < tolerance:
            break
    return x, e

def SuccesiveOverRelaxation(A, b, K, tolerance):
    n = len(b)
    x = np.zeros_like(b)
    w = 1.05
    e = []
    for k in range(K):
        prev_x = x.copy()
        for i in range(n):
            sum = 0.0
            for j in range(i - 1):
                sum += np.dot(A[i][j], x[j])
            for j in range(i+1, n):
                sum += np.dot(A[i][j], x[j])
            x[i] = w*((b[i]-sum) / float(A[i][i]))
        error = np.abs(np.linalg.norm(x)) - np.abs(np.linalg.norm(prev_x))
        e.append(error)
        #print(error)
        if error < tolerance:
            break
    return x, e

def main():
    A = readMatrixFile("A1.matrix", 793)
    b = readRHSFile("b1.rhs", 793)
    max_iterations = 100
    tol = 0.1 # beause my pc is too slow
    #A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
    #b = [1.0, 2.0, 3.0]

    jx, je = jacobi(A, b, max_iterations, tol)
    gx, ge = guassSeidel(A, b, max_iterations, tol)
    sx, se = SuccesiveOverRelaxation(A,b,max_iterations, tol)
    print('jacobi converged after', len(je), 'iterations')
    print('jacobi matrix: ', jx)
    print('guass-seidel converged after', len(ge), 'iterations')
    print('guass-seidel matrix: ', gx)
    print('SOR with w=1.05 converged after', len(se), 'iterations')
    print('SOR w=1.05 matrix: ', sx)
main()