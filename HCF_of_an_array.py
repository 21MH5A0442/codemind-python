n=int(input())
x=list(map(int,input().split()))
n1=max(x)
n2=min(x)
s=1
for i in range(n2,n1+1):
    if n2%i==0 and n1%i==0:
        s=i
print(s)