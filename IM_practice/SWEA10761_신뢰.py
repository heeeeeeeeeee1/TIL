# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    work, *res = input().split() # 4 B 2 O 1 O 2 B 4
    # print(work, res)
    pre_robot = ''  # 여긴 왜 노란줄이죠
    pre_distance = 0
    time = 0
    # 로봇 B, O의 이전 위치 저장(시작위치 1)
    now_BO = [1] * 2  # [0]: B가 이전에 있었던 위치, [1]: O가 이전에 있었던 위치
    # [,] 이렇게도 되나요 -> no

    for r in range(int(work)):
        robot = res[r*2]
        pos = int(res[r*2+1])   # 아직 문자 -> 정수
        # print(robot, pos)

        # 로봇의 실제 이동위치는 |(이전 위치- 현재 위치)|
        if robot == 'B':  # 현재 robot이 B라면
            distance = abs(now_BO[0] - pos)  # 이렇게 해줘야 실제로 간 거리로 계산함
        else:             # 'O'라면
            distance = abs(now_BO[1] - pos)

        # A. 이전 작업자와 현재작업자가 다를 경우
        # 작업정보를 현재작업자로 갱신
        if pre_robot != robot:
            # 1. 이전 작업자가 나보다 더 많거나 같이 이동했을 경우 -> 현재 작업자는 대기하다가 버튼만 누르면 됨
            if pre_distance >= distance: # distance는 robot이 가야하는 `위치`이다. 실제로 이동한 거리가 아니다.
                # real_distance?: BO에 저장된 이전 위치 정보에서 현재 위치 빼고 절댓값 씌우기
                time += 1
                # 이전 작업자(`현재 작업자`가 이전 작업자가 됨) 정보, 이동거리 저장(버튼 누른 후 저장)
                pre_robot = robot
                pre_distance = 1    # 이동 완료해서 대기 후 버튼 누르기 때문

                # 현재 위치 갱신
                if robot == 'B':
                    now_BO[0] = pos
                else:
                    now_BO[1] = pos

            # 2. 이전 작업자가 나보다 적게 이동했을 경우 -> 현재 작업자는 남은거리를 이동 후 버튼 누르기
            else:       # pre_distance < distance
                time += (distance - pre_distance + 1)   # 남은 거리: 현재 작업자 거리 - 이전 작업자 거리
                pre_robot = robot   # 버튼 누르기 +1????
                pre_distance = distance - pre_distance + 1

                # 현재 위치 갱신
                if robot == 'B':
                    now_BO[0] = pos
                else:
                    now_BO[1] = pos

        # B. 이전 작업자가 나일 경우(이전작업자==현재작업자)
        else: # pre_robot == robot
            # 1. 이동거리를 이전에 작업정보에 누적합
            time += (distance + 1)  # +1 : 버튼 누르기
            pre_robot = robot
            pre_distance += (distance + 1)

            # 현재 위치 갱신
            if robot == 'B':
                now_BO[0] = pos
            else:
                now_BO[1] = pos


    print(f'#{tc} {time}')

'''
리뷰
1. ㅎ ㅏ......
'''