n=int(input())
x=list(map(int,input().split()))
g=sorted(set(x))
if len(x)>=3:
    print(g[-3])
else:
    print(g[-1])