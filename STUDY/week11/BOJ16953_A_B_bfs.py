# 1. A를 큐에 넣는다.
# 2. 연산한다.
# 2-1. 2를 곱하거나
# 2-1. 1을 수의 가장 오른쪽에 추가한다. -> 현재 숫자에 *10 +1
# 3. 연산할때마다 cnt += 1
# 4. 연산 반복 후 B와 같아지면 그때의 cnt가 최솟값. 여기에 1더한 값을 출력
# 4-1. 연산을 하다가 B보다 커지면 그만
# 4-2. 큐가 비었는데도 B에 도달하지 못하면 -1출력

# 거꾸로 가도 되나? 그게 그건가
from collections import deque

def check(A,cnt):
    q = deque()
    q.append((A,cnt))
    while q:
        num, cnt = q.popleft()

        if num == B:
            return cnt + 1

        if num * 2 <= B:
            q.append((num*2,cnt+1))

        if num * 10 + 1 <= B:
            q.append((num*10+1, cnt+1))

    else:
        return -1



A, B = map(int, input().split())
cnt = 0
print(check(A,cnt))

'''
리뷰
1. bfs라는걸 알고 풀어서 방향을 잡긴했는데 몰랐으면 못건드렸을듯
2. 같은 레벨의 값들에 대해서 cnt += 1되는게 아니라 모든 값에 대해 cnt 증가돼서 출력결과가 크게 나옴 
2-1. 이것저것 바꿔봤는데도 cnt += 1의 위치를 어디에 둬야할지 모르겠어서
2-2. 서칭함. -> cnt도 같이 튜플로 묶어서 큐에 넣더라...
def check():
    cnt = 0
    while q:
        num = q.popleft()
        mul_two = num * 2
        add_one = num * 10 + 1

        for i in [mul_two, add_one]:
            if i == B:  # B로 만들 수 있으면 연산의 최소 횟수 + 1 출력
                return cnt + 1
            elif i > B:
                break
            q.append(i)
        cnt += 1      # 한세트 연산하고 cnt += 1
        # cnt += 1    # 얘가 이렇게 되면 같은 레벨의 값들인데 카운트를 증가시키게 됨 -> for문 써야되나?
'''

