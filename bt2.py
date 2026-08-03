orders = [
    {"id": "DH01", "name": "iPhone 15 Pro Max", "price": 32000000},
    {"id": "DH02", "name": "Tai nghe AirPods Pro", "price": 5500000},
    {"id": "DH03", "name": "MacBook Pro M3 Max", "price": 65000000},
    {"id": "DH04", "name": "Chuot khong day", "price": 450000},
    {"id": "DH05", "name": "Samsung Galaxy S24", "price": 22000000}
]

tong_doanh_thu = 0
so_don_vip = 0
is_suspicious = False

max_order = orders[0]
min_order = orders[0]

for order in orders:

    # 1. Tổng doanh thu
    tong_doanh_thu += order["price"]

    # 2. Đếm đơn VIP
    if order["price"] >= 15000000:
        so_don_vip += 1

    # 3. Tìm đơn lớn nhất
    if order["price"] > max_order["price"]:
        max_order = order

    # 3. Tìm đơn nhỏ nhất
    if order["price"] < min_order["price"]:
        min_order = order

    # 4. Cắm cờ
    if order["price"] > 50000000:
        is_suspicious = True
        print(f"CANH BAO RUI RO: Phat hien don {order['id']} co gia tri {order['price']:,} VND > 50tr!")

print("\nTong doanh thu:", f"{tong_doanh_thu:,}", "VND")
print("So don hang VIP (>=15tr):", so_don_vip)
print(f"Don hang CAO NHAT: {max_order['id']} - {max_order['name']} ({max_order['price']:,} VND)")
print(f"Don hang THAP NHAT: {min_order['id']} - {min_order['name']} ({min_order['price']:,} VND)")
print("KET LUAN CAM CO:", is_suspicious)

