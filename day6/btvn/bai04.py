# Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict


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

l1 = list(myDict.keys())
l1.sort(reverse=True) 
print("3 gia tri key lon nhat: {}, {}, {}".format(l1[0], l1[1], l1[2]))