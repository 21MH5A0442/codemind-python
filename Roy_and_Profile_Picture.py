n=int(input())
for i in range(int(input())):
    a,b=map(int,input().split())
    if a<n or b<n:
        print("UPLOAD ANOTHER")
    else:
        if (a>=n and b>=n) and a==b:
            print("ACCEPTED")
        else:
            print("CROP IT")