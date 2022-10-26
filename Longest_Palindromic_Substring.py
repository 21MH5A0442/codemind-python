def subs(x):
    s=[[]]
    g=0
    z=[]
    if len(x)<=1:
        return x
    for i in range(len(x)+1):
        for j in range(i+1,len(x)+1):
            s=x[i:j]
            if s==s[::-1] and len(s)>g:
                g=len(s)
                z=s
    return z
x=input()
print(subs(x))