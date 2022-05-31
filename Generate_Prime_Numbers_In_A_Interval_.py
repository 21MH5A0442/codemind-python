def pn(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    return False
def rage(x,y):
    for k in range(x,y+1):
        if pn(k):
            print(k)
n=int(input())
m=int(input())
rage(n,m)