T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # print(arr)

    # 오목판정 함수만들기
    # 1. 8방향 델타만들어서 탐색
    # 우측 부터 시계방향으로
    dr = [0, 1, 1, 1, -1, -1, -1, -1]
    dc = [1, 1, 0, -1, 0, -1, 0, 1]

    # 2. 'o'가 연달아서 5개 있는가 확인
    # 3. arr[r][c]가 'o'일때만 탐색
    # 3-1. '.'일 경우 탐색할 필요 없음
    result = 'NO'
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for k in range(8):              # 8방향 탐색
                    cnt = 1                     # 탐색 방향이 바뀌면 돌 몇 개인지 다시 세야되니까 여기에서 초기화
                    for step in range(1,N):     # 범위를 초과하거나, '.'이 나오기 전까지는 한 방향으로 증가하면서 탐색
                        nr = r + dr[k] * step
                        nc = c + dc[k] * step
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 'o':
                                cnt += 1
                            else:   # 돌이 아닐 경우에 대한 조건이 무조건 있어야 하는가? -> 끊어졌다 이어지는 경우는 세면 안되니까 있어야 될듯
                                break
                        else:   # 범위 조건 안맞으면 다음방향으로 넘어가
                            break

                    if cnt >= 5:
                        result = 'YES'
                if result == 'YES':
                    break
        if result == 'YES':
            break
    else:
        result = 'NO'   # 모든 반복이 종료됐는데도 오목 없으면 NO

    # 4. arr[r][c]기 돌'o'이면 *step만큼 탐색
    # 사실 이때의 step 범위를 어떻게 정해야될지 모르겠음. N까지로 두고 범위에 걸리면 정지되게?
    # 예시 테스트케이스가 5x5로 주어져있긴한데 N은 20까지 가능함
    # 5개 이상인지 확인하면 되는거라 돌 기준으로 5개 더 보면 되긴하지만
    # 연속된 돌의 개수를 세야하는 경우라면? 범위를 어떻게?

    # 4-1. 가다가 '.'을 만나거나 범위가 N이상이면 멈추고
    # 4-2. 그때까지 cnt한 연속적인 돌이 몇개인지 판단
    # 5. 5개 이상이면 YES. 하나만이라도 있으면 되기 때문에 더이상 탐색할 필요 없음
    # 6. 다 탐색했는데 5개 이상이 없으면 NO
    print(f'#{tc} {result}')


'''
리뷰
1. 반복문 탈출 여전히 헤매는 중
2. 그래도 어제보다는 조금 더 자세히 생각해서 pass한듯
2-1. 이 부분에서 else조건들이 없으면 불필요한 반복을 하게됨
    if 0 <= nr < N and 0 <= nc < N:
        if arr[nr][nc] == 'o':
            cnt += 1
        else:   # 돌이 아닐 경우에 대한 조건이 무조건 있어야 하는가? -> 끊어졌다 이어지는 경우는 세면 안되니까 있어야 될듯
            break
    else:   # 범위 조건 안맞으면 다음방향으로 넘어가
        break
'''