# dict = {key: value}
dct = (['apple', 'яблоко'], ['lemon', 'лимон'])

dict_en_ru = dict(dct)

new = dict_en_ru.copy()
new = dict_en_ru['lemon'] = 'лимончик'
print(dict_en_ru)
print(dct)
print(type(dct))
# student = {
#     'name': 'Kirill',
#     'age': 16,
#     'height': 176,
#     'hobby': 'swimming'
# }
#
# for k, v in student.items():
#     print(f' {k}: {v}')




# # print(student['name'])
# print(student.keys())
# print(student.values())
# print(student.items())