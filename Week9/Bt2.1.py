import math
import copy
class Point:
    def __init__(self,x=0,y=1):
        self.__x=int(x)
        self.__y=int(y)
    def read(self):
        data= input("Nhập 2 số tọa độ x và y(cách nhau bởi khoảng trắng: )").split()
        if len(data)>=2:
            self.__x=int(data[0])
            self.__y=int(data[1])
    def print(self):
        return f'({self.__x},{self.__y})'
    def move(self, dx,dy):
        self.__x=self.__x+int(dx)
        self.__y=self.__y+int(dy)
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distance(self):
        #Vì khoảng cách đến gốc tọa độ tương đương căn bậc 2 của tổng x bình phương và y bình phương
        dis= math.sqrt(self.__x**2+self.__y**2)
        return {f'{dis:.2f}'}
    def distance_to_point(self,P):
        #Với P là một điểm thuộc class point được tạo sau
        x1= P.getX()- self.__x
        y1=P.getY()-self.__y
        dis1=math.sqrt(x1**2+y1**2)
        return f'{dis1:.2f}'
class LineSegment:
    def __init__(self, *args):
        if len(args)==0:
            self.__d1=Point(8,5)
            self.__d2=Point(2,0)
        elif len(args)==2:
            if isinstance (args[0],Point) and isinstance (args[1],Point):
                self.__d1=args[1]
                self.__d2=args[2]
        elif len(args)==4:
            self.__d1=Point(args[0],args[1])
            self.__d2=Point(args[2],args[3])
        elif len(args)==1:
            if isinstance(args[0], LineSegment):
                self.__d1 = copy.deepcopy(args[0].__d1)
                self.__d2 = copy.deepcopy(args[0].__d2)
    def read(self):
        data= input("Nhập tọa độ 4 điểm, 2 điểm đầu thuộc d1, 2 điểm sau thuộc d2").split()
        if len(data)>=4:
            d1= Point(data[0],data[1])
            d2= Point(data[2],data[3])
    def print(self):
        print( f'[{self.__d1.print()}, {self.__d2.print()}]')
    
l1=LineSegment(4,5,6,7)
l1.print()