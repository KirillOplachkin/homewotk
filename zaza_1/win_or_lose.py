from random import choice


class PlayCasino:
    def __init__(self, money, plus_or_minus) -> None:
        if isinstance(money, int):
            self.money = money
            self.plus_or_minus = plus_or_minus

    def game(self, number, bid):
        random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30]
        random = choice(random_list)
        print(f"Вы ставите {number}, Сделать ставку {bid}")
        if random == number:
            self.plus_or_minus += bid
            print(f"Выпало: {random}")
            print(f"Вы выиграли! {bid}$!")
            return True
        elif random != number:
            self.money -= bid
            self.plus_or_minus -= bid
            print(f"Выпало: {random}")
            print(f"Вы проиграли: {bid}$")
            return True
        else:
            print("Что то не так")
            return True




