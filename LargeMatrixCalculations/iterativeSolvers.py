import numpy as np

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
def jacobi(A, b, K):
    n = len(b)
    x = np.zeros_like(b)
    
    for k in range(K): # very very slow method for large matrix
        prev_x = x
        for i in range(n):
            sum = 0.0
            for j in range(n):
                if j != i:
                    sum += np.dot(A[i][j], x[j])
            x[i] = (b[i] - sum) / float(A[i][i])
    return x

def guassSeidel(A, b, K):
    n = len(b)
    x = np.zeros_like(b)
    
    for k in range(K):
        for i in range(n):
            sum = 0.0
            for j in range(i - 1):
                sum += np.dot(A[i][j], x[j])
            for j in range(i+1, n):
                sum += np.dot(A[i][j], x[j])
                
            x[i] = (b[i]-sum) / float(A[i][i])
    
    return x

def SuccesiveOverRelaxation(A, b, K):
    n = len(b)
    x = np.zeros_like(b)
    w = 1.05
    
    for k in range(K):
        for i in range(n):
            sum = 0.0
            for j in range(n):
                if j != i:
                    sum += np.dot(A[i][j], x[j])
            x[i] = x[i] + w*((b[i]-sum) / float(A[i][i])) - x[i]
    
    return x

def main():
    A = readMatrixFile("A1.matrix", 793)
    b = readRHSFile("b1.rhs", 793)
    max_iterations = 25
    #A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
    #b = [1.0, 2.0, 3.0]

    print(jacobi(A, b, max_iterations))
    print(guassSeidel(A, b, max_iterations))
    print(SuccesiveOverRelaxation(A,b,max_iterations))
main()