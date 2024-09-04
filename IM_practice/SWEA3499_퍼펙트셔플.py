T = int(input())
for tc in range(1,T+1):
    N = int(input())    # 카드 장수
    cards = input().split() # list 사용하지 않아도 리스트로 생성됨
    # print(cards)
    # 문자열(단어)로 이루어진 경우도 되는지 확인 필요 -> 됨

    # 1. 입력받은 cards를 반으로 나눈다.
    # N(카드 장수)가 홀수이면 먼저 놓는 쪽에 한장이 더 들어가야 한다.
    if N % 2 == 1:
        N = N+1

    half_cards = []
    # 1-1. pop(0)를 N//2만큼 반복해서 half_cards에 append한다.
    for card in range(N//2):
        a = cards.pop(0)
        half_cards.append(a)
    # print(half_cards)
    # print(cards)

    # half_cards와 cards를 순서대로 pop(0)해서
    # result 리스트에 append한다.
    result = []
    while cards:    # 홀수일 때 half_cards가 cards보다 카드 개수 많으니까 얘를 한번 더 pop해야함
        x = half_cards.pop(0)
        result.append(x)
        y = cards.pop(0)
        result.append(y)
    if half_cards:  # cards에 값이 남아있다면
        result.append(half_cards.pop(0))

    # 언패킹하여 출력
    print(f'#{tc}', *result)


'''
리뷰
1. 37분 걸림
2. 처음 설계할 때 카드가 홀수일 경우 고려 안함
2-1. 홀수일때 이렇게 반복하면 y = cards.pop(0) IndexError: pop from empty list
for _ in range(N//2):
    x = half_cards.pop(0)
    result.append(x)
    y = cards.pop(0)    
    result.append(y)
'''

