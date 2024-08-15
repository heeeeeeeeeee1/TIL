# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # N: 버스 노선
    N = int(input())

    # 노선 표기할 리스트 생성
    bus_stop = [0] * 5001   # 1 ~ 5000번 정류장(0번 정류장은 없음)

    # i번째 버스노선은 Ai이상 Bi이하
    for _ in range(N):
        start, end = map(int,input().split())    # 1 3 // 2 5
        for i in range(start, end+1):   # 노선의 시작점 ~ 도착점을 순회하며, 방문하는 버스정류장(인덱스)에 +1씩 카운트
            bus_stop[i] += 1            # i는 인덱스

    # P개의 버스 정류장
    P = int(input())

    result = []
    # 각 정류장에 몇 개의 버스 노선이 다니는지
    for _ in range(P):
        C = int(input())    # 버스 정류장 번호
        # 버스 정류장 번호에 해당하는 값(카운팅 된 숫자)이 버스 노선의 개수
        result.append(bus_stop[C])

    # print(f'#{tc}', ' '.join(map(str, result)))   # join은 iterable 요소를 문자열로 결합
    print(f'#{tc}', *result)    # 뭐야 이렇게 하면 되던거잖아


    ### 문제 이해를 제대로 못했음. 문제를 이해했다면 카운트 하는 다른 문제 유형들이랑 풀이법은 비슷

