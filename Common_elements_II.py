n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=[]
b=[]
for i in x:
    if i not in a:
        a.append(i)
for k in y:
    if k not in b:
        b.append(k)
g=[]
for p in a:
    for q in b:
        if p not in b:
            g.append(p)
            continue
for r in b:
    for s in a:
        if r not in a:
            g.append(r)
            continue
z=[]
for h in g:
    if h not in z:
        z.append(h)
print(*z)