import random
from modul_14.compare import CompareCards

class BlackJack:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.player = [random.choice(self.cards), random.choice(self.cards)]
        self.computer = [random.choice(self.cards), random.choice(self.cards)]
        self.die_or_win = (0, 0, 1000, 0)

    def Game(self):
        print('Choose options:')
        print('1.Draw cards!')
        print('2. Draw card only to computer')
        print('2. Draw card only to player')
        print('4.')
        print(f'Your cards : {sum(self.player)}')
        choice = int(input('Your choice :'))
        while True:
            compare_1 = CompareCards(player_list=self.player,
                                     computer_list=self.computer)
            if choice == 1:
                self.player.append(random.choice(self.cards))
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
                elif choice == 2:
                    self.player.append(random.choice(self.cards))
                    if compare_1.compare_results():
                        break
                elif choice == 3:
                    self.computer.append(random.choice(self.cards))
                    if compare_1.compare_results():
                        break
                elif choice == 4:
                    self.player.append(random.choice(self.die_or_win))
                    self.computer.append(random.choice(self.die_or_win))
        restart_or_no = input('\n Do you want to restart a game?')
        if restart_or_no == 'S':
            black = BlackJack
            black.Game()
        elif restart_or_no == 'another':
            casino_1 = Casino()
            choice_red = int(input('Red comb choice: '))
            choice_black = int(input('Black comb choice: '))
            casino_1.compare_combination(
                choice_red=choice_red,
                choice_black=choice_black
            )
        else:
            pass



black_cards = BlackJack()
black_cards.Game()