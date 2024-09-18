N = int(input())
try:
    temp = []   # 설탕배달 할 수 있는 조합의 봉지 수 저장 후 min 구하기
    x = 0
    while True:
        y = (N - 3 * x) / 5
        if (str(y)[-1]) == '0':
            if type(int(y)) == int:
                # print(y)
                temp.append(int(x + y))
                x += 1
                if x > (N // 3):
                    break
        else:
            x += 1
            if x > (N // 3):
                break
    print(min(temp))

except:
    print(-1)
'''
리뷰
1. y를 계산하면 실수형으로 나오는데 이중에서 4.0, 6.0 이런식으로 나온 y만 정수형으로 변환해야하는데
1-1. int 사용하면 실수형에서 소수점 버리면서 다 정수형으로 변환시켜서 어떻게 해야하지 하다가
1-2. 소수점 첫째자리가 0인 값들만 고려했음
2. 시간복잡도? 그런거 고려 못해 ㅜ 다 append하면 시간초과 나올 것 같기도...
3. 통과하긴했는데 다른 사람들 풀이 보니까 나 또 어렵게 생각했잖아^^?
'''