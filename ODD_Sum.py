n = int(input())
l =list(map(int,input().split()))
sum1 = 0
for j in l:
    if j % 2 != 0:
        sum1 = sum1 + j
print(sum1)