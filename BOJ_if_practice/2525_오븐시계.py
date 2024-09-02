hour, minute = map(int, input().split()) # 현재시간(시, 분)
cooking = int(input()) # 요리하는데 필요한 시간

# 시간 계산 방법대로 진행
time = minute + cooking
# 분끼리 더한 값(time=minute+cooking)이 60이상이면
if time >= 60:
    new_hour = hour + (time//60)
    new_minute = time % 60
# 60으로 나눈 몫 만큼 hour에 더해준다.
# 이 때의 분은 더한값(time)을 60으로 나눈 나머지
else:   # time < 60라면
    new_hour = hour
    new_minute = time # 그대로 더해줌

# 그런데 계산 후의 시간(new_hour)이 24이상이라면
# 24를 빼줘야함
if new_hour >= 24:
    new_hour = new_hour -24

print(f'{new_hour} {new_minute}')
