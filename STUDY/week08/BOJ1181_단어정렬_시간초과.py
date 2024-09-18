N = int(input())
temp = []
for _ in range(N):
    word = input()
    temp.append(word)

temp = list(set(temp))  # 중복값 제거
n = len(temp)
# 일단 길이 짧은 것 부터 긴 순으로 정렬
for i in range(n-1,0,-1):
    for j in range(0,i):
        if len(temp[j]) > len(temp[j+1]):
            temp[j],temp[j+1] = temp[j+1],temp[j]

        # 사전순으로 어떻게 하지
        elif len(temp[j]) == len(temp[j+1]):  # 'wait', 'wont'
            for a in range(len(temp[j])):                   # 길이 같을때
                if ord(temp[j][a]) == ord(temp[j+1][a]):    # 문자 한글자씩 비교했는데 같으면 다음 글자 비교
                    continue
                elif ord(temp[j][a]) > ord(temp[j+1][a]):   # 문자열 한글자씩 비교했는데 왼쪽이 크면
                    temp[j], temp[j+1] = temp[j+1], temp[j] # 스왑하고 정지. 이후 문자 계속 비교하면 값 달라짐
                    break

for x in temp:
    print(x)

'''
리뷰
1. 버블 정렬조차 기억 안나서 참고함
2. 사전순으로 정렬할때 '>'일때만 고려하고, break 안해서 im, it, no 순서 잘못됐었음; 또 조건문;
3. 시간초과
3-1. 그럴만해. 하지만 해결방법 모르겠어
'''