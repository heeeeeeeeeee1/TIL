# 1. N x N 빈 배열 만들기
# 2. 델타(우 하 좌 상) 탐색하면서
# 3. 1씩 증가하는 숫자 채우기
# 4. 범위를 벗어나는 경우 방향 전환

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N x N
    arr = [[0]*N for _ in range(N)] # 빈 2차원 배열 생성

    dr = [0, 1, 0 , -1] # row
    dc = [1, 0, -1, 0]  # column

    r, c = 0, 0          # 시작점
    k = 0                # 방향 인덱스 초기화
    cnt = 1              # 채울 숫자 1부터 시작
    while cnt <= N * N:  # 배열 꽉 찰때까지 진행
        arr[r][c] = cnt  # 현재 위치에 숫자 채우고
        cnt += 1         # 채울 숫자 증가
        nr = r + dr[k]   # 새로운 방향 계산
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0: # 범위에 있고, 이동할 위치의 값이 0일 경우
            r = nr          # 거기로 이동
            c = nc
        else:               # 범위를 벗어나거나 값이 0이아니면
            k = (k+1) % 4   # 방향 전환
            r = r + dr[k]
            c = c + dc[k]

    print(f'#{tc}')
    for lst in arr:
        print(*lst)

'''
리뷰
1. 대충은 안다고 생각했는데 진짜 대충 앎^^;ㅎ
2. 역시 조건문을 제대로 못 작성하는게 문제
2-1. 어디서 값을 입력 할 것이고 어디로 이동할 것인지
'''