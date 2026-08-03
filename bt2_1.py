for sv in students:

    # Làm sạch dữ liệu
    sv["name"] = sv["name"].strip()
    sv["email"] = sv["email"].strip()
    sv["phone"] = sv["phone"].strip()

    email = sv["email"]
    phone = sv["phone"]

    # Validate Email
    email_hop_le = (
        email.count("@") == 1 and
        (email.endswith(".com") or email.endswith(".edu.vn"))
    )

    # Validate Phone
    phone_hop_le = (
        len(phone) == 10 and
        phone.startswith("0") and
        phone.isdigit()
    )

    # Kết quả
    if email_hop_le and phone_hop_le:
        print(f"[{sv['id']}] {sv['name']} | Email: {email} | SDT: {phone} -> HO SO HOP LE")

    else:

        loi = []

        if email.count("@") != 1:
            loi.append("Thieu @")

        elif not (email.endswith(".com") or email.endswith(".edu.vn")):
            loi.append("Sai duoi email")

        if not phone.isdigit():
            loi.append("SDT chua chu")

        elif len(phone) != 10:
            loi.append("SDT khong du 10 so")

        elif not phone.startswith("0"):
            loi.append("SDT khong bat dau bang 0")

        print(f"[{sv['id']}] {sv['name']} | Email: {email} | SDT: {phone} -> KHONG HOP LE ({', '.join(loi)})")