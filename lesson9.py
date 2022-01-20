


class Car:
    # brand = 'BMW'
    # model = 'C-class 150'
    # engine = 'Germany'
    # fuel = 3,5
    # colour = 'red'
    def __init__(self, brand, model, fuel, colour):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Brand should be string')
        if isinstance(model, str):
            self.model = model
        else:
            raise ValueError('Model should be string')
        if isinstance(fuel, str):
            self.fuel = fuel
        else:
            raise ValueError('Fuel should be float')
        if isinstance(colour, str):
            self.colour = colour
        else:
            raise ValueError('Colour should be string')
        if isinstance(price, int)

    def tunning(self, price):
        total = self.price + price_t



    def __str__(self):
        return f'Brand: {self.brand}\n' \
               f'Model: {self.model}\n' \
               f'Fuel: {self.fuel}\n' \
               f'Colour: {self.colour}\n'



car_1 = Car(
    brand='BMW', model='E545', fuel=5.5, colour='red'
)
car_2 = Car(
    brand='Lexus', model='LX470', fuel=4.7, colour='black'
)
print(car_1)
print(car_2)
