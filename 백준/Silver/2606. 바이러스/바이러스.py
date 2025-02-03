import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
A = [[] for _ in range(n+1)]
visited = set()
m = int(input())
count = 0

for _ in range(m):
    v,w = map(int,input().split())
    A[v].append(w)
    A[w].append(v)

def dfs(v,A,visited):
    global count
    visited.add(v)
    count += 1

    for w in A[v]:
        if w not in visited:
            dfs(w,A,visited)


dfs(1,A,visited)

print(count-1) #1번 자기자신 제외