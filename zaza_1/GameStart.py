
from fortune import Fortune
from win_or_lose import PlayCasino
bank = 1000
plus_or_minus = 0
print("Выберите слот и ставьте!")
while True:
    slot = int(input("Выберите слот: "))
    bid = int(input("Ваша ставка: "))
    play = PlayCasino(bank, plus_or_minus)
    play.game(slot, bid)
    plus_or_minus = play.plus_or_minus
    ret = input("Хотите продолжить?: yes|no ")
    if ret == "yes":
        continue
    else:
        if play.plus_or_minus > 0:
            print(f"Вы выиграли {play.plus_or_minus}$")
        else:
            print(f"Вы проиграли {play.plus_or_minus}$")
        a = input("Хотите сыграться в фортуну? ")
        if a == "yes":
            print("Ответить только : Верю или Не верю")
            play_2 = Fortune()
            play_2.game(play.plus_or_minus)
            bank += play_2.result
            print(f"Now you have {bank}$")
            break
        else:
            bank += play.plus_or_minus
            print(f"Now you have {bank}$")
            break
