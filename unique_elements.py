def u(x):
    y=[]
    for i in x:
        if i not in y:
            y.append(i)
    print(*y)
    
    
n=int(input())
x=list(map(int,input().split()))
u(x)