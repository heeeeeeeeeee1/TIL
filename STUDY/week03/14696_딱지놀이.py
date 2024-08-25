# 총 라운드 수
N = int(input())

# 카운팅해서 인덱스에 넣기
def counting(arr):
    COUNTS = [0] * 5    # 숫자 4까지니까. 원소 0은 없어서 0번 인덱스는 안쓰고 1 ~ 4 사용
    for x in arr:       # 배열에서 원소x 가져와서
        COUNTS[x] += 1  # x번째 인덱스에 x 개수 추가
    return COUNTS

for round in range(N):
    A = list(map(int,input().split())) # 첫 숫자는 나머지 숫자들의 개수
    B = list(map(int,input().split()))

    stack_A = A[1:] # 0번째 인덱스 값은 그 라운드의 그림 개수인데 필요 없다고 생각해서 제외
    stack_B = B[1:]

    COUNTS_A = counting(stack_A)
    COUNTS_B = counting(stack_B)

    result = 'D'
    for i in range(4, 0, -1):  # 4 ~ 0 : 값이 큰 것 부터 비교
        if COUNTS_A[i] > COUNTS_B[i]:
            result = 'A'
            break
        elif COUNTS_A[i] < COUNTS_B[i]:
            result = 'B'
            break

    print(result)


