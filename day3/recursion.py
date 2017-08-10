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


stars(1, 8)    