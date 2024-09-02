
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    carrots = list(map(int,input().split()))

    max_cnt = 0             # 연속으로 커지는 당근의 갯수는 최대 얼마?
    cnt = 1                 # 당근의 크기가 연속적으로 커지는 경우 1씩 증가
    for i in range(N-1):    # 0 ~ N-2까지
        # 순회하며 오름차순인지 확인(당근의 크기가 커지는지)
        if carrots[i] < carrots[i+1]:
            cnt += 1    # 왜 1 2 3 4 5 일때 여기까지 안가지; -> cnt 초기값을 0으로 해놔서인듯...
            if max_cnt < cnt:
                max_cnt = cnt   # 그냥 오름차순 당근 하나 셀때마다 최댓값갱신. 이어지는 부분 최대한 순회하고 최댓값 갱신하려면 else에서 최댓값 갱신해야할듯?
        else:           # carrots[i] > carrots[i+1]
            cnt = 1     # 오름차순이 아니라면 구간의 최소 길이는 1
            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')

'''
리뷰
1. 또 똑같아. 조건문 생각을 못해
1-1. D1인데 이렇게 오래 걸릴일이야?
2. if carrots[i] < carrots[i+1]:
IndexError: list index out of range
2-1. 분명히 설계할때 적어놨는데 옮겨 적지도 못함
3. 첫번째 테스트케이스에서 cnt가 5여야 하는데 4이길래 디버깅해봤더니 대소비교하고 아래로 안내려감
3-1. 그런데 그냥 내가 생각했던 로직대로면 비교하고 횟수 증가하는거라 그 길이를 생각하려면 cnt 초기값이 1이어야 함
'''