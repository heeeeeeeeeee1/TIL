from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())    # N: 문서의 개수, M: 궁금한 문서 인덱스
    lst = list(map(int, input().split()))  # 문서 중요도

    papers = deque()
    importance = deque()
    for i, j in enumerate(lst):
        papers.append(i)
        importance.append(j)

    # 인덱스가 M일때의 값을 기억
    # 근데 중요도 같으면 어떻게 해? q를 두개만들까

    # # 그 값이 출력될때까지 deque, enque 반복
    cnt = 0
    while True:
    # 가장 중요도가 큰 것 부터 출력이니까
        mx = max(importance)
        if importance[0] == mx:
            importance.popleft()
            target = papers.popleft()
            cnt += 1    # 출력할때마다 cnt +=1
            if target == M:
                break
        else:
            importance.append(importance.popleft())
            papers.append(papers.popleft())

    print(cnt)

'''
리뷰
1. 문제를 제대로 이해 못해서 문제이해하는데 생각보다 오래걸림^^; 문해력 이슈;
2. if importance[0] == mx: 이렇게 안하고 바로 importance.popleft() 해서 오류남
2-1. 변수에 할당하자-!
3. 작업을 반복하면 타겟 문서의 인덱스가 계속 변경되는데 어떻게 하지?
3-1. 중요도 값이 같을때는 어떻게 하지?
3-2. => deque를 두개 돌리자!(중요도, 문서 인덱스) 인공지능 참고해보니 2차원으로 1개의 덱에 저장하면 되나보다. 하지만 내 생각대로 코딩하고 싶었음
3-3. 인덱스랑 엮여있으면 어려워 하는편.
'''