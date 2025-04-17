import sys

input = sys.stdin.readline

count = 1
while True:
    l,p,v = map(int, input().split())
    if p == l == v == 0:
        break
    ans = l * (v // p) + min(v % p, l)
    print(f"Case {count}: {ans}")
    count+=1