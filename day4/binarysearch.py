# Implement the binary search.
# Return the index of the target number.
#
# Helpful Resources
# https://www.youtube.com/watch?v=D5SrAga1pno
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
#
import math
def binary_search(array, target):
    left = 0
    right = len(array)-1
    mid = left + (right - left)/2 
    while left < right:
        mid = left + (right - left)/2 
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        if array[mid] > target:
            right = mid - 1    
    return -1

data = [
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11]
]

for d in data:
    print("")
    print(" Array: " + str(d[0]))
    print("Target: " + str(d[1]))
    index_of_target = binary_search(d[0], d[1])
    print(" Index: " + str(index_of_target))
