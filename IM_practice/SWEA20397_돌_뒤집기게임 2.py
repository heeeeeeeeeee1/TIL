# 뒤집기 함수
def switch(lst, a):
    if lst[a] == 1:
        lst[a] = 0
    else:
        lst[a] = 1
    return lst


T = int(input()) # 테스트 케이스
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 돌의 수, M: 뒤집기 횟수/// 5 1
    stone = list(map(int, input().split())) # 0 1 0 1 0

    for m in range(M):
        i, J = map(int, input().split())    # i번째 돌을 사이에 두고 마주보는 j개의 돌 /// 2 2

        for j in range(1, J+1):  #J: 2
            # 입력받은 i가 실제 stone의 인덱스와 1 차이나기 때문에 i-1
            if 0 <= i-1-j < N and 0 <= i-1+j < N:         # 주어진 돌을 벗어나는 경우 뒤집기는 중지된다.
                if stone[i-1-j] == stone[i-1+j]:
                    switch(stone, i-1-j)
                    switch(stone, i-1+j)

    print(f'#{tc}', *stone)


'''
리뷰
1. 문제를 잘 읽자. 첫번째 읽을때도 잘못읽고 잘못이해하고, 두번째 읽을때도 범위 벗어나는 경우 어떻게 하는지 안읽어서 문제이해를 제대로 못했다.
2. 인덱스 어렵다
3. 전에는 스위치 전환 stone[i] = 1 - stone[i] 이런식으로 했는데, 이번에는 함수로 만들어봤다. 함수 만들어서 사용하는 것도 잘 안하다보니 단순 구성도 버벅인다.ㅈ
3-1. switch(a)로 만들었었는데 0 1 전환이 안돼서 수정했다.
3-2. 전환이 안되었다기보다는 return을 a로 했더니 stone 리스트에 반영이 안된상태로 출력돼서 리스트도 입력받는 함수로 수정했다.
# 뒤집기 함수(뒤집은 값 반환)
def switch(a):
    if a == 1:
        a = 0
    else:
        a = 1
    return a
'''
