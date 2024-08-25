# 가로, 세로 중 가장 긴 회문 찾기
# 회문 찾기 함수1
# def is_pal(arr,leng):   # arr: 행렬, leng: 회문 길이
#     for lst in arr:     # 2차원 배열에서 리스트 한줄씩 가져오기
#         for i in range(0, N-leng+1):                    # N-leng까지 순회해야함
#             if lst[i:i+leng] == lst[i:i+leng][::-1]:    # 기준 위치부터 회문길이만큼의 값들이 뒤집은 것과 같다면
#                 return True                             # True 반환
#     return False        # 다 찾았는데 없다면 False
#
#
# T = 10
# for t in range(1, T+1):
#     tc = input()  # 의미없는 테스트 케이스
#     N = 100
#     arr1 = [input() for _ in range(N)]          # 정방향 행렬
#     arr2 = [''.join(x) for x in zip(* arr1)]    # 전치행렬
#
#     for leng in range(N,1,-1):  # leng: 회문의 길이. 가장 긴 회문 찾아야하니까 뒤에서부터 순회
#         if is_pal(arr1, leng) or is_pal(arr2, leng):  # 가로 혹은 세로 회문이라면
#             break
#     print(f'#{tc} {leng}')

#----------------------------------------------------------------------------------------

# 회문 찾기 함수2
def is_pal_idx(arr,leng):
    for lst in arr:
        for i in range(0,N-leng+1):
            for j in range(leng//2):            # 양끝값씩 중앙으로 비교하면서 회문 검사
                if lst[i+j] != lst[i+leng-1-j]: # 비교값이 다르면(회문이 아니면)
                    break                       # 다음 시작위치로...
            else:                               # break 안한 경우 else로
                return True                     # 같은 줄(리스트) 순회 어디선가 회문 찾으면 True
    return False                                # 다 끝났는데 회문 못찾았으면 False


T = 10
for t in range(1, T + 1):
    tc = input()  # 의미없는 테스트 케이스
    N = 100
    arr1 = [input().strip() for _ in range(N)]  # 정방향 행렬
    arr2 = [''.join(x) for x in zip(*arr1)]  # 전치행렬

    for leng in range(N, 1, -1):  # leng: 회문의 길이. 가장 긴 회문 찾아야하니까 뒤에서부터 순회
        if is_pal_idx(arr1, leng) or is_pal_idx(arr2, leng):  # 가로 혹은 세로 회문이라면
            break
    print(f'#{tc} {leng}')
'''
리뷰
1. 설명을 참고해도 잘 모르겠다.
1-1. 함수 만들면 깔끔하다. 하지만 나혼자 이렇게까지 구성할 수 있을까?ㅜ
1-2. 전치행렬 처음 적용해봄. zip 처음써봄
2. zip 사용 못하는 경우엔 어떻게 하지?
3. for문안에 있는 테스트케이스 tc로 해야 pass...? 파이참에서 출력은 잘됐는데 SWEA에서는 오류나서 tc부분 수정했더니 pass됨
'''