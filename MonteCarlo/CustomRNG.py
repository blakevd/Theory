# Blake Van Dyken

import sys
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import random

M = sys.maxsize - 1

# Change this seed if you want different numbers
x_i = 29089675 # seed

# Linear congruential RNG
# Generates a random number based on the seed between 0 and 1
def rng():
    global x_i
    x_i = (2 * x_i + x_i) % (M-1)
    return x_i/(M-1)

# Graph helper function
def graph(g, title, data, real_data, num):
    g.hist(data[:num - 1], bins = 10, range = [0,1], alpha = 0.25, color = 'blue', edgecolor = 'black', linewidth = 1, label = 'custom rng')
    g.hist(real_data[:num - 1], bins = 10, range = [0,1], alpha = 0.25, color = 'red', edgecolor = 'black', linewidth = 1, label = 'built-in rng')
    g.set_title("n = " + str(num - 1))
    g.set_xlabel("bins")
    g.set_ylabel("number of random numbers in a bin")
    g.legend()
    
def main():
    fig,ax = plt.subplots(3, 2)
    # fig.delaxes(ax[2, 1])
    fig.suptitle("Custom RNG Graphs")
    data = []
    data2 = [] # for y axis of scatterplot
    real_data = []
    real_data2 = []
    
    # create array of random values from 0 to 1000000
    for i in range(1000000):
        data.append(rng())
        data2.append(rng())
        real_data.append(random.random())
        real_data2.append(random.random())
    # GRAPH

    graph(ax[0,0], "n = 100", data, real_data, 100)
    graph(ax[0,1], "n = 1000", data, real_data, 1000)
    graph(ax[1,0], "n = 10000", data, real_data, 10000)
    graph(ax[2,0], "n = 100000", data, real_data, 100000)
    graph(ax[1,1], "n = 1000000", data, real_data, 1000000)
    
    ax[2,1].scatter(data, data2, color='blue', alpha=0.25)
    ax[2,1].scatter(real_data, real_data2, color='red', alpha=0.25)
    
    # set the spacing between subplots
    plt.subplots_adjust(left=0.1,
                        bottom=0.1, 
                        right=0.9, 
                        top=0.9, 
                        wspace=0.4, 
                        hspace=0.4)
    plt.show()

main()