def pri(arr,n):
    for i in range(0,n):
        print(arr[i],end="")
        
    print()
def gen(n,arr,i):
    if i==n:
        pri(arr,n)
        return
    arr[i]=0
    gen(n,arr,i+1)
    arr[i]=1
    gen(n,arr,i+1)
n=int(input())
arr=[None]*n
gen(n,arr,0)