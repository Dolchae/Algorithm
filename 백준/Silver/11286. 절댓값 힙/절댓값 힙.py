import sys
input = sys.stdin.readline

import heapq

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    # print(heap, "!!!")
    if x == 0:
        if len(heap) == 0:
            print("0")
            continue
        print(heapq.heappop(heap)[1])  
    else:
        heapq.heappush(heap, (abs(x), x))
