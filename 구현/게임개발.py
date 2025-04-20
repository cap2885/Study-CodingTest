
n, m = map(int, input().split())

# 가본 장소 체크하기 위해 맵을 0으로 초기화하고, 현재 위치 1로 설정.
d = [[0] * m for _ in range(n)]
x, y, see = map(int, input().split())
d[x][y] = 1

# 현재 맵 정보 가져오기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 순서대로
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn_left() :
    global see
    see -= 1
    if see == -1:
        see = 3

count = 1  
turn_cnt = 0
while True:
    turn_left()
    check_x = x + dx[see]
    check_y = y + dy[see]

    togo = array[check_x][check_y]
    if togo == 0 and d[check_x][check_y] == 0:
        x += dx[see]
        y += dy[see]
        d[check_x][check_y] = 1

        count += 1
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1
    
    if turn_cnt == 4:
        check_x = x - dx[see]
        check_y = y - dy[see]

        if array[check_x][check_y] == 0:
            x = check_x
            y = check_y
        else:
            break
        turn_cnt = 0

print(count)