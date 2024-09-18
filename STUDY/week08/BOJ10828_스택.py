N = int(input())

stack = []
for _ in range(N):
    command = input().split()
    # command는 리스트임
    # command[0]은 명령 command[1]이 존재할 경우 정수
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack:   # 스택이 차있으면
            print(stack.pop())
        else:       # 스택이 비어있으면
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:   # 스택이 차있으면
            print(0)
        else:       # 스택이 비어있으면
            print(1)
    elif command[0] == 'top':
        if stack:   # 스택이 차있으면
            print(stack[-1])
        else:       # 스택이 비어있으면
            print(-1)


'''
리뷰
1. input값의 개수가 다르면 어떻게 하더라
2. 제일 처음엔 input을 리스트로 받아서 따로 저장했다가 stack에 옮기려고 했는데
2-1. 그럴 필요 없잖아...바로 처리하면되는데 또 복잡하게 생각하네
3. 그냥 단순구현이잖아!
4. python3으로 했더니 시간초과, pypy3으로 했더니 통과
'''