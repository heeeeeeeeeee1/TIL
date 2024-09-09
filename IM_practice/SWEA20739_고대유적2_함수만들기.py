# 함수 시도 했던 코드
def find_max(arr,N,M):  # 배열, 행, 열
    max_val = 0
    for r in range(N):
        cnt = 0     # 행이 바뀌면 초기화
        for c in range(M):
            if arr[r][c] == 1:
                cnt += 1
                if c == M-1:            # 열이 순회 범위의 끝인 경우(행의 끝이 1인 경우)
                    if max_val < cnt:   # 최댓값 비교 후 갱신
                        max_val = cnt
            else:                       # 0인 경우
                if max_val < cnt:       # 최댓값 비교, 갱신
                    max_val = cnt
                    cnt = 0             # 같은 행에서 1 나올 수 있으니까 초기화
                else:
                    cnt = 0
    return max_val

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())    # N: 행, M: 열
    arr = [list(map(int,input().split())) for _ in range(N)]


# 구조물 없으면 0출력(길이가 1인 경우는 구조물 아니고 노이즈임)
# 1이 아예 없거나(다 0이거나) 길이가 1인 경우겠네

# 최대길이(max_val) 구하기
# 연달아 나오는 1 cnt += 1

# 0이 나와서 끊기는 경우. 끊긴 후 max_val과 비교
# cnt가 더 크다면 갱신
# 같은 행에서 다시 1이 나올 수도 있으니까 초기화 해주고 다음 순회 이어갈 수 있도록
# 행의 끝이 1로 끝나면 이때의 길이를 확인하고 최댓값 비교 후 갱신


# 전치행렬 정사각배열 아니어도 이렇게 만들 수 있어?
    arr_t = list(map(list,zip(*arr)))

    result = max(find_max(arr,N,M),find_max(arr_t,M,N))

    if result == 0 or result == 1:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {result}')

'''
리뷰
1. 복붙하면서 cnt 위치 바뀌고, 전치행렬일때 입력값 M,N차이..
'''