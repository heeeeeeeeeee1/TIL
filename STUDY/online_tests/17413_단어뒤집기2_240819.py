
S = input()         # 문자열 입력
stack = []          # 빈 스택
result = ''         # 출력할 결과
tag = False         # < 만나면 True

for s in S:
    if s == '<':                    # < 만나면
        tag = True                  # tag True
        while stack:                # < 이전까지 쌓았던 문자 pop해서
            result += stack.pop()   # 출력결과에 넣기
        result += s                 # 지금 받은 <도 result에 넣기
    elif s =='>':                   # > 만나면
        tag = False                 # tag 변경
        result += s                 # > 이전까지의 문자는 <태그>일테니까 뒤집지 않고 그대로 출력
    elif s == ' ':                  # 공백을 만났다는 건 한 덩어리 단어 끝났다는 뜻이니까
        while stack:                # 그 동안 쌓인 단어 뒤집어서 결과에 추가
            result += stack.pop()
        result += s                 # 공백도 출력해야되니까 result에 추가
    else:                           # <, >, ' '가 아닌 일반 문자이고
        if tag:                     # tag가 True라면
            result += s             # result에 바로 넣어. 근데 이럴일이 없지 않나
        else:                       # tag가 False라면
            stack.append(s)         # 태그 외부의 문자는 stack에 추가

# stack에 남아있으면 pop (<- 이 경우가 문자열은 종료됐는데 뒤에 공백 없는 경우인가?)
while stack:
    result += stack.pop()

print(result)