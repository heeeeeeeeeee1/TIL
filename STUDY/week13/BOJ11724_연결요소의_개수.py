import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline  # 입력 속도 개선

def dfs(now):
    visited[now] = 1
    for next in graph[now]:
        if not visited[next]:
            dfs(next)

# -------------------------------------------------------
N, M = map(int, input().split())    # N: 정점, M: 간선
graph = [[] for _ in range(N+1)]    # 빈 인접리스트
visited = [0] * (N+1)

# 그래프 그리기
for _ in range(M):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 이 부분이 잘 이해안됐음
cnt = 0
for i in range(1,N+1):  # 1 ~ N번 정점 순회
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)

'''
리뷰
1. 탐색한 후 '카운트 증가하는 문제 유형'에 대해 이해를 명확히 하지 못한 것 같다.
2. dfs 탐색할 때 in not visited 조건은 연결된 요소인지 확인하기 위함이고
2-1. cnt 구하기 위한  if not visited 조건은 새로운 탐색 시작을 위한
2-2. 즉, 연결된 요소이면 한번만 카운트 해야하는데 if not visited가 없으면 방문 처리 한 요소도 탐색하게 됨 => cnt 더 셈
3. 재귀 호출 깊이 지정하기...
4. 이 부분 없어서 계속 런타임 오류, 시간초과
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline  # 입력 속도 개선
'''