# t시간 후의 개미 좌표 x, y 출력
w, h = map(int, input().split())    # w(가로. x축), h(세로, y축)
p, q = map(int, input().split())    # 초기위치 좌표값 p, q
t = int(input())    # 개미가 움직일 시간

# p는 x축 위에서, q는 y축 위에서 움직인다.
# w가 6인 경우 x는 [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]으로 움직인다.
# h가 4인 경우 y는 [0, 1, 2, 3, 4, 3, 2, 1]으로 움직인다.
# w, h에 따른 p, q 리스트 만들기

w_list = []
h_list = []

for i in range(w):          # 0 ~ 5 추가
    w_list.append(i)
for j in range(w, 0, -1):   # 6 ~ 1 추가
    w_list.append(j)

for i in range(h):          # 0 ~ 3 추가
    h_list.append(i)
for j in range(h, 0, -1):   # 4 ~ 1 추가
    h_list.append(j)

# 초기 p(q)값 + 움직인 시간 t(1시간당 t만큼 이동)을
# 전체 길이 2w(2h)로 나눈 나머지 값을 인덱스로 한다.
# x, y가 움직이는 주기가 2w, 2h여서 사용하는 것 같은데...
p_result = w_list[(p+t) % (2*w)]
q_result = h_list[(q+t) % (2*h)]

print(f'{p_result} {q_result}')

'''
리뷰
1. 서칭함(서칭해도 잘 모르겠음^^)
2. 점화식(수학식) 세울 생각? 당연히 못했음
3. 왜 왕복 거리로 나눈 '나머지'를 사용해야하는지 모르겠음
4. range 역 범위 또 헷갈림(어디서부터 어디까지인지)_len 사용시 range(len(list)-1, -1, -1)
5. p, q 그대로 쓰긴했는데 비슷하게 생겨서 오타까지 고려하면 다른 변수 사용하는게 나을듯
6. 아 문제에서 반사되는 부분을 이해 잘못해서 더 혼란했던거였네...
'''