# 버블정렬(오름차순)
# 기준위치와 그 다음 위치 값 비교해서 스왑
def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1,0,-1):
        for j in range(0, i):    # 0부터 i-1까지
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# #--------------------------------------------------------------------

# 선택정렬
# 최솟값 찾기 -> 기준 위치*랑 스왑
# 스왑한 값 다음부터 끝까지(정렬되지 않은 남은 배열) 다시 최솟값 찾고 스왑
def selected_sort(lst):
    n = len(lst)                        # 정렬할 배열의 길이
    for i in range(n-1):                # n-2까지만 비교하면됨
        i_min = i                       # 최솟값 인덱스
        for j in range(i+1, n):
            if lst[j] < lst[i_min]:     # 설정한 최솟값보다 지금 순회한 값이 더 작으면
                i_min = j               # 최솟값 인덱스 갱신
        lst[i], lst[i_min] = lst[i_min], lst[i] # 스왑해야지
    return lst

#--------------------------------------------------------------------

# 카운트 정렬(정수형에서 가능)
# 입력된 숫자 범위 만큼 COUNT 배열 만들기
# DATA 값이 COUNT의 인덱스
data = [1,5,0,6,5,9,5,2,3,4,6]
COUNT = [0] * 10            # data에 9까지있으니까 0 ~ 9
temp = [0]  * len(data)     # temp에 정렬된 data 배열 담을 예정

# 1. data 값이 COUNT의 인덱스
for i in data:
    COUNT[i] += 1
# print(COUNT) #[1, 1, 1, 1, 1, 3, 2, 0, 0, 1]

# 2. 누적합
for i in range(1,len(COUNT)):
    COUNT[i] = COUNT[i-1] + COUNT[i]
# print(COUNT) # [1, 2, 3, 4, 5, 8, 10, 10, 10, 11]

# 3. data 뒤부터 순회하면서 temp에 정렬된 값 입력
for i in range(len(data)-1,-1,-1):
    COUNT[data[i]] -= 1
    temp[COUNT[data[i]]] = data[i]
print(temp) # [0, 1, 2, 3, 4, 5, 5, 5, 6, 6, 9]
