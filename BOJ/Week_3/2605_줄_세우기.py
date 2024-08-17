N = int(input())    # 학생수
picked_num = list(map(int,input().split())) # [0, 1, 1, 3, 2]
students = [n for n in range(1, N+1)]       # [1, 2, 3, 4, 5]


for i in range(N):          # N-1까지 순회
    n = picked_num[i]       # 왼쪽으로(앞으로) 이동할 칸수
    t = students[i]         # 학생 번호
    for j in range(i, i-n, -1):  # 해당 학생 위치 변경하고 나머지 학생 밀어내기
        students[j] = students[j-1] # i-1이 i위치로 이동(밀어내기)
    students[i-n] = t # 해당 학생 번호 따로 기억해놨다가 밀어낸 맨 앞으로 이동

print(*students)