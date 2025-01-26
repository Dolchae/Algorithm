import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

def divide(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = divide(arr[:mid])
    right = divide(arr[mid:])

    return merge(left,right)

def merge(left, right):
    sorted = []
    i = 0
    j = 0
    while (i<len(left)) and (j<len(right)):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted

sorted_arr = divide(arr)

for i in sorted_arr:
    print(i)
