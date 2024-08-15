# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 숫자
    N = int(input())
    div = [2, 3, 5, 7, 11]
    result = []

    for i in div:
        cnt = 0               # 나눈 횟수
        while N % i == 0:
            if N % i == 0:    # 해당 숫자로 나눴을 때 나머지가 0이면(나누어 떨어지면)
                cnt += 1      # 계속 나누고 나눈 횟수(cnt)를 갱신한다.
                N = N // i    # 나눠진 몫을 또 나눈다. 안나눠질떄까지
        result.append(cnt)    # 나눈 횟수 result에 저장
    # 안나눠지면 다음 수로 나눈다.
    # 나눈 횟수가 그 숫자의 지수이다.

    # print(f'#{tc}',end=' ')
    # print(*result)
    print(f'#{tc}',' '.join(map(str, result)))  # join 사용할 경우 문자형으로 변경 필요(join은 iterable 요소를 결합하는데 정수형은 해당되지 않기 때문)