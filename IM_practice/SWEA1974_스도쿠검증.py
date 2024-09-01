# 행 순회하면서 count
# 열 순회하면서 count
# count 함수 쓸거면 전치행렬로 만들어야 할듯?
# 그 범위 안에 1 ~ 9 각 숫자 하나씩 있어야 함
# count 쓸거니까 리스트로 가져오자
def check_row(arr):
    for lst in arr: # 한줄 가져옴
        for i in range(1, 10):   # 1부터 9 있는지 확인
            if lst.count(i) != 1: # 하나라도 아니면
                return 0
                break
            # break
    return 1


def check_col(arr):
    arr_t = []  # 전치행렬 생성
    for r in range(9):
        temp = []
        for c in range(9):
            temp.append(arr[c][r])
        arr_t.append(temp)

    for lst_t in arr_t:
        for j in range(1,10):   # 1~9까지 숫자 있는지
            if lst_t.count(j) != 1: # 없거나 1개가 아니라면
                return 0
                break   # 더 볼 것도 없지

    # else:   # 반복문 다 돌아서 1 ~ 9까지가 1개씩만 있다면
    #     result_2 = 1
    return 1


def three_three(arr):
    for r in range(0,6,3):
        for c in range(0,6,3):
            slice_arr = arr[r:r+3]  # 이렇게 가져오면 값 하나로 가져오는거 아닌가 리스트 필요한데
            slice_arr2 = []
            for s in slice_arr:
                slice_arr2.append(s[c:c+3]) # 3x3 배열로 가공

            cnt = [0]*10
            for a in range(3):
                for b in range(3):
                    num = slice_arr2[a][b]
                    cnt[num] += 1

            for u in range(1,10):
                if cnt[u] != 1:
                    result_3 = 0
                    break
            else:   # cnt정렬에 있는 값이
                result_3 = 1

    return result_3


T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]    # 9 x 9배열

    # 행, 열, 3x3순회했을때 모두 조건 충족하면 1
    r1 = check_row(arr)
    r2 = check_col(arr)
    r3 = three_three(arr)

    if r1 == 1 and r2 == 1 and r3 == 1:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
'''
리뷰
1. ㅎ ㅏ... 또 범위 잘못쓰고 조건문 못써서 몇시간을 붙잡고 있었네^^?
'''

# zip으로도 못하지만 zip 안쓰고 전치행렬 만들기
# 생각안나서 예시 만들어서 전치행렬 만들어보기
# a = [[1,2,3],[4,5,6]]
# arr_t = []
# for r in range(3):
#     temp = []
#     for c in range(2):
#         temp.append(a[c][r])
#
#     arr_t.append(temp)
# print(arr_t)


        # if r >= 9 and c >= 9:
        #     break

        # for lst_33 in target:   # 이게 되나
        #     # 이 안에 1~9 숫자 1번씩 있는지 확인
        #     for k in range(1, 10):
        #         if lst_33.count(k) == 1:
        #             continue
        #         else:  # 없거나 1개가 아니라면
        #             result_3 = 0
        #             break  # 더 볼 것도 없지
        #     else:  # 반복문 다 돌아서 1 ~ 9까지가 1개씩만 있다면
        #         result_3 = 1
        # r, c = r+3, c+3
        # if r >= 9 and c >= 9:
        #     break

# cnt = [0] * 10
# for a in range(3):
#     for b in range(3):
#         for x in range(1, 10):
#             if slice_arr2[a][b] == x: # 1~9라면
#                 cnt[x] += 1

# 3 x 3 다 돌았는데
# for v in range(1, 10):
#     if cnt[v] != 1:
#         result = 0
#     else:
#         result = 1