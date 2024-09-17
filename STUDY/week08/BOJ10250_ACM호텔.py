# N을 H로 나눈 몫에서 1을 더하면 방 번호의 호수가 된다. 방번호 YYXX 중에서 XX
# N을 H로 나눈 나머지는 층수가 된다. 방번호 YYXX 중에서 YY

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:              # 나누어 떨어지면
        floor = str(H)
        number = str(N//H)
        if len(number) == 1:    # 한자리수라면 0붙여서 출력
            number = '0' + number
        print(floor+number)
    else:                       # 나머지가 있으면
        floor = str(N % H)
        number = str(N // H + 1)
        # 출력형태 맞추기
        if len(number) == 1:    # 한자리수라면 0붙여서 출력
            number = '0' + number
        print(floor+number)


'''
리뷰
1. 그림만 보고 배열인가 했다가 그냥 나눗셈이길래 쉽네? 했는데
2. 반례에 걸려서 일시정지 ㅎ
///1try///
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = str(N % H)
    number = str(N // H + 1)
    # 출력형태 맞추기
    if len(number) == 1:   # 한자리수라면 0붙여서 출력
        number = '0' + number
    print(floor+number)
2-1. N % H == 0(나누어 떨어질때) 값이 달라진다. 반례 질문게시판 참고함.
'''