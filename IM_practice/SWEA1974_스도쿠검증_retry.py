def row_check(arr):
    for lst in arr:
        if len(set(lst)) == 9:
            result = 1
        else:
            result = 0
            break
    return result


def col_check(arr):
    arr2 = list(map(list, zip(*arr)))
    for lst in arr2:
        if len(set(lst)) == 9:
            result = 1
        else:
            result =  0
            break
    return result


def mini3by3(arr):
    for r in range(0,9,3):
        for c in range(0,9,3):
            lst = arr[r][c:c+3] + arr[r+1][c:c+3] + arr[r+2][c:c+3]
            if len(set(lst)) == 9:
                result = 1
            else:
                result = 0
                break
        if result == 0:
            break
    return result

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)] # 스도쿠 배열

    if row_check(arr) == 1 and col_check(arr) == 1 and mini3by3(arr) == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

'''
리뷰
1. 함수만들어서 해봤는데 return으로 어떻게 받아야 될지 모르겠음
1-1. 그래서 출력값 다르게 나왔다가 result에 1이나 0 할당하고 result를 return하는걸로 바꿔서 pass함
2. 문어박사 아이디어로 풀었는데 코드는 다름ㅋㅋ
'''