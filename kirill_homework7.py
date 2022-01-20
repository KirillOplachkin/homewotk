import random

quesses = 0
number = random.randint(1, 10)
print('программа загадала число от 1 до 100, Угадай !')
while True:
    quess = int(input('Введите число : '))
    quesses += 1
    if quess < number:
        print('Угадано неверно (загаданное число больше твоего)!')
    if quess > number:
        print('Угадано неверно (загаданное число меньше твоего)!')
    if quess == number:
        print(f'Вы угадали число! за {quesses} попытку-ок')
        break





