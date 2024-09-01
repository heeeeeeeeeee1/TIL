# 1632 누울 자리를 찾아라
N = int(input())
arr = [list(input()) for _ in range(N)]

row_result = 0 # 누울 수 있는 자리 몇개인지
for r in range(N):                  # 행 우선순회
    cnt = 0
    for c in range(N):
        if arr[r][c] == '.':        # 빈 자리라면
            cnt += 1
            if c == N-1:            # 순회 끝이 '.'로 끝나고
                if cnt >= 2:        # 누울자리('.') 2이상인지 확인하고
                    row_result += 1 # 맞으면 result 증가
        else:                       # X인 경우
            if cnt == 0:            # 첫 시작이 'X'라서 cnt가 아무것도 없으면
                continue            # 계속 순회
            else:                   # 앞에서 '.'가 카운팅된 경우(즉, X가 나와서 누울자리 카운팅이 끊긴 경우)
                if cnt >= 2:        # 끊긴 cnt가 2이상이면
                    row_result += 1 # 누울자리 +1
                    cnt = 0         # 다시 이어서 돌아야 될 수 도 있으니까 초기화
                else:
                    cnt = 0

col_result = 0 # 누울 수 있는 자리 몇개인지
for c in range(N):                  # 열 우선순회
    cnt = 0
    for r in range(N):
        if arr[r][c] == '.':        # 빈 자리라면
            cnt += 1
            if r == N-1:            # 순회 끝이 '.'로 끝나고///왜 이 조건 내려가지? 그냥 파란 블럭이 그렇게 가는건가
                if cnt >= 2:        # 누울자리('.') 2이상인지 확인하고///여기서 튕기긴하는데
                    col_result += 1 # 맞으면 result 증가
        else:                       # X인 경우
            if cnt == 0:            # 첫 시작이 'X'라서 cnt가 아무것도 없으면
                continue            # 계속 순회
            else:                   # 앞에서 '.'가 카운팅된 경우(즉, X가 나와서 누울자리 카운팅이 끊긴 경우)
                if cnt >= 2:        # 끊긴 cnt가 2이상이면
                    col_result += 1 # 누울자리 +1
                    cnt = 0         # 다시 이어서 돌아야 될 수 도 있으니까 초기화
                else:               # .X.X 퐁당퐁당으로 순회될때 cnt가 2미만이므로 누울자리 안되고, cnt초기화 되어야함
                    cnt = 0         # 휴 찾았나...
print(f'{row_result} {col_result}')

'''
리뷰
1. 이런 유형풀때마다 항상 뭔가 빠져있다.
2. 테스트 케이스에 따라 내가 오류를 잡아낼 수도, 없을 수도 있다는게 가장 문제(테스트 케이스 영향을 많이 받는다는 소리)
2-1. 반례 찾기, 테스트 케이스 만들기 연습 필요
'''