# arr[r][c]의 값 만큼 상하좌우 범위 곱하기
# 십자모양 범위 누적합
# 그 중에서 최댓값 구하기

T = int(input())    # 테스트 케이스
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N줄에 걸쳐 M개씩 풍선(N x M)
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 생성

    # 델타 생성 for문으로 해볼까
    max_pang = 0
    for r in range(N):
        for c in range(M):
            spread = arr[r][c]  # 터지는 풍선 안 꽃가루 개수
            total_spread = spread
            for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:  # 우 하 좌 상
                for mul in range(1, spread+1):           # 중앙 꽃가루 개수 만큼 퍼지고
                    nr = r + dr * mul
                    nc = c + dc * mul
                    if 0 <= nr < N and 0 <= nc < M:     # 배열의 범위 안에 있을 경우
                        arr[r][c] += arr[nr][nc]            # 그 범위에 해당하는 값 누적합

            # 십자모양 누적합 중에서 최댓값 구하기
            if max_pang < total_spread:
                max_pang = total_spread

    print(f'#{tc} {max_pang}')

'''
리뷰
1. spread = arr[r][c] 이렇게 한번만 변수로 받아줬는데, 이 부분이 꽃가루 퍼지는 범위로도 들어가고 누적합 받는 역할도 해서 답이 제대로 안나이ㅘㅆ나봄
1-1. spread = arr[r][c]  
     total_spread = arr[r][c] <- 이렇게 해도 되고 total_spread = spread 이렇게 해도 되고 
'''