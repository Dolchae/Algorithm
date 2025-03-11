import sys

input = sys.stdin.readline
times = []

n = int(input())

for _ in range(n): 
    s, e = map(int, input().split())  
    times.append((s, e))  

times.sort(key=lambda x: (x[1], x[0]))

ans = 0

prev = 0
ans += 1
for cur in range(1,len(times)):
    if times[prev][1] <= times[cur][0]: #이전 회의 종료 시간 <= 현재 회의 시작 시간
        prev = cur
        ans += 1

print(ans)