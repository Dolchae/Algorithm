import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append((int(input()),i))

arr.sort()


max = arr[0][1] - 0  #현재 위치 - 기존 위치
for i in range(n):
    tmp = arr[i][1] - i
    if max < tmp:
        max = tmp
        
print(max+1)