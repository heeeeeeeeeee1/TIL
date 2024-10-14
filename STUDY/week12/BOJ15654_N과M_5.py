N, M = map(int, input().split())
nodes = list(map(int,input().split()))
nodes.sort()    # 사전 순으로 증가하는 순서로 출력해야하니까 오름차순 정렬 후 탐색 시작

result = []
def back_tracking():
    if len(result) == M:
        print(*result)
        return

    for i in nodes:
        if i not in result:
            result.append(i)
            back_tracking()
            result.pop()        # 수열의 길이가 M이면 제일 끝 숫자 빼고 다른 가지 탐색해서 넣어야지

back_tracking()

'''
리뷰
1. 틀을 외운느낌?
'''