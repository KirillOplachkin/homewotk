movies = {
    'Темнота': {'Kirill': 7, 'Anna': 10},
    'Брат': {}
}

def add_movies(movie):
    if movie in movies.keys():
        print('Этот фильм уже существует!')
    else:
        movies.update({movie: dict()})
        print('Фильм успешно добавлен')

def rate_movies(movie):
    if movie in movies.keys():
        name = input('Введите свое имя :')
        numb = input('Введите оценку :')
        if numb < 1 or numb > 10:
            print('Оценка должна быть от 1 до 10!')
        else:
            movies[movie].update({name: numb})
            print(f'Добавлена оценка для {movie}, {name} оценил его на {numb} ')
    else:
        print('Этого фильма не существует')

def average_movies():
    for movie, rates in movies.items():
        numb = []
        for i in rates.values():
            numb.append(i)
        if len(numb) == 0:
            print(f'Ещё не оценена для {movie}')
        else:
            print(f'{movie} оценена {sum(numb)/len(numb)}')

while True:
    for f, r in movies.items():
        print(f'{f}: {r}')

    command = input('\nДобавьте комманду(1 - добавить фильм , 2 - добавить оценку, 3 - показать рейтинги , 0 - завершить программу )')

    if command == '0':
         print('Программа завершена ')
         break

    if command == '1':
        film = input('Введите название фильма :')
        add_movies(film)

    if command == '2':
        film = input('Введите название фильма, который хотите оценить :')
        rate_movies(film)

    if command == '3':

        average_movies()

    else:
        print('Команды не существует!')




