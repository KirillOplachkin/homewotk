# words = ['dict', 'list', 'tuple']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# def obj_index(list):
#     while 1:
#         try:
#             index = int(input('enter index:'))
#             print(numbers[index])
#         except IndexError:
#             print(f'Вводить только числа! от 0 до {len(numbers) - 1}')
#         except ValueError:
#             print('Вводить только буквы')




dct = {
    'name': 'Kirill',
    'age': 16
}
print(dct.get('hobby', 'нет такого'))

# try:
#     print(2 / 0)
# except ZeroDivisionError:
#     print('Не делим на ноль')