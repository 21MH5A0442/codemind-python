def ugly(n):
    while n%2==0:
        n=n//2
    if n==1:
        return True
    while n%3==0:
        n=n//3
    if n==1:
        return True
    if n!=1:
        return False
if ugly(int(input())):
    print ("Ugly Number")
else:
    print("Not Ugly Number")