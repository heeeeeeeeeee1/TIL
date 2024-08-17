# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올때까지 0의 개수 구하기

# 팩토리얼 못해요^^
# N! 얼만지 구하고
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 팩토리얼 계산. 정수
target = factorial(int(input()))

# 슬라이싱, 인덱싱을 위해 문자열 리스트로 변환
target_list = list(str(target))

# 역순으로 순회하면서 0이면 카운팅, 아니면 멈춤
count = 0
for i in range(len(target_list)-1,-1,-1):
    if target_list[i] == '0': # 문자열
        count += 1
    else:
        break

print(count)




