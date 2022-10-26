from itertools import permutations
def perm(x):
    z=0
    for i in permutations(x):
        d=int("".join(i))
        if d%2==0:
            z=max(d,z)
    if z==0:
        print(-1)
    else:
        print(z)
s=input()
x=""
for i in s:
    if i.isnumeric():
        x+=str(i)
perm(set(x))