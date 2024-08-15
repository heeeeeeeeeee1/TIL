# N개의 정수가 들어있는 배열에서
# M개의 합이 가장 큰 경우와 가작 작은 경우의 차이 출력

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 정수의 개수 N, 구간의 개수
    N, M = map(int, input().split())

    # N개의 정수 ai
    ai = list(map(int, input().split()))

    # ai에서 M만큼의 구간합 중에 가장 큰 경우와 작은경우 구하고 뺄셈
    max_val = 0 # 1 이상의 정수 주어지므로 초기값을 0으로 설정. 저번에 풀었을때는 -1e9, 1e9로 했었는데
    min_val = 100000000000
    for i in range(N-M+1):  # N-M까지 순회
        total = 0
        for j in range(i, i+M):
            total += ai[j]  # total: M 구간 만큼의 합
        # 한 사이클 당의 누적합과 max/min_val 값 비교
        if max_val < total: # 합이 현재 최댓값보다 크면
            max_val = total # 최댓값 갱신

        if min_val > total: # 합이 현재 최솟값보다 작으면
            min_val = total # 최솟값 갱신

    # 최댓값 - 최솟값
    result = max_val - min_val

    # 테스트 케이스, 값 출력
    print(f'#{tc} {result}')