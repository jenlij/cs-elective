def bubble_sort_recursion(array, i = 0):
    if i == len(array):
        return array

    swapped = False
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            swapped = True
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp

    if swapped == False:
        return array

    return bubble_sort_recursion(array, i + 1)

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
    sorted_array = bubble_sort_recursion(array)
    print("Output: " + str(sorted_array))
