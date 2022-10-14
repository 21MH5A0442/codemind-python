a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    d=0
    for j in range(b,c+1):
        j=str(j)
        if j[-1]=='2' or j[-1]=='3' or j[-1]=='9':
            d+=1
    print(d)