import math
class Point:
    def __init__(self,x=0,y=1):
        self.__x=int(x)
        self.__y=int(y)
    def read(self):
        #Đọc theo 1 dòng, tách theo x và y
        # Dùng input() để nhận dòng chữ (VD: "-50 100")
    # Dùng .split() để cắt dòng đó ra thành mảng: ['-50', '100']
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