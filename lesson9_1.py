class Phone:
    def __init__(self, number , camera , screen , memory):
        if isinstance(number, str):
            self.number = number
        else:
            raise ValueError('Number is not str')
        if isinstance(camera, float):
            self.camera = camera
        else:
            raise ValueError('Camera should be float')
        if isinstance(screen, bool):
            self.screen = screen
        else:
            raise ValueError('Screen should be boolean')
        if isinstance(memory, int):
            self.memory = memory
        else:
            raise ValueError('Memory is integer')

    def __str__(self):
        return f'Number: {self.number}\n' \
               f'Camera: {self.camera}\n' \
               f'Screen: {self.screen}\n' \
               f'Memory: {self.memory}\n'

iphone_13 = Phone('+996558111667', 5.6, True, 512)
print(iphone_13)


class Samsung(Phone):
    def __init__(self, number , camera , screen , memory):
        super().__init__(number , camera , screen , memory)
