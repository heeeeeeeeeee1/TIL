T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())    # N: 행/열, M: 스프레이 세기
    arr = [list(map(int,input().split())) for _ in range(N)]    # N x N 배열

    # + 모양 스프레이
    max_flies = 0
    for r in range(N):
        for c in range(N):
            dead_flies = arr[r][c]  # 현재 위치를 기본으로 두고///얘 위치 여기 맞아? 초기화 위치
            for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:  # 이렇게 하는게 맞던가

                for step in range(1, M):           # M: 순회하는 위치 기준 분사 거리
                    nr = r + dr * step
                    nc = c + dc * step
                    if 0 <= nr < N and 0 <= nc < N:  # 분사된 스프레이가 배열 범위에 있다면
                        dead_flies += arr[nr][nc]    # 일단 조건에 해당하는 파리 다 더해

            # ㅎ ㅏ 얘 위치도 제대로 못잡네^^ + 모양으로 다 더한 dead_flies가 최댓값보다 크면 갱신
            if max_flies < dead_flies:   # arr배열 안의 파리 합이 가장 클 때
                max_flies = dead_flies   # 갱신

    # x 모양 스프레이
    for r in range(N):
        for c in range(N):
            dead_flies = arr[r][c]  # 현재 위치를 기본으로 두고///얘 위치 여기 맞아? 초기화 위치
            for dr, dc in [[-1, 1], [1, 1], [1, -1], [-1, -1]]:  # 우상/ 우하\ 시계방향으로 델타 생성

                for step in range(1, M):  # M: 순회하는 위치 기준 분사 거리
                    nr = r + dr * step
                    nc = c + dc * step
                    if 0 <= nr < N and 0 <= nc < N:  # 분사된 스프레이가 배열 범위에 있다면
                        dead_flies += arr[nr][nc]  # 일단 조건에 해당하는 파리 다 더해

            # ㅎ ㅏ 얘 위치도 제대로 못잡네^^ + 모양으로 다 더한 dead_flies가 최댓값보다 크면 갱신
            if max_flies < dead_flies:  # arr배열 안의 파리 합이 가장 클 때
                max_flies = dead_flies  # 갱신

    # 한번에 잡을 수 있는 최대 파리수
    print(f'#{tc} {max_flies}')


'''
리뷰
1. 델타 안한지 조금 돼서 기억 가물가물
2. +모양, x모양 델타 따로 만들어서 두개로 할까 했다가
2-1. 8방향 델타 만들어서 range의 step을 2로 하면(퐁당퐁당) 가능하지 않을까 라고 생각했는데 
2-2. for문이 너무 많은것 같아서 + 구현 못함^^;
2-3. 처음 생각했던 방법으로 돌아옴
3. step 범위 M-1로 해서 for문 아래로 못내려감
4. 초기화되는 dead_flies 위치와 최댓값 갱신하는 조건문 여전히 헷갈림;
'''