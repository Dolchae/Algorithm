import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = set()

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(cur):
    visited.add(cur)
    for k in range(len(graph[cur])):
        value = graph[cur][k]
        if value in visited: continue
        visited.add(value)
        dfs(value)



count = 0
for i in range(1,n+1):
    if i not in visited:
        dfs(i)
        count += 1

print(count)