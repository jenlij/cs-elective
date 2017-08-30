##CHALLENGE 1###
# Prison Labor Dodgers
# ====================

# Commander Lambda is all about efficiency, including using her bunny prisoners for manual labor. But no one's been properly monitoring the labor shifts for a while, and they've gotten quite mixed up. You've been given the task of fixing them, but after you wrote up new shifts, you realized that some prisoners had been transferred to a different block and aren't available for their assigned shifts. And manually sorting through each shift list to compare against prisoner block lists will take forever - remember, Commander Lambda loves efficiency!

# Given two almost identical lists of prisoner IDs x and y where one of the lists contains an additional ID, write a function answer(x, y) that compares the lists and returns the additional ID.

# For example, given the lists x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13], the function answer(x, y) would return 6 because the list x contains the integer 6 and the list y doesn't. Given the lists x = [14, 27, 1, 4, 2, 50, 3, 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50], the function answer(x, y) would return -4 because the list y contains the integer -4 and the list x doesn't.

# In each test case, the lists x and y will always contain n non-unique integers where n is at least 1 but never more than 99, and one of the lists will contain an additional unique integer which should be returned by the function.  The same n non-unique integers will be present on both lists, but they might appear in a different order, like in the examples above. Commander Lambda likes to keep her numbers short, so every prisoner ID will be between -1000 and 1000.


def answer(x, y):
    #write a function that compates the lists and returns the additional id
    dict = {}
    new_array = x + y
    for i in new_array:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 0              
    for key in dict:
        if dict[key] == 0:
            return key

def prison_dogers_main():
    x = [13, 5, 6, 2, 5]
    y = [5, 2, 5, 13]
    print answer(x, y) #6

    x1 = [14, 27, 1, 4, 2, 50, 3, 1]
    y1 = [2, 4, -4, 3, 1, 1, 14, 27, 50]
    print answer(x1, y1) #-1


#prison_dogers_main()
       


##CHALLENGE 2####

# Lovely Lucky LAMBs
# ==================

# Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous, she'll hand out Lucky LAMBs (Lambda's All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks, a pillow for their bunks, or even a third daily meal!

# However, actually passing out LAMBs isn't easy. Each henchman squad has a strict seniority ranking which must be respected - or else the henchmen will revolt and you'll all get demoted back to minions again! 

# There are 4 key rules which you must follow in order to avoid a revolt:
#     1. The most junior henchman (with the least seniority) gets exactly 1 LAMB.  (There will always be at least 1 henchman on a team.)
#     2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do.
#     3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get.  (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them.  The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.)
#     4. You can always find more henchmen to pay - the Commander has plenty of employees.  If there are enough LAMBs left over such that another henchman could be added as the most senior while obeying the other rules, you must always add and pay that henchman.

# Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of LAMBs.

# Write a function called answer(total_lambs), where total_lambs is the integer number of LAMBs in the handout you are trying to divide. It should return an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs (that is, being as generous as possible to those you pay and as stingy as possible, respectively) while still obeying all of the above rules to avoid a revolt.  For instance, if you had 10 LAMBs and were as generous as possible, you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending seniority), whereas if you were as stingy as possible, you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore, answer(10) should return 4-3 = 1.

# To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts: you can expect total_lambs to always be between 10 and 1 billion (10 ^ 9).

# Test cases
# ==========

# Inputs:
#     (int) total_lambs = 10
# Output:
#     (int) 1

# Inputs:
#     (int) total_lambs = 143
# Output:
#     (int) 3

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

def answer(total_lambs):
    #Rule 1: 1 lamb per junior henchman. will always be 1 junior
    #Rule 2: 1 level above, max 2times lambs of level below
    #Rule 3: 1 level below, sum no greater than 1 level above
    #Rule 4: everyone gets paid, can add more people to team if necessary
    #lambs must be ints
    #find difference between min and max num of henchmen who can share the lambs
    summation = 0
    i = 0
    # while total_lambs - summation > 2**i:
    #     summation = summation + 2**i
    #     i = i + 1
    # summation2 = 1
    # j = 1
    # while total_lambs > summation2:
    #     summation2 = summation2 + 2**j
    #     j = j + 1
    # return abs(i - j)  
    while total_lambs - summation > 2**i:
        summation = summation + 2** i
        i = i + 1
    fib = 1
    next_fib = 1
    summation2 = 0
    j = 0
    while total_lambs - summation2 > next_fib:
        summation2 = summation2 + fib
        fib, next_fib = next_fib, next_fib + fib
        j = j + 1
    return abs(i-j)


def lambs_main():
    print answer(10)  #1 
    print answer(143)  #3

lambs_main()

1
2
4

1
1
2
3



1
1
2
3
5
8
13
21
34
55

#143


1
2
4
8
16
32
64





