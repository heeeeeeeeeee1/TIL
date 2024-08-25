# 각 색종이의 보이는 부분의 면적 구하기
N = int(input())    # 색종이 장수

# 1001칸 2차원 배열 만들기
arr = [[0]*1001 for _ in range(1001)]

# 색종이 놓기
for n in range(1, N+1):
    x, y, w, h = map(int, input().split())  # x, y: 색종이 시작 좌표, w: 너비, h: 높이
    for i in range(x, x+w):
        for j in range(y, y+h):
            arr[i][j] = n                   # 1번 색종이면 1, 2번 색종이면 2로 칠하기


# 각 색종이 면적 구하기 1
# for n in range(1, N+1):             # 색종이 번호 이용하기 위함
#     result = 0
#     for k in range(1001):           # 도화지 전체 순회하여
#         result += arr[k].count(n)   # n으로 칠해진 n번 색종이 면적 구하기
#
#     print(result)

# 각 색종이 면적 구하기 2
for n in range(1, N+1):
    result = 0
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == n:  # 색종이 번호(n)에 해당한다면
                result += 1     # 1씩 증가 => 즉, 색종이 면적
    print(result)

'''
리뷰
1. 왜 1001이어야 할까. 아 1001칸이면 0 ~ 1000이니까 1001이어야 되는게 맞네; 왜 1000이라고 생각했지
2. 정보를 따로 저장할 필요없었다...어차피 덮여씌워지니까
'''