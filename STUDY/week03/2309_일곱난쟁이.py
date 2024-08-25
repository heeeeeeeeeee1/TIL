# 9 난쟁이 키 입력
N = 9    # 난쟁이 9명
dwarf9 = 0
dwarfs = [] # 난쟁이 9명 키 리스트
for _ in range(N):
    dwarf = int(input())
    dwarfs.append(dwarf)
    dwarf9 += dwarf       # 난쟁이 9명의 키 총합
    dwarf2 = dwarf9 - 100 # 100이 난쟁이 7명 키의 합이니까 9명의 합에서 빼면 난쟁이 7명에 해당하지 않는 2명의 키의 합

# print(dwarf9) # 140
# print(dwarf2) # 40
# print(dwarfs) # [20, 7, 23, 19, 10, 15, 25, 8, 13]

# 어차피 정렬해야되니까 복습겸 선택정렬 함수 정의
def selection_sort(arr):
    for i in range(len(arr)): # i는 인덱스
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 남의 집 난쟁이 2명 찾기
find_dwarf2 = False                 # 난쟁이 2명 못찾음
for i in range(N-1):                # i는 N-2까지 순환
    for j in range(i+1, N):         # j는 i 다음부터 N-1까지 순환
        if dwarfs[i] + dwarfs[j] == dwarf2: # 40
            # 리스트에서 제거
            a = dwarfs[i]
            b = dwarfs[j]
            dwarfs.remove(a)
            dwarfs.remove(b)
            find_dwarf2 = True      # 난쟁이 2명 찾음
            break
    if find_dwarf2 == True:         # 설명 봐도 왜 하는지 잘 모르겠음. 이 부분 없으면 난쟁이 찾았는데 반복문 계속 되나?
        break

# 남은 난쟁이 7명 키 리스트 오름차순 정렬해서 출력
selection_sort(dwarfs)

for height in dwarfs:
    print(height)
