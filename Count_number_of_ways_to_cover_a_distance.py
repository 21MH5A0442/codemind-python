n=int(input())
a=1
b=1
c=2
for i in range(n-2):
    k=a+b+c
    a=b
    b=c
    c=k
print(k)