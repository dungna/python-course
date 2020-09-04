a = float(input("Nhap canh 1 = "))
b = float(input("Nhap canh 2 = "))
c = float(input("Nhap canh 3 = "))

if (a + b > c) and (a + c > b) and (b + c > c):
    if (a * a == b * b + c * c) or (b * b == a * a + c * c) or (c * c == a * a + b * b):
        print("Canh cua tam gia vuong")
    elif a == b == c:
        print("Canh cua tam giac deu")
    elif (a == b) or (a == c) or (b == c):
        print("Canh cua tam giac can")
    elif (a * a > b * b + c * c) or (b * b > a * a + c * c) or (c * c > a * a + b * b):
        print("Canh cua tam giac tu")
    else:
        print("Canh cua tam giac nhon") 
else:
    print("3 canh vua nhap khong phai la canh cua 1 tam giac")

