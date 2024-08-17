# 복잡하게 생각하지 않기로 했다. 유사문제 SWEA에서 풀었음 ㅋ.ㅋ.. => 근데 왜 안되냐 ㅋ

# 테스트 케이스 주어지지 않았을 때 반복적으로 입력 받아오는 법?
# for _ in range(4): # 그냥 테스트 케이스 개수 직접 입력?


while True:
    pal = input() # 문자열로 입력
    if pal == '0':
        break
    elif pal == pal[::-1]: # 문자열로 받아와야 가능
        result = 'yes'
    else:
        result = 'no'
    print(result)

    # for i in range(n): # n은 입력받은 값의 길이, i는 인덱스
    #     mid = n // 2
    #     if pal[mid]:
    #         continue
    #     elif pal[i] == pal[-2 * i - 1]:
    #         result = 'yes'
    #     else:
    #         result = 'no'
    #
    #     print(result)
    #
    #
    #
