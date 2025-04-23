from collections import deque 
def solution(progresses, speeds):
    queue = deque(progresses) 
    result = [] 
    num = len(queue)
    while queue: 
        cnt = 0 
        for i in range(num): 
            queue[i] += speeds[i] 
        while queue and queue[0] >= 100:
            queue.popleft()
            speeds.pop(0)
            cnt += 1
            num -= 1

        if cnt > 0:
            result.append(cnt) 
    return result