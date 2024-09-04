T = int(input())
for tc in range(1, T+1):
    N,K = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 0  # 행, 열 순회한 결과 하나로 합쳐야 하니까 여기에

    #  행 우선 순회(가로)
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:  # 1이면
                cnt += 1
                if c == N-1 and cnt == K:   # 00111 이런식으로 순회의 끝이 1이라면 c == N-1
                    result += 1             # and cnt값이 단어의 길이와 같다면 result에 1추가
            else:               # 0이면
                if cnt == K:    # 입력받은 K와 같다면
                    result += 1 # 정답 카운트 +1
                    cnt = 0     # K와 같아도 같은 행에서 K와 같은 단어 들어갈 자리가 또 나올 수 있으니까 초기화
                else:
                    cnt = 0     # 같은 행에서 또 1 나올 수 있으니까 초기화
        # if cnt == K:
        #     result += 1       # 여기에서 00111로 끝나는 케이스에 대한 카운트 해도 됨

    #  열 우선 순회(세로)
    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:  # 1이면
                cnt += 1
                if r == N-1 and cnt == K:   # 00111 이런식으로 순회의 끝이 1이라면 c == N-1
                    result += 1             # and cnt값이 단어의 길이와 같다면 result에 1추가
            else:               # 0이면
                if cnt == K:    # 입력받은 K와 같다면
                    result += 1 # 정답 카운트 +1
                    cnt = 0     # K와 같아도 같은 행에서 K와 같은 단어 들어갈 자리가 또 나올 수 있으니까 초기화
                else:
                    cnt = 0     # 같은 행에서 또 1 나올 수 있으니까 초기화

    print(f'#{tc} {result}')

'''
리뷰
1. 또 모르냐
2. arr[r][c] == 1: 하위조건이 없어서 1100111 이렇게 끝나는경우 result 값이 이상했었음
2-1. 수정함. 그런데 이렇게 (행이나 열 인덱스가 범위의 끝과 같다면 이라는 식으로) 조건 걸어주는게 맞는지 확신은 없음
'''