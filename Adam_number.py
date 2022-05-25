n=str(input())
s=n[::-1]
x=int(n)*int(n)
z=int(s)*int(s)
y=str(z)[::-1]
if str(x)==str(y):
    print(True)
else:
    print(False)