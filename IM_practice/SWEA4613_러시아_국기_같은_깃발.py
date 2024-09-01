# 모든 색의 줄이 최소 1개 이상 있다.
# 러시아 국기니까 0행은 무조건 W다.
# N-1행은 무조건 R다.
# B(파랑)인 줄은 그 사이 어느 행에서 최소 1행 있어야한다.
# 각 행에서 W, R, B 카운팅 후 가장 많은 색으로 나머지를 다시 색칠하는게 최솟값 아닐까
# 그런데 이렇게 하면 흰색줄이 몇줄인지 빨강이 몇줄인지,


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split()) # N행 M열
    arr = [list(input()) for _ in range(N)] # 리스트 안에 문자열 ['WRWRW', 'BWRWB', 'WRWRW', 'RWBWR']
    # print(arr)

    mx = 0
    for i in range(N-2):            # 흰색, 파란색, 빨간색 영역을 나누는 두 개의 경계선(i와 j)의 위치를 결정하는 이중 반복문
        for j in range(i+1, N-1):
            cnt = 0                 # 현재 경계선 조합에 대한 일치 개수를 저장할 변수 cnt를 초기화
            for s in range(i+1):    # 첫 번째 경계선(i) 이전까지의 행에서 흰색('W')의 개수를 세어 cnt에 더함
                cnt += arr[s].count('W')
            for s in range(i+1, j+1):   # 첫 번째 경계선(i)과 두 번째 경계선(j) 사이의 행에서 파란색('B')의 개수를 세어 cnt에 더합
                cnt += arr[s].count('B')
            for s in range(j+1, N):
                cnt += arr[s].count('R')    # 두 번째 경계선(j) 이후의 행에서 빨간색('R')의 개수를 세어 cnt에 더합

            mx = max(mx, cnt)   # 현재 경계선 조합에 대한 일치 개수(cnt)와 기존의 최대 일치 개수(mx)  중 큰 값을 mx에 저장
    print(f'#{tc} {N*M-mx}')

'''
리뷰

'''
#
# cnt_r, cnt_b, cnt_w = 0, 0, 0
# for lst in arr:
#     for i in range(len(lst)):
#         if lst[i] == 'R':
#             cnt_r += 1
#         elif lst[i] == 'B':
#             cnt_b += 1
#         elif lst[i] == 'W':
#             cnt_w += 1
#
# print(cnt_r)