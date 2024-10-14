N, M = map(int, input().split())

result = []                     # 출력할 수열 담을 리스트
def back_tracking():
    if len(result) == M:
        print(*result)
        return

    for i in range(1,N+1):
        if i not in result:     # 방문하지 않았다면
            result.append(i)    # 추가
            back_tracking()
            result.pop()        # result에 있는 마지막 숫자 빼줘야 돌아가서 다른 숫자 담지

back_tracking()

'''
리뷰
1. 외운 느낌
'''