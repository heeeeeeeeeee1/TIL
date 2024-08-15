# 양쪽 모두 거리 2이상의 공간이 확보될 때 조망권 확보

# 테스트 케이스 10개
T = 10
for tc in range(1, T+1):
    # 건물의 개수 N
    N = int(input())    # 10

    # N개의 건물의 높이
    b = list(map(int, input().split())) # buildings

    # 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이 0
    # 각 빌딩의 높이 최대 255
    # 테스트 케이스 번호, 공백 문자 후 조망권 확보된 세대의 수 출력
    result_sum = 0
    for i in range(2, N-2):   # 맨 앞은 00이니까 인덱스2부터 N-1까지 순환. 맨뒤도 00이니까 줄여도 됨
        # i-2 ~ i+2 범위 중에 i(기준위치)가 가장 크면 조망권 확보
        # i가 가장 크다면 이 범위 중에 i와 나머지 빌딩 중 높은 빌딩과의 차이가 조망권을 가진 세대 수
        b_list = [b[i-2], b[i-1], b[i+1], b[i+2]]
        # 이중에 최댓값이랑 b[i]랑 뺐을때 0이상이면 되는거 아니야?
        # max_b = max(b_list)
        # 내장함수 미사용시
        max_b = 0
        for build in b_list:
            if build > max_b:
                max_b = build

        if b[i] - max_b > 0:
            result = b[i] - max_b
            result_sum += result

    print(f'#{tc} {result_sum}')



# 2. 좌 우 나눠서 최댓값?
#   for j in range(i-2, i+3): #