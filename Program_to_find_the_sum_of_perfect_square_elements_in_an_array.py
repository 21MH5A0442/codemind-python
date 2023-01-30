import math
def perf(n):
    n1=math.sqrt(n)
    if int(n1)*int(n1)==n:
        return True
    return False
d=int(input())
x=list(map(int,input().split()))
s=0
for i in x:
    if perf(i):
        s=s+i
print(s)