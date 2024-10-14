N, M = map(int, input().split())

result = []
def back_tracking(num):
    if len(result) == M:    # 기저조건
        print(*result)
        return

# 중복 제거 어떻게 하지?

    for i in range(num,N+1):  # 1부터 N까지 자연수 중에서 중복 없이 M개 고르기
        if i not in result:
            result.append(i)
            back_tracking(i+1)
            result.pop()

back_tracking(1)


'''
리뷰
1. 코드 찍고 봤더니 순열 되어버림(N과 M시리즈 1번?)
1-1. 어떻게 중복 제거 하지?
1-2. 매개변수/인자에 아무것도 없이 함수 호출하다보니까 계속 1부터 시작 -> 모든 경우 다 구함

# 길이가 M인 수열 구하기
def back_tracking():
    if len(result) == M:    # 기저조건
        print(*result)
        return

    for i in range(1,N+1):  # 1부터 N까지 자연수 중에서 중복 없이 M개 고르기
        if i not in result:
            result.append(i)
            back_tracking()
            result.pop()

back_tracking()

2. 그래서 흘깃 서칭해봤더니 for문을 1부터 시작안하면 되는 것이었다^.^
2-1. back_tracking(i+1)식으로 재귀호출하면 [2,1] 이런식의 조합은 안생김. 바로 [2,3]부터 시작
'''