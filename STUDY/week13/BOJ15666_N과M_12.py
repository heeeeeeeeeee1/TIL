def recur(start):
    if len(result) == M:
        print(*result)
        return

    for i in range(start, len(lst)):
        result.append(lst[i])
        recur(i)
        result.pop()    # 돌아왔을 때(return) 끝 숫자 빼줘야 다음 (자식노드) 탐색할 때 다른 조합 생성 가능


N, M = map(int, input().split())
lst = list(map(int,input().split()))
lst = list(set(lst))    # 같은 값이 여러개면 모든 조합이 다 출력되므로 중복제거 후 탐색 시작
lst.sort()              # 정렬 후 탐색해야 비내림차순 수열 가능

result = []
recur(0)                # 입력값(리스트)의 0번 인덱스부터 시작


'''
리뷰
1. 여전히 재귀 헷갈림
2. 입력값을 리스트로 받고, 이 요소를 그대로 for문 돌렸더니 순열됨(모든 경우의 수 다 나옴)
2-1. 그럼 인덱스를 이용하자 -> 같은 값이 수열로 만들어져도 되니까 recur(i+1)가 아닌 recur(i)형태로 재귀 호출
3. 같은 숫자가 2개 이상이면 그 조합까지도 다 출력됨.
3-1. 중복값을 미리 지워서 탐색하면 중복 제거 되지 않을까? -> 최종본
'''