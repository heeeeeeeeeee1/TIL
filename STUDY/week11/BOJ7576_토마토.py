from collections import deque

M, N = map(int,input().split()) # M: 가로칸의 수, N: 세로칸의 수
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

q = deque()

# 익은 토마토(1) 찾아서 큐에 넣기. 1 여러개일 수 있음
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            q.append((r,c))

while q:
    r, c = q.popleft()  # 토마토 행열 좌표 꺼내기
    visited[r][c] = 1   # 시작 토마토 방문표시

    # 익은 토마토 기준으로 우 하 좌 상 탐색
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr = r + dr
        nc = c + dc
        # 범위를 넘어서지 않고 안익은 토마토이며 방문한적이 없다면
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc]==0 and visited[nr][nc]==0:
            arr[nr][nc] = arr[r][c] + 1     # 토마토 익히고(arr를 토마토 익는데 소요된 날짜로 채우기)
            visited[nr][nc] = 1             # 방문표시 하고
            q.append((nr,nc))               # 큐에 넣기


    # arr의 -1은 토마토가 들어있지 않은 칸
    # arr에 -1이 있어도 다 익을 수 있음. 다 안익을 수도 있고

# 토마토가 모두 익지는 못하는 상황이면 -1 출력
# 5번째 테스트 케이스처럼 처음부터 다 익어있는 경우 0일 걸림
days = -1
for lst in arr:
    if lst.count(0) != 0:   # 0이 하나라도 있으면
        days = -1           # 이 부분 없어서 틀렸었음.
        break
    else:   # 토마토가 다 익긴했으면(0 없으면)///-1이 있을 수는 있겠지
        days = max(days,max(lst))   # 최댓값이 최소 날짜


if days >= 0:       # 갱신한 최댓값이 0보다 크거나 같으면
    # 마지막 테케의 경우, 이미 익은 상태의 토마토들만 있어서 arr에 새로 날짜를 입력하는 작업을 하지 않았지만, 익은 토마토 표시인 1이 위의 else에 걸려서 날짜취급을 받고 days가 1로 갱신됨
    print(days-1)   # arr[nr][nc] = arr[r][c] + 1 <- 익은 토마토(arr[r][c])는 1이고 날짜를 이렇게 계산해서 토마토 익는데 소요된 시간이 2부터 시작하게 되므로 1 빼줘야홤
else:
    print(days)


'''
리뷰
1. 지난주에 시도했다가 못풀었던 문제 재시도
1-1. 다른 bfs문제도 풀고 스터디장 힌트도 들었어서 날짜를 어떻게 구할지에 대해 방향 잡을 수 있었음
2. 토마토 다 익히고 마지막에 넣은 날짜값(arr[nr][nc] = arr[r][c] + 1)을 어떻게 알지?
2-1. 마지막 arr[nr][nc]를 기억하면 되지 않을까 했는데
2-2. 이미 arr가 날짜로 다 채워졌어도 q에 좌표가 더 들어있으면 루프가 더 돈다.
2-3. 마지막 nr, nc위치가 최소 날짜가 아니였다.
2-4. 그럼 arr가 날짜로 다 채워지면 루프 종료 할 수 있나? -> 모르겠다. 루프 종료하면 전체 배열 다시 봐야지
3. 루프 종료 후 if문 안에 days = -1없어서 틀렸었다.
3-1. 이거 없으면 첫줄에 0없는 케이스의 경우에 days는 days대로 증가하면서 나중에 0나왔을때 반복문 탈출하게돼서 출력값 다르게 나옴
3-2. [반례] -1 나와야 하는데 2 나왔음
3 3
1 0 0
0 0 -1
0 -1 0
'''