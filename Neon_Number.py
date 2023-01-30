n=int(input())
n1=n*n
n1=str(n1)
s=0
for i in n1:
    s=s+int(i)
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")