# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 양수의 개수 N
    N = int(input())

    # N개의 양수 ai
    ai = list(map(int, input().split()))

    # 가장 큰 수 구하기
    # mx = max(ai)    # 내장함수
    # mx = 1       # 조건에서 1보다 큰 양수라고 했으니 초기값 0으로 설정
    mx = ai[0] # 혹은 리스트의 0번째 값을 초기값으로
    for val in ai:
        if mx < val:
            mx = val

    # 가장 작은수 구하기
    # mn = min(ai)    # 내장함수
    # mn = -10000
    mn = ai[0]
    for val in ai:
        if mn > val:
            mn = val

    # 차이
    result = mx - mn

    # 테스트 케이스 번호, 답 출력
    print(f'#{tc} {result}')

### 와 초기값을 ai[0]으로 안하고 임의 값 대충 넣었는데... 결과값이 달라지네;