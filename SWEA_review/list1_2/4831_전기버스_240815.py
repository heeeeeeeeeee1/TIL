# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력
# 노선수 T
T = int(input())
for tc in range(1, T+1):
    # K: 최대이동 정류장 수, N: 총 정류장 수, M: 충전기 설치된 정류장 수
    K, N, M = map(int,input().split())

    # 출발지 + 충전기 설치된 정류장 번호 + 도착지
    charge_stop = [0] + list(map(int, input().split())) + [N]

    # 일단 전진하다가 K범위 이상이어서 못가면 이전 충전기 위치로 돌아와서 충전
    charge = 0
    start = 0
    for i in range(1, M+2):                        # 출발지부터 도착지까지(1 ~ M+1까지)
        # 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우 0 출력
        if charge_stop[i] - charge_stop[i-1] > K:  # 현재위치에서 직전위치사이 거리가 K보다 크면
            charge = 0                             # 이동불가
            break
        if charge_stop[i] - start > K:  # 시작점에서 충전기 위치가 K보다 크면
            start = charge_stop[i-1]    # 이전 정류장에서 충전했어야 함
            charge += 1                 # 충전했으니까 충전횟수 +1

    print(f'#{tc} {charge}')

### 혼자 힘으로 못풂ㅋ