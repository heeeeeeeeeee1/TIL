T = 10
for tc in range(1,T+1):
    N = int(input())    # 회문의 길이
    arr = [list(input()) for _ in range(8)]
    # print(arr)

    # 행 우선 순회
    pal = 0 # 회문 카운팅
    for r in range(8):
        for c in range(8-N+1):  # 전체 길이가 8이고 - 회문의 길이(N) 까지만 가야됨
            cnt = 0
            for k in range(N//2):   # 회문의 길이를 반 나눈 만큼 반복
                if arr[r][c+k] == arr[r][c+N-1-k]:  # 양끝에서부터 중앙으로 비교
                    cnt += 2    # 일치하면 cnt +1
                else:
                    break
            # k 순회 종료 후
            if N % 2 == 1:      # 홀수라면
                if (cnt + 1) == N:  # cnt에 1 더한후 N과 비교
                    pal += 1    # 회문 맞으니까 +1
            else:                # 짝수일 경우
                if cnt == N:    # 문자 하나씩 비교했을 때 센 cnt 누적합과 N(회문의 길이)이 같다면
                    pal += 1    # 회문 맞으니까 +1

    # 열 우선 순회
    # pal = 0 # 회문 카운팅
    for c in range(8):
        for r in range(8-N+1):
            cnt = 0
            for k in range(N//2):   # 회문의 길이를 반 나눈 만큼 반복
                if arr[r+k][c] == arr[r+N-1-k][c]:  # 양끝에서부터 중앙으로 비교
                    cnt += 2    # 일치하면 cnt +1
                else:
                    break
            # k 순회 종료 후
            if N % 2 == 1:      # 홀수라면
                if (cnt + 1) == N:  # cnt에 1 더한후 N과 비교
                    pal += 1    # 회문 맞으니까 +1
            else:                # 짝수일 경우
                if cnt == N:    # 문자 하나씩 비교했을 때 센 cnt 누적합과 N(회문의 길이)이 같다면
                    pal += 1    # 회문 맞으니까 +1

    print(f'#{tc} {pal}')


'''
리뷰
1. 행, 열 순회 코드 복사해서 붙여넣을거면 범위, r, c 잘 확인하기
2. 테스트 케이스 썼는지, 테스트 케이스 여러개 순회하도록 만들어 놨는지 확인하기
3. 초기화 위치, 초기값 크기 확인
4. N을 회문의 길이로 입력받았는데 평소에 사용하던 N(전범위)이랑 혼용해서 출력값 이상하게 나옴^^;

'''