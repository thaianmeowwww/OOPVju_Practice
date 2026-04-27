import json
import math

# ============================================================
# HƯỚNG DẪN SỬ DỤNG CÁC LOẠI HÀM TRONG CLASS:
#
#   - Hàm thường (có self)  : Thao tác trên 1 chiếc tủ lạnh cụ thể
#   - @classmethod (có cls) : Dùng để tạo/khởi tạo những chiếc tủ lạnh mới (factory)
#   - @staticmethod         : Công thức/kịch bản độc lập, không dựa vào dữ liệu tủ nào
# ============================================================


class TuLanh:
    def __init__(self, nhanhieu='Elextrolux', maso='UNKNOWN', nuocsx='Việt Nam',
                 tkdien=True, dungtich=256, gia=7000000):
        self.__nhanhieu = nhanhieu
        self.__maso     = maso
        self.__nuocsx   = nuocsx
        self.__tkdien   = tkdien
        self.__dungtich = dungtich
        self.__gia      = gia

        # Gọi cap_nhat_trang_thai() để sinh ra self.trang_thai ngay khi khởi tạo.
        # Biến trang_thai không khai báo thẳng trong __init__ mà được
        # "khai sinh" bên trong hàm này tại dòng self.trang_thai = ...
        self.cap_nhat_trang_thai()

    # ----------------------------------------------------------
    # cap_nhat_trang_thai: Đồng bộ chữ 'Có'/'Không' với __tkdien
    # Gọi lại mỗi khi __tkdien thay đổi để dữ liệu không bị lệch pha
    # ----------------------------------------------------------
    def cap_nhat_trang_thai(self):
        if self.__tkdien:
            self.trang_thai = 'Có'
        else:
            self.trang_thai = 'Không'

    # ----------------------------------------------------------
    # to_dict: Chuyển thuộc tính private → dict để JSON có thể đọc được
    # ----------------------------------------------------------
    def to_dict(self):
        return {
            "nhan_hieu": self.__nhanhieu,
            "ma_so":     self.__maso,
            "nuoc_sx":   self.__nuocsx,
            "tk_dien":   self.__tkdien,
            "dung_tich": self.__dungtich,
            "gia":       self.__gia
        }

    # ----------------------------------------------------------
    # hienThi: In toàn bộ thông tin của tủ ra màn hình
    # ----------------------------------------------------------
    def hienThi(self):
        print(f"Nhãn hiệu: {self.__nhanhieu}")
        print(f"Mã số: {self.__maso}")
        print(f"Nước SX: {self.__nuocsx}")
        print(f"T/K điện: {self.trang_thai}")
        print(f"Dung tích: {self.__dungtich}L")
        print(f"Giá: {self.__gia}VNĐ")

    # ----------------------------------------------------------
    # makeCopy: Sao chép toàn bộ dữ liệu từ tủ 'tl' sang tủ hiện tại (self)
    # Cách dùng: tu_lanh_1.makeCopy(tu_lanh_2) → tủ 1 trở thành bản sao của tủ 2
    # Phải copy cả trang_thai vì __init__ chỉ chạy 1 lần lúc mới tạo tủ —
    # sau đó nếu chỉ copy __tkdien mà không copy trang_thai thì 2 giá trị bị lệch pha
    # ----------------------------------------------------------
    def makeCopy(self, tl):
        self.__nhanhieu = tl.__nhanhieu
        self.__maso     = tl.__maso
        self.__nuocsx   = tl.__nuocsx
        self.__tkdien   = tl.__tkdien
        self.__dungtich = tl.__dungtich
        self.__gia      = tl.__gia
        self.trang_thai = tl.trang_thai  # Đồng bộ luôn nhãn chữ để khỏi lệch

    # ----------------------------------------------------------
    # nhapThongTin: Đọc 1 dòng input theo định dạng "A|B|C|D|E|F"
    # Dùng split('|') thay vì gọi input() 6 lần để đúng với định dạng đầu vào
    # ----------------------------------------------------------
    def nhapThongTin(self):
        data = input().strip().split('|')
        self.__nhanhieu = data[0]
        self.__maso     = data[1]
        self.__nuocsx   = data[2]
        self.__tkdien   = True if data[3].strip() == 'True' else False
        self.__dungtich = int(data[4])
        self.__gia      = int(data[5])

        # Cập nhật lại chữ 'Có'/'Không' sau khi nhập thông tin mới
        self.cap_nhat_trang_thai()

    # ----------------------------------------------------------
    # layNhanHieu / layNhan: Getter trả về nhãn hiệu (2 tên khác nhau, cùng tác dụng)
    # SỬA: Giữ lại cả 2 để tránh phá code các testCase đang dùng từng cái
    # ----------------------------------------------------------
    def layNhanHieu(self):
        return str(self.__nhanhieu)

    def layNhan(self):
        return self.__nhanhieu

    # ----------------------------------------------------------
    # soNguoiSD: Tính số người sử dụng dựa trên dung tích
    # SỬA LỖI: Thêm "return nguoi" — trước đây tính xong nhưng bỏ mất kết quả
    # ----------------------------------------------------------
    def soNguoiSD(self):
        a     = int(self.__dungtich % 100)
        nguoi = math.floor(a)
        return nguoi  # ← SỬA: Trả về kết quả thay vì bỏ đi

    # ----------------------------------------------------------
    # cungNhanHieu: So sánh nhãn hiệu 2 tủ (không phân biệt hoa/thường, khoảng trắng)
    # ----------------------------------------------------------
    def cungNhanHieu(self, tl):
        nhan_hieu_1 = self.__nhanhieu.strip().lower()
        nhan_hieu_2 = tl.__nhanhieu.strip().lower()
        return nhan_hieu_1 == nhan_hieu_2  # (==) đã trả về True/False trực tiếp

    # ----------------------------------------------------------
    # layGia: Getter trả về giá tủ
    # ----------------------------------------------------------
    def layGia(self):
        return self.__gia


