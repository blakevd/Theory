import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np
import random

# reads in node files
def input(name):
    file = open(name, 'r')
    
    points = []
    for line in file:
        i = line.replace('\t', ' ').replace('\n', ' ').strip().split(' ')
        while '' in i:
            i.remove('')
        if i[0] != '#':
            points.append( [ float(i[1]), float(i[2]) ] )
            
    return points

def addRandomPoints(points):
    p = points.copy()
    for i in range(250):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        p = np.append(points, np.array([x, y]))
    
    return p

def main():
    circle = np.array(input('circle2d-outer.node'))
    points = addRandomPoints(circle)
    
    print(len(circle), len(points))
    tri = Delaunay(points)
    plt.triplot(points[:,0], points[:,1], tri.simplices)
    plt.plot(points[:,0], points[:,1], 'o')
    plt.show()

main()