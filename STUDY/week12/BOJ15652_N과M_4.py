N, M = map(int, input().split())

result = [] # 수열 담을 리스트
def back_tracking(num):
    if len(result) == M:    # 1부터 N까지 자연수 중에서 M개 골랐다면
        print(*result)      # 수열 출력
        return

    for i in range(num,N+1):
        # 같아도 되니까 not in 조건은 없어도 되겠네?
        # i로 재귀 호출하면 3 2 1 이런식으로 작아지지도 않겠네? -> 비내림차순 가능
        result.append(i)
        back_tracking(i)
        result.pop()

back_tracking(1)

'''
리뷰
1. 앞에서 푼 N과 M 시리즈 응용했더니 출력값 나옴
'''