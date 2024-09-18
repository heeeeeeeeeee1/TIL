remains = []
for _ in range(10):
    n = int(input())
    remains.append(n % 42)

print(len(set(remains)))