# Blake Van Dyken

import sys
import numpy as np
from numpy import log as ln
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
    Tr = a + ((b - a)/(1 - 0)) * r # max r is 1 min r is 0
    Fx = (2*ln(Tr)) * (2*ln((1-Tr))) # ln(a^b) = b*ln(a)
    
    return ((b - a) / n) * (Fx_sum + Fx), (Fx_sum + Fx)
    
def main():
    prev = 0
    for n in range(1000):
        result, value = MonteCarlo(prev, n+1, rng())
        print(result)
        prev = value
        
main()