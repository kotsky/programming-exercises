'''
You are given 2 sorted arrays same length, which contain 
integers. Count same numbers from these arrays.
'''

arr1 = [13, 27, 35, 40, 49, 55, 59]
arr2 = [17, 35, 39, 40, 55, 58, 60]

# O(N) Time / Space
# def countSameNumbers(arrayOne, arrayTwo):
#     table_of_numbers = getUniqueNumbersFromArrayTwo(arrayTwo)
#     count_of_same_numbers = 0
#     for num in arrayOne:
#         if num in table_of_numbers:
#             count_of_same_numbers += 1
#     return count_of_same_numbers
#
#
# def getUniqueNumbersFromArrayTwo(array):
#     table = {}
#     for num in array:
#         table[num] = True
#     return table

# O(N) Time / O(1) Space
def countSameNumbers(arrayOne, arrayTwo):
    pointer_one = 0
    pointer_two = 0
    array_length = len(arrayOne)
    counter_of_unique_numbers = 0
    while pointer_one < array_length and pointer_two < array_length:
        if arrayOne[pointer_one] == arrayTwo[pointer_two]:
            counter_of_unique_numbers += 1
            pointer_one += 1
            pointer_two += 1
        elif arrayOne[pointer_one] < arrayTwo[pointer_two]:
            pointer_one += 1
        else:
            pointer_two += 1
    return counter_of_unique_numbers

print(countSameNumbers(arr1, arr2))
