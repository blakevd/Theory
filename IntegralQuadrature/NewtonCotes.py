# Blake Van Dyken

from email.charset import BASE64
from time import perf_counter
import numpy as np
import matplotlib.pyplot as plt

# global vars
TRUE_ANS = 6.305171

def Integral(x):
    return 1 + np.sin(x) * np.cos((2*x)/2)*np.sin(4*x)

# Composite midpoint rule
def ConstantInterpolant(N, a, b, function):
    global TRUE_ANS
    sum = 0
    data = [0]
    ABS_Error_Data = [0]
    Rel_Error_Data = [0]
    Per_Error_Data = [0]
    
    for i in range(1, N + 1, 1): # N + 1 because range end is exclusive
        delta_x = (b - a) / N
        x_i = a + (i - .5) * delta_x
        
        w_i = delta_x
        sum += w_i * function(x_i)
        
        # data for charts
        data.append(sum)
        err = TRUE_ANS - sum
        ABS_Error_Data.append(err)
        Rel_Error_Data.append(err/TRUE_ANS)
        Per_Error_Data.append(err/TRUE_ANS * 100)
        
    return sum, data, ABS_Error_Data, Rel_Error_Data, Per_Error_Data

# composite trapezoid rule
def LinearInterpolant(N, a, b, function):
    sum = 0
    data = [0]
    ABS_Error_Data = [0]
    Rel_Error_Data = [0]
    Per_Error_Data = [0]
    
    for i in range(1, N + 1, 1): # N + 1 because range end is exclusive
        delta_x = (b - a) / (N - 1)
        x_i = a + (i - 1) * delta_x
        
        w_i = delta_x # if i = 2, N - 1
        if (i == 1 or i == N): # if i = 1, N
            w_i = delta_x / 2
        
        sum += w_i * function(x_i)
        
        # data for charts
        data.append(sum)
        err = TRUE_ANS - sum
        ABS_Error_Data.append(err)
        Rel_Error_Data.append(err/TRUE_ANS)
        Per_Error_Data.append(err/TRUE_ANS * 100)
        
    return sum, data, ABS_Error_Data, Rel_Error_Data, Per_Error_Data

# composite simpson formula
def QuadraticInterpolant(N, a, b, function):
    sum = 0
    data = [0]
    ABS_Error_Data = [0]
    Rel_Error_Data = [0]
    Per_Error_Data = [0]
    
    for i in range(1, (2*N+1) + 1, 1): # N + 1 because range end is exclusive
        delta_x = (b - a) / (2 * N)
        x_i = a + (i - 1) * delta_x
        
        w_i = (4 * delta_x) / 3 # for i= even
        if (i % 2 != 0): # for i =  odd
            w_i = (2 * delta_x) / 3
        elif (i == 1 or i == 2*N+1): # for i = 1, 2N+1
            w_i = delta_x / 3
            
        sum += w_i * function(x_i)
        
        # data for charts
        data.append(sum)
        err = TRUE_ANS - sum
        ABS_Error_Data.append(err)
        Rel_Error_Data.append(err/TRUE_ANS)
        Per_Error_Data.append(err/TRUE_ANS * 100)
        
    return sum, data, ABS_Error_Data, Rel_Error_Data, Per_Error_Data

# Guassian Quadrature for finding x_i and w_i
def GuassianQuadrature(N, a, b, function):
    def Helper(x_i): # value we pass to function
        return ((b-a)/2)*x_i + (a+b)/2
    
    sum = 0
    
    # All below is taken from the Gauss-Legendre Quadrature Table
    if(N == 1):
        x_i = 0
        w_i = 2
        
        sum = w_i*function(Helper(x_i))
    elif(N==2):
        x_i = np.sqrt(1/3)
        x_i_neg = -x_i
        w_i = 1
        
        sum = w_i*function(Helper(x_i)) + w_i*function(Helper(x_i_neg))
    elif(N==3):
        x_i = 0
        w_i = 8/9
        
        x_i2 = np.sqrt(3/5)
        x_i2_neg = -x_i2
        w_i2 = 5/9
        
        sum = w_i*function(Helper(x_i)) + w_i2*function(Helper(x_i2)) + w_i2*function(Helper(x_i2_neg))
    elif(N==4):
        x_i = np.sqrt(( 3 - 2 * np.sqrt(6/5) ) / 7)
        x_i_neg = -x_i
        w_i = (18 + np.sqrt(30)) / 36
        
        x_i2 = np.sqrt(( 3 + 2 * np.sqrt(6/5) ) / 7)
        x_i2_neg = -x_i2
        w_i2 = (18 - np.sqrt(30)) / 36
    
        sum = w_i*function(Helper(x_i)) + w_i*function(Helper(x_i_neg)) + w_i2*function(Helper(x_i2)) + w_i2*function(Helper(x_i2_neg))
    elif(N==5):
        x_i = 0
        w_i = 128/225
        
        x_i2 = (1/3) * np.sqrt(5 - 2 * np.sqrt(10/7))
        x_i2_neg = -x_i2
        w_i2 = (322 + 13 * np.sqrt(70)) / 900
        
        x_i3 = (1/3) * np.sqrt(5 + 2 * np.sqrt(10/7))
        x_i3_neg = -x_i3
        w_i3 = (322 - 13 * np.sqrt(70)) / 900
        
        sum = w_i*function(Helper(x_i)) + w_i2*function(Helper(x_i2)) + w_i2*function(Helper(x_i2_neg)) + w_i3*function(Helper(x_i3)) + w_i3*function(Helper(x_i3_neg))
    return (b - a) / 2 * sum

# Helper function to graph all three methods
def helpGraph(ax, data, xlab, ylab):
    ax.plot(data[0], color = "red", alpha = 0.25, label = "constant")
    ax.plot(data[1], color = "green",  alpha = 0.25, label = "linear")
    ax.plot(data[2], color = "blue",  alpha = 0.25, label = "quadratic")
    ax.legend()
    ax.set_ylabel(ylab)
    ax.set_xlabel(xlab)

def main():
    fig,ax = plt.subplots(3, 2)
    fig.suptitle("Integral Quadrature Graphs")
    
    a = 0
    b = 2*np.pi
    N = 1024
    guass_N = [2,3,4,5]
    
    # find newton cotes for n = 1024 and get chart data for each
    const, constData, const_ABS_Error_Data, const_Rel_Error_Data, const_Per_Error_Data = ConstantInterpolant(N, a, b, Integral)
    lin, linData, lin_ABS_Error_Data, lin_Rel_Error_Data, lin_Per_Error_Data = LinearInterpolant(N, a, b, Integral)
    quad, quadData, quad_ABS_Error_Data, quad_Rel_Error_Data, quad_Per_Error_Data = QuadraticInterpolant(N, a, b, Integral)
    
    # Basic True ans Graphs
    helpGraph()
    
    # ABS Error Graphs

    # find guassian quadrature for N=2 to 5
    for n in guass_N:
        guass = GuassianQuadrature(n, a, b, Integral)
        print("N = ", n, " guass = ", guass)
    
    plt.show()
    
main()