

#
# def sort(array):
#     swapped = False
#     for i in range(len(array)-1, 0, -1):
#         for j in range(i):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#                 swapped = True
#             if swapped:
#                 swapped = False
#         return array
#
# arr_1 = [76, 99, 156, 34, 5, 90, 14, 8]
# print(f'Sorted list: {sort(arr_1)}')
#
def quick_sort(array):
    if len(array) <= 1:
        return array
    element = array[0]
    left = list(filter(lambda num: num < element, array))
    centre = [nums for nums in array if array == element]
    right = list(filter(lambda num: num > element, array))

    return left + centre + right

arr_1 = [76, 99, 156, 34, 5, 90, 14, 8]
print(f'Sorted list: {quick_sort(arr_1)}')

list_1 = ('Elle', 'Adi', 'Lol')
for i in list_1:
    if i == 'Elle':
        print(i)

for i in range(20):
    if i % 2 == 0:
        print(i)


b = [num for num in range()