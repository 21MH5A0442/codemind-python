n=int(input())
a=n+1
b=n-1
def pal(n):
    x=str(n)
    z=x[::-1]
    if z==x:
        return True
    else:
        return False
while pal(a)==False:
    a=a+1
while pal(b)==False:
    b=b-1
if abs(a-n)>abs(b-n):
    print(b)
elif abs(a-n)==abs(b-n):
    print(str(b)+" "+str(a))
else:
    print(a)