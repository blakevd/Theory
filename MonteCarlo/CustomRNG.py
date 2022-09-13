# Blake Van Dyken

import sys
import numpy as np
import matplotlib.pyplot as plt

M = sys.maxsize
a = 16807
c = 0

x_i = 29089675756 # seed

# Linear congruential RNG
def rng():
    global x_i
    x_i = (a * x_i + c) % M
    return x_i
    
    
def main():
    for i in range(99):
        print(rng()/M-1)

main()