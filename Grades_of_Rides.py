a,b,c=map(int,input().split())
h=50
s=60
v=100
if a>h and b>s and c>v:
    print(10)
elif a>h and b>s and c<=v:
    print(9)
elif b>s and c>v and a<=h:
    print(8)
elif a>h and c>v and b<=s:
    print(7)
elif a>h or b>s or c>v:
    print(6)
else:
    print(5)