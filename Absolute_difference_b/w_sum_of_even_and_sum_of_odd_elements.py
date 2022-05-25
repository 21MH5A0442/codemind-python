n = int(input())
l =list(map(int,input().split()))
sum1 = 0
sum2=0
for j in l:
    if j % 2 == 0:
        sum1 = sum1 + j
for k in l:
    if k % 2 != 0:
        sum2 = sum2 + k
print(abs(sum1-sum2))
