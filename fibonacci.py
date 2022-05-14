def fib(n):
    a=0
    b=1
    c=3
    print(a,end=" ")
    print(b,end=" ")
    while c<n:
        sum1=a+b
        a=b
        b=sum1
        c=c+1
        print(b,end=" ")
    print(a+b)
fib(int(input()))