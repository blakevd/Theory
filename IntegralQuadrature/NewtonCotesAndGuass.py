# Blake Van Dyken

from email.charset import BASE64
from pickle import TRUE
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
    ABS_Error_Data = []
    Rel_Error_Data = []
    Per_Error_Data = []
    
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
    ABS_Error_Data = []
    Rel_Error_Data = []
    Per_Error_Data = []
    
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
    ABS_Error_Data = []
    Rel_Error_Data = []
    Per_Error_Data = []
    
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
    
    result = (b - a) / 2 * sum
    return result, (TRUE_ANS - result)/result * 100

# Helper function to graph all three methods
def helpGraph(ax, data, title, xlab, ylab):
    if (len(data) == 3): # plot newton cotes
        ax.plot(data[0], color = "red", alpha = 0.35, label = "constant")
        ax.plot(data[1], color = "green",  alpha = 0.35, label = "linear")
        ax.plot(data[2], color = "blue",  alpha = 0.35, label = "quadratic")
    else: # plot guassian
        ax.plot([2,3,4,5], data, color = "red", alpha = 0.35, label = "guassian")
    ax.legend()
    ax.set_title(title)
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
    
    print("True ans: ", TRUE_ANS)
    print("Constant ans: ", const)
    print("Linear ans: ", lin)
    print("Quadratic ans: ", quad)
    # find guassian quadrature for N=2 to 5
    guassData, guass_Perc_Error_Data = [], []
    for n in guass_N:
        guass, data = GuassianQuadrature(n, a, b, Integral)
        guassData.append(guass)
        guass_Perc_Error_Data.append(data)
        print("N = ", n, " guass = ", guass)
    
    # Basic True ans Graphs
    helpGraph(ax[0, 0], [constData, linData, quadData], "Graph of Approximations at N", "N", "Approximation at N")
    
    # ABS Error Graphs
    helpGraph(ax[0, 1], [const_ABS_Error_Data, lin_ABS_Error_Data, quad_ABS_Error_Data], "Graph of ABS Error", "N", "Approx. ABS Error")
    
    # Rel Error Graphs
    helpGraph(ax[1, 0], [const_Rel_Error_Data, lin_Rel_Error_Data, quad_Rel_Error_Data], "Graph of Relative Error", "N", "Approx. Rel. Error")
    
    # Percent Error Graphs
    helpGraph(ax[1, 1], [const_Per_Error_Data, lin_Per_Error_Data, quad_Per_Error_Data], "Graph of Percent Error", "N", "% Error")

    # Guassian True Error graph
    helpGraph(ax[2, 0], guassData, "Graph of Approximations at N", "N", "Approximation at N")
    
    # Guassian Perc Error graph
    helpGraph(ax[2, 1], guass_Perc_Error_Data, "Graph of Percent Error", "N", "% Error")

    plt.subplots_adjust(hspace=0.35)
    plt.show()
    
main()