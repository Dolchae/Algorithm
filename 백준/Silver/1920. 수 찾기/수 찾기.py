import sys
input = sys.stdin.readline

def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    M = int(input().strip())
    B = list(map(int, input().strip().split()))
    
    A.sort()
    
    output = []  # 출력 결과를 저장할 리스트
    
    for target in B:
        start = 0
        end = N - 1
        found = False
        
        while start <= end:
            mid = (start + end) // 2
            if target < A[mid]:
                end = mid - 1
            elif target > A[mid]:
                start = mid + 1
            else:
                found = True
                break
                
        output.append("1" if found else "0")
    
    sys.stdout.write("\n".join(output))
    
if __name__ == '__main__':
    main()
