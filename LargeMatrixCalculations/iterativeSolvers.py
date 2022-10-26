import numpy as np

def readMatrixFile(file, matrix_size):
    f = open(file)
    M = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    for line in f:
        values = int(line.split(" "))
        M[values[0]][values[1]] = values[2]
    return M

def jacobi():
    return

def guassSeidel():
    return

def SuccesiveOverRelaxation():
    w = 1.05

def main():
    A1 = readMatrixFile("A1.matrix", 793)
    print(A1[0])
    
main()