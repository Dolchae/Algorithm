import sys
input = sys.stdin.readline

N, target = map(int,input().split())
A = []
for _ in range(N):
    A.append(int(input()))

A.reverse()

cur, ans = 0,0
for i in A:
    if cur == target:
        break
    if i <= (target-cur):
        ans += (target-cur) // i
        cur += i * ((target-cur) // i)



print(ans)