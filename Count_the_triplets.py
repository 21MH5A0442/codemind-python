for i in range(int(input())):
    s=int(input())
    x=list(map(int,input().split()))
    c=0
    z=[]
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if(x[i]+x[j])in x:
                z.append([min(x[i],x[j]),max(x[i],x[j])])
                c=c+1
    if len(z):
        print(len(z))
    else:
        print(-1)