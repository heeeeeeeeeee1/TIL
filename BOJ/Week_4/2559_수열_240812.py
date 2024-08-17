# 2559 수열

# N 전체 날짜의 수, K 연속적인 날짜 수
N, K = map(int, input().split())
temp = list(map(int, input().split()))

# 2.
# K까지의 초기 합 구하기
# sum함수 사용X
temp_sum = 0
for k in range(K):  # K: 연속적인 날짜의 수
    temp_sum += temp[k]

# 0 ~ K의 합을 (가장 큰 온도들의 합) 초기값으로 둠
max_sum = temp_sum

for i in range(K, N):  # K부터 N전까지(N-1까지) 순회
    temp_sum = temp_sum + temp[i] - temp[i-K]   # 온도 합계에서 지금 위치 값 더하고 K전에 있는 값은 빼줌

    if max_sum < temp_sum: # 초기값보다 한칸 순회해서 계산한 합이 더 크면
        max_sum = temp_sum # 갱신

print(max_sum)





# 1.
# max_sum = -100000
# for n in range(N-K+1):    # N-K까지 순회
#     temp_sum = 0
#     for i in range(n, n+K):
#         # K범위 만큼 합산
#         temp_sum += temp[i]
#
#     if max_sum < temp_sum:
#         max_sum = temp_sum

