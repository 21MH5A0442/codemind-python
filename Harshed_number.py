n=int(input())
x=n
sum1=0
while x>0:
    c=x%10
    sum1=sum1+c
    x=x//10
if n%sum1==0:
    print(True)
else:
    print(False)