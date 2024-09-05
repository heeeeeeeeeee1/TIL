T = int(input())    # 테스트 케이스
for tc in range(1,T+1):
    N = int(input())    # 격자판 크기
    arr = [list(input()) for _ in range(N)]

    # 1. 행(r) 우선 순회하며 처음으로 '#'나왔을 때의 열(c1) 기억하기
    find = 0
    r1 = c1 = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '#':
                r1 = r
                c1 = c
                find = 1
                break
        if find == 1:
            break
    # print(r1)
    # print(c1)
    # 이미 찾았으면//열 순회만 끝나고 행순회는 계속됨... 어떻게 멈춰 -> 교수님들이 수술해줌
    # r1을 찾았다면 다음 행 순회 하지 않도록

    # 2. 행(r) 우선 순회에서 열을 역순으로 순회할때. 즉, 뒤에서 가장 먼저 '#'이 나왔을 때의 열(c2) 기억하기
    c2 = 0
    for c in range(N-1, -1, -1):
        if arr[r1][c] == '#':
            c2 = c
            break

    # 3. 이 사이 범위만큼 range(c1,c2+1)이 정사각형의 한 변의 길이

    # 4. 이 범위만큼만 행, 열 순회
    # 5. 이 범위 순회 중 중간에 '.'이 나오면 정사각형 아님
    result = 0
    for r in range(r1,r1+c2-c1+1):
        for c in range(c1,c2+1):    # c2까지
            if arr[r][c] == '#':
                result = 1
                arr[r][c] = '.'     # 판단하고 '.' 으로 바꾸면? -> 나중에 전범위 순회했는데 '#'나오면 정사각형 아니겠지
            else:
                result = 0
                break
        if result == 0:
            break


    for r in range(N):
        for c in range(N):
            if arr[r][c] == '#':    # 하나라도 '#' 나오면 정사각형 아니라는 거니까
                result = 0
                break
    # else:   # 다 '.'이라면 정사각형이라는 거니까... 가 아니잖아^^ '.'이 하나라도 나오면 result
    #     result = 1 # 이거쓰면 안되네^^ 생각좀 하고 써라



    if result == 1:
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')

'''
리뷰
1. 문자열인데 생각없이 map(int, -) 사용;
1-1. 와 입력받는 부분 제대로 못했음;; list(input())
2. 전에 어렵게 생각해서 시도만하고 못풀었음
3. 다시 시도했는데 아이디어 생각안나서 주워들은 아이디어 착안함
4. 반복문 탈출 원하는대로 못해.
5. 참거짓 판단하는 True False와 단순 플래그로 사용한 True False...
5-1. if find == True: 안하고 if True: 했었음ㅋ
6. 범위를 잘보자^^;

'''


