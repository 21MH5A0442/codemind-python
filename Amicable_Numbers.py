a=int(input())
b=int(input())
f=0
e=0
for i in range(1,a+1):
    if a%i==0:
        f=f+i
for j in range(1,b+1):
    if b%j==0:
        e=e+j
        
if f==e:
    print("Amicable")
else:
    print("Not Amicable")