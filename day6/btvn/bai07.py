"""
Bài 07: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
Ví dụ:
    dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
    keys = ["name", "salary"]
    Output: {'name': 'Kelly', 'salary': 8000}
"""

sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
new_dict = {i: sampleDict[i] for i in keys}
print(new_dict)