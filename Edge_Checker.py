a,b=map(int,input().split())
if a+1==b or b-1==a or a-1==b or b+1==a:
    print("Yes")
elif a%10==0 and b%10==1 or a%10==1 and b%10==0:
    print("Yes")
else:
    print("No")