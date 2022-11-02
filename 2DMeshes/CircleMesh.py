import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

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
    s_side = s.side / 4
    
    # bottom left
    p0 = [(0, 0) for i in range(4)]
    p0[0] = (s.points[0][0], s.points[0][1])
    p0[1] = (s.points[1][0]/2, s.points[1][1])
    p0[2] = (s.points[2][0], s.points[2][1]/2)
    p0[3] = s.get_center()
    s0 = Square(s_side, p0)
    
    p1 = [(0, 0) for i in range(4)]
    p1[0] = (s.points[1][0]/2, s.points[1][1])
    p1[1] = (s.points[1][0], s.points[1][1])
    p1[2] = s.get_center()
    p1[3] = (s.points[3][0], s.points[3][1]/2)
    s1 = Square(s_side, p1)
    
    p2 = [(0, 0) for i in range(4)]
    p2[0] = (s.points[2][0], s.points[2][1]/2)
    p2[1] = s.get_center()
    p2[2] = (s.points[2][0], s.points[2][1])
    p2[3] = (s.points[3][0]/2, s.points[3][1])
    s2 = Square(s_side, p2)
    
    p3 = [(0, 0) for i in range(4)]
    p3[0] = s.get_center()
    p3[1] = (s.points[1][0], s.points[3][1]/2)
    p3[2] = (s.points[3][0], s.points[3][1])
    p3[3] = (s.points[3][0]/2, s.points[3][1])
    s3 = Square(s_side, p3)
    
    return s0, s1, s2, s3

def isInCircle(points, center, r):
    dx = np.abs(points[0] - center[0])
    dy = np.abs(points[1] - center[1])
    if (dx > r or dy > r):
        return False
    
    return (dx*dx + dy*dy <= (r*r))

def isCloseToCircle(s_center, r):
    tol = 0.1
    dx = s_center[0]
    dy = s_center[1]
    #print(dx, dy)
    return (dx <= tol and dx >= -tol) or (dy <= tol and dy >= -tol)

def divideAndConquor(s, center, radius, list):
    if(isInCircle(s.points[0], center, radius)): # if square is inside keep going otherwise ignore and throw away
        # if top right is inside then stop recursing
        #print(isInCircle(s.points[3], center, radius), isCloseToCircle(s.get_center(), radius))
        if(isInCircle(s.points[3], center, radius) or isCloseToCircle(s.get_center(), radius)):
            list.append(s)
            return
        else:
            s0, s1, s2, s3 = divideSquare(s)
            divideAndConquor(s0, center, radius, list)
            divideAndConquor(s1, center, radius, list)
            divideAndConquor(s2, center, radius, list)
            divideAndConquor(s3, center, radius, list)
    
    return 
            
        
def main():
    center = (0, 0)
    radius = 2
    side = radius
    
    # create square around the circle
    points = [center, (center[0] + side, center[1]), (center[0], center[1] + side), (center[0] + side, center[1] + side)]
    square = Square(radius, points)
    
    list = []
    divideAndConquor(square, center, radius, list)
    fig, ax = plt.subplots(1)
    ax.set_xlim(left = 0, right = 2)
    ax.set_ylim(bottom = 0, top = 2)
    for s in list:
        ax.add_patch(Rectangle(s.points[0], s.side, s.side, color='purple', alpha=0.1,))
    
    plt.show()
    
print(main())