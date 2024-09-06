T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]
    # print(flag)

    min_paint = 1000
    for i in range(N-2):
        for j in range(i+1,N-1):    # 이렇게 하면 범위는 2개, 영역은 3개
            paint = 0
            for s in range(i+1):
                paint += (M - flag[s].count('W'))
            for s in range(i+1,j+1):
                paint += (M - flag[s].count('B'))
            for s in range(j+1,N):
                paint += (M - flag[s].count('R'))

            min_paint = min(min_paint,paint)

    print(f'#{tc} {min_paint}')

'''
리뷰
1. 문어박사 아이디어 대충 기억나서 끄적였는데 막힘 -> 다시 참고함
1-1. 다른점이 있다면 칠할 횟수를 마지막이 아니라 순회하면서 정했다는 부분
2. 범위는 맞았는데 색칠된 부분 카운팅할때 변수 없이 _ 로 순회함... 필요없다고 생각했는데 필요함^^
3. 최솟값을 0으로 설정했었음
4. cnt와 paint를 구분해서 누적합 했었는데 그럴필요 없었고, 누적합도 이상하게 되고 있었다.
5. 왜 2개만 맞냐
'''