# 1. 0,1전환 함수 만들기
def switch(a):  # 1에서 입력받은 값 빼면 0은 1로, 1은 0으로
    a = 1 - a
    return a

T = int(input())
for tc in range(1,T+1):
    bit = [0] + list(map(int,input()))    # 메모리 원래 값
    # print(bit)

    # 2. empty에서 bit 모양으로 만들기
    empty = [0] * (len(bit))  # 1번째 누르면 1번 이후로 다 덮어 씌워야 하므로

    cnt = 0
    for i in range(1,len(bit)):         # 인덱스 0은 사용안할거
        if empty[i] != bit[i]:          # 채워나가는 빈배열과 입력받은(만들어야 하는) 값 다르면 01전환
            cnt += 1                    # 스위치 눌렀으면 cnt +1
            for k in range(i,len(bit)):   # 그 위치 기준으로 배열 끝까지 다 스위치 누르기
                empty[k] = switch(empty[k])


    # 출력 전 인덱스 주의
    # 1부터 출력해야됨
    print(f'#{tc} {cnt}')

'''
리뷰
1. for k in range(len(bit)): 이부분 잘못된건데 pass됨. cnt 출력문제라 pass 나왔을 뿐. 배열 출력하는 문제 나왔으면 틀렸을 문제
-> for k in range(i,len(bit)):로 수정함.
'''