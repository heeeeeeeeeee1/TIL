# 스위치 수
N = int(input())    # light의 길이

# 스위치 상태. 1 ~ 8 번 인덱스 맞추기 위해 미리 0번 자리에 -1 추가
light = [-1] + list(map(int, input().split()))  # [-1, 0, 1, 0, 1, 0, 0, 0, 1]

# 학생수
student = int(input())

# 스위치 바꾸는 딕셔너리나 함수

# 성별 s, 받은 수 num
for stu in range(student):  # 학생 수 만큼 반복해야 입력 받겠지
    s, num = map(int, input().split())
    if s == 1:    # 남학생
        for i in range(1, N+1): # 1 ~ 8(N)까지
            if i % num == 0:    # num 배수 만큼 스위치 바꿔
                light[i] = 1 - light[i] # 원래가 1이면 0으로 바꾸고, 0이면 1로 바꿔

    # if s == 1:  # 남학생
    #     for i in range(num, N + 1, num):  # num의 배수마다 <- 이 코드가 더 효율적
    #         light[i] = 1 - light[i]       # 스위치 상태 반전

    elif s == 2:    # 여학생
        light[num] = 1 - light[num]  # 받은 그 수(중앙값)는 무조건 바꿈
        for j in range(N//2):
            if num + j > N or num - j < 1:        # 범위 넘어서면
                break                             # 멈춤
            elif light[num + j] == light[num - j]: # 좌우 같으면
                light[num + j] = 1 - light[num + j] # 스위치 끄기/켜기
                light[num - j] = 1 - light[num - j]
            else:       # 좌우 다르면
                break   # 멈춤

# 마지막 스위치까지 한 줄에 20개씩 출력
# 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력
for k in range(1, N+1):
    print(light[k], end = ' ')
    if k % 20 == 0: # k(스위치 번호)가 20의 배수이면
        print()     # 줄 바꿈