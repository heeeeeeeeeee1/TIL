# 첫 번째 수로 양의 정수가 주어진다.
# 두 번째 수는 양의 정수 중에서 하나를 선택한다.
# 세 번째부터 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다. 예를 들어, 세 번째 수는 첫 번째 수에서 두 번째 수를 뺀 것이고, 네 번째 수는 두 번째 수에서 세 번째 수를 뺀 것이다.
# 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.

num = int(input())

max_len = 0                         # 가장 긴 리스트의 길이 초기값 설정
for i in range(1, num+1):           # 입력 받은 숫자에서 1 뺐을때 부터 부터 빼기
    temp = [num, i]                 # 100, 1 넣고 아래에서 뺄셈한 값 계속 추가
    while True:
        val = temp[-2] - temp[-1]   # 뒤에서 두번째 값에서 맨 끝값 빼기
        temp.append(val)            # 뺄셈하고 temp에 추가
        if val < 0:                 # 뺀값(val)이 0보다 작으면
            temp.pop()              # 음의 정수 버리고 끝(이미 위의 while문으로 음의 정수 추가된 상태이기 때문)
            break

    if max_len < len(temp): # while문 종료 후 생성된 temp의 길이가 max_len보다 크면
        max_len = len(temp) # 최대 길이 갱신
        max_temp = temp     # 가장 긴 리스트를 임시저장(이 때의 temp가 가장 긴 것이므로)

# 이때의 max_len과  max_temp 요소 출력
print(max_len)
print(*max_temp)

'''
리뷰
1. 반복문 범위 설정 num+1로 안하고 num으로 했더니 런타임 에러
2. 쉬운 문제인데도 조건문 어려워(while 쓸 생각을 못함)
3. 여기저기 타인의 코드 참고
'''