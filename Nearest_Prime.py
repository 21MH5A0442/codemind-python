def primes(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
def near(n):
    x = n
    y = n
    while primes(x) == False:
        x = x-1
    while primes(y) == False:  
        y = y + 1
    #if abs(n-x) == abs(n-y):
     #   return x,y
    if abs(n-x) > abs(n-y):
        return y
    else:
        return x
x = int(input())
for i in range(x):
    print(near(int(input())))