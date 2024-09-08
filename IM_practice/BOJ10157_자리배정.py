col, row = map(int,input().split())
target = int(input())

# 방향전환 델타(상, 우, 하, 좌)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 만일 모든 좌석이 배정되어 해당 대기번호의 관객에게 좌석을 배정할 수 없는 경우 0 출력
if target > col * row:
    print(0)

else:
    ## 현재 위치에 값 입력 후 이동
    arr = [[0] * col for _ in range(row)]
    cnt = 0 # 한칸 이동할때마다 증가시키고, 그 값을 빈 배열에 입력
    r = row-1   # 문제 그림에서 처럼 출발
    c = 0   # 출발 인덱스
    k = 0   # 방향전환 인덱스
    while cnt <= target: # 빈배열에 입력할 숫자는 전체 배열크기
        cnt += 1
        arr[r][c] = cnt  # 숫자 채우기
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < row and 0<= nc < col and arr[nr][nc] == 0: # 이동할 위치가 범위 안에 있고 0이라면(값이 안채워져있다면)
            # 그 곳으로 이동
            r = nr
            c = nc
        else:   # 범위 벗어나면
            k = (k+1) % 4   # 방향전환
            r = r + dr[k]
            c = c + dc[k]

    # target의 위치 구하기(x,y)
    x = y = 0
    for r in range(row):
        for c in range(col):
            if arr[r][c] == target:
                # y좌표는 행 전체 길이 - r
                # x좌표는 열인덱스 + 1
                x = c + 1
                y = row - r
                print(x, y)

'''
리뷰
1. 달팽이 오랜만에 풀려니 난리났다.
2. 주어진 범위가 큰 것은 알고 있지만 일단 달팽이처럼 풂
2-1. arr = [[0] * col for _ in range(row)]를 else안으로 이동하고
2-2. while cnt <= col*row:에서 while cnt <= target:로 바꿨더니 패스함.
3. 문제를 잘읽자^^ 조건 다 안챙기고 제출해서 틀림.
3-1. 만일 모든 좌석이 배정되어 해당 대기번호의 관객에게 좌석을 배정할 수 없는 경우 0 출력
'''