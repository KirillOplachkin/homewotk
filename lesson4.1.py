

menu = {
 'beshbarmak' : {'мясо', 'лапша', 'картошка'},
 'lagman' : {'лапша', 'мясо', 'перец'},
 'plov' : {'мясо', 'рис', 'морковь'},
 'svejiy salat' : {'огурец', 'томат', 'лук'}
}

quest = input('Введите ингредиенты:')
for name, ing in menu.items():
     if quest in ing:
         print(name)
     else:
          print(f'{quest} нет в меню, но есть {name}')