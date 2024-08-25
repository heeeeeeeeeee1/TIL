# 0초부터 붕어빵 만들기 시작, M초동안 K개 붕어빵
# time//M * K : 손님이 방문했을 때(time) 만들어져 있는 붕어빵 개수

T = int(input())    # 테스트 케이스
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    customer = list(map(int, input().split()))

    customer.sort()                 # 손님이 도착하는 순서대로 정렬
    result = 'Possible'             # 한 명이라도 불가능하면 Impossible이기 때문에 이렇게 설정하는 것이 최적화
    cnt = 0                         # 손님 수
    for time in customer:           # 손님 도착 시간 가져오기
        cnt += 1                    # 손님 왔으니 cnt +1
        if time//M * K < cnt:       # 만들어진 붕어빵이 손님 수보다 작으면
            result = 'Impossible'   # 붕어빵 제공 불가
            break

    print(f'#{tc} {result}')

'''
리뷰
1. 코딩 못해서 유튜브 참고. 만들어지는 붕어빵과 손님 수로 식을 세울 생각을 못함(식을 봐도 잘 이해안됨)
2. 만족하는 경우(time//M * K >= cnt)를 if로 두면 불만족 하는 경우가 될 때까지 순회해야하므로
2-1. 불만족 하는 경우 반복문이 종료되는 조건문으로 작성하는게 좋음
3. 위와 같이(1-1) 작성 했을 때, 손님들이 도착하는 순서대로 정렬해주지 않으면 일부 테스트케이스 오답일 수 있음

cf.부분정답일 때 고려할 사항
입력이 모두 0이라면? 음수 섞여있으면? 모두 같은 값이라면? 모든 값이 최소, 최댓값이라면?
일부가 정렬안되어있으면? 모두 경계값이면?

'''