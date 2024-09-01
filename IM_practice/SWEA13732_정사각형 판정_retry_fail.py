# 연속된 '#'의 개수를 cnt
# 연속되지 않고 #이 1로 cnt 되는 순간 정사각형이 아니게 되므로 더 이상 순회할 필요 없음
# '#'를 카운팅 후 기억하고 있어야함 -> 저장 리스트 만들자
# 1. 각 행, 열 마다 연속된 '#' 카운팅해서 저장하기
# 체크리스트 확인 함수
def check(lst):  # 행열 체크리스트
    check_cnt = 0
    max_val = max(lst)  # 아무 숫자나 기준 잡은거임
    for i in range(N):
        if i != 0:
            if row_check[i] == max_val:
                check_cnt += 1
                if i == N-1:
                    break
            else: # 값이 다른데(보통 0일거고, 0아닐수도)
                if check_cnt == 0:
                    continue
                else:
                    break  # 연달아서 같은 수 없으면 멈춰도 되지 ->  아니 안되잖아..0일 수도 있는데

    if check_cnt == max_val:  # 다 순회하고 같으면
        return 'yes'
    else:
        return 'no'


T = int(input())    # 테스트 케이스
for tc in range(1,T+1):
    N = int(input())    # N x N
    arr = [list(input()) for _ in range(N)] # 문자열 배열
    # print(arr) # [['.', '.', '.'], ['.', '#', '#'], ['.', '#', '#']]

    # 카운팅해서 저장할 리스트
    row_check = [0] * N # 하 왜N-1이라고 생각했었지?
    col_check = [0] * N

    # 연속된 '#' 카운팅

    # while True:
    #     if arr[r][c] == '#':
    # 습,,, for문으로 해야될것같은데?


    # 1. 행 우선순회
    for r in range(N):
        cnt = 0 # 행(r)이 바뀌면 초기화
        for c in range(N):
            if arr[r][c] == '#':    # '#'이라면
                cnt += 1            # cnt를 check리스트에 저장해야되네
                # 연속된거 세야됨
                # 아 '.'으로 안끝나고 '#'로 끝나는 경우 체크리스트에 안담김...
                if c == N-1:    # '#'으로 끝났을때(더이상 순회할 값이 없으면) 여기서 저장
                    row_check[r] = cnt
            else:                   # 아닌 경우('.'라면)
                if cnt == 0:        # '#'을 아직 못찾았다면
                    continue        # 계속 순회
                else:               # '#'찾았는데 이어서 '.' 만난 경우이면 그만 순회. 그동안 카운팅한 cnt를 리스트에 저장
                    row_check[r] = cnt   # 그만 순회하고 그 행을 인덱스로 한 row_check 리스트에 저장.어차피 0번부터 순서대로 저장될듯
                    break   # 사실 더 돌필요 없..?이 아니라 나중에 이어질수도 있나...?
                    # 근데 끊겼다가 다시 # 되는 경우는 이문제 조건에 안맞는거 아닌가? 하나의 정사각형 만들어야 되니까?
                    # 그리고 1이 나오는 순간 행 순회고 열 순회고 더 순회할 필요도 없을듯 이미 정사각형 아닌거여서
                    # break하면 안되네 중간에 ..##.이런식으로 나올수도 있어서
    print(row_check)

    # 2. 열 우선순회
    for c in range(N):
        cnt = 0 # 열(c)이 바뀌면 초기화
        for r in range(N):
            if arr[r][c] == '#':    # '#'이라면
                cnt += 1            # cnt를 check리스트에 저장해야되네
                if r == N-1:
                    col_check[c] = cnt  # 악
                # 연속된거 세야됨
            else:                   # 아닌 경우('.'라면)
                if cnt == 0:        # '#'을 아직 못찾았다면
                    continue        # 계속 순회
                else:               # '#'찾았는데 이어서 '.' 만난 경우이면 그만 순회. 그동안 카운팅한 cnt를 리스트에 저장
                    col_check[c] = cnt   # 그만 순회하고 그 행을 인덱스로 한 row_check 리스트에 저장
                    break
    print(col_check)


    if check(row_check) == 'yes' and check(col_check) == 'yes':
        result = 'yes'
    else:
        result = 'no'


    print(f'#{tc} {result}')





    # 체크리스트 확인
    # for i in range(N):
    #     side1 = row_check[i]
    #     side2 = col_check[i]
    #     if side1 != 0 and side2 != 0:
    #         if row_check[i] == col_check[i] and side1 == row_check.count(side1) and side2 == col_check.count(side2):
    #             result = 'yes'  # 숫자0인 경우(cnt가 0인경우) False로 따지나? 0인 경우가 여러개일수도 있자나...0이 0개가 아닐수도ㅋ
    #         else:
    #             result = 'no'
    #             # and 조건으로 이어서 사용하는거랑 하위 조건으로 쓰는거랑 무슨 차이인가...단축?



'''
리뷰
1. append는 리스트의 끝에 추가된다. # 카운팅한 cnt append로 체크리스트에 추가하려고 했더니 인덱스 안맞음


'''