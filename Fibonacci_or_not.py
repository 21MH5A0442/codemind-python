def fib(n):
    a=0
    b=1
    while b<n:
        sum1=a+b
        a=b
        b=sum1
    if a==n or b==n:
        return True
    else:
        return False
print(fib(int(input())))