# January 1, 1701 was a Saturday. How many Saturdays were on the first of the month between 1701 and 1800?
#0.for each year 1701 through 1800 (inclusive)
#1.loop through month 1 through 12
#2. for each month, check day of week of day 1
#3. if day of week equals 5 (sat), add to sum
import datetime
def first_sat():
    sum = 0
    for year in range(1701, 1801):
        for month in range(1, 13):
            d = datetime.datetime(year, month, 1)
            if d.weekday() == 5:
                sum += 1
    return sum            


print first_sat()


# Elon Musk Riddle

#1000
#500
#100
#50
#10
#5
#1


#special cases
#4
#9
#40
#90
#400
#900

#if subtract 1000 > 0, M
#if subtract 500 > 0, D
#100 C
#50 L
#10 X
#5 V
#1 I

def roman_converter(num):
    translation = ''
    if ((num - 1000) > 0):
        translation += 'M'
        num = num - 1000
        print num

    if ((num - 500) > 0):
        translation += 'D'
        num = num - 500
        print num        
    while num > 99:    
        if((num - 100) > 0):
            translation += 'C'
            num = num - 100
            print num
    while num > 50:        
        if ((num - 50) > 0):
            translation += 'L'
            num = num - 50
            print num
    while num > 10:        
        if ((num - 10) > 0):
            translation += 'X'
            num = num - 10
            print num
    while num > 5:        
        if ((num - 5) > 0):
            translation += 'V'
            num = num - 5
            print num
    while num > 0:        
        if ((num - 1) >= 0):
            translation += 'I'  
            num = num - 1
            print num
    return translation


# print roman_converter(999)                           
        
