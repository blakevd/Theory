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
    p = []
    while len(p) != 250:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if (np.sqrt(x**2 + y**2) < 1):
            p.append([x, y])
        
    return p

def main():
    # this adds 250 random points then triangulates it
    circle = np.array(input('circle2d-outer.node'))
    randPoints = np.array(addRandomPoints(circle))

    points = np.vstack((circle, randPoints))
    tri = Delaunay(points)
    plt.triplot(points[:,0], points[:,1], tri.simplices)
    plt.plot(points[:,0], points[:,1], 'o')
    plt.title('Delaunay triangulation with 250 random points in circle2d-outer')
    
    # This just triangulates a mesh
    plt.figure()
    circle2 = np.array(input('circle2d.node'))
    tri = Delaunay(circle2)
    plt.triplot(circle2[:,0], circle2[:,1], tri.simplices)
    plt.plot(circle2[:,0], circle2[:,1], 'o')
    plt.title('Delaunay triangulation mesh of circle2d')

    plt.show()

main()