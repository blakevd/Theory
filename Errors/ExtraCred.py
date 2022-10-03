# Blake Van Dyken

import numpy as np
import matplotlib.pyplot as plt
from decimal import *

def decFactorial(val):
    fact = Decimal(1)
    for i in range(1, (int)(val+1), 1):
        fact = fact * Decimal(i)
    
    return fact

def extraCred(n):
    if (n <= 1000):
        getcontext().prec = n # large decimal places
    else:
        getcontext().prec = 1000
    result = 0
    for i in range(n):
        k = Decimal(i)
        result += ( (Decimal(-1)**k) * decFactorial((6*k)) * (Decimal(545140134) * k + 13591409) ) / ( decFactorial(3 * k) * (decFactorial(k)**Decimal(3)) * Decimal(640320)**(Decimal(3)*k+Decimal(3/2)))

    return 12 * result

def main():
    n = [10, 100, 1000, 10000]
    for v in n:
        print('n = ', n, ' : ', extraCred(v))
    
    print("\nExtra Credit Problem: \n")
    
main()