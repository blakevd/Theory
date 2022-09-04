# Blake Van Dyken

import matplotlib.pyplot as plt

T_cup_start = 84 # celcius
T_room_start = 19 # celcius
r = 0.025

# Forward Euler method
def forwardEuler(cupTemp, roomTemp, h):
    result = cupTemp + h * -(r) * (cupTemp - roomTemp)
    return result
    

cup_temps = []
h_values = {0.25, 9.5, 1, 5, 19, 15, 30}
prev_result = T_cup_start

for h in h_values:
    prev_result = forwardEuler(prev_result, T_room_start, h)
    cup_temps.append(prev_result)
    
plt.plot(cup_temps)
plt.show()