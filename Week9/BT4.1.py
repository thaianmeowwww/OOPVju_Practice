class TuLanh:
    def __init__(self, nhanhieu='Elextrolux', maso='UNKNOWN', nuocsx='Việt Nam', tkdien=True, dungtich=256, gia=7000000):
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        self.__tkdien = tkdien
        self.__dungtich = dungtich
        self.__gia = gia
        
        # Tạo biến lưu trạng thái chữ
        #Phải gán self vì về sau(ở các hàm khác còn dùng trạng thái này)
        if self.__tkdien:
            self.trang_thai = 'Có'
        else:
            self.trang_thai = 'Không'

    def print(self):
        print(f"Nhãn hiệu: {self.__nhanhieu}")
        print(f"Mã số: {self.__maso}")
        print(f"Nước SX: {self.__nuocsx}")
        # Sửa lại tên biến ở đây cho khớp với lúc khai báo
        print(f"T/K điện: {self.trang_thai}") 
        print(f"Dung tích: {self.__dungtich}L")
        print(f"Giá: {self.__gia}VNĐ")