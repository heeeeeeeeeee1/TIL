# a = [1,3,4,6,9]
# print(a.index(6))

# 1. 학생 10명 각각의 총점 구하기
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split()) # N: 학생수, K: 알고싶은 학생 번호

    total_list = []
    for _ in range(N): # 학생 수 만큼 반복
        middle, final, task = map(int, input().split())
        total = middle*0.35 + final*0.45 + task*0.2 # 총점 구하기
        total_list.append(total)    # 각각의 총점을 total_list에 담기

    print(total_list)
    total_list2 = sorted(total_list,reverse=True)   # 내림차순
    print(total_list2)

    standard = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

    # 일단 정렬한 리스트에 점수 부여해보자
    for i in range(N):
        total_list2[i:i+N//10] = standard[i]

    # .index 쓰면 되나