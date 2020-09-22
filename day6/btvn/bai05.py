# Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử. Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict

d = {
	"k1": (1, 2, 3, 4, 5),
	"k2": ("hello", "chao", "add", "asadas", "thu5"),
	"k3": ("e", "d", "c", "b", "a"),
}

for i in d:
	print(d[i][4])