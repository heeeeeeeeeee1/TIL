# 최대이익을 위해 최댓값을 찾는다.
# for i range(??)
# 최댓값에서 그 전의 값들을 빼고, 누적합 해준다.
# total += (max(price) - price[i])

# 최댓값에 도달하면 그 이후에 남은 리스트 중에 최댓값 또 구한다.

# i가 배열의 끝까지 갈때까지 반복
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    price = list(map(int, input().split()))
    # print(price)

    max_profit = 0
    start = 0           # 시작 인덱스
    while start < N:    # N되면 멈춤
        max_i = start   # 새로 순회 시작할 위치(start). 제일 첫 loop 말고는 최댓값 직후의 인덱스가 start
        for i in range(start+1, N):     # 최댓값의 인덱스 갱신 start는 자기 자신이라서 최댓값으로 삼을 인덱스의 범위는 그 다음 부터 보면 됨
            if price[max_i] < price[i]:
                max_i = i
        for i in range(start, max_i):   # 현재 위치부터 최댓값 인덱스 까지 순회
            # if price[i] < price[max_i]:
            max_profit += (price[max_i] - price[i])

        # 최댓값 인덱스 변경
        start = max_i+1

    print(f'#{tc} {max_profit}')

'''
리뷰
1. 접근 방법은 비슷했는데 시간 초과뜸
1-1. max, index로 매번 최댓값과, 최댓값 인덱스 구하는 작업 필요해서 그런듯
    max_profit = 0
    i = 0           # 시작 인덱스
    while i < N:    # N되면 멈춤
        mx = max(price[i:]) # i는 제일 처음말고는 최댓값 직후 인덱스
        max_i = price.index(mx) # 최댓값의 인덱스
        for a in range(i, max_i+1):
            if price[a] < mx:
                max_profit += (mx - price[a])

        # 최댓값 인덱스 변경
        i = max_i+1
2. 최댓값 인덱스 갱신 방법 생각안나서 이전 풀이 참고함
'''