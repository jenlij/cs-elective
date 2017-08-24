# Given a rotated array, return the index of a target value. 
# Return -1 if the target value does not exist in the array.
#start with linear search. loop through array. If array[i] == target, return i

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

# linear search up to pivot point
# binary search remaining section if not found


# if target is greater than pivot point
def binary_search(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = left + (right - left)/2 
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        if array[mid] > target:
            right = mid - 1    
    return -1


def rotated_array(array, target):
    return -1

data = [
    [[7, 8, 9, 10, 1, 2, 3, 4, 5, 6 ], 5],
    [[ 9, 10, 1, 2, 3, 4, 5, 6, 7, 8], 9],
]

for d in data:
    print("")
    print(" Array: " + str(d[0]))
    print("Target: " + str(d[1]))
    index_of_target = binary_search(d[0], d[1])
    print(" Index: " + str(index_of_target))

