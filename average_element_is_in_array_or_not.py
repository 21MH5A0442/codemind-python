n=int(input())
x=list(map(int,input().split()))
sum1=0
for i in x:
    sum1=sum1+i
avg= sum1//n
for j in x:
    if avg==j:
        print(True)
        break
else:
    print(False)
