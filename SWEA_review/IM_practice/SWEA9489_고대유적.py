T = int(input())    # 사진 데이터 개수

for tc in range(1,T+1):
    N, M = map(int, input().split())    # N: 행, M: 열
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행, 열 순회하여 연속된 1 중에 가장 긴 값 찾기
    max_cnt = 0 # 최댓값 초기 설정
    for r in range(N):
        cnt = 0                     # 한 행 당 연속된 1이 몇 개 인지 세고, 초기화
        for c in range(M):
            if arr[r][c] == 1:      # 1이면
                cnt += 1            # cnt 증가
                if max_cnt < cnt:
                    max_cnt = cnt
            else:                   # 0이면
                cnt = 0             # 남은 배열 이어서 1찾기. cnt 초기화


    for c in range(M):
        cnt = 0                     # 한 열 당 연속된 1이 몇 개 인지 세고, 초기화
        for r in range(N):
            if arr[r][c] == 1:      # 1이면
                cnt += 1            # cnt 증가
                if max_cnt < cnt:   # 항상 0으로 1이 끊기는 건 아니잖아. 1로 끝날 수도 있잖아
                    max_cnt = cnt
            else:           # 0이면
                cnt = 0     # 남은 배열 이어서 1찾기. cnt 초기화

    print(f'#{tc} {max_cnt}')

'''
리뷰
1. while 사용 가능한가?
2. 한번에 행, 열 동시 순회 가능한가? 몇몇 문제에서 가능했던 것 같은데 그런 케이스는 어떤 경우인가
3. ㅎ ㅏ arr 만들때 M(열)넣음. 왜 이게 맞다고 생각하면서 넣었지...?
3-1. 테스트 케이스는 정사각 배열이라 상관없지만 직사각 배열이면 오류남=> N(행)으로 수정
4. 이렇게 했더니 테스트케이스 8개만 통과임. 열 순회 마치고 최댓값 갱신하려는 의도로 했던거라 애초에 잘못 생각하고 있던게 맞음
for r in range(N):
    cnt = 0             # 한 행 당 연속된 1이 몇 개 인지 세고, 초기화
    for c in range(M):
        if arr[r][c] == 1:  # 1이면
            cnt += 1        # cnt 증가
        else:               # 0이면
            cnt = 0         # 남은 배열 이어서 1찾기. cnt 초기화
        if max_cnt < cnt:   # 항상 0으로 1이 끊기는 건 아니잖아. 1로 끝날 수도 있잖아
            max_cnt = cnt
4-1. 최댓값 갱신하는 조건문이 if 안에 있어야 정확한 max_cnt 나옴. 중간에 있는 연속된 1의 수도 바로바로 갱신

'''