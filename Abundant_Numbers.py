n=int(input())
x=[]
sum1=0
for i in range(1,n):
    if n%i==0:
        x.append(i)
for i in x:
    sum1=sum1+i
if sum1>n:
    print(True)
else:
    print(False)