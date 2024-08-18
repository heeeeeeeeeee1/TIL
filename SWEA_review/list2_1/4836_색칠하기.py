T = int(input())          # 테스트 케이스
for tc in range(1, T+1):
    N = int(input())      # N개의 영역

    # 빈 도화지
    arr = [[0]*10 for _ in range(10)]

    # 색칠할 범위, 색
    for n in range(N):                  # N개의 영역에 칠하기
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):       # +1 안해도 되나? => 해야되네
            for c in range(c1, c2+1):
                arr[r][c] += color      # 입력받은 색으로 칠하기(빨강 1, 파랑 2)

    # 보라색(3) 칸 수 구하기1
    result = 0
    # for r in range(10):
    #     for c in range(10):
    #         if arr[r][c] == 3:
    #             result += 1

    # 보라색 칸 수 구하기2(count 메서드로 카운팅)
    for lst in arr:
        result += lst.count(3)

    print(f'#{tc} {result}')

'''
리뷰
1. 백준 10163 색종이랑 비슷한 문제. 백준에서는 색칠할때 범위 +1 해주지 않아도 됐던 것 같은데 무슨 차이지?
1-1. 백준문제는 좌표로 범위를 준 것이 아니라 끝 좌표랑 너비, 높이로 줘서 그런가보다
'''