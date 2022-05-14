a,b=map(int,input().split())
z=max(a,b)
while True:
    if z%a==0 and z%b==0:
        print(z)
        break
    z+=1