N = int(input())    # N번째 영화 제목

# 666이 나오면 cnt 증가
# cnt가 입력받은 N과 같으면 그때의 666이 들어간 값(target) 출력
target = 0  # 증가시키면서 666 찾을 대상
cnt = 0
while True:
    if '666' in str(target):    # in 사용하려면 문자여야 하니까
        cnt += 1
        if N == cnt:            # 입력받은 N과 666이 들어있는 수의 순번이 같으면
            break
    target += 1
print(target)


'''
리뷰
1. 5666에서 6660, 6661, 6662 ~ 6666이런식으로 넘어가는데 어떻게 구현하지?라고 생각해서 코딩을 못했는데
1-1. 이것도 대충 구글링 해보니까 내가 또 어렵게 생각하고 있었음^^;
'''