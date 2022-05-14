a,b=map(int,input().split())
z=max(a,b)
for i in range(1,z+1):
    if a%i==0 and b%i==0:
        x=i
print(x)