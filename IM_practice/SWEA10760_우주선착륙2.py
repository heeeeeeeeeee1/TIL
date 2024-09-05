T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())    # N줄, M개
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 8방향 델타 우상 대각선부터 시계방향으로
    dr = [-1, 0, 1, 1, 1, 0, -1, -1]
    dc = [1, 1, 1, 0, -1, -1, -1, 0]

    # 8방향 탐색 후 기준값(arr[r][c]보다 높으면 cnt +1

    result = 0
    for r in range(N):
        for c in range(M):
            cnt = 0
            for k in range(8):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M: # 내가 탐색할 위치가 범위 안에 있고
                    if arr[r][c] > arr[nr][nc]: # 비교 위치 보다 탐색할 위치가 작을때 -> 예비후보지
                        cnt += 1
            # cnt가 4이상이면 result += 1
            if cnt >= 4:
                result += 1

    print(f'#{tc} {result}')

'''
리뷰
1. 코드 복붙할 때 주의
2. 엥? 출력값 이상해서 디버깅 해봤는데 이상없어서 그냥 다시 출력해봤는데 맞게 나온다?
2-1. -> 36분
'''