T = int(input())
for tc in range(1,T+1):
    N = int(input())    # 노선 수
    # 원래는 카운트정렬에 넣으려고 했는데
    count = [0] * 1001  # 버스 정류장 번호는 1번~1000번

    for _ in range(N):  # 노선 수 만큼 반복
        bus, start, end = map(int, input().split())

        # 일반버스: 1, 광역버스: 2, 광역 급행: 3
        if bus == 1:                        # 일반 버스일 경우
            for i in range(start,end+1):    # 출발점부터 도착점까지 모두 정차
                count[i] += 1

        elif bus == 2:          # 광역 버스일 경우
            if start % 2 == 0:  # 출발점이 짝수이면 사이의 모든 짝수 번호 정류장에 정차
                for i in range(start,end+1,2):
                    count[i] += 1
            if start % 2 == 1:  # 홀수이면 모든 홀수 정류장에 정차
                for i in range(start,end+1,2):
                    count[i] += 1
        elif bus == 3:          # 광역 급행일 경우
            if start % 2 == 0:  # 출발점이 짝수일 경우 모든 4의 배수 번호 정류장 정차
                for i in range(start,end+1):
                    if i % 4 == 0:
                        count[i] += 1
            if start % 2 == 1:  # 홀수인 경우 3의 배수이면서 10의 배수가 아닌 정류장 정차
                for i in range(start,end+1):
                    if i % 3 == 0 and i % 10 != 0:
                        count[i] += 1

    # 최대 몇개 노선이 일치하는가
    print(f'#{tc} {max(count)}')
'''
리뷰
1. ㅎ ㅏ42분동안 생각만 하고 코딩못해서 삼성시 버스노선 예전 코드 대충 봤는데
1-1. 또 어렵게 생각하고 있었음. 버스마다 다르게 카운팅 배열에 넣으려고 했는데 겹치는 것만 구하면 돼서 그럴 필요가 없었음
'''