import sys
sys.setrecursionlimit(10**7)

t = int(input())

def countWorm(x,y):
    if x<0 or x>=row or y<0 or y>=col or ground[x][y] != 1:
        return False
    ground[x][y] = -1 #방문처리
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        countWorm(x+dx,y+dy)

    return True


for _ in range(t):
    row, col, num = map(int, input().split())
    ground = [[0 for _ in range(col)] for _ in range(row)]
    worms = 0

    for _ in range(num):
        x,y = map(int,input().split())
        ground[x][y] = 1

    for i in range(row):
        for j in range(col):
            if ground[i][j] == 1:
                if(countWorm(i,j)): worms += 1

    print(worms)

