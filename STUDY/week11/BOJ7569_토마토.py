from collections import deque
M, N, H = map(int, input().split()) # M: 가로칸의 수, N: 세로칸의 수, H: 높이
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]

# print(arr)
q = deque()
# 익은 토마토 찾아서 큐에 넣기
for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] == 1:
                q.append((h,r,c))

# bfs
while q:
    h, r, c = q.popleft()

    # 우 하 좌 상 수직상 수직하
    for dh, dr, dc in [(0,0,1),(0,1,0),(0,0,-1),(0,-1,0),(-1,0,0),(1,0,0)]:
        nh = h + dh
        nr = r + dr
        nc = c + dc
        # 범위 안에 있고 안익은 토마토이며 방문하지 않았다면
        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and arr[nh][nr][nc] == 0 and visited[nh][nr][nc] == 0:
            arr[nh][nr][nc] = arr[h][r][c] + 1  # 익히고(날짜로 채워넣어)
            visited[nh][nr][nc] = 1 # 방문표시
            q.append((nh,nr,nc))    # 큐에 넣어

# 루프 종료 후
days = -1
wrong = 0
for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] == 0:   # 하나라도 0이면(안익은 토마토)
                days = -1
                wrong = 1
                break
            else:
                if days < arr[h][r][c]:
                    days = arr[h][r][c]
        if wrong == 1:
            break
    if wrong == 1:
        break


if days >= 0:
    print(days-1)
else:
    print(-1)

'''
리뷰
1. 2차원 토마토 풀어봐서 약간 틀이 외워진 느낌?
2. 3차원 인덱스 모르면 못푼다 : 리스트[높이인덱스][세로인덱스][가로인덱스] = 값
3. 이 부분이 for문 안에 잘못 들어가있었다.
else:
    if days < arr[h][r][c]:
        days = arr[h][r][c]

# 3에 대한 반례
[반례1]
5 5 2
1 0 1 -1 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 -1
-1 -1 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
output: 3
----------
[반례2]///토마토를 처음에 한번에 몰아넣지 않은 경우
10 1 1
1 0 0 0 0 0 0 0 0 1
output: 4
'''