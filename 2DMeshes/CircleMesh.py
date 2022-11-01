import numpy as np
from pkg_resources import parse_version

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

def divideAndConquor(s, c_radius, list):
    # square is inside circle if s*sqrt(2) <= radius
    print(s.side, c_radius)
    if s.side > c_radius: # square is too big for circle
        s0, s1, s2, s3 = divideSquare(s)
        divideAndConquor(s0, c_radius, list)
        divideAndConquor(s1, c_radius, list)
        divideAndConquor(s2, c_radius, list)
        divideAndConquor(s3, c_radius, list)
    else:
        list.append(s)
        print(s)
        
def main():
    center = (0, 0)
    radius = 2
    side = np.sqrt(2)*radius
    
    # create square around the circle
    points = [center, (center[0] + side, center[1]), (center[0], center[1] + side), (center[0] + side, center[1] + side)]
    square = Square(radius*np.sqrt(2), points)
    
    list = []
    divideAndConquor(square, radius, list)
    return list
    
print(main())