countries = {
    'kg': {'red', 'yellow'},
    'kz': {'blue', 'yellow'},
    'rus':{'white', 'red', 'blue'},
    'usa':{'white', 'red', 'blue'},
    'japan':{'white', 'red'},
    'de':{'black', 'red', 'yellow'}
}


while True:
    colours = input('Введите цвет флага: ')

    if colours == 'q':
        print('Программа завершена.')
        break
    for name, ing in countries.items():
        if colours in ing:
            print(name)
