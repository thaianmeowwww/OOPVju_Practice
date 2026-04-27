import math
import copy

class Point:
    def __init__(self, x=0, y=1): # Gán mặc định x=0, y=1 [cite: 7]
        self.__x = int(x)
        self.__y = int(y)
        
    def read(self):
        data = input().split()
        if len(data) >= 2:
            self.__x = int(data[0])
            self.__y = int(data[1])
            
    def print(self):
        # In có 1 khoảng trắng sau dấu phẩy [cite: 14, 15]
        return f'({self.__x}, {self.__y})' 
        
    def move(self, dx, dy):
        self.__x += int(dx)
        self.__y += int(dy)
        
    def getX(self):
        return self.__x
        
    def getY(self):
        return self.__y
        
    def distance(self):
        # Trả về số thực thay vì chuỗi [cite: 25]
        return math.sqrt(self.__x**2 + self.__y**2)
        
    def distance_to_point(self, P):
        # Trả về số thực thay vì chuỗi [cite: 27]
        x1 = P.getX() - self.__x
        y1 = P.getY() - self.__y
        return math.sqrt(x1**2 + y1**2)

class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            # Sửa lại thành (8, 5) và (1, 0) theo đúng đề bài [cite: 33]
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 2:
            if isinstance(args[0], Point) and isinstance(args[1], Point):
                self.__d1 = args[0]
                self.__d2 = args[1]
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
        rad = math.atan2(dy, dx)
        degree = math.degrees(rad)
        deg_duong = (degree + 360) / 360
        final_angle = round(deg_duong) % 360
        return int(final_angle)

class LineSegmentTest:
    @staticmethod
    def testCase():
        A = Point(2, 5)
        B = Point(20, 35)
        AB = LineSegment(A, B)
        AB.move(35, 51)
        AB.print()
        CD = LineSegment()
        CD.read()
        length = CD.length()
        # Định dạng |CD|=123.45 chính xác theo đề bài 
        print(f'|CD|={length:.2f}')
        try:
            n_str = input().strip()
            if not n_str:
                return
            n = int(n_str)
            segments = []
            for _ in range(n):
                data = input().split()
                if len(data) >= 4:
                    seg = LineSegment(int(data[0]), int(data[1]), int(data[2]), int(data[3]))
                    segments.append(seg)
                    
            # So sánh bằng hàm length() trả về số thực
            segments.sort(key=lambda s: s.length())
            
            for seg in segments:
                seg.print()
        except ValueError:
            pass

    @staticmethod
    def main():
        # Gọi cả 3 kịch bản [cite: 80]
        LineSegmentTest.testCase()