T = int(input())
for i in range(1,T+1): # T만큼 반복
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')