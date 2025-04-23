# 알고리즘 고득점 kit - 해시
def solution(participant, completion):
    dict = {} 
    for i in participant: 
        if i in dict: 
            dict[i] += 1 
        else: 
            dict[i] = 1 
    for j in completion: 
        dict[j] -= 1 
        if dict[j] == 0:
            del dict[j]
    answer = list(dict.keys())
    return answer[0]