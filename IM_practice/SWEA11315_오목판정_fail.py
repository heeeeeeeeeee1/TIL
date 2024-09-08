#
# 왜 4방향만 탐색하면 되지? 하지만 시험이었다면 난 8방향을 봤을거라 8방향 델타 만들거임
# 그런데 격자판이 5 초과 되는 크기일 때 이 방법으로 하면 오목 개수를 세는 경우 틀릴것 같은데? 계속 중복으로 개수 카운팅 돼서...
# 아 이 문제는 YES NO 판정이라 상관없네;
#
# 오목 판정 함수 만들기
# def omok(arr):
#     # 8방향 델타 만들기
#     dr = [-1, 0, 1, 1, 1, 0, -1, -1]
#     dc = [1, 1, 1, 0, -1, -1, -1, 0]
#
#     # 현재 위치가 돌이 있든 없든 상관없이
#     result = ''
#     for r in range(N):
#         for c in range(N):
#
#                 for k in range(8):
#                     cnt = 1
#                     for step in range(1,6):
#                         nr = r + dr[k] * step
#                         nc = c + dc[k] * step
#                         if 0 <= nr < N and 0 <= nc < N and arr[r][c] == 'o':
#                             if arr[nr][nc] == 'o':
#                                 cnt += 1
#                 if cnt >= 5:
#                     result = 'YES'
#                     break
#                 else:
#                     result = 'NO'
#         if result == 'YES':
#             break
#     return result
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())    # 오목판 크기 N x N
#     arr = [list(input()) for _ in range(N)] # 문자열 오목배열
#     print(f'#{tc} {omok(arr)}')
