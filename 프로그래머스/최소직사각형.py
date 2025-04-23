# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 알고리즘 고득점 kit - 완전탐색
def solution(sizes):
    answer = 0
    w = []
    h = []
    for i in sizes:
        w.append(max(i))
        h.append(min(i))
    w_max = max(w)
    h_max = max(h)
    answer = w_max * h_max
    return answer