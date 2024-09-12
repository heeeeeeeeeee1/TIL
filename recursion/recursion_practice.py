# 연습문제) 0 1 2 3 4 5 5 4 3 2 1 0 재귀 호출 이용하여 구현

def func(x):
    if x == 6:
        return
    print(x, end = '')
    func(x+1)
    print(x, end='')

func(0)


def func(x):
    # 1. 기저조건(종료조건)
    if x == 6:
        return

    # 후보군을 반복하면서
    # 2. 다음 재귀 호출 전
    print(x, end=' ')
    # 3. 재귀 호출 (현재 값에 무슨 수식을 적용해서 넘겨줄까 ?)
    func(x + 1)  # 다음 재귀 호출에서는 현재보다 x 값이 1이 커야한다.
    # 4. 호출하고 돌아왔을 때
    print(x, end=' ')

start = 0
func(start)
