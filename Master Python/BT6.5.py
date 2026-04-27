"""
CÁCH HOẠT ĐỘNG:
map() lấy từng món trong 'iterable' bỏ vào 'function' để xử lý.
Kết quả trả về là một 'map object', nên thường cần bọc list() bên ngoài để xem.

# --- VÍ DỤ 1: CHUYỂN CHUỖI THÀNH SỐ (Hay dùng nhất với split) ---
# Giả sử bạn nhập từ bàn phím: "1 2 3"
input_data = "1 2 3"
numbers = list(map(int, input_data.split()))
print(numbers)  # Kết quả: [1, 2, 3]


# --- VÍ DỤ 2: BÌNH PHƯƠNG CÁC SỐ (Dùng lambda - hàm ẩn danh) ---
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Kết quả: [1, 4, 9, 16]


# --- VÍ DỤ 3: DÙNG VỚI HÀM CÓ SẴN (In hoa tất cả chữ) ---
names = ["anh", "binh", "chi"]
upper_names = list(map(str.upper, names))
print(upper_names)  # Kết quả: ['ANH', 'BINH', 'CHI']

LƯU Ý QUAN TRỌNG:
- map() không làm thay đổi danh sách gốc.
- map() chạy rất nhanh vì nó được tối ưu hóa ở tầng hệ thống.
- Nếu các danh sách đầu vào có độ dài khác nhau, map() sẽ dừng lại ở danh sách ngắn nhất.
"""


n = int(input())
nums = list(map(int, input().split()))

chan = 0
le = 0

# Duyệt qua từng số (gọi là 'so') trong danh sách 'nums'
for so in nums:
    if so % 2 == 0:
        chan += 1  # Tăng số lượng chẵn lên 1
    else:
        le += 1    # Tăng số lượng lẻ lên 1

print(f'Chẵn: {chan}, Lẻ: {le}')