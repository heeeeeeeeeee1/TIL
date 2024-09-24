'''
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def DFS(now):
    visited[now] = 1           # 방문 표시
    print(now)
    for next in graph[now]:
        if not visited[next]:  # 인접 정점이 방문표시 되어 있지 않다면
            DFS(next)          # 재귀 호출


V, E = map(int, input().split())    # V: 정점, E: 간선

# 빈 인접리스트 만들기
graph = [[] for _ in range(V+1)]
temp = list(map(int, input().split()))
for i in range(E):  # 간선수 만큼 반복해야 인접리스트를 채우겠지?
    v1, v2 = temp[2*i], temp[2*i+1]
    graph[v1].append(v2)
    graph[v2].append(v1)
# print(graph)

visited = [0]*(V+1)

start = 1       # 시작 정점
stack = [start] # 시작정점 스택에 넣기
# 시작 정점 방문 표시 안해도 되지 않나?
DFS(start)