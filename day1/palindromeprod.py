

#from 999 to 100, find divisor of large palindrome
#how to determine palindrome? 6 digits, see if 0/5, 1/4, 2/3 match

def palindrome():
    for i in range(100, 1000):
        for j in range(100, 1000):
            x = list(str(i * j))
            if ((x[0] == x[5]) and (x[1] == x[4]) and (x[2] == x[3])):
                return x

print palindrome()


# A palindromic number reads the same both ways. The largest 
# palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.