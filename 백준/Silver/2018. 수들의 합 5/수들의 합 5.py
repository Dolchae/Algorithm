import sys
input = sys.stdin.readline

n = int(input())

start, end, sum, ans = 1,1,1,0


while end <= n:
    if sum < n:
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    else: #정답 케이스
        ans += 1
        sum -= start
        start += 1

print(ans)
