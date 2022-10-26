n=int(input())
s=""
for i in str(n):
    if int(i)%2!=0:
        s+=str(int(i)*int(i))
print(s)