def fact(n):
    s=1
    for i in range(1,n+1):
        s*=int(i)
    return s
x=int(input())
c=0
for n in str(x):
    c+=fact(int(n))
if c==x:
    print("The number",x,"is a strong number")
else:
    print("The number",x,"is not a strong number")