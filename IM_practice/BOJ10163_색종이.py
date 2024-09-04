N = int(input())

# 도화지 만들기
arr = [[0]*1001 for _ in range(1001)]

for papers in range(1, N+1):
    x, y, w, h = map(int, input().split())

    # 색종이 칠하기
    for r in range(x,x+w):
        for c in range(y,y+h):
            arr[r][c] = papers

# 각 색종이 넓이 구하기
for papers in range(1, N + 1):
    cnt = 0
    for r in range(1001):
        for c in range(1001):
            if arr[r][c] == papers:
                cnt += 1

    print(cnt)