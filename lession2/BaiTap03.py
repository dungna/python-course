n = input("Nhap so nguyen duong < 1000 vao: ")

if n.isnumeric() == True:
    if isinstance(int(n), int) == True:
        if int(n) >= 0:
            if int(n) < 1000:
                tong = 0
                for i in range(int(n) + 1):
                    tong += i
                print("Tong so cac chu so la", str(tong))
            else:
                print("So vua nhap vao la so nguyen duong lon hon 1000!")
        else:
            print("So vua nhap khong phai la so nguyen duong")
    else:
        print("So vua nhap vao khong phai la 1 so nguyen duong")
else:
     print("So vua nhap vao khong phai la 1 so")

