# Blake Van Dyken

import numpy as np
import matplotlib.pyplot as plt

T_cup_start = 84 # celcius
T_room_start = 19 # celcius
r = 0.025

# Forward Euler equation
def forwardEulerEquation(cupTemp, roomTemp, h):
    result = cupTemp + h * -(r) * (cupTemp - roomTemp)
    return result
    
def forwardEuler():
    cup_temps = []
    h_values = [0, 0.25, 9.5, 1, 5, 19, 15, 30]
    
    # plot with few h values
    prev_result = T_cup_start
    for h in h_values:
        prev_result = forwardEulerEquation(prev_result, T_room_start, h)
        cup_temps.append(prev_result)
    
    fig, (g1, g2) = plt.subplots(2)
    g1.set_title("fewer h values")
    g1.plot(cup_temps)
    
    # create more h values   
    more_h_values = np.arange(0, 30, 0.25)
    more_cup_temps = []
    
    # plot with more h values
    prev_result = T_cup_start
    for h in more_h_values:
        prev_result = forwardEulerEquation(prev_result, T_room_start, h)
        more_cup_temps.append(prev_result)
        
    g2.set_title("more h values")
    g2.plot(more_cup_temps)
    plt.show()

forwardEuler()