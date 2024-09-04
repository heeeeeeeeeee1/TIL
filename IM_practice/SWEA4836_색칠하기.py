T = int(input())
for tc in range(1,T+1):
    N = int(input())    # 칠할 영역의 개수

    # 도화지 만들기
    arr = [[0]*10 for _ in range(10)]
    # print(arr)
    # 칠할 영역 좌표
    for _ in range(N):
        r1,c1,r2,c2,color = map(int,input().split())

        # 입력받은 정보로 칠하기
        # 한번 반복할때 마다 칠함
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color

    # 보라색이면 3
    cnt = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                cnt += 1


    print(f'#{tc} {cnt}')