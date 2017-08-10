# def example_one(num):
#     if num == 10:
#         return

#     print(num)
#     example_one(num + 1)

# example_one(0)

# for i in range(0, 10):
#     print i        

def countdown(n):
    if n < 0:
        return
    print n
    countdown(n - 1)

# countdown(10)  
def fibonacci(x, y, n):
    if n == 0:
        return
    print x
    fibonacci(y, x + y, n - 1)


# fibonacci(1,1,12)    

def stars(n, max):
    if max == 0:
        return
    print "*" * n
    stars(n + 1, max - 1)


# stars(1, 8)    

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

# print factorial(6)    


def reverse_array(array, i):
    if array == None or i >= (len(array) /2):
        return array
    array[i], array[len(array)-1-i] = array[len(array)-1-i], array[i]
    return reverse_array(array, i+1)

print reverse_array([2,4,3,6,5,7], 0)
print reverse_array(None, 0)
    