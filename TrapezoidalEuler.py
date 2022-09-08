# Blake Van Dyken

import numpy as np
import matplotlib.pyplot as plt

T_cup_start = 84 # celcius
T_room_start = 19 # celcius
r_start = 0.025

# Forward Euler equation
def forwardEulerEquation(cupTemp, roomTemp, h):
    return cupTemp + (h * -(r_start) * (cupTemp - roomTemp))

# just Euler equation
def EulerEquation(r, T_cup, T_surround):
    return -r *(T_cup - T_surround)

# trapezoidal eq
def trapezoidalEuler(step, thresh):
    cup_values = []
    threshold = thresh
    h_values = np.arange(0, 301, step)
    
    y_n = forwardEulerEquation(T_cup_start, T_room_start, 0) # should be 82.375
    
    for h in (h_values):
        k_curr = EulerEquation(r_start, y_n, T_room_start)
        
        k = 1
        while (True):
            k_next = EulerEquation(r_start, y_n, T_room_start) # get next y_k+1 item
            
            if (k_next - k_curr < threshold): # compare successive values
                cup_values.append(y_n)
                y_next = y_n + (h/2)*(k_curr+k_next) # make next y_n using trapezoidal eq
                y_n = y_next
                break
            else:
                y_n = forwardEulerEquation(y_n, T_room_start, h)
                k+=1 # inc k
    
    return cup_values  
    # print(cup_values, "\ncount:", len(cup_values))
   
def main():
    fig,ax = plt.subplots(4, 2)
    fig.delaxes(ax[3, 1])
    
    fig.suptitle("Trapezoidal Euler Method graphs")
    
    step = .2
    
    ax[0, 0].set_ylabel("temperature of cup (Celcius)")
    ax[0, 0].set_xlabel("time elapsed (seconds)")
    ax[0, 0].set_title("h = 30")
    ax[0, 0].plot(trapezoidalEuler(30, step))
    
    ax[1, 0].set_ylabel("temperature of cup (Celcius)")
    ax[1, 0].set_xlabel("time elapsed (seconds)")
    ax[1, 0].set_title("h = 15")
    ax[1, 0].plot(trapezoidalEuler(15, step))
    
    ax[2, 0].set_ylabel("temperature of cup (Celcius)")
    ax[2, 0].set_xlabel("time elapsed (seconds)")
    ax[2, 0].set_title("h = 10")
    ax[2, 0].plot(trapezoidalEuler(10, step))
    
    ax[3, 0].set_ylabel("temperature of cup (Celcius)")
    ax[3, 0].set_xlabel("time elapsed (seconds)")
    ax[3, 0].set_title("h = 5")
    ax[3, 0].plot(trapezoidalEuler(5, step))
    
    ax[0, 1].set_ylabel("temperature of cup (Celcius)")
    ax[0, 1].set_xlabel("time elapsed (seconds)")
    ax[0, 1].set_title("h = 1")
    ax[0, 1].plot(trapezoidalEuler(1, step))
    
    ax[1, 1].set_ylabel("temperature of cup (Celcius)")
    ax[1, 1].set_xlabel("time elapsed (seconds)")
    ax[1, 1].set_title("h = .5")
    ax[1, 1].plot(trapezoidalEuler(.5, step))
    
    ax[2, 1].set_ylabel("temperature of cup (Celcius)")
    ax[2, 1].set_xlabel("time elapsed (seconds)")
    ax[2, 1].set_title("h = .25")
    ax[2, 1].plot(trapezoidalEuler(.25, step))
    
    # set the spacing between subplots
    plt.subplots_adjust(left=0.1,
                        bottom=0.1, 
                        right=0.9, 
                        top=0.9, 
                        wspace=0.4, 
                        hspace=0.4)
    plt.show()
main()