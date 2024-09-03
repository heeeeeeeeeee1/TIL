# 4바이트 커질때마다 0번 인덱스에 'long' 추가
# 4로 나누어 떨어져야하고, 4로 나눈 몫만큼 'long' 추가
N = int(input())

result = ''
for i in range(N//4):
    result += 'long '

print(f'{result}' 'int')

'''
리뷰
1. result를 리스트로 하려고 했다가 그렇게 하면 출력할 때 언패킹해야돼서 문자열로 수정후 더해줌
'''