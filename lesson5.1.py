abiturients = [
    {'name': 'Kirill', 'ORT': 150},
    {'name': 'Liza', 'ORT': 220},
    {'name': 'Bogdan', 'ORT': 90}
]
abiturients2 = [
    {'name': 'Kirill', 'ORT': 150},
    {'name': 'Liza', 'ORT': 220},
    {'name': 'nikita', 'ORT': 90}
]


def list_students(list):
    for i in list:
        for k, v in i.items():
            print(f'{k}: {v}', end=' ')
# list_students(abiturients)
list_students(abiturients2)


def add_students(list, name, ORT):
    list.append(dict(name=name, ORT=ORT))
    list_students(list)


add_students(abiturients2, 'Larisa', 160)

def del_students(list, name):
    for i in list:
        if name.title() == i['name']:
            del_s = list.pop(i)
            print(f'{del_s} Удалён из списка')
    list_students(list)

del_students(abiturients2, 'nikita')