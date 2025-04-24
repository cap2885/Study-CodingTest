from collections import deque
def solution(begin, target, words):
    def bfs():
        queue = deque()
        queue.append([begin, 0])
        while queue:
            now, step = queue.popleft()
            if now == target:
                return step
            for i in words:
                cnt = 0
                for j in range(len(now)):
                    if now[j] != i[j]:
                        cnt += 1
                if cnt == 1:
                    queue.append([i, step + 1])
    if target not in words:
        return 0
    answer = bfs()
    return answer