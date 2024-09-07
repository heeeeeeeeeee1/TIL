
# 왜 4방향만 탐색하면 되지? 하지만 시험이었다면 난 8방향을 봤을거라 8방향 델타 만들거임
# 그런데 격자판이 5 초과 되는 크기일 때 이 방법으로 하면 오목 개수를 세는 경우 틀릴것 같은데? 계속 중복으로 개수 카운팅 돼서...
# 아 이 문제는 YES NO 판정이라 상관없네;

# 오목 판정 함수 만들기
def omok(arr):
    # 8방향 델타 만들기
    dr = [-1, 0, 1, 1, 1, 0, -1, -1]
    dc = [1, 1, 1, 0, -1, -1, -1, 0]

    result = 'NO'
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                  # 그 방향으로 돌이 몇개인지 카운팅
                for k in range(8):  # 8방향으로 탐색
                    cnt = 1
                    for step in range(1,6): # 최대로 이어질 수 있는 경우가 N까지여서 이렇게 하긴했는데 맞는지는 모르겠음
                        nr = r + dr[k] * step   # step: 그 방향으로 연달아 탐색
                        nc = c + dc[k] * step
                        if 0 <= nr < N and 0 <= nc < N:  # 탐색할 곳이 범위 안에 있고
                            if arr[nr][nc] == 'o':
                                cnt += 1
                            else:
                                break
                        else:
                            break
                    # 다음 방향으로 넘어가기 전에 cnt 5 이상인지 판단
                    if cnt >= 5:    # 다 숫자 세고 돌이 5개 이상 있으면
                        result = 'YES'

                        return result

    return result



T = int(input())
for tc in range(1,T+1):
    N = int(input())    # 오목판 크기 N x N
    arr = [list(input()) for _ in range(N)] # 문자열 오목배열
    print(f'#{tc} {omok(arr)}')


'''
리뷰
1. 접근은 맞았는데
2. 또 조건문 못세워서 fail
2-1. break와 함수 만들어서 사용시 return 값 유의
'''
