def subs(x):
    z=[]
    for i in range(len(x)+1):
        for j in range(i+1,len(x)+1):
            s1=x[i:j]
            z.append(sum(s1))
    print(max(z))
n=int(input())
x=list(map(int,input().split()))
subs(x)