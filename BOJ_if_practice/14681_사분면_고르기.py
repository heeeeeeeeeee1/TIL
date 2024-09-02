x = int(input())
y = int(input())

if x > 0 and y > 0:
    Quadrant = 1
elif x < 0 and y > 0:
    Quadrant = 2
elif x < 0 and y < 0:
    Quadrant = 3
else:
    Quadrant = 4

print(Quadrant)