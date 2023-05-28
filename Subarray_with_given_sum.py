for i in range(int(input())):
    s,k=map(int,input().split())
    x=list(map(int,input().split()))
    z=[]
    strt=0
    for i in range(len(x)):
        while sum(x[strt:i+1])>k:
            strt+=1
        if sum(x[strt:i+1])==k:
            z.append([strt+1,i+1])
            break
    if len(z):
        print(*z[0])
    else:
        print(-1)
        