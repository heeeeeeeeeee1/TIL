T = int(input())
for tc in range(1,T+1):
    field = list(input())   # 또 input 한번에 못받아;

    ball = 0
    while field:
        now = field.pop()    # ) 아닌건 다 pop됨
        if now == ')':
            next = field.pop()
            if next == '(': # 이 경우는 공 1개인거 확인했으니까 다시 append할 필요없음
                ball += 1
            elif next == '.' or '|':
                ball += 1
                field.append(next)  # 다시 비교해야되니까 append

        elif now == '(':
            ball += 1

    print(f'#{tc} {ball}')


'''
리뷰
1. 1시간 36분 걸림;
2. 아이디어가 생각이 안났음
2-1. 일반 문자열 순회로 풀려다가 pop(0)로 해결하려고 했는데 append도 해야돼서
2-2. 스택구조로 생각하는게 나은 것 같아 다시 생각함
2-3. 이런 문제 유형 조건 고려하는게 항상 헷갈리는데 어렵게 생각해서 그런 것 같다.
3. 조건문 뭐가 부족한지 모르겠으면 디버깅을 해보자
3-1. 물론 디버깅을 뇌가 못따라가면 디버깅을 해도 힘들다
4. 예전에 다른 문제들 풀었던 게 애매하게 뇌에 남아있는게 도움이 될 수도, 독이 될 수도


낙서 메모
# if field:   # field가 차있으면
# 남은거 pop..할 필요 없네 계산기 아니라서

# 뭐야 ( or )면 카운팅하면 되는거네
# ()는 하나만 세고 or 두개 세고 () 이렇게 나오는 경우 -1
# 아 append할거면 stack으로 해야겠네
'''

