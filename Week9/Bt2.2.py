import math
import copy

class Point:
    def __init__(self, x=0, y=0):
        self.__x = int(x)
        self.__y = int(y)
        
    def read(self):
        data = input().split()
        if len(data) >= 2:
            self.__x = int(data[0])
            self.__y = int(data[1])
            
    def print(self):
        return f'({self.__x}, {self.__y})'
        
    def move(self, dx, dy):
        self.__x += int(dx)
        self.__y += int(dy)
        
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

class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(0, 0)
            self.__d2 = Point(0, 0)
        elif len(args) == 2:
            if isinstance(args[0], Point) and isinstance(args[1], Point):
                self.__d1 = copy.deepcopy(args[0])
                self.__d2 = copy.deepcopy(args[1])
        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        elif len(args) == 1:
            if isinstance(args[0], LineSegment):
                self.__d1 = copy.deepcopy(args[0].__d1)
                self.__d2 = copy.deepcopy(args[0].__d2)
                
    def read(self):
        data = input().split()
        if len(data) >= 4:
            self.__d1 = Point(data[0], data[1])
            self.__d2 = Point(data[2], data[3])
            
    def print(self):
        print(f'[{self.__d1.print()}; {self.__d2.print()}]')
    
    def move(self, dx, dy):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)
        
    def length(self):
        return self.__d1.distance_to_point(self.__d2)
        
    def angle(self):
        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()
        
        # Tính góc theo radian từ atan2
        rad = math.atan2(dy, dx)
        # Chuyển đổi sang độ
        degree = math.degrees(rad)
        # Nếu góc âm, cộng 360 để được góc dương
        if degree < 0:
            degree += 360
        # Làm tròn đến số nguyên gần nhất
        return round(degree)

class LineSegmentTest:
    @staticmethod
    def testCase():
        # Đọc đoạn thẳng từ input
        CD = LineSegment()
        CD.read()
        
        # Lưu bản gốc trước khi dịch
        CD_original = LineSegment(CD)
        
        # In đoạn thẳng ban đầu
        CD.print()
        
        # In độ dài
        length = CD.length()
        print(f'{length}')
        
        # In góc
        angle = CD.angle()
        print(f'{angle}')
        
        # Dịch đoạn thẳng
        CD.move(1, 1)
        CD.print()
        
        # In đoạn thẳng ban đầu (từ bản lưu)
        CD_original.print()
