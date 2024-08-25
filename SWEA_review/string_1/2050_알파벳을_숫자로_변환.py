# 각 알파벳 숫자로 변환
alphabet = input()

result = []
for a in alphabet:
    ans = ord(a)-64
    result.append(ans)

print(*result)
