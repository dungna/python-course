# Bài 10: Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản

string = 'This is a test example sentence test'
str = string.split(" ")
d = {}
for i in str:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
 
print(d)