# Implement the bubble sort algorithm in the bubble_sort method.
# Return the sorted array.
#
# Helpful Resources
# https://www.youtube.com/watch?v=8Kp-8OGwphY
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
#

def bubble_sort(my_array):
    swapped = True
    arrLength = len(my_array)
    while swapped == True:
        swapped = False
        for i in range(arrLength-1):
            if my_array[i] > my_array[i+1]:
                temp1 = my_array[i]
                temp2 = my_array[i+1]
                my_array[i+1] = temp1
                my_array[i] = temp2
                swapped = True
           
    #repeat loop 1 until no two values were swapped
    #repeat loop 2 comparing array[i] to array[i+1]
    #if array[i]  > array[i+1], swap and set swapped = true
    return my_array

# print bubble_sort([5,4,3,2,1])



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
    sorted_array = bubble_sort(array)
    print("Output: " + str(sorted_array))

# instructor solution
def bubs(arr):
    swapped = True
    while (swapped):
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr
print bubs([5,4,3,2,1])