def match(s1,s2):
    x1=[]
    j=0
    for i in s1:
        x1.insert(j,i)
        j=j+2
    m=1
    for k in s2:
        x1.insert(m,k)
        m=m+2
    ss="".join(x1)
    print(ss)
s=input()
al="abcdefghijklmnopqrstuvwxyz0123456789"
c=0
x=[]
y=[]
for i in s.lower():
    if i not in al:
        c=c+1
    elif i.isdigit():
        if int(i)%2==0:
            x.append(i)
        else:
            y.append(i)
if c%2==0:
    match(x,y)
else:
    match(y,x)
        