glasniye = "aeioyuаеоуэыяёюи"

while True:
    glas, soglas = 0, 0
    word = input("Введите слово:")
    if word == "q":
        print("Программа завершена")
        break
    for i in word.lower():
        if i in glasniye:
            glas += 1
        else:
            soglas += 1
    glas_procent = (glas / len(word)) * 100
    soglas_procent = (soglas / len(word)) * 100

    print(
        f"Слово: {word}\n"
        f"Общее количество букв: {len(word)}\n"
        f"гласных : {glas}\n"
        f"согласных : {soglas}\n"
        f"Гласные/согласные: {round(glas_procent, 2)} % / {round(soglas_procent, 2)} %"
    )
