# 문제의 점수는 그 문제까지 연속된 O의 개수

T = int(input())

for tc in range(T): # 테스트 케이스 수 만큼 반복. 테스트 케이스 출력 필요X
    OX = input()

    total = 0 # O가 연속적으로 있을 때 누적합
    point = 0 # O일 때의 점수
    for i in range(len(OX)):
        if OX[i] == 'O':
            point += 1
            total += point

        elif OX[i] == 'X':
            point = 0

    print(total)