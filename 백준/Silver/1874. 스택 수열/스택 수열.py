import sys
input = sys.stdin.readline

stack = []

n = int(input())
flag = True #none판단
ans = []


i = 1
for _ in range(n):
    k = int(input())
    if k >= i:
        while k >= i:
            stack.append(i)
            ans.append('+')
            i += 1
        stack.pop()
        ans.append('-')
    else: # k < i
        if stack[-1] == k:
            stack.pop()
            ans.append('-')
        else:
            flag = False
            break

if flag:
    for i in ans:
        print(i)
else:
    print("NO")
