T = int(input())
for tc in range(1,T+1):
    N = int(input())    # 곱해질 값

    count = [0] * 10    # 0 ~ 9 숫자 있는지 셀거니까

    # 근데 이러면 나중에 길이로 0 ~ 9 있는지 확인 못하겠는데?

    k = 1
    while True:
        temp = list(str(k * N))

        num = []
        for t in temp:  # 인덱스로 사용할거니까 다시 정수로 변환
            num.append(int(t))
        # print(num)  # [1, 2, 9, 5]
        # num = list(set(num)) ?? 아니 할필요없는데

        # 변환한 숫자를 count의 인덱스로 이용해서 저장
        for i in num:
            count[i] += 1
        # print(count)

        cnt = 0
        for c in range(len(count)):
            if count[c] != 0:       # 아니 왜 count로 했냐 인덱스로 써야되는데
                cnt += 1


        if cnt == 10:   # 0이 아닌것이 10개라면 0 ~ 9까지 다 있는거
            break
        else:
            k += 1

    print(f'#{tc} {k*N}')


'''
리뷰
1. 디버깅에 손이 안간다
2. 2시간동안 못풀었음^^;
2-1. 알고보니 print(f'#{tc} {k*N}')로 안하고 print(f'#{tc} {k}')로 해서 틀렸음^^;
2-2. 문해력 이슈
'''