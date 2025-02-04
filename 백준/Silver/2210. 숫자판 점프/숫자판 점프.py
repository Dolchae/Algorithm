import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dy = [1,-1,0,0]
dx = [0,0,1,-1]
A = []
ans = set()


for _ in range(5):
        A.append(list(map(int,input().split())))


def dfs(x,y,cur):
    cur += str(A[x][y])
    if len(cur) == 6:
        ans.add(cur)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx,ny,cur)



for i in range(5):
    for j in range(5):
        #cur = str(A[i][j])
        dfs(i,j,"")
        #print(i,j)

print(len(ans))