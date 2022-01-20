letters = []
numbers = []

objects = [
  'h', 6.13, 'c', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'G'
]
for i in objects:
    if type(i) == str:
        letters.append(i)
    elif type(i) == int or type(i) == float:
        numbers.append(i)

letters.append(True)

letters.reverse()
del numbers[0]
numbers.insert(1, 2)
numbers.sort()

print(letters)
print(numbers)

