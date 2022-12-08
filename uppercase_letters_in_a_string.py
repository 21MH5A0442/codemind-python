n=str(input())
x=list(n)
c=0
ls=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in x:
    for j in ls:
        if i==j:
            c=c+1
print(c)