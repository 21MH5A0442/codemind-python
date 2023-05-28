z=[]
n=int(input())
m=int(input())
for i in range(n):
    x=list(map(int,input().split()))
    z.append(x)
c=0
for i in z:
    c=c+sum(i)
print(c)