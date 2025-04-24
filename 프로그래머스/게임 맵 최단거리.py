from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    queue = deque()
    # 상, 하, 좌, 우
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]
    
    def bfs(x, y):
        queue.append((x, y))
        while queue:   
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
    bfs(0, 0)
    answer = maps[n-1][m-1]
    if answer == 1 or answer == 0:
        real_answer = -1
    else:
        real_answer = answer
    return real_answer