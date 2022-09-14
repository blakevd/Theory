# Blake Van Dyken

import sys
import numpy as np
from numpy import log as ln
import matplotlib.pyplot as plt
import random
import math

M = sys.maxsize - 1

graph_answer = np.repeat(8 - ((2*math.pi**2)/3), 1000000)

# Change this seed if you want different numbers
x_i = 13 # seed

# Linear congruential RNG
# Generates a random number based on the seed between 0 and 1
def rng():
    global x_i
    x_i = (2 * x_i + x_i) % (M-1)
    return x_i/(M-1)

# r = random number
# n = integral approx step
# Fx_sum = sum of prev values calculated
def MonteCarlo(Fx_sum, n, r):
    a = 0
    b = 1
    Tr = a + ((b - a)/(1 - 0)) * r # max r is 1 min r is 0
    Fx = (2*ln(Tr)) * (2*ln((1-Tr))) # ln(a^b) = b*ln(a)
    
    return ((b - a) / n) * (Fx_sum + Fx), (Fx_sum + Fx)

# Graph helper function
def graph(g, title, data, real_data, num):
    g.plot(data[:num - 1], alpha = 0.5, color = 'blue', label = 'custom rng') # graph custom rng points
    g.plot(real_data[:num - 1], alpha = 0.5, color = 'red', label = 'built-in rng') # graph actual rng points
    g.plot(graph_answer[:num - 1], alpha = 0.5, color = 'green', label = 'solution') # graph answer line
    g.set_title("n = " + str(num - 1))
    g.set_xlabel("steps (n)")
    g.set_ylabel("Integral Approximation after n steps")
    g.legend()

# Solving for f(x) = ln(x^2)*ln((1 - x)^2) = 1.42...  
def main():
    fig,ax = plt.subplots(3, 2)
    fig.delaxes(ax[2, 1])
    fig.suptitle("Monte Carlo Graphs")
    
    data = [] 
    result = 0
    prev = 0
    # result for my RNG method
    for n in range(1000000):
        result, value = MonteCarlo(prev, n+1, rng())
        data.append(result)
        prev = value
        
    real_data = []
    result2 = 0
    prev2 = 0
    # result for built in RNG method
    for x in range(1000000):
        result2, value2 = MonteCarlo(prev2, x+1, random.random())
        real_data.append(result2)
        prev2 = value2
        
    graph(ax[0,0], "n = 100", data, real_data, 100)
    graph(ax[0,1], "n = 1000", data, real_data, 1000)
    graph(ax[1,0], "n = 10000", data, real_data, 10000)
    graph(ax[2,0], "n = 100000", data, real_data, 100000)
    graph(ax[1,1], "n = 1000000", data, real_data, 1000000)
    
    # set the spacing between subplots
    plt.subplots_adjust(left=0.1,
                        bottom=0.1, 
                        right=0.9, 
                        top=0.9, 
                        wspace=0.4, 
                        hspace=0.4)
    plt.show()
        
main()