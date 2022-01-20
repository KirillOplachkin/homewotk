from random import choice


class Fortune:
    def game(self, bid):
        self.result = 0
        myth_animal = ["Пегас", "Кентавр", "Пифон"]
        random = choice(myth_animal)
        question = choice(myth_animal)
        answer = input(f"За дверью стоит {question}?")
        if bid > 0:
            if answer == "Верю" and random == question or answer == "Не верю" and random != question:
                print(f"За дверью стоял {random}")
                self.result = bid * 2
                print(f"Вы победили! Ваш выигрыш равен: {self.result}$")
            if answer == "верю" and random != question or answer == "не верю" and random == question:
                print(f"За дверью стоял {random}")
                self.result = 0
                print(f"Вы победили! Ваш выигрыш равен: {self.result}$")
        elif bid < 0:  # если проигрывали и вы в минусе
            if answer == "верю" and random == question or answer == "не верю" and random != question:
                print(f"За дверью стоял {random}")
                self.result = 0
                print(f"Вы победили! Ваш проигрыш равен: {self.result}$")
            if answer == "верю" and random != question or answer == "не верю" and random == question:
                print(f"За дверью стоял {random}")
                self.result = bid * 2
                print(f"Вы проиграли! Ваш проигрыш равен: {self.result}$")