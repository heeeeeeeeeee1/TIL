T = 10
for tc in range(1,T+1):
    dump = int(input())
    boxes = list(map(int,input().split()))

    # 주어진 평탄화 횟수대로 작업 후 가장 최고점과 최저점의 높이 차 구하기
    # dump 반복될 때마다
    for i in range(dump):
        boxes.sort()                # 오름차순 정렬 후
        boxes[-1] = boxes[-1] - 1   # 가장 높은 곳[-1]에 -1
        boxes[0] = boxes[0] + 1     # 가장 낮은 곳[0]에 +1
        # dump 총 횟수 이전에 모든 평탄화가 끝나면 이때의 높이차는 0 또는 1
        if len(set(boxes)) == 0 or len(set(boxes)) == 1:
            print(f'#{tc} {boxes[-1] - boxes[0]}')
        else:
            continue

    # dump 종료 후 최고점과 최저점 높이 차 출력
    boxes.sort()
    print(f'#{tc} {boxes[-1] - boxes[0]}')

'''
리뷰
1. 처음 이 문제 봤을 때는 건드리지도 못했던것 같은데
2. sort, set 사용하니까 쉽게 풀었다. 20분 걸림
3. 예전에 풀이 설명 들었던 기억이 남아있어서 풀 수 있었다.
'''