# 1000명의 수학 성적 중 최빈수 구하기
# 각 학생의 점수는 0 ~ 100이하
# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 각 테스트 케이스 번호 또 줌
    _ = int(input())

    # 학생 1000명의 점수
    scores = list(map(int,input().split()))

    # 최빈수 구하기
    cnt_list = [0] * 101    # 0 ~ 100점 빈도수 체크할 리스트 생성

    # 가져온 점수가 cnt_list의 인덱스로, 헤당하는 인덱스에 점수가 몇개인지 누적 카운팅
    for score in scores:
        cnt_list[score] += 1

    max_score = 0  # 최빈 점수(인덱스)
    max_cnt = 0    # 최빈수의 개수(최빈수가 몇개 있는지)
    for idx in range(len(cnt_list)):
        if max_cnt <= cnt_list[idx]: # 최빈수가 여러개이면 가장 큰 점수 출력
            max_cnt = cnt_list[idx]  # 최빈수의 개수 갱신
            max_score = idx          # 그때의 인덱스(최빈 개수에 해당하는 최대 점수)

    print(f'#{tc} {max_score}')


#### 아 머리 안굴러가네... 쉬운건데.._240815