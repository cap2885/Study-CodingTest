# 알고리즘 고득점 kit - 스택/큐
def solution(arr):
    stack = []
    cnt = 0
    for i in arr:
        if cnt == 0:
            stack.append(i)
            cnt += 1
            continue
        elif i == stack[-1]:
            pass
        else:
            stack.append(i)
    return stack