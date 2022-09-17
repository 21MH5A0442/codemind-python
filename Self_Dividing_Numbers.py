n=int(input())
m=int(input())
for i in range(n,m+1):
    j=i
    c=0
    x=0
    while i:
        d=i%10
        i=i//10
        x+=1
        if d!=0:
            if j%d==0:
                c+=1
    if x==c:
        print(j,end=" ")