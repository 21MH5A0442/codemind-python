def pn(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
def np(x,y):
    for k in range(1,6):
        z=x+y
        m=z+k
        if pn(m):
            break
    print(m-z)
x=int(input())
y=int(input())
np(x,y)