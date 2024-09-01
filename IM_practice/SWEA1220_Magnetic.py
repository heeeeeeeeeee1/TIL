# 1. 파랑(2) 찾고, 직전 값이 1인 경우 교착
# 2. 직전 색깔(prev)을 갱신///파랑이 만난 직전 색
# 빨강이든 파랑이든 하나 기준색 잡고, 한 방향으로 순회하면 될듯

T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for c in range(100):        # 열 우선 순회
        prev = 0                # 직전 값(파랑이 만난 직전 값)
        for r in range(100):
            if arr[r][c] != 0:  # 0이 아닐때(값이 있을때)
                if arr[r][c] == 2 and prev == 1:    # 파랑이고 직전(prev)이 1(빨강)일 때
                    result += 1  # 교착 +1
                prev = arr[r][c]    # 직전 값 갱신(계속 순회할거니까 지금 값이 직전 값.)

    print(f'#{tc} {result}')

'''
리뷰
1. 문제 이해하는게 어려웠다.(유튜브 참고함)
2. 문제를 제대로 이해했다면 어려운 수준은 아닌 것 같다.
'''