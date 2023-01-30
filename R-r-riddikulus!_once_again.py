a,b=map(int,input().split())
x=list(map(int,input().split()))
for i in range(b):
    x.append(x.pop(0))
print(*x)