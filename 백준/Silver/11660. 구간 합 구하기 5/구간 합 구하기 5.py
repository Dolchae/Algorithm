import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [0 for _ in range(n)]

#arr 입력 받아 저장
for i in range(n):
    tmp = list(map(int,input().split()))
    arr[i] = tmp


sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

#합 배열 1행 채우기
for i in range(1,n+1):
    sum[1][i] = sum[1][i-1] + arr[0][i-1]

#합 배열 1열 채우기
for i in range(1,n+1):
    sum[i][1] = sum[i-1][1] + arr[i-1][0]

#나머지 합 배열 구하기
for i in range(1,n+1):
    for j in range(1,n+1):
        sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + arr[i-1][j-1]

#테스트케이스에 대한 합 출력
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    ans = sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1]
    print(ans)