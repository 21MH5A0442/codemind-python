n=int(input())
z=[]
for i in range(n):
    z.append(int(input()))
x=[]
for j in range(n):
    x.append(int(input()))
for i in z:
    for j in x:
        if i<=j:
            x.remove(j)
        else:
            continue
print(len(x))