'''
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
from collections import deque

def BFS():
    while q:
        now = q.popleft()           # 큐에 담긴 노드 popleft
        print(now)
        for next in graph[now]:
            if not visited[next]:   # 방문하지 않았다면
                q.append(next)      # 큐에 넣고
                visited[next] = 1   # 방문표시


V, E = map(int, input().split())
temp = list(map(int,input().split()))
graph = [[] for _ in range(V+1)]# 빈 인접리스트

for i in range(E):
    v1, v2 = temp[2*i], temp[2*i+1]
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (V+1)

q = deque()
start = 1
q.append(start)
visited[start] = 1
BFS()   # 함수 호출

'''
#1 1 2 3 4 5 7 6
'''