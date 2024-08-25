# 수열의 길이
N = int(input())

# 수열(N개의 숫자)
seq = list(map(int, input().split()))   # sequence: 수열

# 오름차순(ascending) 수열인지 내림차순(descending) 수열인지, 각 정렬이 얼마나 지속되는지(길이가 얼마나 되는지)
max_ascending = 1
max_descending = 1
ascending = 1
descending = 1
for i in range(N-1):        # i는 인덱스. 비교하면서 순회하니까 i+1 out of range 방지하려면 i가 0부터 N-2까지 순회
    if seq[i] <= seq[i+1]:  # 오른쪽값이 기준위치 보다 크거나 같으면(처음에 같을때 고려안해서 수정)
        ascending += 1      # 오름차순 수열 +1'
    else:
        ascending = 1       # 오름차순 수열 끊기면 초기화

    if seq[i] >= seq[i+1]:  # 아 같은건 양쪽 다 포함이네?
        descending += 1
    else:
        descending = 1      # 내림차순 수열 끊기면 초기화


    # 위의 for문에서 descending에 해당되지 않아도 max_를 0으로 해놔서 max_값이 증가하게 됨; => 연속되는 수열이려면 2이상이어야 하므로 초기값 1로 수정
    if descending > max_descending:
        max_descending = descending
    # 가장 긴 값으로 순회마다 갱신
    if ascending > max_ascending:
        max_ascending = ascending


# 길이가 같은 경우는 고려안해도 되나? 어차피 크면 갱신이고 같거나 작으면 현재 최대길이 유지니까?
if max_ascending > max_descending:
    print(max_ascending)
else:
    print(max_descending)

