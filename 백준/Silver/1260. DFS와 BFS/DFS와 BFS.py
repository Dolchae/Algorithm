import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline
N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
queue = deque()

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

def dfs(v):
    visited[v] = True
    print(v,end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue.append(v)
    while queue:
        cur = queue.popleft()
        visited[cur] = True
        print(cur,end=" ")
        for k in graph[cur]:
            if not visited[k]:
                queue.append(k)
                visited[k] = True



dfs(V)
print()
visited = [False] * (N+1)
bfs(V)