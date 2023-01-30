for i in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    x1=sum(x)
    g=(n*(n+1))//2
    print(g-x1)