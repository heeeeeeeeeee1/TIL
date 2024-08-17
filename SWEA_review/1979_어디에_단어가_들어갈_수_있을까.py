# 2차원 배열에서 연속된 1(흰색부분)의 길이가 K일때 카운팅
# 흰색부분 1, 검은색 부분 0
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N: 가로 세로 길이, K: 단어의 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]    # 2차원 배열

    # 행 방향 순회
    result = 0  # K가 들어갈 수 있는 자리수
    for r in range(N):
        cnt = 0  # 연속된 1의 길이. 행 기준으로 열 순회를 마쳤다면(가로로 한 줄 순회 끝났다면) 초기화
        for c in range(N):
            if puzzle[r][c] == 1:
                cnt += 1         # 1 증가
            else:                # 0이고
                if cnt == K:     # 앞에서 카운팅한 1이 K와 같으면
                    result += 1  # K 들어갈 수 있는 자리수 카운팅 + 1
                cnt = 0          # 이후로 1이 이어질 수 있으니까 초기화
        if cnt == K:             # 행을 순회했을 때 1이 K 길이면서, 0으로 끝나지 않고 1로 끝난 경우
            result += 1          # 첫 조건문에서 카운팅 되지 않았으므로 여기서 + 1

    # 열 방향 순회
    for c in range(N):
        cnt = 0                  # 연속된 1의 길이. 열 기준으로 행 순회를 마쳤다면(세로로 한 줄 순회 끝났다면) 초기화
        for r in range(N):
            if puzzle[r][c] == 1:
                cnt += 1         # 1 증가
            else:                # 0이고
                if cnt == K:     # 앞에서 카운팅한 1이 K와 같으면
                    result += 1  # K 들어갈 수 있는 자리수 카운팅 + 1
                cnt = 0          # 이후로 1이 이어질 수 있으니까 초기화
        if cnt == K:             # 열을 순회했을 때 1이 K 길이면서, 0으로 끝나지 않고 1로 끝난 경우
            result += 1          # 첫 조건문에서 카운팅 되지 않았으므로 여기서 + 1

    print(f'#{tc} {result}')

    '''
    리뷰
    1. 처음에 리스트 한줄씩 입력받고 순회하는 방법으로 하려다가 막힘 => 다른 사람들 코드 참고해서 2차원 배열로 함.
    2. 여전히 헷갈리는 cnt, result 초기화 위치
    3. 마지막 조건문(1로 종료되었을 경우 카운팅 하기) 고려 못했음
    '''

