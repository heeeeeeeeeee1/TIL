# 수학여행 참가 학생 수 N,한방에 배정될 수 있는 최대 인원 수 K
n, k = map(int,input().split())

student_lst = [] # 학생 각각의 튜플을 담을 리스트
for _ in range(n): # 참가 학생 수 만큼 반복
    student = tuple(map(int, input().split()))  # 성별 s, 학년 y 가진 각각의 student 생성
    student_lst.append(student)
# print(student_lst) # [(1, 1), (0, 1), (1, 1), (0, 2), (1, 2), (0, 2), (0, 3), (1, 3), (1, 4), (1, 3), (1, 3), (0, 6), (1, 5), (0, 5), (1, 5), (1, 6)]
# student를 튜플로 묶을지 리스트로 묶을지 고민했었는데 딕셔너리로 만들거면 key값에 리스트 못오니까 튜플로 만들어야되네


# 같은 것끼리 숫자 카운팅해서 딕셔너리?

student_dict = {}
# count = 0
# for student in student_lst:
#     if student not in student_dict: # 딕셔너리에 student 없으면 key로 추가하고 count 1
#         count += 1 # 숫자 증가
#         student_dict.update({student : count})  # 딕셔너리에 student는 key값으로 추가, count는 value로 추가
#     else: # 있으면 count += 1 하고 value 값 갱신
#         count += 1
#         student_dict[student] = count # 해당 student 튜플을 key 값으로 하는 value를 count로 갱신
# print(student_dict)

# 조건문 못쓰겠어서 인공지능 선생님 도움 받음^^ 괜히 어렵게 생각함; 바로 key value 넣으면 되는데
for student in student_lst:
    if student in student_dict: # 딕셔너리에 student 있으면
        student_dict[student] += 1 # key(student) value(학생수 누적합) 추가
    else: # 없으면
        student_dict[student] = 1  # key(student) value(학생수 1) 추가
# print(student_dict)


# values 메서드
all_values = list(student_dict.values()) # 각 성별, 학년 튜플에 해당하는 학생 수로 만든 리스트
result = 0
for v in all_values:
    int_value = int(v)
    if int_value <= k: # k이하일 경우 ex. k = 2
        room = 1 # 방은 1개 배정
        result += room
    elif int_value > k: # K 초과일 경우
        if int_value % k == 0: # k로 나눈 나머지가 0이면(즉, 나누어 떨어지면)
            room = int_value // k # 몫만큼 방 배정
            result += room
        else: # k로 나눴을 때 나머지가 발생하는 경우
            room = int_value // k + 1 # 몫 + 1(나머지 수용할 수 있는 방)
            result += room

print(result)