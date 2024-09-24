from collections import deque

def dfs(now):
  visited[now] = 1  # 현재정점 방문처리
  # print(now, end=' ')
  result_dfs.append(now)
  for next in sorted(graph[now]): # 현재정점 인접노드가
    if not visited[next]:
      visited[next] = 1
      dfs(next)

def bfs(now):
  while q: # 큐가 빌때까지
    now = q.popleft()
    # print(now, end=' ')
    result_bfs.append(now)
    for next in sorted(graph[now]):
      if not visited2[next]:# 방문하지 안않았다면
        q.append(next)    # 전부 큐에 넣고
        visited2[next] = 1 # 방문표시


N, M, V = map(int, input().split())# 정점, 간선, 시작정점
# 빈 인접리스트
graph = [[] for _ in range(N+1)]
for _ in range(M): # 간선 수만큼 반복
  n1, n2 = map(int,input().split())
  graph[n1].append(n2)
  graph[n2].append(n1) # 양방향이니까

visited = [0] * (N+1)
visited2 = [0] * (N+1)


stack = [V] # 시작정점
q = deque([V])

visited2[V] = 1

result_dfs = []
dfs(V)

result_bfs = []
bfs(V)

print(*result_dfs)
print(*result_bfs)


'''
리뷰
1. 귀가하면서 폰으로 했더니 디버깅이 불가능해서 그냥 제출했는데 런타임에러이거나 틀림
1-1. popleft 앞에 q.를 안붙여서 런타임에러..ㅋㅋ
1-2. visited 두개 안만들어서 출력형태 달랐음
2. 두번째 테스트케이스만 출력 안나와서 당황스러웠는데
2-1. 3번이 시작점이고, 인접정점이 여러개일 경우 작은것부터 라는 문제 조건...
2-3. => graph[now]가 리스트니까 sorted해서 작은 것부터 탐색! 순수 내 아이디어라기보단 최근에 어디선가 본 기억이 남아있어서 쓸 수 있었던 것 같다.
'''