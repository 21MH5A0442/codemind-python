a=int(input())
c=""
while a>0:
    c=chr(65+(a-1)%26)+c
    a=(a-1)//26
print(c)