n, m = map(int, input().split())
x, y, see = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

cnt = 1
# 북, 동, 남, 서 순서대로
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

if see == 0:
    togo = 3
else:
    togo = see - 1

# if togo