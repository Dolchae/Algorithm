import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int,input().split()))
S = [0] * n

for i in range(1,n):
    cur = line[i]
    cur_index = i
    for j in range(i-1,-1,-1):
        if j == 0:
            cur_index = 0
        if line[j] < cur:
            cur_index = j+1
            break
    for k in range(i,cur_index,-1):
        line[k] = line[k-1]
    line[cur_index] = cur


for i in range(n):
    S[i] = S[i-1] + line[i]

sum = 0
for i in range(n):
    sum += S[i]

print(sum)