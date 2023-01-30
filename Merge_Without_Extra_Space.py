for i in range(int(input())):
    a,b=map(int,input().split())
    x1=list(map(int,input().split()))
    x2=list(map(int,input().split()))
    x3=x1+x2
    print(*sorted(x3))