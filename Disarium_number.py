n=str(input())
x=len(n)
s=0
m=n
while int(n)>0:
    z=int(n)%10
    s=s+z**int(x)
    n=int(n)//10
    x=x-1
if int(s)==int(m):
    print(True)
else:
    print(False)