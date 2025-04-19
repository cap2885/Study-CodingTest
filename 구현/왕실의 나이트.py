location = input()
x = int(ord(location[0])) - int(ord('a')) + 1
y = int(location[1])

steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]
cnt = 0
for step in steps:
    dx = x + step[0]
    dy = y + step[1]
    if (1 <= dx <= 8) & (1 <= dy <= 8) :
        cnt += 1 

print(cnt)