# ============================================================
# TuLanhTest: Tập hợp các kịch bản kiểm thử
# Dùng @staticmethod vì các hàm test không dựa vào tủ lạnh cụ thể nào
# ============================================================
class TuLanhTest:

    @staticmethod
    def testCase():
        # Đọc tủ thứ 1 (sẽ được in ra đầu tiên)
        tl2 = TuLanh()
        tl2.nhapThongTin()
        # Đọc tủ thứ 2 (sẽ được copy sang tl3)
        tl1 = TuLanh()
        tl1.nhapThongTin()

        print('= = = = = = = =')
        tl2.hienThi()
        print('= = = = = = = =')

        tl3 = TuLanh()
        tl3.makeCopy(tl1)  # tl3 là bản sao của tl1
        tl3.hienThi()
        print('= = = = = = = =')

    @staticmethod
    def testCase2():
        # Nhập n tủ rồi in ngược từ cuối về đầu
        n = int(input())
        danhsach = []
        if 0 < n < 100:
            for i in range(n):
                tl = TuLanh()
                tl.nhapThongTin()
                danhsach.append(tl)
            for tl in reversed(danhsach):
                print('= = = = = = = =')
                tl.hienThi()
                print('= = = = = = = =')

    @staticmethod
    def testCase3():
        # Nhập n tủ rồi sắp xếp theo giá giảm dần
        n = int(input())
        danhsach = []
        if 0 < n < 100:
            for i in range(n):
                tl = TuLanh()
                tl.nhapThongTin()
                danhsach.append(tl)

        def laygiasosanh(tl_hien_tai):
            return tl_hien_tai.layGia()

        danhsach.sort(key=laygiasosanh, reverse=True)  # reverse=True: Giảm dần

        for tl in danhsach:
            print('= = = = = = = =')
            tl.hienThi()
            print('= = = = = = = =')

    @staticmethod
    def testCase4():
        # Nhập n tủ rồi lưu toàn bộ vào file DsTuLanh.json
        n = int(input())
        danhsach = []
        if 0 < n < 100:
            for i in range(n):
                tl = TuLanh()
                tl.nhapThongTin()
                danhsach.append(tl)

        # Tuần tự hóa: chuyển danh sách đối tượng → danh sách dict
        danhsach_dict = [tl.to_dict() for tl in danhsach]

        try:
            with open("DsTuLanh.json", "w", encoding="utf-8") as f:
                # ensure_ascii=False : giữ tiếng Việt có dấu
                # indent=4          : file JSON dễ đọc hơn
                json.dump(danhsach_dict, f, ensure_ascii=False, indent=4)
            print("Đã lưu danh sách vào tập tin DsTuLanh.json thành công!")
        except Exception as e:
            print(f"Có lỗi xảy ra khi lưu file: {e}")

    @staticmethod
    def testCase5():
        # Nhập n tủ rồi thống kê số lượng theo từng nhãn hiệu (sắp xếp A-Z)
        n = int(input())
        danhsach = []
        if 0 < n < 100:
            for i in range(n):
                tl = TuLanh()
                tl.nhapThongTin()
                danhsach.append(tl)

        thongke = {}  # Dictionary: { "Nhãn hiệu": số lượng }

        for tl in danhsach:
            nhanhieu = tl.layNhan().strip().capitalize()  # Chuẩn hóa: xóa trắng + viết hoa chữ đầu

            if nhanhieu in thongke:
                thongke[nhanhieu] += 1
            else:
                thongke[nhanhieu] = 1  # Xuất hiện lần đầu → thêm mới

        # Sắp xếp theo ABC rồi in kết quả
        for nhanhieu in sorted(thongke.keys()):
            print(f'{nhanhieu} ({thongke[nhanhieu]})')
