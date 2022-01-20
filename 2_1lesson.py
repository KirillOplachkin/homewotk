class Character:
    def __init__(self, name, height, skill):
        self.name = name
        self.height = height
        self.skill = skill
    def __str__(self):
        return f'Name : {self.name}\n'\
               f'Height: {self.height}\n' \
               f'Skill: {self.skill}\n'\

class Magacian(Character):
    def attack(self):
        return f'Attacking with spell {self.skill}'

class Titan(Character):
        def attack(self):
            return f'Attacking with spell {self.skill}'


mag = Magacian('jx', 12, 'fireball')
titan = Titan('sjbc', 15, 'box')
print(mag.attack())
print(titan.attack())





