'''
FAIL
으악 디버깅 못하겠어요
'''
from collections import deque
M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

def bfs(arr):
    q = deque()

    # 익은 토마토 찾기(여러개인 경우도 다 큐에 넣기)
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                q.append((r, c))


    days = -1   # 0으로 했었는데 문해력 이슈일까? 0일차부터 4방향으로 익기 시작하는거야? 1일차가 아니라?
    while q:
        r, c = q.popleft()
        for nr,nc in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)]: # 왼 오 앞(상) 뒤(하)
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:  # 범위안에 있고 현위치가 익은 토마토라면
                # 같은 레벨의 상하좌우 토마토는 내일 익겠지
                arr[nr][nc] = 1     # 익어라
                q.append((nr,nc))   # 얘 기준으로 상하좌우 또 봐야되니까 큐에 넣어
        days += 1   # 4방향으로 다 익히고 날짜(일) 증가

        # 이미 익은애는 어떡해? 상관없어?

    # q에 아무것도 없으면 작업 다 했다는거니까
    # 이 때 하나라도 안익은 토마토 있으면 -1
    for row in arr:
        if row.count(0) >= 1:
            return -1   # 함수 return 이렇게 나뉘어지는거 왜 아직도 명확하게 모르겠죠?
    return days

print(bfs(arr))


'''
리뷰
1. 토마토를 중심으로 같은 레벨에 있는 토마토가 영향을 받으니까 BFS?
1-1. 문제를 봤을때 DFS, BFS 구분 못하겠어요!
2. 익은 토마토가 여러개인 경우 어떻게 해야되나 했는데
2-1. 큐에 다 넣으면 되는거였다. ft.퍼선생
'''