# bfs
# (1,1)에서 시작하고 (N,M)에 도착하면 된다 == 결국 끝(0,0)에서 끝(N-1,M-1) 가면된다. 1씩 빼야지
# 원본 arr에는 +1씩하면서 바꾸고
# visited 표시해서 탐색했던데 다시 안가게 하고 ㅇㅇ

from collections import deque

def bfs(start_r,start_c):
    visited[start_r][start_c] = 1   # 시작점 방문처리
    q.append((start_r,start_c))

    while q:
        r, c = q.popleft()
        # 인접한 칸만 이동할 수 있으므로 우하좌상
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr = r + dr
            nc = c + dc
            # 방문하지 않았고 이동할 수 있으면(1이라면)
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                q.append((nr, nc))
                arr[nr][nc] = arr[r][c] + 1 # 거리 측정
                visited[nr][nc] = 1

    return arr[N-1][M-1]


N, M = map(int, input().split())    # N개 줄, M개의 정수로 미로///(N,M)의 위치로 이동할 때 지나야 하는 최소 칸수 구하기
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q = deque()

start_r = start_c = 0
print(bfs(start_r,start_c))

'''
리뷰
1. '14940 쉬운 최단거리' 푼 후에 풀었더니 조금 수월하게 푼듯
'''


