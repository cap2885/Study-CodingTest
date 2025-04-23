def solution(array, commands):
    answer = []
    for i in commands:
        q = i[0] - 1
        w = i[1]
        e = i[2]
        if (q + 1) == w:
            a = array[q]
            c = a
        else:
            a = array[q:w]
            b = sorted(a)
            c = b[e - 1]
        answer.append(c)

    return answer

# 정렬