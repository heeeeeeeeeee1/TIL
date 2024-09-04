T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # N x N 순회하면서
    # M x M 범위에 있는 파리의 합 중 최댓값

    max_flies = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            flies = 0
            for x in range(M):
                for y in range(M):
                    flies += arr[r+x][c+y]


            if max_flies < flies:
                max_flies = flies

    print(f'#{tc} {max_flies}')