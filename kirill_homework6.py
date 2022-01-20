numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [2, 4, 6, 8, 10]


b = list(map(lambda x: x ** 2, numbers2))

print(b)

while 1:
    try:
        index = int(input('Введите индекс :'))
        if index == 'stop':
         print('Программа завершена ')

        print(numbers[index])
    except IndexError:
        print(f'Вводить только числа от 0 до {len(numbers) - 1}')
    except ValueError:
        print('Вводить только числа!')


