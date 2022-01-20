
# for, while
# word = "python"


# for i in range(1, 5+1):
#     print(i)
#     if i == 3:
#     # print("medium")

# word = "python"
# index = 0
# while len(word) != index:
#     print(word[index])
#     print(index)
#     index += 1

# round = 0
# while round !=5:
#     round += 1
#     if round == 3:
#         print("пропускаем")
#         continue
#     print(round)



# counter = 0
# while counter < 5:
#     print(counter)
#     counter += 1
#     if counter == 3:
#         print("something wrong")
#         continue
    # if counter == 3:
    #     print("Program finished")
    #     break
min = 1
max = 100
medium = (1 + 100) // 2
secret_number = 45


while True:
    answer = input(f"{medium}")
    if answer == "Yes":
        print("yes")
        break
    elif answer == ">":
        min = medium
    elif answer == "<":
        medium = max
    else:
        print("incorrect")