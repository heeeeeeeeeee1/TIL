from collections import deque

# N명의 사람, K번째 사람 제거
# 모두 제거될 때까지 계속
N, K = map(int, input().split())

# 큐 만들기
q = deque()
for i in range(1,N+1):
    q.append(i)

# K번째 사람이 0번 인덱스가 되도록 하려면
# K-1만큼 popleft 하면됨
print('<', end='')
while len(q) != 1:  # 1개 남을 때까지 반복///출력형태를 맞추기위한 시도..
    for _ in range(K-1):
        q.append(q.popleft())

    # K번째 사람이 제일 앞으로 왔으니까 이걸 출력하면 된다.
    ans = q.popleft()
    print(str(ans)+', ',end='')
print(*q,end='')
print('>')


'''
리뷰
1. 전에 접한적 있던 스터디 문제인데
1-1. 이 아이디어가 그 당시 스터디원 중 누군가의 아이디어였는지, 내 아이디어인지 모르겠다.
1-2. 전자인 것 같다.
1-3. 그때는 못풀었음
2. 출력형태 맞추기 어려워
'''