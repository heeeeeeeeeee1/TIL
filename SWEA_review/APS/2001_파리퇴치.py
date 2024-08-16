# 1. M x M 사이즈의 파리채 범위 순회하며 누적합산하기
# 2. 순회하며 누적합계 최댓값 갱신

# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    # N x N 영역에서 M x M 파리채로 파리 죽이기
    N, M = map(int, input().split())

    # N x N 배열(파리 수 입력)
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_dead = 0                                    # 죽은 파리 최댓값 초기값 설정
    for r in range(N-M+1):                          # N-M까지 순회(파리채 전체가 순회할 범위)
        for c in range(N-M+1):
            dead_flies = 0                          # 죽은 파리 합계 초기화
            for mr in range(r, M+r):                # M x M 파리채 범위 순회
                for mc in range(c, M+c):            # mr: m의 row, mc: m의 column
                    dead_flies += arr[mr][mc]       # 죽은 파리 더하기

            if max_dead < dead_flies:               # 방금 범위의 파리들이 제일 많이 죽은 것이라면
                max_dead = dead_flies               # 최댓값 갱신

    # 최대한 많은 파리 죽이기
    print(f'#{tc} {max_dead}')
