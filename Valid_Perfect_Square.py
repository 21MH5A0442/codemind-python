import math
def perf(n):
    n1=math.sqrt(n)
    if n==int(n1)**2:
        return True
    return False
    
for i in range(int(input())):
    n=int(input())
    print(perf(n))