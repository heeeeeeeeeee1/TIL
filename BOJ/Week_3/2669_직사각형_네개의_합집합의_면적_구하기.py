# 직사각형 합집합 면적

arr = [[0] * 100 for _ in range(100)] # 100. 101까지 해야되나?

# 직사각형 크기에 맞게 1채우기
# 좌표 만큼 어떻게 채움?
for t in range(4):     # 입력줄은 4줄
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2): # r: row
        for c in range(x1, x2): # c: column
            if arr[r][c] == 0:
                arr[r][c] = 1

result = 0
for r in range(100):
    for c in range(100):
        if arr[r][c] == 1:
            result += 1

print(result)