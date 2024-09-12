'''
* '개발자 장고' 유튜브 - 3.백트래킹 참고
1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문여부 확인)
- 재귀함수에서 M개를 선택할경우 print

2. 시간복잡도
- N! > 가능(문제에서 최대 8. 팩토리얼 10까지는 되니까)
cf)
- N^N : 중복이 가능, N = 8까지 가능(최대 2억이 넘지 않으려면)
- N! : 중복이 불가. N = 10까지 가능

3. 자료구조
- 결과값 저장 int[]
- 방문여부 체크 bool[]
'''
import sys
input = sys.stdin.readline  # 입출력 빠르게

# 1 ~ N까지 자연수 중 중복없이 M개 고르기
N, M = map(int,input().split())

result = []
check = [False] * (N+1) # 인덱스 맞추기 위한 N+1개


def recur(num):
    if num == M:    # M이 되면 리턴(종료 조건)
        print(' '.join(map(str, result)))   # 결과값(result)을 공백으로 이어서 출력. join은 문자열 메서드
        return
    for i in range(1,N+1):  # 1부터 N까지의 자연수
        if check[i] == False:   # 방문하지 않았다면
            check[i] = True     # 방문 표시하고
            result.append(i)    # 결과리스트에 추가
            recur(num+1)
            check[i] = False
            result.pop()

recur(0)

'''
리뷰
1. 재귀 알듯말듯하다.
'''