n=int(input())
x=list(map(int,input().split()))
s=1
for i in x:
    s=s*i
for i in x:
    print((s//i),end=" ")