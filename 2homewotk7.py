while True:
    number = int(input('Введите число:'))

    if number < 0 or str(number) != str(number)[::-1]:
        print('Универсальное число!')

    else:
        print('Неуверсальное число !')
    break