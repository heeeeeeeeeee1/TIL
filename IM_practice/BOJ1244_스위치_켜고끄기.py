# 1. 스위치 01전환 함수 만들기
def switch(a):
    if a == 1:
        a = 0
    else:
        a = 1
    return a

N = int(input())    # 스위치 개수
lst = [0] + list(map(int,input().split()))  # 인덱스 번호 맞추기 위한 [0] 추가
students = int(input()) # 학생수
# print(lst)

# 성별, 스위치번호(학생이 받은 수)
for _ in range(students):
    sex, num = map(int,input().split())

    if sex == 1:    # 2. 남자일 경우
        for i in range(num,len(lst),num):   # 받은수(num)의 배수에 해당하는 숫자 스위치 누르기
            lst[i] = switch(lst[i])
    else:           # 3. 여자일 경우(2인경우)
        # for i in range(num, len(lst)):    # 0번 인덱스는 사용안할거니까
        lst[num] = switch(lst[num])         # 일단 기준위치 누르고
        for j in range(1,N):
        # for j in range(1, len(lst) // 2): # 이렇게 해도 pass 됨
            # 범위 넘어가면 그만
            if num-j <= 0 or num+j > N:
                break
            if lst[num-j] == lst[num+j]:    # 같으면 i도 누르고 같은애들도 누르고
                lst[num-j] = switch(lst[num-j])
                lst[num+j] = switch(lst[num+j])

            # 같지 않으면 그만
            else:
                break

# 바뀐 스위치 배열 출력
# 출력형태 지키기^^
# result = lst[1:]

for k in range(1,len(lst)):
    print(lst[k], end = ' ')
    if k % 20 == 0: # k(스위치 번호)가 20의 배수이면
        print()     # 줄 바꿈

# for x in range(0,len(result),20):
#     print(*result[x:x+20],end='')
#     print()

'''
리뷰
1. 여학생 조건 SWEA 돌뒤집기 게임2 생각하고 i, j 이중 for문으로 돌렸다가 num만 필요하다는 것을 인지하고 수정
2. 출력형태 이렇게 안돼? 아 줄 바꿈이 안됐넼
for x in range(0,len(result),20):
    print(*result[x:x+20])
3. 출력형태도 출력형태인데
4. 인덱스 에러 계속 나서 17번 제출함 ㅡㅡ
4-1. 주어진 스위치 개수 N개와 [0] 추가후 len(lst)의 차이로 인해 for j in range(1,N): 이부분에서 오류난 것 같은데
4-2. 나는 N대신 len(lst)로 해도 된다고 생각했음. 인덱스 8까지 가도 된다고 생각함...
4-3. 어차피 범위 조건에서 걸리는거 아니야? 음... 아닌가봐..
'''

