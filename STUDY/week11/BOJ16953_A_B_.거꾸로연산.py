# B에서  A 만들기(거꾸로 생각하기)
import sys
input = sys.stdin.readline
A, B = map(int,input().split())

cnt = 1             # 연산 횟수 세기
while True:
    if B == A or B < A:
        break

    elif B % 2 == 0:  # 짝수라면
        B = B // 2  # 2로 나누기
        cnt += 1

    elif str(B)[-1] == '1':   # 끝자리가 1이라면(정수일 경우 인덱싱 불가)
        B = (B - 1) // 10   # 1 빼고 10으로 나누기
        cnt += 1

    else:   # 연산 불가하면(2로 나누기도 안되고 1의자리 1도 못빼고)
        break

if B == A:
    print(cnt)
else:
    print(-1)


'''
리뷰
1. 나한테는 bfs보단 이렇게 접근하는게 더 쉽다...
2. 시간초과 떴다
cnt = 0             # 연산 횟수 세기
while A != B:       # A가 B랑 같아지면 루프 종료
    if B % 2 == 0:  # 짝수라면
        B = B // 2  # 2로 나누기
        cnt += 1

    if str(B)[-1] == '1':   # 끝자리가 1이라면(정수일 경우 인덱싱 불가)
        B = (B - 1) // 10   # 1 빼고 10으로 나누기
        cnt += 1

    # 연산을 반복하면서 B가 A보다 작다면
    # A에서 B를 만들 수 없는 경우이므로 cnt 초기화
    # 초기화 하지 않아도 되지만, 아래에서 루프 종료후 cnt가 0이상인지 아닌지로 출력 구분하기 위해 초기화
    if B < A:
        cnt = 0
        break

# 루프 종료 후
if cnt > 0:         # cnt가 0이상이면
    print(cnt+1)    # 연산의 최솟값에 1 더한 값 출력
else:               # 아니라면(만들 수 없다면)
    print(-1)
2-1. 시간초과를 해결하기 위해 이것 저것 시도함 -> 루프 탈출 조건이 빈약해 불필요한 연산을 계속했던것...
'''