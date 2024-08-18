# 1. 4방향 델타 만들기
# 2. 한 방향으로 'o'가 5개 연속으로 있는지 확인
# 3. 모든 좌표 순회
# 5목인지 확인하는 함수
def solve():
    for r in range(N):
        for c in range(N):  # 모든 좌표 순회
            for dr, dc in [[0, 1], [1, 1], [1, 0], [1, -1]]:  # 우, \ 우측 아래 대각, 하, / 좌측 하단 대각
                for mul in range(5):  # 5목이니까 5. 시작점 포함 위치 검사
                    nr = r + dr * mul  # next row
                    nc = c + dc * mul  # next column
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':  # 범위 내에 있고 arr배열에 돌 있으면
                        pass  # 성공(돌 있으면 같은 방향의 옆칸(*mul)도 검사)
                    else:
                        break  # 실패(반복문 탈출)
                else:
                    return 'YES'  # 돌 5개(arr[r][c]:내위치 포함) 있으면 YES
    return 'NO'  # 다 순회했는데 해당안되면 NO


T = int(input())        # 테스트 케이스
for tc in range(1, T+1):
    N = int(input())    # N x N 배열
    arr = [input() for _ in range(N)]

    result = solve()    # 함수 호출
    print(f'#{tc} {result}')

'''
리뷰
1. 다중 루프를 탈출하기 위해서는 flag를 이용하는 것보다 함수화 하는 것이 더 편하다고 한다.
2. 같은 문제여도 다른 방법으로 코딩하면 또 헷갈리는 반복문, 조건문 ㅋ
'''