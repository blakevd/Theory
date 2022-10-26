import numpy as np

# reads in sparse matrix and stores as a 2D array
def readMatrixFile(file, matrix_size):
    f = open(file)
    M = [[0 for i in range(matrix_size+1)] for j in range(matrix_size+1)]
    for line in f:
        values = line.split(" ")
        M[int(values[0])][int(values[1])] = float(values[2])
    return M

# solves Ax = b jacobis method
def jacobi(A, b, n):
    Diagonal = np.diag(A)
    Left = A - np.diagflat(Diagonal)
    
    for _ in range():
        return

def guassSeidel():
    return

def SuccesiveOverRelaxation():
    w = 1.05

def main():
    M1 = readMatrixFile("A1.matrix", 793)
    
    
main()