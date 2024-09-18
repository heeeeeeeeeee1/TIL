A = int(input())
B = int(input())
C = int(input())

cal = str(A * B * C)

for i in range(10):
    print(cal.count(str(i)))
