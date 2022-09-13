# Blake Van Dyken

from cmath import exp
import sys
from turtle import color
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
    x_i = (a * x_i + c) % M
    return x_i/(M-1)

# Solving for f(x) = ln(x^2)*ln((1 - x)^2)
def MonteCarlo(data, prev_Fx, n):
    a = 0
    b = 1
    Tr = a + ((b - a)/(M - 0))*rng()
    Fx = np.log(exp(pow(Tr , 2))) * np.log(exp(pow(1 - Tr , 2)))
    
    
    return ((b - a) / n) * (prev_Fx + Fx)
    
def main():
    print()
    
    
main()