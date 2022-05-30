def pn(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    return False
def div(x):
    d=0
    for k in range(1,x+1):
        if x%k==0:
            if pn(k)==False:
                d=d+1
    print(d)

x=int(input())
div(x)