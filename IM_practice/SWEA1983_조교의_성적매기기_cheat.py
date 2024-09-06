# 못 풀어서 블로그 참고함

# 1. 학생 10명 각각의 총점 구하기
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split()) # N: 학생수, K: 알고싶은 학생 번호

    # 평점 기준 10개. 인덱스는 0 ~ 9
    standard = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

    total_list = []
    for _ in range(N): # 학생 수 만큼 반복
        middle, final, task = map(int, input().split())
        total = middle*0.35 + final*0.45 + task*0.2 # 총점 구하기
        total_list.append(total)    # 각각의 총점을 total_list에 담기
    # print(total_list)

    # 2. K번째 학생의 성적 기억하기
    score = total_list[K-1]
    # print(score)

    # 3. 내림차순 정렬
    # sort()는 원본 데이터가 정렬된다
    total_list.sort(reverse=True)
    # print(total_list)

    # 4. 학생수는 10의 배수로 주어지고, 평점은 N/10비율로 부여 가능
    div = N//10

    # K번째 학생의 성적(score)에 해당하는, 정렬된 total_list의 인덱스를 구한 후 div로 나눠주면 standard의 인덱스와 맞아 떨어진다.
    # (index 메서드는 값을 넣으면 인덱스를 찾아준다.)
    standard_idx = total_list.index(score) // div
    # 이렇게 나눠주면 30명일때 정렬된 리스트에서 0~2번째 학생은 standard_idx 0, 3~5번째 학생은 standard_idx 1, ~ , 27~29번째 학생은 standard_idx 9
    # standard = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']의 0 ~ 9인덱스에 N//10 만큼씩 매칭된다.

    # 인덱스를 이용해 평점 기준(standard)과 매칭한다.
    print(f'#{tc} {standard[standard_idx]}')

'''
리뷰
1. 하루종일 잡고 있었는데 어떻게 학생 인덱스와 성적, 평점을 연결시켜서 찾아야 할지 모르겠다. 코드를 못짜겠음
2. N/10만큼씩 동일하게 부여되는 부분도 코딩하지 못함
3. 다시 한번 생각해보려고 했으나 그래도 모르겠어서 블로그 참고함
4. 내장함수, 메서드도 자주 사용해야 문제 풀 때 쓸 수 있을듯... 사용하면 쉽게 푸는데 쓸 줄 몰라서 못씀
5.
    # 학생들의 총점과 순서(진짜 인덱스+1)
    # info = list(enumerate(total_list,1))  # enumerate는 시작점을 설정할 수 있다.
    # print(info)    # 튜플형태로 묶임
    #
    # print(info[0][1])  # [0]이면 각 학생의 번호와 성적 튜플. [i][1]은 성적

    # print(total_list)
    # total_list2 = sorted(total_list,reverse=True)   # 내림차순
    # print(total_list2)
    #
    # standard = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    #
    # # 일단 정렬한 리스트에 점수 부여해보자
    # for i in range(N):
    #     total_list2[i:i+N//10] = standard[i]
'''
