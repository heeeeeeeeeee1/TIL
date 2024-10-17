# 1. 그래프 그리기
# 2. 탐색
# 2-1.

def dfs(now):
    visited[now] = 1          # 방문표시
    print(f"Visit {now}")
    for next in graph[now]:
        if not visited[next]: # 방문하지 않았다면
            dfs(next)         # 재귀 호출

computers = int(input())    # 노드 수
links = int(input())        # 간선 수
graph = [[] for _ in range(computers+1)]    # 인접리스트
visited = [0] * (computers+1)               # 인덱스 0번은 사용 안함

# 인접리스트 채우기
for _ in range(links):
    c1, c2 = map(int,input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)    # 양방향
# print(graph)  # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

start = 1
dfs(start)
print(sum(visited)-1)   # 시작노드에 대해 방문처리한 값을 빼줘야 감염된 컴퓨터 수 나옴

'''
리뷰
1. dfs 재귀 기본 구조로 풀면되는데 그 사이에 잊어버렸다;
2. 바이러스에 감염되는 컴퓨터의 수를 bfs 최단거리 구하는 것처럼 하려고 했는데
2-1. dfs로 하려니... 안되는듯?
3. 그렇다면 탐색 종료 후 visited의 합을 구하면 되겠네?
3-1. 시작노드를 방문처리 하면 출력값이 1 크게 나오게 되어서 아래와 같이 하면 안될까 했는데
def dfs(now):
    for next in graph[now]:
        if not visited[next]: # 방문하지 않았다면
            visited[next] = 1  # 방문표시
            dfs(next)         # 재귀 호출
3-2. 이렇게 하면 방문처리를 재귀 호출전에 미리 해서 안됨
3-3. 아직 탐색되지 않은 노드인데 방문했다고 간주됨 -> 재귀호출 후에 방문처리 하는 것으로 수정함.

'''
