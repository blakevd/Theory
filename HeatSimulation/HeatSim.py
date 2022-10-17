# Blake Van Dyken

import numpy as np
import matplotlib.pyplot as plt

# Variables
initTemp = 20.0 # Celcius
startTemp = 60.0
endTemp = 20.0

L = 2.5 # cm Length
a = 0.035 # cm^2/s Thermal diffusivity

def stencil(u_prev, u, u_next, dx):
    return (u_next - 2*u + u_prev) / (dx**2)

def graphThermalDiff(N, delta_t, total_time):
    delta_x = L / (N-1)
    values = []
    times = np.arange(0.0, total_time + delta_t, delta_t)
    for t in times:
        if t == 0.0:
            values.append(startTemp)
        elif t == total_time:
            values.append(endTemp)
        else:
            if t == delta_t: # first item
                values.append(a * delta_t * stencil(startTemp, initTemp, initTemp, delta_x) + initTemp)
            elif t == total_time - delta_t: # second to last item
                values.append(a * delta_t * stencil(initTemp, initTemp, endTemp, delta_x) + initTemp)
            else:
                values.append(a * delta_t * stencil(initTemp, initTemp, initTemp, delta_x) + initTemp)

    plt.figure()        
    plt.plot(times, values, "o")
    title = "Graph for N = ", N, " and delta t = ", delta_t
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Temperature")

def main():
    total_time = 5.0
    
    N = 8
    delta_t = 0.01
    graphThermalDiff(N, delta_t, total_time)
    
    N = 16
    graphThermalDiff(N, delta_t, total_time)
    
    N = 32
    graphThermalDiff(N, delta_t, total_time)
    
    N = 64
    graphThermalDiff(N, delta_t, total_time)
    
    N = 32
    delta_t = 0.001
    graphThermalDiff(N, delta_t, total_time)
    
    delta_t = 0.1
    graphThermalDiff(N, delta_t, total_time)
    
    plt.show()
   
main()