# 1. 빈 보드 만들고 초기돌 놓기
# 2. 8방향으로 뻗어가면서 뒤집을 돌(bw) 있는지 확인
# 3. 현재 돌이랑 다른 색의 돌이 있다면 임시 보관함(temp)에 저장
# 4. 현재 돌이랑 같으면 저장해놨던 임시 돌들을 뒤집음(현재 돌이랑 같은색으로 만들기)
# 테스트 케이스
T = int(input())
for t in range(1, T+1):
    # N: 보드의 한변의 길이(4, 6, 8중 하나), M: 돌을 놓는 횟수
    N, M = map(int, input().split())

    # 빈 보드 만들기
    board = [[0] * (N+1) for _ in range(N+1)] # 좌표가 그대로 인덱스 될 수 있게 N+1

    # 초기돌 놓기
    m = N//2    # middle
    board[m][m] = board[m+1][m+1] = 2   # 2: 백돌
    board[m][m+1] = board[m+1][m] = 1   # 1: 흑돌

    # 8방향 델타(우측부터 시계방향 순회)
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    for _ in range(M):  # M: 돌을 놓는 횟수
        c, r, bw = map(int,input().split())  # col, row
        board[r][c] = bw            # 보드에 돌 놓기. bw: 흑돌1 혹은 백돌2

        for k in range(8):          # 8방향으로 뻗어감
            temp = []               # 뒤집을 후보 돌 좌표 담기
            for x in range(1, N):   # N: 보드 한변의 길이, x: 뻗어나가는 거리
                nr = r + dr[k] * x
                nc = c + dc[k] * x
                if 1 <= nr <= N and 1 <= nc <= N: # 범위 안에 있고
                    if board[nr][nc] == 0:        # 인접한 돌이 0이면(없으면)
                        break                     # 뒤집을게 없음
                    elif board[nr][nc] == bw:     # 인접한 돌이 내 위치의 돌 색과 같으면
                        for tr, tc in temp:       # 뒤집을 후보가 있는 동안(데이터가 있다면)
                            board[tr][tc] = bw    # 임시 후보 돌 꺼내서 뒤집기
                        break
                    else:                       # 다른 색의 돌이면
                        temp.append((nr, nc))   # 뒤집을 후보에 저장
                else:                           # 한 방향의 범위를 벗어나면
                    break                       # 멈추고 그 다음 방향으로

    #-------------------------------------------------------------------------------------

    bcnt = 0    # black
    wcnt = 0    # white
    for lst in board:           # 돌을 놓은 2차원 배열 보드에서 lst를 가져오고
        bcnt += lst.count(1)    # 1(흑돌) 카운팅 # count(찾으려는 값): iterable 자료형에서 사용 가능
        wcnt += lst.count(2)    # 2(백돌) 카운팅

    # 보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임 종료

    # 테스트 케이스, 흑돌, 백돌 개수 출력
    print(f'#{t} {bcnt} {wcnt}')