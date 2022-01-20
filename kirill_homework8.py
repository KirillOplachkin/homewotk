import random
import datetime

name = input('Введите имя: ')
attempt = int(input('Количество попыток: '))
attempt_1 = attempt
start = datetime.datetime.now()
with open('results.txt', 'w', encoding='UTF-8 ') as file:
    while attempt != 0:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        c = a * b

        try:
            solve = int(input(f'{a} * {b} = ?'))
            attempt -= 1
            if solve == c:
                print(f'Правильно , ответ : {c}')
                print(f'Осталось : {attempt} попыток')
                file.write(f'{a}*{b} = {solve}, {c} - правильно\n')
            else:
                print(f'Неправильно,  ответ: {c}')
                print(f'Осталось : {attempt} попыток')
                file.write(f'{a}*{b} = {solve}, {c} - неправильно\n')
        except ValueError:
            print('Вводить только целые числа! ')

    time = datetime.datetime.now() - start
    file.write(f'было использовано {attempt_1} попыток, потрачено времени {time},  имя:  {name} \n')




