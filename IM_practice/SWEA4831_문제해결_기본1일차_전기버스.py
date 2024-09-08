T = int(input())    # 노선 수
for tc in range(1,T+1):
    K, N, M = map(int,input().split())  # K: 충전 후 가능한 최대 이동 정류장 수, N: 종점 정류장 번호, M: 정류장 수
    bus_stop = [0] + list(map(int,input().split())) + [N]
    # print(bus_stop)

    # 출발점에는 항상 충전기가 설치되어있지만 충전횟수에는 포함하지 않는다.
    charge = 0
    start = bus_stop[0]
    for i in range(1,M+2): # 정류장 개수(M)에 출발점, 도착점 추가 했고 도착점까지 가야되니까
        # 정류장들 간의 사이 간격이 K보다 크면 어차피 도착점에 도착못함
        if bus_stop[i] - bus_stop[i-1] > K:
            charge = 0
            break

        # start를 기준으로 거리를 비교해서 이동
        elif bus_stop[i] - start > K:
            start = bus_stop[i-1]
            charge += 1

    print(f'#{tc} {charge}')


'''
리뷰
1. 이 풀이방법이 훨씬 간단하긴한데 시험상황에서 내가 생각해낼 수 있을까
2. 인덱스 에러 주의
'''