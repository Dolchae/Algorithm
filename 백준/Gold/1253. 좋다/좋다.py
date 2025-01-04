import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

ans = 0

for k in range(n):
    target = arr[k]
    start = 0
    end = n - 1
    while start<end:
        if arr[start]+arr[end] == target:
            if start != k and end != k:
                ans += 1
                break
            elif start == k:
                start += 1
            elif end == k:
                end -= 1
        elif arr[start]+arr[end] < target:
            start += 1
        else:
            end -= 1
print(ans)
