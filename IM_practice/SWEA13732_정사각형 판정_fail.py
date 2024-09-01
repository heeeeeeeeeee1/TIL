
T = int(input())
for tc in range(1,T+1):
    N = int(input())    # 격자판 크기
    arr = [list(input()) for _ in range(N)] # [['.', '.', '.'], ['.', '#', '#'], ['.', '#', '#']]


    # 행, 열 좌표 카운팅할 배열 만들기
    row_check = [0] * N
    col_check = [0] * N


    # 순회하면서 '#'카운팅 배열에 입력
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '#':    # '#'이라면 그 위치를...음.. 이떄의r,c일까
                row_check[r] += 1
                col_check[c] += 1
            # else:   # '.'일때 조건이 따로 필요한가?

    # 조건1
    for i in range(N):
        if row_check[i] == col_check[i]:    # 아 다 같으면 안되겠네. 아닌경우도 있ㄴ
            # 일단 같아야 하고
            r_check = row_check[i]
            c_check = row_check[i]
            # 조건2
            if r_check == row_check.count(r_check) and c_check == col_check.count(c_check):
                result = 'yes'
            else:
                result = 'no'

    print(f'#{tc} {result}')



