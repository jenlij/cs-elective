# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 50000000.

import datetime

def run_program():
    MAX = 50000000

    # Write your algorithm here!

    print("The sum of all the multiples of 3 or 5 below " + str(MAX) + " is " + str(sum) + ".")

start_time = datetime.datetime.now()
run_program()
end_time = datetime.datetime.now()
duration = end_time - start_time
print("This program ran in " + str(duration))