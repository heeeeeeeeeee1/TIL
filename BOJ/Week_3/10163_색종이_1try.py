# 각 색종이의 보이는 부분의 면적 구하기
# 색종이 장수
N = int(input())

# 1001칸이면 인덱스는 0 ~ 1000
arr = [[0]*1000 for _ in range(1000)]

# 색종이 정보 저장
papers = []

# 색종이 N개가 한 도화지에 표시
for i in range(N):                          # i: 색종이 번호
    x, y, w, h = map(int, input().split())  # x(열), y(행), 너비(width), 높이(height)
    papers.append((x, y, w, h))             # 색종이 정보 튜플로 리스트에 저장
    for r in range(y, y+h):                 # 색종이 범위 칠하기
        for c in range(x, x+w):
            arr[r][c] = i + 1               # 색종이 번호로 칠하기. 1번 색종이면 1, 2번 색종이면 2

# ----------------------------------------------
# 각 색종이 보이는 면적 계산
for j in range(N):
    x, y, w, h = papers[j]                  # 저장해뒀던 색종이 정보 불러오기
    count = 0
    for r in range(y, y+h):
        for c in range(x, x+w):
            if arr[r][c] == j + 1:          # 해당 색종이 번호와 일치하면 보이는 부분
                count += 1

    print(count)


    # 색종이 순서도 중요하네?
        # print(arr)    # 색종이 순서도 중요하네? 마지막꺼만 칠해지나
        # 첫번째 장은 보이는 것만 되는게 아니라 원본 그대로의 면적이 출력 되는것 같은데?
        # 한번 좌표로 색칠하는거 해봤다고 룰루랄라 하다가 마지막값만 맞게 나와서 문제 다시 읽음 ㅋㅋ
        # 첫번째 색종이도 보이는 만큼의 면적 구해야됨


        #2. 다른 도화지에 저장하고 저장한 그 배열 넓이 출력력