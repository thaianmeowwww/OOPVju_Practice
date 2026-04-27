line=input()
cou=line.split( )
print(len(cou))



"""
CÚ PHÁP: string.split(separator, maxsplit)
- separator: Ký tự phân tách (mặc định là khoảng trắng)
- maxsplit: Số lần cắt tối đa (mặc định là tất cả)

# --- CÁCH 1: DÙNG MẶC ĐỊNH (Xử lý tốt khoảng trắng thừa) ---
txt1 = "  Python   is    fun  "
result1 = txt1.split() 
print(result1) # ['Python', 'is', 'fun']

# --- CÁCH 2: CẮT THEO KÝ TỰ CHỈ ĐỊNH ---
txt2 = "apple-orange-banana"
result2 = txt2.split("-")
print(result2) # ['apple', 'orange', 'banana']

# --- CÁCH 3: GIỚI HẠN SỐ LẦN CẮT ---
txt3 = "090-123-456-789"
result3 = txt3.split("-", 1)
print(result3) # ['090', '123-456-789']
LƯU Ý: 
- split() luôn trả về một LIST (danh sách).
- Nếu dùng split(" "), Python sẽ KHÔNG tự gom nhiều dấu cách.
- Nếu dùng split() không tham số, Python SẼ tự gom nhiều dấu cách.
"""

