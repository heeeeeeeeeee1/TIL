a, b, c = map(int, input().split())

if a == b:
    if b == c or a == c:
        price = 10000 + a*1000
    else:   # 2개만 같음
        price = 1000 + a*100

elif b == c:
    if a == c or a == b:
        price = 10000 + b * 1000
    else:  # 2개만 같음
        price = 1000 + b * 100

elif a == c:
    if a == b or b == c:
        price = 10000 + a * 1000
    else:  # 2개만 같음
        price = 1000 + a * 100

elif a != b and b != c:   # 3개가 다 다르면
    price = max(a, b, c) * 100

print(price)

'''
리뷰
1. 생각보다 오래걸림, 쉬울거라고 생각했는데 오만했다^^;
2. 코드 복붙해서 b ==c 조건에 b로 안되어있고 a로 되어있었음;
'''