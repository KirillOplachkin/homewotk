#Задача 1
class Family:
    def __init__(self, name, height, instruct):
        self.name = name
        self.height = height
        self.instruct = instruct


    def __str__(self):
        return f'Name : {self.name}\n'\
               f'Height: {self.height}\n' \
               f'instruct: {self.instruct}\n'\

class GrandFather(Family):
    def fuction(self):
        return f'Give {self.instruct} instruction for all family'

class Father(Family):
    def fuction(self):
        return f'Give {self.instruct} instruction for son'

class Son(Family):
    def fuction(self):
        return f'{self.instruct} instruction'

gf = GrandFather('Ivan', 1.69, 'Hard')
f = Father('Kirill', 1.87, 'Middle')
s = Son('Bogdan', 1.45, 'Not have')
print(gf.fuction())
print(f.fuction())
print(s.fuction())

#задача 2
print(
'Задача №2'
)
class SpiderMan:
    def __init__(self, name, skill):
        self.name = name
        self.__skill = skill

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Skill: {self.__skill}\n'
    def attack(self):
        return f'Spiderman attack with {self.__skill}'

s = SpiderMan('Peter', 'Web')
print(s)
print(s.attack())

print(
 'Задача №3'
)
#задача№3


class Person:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Skill: {self.skill}\n'

class Titan:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Skill: {self.skill}\n'
    def attack(self):
        return f'Attack with {self.skill} '

class SpiderMan:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Skill: {self.skill}\n'
    def attack(self):
        return f'Attack with {self.skill} '

class Syclop:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Skill: {self.skill}\n'
    def attack(self):
        return f'Attack with {self.skill} '

t = Titan('', 'SuperPower')
s = SpiderMan('', 'Web')
syc = Syclop('', 'Eyes')
print(t.attack())
print(s.attack())
print(syc.attack())

print(
    'Задача №4'
)
#
# class family:
#     class family:
#         def __init__(self, name, fu):
#             self.name = name
#             self.love = love
#
#         def __str__(self):
#             return f'Name : {self.name}\n' \
#                    f'Love : {self.love}\n'\
#
# class grandfather(family):
#     def function(self):
#         return f''

class Bread:
    def __init__(self, typ, compound):
        self.type = typ
        self.compound = compound
    def __str__(self):
        return f'Type: {self.type}\n' \
               f'Compound: {self.compound}\n'

class Pshenichnyi(Bread):
    def typ(self):
        return f'Consists by {self.compound}% of flour'

class Rjanoi(Bread):
    def typ(self):
        return f'Consists by {self.compound}% of flour'

class Soldatskyi(Bread):
    def typ(self):
        return f'Consists by {self.compound}% of flour'

p = Pshenichnyi('', 90)
r = Rjanoi('', 50)
s = Soldatskyi('', 25)
print(p.typ())
print(r.typ())
print(s.typ())





