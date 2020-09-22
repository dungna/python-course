# Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
d1 = {
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

d2 = {
	1: 4,
	5: 3,
	2: 8,
	8: 5,
	9: 10,
	12: 3,
	14: 1,
	3: 4,
	17: 99,
}


k1 = list(d1.keys())
k2 = list(d2.keys())

for i in range(len(k1) - 1):
	for j in range(len(k2)-1):
		if k1[i] == k2[j] and d1[k1[i]] == d2[k2[j]]:
			print("({}".format(k1[i]) + ",{}".format(d1[k1[i]]) + ")")
