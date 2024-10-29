import sys
sys.setrecursionlimit(10**6)

# 배추 찾아서 dfs 탐색
def dfs(r, c):
    # 우 하 좌 상
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        # 범위 안에 있고 배추 있으면
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
            # 또 탐색하지 않도록 탐색한 배추는 지워
            arr[nr][nc] = -1
            dfs(nr, nc)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # M: 가로(열 길이), N: 세로(행 길이), K: 배추 개수
    arr = [[0]*M for _ in range(N)]
    # visited = [[0]*M for _ in range(N)]

    for _ in range(K):  # 배추 위치
        c, r = map(int, input().split())
        arr[r][c] = 1   # 배추 입력


    # 배추들이 모여있는 곳 찾으면 지렁이 += 1
    worm = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                dfs(r,c)   # 모여 있는 배추 찾고, 더이상 없으면 return 됨
                worm += 1
    print(worm)

'''
리뷰
1. 재귀 깊이 설정 기억하자^^
import sys
sys.setrecursionlimit(10**6)
'''