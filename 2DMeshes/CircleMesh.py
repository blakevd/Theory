import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle

class Square:
    # points: [2]-------[3]
    #         |           | = side
    #         [0]-------[1]
    def __init__(self, side, points=[(0, 0) for i in range(4)]):
        self.side = side
        self.points = points # 2d array of points
        
    def get_center(self):
        x = (self.points[0][0] + self.points[3][0]) / 2
        y = (self.points[0][1] + self.points[3][1]) / 2
        return (x, y)

def divideSquare(s):
    L = s.side / 2
    c = s.get_center()
    # bottom left
    p0 = [(0, 0) for i in range(4)]
    p0[0] = (c[0] - L, c[1] - L)
    p0[1] = (c[0], c[1] - L)
    p0[2] = (c[0] - L, c[1])
    p0[3] = c
    s0 = Square(L, p0)
    
    p1 = [(0, 0) for i in range(4)]
    p1[0] = (c[0], c[1] - L)
    p1[1] = (c[0] + L, c[1] - L)
    p1[2] = c
    p1[3] = (c[0] + L, c[1])
    s1 = Square(L, p1)
    
    p2 = [(0, 0) for i in range(4)]
    p2[0] = (c[0] - L, c[1])
    p2[1] = c
    p2[2] = (c[0] - L, c[1] + L)
    p2[3] = (c[0], c[1] + L)
    s2 = Square(L, p2)
    
    p3 = [(0, 0) for i in range(4)]
    p3[0] = c
    p3[1] = (c[0] + L, c[1])
    p3[2] = (c[0], c[1] + L)
    p3[3] = (c[0] + L, c[1] + L)
    s3 = Square(L, p3)
    
    return s0, s1, s2, s3

def isInCircle(points, r):
    dxy = np.sqrt(points[0]**2 + points[1]**2)
    return (dxy < r)

def divideAndConquor(s, parent, center, radius, list, i):
    i+=1
    if i <= 4:
        if(isInCircle(parent.points[3], radius)):
            # skip squares that are inside circle
            return
        else:
            if i <= 3:
                if parent in list:
                    list.remove(parent) # remove prev
                list.append(s) # add to list if we are in circle
                s0, s1, s2, s3 = divideSquare(s)
                divideAndConquor(s0, s, center, radius, list,i)
                divideAndConquor(s1, s, center, radius, list,i)
                divideAndConquor(s2, s, center, radius, list,i)    
                divideAndConquor(s3, s, center, radius, list,i)
            else:
                if parent in list:
                    list.remove(parent) # remove prev
                list.append(s) # add to list if we are in circle
                s0, s1, s2, s3 = divideSquare(s)
                if isInCircle(s0.get_center(), radius):
                    divideAndConquor(s0, s, center, radius, list,i)
                if isInCircle(s1.get_center(), radius):
                    divideAndConquor(s1, s, center, radius, list,i)
                if isInCircle(s2.get_center(), radius):
                    divideAndConquor(s2, s, center, radius, list,i)
                if isInCircle(s3.get_center(), radius):
                    divideAndConquor(s3, s, center, radius, list,i)
        
def main():
    center = (0, 0)
    radius = 2
    side = radius
    
    # create square around the circle
    points = [center, (center[0] + side, center[1]), (center[0], center[1] + side), (center[0] + side, center[1] + side)]
    square = Square(radius, points)
    
    list = []
    i = 0
    s0, s1, s2, s3 = divideSquare(square)
    divideAndConquor(s0, square, center, radius, list,i)
    divideAndConquor(s1, square, center, radius, list,i)
    divideAndConquor(s2, square, center, radius, list,i)
    divideAndConquor(s3, square, center, radius, list,i)
    
    # GRAPH result
    fig, ax = plt.subplots(1)
    ax.set_xlim(left = 0, right = 2)
    ax.set_ylim(bottom = 0, top = 2)

    ax.add_patch(Circle(center, radius, color='black', alpha=0.1))
    for s in list:
        if isInCircle(s.points[0], radius): # only add the inside things to the graph
            ax.add_patch(Rectangle(s.points[0], s.side, s.side, color='blue', alpha=0.1,))
    
    plt.show()
    
print(main())