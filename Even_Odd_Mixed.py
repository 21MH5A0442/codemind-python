n=int(input())
t=n
even=0
odd=0
while n>0:
    r=n%10
    if r%2==0:
        even+=1
    elif r%2!=0:
        odd+=1
    n=n//10
if even>0 and odd>0:
    print("Mixed")
elif even>0 and odd<=0:
    print("Even")
else:
    print("Odd")
    