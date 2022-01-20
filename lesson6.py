word = ('one', 'two', 'three', 'four', 'five')
numbers = [1, 2, 3, 4, 5]

# new = dict(zip(numbers, word))
# print(new)
# a = list(filter(lambda x: len(x) <= 6, word))
# print(a)

b = list(map(lambda x: x*x, numbers))
print(b)
#
# dct = {}
# c = 0

# while c < len(word):
#     dct[word[c]] = numbers[c]
#     c += 1
#     print(dct)
# fltr = lambda x: x ** 5
#
# print(fltr(5))


# def bigger(list, func):
#     for i in list:
#         print(func(i))
# #
# # def up_letter(words):
# #     return words.title() + '!'
# #
# #
# #
# # bigger(word, up_letter())
#
# # lambda значение: выражение
#
# # new = lambda x, y: print(x)
# #
# # print(new(5, 9))
#
# # lf = lambda words: words.title() + '!'
#
# bigger(word, lambda words: words.title() + '!' )

# bigger(word, lf)





