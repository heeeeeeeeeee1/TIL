T = int(input())    # 테스트 케이스
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    result = 0                      # 일치하지 않으면 0

    # 풀이 1
    # for s2 in range(M-N+1):         # M-N까지 순회하면 됨. 이 범위 넘어가면 str1이 str2에 있을 수 없음
    #     if str1 == str2[s2:s2+N]:   # str1과 str2의 일부가 일치하면 1
    #         result = 1
    #         break

    # 풀이 2
    for i in range(M-N+1):  # str2
        for j in range(N):  # str1
            if str1[j] != str2[i+j]:    # str2에 str1이 없다면
                break                   # 그대로 result = 0이겠지
        else:
            result = 1                  # str2에 str1이 있다면 1
            break                       # 겹치는거 한번이라도 확인했으면 그만 돌아도 되니까 break

    print(f'#{tc} {result}')

'''
리뷰
1. in 안쓰고 구성하려다 보니 복잡하게 생각했음(문자 하나씩 비교하고 일치하면 다음 값 이어서 비교하고, 다른면 str2 인덱스 이동하는 방식으로 생각함)
2. 인공지능 도움받고 보니 생각보다 간단하게 풀 수 있는 문제였다.
3. 슬라이싱으로 조건문에 넣어서 순회하는 방법 처음 써봄(다른 사람들이 쓰는거 보기만 함)
4. result=0으로 기본 설정 해놓고 조건 충족하면 1로 바뀌게 하니까 코드가 더 간단해졌다.
4-1. 이 생각을 못하고 하나하나 조건문으로 넣으려고 했음(1일때와 0일때)
'''