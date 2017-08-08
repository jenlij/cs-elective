# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 50000000.

import datetime

#1.while i is less than max, test if i is divisible by 3 or 5
#2. if yes, add to sum
#3. end when i >= MAX
def run_program():
    MAX = 50000000
    # MAX = 100
    summation = 0
    i = 1
    while i <= MAX:
        if ((i % 3 == 0) or (i % 5 == 0)):
            summation += i
        i += 1
    # print("The sum of all the multiples of 3 or 5 below " + str(MAX) + " is " + str(summation) + ".")
    return summation 

# start_time = datetime.datetime.now()
# print run_program()
# end_time = datetime.datetime.now()
# duration = end_time - start_time
# print("This program ran in " + str(duration))


def run2():
    MAX = 50000000
    summation = 0
    i = 3
    j = 5
    k = 15
    #sum of mult 3
    #plus sum of mult 5
    #minus mult of 15
    #1.calculate sum of multiples of 3 (5, 15)
    #a. loop until i >= max
    #b. add i to sum
    while i <= MAX:
        if (i % 3 == 0):
            summation += i
        i += 3
    while j <= MAX:        
        if (j % 5 == 0):
            summation += j
        j += 5
    while k <= MAX:        
        if(k % 15 == 0):
            summation -= k
        k += 15      
    return summation

# start_time = datetime.datetime.now()
# print run2()
# end_time = datetime.datetime.now()
# duration = end_time - start_time
# print("This program ran in " + str(duration))


# solution
def sum_div_by(num, max):
    sum = 0
    i = num
    while i < max:
        sum = sum + i
        i = i + num
    return sum     

def run_me():
    MAX = 1000
    sum = sum_div_by(3, MAX) + sum_div_by(5, MAX) - sum_div_by(15, MAX)
    return sum

start_time = datetime.datetime.now()
print run_me()
end_time = datetime.datetime.now()
duration = end_time - start_time
print("This program ran in " + str(duration))   

# optimal solution trianglular numbers
# (1+2+3+4...) = n(n+1)/2
# (3+6+9+12+15) = 3(1+2+3+4+5)
# 3n(n+1)/2
# constant time
def opt(num, max):
    p = int((max - 1) / num)
    sum = num * (p * (p + 1)) / 2
    return int(sum)

def run_me2():
    MAX = 1000
    sum = opt(3, MAX) + opt(5, MAX) - opt(15, MAX)
    return sum

start_time = datetime.datetime.now()
print run_me2() 
end_time = datetime.datetime.now()
duration = end_time - start_time 
print("This program ran in " + str(duration))
