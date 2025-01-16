import sys
input = sys.stdin.readline

N = input().strip()
arr = []

for i in N:
    arr.append(int(i))

for i in range(len(arr)):
    max = i
    for j in range(i,len(arr)):
        if arr[max] < arr[j]:
            max = j
    arr[i], arr[max] = arr[max],arr[i]

for i in arr:
    print(i,end="")