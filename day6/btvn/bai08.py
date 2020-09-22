# Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
myDict = {
	1: 4,
	5: 3,
	2: 5,
	8: 1,
	6: 100,
	12: 3,
	14: 1,
	15: 4,
	16: 200
}

l1 = list(myDict.values())
l1.sort(reverse=True) 
print("3 gia tri lon nhat: {}, {}, {}".format(l1[0], l1[1], l1[2]))