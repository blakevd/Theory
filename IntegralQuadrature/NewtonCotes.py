# Blake Van Dyken

import numpy as np
import matplotlib.pyplot as plt

def Integral(x):
    return 1 + np.sin(x) * np.cos((2*x)/2)*np.sin(4*x)

def ConstantInterpolant(N, a, b, function):
    sum = 0
    for i in range(1, N + 1, 1): # N + 1 because range end is exclusive
        delta_x = (b - a) / N
        x_i = a + (i - .5) * delta_x
        
        w_i = delta_x
        sum += w_i * function(x_i)
        
    return sum

def LinearInterpolant(N, a, b, function):
    sum = 0
    for i in range(1, N + 1, 1): # N + 1 because range end is exclusive
        delta_x = (b - a) / (N - 1)
        x_i = a + (i - 1) * delta_x
        
        w_i = delta_x # if i = 2, N - 1
        if (i == 1 or i == N): # if i = 1, N
            w_i = delta_x / 2
        
        sum += w_i * function(x_i)
        
    return sum

def QuadraticInterpolant(N, a, b, function):
    sum = 0
    for i in range(1, (2*N+1) + 1, 1): # N + 1 because range end is exclusive
        delta_x = (b - a) / (2 * N)
        x_i = a + (i - 1) * delta_x
        
        w_i = (4 * delta_x) / 3 # for i= even
        if (i % 2 != 0): # for i =  odd
            w_i = (2 * delta_x) / 3
        elif (i == 1 or i == 2*N+1): # for i = 1, 2N+1
            w_i = delta_x / 3
            
        sum += w_i * function(x_i)
        
    return sum

def GuassianQuadrature(N, a, b, function):
    def Helper(x_i): # value we pass to function
        return ((b-a)/2)*x_i + (a+b)/2
    
    # for N = 1
    sum = 0
    
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

def example(x):
    return 2*x**2 + x + 1

def main():
    a = 0
    b = 2*np.pi
    N = 1024
    guass_N = [2,3,4,5]
    
    const = ConstantInterpolant(N, a, b, Integral)
    lin = LinearInterpolant(N, a, b, Integral)
    quad = QuadraticInterpolant(N, a, b, Integral)
    
    print(const)
    print(lin)
    print(quad)
    
    for n in guass_N:
        guass = GuassianQuadrature(n, a, b, Integral)
        print("N = ", n, " guass = ", guass)
    
main()