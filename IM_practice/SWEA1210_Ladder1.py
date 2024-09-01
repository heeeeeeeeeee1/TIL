T = 10 # 테스트 케이스
for tc in range(1,T+1):
    t = int(input())    # 테스트 케이스 각 번호
    N = 100             # 100 x 100 배열
    arr = [list(map(int, input().split())) for i in range(N)]
    # print(arr)

    # 도착점에서 거꾸로 올라가기
    # 1. 도착점(2) 찾기
    for find_end in range(N):       # find_end는 인덱스
        if arr[99][find_end] == 2:  # 99행(100번째 행)에서 2를 찾아라
            end = find_end          # end:그 때의 인덱스
    # print(end) # 57

    #2. 3방향(좌,우,상) 델타 생성(올라가기만 할거라서 하는 안함)
    # 좌우 방향을 우선으로 둬야 알맞게 올라갈 수 있을듯
    # 상방향부터 탐색하면 옆으로 꺾지를 못하니까?
    dr = [0, 0, -1]
    dc = [-1, 1, -0]

    # 탐색 시작 위치 지정
    r = 99
    c = end

    while r > 0:
        for k in range(3):  # 3방향 탐색
            nr = r + dr[k]  # 탐색할 행좌표
            nc = c + dc[k]  # 탐색할 열좌표
            # 탐색할 값이 전체 배열 안에 있고, 1이면
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                arr[r][c] = 0  # 지나온 길(arr[r][c])은 다시 탐색 못하게 0으로 채우고
                r = nr  # 1인 곳으로 이동하고
                c = nc
                break

    print(f'#{t} {c}')


'''
리뷰
1. 왜 조건을 이렇게 달았지? 발견해서 다행///if 0 <= arr[nr][nc] < N and arr[nr][nc] == 1:
2. 이중 for문으로 돌렸다가 쓸데없이 열 순회함
    for r in range(N-1,-1,-1):
        for c in range(end,-1,-1):    # 얘를 순회돌려서 잘못된 값이 나온거?
            for k in range(3):  # 3방향 탐색
                nr = r + dr[k]  # 탐색할 행좌표
                nc = c + dc[k]  # 탐색할 열좌표
                # 탐색할 값이 전체 배열 안에 있고, 1이면
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                    arr[r][c] = 0   # 지나온 길(arr[r][c])은 다시 탐색 못하게 0으로 채우고
                    r = nr          # 1인 곳으로 이동하고
                    c = nc
    # 탐색 다 했으면 종료됐을 때의 열(c) 출력
    print(c)

3. while로 수정했는데 break 안해서 또 무한루프에 갇힘
3-1. break 없으면 1인 지점 찾아 놓고 다음 델타순회 이어서 함
3-2. while 종료 조건 제대로 못세움
'''
