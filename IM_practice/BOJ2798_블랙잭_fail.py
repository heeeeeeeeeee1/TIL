# 1. cards 정렬하기(해도되고 안해도될듯)
# 2. 하나 기준으로 잡고 나머지 숫자2개 조합 바꾸면서 합 구하기
# 3. 그 합이 M과 유사(M보다 작거나 같다)한지 확인
# 4. 가장 M과 유사한 값 출력
'''
8 21
2 3 5 6 8 9 10 11
'''

N, M = map(int, input().split())        # N: 카드 수, M: 딜러가 부르는 수(카드 3장의 합과 유사해야 하는 수)
cards = list(map(int,input().split()))  # 카드 입력

# 두개 뽑고 더해.근데 이렇게 할거면 자기자신 또 더하지 않게 범위 설정해야..?
temp = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = cards[i] + cards[j] + cards[k]
            temp.append(total)
# print(temp)       # 중복값도 그냥 그대로 담김
temp = set(temp)    # 시간초과 떠서 중복값 제거 시도했지만 여전히 시간초과
temp = list(temp)
# print(temp)

# 이렇게 생각했었는데, 누락 조합 발생
# temp = []
# for i in range(N):
#     for j in range(i+1, N-1):
#         total = cards[i] + cards[j] + cards[j+1]   # 모든 경우의 합 구하기
#         # 이 합이 M과 가까운지 어떻게 알지?
#         # 합을 리스트에 담고 그 중에서 M이랑 가까운걸 찾아?
#         temp.append(total)
# print(temp)

# temp 값 오름차순 정렬하고 M보다 큰 건 순회하지 말자
temp.sort() # 왜 while에서 블랙잭 구했는데 여기로 다시 올라가지?
# print(temp)
blackjack = 0
while True:
    for x in range(len(temp)):
        if temp[x] > M:             # M보다 크고, 정확히 M인 값도 없으면?
            blackjack = temp[x-1]   # 직전 값이 blakjack
            break
        elif temp[x] == M:          # M과 같다면
            blackjack = temp[x]     # 이 값이 blackjack
            break
        # else: # 필요해?
    if blackjack:                   # 블랙잭 이미 구했으면(값이 있으면) -> 굳이? 이조건?
        break                       # 그만 돌아

print(blackjack)


'''
리뷰
1. 처음엔 정렬해서 3개씩 더해보면서 M과 가까운 수를 찾으려고 했다.
1-1. 그렇게 하면 못 더해보는 조합이 생겨서 다시 생각해야했다.
2. 으휴 또 무한루프
3. 두번째 테스트 케이스 카드3개합 중에 497없음ㅋ -> 잘못 접근함
3-1. 그냥 전범위 다 순회돌림
4. 중간에 확인용 print 다시 확인하고 제출하기^^
5. 어렵게 생각해서 실패한 케이스
'''