# 회문검사 함수 -> 최대 길이 반환
def pal(arr,N):
    max_pal = 0
    for r in range(N):
        for length in range(N,0,-1):   # 회문 길의 범위를 정해서 그 길이에 해당하는 회문을 찾는다. 1개짜리도 회문임. 제일 길면 길이가 100(N)이겠지
            for c in range(N-length):   # length for문 범위를 역순으로 하면 긴 것부터 찾아서 금방 끝나긴 하겠네
                if arr[r][c:c+length] == arr[r][c:c+length][::-1]:  # 뒤집어서 회문검사///범위 확인 필요
                    if max_pal < length:  # 지금 구한 회문의 길이가 max_pal보다 길면
                        max_pal = length  # 갱신
    return max_pal

T = 10
for t in range(1,T+1):
    tc = int(input())   # 아마 이렇게 받아야?

    N = 100             # 100 x 100
    arr = [list(input()) for _ in range(N)]

    # 전치행렬
    arr_t = list(map(list,zip(*arr)))

    # 가로, 세로 회문 중 최대 길이 출력
    result = max(pal(arr,N),pal(arr_t,N))

    print(f'#{tc} {result}')


'''
리뷰
1. 왜 이렇게 하면 안되는지 정확히 모르겠다.
def pal(arr,N):
    max_pal = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c:] == arr[r][N-1:c-1:-1]:  # 뒤집어서 회문검사///범위 확인 필요
                if max_pal < len(arr[r][c:]):  # 지금 구한 회문의 길이가 max_pal보다 길면
                    max_pal = len(arr[r][c:])  # 갱신
    return max_pal
1-1. ㅇ ㅏ 내가 잘못생각하고 있었다^^; 위 코드처럼 하면 기준위치부터 끝까지 vs 끝에서부터 기준위치까지를 비교하는거라 중간에 있는 회문은 검사 불가능함
2. 이 문제는 전체 테스트케이스 변수로 출력하면 fail 뜬다.
'''