T = int(input())
for tc in range(1,T+1):
    N, Q = map(int, input().split())    # N: 가지고 있는 상자 수, Q: 뒤집을 횟수

    boxes = [0] * (N+1)  # 현주가 가지고 있는 상자 수 -> 리스트로 만들기
    for i in range(1, Q+1):  # 바꿀 상자의 범위(L부터 R까지)
        L, R = map(int, input().split())
        # i번째이면 L ~ R 범위의 상자값을 i로 변경
        for x in range(L, R+1):  # L부터 R까지니까
            boxes[x] = i

    print(f'#{tc}', *boxes[1:])

'''
리뷰
1. 범위를 잘보자^^
2. 뇌 살짝 빼고 해도 출력값 나오네! 이런 문제만 만났으면 좋겠다
3. 라고 생각했는데 제한시간 초괔ㅋㅋㅋㅋㅋㅋIM 시간 상관없다면서요ㅜ
3-1. N, Q가 1000까지네...
3-2. 아니 그게 문제가 아니라 for문 안에서 print 찍었잖아?
'''