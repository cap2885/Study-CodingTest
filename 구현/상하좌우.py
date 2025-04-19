# 시뮬레이션
n = int(input())
plan = list(map(str, input().split()))

x = 1
y = 1

for i in plan :
    if i == "R" :
        if y < n:
            y += 1
    elif i == "U":
        if x > 1:
            x -= 1
    elif i == "D":
        if x < n:
            x += 1
    else:
        if y > 1:
            y -= 1

print(x, y)
