import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = list(map(int, input().split())) #갑옷
arr.sort()

start = 0
end = len(arr) - 1
ans = 0

while start<end:
    tmp = arr[start] + arr[end]
    if tmp == m:
        ans += 1
        start+=1
        end-=1
    elif tmp < m:
        start += 1
    else:
        end -= 1

print(ans)