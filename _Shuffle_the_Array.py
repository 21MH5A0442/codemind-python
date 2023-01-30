n=int(input())
x=list(map(int,input().split()))
s=int(input())
s1=x[:s]
s2=x[s:]
z=[]
for i,j in zip(s1,s2):
    z.append(i)
    z.append(j)
print(*z)