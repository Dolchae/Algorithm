import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lesson = list(map(int,input().split()))


def blu_ray(mid):
    count = 1
    cur = 0
    for k in lesson:
        if cur + k > mid:
            count += 1
            cur = k
        else:
            cur += k

    return count


start = max(lesson)
end = sum(lesson)
while start < end:
    mid = (start+end)//2
    count = blu_ray(mid)
    if count > M:
        start = mid+1
    else:
        end = mid

print(start)
