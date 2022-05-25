n = int(input())
l =list(map(int,input().split()))
sum1 = 0
for j in range(len(l)):
    if j % 2 != 0:
        sum1 = sum1 + l[j]
print(sum1)