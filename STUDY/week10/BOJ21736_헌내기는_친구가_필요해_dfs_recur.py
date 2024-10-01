import sys
sys.setrecursionlimit(10**6)  # 재귀 제한 증가. 이부분 없어서 계속 틀렸었는데...왜?...계속 호출되는거야?

def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:  # 범위 밖에 있으면 그만
        return 0

    if arr[x][y] == 'X':    # 벽이면 그만
        return 0

    global cnt
    if arr[x][y] == 'P':  # 사람만나면
        cnt += 1          # 만난 사람 수 +1

    arr[x][y] = 'X'   # 탐색했으면 표시(벽으로 만들기)

    # 재귀적 호출
    dfs(x+1,y)   # 이렇게 해야 누적합 가능
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x,y-1)


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


cnt = 0
dfs(start_x,start_y)
if cnt > 0:  # 사람을 만났다면
    print(cnt)
else:          # 못만났다면
    print('TT')


'''
리뷰
1. 처음에 델타로 풀려고 해서 '? 이러면 DFS, BFS 한 이유가 없는데?' 
2. 이코테 참고함
3. 문제를 봤을때 델타인지 DFS인지 BFS인지 구분 못함
3-1. 아직 어떻게 DFS, BFS로 접근해야되는지 잘 모르겠음.
4. 좌표 x, y 와 행 열 x, y혼란(수학문제 풀 때의 x, y 좌표랑 섞여서 혼란했음.이때의 x는 열번호 y는 행번호니까?)
5. 함수로 만들어서 쓸 때 return을 뭘 해줄건지 항상 확신이 없음
6. 재귀적으로 생각하지 못한 코드
cnt = 0
if arr[x][y] != 'X':
    if arr[x][y] == 'P':  # 사람만나면
        cnt += 1
    arr[x][y] = 'X'   # 탐색했으면 표시
    # 재귀적 호출
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x,y-1)
    return cnt
7. 인공지능 도움 살짝^.^
8. RecursionError : 'X'로 바꿔서 그런게 아닐까
def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:  # 범위 밖에 있으면 그만
        return 0

    if arr[x][y] == 'X':    # 벽이면 그만
        return 0

    global cnt
    if arr[x][y] == 'P':  # 사람만나면
        cnt += 1          # 만난 사람 수 +1

    arr[x][y] = 'X'   # 탐색했으면 표시(벽으로 만들기)

    # 재귀적 호출
    dfs(x+1,y)   # 이렇게 해야 누적합 가능
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x,y-1)

    return cnt
'''