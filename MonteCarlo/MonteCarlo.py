# Blake Van Dyken

import sys
import numpy as np
import matplotlib.pyplot as plt
import random

M = sys.maxsize - 1
a = 16807
c = 0

# Change this seed if you want different numbers
x_i = 13 # seed

# Linear congruential RNG
# Generates a random number based on the seed between 0 and 1
def rng():
    global x_i
    x_i = (a * x_i + c) % (M - 1) 
    return x_i/(M-1)

# Solving for f(x) = ln(x^2)*ln((1 - x)^2) = 1.42...
def MonteCarlo(Fx_sum, n, r):
    a = 0
    b = 1
    Tr = a + ((b - a)/(M - 1)) * r
    Fx = np.log(Tr**2) * np.log((1-Tr)**2)
    print(Tr)
    return ((b - a) / n) * (Fx_sum + Fx), (Fx_sum + Fx)
    
def main():
    prev = 0
    for n in range(99):
        result, value = MonteCarlo(prev, n+1, rng())
        #print(result, value)
        prev = value
        
    
    
main()