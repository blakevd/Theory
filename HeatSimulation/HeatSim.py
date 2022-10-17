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
    
    # list of all u_i items
    values = np.ones(N)*initTemp
    
    # time step
    times = np.arange(0.0, total_time + delta_t, delta_t)
    
    for t in times:
        for i in range(0, N):     
            if i == 0:
                values[i] = (startTemp)
            elif i == N-1:
                values[i] = (endTemp)
            else:
                values[i] = (a * delta_t * stencil(values[i-1], values[i], values[i+1], delta_x) + initTemp)

    plt.figure()        
    plt.plot(values, "o")
    plt.plot(values, "g")
    title = "Graph for N = ", N, " and delta t = ", delta_t
    plt.title(title)
    plt.xlabel("Time(seconds)")
    plt.ylabel("Temperature(Celcius)")

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