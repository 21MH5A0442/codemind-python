from itertools import permutations
a,b=map(int,input().split())
s=[i for i in range(1,a+1)]
s1=""
for i in s:
    s1=s1+str(i)
z=[]
for i in permutations(s1):
    z.append(i)
s2=""
for i in z[b-1]:
    s2=s2+i
print(int(s2))