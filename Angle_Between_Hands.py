s=input()
a=int(s[:2])
b=int(s[3:])
d=(360/12)*a+(1/2)*b
e=(360/60)*b
re=abs(d-e)
if re>180:
    re=360-re
print(re)