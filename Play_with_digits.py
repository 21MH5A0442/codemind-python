n=int(input())
x=str(input())
z=x.replace(" ","")
s=0
for i in z:
    s=s+int(i)
print(s)