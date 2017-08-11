# Implement the insertion sort algorithm.
# Return the sorted array.
#
# Helpful Resources
# https://www.youtube.com/watch?v=DFG-XuyPYUQ
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
#

import datetime

# Steps
# =====
# for each element i in array
# store value at i in temp variable
# loop backwards from j=i until reach end of array or until you hit a val less than val at i
# move the val at array[j-1] to array[j]

def insertion_sort(my_array):
    for i in range(len(my_array)):
        temp = my_array[i]
        j = i
        while((j > 0) and (my_array[j-1] > temp)): 
            array[j] = array[j-1] 
            j -= 1
        array[j] = temp    
    return my_array

input_arrays = [
    [],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4],
    [4, 6, 1, 3, 7, 8, 4, 3, 4],
    [1],
    [1, 3, 2]
]

for array in input_arrays:
    print("")
    print(" Input: " + str(array))
    sorted_array = insertion_sort(array)
    print("Output: " + str(sorted_array))

# O(n^2)     

# reverse array
# O(n)
def reverse(my_array):
    j = len(my_array) - 1
    for i in range(0, len(my_array) /  2):
        my_array[i], my_array[j] = my_array[j], my_array[i]
        j = j - 1
    return my_array

for array in input_arrays:
    print("")
    print(" Input: " + str(array))
    sorted_array = reverse(array)
    print("Output: " + str(sorted_array))
