n=str(input())
x=list(n)
c=0
ls=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in x:
    for j in ls:
        if i==j:
            c=c+1
print(c)