def solution(numbers, target):
    array = [0]

    cnt = 0
    for leaf in numbers:
        temp = []
        for leaves in array:
            temp.append(leaves + leaf)
            temp.append(leaves - leaf)
        
        array = temp
    answer = array.count(target)
    # for i in array:
    #     if i == target:
    #         cnt += 1
    return answer