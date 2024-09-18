N = int(input())

# input 받아서 리스트에 추가
lst = []
for _ in range(N):
    lst.append(input())

# 중복값 제거
lst = list(set(lst))

# 알파벳 순 정렬
lst.sort()

# 길이 순으로 오름차순 정렬(짧은 것부터 긴 것)
# 앞에서 알파벳순으로 이미 정렬된 상태에서 정렬하기 때문에 길이순으로만 한번 더 정렬하면 됨
lst.sort(key=len)

print('\n'.join(lst))

'''
리뷰
1. 시간초과를 벗어나지 못해서 구글링했다.
1-1. 대충 훑어봤는데 sort()의 key를 사용하면되는 것이었다...!
1-2. 또 어렵게 생각함
2. print('\n'.join(lst)) 이렇게도 출력되는군
'''