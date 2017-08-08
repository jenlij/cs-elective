import datetime
def bubble_sort(array):
    array_length = len(array)
    total_number_of_passes = array_length

    for i in range(0, total_number_of_passes):
        for j in range(0, array_length):
            if j == array_length - 1:
                continue

            if array[j] > array[j + 1]:

                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array


def run_and_measure(array):
    start_time = datetime.datetime.now()
    bubble_sort(array)
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print("array size: " + str(len(array)) + "this bubble sort took " + str(duration))



for i in range(0, 7000, 1000):
    run_and_measure(range(i, 0, -1))   

#for bubble sort:
#Omega - best case scenario (already sorted): linear time O(n)
#Big O -worst case scenario (reverse order): exponential time O(n^2)
#Theta - average scenario: also expontial time

# 7n * n + 1n + 2 = 7n^2 + n + 2 -> n^2
