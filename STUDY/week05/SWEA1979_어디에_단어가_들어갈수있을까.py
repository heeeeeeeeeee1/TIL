# N x N 크기의 단어 퍼즐 모양에서 특정 길이 K 갖는 단어가 들어갈 수 있는 자리의 수
# 1.
T = int(input())    # 테스트 케이스
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N x N, K: 단어의 길이
    arr = [list(map(int,input().split())) for _ in range(N)]    # 흰색 1, 검은색 0

    # 가로공간 중에 1이면 cnt+1(연속된 1 개수 세기)
    # 연속된 1이 K 길이만큼 일때(K 넘으면 안됨)
    result = 0  # K가 몇개인지
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:  # 배열의 값이 1이면
                cnt += 1        # cnt 증가. cnt가 K면 stop..할수가없네, 0나와서 끊겨야되네
            else:               # 0이면
                if cnt == K:    # 이전까지 카운팅한 1이 K랑 같은지 확인
                    result += 1 # 같으면 result +1
                    cnt = 0

                # 다르면 딱히 뭐 할거 없지 않나, 계속 순회하면되지
                else:
                    cnt = 0     # 다시 1로 시작할 수도 있으니까 cnt 초기화
        # 반복문 1회 끝나면(== 한 행 순회 끝나면) 뭐해야되지
        # 아 다시 1로 시작했다가 0 안만나서 안 끊기네
        else:
            if cnt == K:
                result += 1

    # 세로공간 중에 연속된 1이 K 길이만큼 일때
    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
            else:   # 0이면
                if cnt == K:
                    result += 1
                    cnt = 0
                else:
                    cnt = 0
        else:
            if cnt == K:
                result += 1

    print(f'#{tc} {result}')