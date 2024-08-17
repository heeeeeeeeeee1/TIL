# 종이자르기 => 가장 큰 종이 조각의 넓이 출력
# 가로, 세로(길이여서 행 열 헷갈림...)
column, row = map(int, input().split())

# 칼로 잘라야 하는 점선 개수
cut = int(input()) # 3

# 가로 세로 길이를 각각 추가한 리스트 생성
row_list = [0, row]
column_list = [0, column]

# 추후 리스트 정렬을 위한 함수 정의
def selection_sort(arr, N): # arr: 배열, N: 배열 길이
    for i in range(N-1): # 기준위치. N-1까지인데 굳이 자기 자신 비교할 필요 없어서 N-2까지 비교하면 되니까
        min_idx = i
        for j in range(i+1, N): # 비교 원소 범위. i+1 부터 N-1까지
            if arr[min_idx] > arr[j]: # 탑색한 최솟값(arr[j])이 설정한 최솟값(arr[min_idx])보다 작으면
                min_idx = j # 구간의 최솟값(인덱스)을 기준위치로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # 기준위치 i랑 바꿔야함


# 순회하며 가로, 세로 구분해서 리스트에 추가
for i in range(cut): # cut만큼 반복할거야(3이니까 0 ~ 2)
    # m, cut_num = list(map(int, input().split())) # 0 3 / 1 4 / 0 2
    m, cut_num = map(int, input().split())  # 0 3 / 1 4 / 0 2
    if m == 0: # 0이면
        row_list.append(cut_num) # 가로 자르기(행 자르기) 점선을 리스트에 추가
    elif m == 1: # 1이면
        column_list.append(cut_num) # 세로 자르기(열 자르기) 점선을 리스트에 추가


# 위에서 정의한 선택 정렬 함수 사용해 각 리스트 정렬(오름차순)
# 사실 이 예시에서는 입력 순서대로 가져오면 오름차순이어서 안해도 되긴 함
selection_sort(row_list, len(row_list))
selection_sort(column_list, len(column_list))


# 가장 긴 길이 찾기 함수
def max_length(arr): # arr: 오름차순으로 정렬된 배열
    # 각 요소들의 차이가 긴 길이 찾기
    max_val = 0
    for i in range(1, len(arr)): # 뒤에서부터 가져오기
        length = arr[i] - arr[i-1]    # 기준값과 그 앞의 값 뺄셈 => 사각형 한 변의 길이
        # 뺀 값 중에 최댓값 반복문 돌 때마다 갱신
        if max_val < length:
            max_val = length
    return max_val

# 정의한 최대 길이 찾기 함수 사용하여 가장 긴 길이 찾기
row_max = max_length(row_list)
column_max = max_length(column_list)


# 최댓값끼리 곱하면 => 최대 넓이
result = row_max * column_max
print(result)
