# 전치행렬 만들면 되나

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # 90도 회전
    arr_t90 = []
    for r in range(N):
        temp = []
        for c in range(N-1,-1,-1):
            temp.append(arr[c][r])
        arr_t90.append(temp)
    # print(arr_t90)

    # 90도 회전한거 한번더 회전하면 180도 회전
    arr_t180 = []
    for r in range(N):
        temp = []
        for c in range(N-1,-1,-1):
            temp.append(arr_t90[c][r])
        arr_t180.append(temp)
    # print(arr_t180)   # [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


    # 270도 회전과 동일
    arr_t270 = []
    for r in range(N-1,-1,-1):
        temp = []
        for c in range(N):
            temp.append(arr[c][r])
        arr_t270.append(temp)
    # print(arr_t270)    # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

    print(f'#{tc}')
    # 정답 출력형태 만들기
    for i in range(N):
        result = []
        result.append(arr_t90[i])
        result.append(arr_t180[i])
        result.append(arr_t270[i])

        # 출력형태 맞추기 2
        for x in range(3):  # 3가지 각도니까
            a = result[x]
            # new = []
            # for y in range(len(a)):
            #     b = str(a[y])   # str로 변환
            #     new.append(b)

            print(''.join(map(str,a)), end=' ') # 그냥 이렇게 하면 되는거였다. a를 *a(언패킹)하려고 했었다..
        print()

        # 출력형태 맞추기 1
        # for x in range(3):  # 3가지 각도니까
        #     a = result[x]
        #     new = []
        #     for y in range(len(a)):
        #         b = str(a[y])   # str로 변환
        #         new.append(b)
        #
        #     print(''.join(new), end=' ')
        # print()
'''
리뷰
1. 으 몰라 회전하려고 생각했다기 보다 출력형태 보고 맞추려고 한 느낌
2. 테스트 케이스 하나로만 돌려보다가 그냥 냄;
3. output 형태 안맞추고 그냥 내서 fail
4. join, map 쓸 줄 몰라서 출력형식 맞추는데 헤맴
'''


# arr_t = []
# for r in range(N):
#     temp = []
#     for c in range(N):
#         temp.append(arr[c][r])
#     arr_t.append(temp)

# print(arr_t)    # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]