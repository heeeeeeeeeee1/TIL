# 빙고 확인 함수 만들기
# 가로, 세로, 대각/, 대각\의 합이 0인 줄이 몇개인지 확인
# 3줄이상이면 빙고
def is_bingo(arr,N):
    cnt = 0
    # 행방향 빙고 확인
    for lst in arr:
        if sum(lst) == 0:
            cnt += 1

    # 열방향 빙고 확인
    for c in range(N):
        c_total = 0
        for r in range(N):
            c_total += arr[r][c]
        if c_total == 0:
            cnt += 1

    # 대각\ 빙고 확인
    cross_total1 = 0
    for r in range(N):
        cross_total1 += arr[r][r]
    if cross_total1 == 0:
        cnt += 1

    #  대각/ 빙고 확인
    cross_total2 = 0
    for r in range(N):
        cross_total2 += arr[r][N-1-r]
    if cross_total2 == 0:
        cnt += 1

    return cnt


N = 5
# 철수 빙고판
cheolsu = [list(map(int,input().split())) for _ in range(N)]

# 사회자가 부르는 번호(1차원 리스트)
call_num = []
for _ in range(N):
    call_num += list(map(int, input().split()))
# print(call_num)

# 철수 빙고판에서 사회자가 불러주는 번호를 찾아 0으로 만들기
# result = 0

result = 0  # 몇번째 수를 불렀을때인지
bingo = 0
for num in call_num:
    result += 1
    for r in range(N):
        for c in range(N):
            if cheolsu[r][c] == num:    # 사회자가 부른 번호와 일치한 철수의 빙고판 숫자를
                cheolsu[r][c] = 0       # 0으로 만들기
                if is_bingo(cheolsu,N) >= 3:   # 사회자가 번호 부를때 마다 빙고인지 확인 ->  몇줄 선 그어 졌는지 반환
                    bingo = 1
                    print(result)
                    break
        if bingo == 1:
            break
    if bingo == 1:
        break


'''
리뷰
1. if is_bingo(cheolsu,N) >= 3:  으로하면 num이 18 나온다.
1-1. for num in call_num: 이부분이 안쪽에 있어서 밖으로 뺌
2. 이제 25가 나온다;
3. 아잇ㅡㅡ문제 제대로 안보냐
3-1. 몇 번을 불렀을 때가 아니라 몇 번째 수를 불렀을때인지 구하는거잖아 ㅡㅡ
'''