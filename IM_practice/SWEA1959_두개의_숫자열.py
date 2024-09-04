T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A,B 중 뭐가 더 긴지 확인
    A_len = len(A)
    B_len = len(B)

    # 같을 때는?
    if A_len >= B_len:
        long = A    # 길이에 따른 변수명 변환
        short = B
    else:
        long = B
        short = A

    # 긴 배열을 짧은 배열 길이만큼 잘라서 비교
    max_val = []    # 어차피 20개니까
    for l in range(len(long)-len(short)+1):  # long에서 가져오자
        split = long[l:l+N] # 끝까지 나눠지네
        split_sum = 0
        for s in range(len(short)):
            split_sum += (split[s] * short[s])
        max_val.append(split_sum)

    result = max(max_val)

    print(f'#{tc} {result}')

'''
리뷰
1. 짧은 배열 만큼 긴 배열을 순회하자고 했는데 범위를 N, M으로 사용했다가
1-1. 이렇게 하면 처음에 배열을 long, short로 나눈거랑 안맞아서 len 사용해서 수정
'''