# Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict

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

uniqueValues = set(myDict.values())
print(uniqueValues)