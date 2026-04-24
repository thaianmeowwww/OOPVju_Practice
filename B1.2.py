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
            
    def move(self, dx, dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy
        
    def print(self):
        print(f'({self.__x}, {self.__y})')
        
    def getX(self):
        return self.__x
        
    def getY(self):
        return self.__y
        
    def distance(self):
        return math.sqrt(self.__x**2 + self.__y**2)
        
    def distance_to_point(self, P):
        x1 = P.getX() - self.__x
        y1 = P.getY() - self.__y
        return math.sqrt(x1**2 + y1**2)

class PointTest:
    @staticmethod # Để có thể gọi phương thức này mà không cần tạo đối tượng của lớp PointTest
    def main():
        A = Point(3, 4)
        A.print()
        
        B = Point()
        B.read()
        B.print()
    
        C = Point(-B.getX(), -B.getY())
        C.print()
        B.distance()
        A.distance_to_point(B)

if __name__ == '__main__':
    PointTest.main()