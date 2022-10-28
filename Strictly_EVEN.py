n=int(input())
x=list(map(int,input().split()))
c=[]
for i in range(len(x)):
    if x[i]%2==0:
        c.append(i)
        
d=0
for k in c:
    if k%2==0:
        d+=1
if d==len(c):
    print("True")
else:
    print("False")