T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    # print(numbers)

    # sort() 사용하면 원본 수정됨
    # 오름차순 정렬
    numbers.sort()
    # print(numbers)

    # 결과 담을 리스트
    result = [0] * N

    # 입력받은, 정렬된 리스트의 1 ~ N//2까지는 result의 홀수 인덱스에 순서대로 넣고
    # N//2 ~ N-1까지는 짝수인덱스에 역순으로 넣는다.
    num1 = numbers[:N//2]
    # print(num1)
    num2 = numbers[N//2:]
    for i in range(len(num1)):
        result[2*i+1] = num1[i]

    num2.sort(reverse=True)
    # print(num2)
    for j in range(len(num2)):
        result[2*j] = num2[j]

    print(f'#{tc}',end=' ')
    # 문제를 잘읽자^^ 10개까지만 출력이다
    for r in range(10):
        print(result[r],end=' ')
    print()
    # print(f'#{tc}', *result)

'''
리뷰
1. 원본에서 정렬할 수 있는 방법이 있을 것 같은데 더 혼란해지기만 해서
1-1. 속편하게 다 슬라이싱하고, 결과 받을 리스트 따로 만들었다
2. 출력 10개까지만 하는건데 제대로 안읽어서 10개중 7개만 맞음^^;
'''