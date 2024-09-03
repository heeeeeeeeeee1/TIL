while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    # 더이상 받을 값이 없으면 break
    except:
        break

'''
리뷰
1. 종료조건이 없는데 어떻게 하지?
1-1. -> a, b 나눠서 리스트 담고 리스트 길이 0되면(가져올 값 없으면) 종료되게?
1-2. -> 그렇게 복잡하게 푸는 문제 아닌것 같은데?
2. 서칭해봤더니 예외처리였다.
'''