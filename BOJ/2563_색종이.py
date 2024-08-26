T = int(input())
# 흰 도화지
arr = [[0]*100 for _ in range(100)]

for tc in range(1, T+1):
    # 주어진 좌측 꼭짓점 값 x, y
    x, y = map(int, input().split())

    # 색종이 한 변의 길이 10
    n = 10

    for r in range(x, x+n):
        for c in range(y, y+n):
            if arr[r][c] == 0:  # 흰 도화지이면
                arr[r][c] = 1   # 1로 칠해라

# 2차원 배열 카운트
result = 0
for lst in arr:
    result += lst.count(1)

print(result)

'''
리뷰
1. 생각없이 풀다가 100, 200, 300 나옴
2. 색종이 여러장이 한 도화지에 있는 것
3. ㅎ ㅏ.. 변수명 x, y로 중복해서 계속 y값 증가했던거...=> r, c로 변경해서 해결
'''