al="abcdefghijklmnopqrstuvwxyz"
s=input()
z=[]
y=[]
s1=""
for i in s:
    if i not in al:
        z.append(s.index(i))
        y.append(i)
    elif i in al:
        s1=s1+i
s2=list(s1[::-1])
for j in z:
    s2.insert(j,s[j])
print("".join(s2))