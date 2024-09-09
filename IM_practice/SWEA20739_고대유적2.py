T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())    # N: 행, M: 열
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 행의 끝이 1로 끝나면 이때의 길이를 확인하고 최댓값 비교 후 갱신
    # 최대길이(max_val) 구하기
    # 연달아 나오는 1 cnt += 1
    # 0이 나와서 끊기는 경우. 끊긴 후 max_val과 비교
    # cnt가 더 크다면 갱신
    # 같은 행에서 다시 1이 나올 수도 있으니까 초기화 해주고 다음 순회 이어갈 수 있도록

    # 가로
    max_val = 0
    for r in range(N):
        cnt = 0     # 행이 바뀌면 초기화
        for c in range(M):
            if arr[r][c] == 1:
                cnt += 1
                if c == M-1:            # 열이 순회 범위의 끝인 경우(행의 끝이 1인 경우)
                    if max_val < cnt:   # 최댓값 비교 후 갱신
                        max_val = cnt
            else:                   # 0인 경우
                if max_val < cnt:   # 최댓값 비교, 갱신
                    max_val = cnt
                    cnt = 0         # 같은 행에서 1 나올 수 있으니까 초기화
                else:               # 짧더라도 초기화
                    cnt = 0

    # 세로
    for c in range(M):
        cnt = 0     # 열이 바뀌면 초기화
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
                if r == N-1:            # 열이 순회 범위의 끝인 경우(행의 끝이 1인 경우)
                    if max_val < cnt:   # 최댓값 비교 후 갱신
                        max_val = cnt
            else:                   # 0인 경우
                if max_val < cnt:   # 최댓값 비교, 갱신
                    max_val = cnt
                    cnt = 0         # 같은 행에서 1 또 나올 수 있으니까 초기화
                else:
                    cnt = 0         # 짧더라도 초기화


    # 구조물 없으면 0출력(길이가 1인 경우는 구조물 아니고 노이즈임)
    # 1이 아예 없거나(다 0이거나) 길이가 1인 경우겠네
    if max_val == 0 or max_val == 1:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {max_val}')



'''
리뷰
1. 함수로 만들어서 전치행렬로 해볼까 했는데 런타인 에러 떠서 원래하던 방법대로 다시 함
1-1. N, M이 달라서 함수 매개변수로 arr, N, M 쓰려고 했는데 전치행렬인 경우 인자에 어떻게 넣어야 되는걸까  
2. else의 else(0나와서 연속된 1 끊겼는데 최대길이는 아닌경우) 고려안해서 수정함
3. 행 순회 코드 복붙해서 열 만들었는데 r == N-1: 이부분 M으로 되어있었음. 
'''
