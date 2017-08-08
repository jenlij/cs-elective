import datetime

def run_program(max):
    sum = 0

    for i in range(1, max):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i

    print("The sum of all the multiples of 3 or 5 below " + str(max) + " is " + str(sum) + ".")

def run_and_measure(max):
    start_time = datetime.datetime.now()
    run_program(max)
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print("This program ran in " + str(duration))


for i in range(0, 7000, 1000):
    run_and_measure(i)