from collections import deque

def bfs(x,y):   # 행, 열
    q = deque([(x,y)])
    cnt = 0
    while q:
        x, y = q.popleft()
        for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 'X':    # 범위 안에 있고 X(벽)이 아닌 경우
                if arr[nx][ny] == 'P':  # 사람 만났다면
                    cnt += 1
                q.append((nx,ny))
                arr[nx][ny] = 'X'   # 방문표시(벽으로 바꾸기). 다시 방문안하기 위함

    return cnt


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# 도연이 현재위치 찾기
start_x = start_y = 0
for x in range(N):      # 행
    for y in range(M):  # 열
        if arr[x][y] == 'I':
            start_x = x
            start_y = y
            break
    if arr[start_x][start_y] == 'I':
        break

arr[start_x][start_y] = 'X'     # 방문 표시
result = bfs(start_x,start_y)   # 호출

if result > 0:  # 사람을 만났다면
    print(result)
else:          # 못만났다면
    print('TT')


'''
리뷰
1. 처음에 방문표시하는 위치 이렇게해서 P를 만날 수 없는 구조로 짬; 왜 그랬대?
if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 'X':    # 범위 안에 있고 X(벽)이 아닌 경우
    q.append((nx,ny))
    arr[nx][ny] = 'X'   # 방문표시(벽으로 바꾸기). 다시 방문안하기 위함
    if arr[nx][ny] == 'P':  # 사람 만났다면
        cnt += 1
2. dfs, bfs 둘다 가능하다고 해서 bfs로도 해보긴 했는데 여전히 어느 경우에 dfs, bfs, 델타 인지 명확히 모르겠음

'''