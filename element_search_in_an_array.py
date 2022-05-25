a = int(input())
x = list(map(int,input().split()))
y = int(input())
for i in range(a):
    if x[i] == y:
        print(True)
        break
else:
    print(False)
