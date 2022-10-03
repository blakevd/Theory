# Blake Van Dyken

from re import X
from unicodedata import decimal
import numpy as np
import matplotlib.pyplot as plt
from decimal import *

def StirlingsApprox(n):
    return np.sqrt(2*np.pi*n) * (n / np.e)**n

def StirlingErrors():
    # Stirling
    STIRLING_ANS = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800] # factorial from 1 to 10
    stirling_abs = []
    stirling_rel = []
    
    for n in range(1, 11, 1): # 1 to 10 by 1
        prediction = StirlingsApprox(n)
      
        # Calc Errors
        error = STIRLING_ANS[n-1] - prediction
        stirling_abs.append(error)
        stirling_rel.append(error / STIRLING_ANS[n-1])
        
    return STIRLING_ANS, stirling_abs, stirling_rel

def StirlingGraph():
    true, abs, rel = StirlingErrors()

    plt.figure()
    plt.plot(range(1,11,1), abs, 'bo')
    plt.xlim((0, 11))
    plt.xlabel("N")
    plt.ylabel("Absolute Error")
    plt.title("Graph of Stirlings Absolute Error")
        
    plt.figure()
    plt.plot(range(1,11,1), rel, 'go')
    plt.xlim((0, 11))
    plt.xlabel("N")
    plt.ylabel("Relative Error")
    plt.title("Graph of Stirlings Relative Error")
    
def arcTanExpansion(n):
    sum = 1
    denom = 3
    for i in range(n):
        if (i % 2 == 0):
            sum = sum - 1/denom
        else:
            sum = sum + 1/denom
        denom += 2
    
    return sum

# counts the number of decimals that are the same between a and b
def countAccurateDecimals(a, b):
    a_str = str(a)
    b_str = str(b)
    len = 1
    
    result = 0
    for num in a_str:
        if (b_str[len-1] != "."):
            areEqual = Decimal(num).compare(Decimal(b_str[len-1]))
            if (areEqual == 0):
                result += 1
            else:
                break # get out of loop we dont need the rest
            
        len += 1
    
    return result

def ApproxPiOverFour():
    tan_expansion_terms = []
    tan_i = []
    actual = 0.78539816339
    
    for i in range(4, 10004):
        approx = arcTanExpansion(i)
        tan_i.append(i)
        tan_expansion_terms.append(approx)
    
    plt.figure() 
    plt.plot(tan_expansion_terms, tan_i, ".")
    plt.plot([actual, actual], [tan_i[0], tan_i[len(tan_i) - 1]])
    plt.xlabel("Approximate Expansion Value")
    plt.ylabel("Number of expansion terms used")
    
    last_term = tan_expansion_terms[len(tan_expansion_terms) - 1]
    print("rate of convergence: ", countAccurateDecimals(last_term, actual) / last_term)
    

def Chudnovsky():
    x = np.sqrt(2)
    pi_approx = (2 + x)
    y = (2**(1/4))
    
    abs_error = []
    abs_BigO = []
    
    for n in range(1, 10, 1):
        # calulate with chuds            
        x = (1/2) * (np.sqrt(x) + (1 / np.sqrt(x)))
        pi_approx = pi_approx * ((x + 1)/(y + 1))
        y = (y*np.sqrt(x) + (1 / np.sqrt(x))) / (y + 1)
        
        # store error
        abs_error.append(np.abs(np.pi - pi_approx))
        exp = -(2)**n+1
        abs_BigO.append(10**exp)
        
    plt.figure()
    plt.plot(abs_error, "ro", alpha = 0.15)
    plt.plot(abs_BigO, "go", alpha = 0.15)
    plt.title("ABS Error of approx. pi using Chudnovsky")
    plt.ylabel("Approximate pi_nth Value")
    plt.xlabel("Number of expansion terms used")


def main():
    StirlingGraph()
    ApproxPiOverFour()
    Chudnovsky()
    plt.show()
    
main()