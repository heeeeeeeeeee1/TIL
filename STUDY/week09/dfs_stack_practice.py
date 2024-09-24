'''
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def DFS():
    while stack:    # 스택이 차있는 동안
        now = stack.pop()
        print(now)
        for next in graph[now]:
            if not visited[next]:   # 방문하지 않았으면
                stack.append(next)  # 스택에 넣고
                visited[next] = 1   # 방문 표시


V, E = map(int, input().split())
temp = list(map(int, input().split()))
graph = [[] for _ in range(V+1)]    # 빈 인접리스트

for i in range(E):  # 간선 수 만큼 반복
    v1, v2 = temp[2*i], temp[2*i+1]
    graph[v1].append(v2)
    graph[v2].append(v1)
# print(graph)
visited = [0] * (V+1)

# 1. 시작 정점 스택에 넣고, 방문표시
start = 1
stack = [start]
visited[start] = 1

# 2. 함수호출
DFS()


'''
리뷰
1. 이렇게 하면 현재 정점(now)의 자식 정점(next)중에 마지막에 스택에 들어간(우측 정점)이 pop되면서 우측 정점 위주로 깊이 우선 탐색하게 됨
'''