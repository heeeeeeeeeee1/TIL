# X: 영수증에 적힌 총 금액
# N: 영수증에 적힌 물건의 종류 수
# a: 각 물건의 가격, b: 개수
# 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes, 불일치 No
X = int(input())
N = int(input())
total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += (a*b)  # (물건 가격 * 개수) 누적합

# 반복문 종료 후 total과 X가 같은지 확인
if X == total:
    print('Yes')
else:
    print('No')