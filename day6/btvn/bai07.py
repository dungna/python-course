my_dict = {'a': 100, 'b':200, 'c':300}
new_dict = {}
keys = ['a','b']

for key in my_dict:
    if key in keys:
        new_dict.update({key: my_dict.get(key)})
print(new_dict)