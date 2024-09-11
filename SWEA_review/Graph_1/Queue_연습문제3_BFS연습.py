# import sys
# sys.stdin = open('input.txt','r')
'''
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# BFS 함수 만들기
# 너비 우선 탐색
# 큐의 선입 선출 특징 이용
# adjL = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
from collections import deque
def BFS(node):
    q = deque([node])
    # q = [node]                      # 인자로 받은 노드 q에 삽입
    while q:
        # print(q)
        now = q.popleft()         # 큐에 있는 노드 꺼내기
        # now = q.pop(0)
        print(now, end = ' ')       # 현재 위치 출력
        for next in adjL[now]:
            if visited[next] == 1:  # 방문한 인접노드라면 넘어가
                continue
            visited[next] = 1       # 첫 방문이면 방문표시
            # print(visited)
            q.append(next)
        # print('-----')


# 노드 개수, 간선 수
V, E = map(int,input().split())

# 인접리스트 만들기
adjL = [[]*(V+1) for _ in range(V+1)]

# 방문기록증 만들기
visited = [0]*(V+1)

temp = list(map(int,input().split()))
# 인접리스트 채우기
for i in range(E):  # 간선 수 만큼 반복. input데이터가 그렇게 생김. V+1(노드의 개수+1)해도 상관없을듯?
    # 짝수 인덱스: 부모노드?, 홀수 인덱스: 인접노드
    n1 = temp[2*i]
    n2 = temp[2*i+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
# print(adjL)

start = 1           # 1번 노드에서 시작할거고
visited[start] = 1  # 방문표시하고 시작
print(f'#1', end =' ')
BFS(start)          # 탐색


'''
리뷰
1. 큐, 덱 안써봐서 하나씩 프린트하면서 확인해봄
2. 잘 이해 안돼서 ppt이용해서도 확인해봄
'''