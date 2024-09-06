# 1. 0,1 전환 스위치 함수 만들기
def switch(a):  # 값을 넣으면 값을 반환
    if a == 1:
        a = 0
    else:
        a = 1
    return a


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))

    # 2. before[i]가 after[i]와 같지 않으면 스위치 누르기
    # 3. 스위치 누를때 마다 cnt +1
    cnt = 0
    for i in range(N):  # 인덱스 상관있나? 배수로 스위치 누르는거 아니어서 상관없을듯
        if before[i] != after[i]:
            cnt += 1
            for j in range(i, N):
                before[j] = switch(before[j])   # 아 끝까지 다눌려야되넼

    print(f'#{tc} {cnt}')



'''
리뷰
1. 스위치를 누를 때 전 범위 다 눌러야 한다는 점을 설계할 때 빼놓음
2. 스위치 함수 만들어 놓고 switch(before[j]) 이렇게 호출만해서 실제 before 리스트에 반영이 안됐었음
'''