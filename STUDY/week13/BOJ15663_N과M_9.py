# N개의 자연수 중에서 M개를 고른 수열
# 중복 수열 여러번 출력 X
# 사전 순으로 증가하는 순서로 출력
N, M = map(int, input().split())
lst = list(map(int,input().split()))
# lst = list(set(lst))
lst.sort()

visited = [0] * len(lst)
result = []     # 수열 담을 리스트
def sequence():
    # 기저조건
    if len(result) == M:
        print(*result)
        return

    pre = 0                     # 직전 요소 기억
    for i in range(len(lst)):   # i는 인덱스
        if visited[i] == 0 and pre != lst[i]:    # 방문하지 않았고, 이전에 뽑은 숫자가 아니라면
            result.append(lst[i])
            visited[i] = 1
            pre = lst[i]
            sequence()
            result.pop()
            visited[i] = 0      # 방문표시 원복

sequence()

'''
리뷰
1. 그동안 풀었던 N과 M을 응용해서 풀려고 했는데
1-1. set으로 중복제거후 해도,
1-2. for문 range 조정하거나 재귀호출 부분을 조정해 봐도
1-3. 중복을 없애지 못하거나 1 1, 7 7 이런식으로 나오게 됨
2. 서칭함
2-1. 직전에 뽑은 숫자를 안뽑도록 pre에 저장해주고, 조건식 세우면 됨
'''