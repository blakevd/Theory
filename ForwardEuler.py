# Blake Van Dyken

from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

T_cup_start = 84 # celcius
T_room_start = 19 # celcius
r = 0.025

# Forward Euler equation
def forwardEulerEquation(cupTemp, roomTemp, h):
    result = cupTemp + (h * -(r) * (cupTemp - roomTemp))
    return result

def forwardEuler(cup_temps, h_values, g, l):
    prev_result = T_cup_start
    for h in h_values:
        prev_result = forwardEulerEquation(prev_result, T_room_start, h)
        cup_temps.append(prev_result)
    
    g.set_ylabel("temperature of cup (Celcius)")
    g.set_xlabel("time passed in seconds")
    g.set_title(l)
    g.plot(cup_temps, "-")
    
        
def main():
    fig,ax = plt.subplots(4, 2)
    fig.delaxes(ax[3, 1])
    
    fig.suptitle("Forward Euler Method graphs")
    
    # GRAPH 1
    cup_temps = []
    h_values = np.arange(0, 301, 30) # create h values
    print(h_values)
    forwardEuler(cup_temps, h_values, ax[0, 0], "h = 30s")
    
    # GRAPH 2
    cup_temps = []
    h_values = np.arange(0, 301, 15) # create h values
    forwardEuler(cup_temps, h_values, ax[1, 0], "h = 15s")
    
    # GRAPH 3
    cup_temps = []
    h_values = np.arange(0, 301, 10) # create h values
    forwardEuler(cup_temps, h_values, ax[2, 0], "h = 10s")
    
    # GRAPH 4
    cup_temps = []
    h_values = np.arange(0, 301, 5) # create h values
    forwardEuler(cup_temps, h_values, ax[3, 0], "h = 5s")
    
    # GRAPH 5
    cup_temps = []
    h_values = np.arange(0, 301, 1) # create h values
    forwardEuler(cup_temps, h_values, ax[0, 1], "h = 1s")
    
    # GRAPH 6
    cup_temps = []
    h_values = np.arange(0, 301, 0.5) # create h values
    forwardEuler(cup_temps, h_values, ax[1, 1], "h = 0.5s")
    
    # GRAPH 7
    cup_temps = []
    h_values = np.arange(0, 301, 0.25) # create h values
    forwardEuler(cup_temps, h_values, ax[2, 1], "h = 0.25s")
   
    # set the spacing between subplots
    plt.subplots_adjust(left=0.1,
                        bottom=0.1, 
                        right=0.9, 
                        top=0.9, 
                        wspace=0.4, 
                        hspace=0.4)
    plt.show()  

main()