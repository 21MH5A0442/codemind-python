x=int(input())
for y in range(0,x):
    n,a,b,k=map(int,input().split())
    L=0
    if (a%b==0):
        L=a
    elif (b%a==0):
        L=b
    else:
        L=a*b
    f=n//L
    c=n//a
    d=n//b
    c=c-f
    d=d-f
    if c+d>=k:
        print("Win")
    else:
        print("Lose")