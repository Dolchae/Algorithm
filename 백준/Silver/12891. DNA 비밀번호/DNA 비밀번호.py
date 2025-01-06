import sys
input = sys.stdin.readline

s_len, pw_len = map(int,input().split())
s = input()
checkSecret = 0 #몇 개 충족했는지 확인
checkList = list(map(int, input().split())) #입력 받은 문자열 리스트
myList = [0] * 4 #상태 리스트

ans = 0

def myadd(c):
    global checkSecret, myList, checkList
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):
    global checkSecret, checkList, myList
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

for i in checkList:
    if i == 0:
        checkSecret += 1

for i in range(pw_len):
    myadd(s[i])

if checkSecret == 4:
    ans += 1

for i in range(pw_len,s_len):
    j = i - pw_len
    myadd(s[i])
    myremove(s[j])
    if checkSecret == 4:
        ans += 1

print(ans)
