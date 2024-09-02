# 윤년이면 1, 아니면 0
year = int(input())

# 4의 배수이면서 100의 배수가 아닐때거나
if year % 4 == 0 and year % 100 != 0:
    result = 1
elif year % 400 == 0:   # 400의 배수이거나
    result = 1
else:
    result = 0

print(result)