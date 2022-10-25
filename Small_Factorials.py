def fact(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

for i in range(int(input())):
    a=fact(int(input()))
    print(a)