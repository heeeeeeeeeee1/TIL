import sys

N = int(input())
temp = []
for _ in range(N):
    temp.append(int(sys.stdin.readline()))

temp.sort()
# print(temp)
for a in temp:
    print(a)

'''
리뷰
1. 이거 맞아?
2. 맞는것 같은데 틀렸다길래 input = sys.stdin.readline 써봤는데
2-1. 틀렸다길래 확인해보니까 공백 들어가있었음. 사용을 안하다 보니 사용 방법을 몰라서 못씀.
2-2. int(sys.stdin.readline()) int 씌우면 공백 안들어가네
'''