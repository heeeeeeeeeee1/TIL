# 최소 충전 횟수 구해야되니까 한번 충전해서 최대한 멀리가야겠네

T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    # 충전소가 있으면 1 없으면 0
    station = [1] + [0] * n   # 0번째 인덱스(출발점)에서는는 항상 충전된 상태로 출발
    for a in lst:       # 충전소가 있다면
        station[a] = 1          # 해당 인덱스에 1(있다고) 표시
    # print(lst)

    # 일단 station 전진
    i = 0   # 모든 버스는 0에서 시작. 만큼 이동
    result = 0
    charge = 0
    while i < n or result == 0: # 언제 종료됨? 여기 틀렸나. 더 이상 전진할 수 없으면 종료되는건데
        if station[i] == 1: # 충전기가 있다면
            charge += 1 # 충전하고
            result += charge
            i = i + k   # 전진
        else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     +
            for j in range(i-1,i-k,-1):
                if station[j] == 1:
                    charge += 1
                    result += charge
                    i = i + k
                else:   # 되돌아가도 없으면
                    result = 0  # 도착못해
                    break

    print(f'#{tc} {result}')

# 충전해서 N까지 가야되는건데
# 인덱스 0일때는 무조건 충전했다고 침(노 카운트)
# 충전기가 있으면 충전(charge+=1) -> k만큼 전진
# (K만큼 이동해서 간 자리에) 충전기 없으면 근처에 충전기 있는지 확인
# 있으면 거기로 이동해서 충전(charge+=1) -> k만큼 전진
# 없으면 stop
# 종점에 도착할 수 없는 경우 0 출력

'''
리뷰
1. 어디선가 while을 썼던 걸 봐서 사용하는 느낌. 
1-1. 문제를 보고 스스로 while 사용해서 풀어야겠다는 생각을 할 수 있었을까?
'''