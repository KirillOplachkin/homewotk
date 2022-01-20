class Animal():
    Class = ['Bird', 'Fish']
    def __init__(self, name, size, age):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name should be string!! ')
        if isinstance(size, str):
            self.size = size
        else:
            raise ValueError('Size should be string!!')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age should be integer!!')

    def __str__(self):
        return f'Name: {self.name} \n' \
               f'Size: {self.size} \n' \
               f'Age: {self.age} \n'

bird = Animal('Eagle', 'Middle', 12)
print(bird)

class Fish(Animal):
    def __init__(self,name, size, age, fin, length, speed):
        super().__init__(name, size, age,)
        if isinstance(fin, str):
            self.fin = fin
        else:
            raise ValueError('Fin should be string')
        if isinstance(length, float):
            self.length = length
        else:
            raise ValueError('Length should be float')
        if isinstance(speed, str):
            self.speed = speed
        else:
            raise ValueError('Speed should be string')

    def __str__(self):
        return super(Fish, self).__str__() + f'Fin: {self.fin} \n' \
                                             f'Length: from {self.length} m \n' \
                                             f'Speed: {self.speed} \n'
fish_1 = Fish('shark', 'big', 2, 'have', 4.9, 'very fast')
print(fish_1)


