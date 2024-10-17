# 1. '-'를 찾아라 -> '-'기준으로 분리한다.
# 2. '+'로 이어져있는 값은 '+'기준으로 한번 더 분리한다.
# 2-1. 누적합 해준 후 뺄셈을 위한 리스트에 저장한다.
# 3. 뺼셈을 위한 리스트에 저장되어 있는 값을 누적뺄셈한다.

String = input().split('-')
# print(String)   # ['55', '50+40']

minus = []              # 뺄셈할 예정인 리스트
for i in String:
    total = 0
    temp = i.split('+') # '+'기준으로 분리. temp는 리스트임
    # print(temp)
    for j in temp:      # '+'로 분리한 숫자들 더하기
        total += int(j)
    minus.append(total) # 덧셈한 값들 뺄셈 예정인 리스트에 넣기

result = minus[0]
for m in range(1,len(minus)):
    result -= minus[m]
print(result)
'''
리뷰
1. 문자열.split('구분자', 분할 횟수)
1-1. 입력을 어떻게 받아하지? 입력값을 어떻게 가공해야하지?
1-2. 될듯 말듯 해서 붙잡고 있다가 치팅했다. split하면 되는거였는데 또 어렵게 생각함^.^
1-3. split 쓸 생각 못해서 숫자, +, - 어떻게 구분해야될지 고민했던 이리저리 시도했던 코드(지저분)
temp = input()  # 문자열
# '-'가 나올때까지 더한다.
# '-'가 나오면 여태까지 더한거에서 그 뒷값 뺸거 뺴야되는데
# 계산기 처럼 풀어야 되나
temp_num = ''    # 숫자이어붙여서 n의 자리수 만들기
expected_minus = []
calculate = 0     # 덧셈 조각 리스트에 넣어?

for i in temp:
    if i.isdigit() == True: # 숫자모양의 문자라면
        temp_num += i    # 이렇게 더하면 n의 자리수 숫자 붙으니까?

    elif i == '-':      # 뺄셈이라면
        # 이전 까지 누적합 했던거 뺼셈 예정 리스트에 넣어
        expected_minus.append(temp_num)
        # calculate에 있는 숫자들 서로 빼
        # calculate = 0
        temp_num = ''  # 다음 문자형 숫자 받아야되니까 초기화
    else:   # 덧셈이라면
        temp_num += i   # 이전까지 temp_num에 담은 숫자형태의 문자를 숫자로 변환후 누적합
        # calculate += int(temp_num)
        # calculate = 0

print(calculate)
print(expected_minus)
'''




