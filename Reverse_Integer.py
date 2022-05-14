n=str(input())
if n.startswith("-"):
    j=n.replace("-","")
    x=int(j)
    z=""
    while x>0:
        a=x%10
        if a!=0:
            z=z+str(a)
        x=x//10
    z="-"+z
    print(z)
        
    
else:
    x=int(n)
    z=""
    while x>0:
        a=x%10
        if a!=0:
            z=z+str(a)
        x=x//10
    print(z)
