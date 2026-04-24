import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = int(x)
        self.__y = int(y)
        
    def read(self):
        data = input().split()
        if len(data) >= 2:
            self.__x = int(data[0])
            self.__y = int(data[1])
            
    def print(self):
        print(f'({self.__x}, {self.__y})')
        
    def move(self, dx, dy):
        self.__x = self.__x + int(dx)
        self.__y = self.__y + int(dy)
        
    def getX(self):
        return self.__x
        
    def getY(self):
        return self.__y
        
    def distance(self):
        dis = math.sqrt(self.__x**2 + self.__y**2)
        return dis
        
    def distance_to_point(self, P):
        x1 = P.getX() - self.__x
        y1 = P.getY() - self.__y
        dis1 = math.sqrt(x1**2 + y1**2)
        return dis1