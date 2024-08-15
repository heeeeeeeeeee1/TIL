# 가장 많은 카드에 적힌 숫자(0~9), 그 숫자가 적힌 카드가 몇장인지 출력
# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 카드 장수 N
    N = int(input())

    # N개의 숫자 ai(cards)가 여백없이 주어짐(0으로 시작할 수도 있음)
    cards = list(map(int, input()))

    # 각 숫자가 몇장씩 있는지 기록할 리스트 생성
    # 8이 3장이면 인덱스 8번 위치에 3 기록. COUNTS[8] = 3
    # 카드에 적힌 숫자는 0 ~ 9이므로 10칸의 리스트 생성
    COUNTS = [0] * 10   # 아니... 처음에 이걸 왜 9칸으로 했냐...

    # 가장 많은 숫자 카운트
    for i in range(N): # i: 인덱스, N: 카드 장수
        COUNTS[cards[i]] += 1
    # print(COUNTS)   # [1, 1, 1, 0, 0, 0, 0, 1, 1, 0]

    # 가장 많은 카드 장수
    max_cnt = max(COUNTS)   # 최댓값 미리 구하지 않아도 아래에서 순회하면서 한번에 처리 가능

    # 가장 많은 카드의 '숫자': max_cnt의 인덱스(num)
    max_num = 0
    for num in range(len(COUNTS)):  # num은 인덱스(즉, 카드에 적힌 숫자)
        if COUNTS[num] == max_cnt:  # max_cnt가 위치한 COUNTS배열의 num인덱스를 찾아라
            # if max_num < num:     # 카드 장수 max_cnt가 같은게 여러개이면, 적힌 숫자(num)가 큰 쪽 출력/// < 나 <= 나 출력은 똑같네?
            # if max_num <= num:      # = 조건 없어도 pass는 됨... 어차피 작은 번호부터 순회돼서 그런듯
            max_num = num       # 최대 장수의 숫자(인덱스)보다 방금 조건에 충족한 인덱스가 더 크다면 갱신. 위의 조건 없이 이것만 해도 될듯? 작은 수부터 순회하고 갱신되니까?
    print(f'#{tc} {max_num} {max_cnt}')
