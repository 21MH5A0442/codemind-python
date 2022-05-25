def ev(x):
    c=[]
    for i in x:
        if i%2!=0:
            c.append(i)
    if len(c)>0:
        print("False")
    else:
        print("True")
n=int(input())
x=list(map(int,input().split()))
ev(x)