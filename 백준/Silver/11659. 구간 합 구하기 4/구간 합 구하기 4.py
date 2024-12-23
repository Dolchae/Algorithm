import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(map(int,input().split()))
sum = []
tmp = 0

for i in range(n):
    tmp += arr[i]
    sum.append(tmp)


for _ in range(m):
    i,j = map(int,input().split())
    i -= 2
    j -= 1
    if i==-1:
        ans = sum[j]
    else:
        ans = sum[j] - sum[i]
    print(ans)
