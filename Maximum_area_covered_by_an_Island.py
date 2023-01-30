def check(i,j,grid):
    if (i<0 or j<0 or i>=len(grid) or j>=len(grid[0])):
        return 0
    if grid[i][j]==0:
        return 0
    grid[i][j]=0
    count=1
    for a in range(i-1,i+2,1):
        for b in range(j-1,j+2,1):
            if not(i!=a and j!=b):
                count += check(a,b,grid)
    return count
a,b=map(int,input().split())
grid=[]
z=[]
for _ in range(a):
    x=list(map(int,input().split()))
    grid.append(x)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==1:
            z.append(check(i,j,grid))
print(max(z))  