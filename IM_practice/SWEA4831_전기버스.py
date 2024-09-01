# 충전해서 N까지 가야되는건데
# 인덱스 0일때는 무조건 충전했다고 침(노 카운트)
# 충전기가 있으면 충전(charge+=1) -> k만큼 전진
# (K만큼 이동해서 간 자리에) 충전기 없으면 근처에 충전기 있는지 확인
# 있으면 거기로 이동해서 충전(charge+=1) -> k만큼 전진
# 없으면 stop
# 종점에 도착할 수 없는 경우 0 출력

# 최소 충전 횟수 구해야되니까 한번 충전해서 최대한 멀리가야겠네

T = int(input())
for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    # 충전소가 있으면 1 없으면 0
    station = [0] * (n+1)  # 0번째 인덱스(출발점)에서는는 항상 충전된 상태로 출발
    for a in lst:  # 충전소가 있다면
        station[a] = 1  # 해당 인덱스에 1(있다고) 표시
    # print(station)

    # 일단 station 전진
    i = 0  # 모든 버스는 0에서 시작. 만큼 이동
    charge = 0
    while i < n:        # 언제 종료됨? 여기 틀렸나. 더 이상 전진할 수 없으면 종료되는건데. 예를 들어 9에서 3 전진했으면 어차피 n초과니까 반복문 정지되거 아니야?
        if i == 0:      # 출발점이면
            i = i + k   # charge 증가하지 않고 그냥 k만큼 전진
        else:
            if station[i] == 1:  # 충전기가 있다면
                charge += 1      # 충전하고
                i = i + k        # 전진
            else:                # station[i] == 0:
                for j in range(i - 1, i - k, -1):   # 이전으로 돌아가서
                    if station[j] == 1:             # 1 있는지 확인. 1이면
                        charge += 1                 # 충전하고
                        i = j + k                   # 전진
                        break   # 여기서 break 걸어야 하나. 되돌아갈 때 내 위치 기준 가장 가까운 1에서 충전하고 다시 전진하면 되는데
                                # 1이 아니라면 다음 순회 이어서

                else:   # 순회 다했는데 1없으면 이전으로 되돌아가도 1 없으면 더 이상 못감
                    charge = 0  # 도착지 도착 불가 # charge = 0으로 할까 생각했는데 그럼 초기화 될까봐 다른 변수 둠.
                    break

    print(f'#{tc} {charge}')


'''
리뷰
1. 어디선가 while을 썼던 걸 봐서 사용하는 느낌.
1-1. 문제를 보고 스스로 while 사용해서 풀어야겠다는 생각을 할 수 있었을까?
2. 0번 인덱스를 [1]로 추가해줬었는데, 이렇게 되면 0번(출발점)에서도 충전 횟수 카운팅된다
2-1. -> station[0] = 0으로 두고 첫 if문에 충전 안하고 k만큼 이동하는 코드 작성
3. i = j + k 인데 i = i + k로 작성했었음. 
3-1. while i < N, i <= N 돌려막음. 3번과 함께 전기버스 문제 변형으로 최대한 많이 갈 수 있는 거리 구하는 방식으로 구하다가 오류있는 것 찾아냄
3-1. 하지만 잘못된 코드로도 swea pass...
4. result를 따로 두고 charge를 누적합 했었음... 마지막 else에서 charge = 0으로 하면 뭔가 꼬일 것 같았음(명확한 이유가 있어서가 아니라 그냥 불안해서 변수 추가 한거)
4-1. 하지만 result += charge로 하게되면 불필요하게 누적합됨
'''