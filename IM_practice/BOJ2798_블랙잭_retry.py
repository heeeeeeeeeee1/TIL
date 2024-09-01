# 1. cards 정렬하기(해도되고 안해도될듯)
# 2. 하나 기준으로 잡고 나머지 숫자2개 조합 바꾸면서 합 구하기
# 3. 그 합이 M과 유사(M보다 작거나 같다)한지 확인
# 4. 가장 M과 유사한 값 출력

N, M = map(int, input().split())        # N: 카드 수, M: 딜러가 부르는 수(카드 3장의 합과 유사해야 하는 수)
cards = list(map(int,input().split()))  # 카드 입력

# 두개 뽑고 더해.근데 이렇게 할거면 자기자신 또 더하지 않게 범위 설정해야..?
max_val = 0
for i in range(N):                      # 범위 이렇게해도 백준 패스함
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = cards[i] + cards[j] + cards[k]
            if total <= M:              # 더한 값이 M보다 작고
                if max_val < total:     # 지금 더한값이 max_val보다 크다면
                    max_val = total     # 갱신

print(max_val)

# 범위 차이///각 범위는 풀이마다 조금씩 다름
max_val = 0                             # 카드는 다 양의 정수니까 0으로 초기값 설정
for i in range(N-2):                    # 3개 뽑으니까 i는 N-3까지
    for j in range(i+1, N-1):           # j는 N-2까지
        for k in range(j+1, N):
            total = cards[i] + cards[j] + cards[k]
            if total <= M:              # 더한 값이 M보다 작고
                if max_val < total:     # 지금 더한값이 max_val보다 크다면
                    max_val = total     # 갱신

print(max_val)

'''
리뷰
1. 시간초과로 다시 풀기
2. 다른 사람 풀이 대충 참고
3. 이렇게 풀리는 걸 왜 어렵게 푼거야?
4. 조건문 ㅡㅡ


'''