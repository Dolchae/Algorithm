import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
maze = [[] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]


for i in range(n):
    tmp = input().strip()
    for j in tmp:
        maze[i].append(int(j))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    global count

    while queue:
        x,y = queue.popleft()

        if x == n-1 and y == m-1:
            return maze[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0<=ny<m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))

print(bfs(0,0))
