# 0. visited 빈 배열 만들어서 +1씩 추가
# 1. bfs 탐색할거니까 큐 만들기
# 2. 목표지점(2) 찾기
# 3. bfs 탐색. 같은 레벨에 있으면 같은 숫자가 되도록 레벨 증가할때마다 +1
# 4. 원래 갈 수 없는 땅인 위치는 0
# 5. 갈수는 있지만 도달할수 없는 위치는 -1 -> 이게 뭔소릴까(1이긴한데 목표지점이랑 이어지진 않는다고?)

from collections import deque

def bfs(r,c):
    q.append((r, c))
    visited[r][c] = 1
    # arr[r][c] = 0 # 여기에 넣었다가 증가된 숫자중에 2가되면 0으로 리셋하는 경우 발생

    while q:
        r, c = q.popleft()
        # r, c 기준으로 우하좌상(가로 세로만 움직일수 있으니까) 땅이 1이면 갈 수 있음. 0이면 못감

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr = r + dr
            nc = c + dc
            # 범위안에 있으면서 땅이 1이면 ㄱ
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1 # 방문표시. 탐색한곳은 다시 안보기
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr,nc))

    # 원래 갈수 없는 땅은 0, 갈 수 있는 땅 중에 도달할수 없는 위치 -1
    # 그럼 arr 다 탐색하고 나서 0인 위치는 어차피 탐색못해서 그대로 두면 0이고
    # 다 탐색했지만 여전히 1인 곳은 -1로 바꿔주면 되나? 시간초과 안되려나...
    # 탐색하면서 한번에 처리 어떻게 해?
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1 and visited[r][c] == 0:
                arr[r][c] = -1

    return arr

# ----------------------------------------------------------------------------
n, m = map(int, input().split())    # n: 세로 크기(행 개수), m: 가로 크기(열 개수)
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

q = deque()
# 목표지점(시작점) 찾기
find = 0
for r in range(n):
    for c in range(m):
        if arr[r][c] == 2:
            start_r = r
            start_c = c
            find = 1
            break
    if find == 1:  # 목표지점 1개니까 찾았으면 그만 돌아
        break

arr[start_r][start_c] = 0
result = bfs(start_r,start_c)

for lst in result:
    print(*lst)

'''
리뷰
1. visited에 arr상하좌우가 1인 경우로 하니까 arr에는 그대로 1이어서 출력처럼 안나옴. 2였던게 3이 되기도 함
1-1. 빈 배열(visited)에 채워 넣으려면 우, 하 만 탐색해야함(?)
1-2. 어차피 최단거리 구하는거니까 우, 하 로만 가면된...다고 생각했는데
1-3. 예제가 0,0에서 시작해서 그렇지 다른 케이스면 아닐수도 있잖아?ㅋ
1-4. 그냥 원본 배열을 수정해야겠다 
2. 아니 근데 계속 탐색했던데 또 탐색하게 돼서 visited 필요하네...
2-1. visited는 표시하되 최단거리 표시한 배열 수정은 arr원본에!
3. 런타임에러 떴는데 이부분이었다...
# 목표지점(시작점) 찾기
for r in range(n):
    for c in range(m):
        if arr[r][c] == 2:
            start_r = r
            start_c = c
            break
    if arr[start_r][start_c] == 2:  # 목표지점 1개니까 찾았으면 그만 돌아
        break
'''