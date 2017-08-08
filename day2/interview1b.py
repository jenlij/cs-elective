import datetime

def sum_divisible_by(number, max):
    sum = 0
    i = number
    while i < max:
        sum = sum + i
        i = i + number
    return sum

def run_program(max):
    sum = sum_divisible_by(3, max) + sum_divisible_by(5, max) - sum_divisible_by(15, max)
    print("The sum of all the multiples of 3 or 5 below " + str(max) + " is " + str(sum) + ".")



def run_and_measure(max):
    start_time = datetime.datetime.now()
    run_program(max)
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print("This program ran in " + str(duration))

for i in range(0, 7000, 1000):
    run_and_measure(i)