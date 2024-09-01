N = int(input())    # 기둥 개수
# 높이 저장 리스트 만들기
# 입력받은 L 중에서 가장 큰 값을 저장 리스트의 길이에 사용하려고 함
L_lst = []
H_lst = []
for _ in range(N):
    L, H = map(int, input().split())    # L(기둥 왼쪽)을 좌표로 사용하고, H(높이)를 값으로 사용
    L_lst.append(L)
    H_lst.append(H)
# print(L_lst)

lst_len = max(L_lst)    # 리스트의 길이는 입력받은 L의 값 중 가장 큰 값+1이다.
lst = [0] * (lst_len+1)
# print(lst)

# 1. 리스트 채우기
for i in range(N):
    lst[L_lst[i]] = H_lst[i]
# print(lst)

# 1. 최고 높이 위치(인덱스) 구하기
max_h = max(H_lst)
max_pos = lst.index(max_h)
# print(max_h)    # 10
# print(max_pos)  # 8


# 2. 최고 높이 위치 전까지는 최댓값 갱신하면서 높이 값 갱신하기
max_val = lst[0]
for x in range(max_pos+1):
    if max_val < lst[x]:    # 지금 순회한 값이 max_val보다 크다면
        max_val = lst[x]    # 최댓값 갱신하고
    else:   # 작다면(같다는 조건은..?노상관?)
        lst[x] = max_val    # lst 갱신
# print(lst)  # [0, 0, 4, 4, 6, 6, 6, 6, 10, 0, 0, 4, 0, 6, 0, 8]

# 3. 최고 높이 이후는, 뒤에서부터 최댓값 갱신하면서 lst 갱신
max_val2 = lst[-1]
for y in range(lst_len,max_pos,-1):
    if max_val2 < lst[y]:   #
        max_val2 = lst[y]
    else:
        lst[y] = max_val2
# print(lst)  # [0, 0, 4, 4, 6, 6, 6, 6, 10, 8, 8, 8, 8, 8, 8, 8]

# 4. 리스트에 적힌 숫자들 다 더하면 최소 창고 다각형 면적
result = sum(lst)
print(result)

'''
리뷰
1. 카운팅 리스트(lst) 길이를 어떻게 할지 헤맸다(1-1)
1-1.
for _ in range(N):  # 또 input받아서 그러네...비효율+ 어차피 안됨 아니그러면 카운트리스트 길이 어떻게 정함? 1000개로 해?
    L, H = map(int, input().split())    # L(기둥 왼쪽)을 좌표로 사용하고, H(높이)를 값으로 사용
    lst[L] = H
print(lst)
2 .테스트 케이스 하나만 가지고해서 이 방법이 맞는지는 채점해봐야 알듯. 출력은 된다.
2-1. 반례에 하도 당해서 무섭다
3. 뒤에서부터 최댓값 갱신할 때 뉴런 느슨해져서 위에서한 코드 복붙한 느낌
'''
