# 각 색종이의 보이는 부분의 면적 구하기


# 색종이 장수
N = int(input())

arr = [[0] * 1001 for _ in range(1001)] # 1000이야 1001이야?
# 색종이 N개가 한 도화지에 표시
for n in range(1, N+1):                       # i: 색종이 번호
    si, sj, w, h = map(int, input().split())  # si: start i, sj: start j, 너비(width), 높이(height)
    for i in range(si, si+h):
        # 하나씩 표시하는 방법
        # for j in range(sj, sj+w):
        #     arr[i][j] = n               # 색종이 번호로 칠하기. 1번 색종이면 1, 2번 색종이면 2
        # lst 단위로 표시하는 방법
        arr[i][sj:sj+w] = [n] * w


# 2. cnts 배열 사용해서 arr 한번만 순회/// 출력값이 다른데? 12점 나옴
cnts = [0] * (N+1)
for lst in arr:
    for n in lst:
        cnts[n] += 1

print(*cnts[1:], sep ='\n')    # 0번 인덱스는 사용X => 1번부터 슬라이싱 # 가로로 연달아 출력 되므로 세로로 분리


# 1. 색종이 번호를 배열에 기록하는 방법(오래 걸림)
# for n in range(1, N+1):
#     cnt = 0
#     for lst in arr:
#         cnt += lst.count(n) # 색종이 번호에 해당하는 숫자 각각 카운팅(count: 문자열, 리스트 메서드)
#     print(cnt)


