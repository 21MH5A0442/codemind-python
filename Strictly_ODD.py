n=int(input())
x=list(map(int,input().split()))
c=[]
for i in x:
    if i%2!=0:
        c.append(i)
d=0
for i in c:
    if x.index(i)%2!=0:
        d+=1
if d==len(c):
    print("True")
else:
    print("False")