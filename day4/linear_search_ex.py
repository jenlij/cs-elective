# Implement the lineaer search algorithm.
# Return the index of the target value.
#
# Helpful Resources
# https://www.youtube.com/watch?v=CX2CYIJLwfg
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSequentialSearch.html
#

def linear_search_bad_version(array, target):
    for i in array:
        if i == target:
            return array.index(i)
    return -1

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

def linear_search_recursive(array, target, i):
    if i >= len(array):
        return -1 
    if array[i] == target:
        return i
    return linear_search_recursive(array, target, i+1)
    
    

data = [
    [[], 5],
    [[1, 3, 5, 7, 10], 5],
    [range(0, 20, 3), 19],
    [range(0, 20, 2), 18],
    [[1, 2, 3], 10]
]

for d in data:
    print("")
    print(" Array: " + str(d[0]))
    print("Target: " + str(d[1]))
    index_of_target = linear_search_recursive(d[0], d[1], 0)
    print(" Index: " + str(index_of_target))
