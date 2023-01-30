for i in range(int(input())):
    n=int(input())
    n1=str(n)
    if n1==n1[::-1]:
        print("True")
    else:
        print("False")