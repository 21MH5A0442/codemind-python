n=int(input())
x=list(map(int,input().split()))
x1=[i for i in range(0,max(x)+1)]
z=[]
for i in x1:
    if i not in x and i>0:
        z.append(i)
if len(z):
    print(z[0])
else:
    print(max(x)+1)