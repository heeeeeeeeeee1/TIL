# import sys
# sys.stdin = open('input.txt','r')
# 깊이 우선 탐색
# adjL = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
nodes = []
def DFS(node):
    nodes.append(str(node))      # 일단 현재위치 출력
    for next in adjL[node]:     # 인접노드 중 방문하지 않았으면 방문
        if visited[next] == 1:  # 방문했으면 다음 노드 탐색
            continue
        visited[next] = 1       # 첫 방문이면 방문했다고 1 표시
        DFS(next)               # 인접노드를 부모노드로 하는 DFS 함수 호출. 모든 인접노드 방문했으면 리턴


# 노드의 개수, 간선의 개수
V, E = map(int, input().split())

# 1. 인접리스트 만들기
adjL = [[]*(V+1) for _ in range(V+1)]

# 2. 방문 기록증 만들기
visited = [0] * (V+1)

# 3. 인접리스트 채우기
temp = list(map(int,input().split()))
for i in range(E):  # 간선 수 만큼 반복.  노드 개수(V)+1해도 상관은 없을듯
    # 짝수, 홀수 인덱스 나눠서 인접리스트에 넣기
    n1 = temp[2*i]
    n2 = temp[2*i+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
# print(adjL)

# 자 이제 위로 올라가서 함수 만들어

# 시작노드는 1이고, 방문했다고 visited에 표시하고 시작
start = 1
visited[1] = 1
print('#1',end=' ')
DFS(start)
print('-'.join(nodes))

'''
리뷰
1. 어찌저찌 코드를 작성하긴 했는데
2. 출력형태 맞추는걸 해맸다
3. pass이긴한데 nodes를 함수밖에서 저렇게 쓸 수 있는거야...?
'''