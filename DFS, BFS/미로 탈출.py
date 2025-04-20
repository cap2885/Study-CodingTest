from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 맵을 벗어난 경우 무시
                continue
            if graph[nx][ny] == 0: # 괴물있는 부분 무시
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))


