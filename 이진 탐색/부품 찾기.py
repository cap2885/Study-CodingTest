a = int(input())
data_a = list(map(int, input().split()))
b = int(input())
data_b = list(map(int, input().split()))

data_a = sorted(data_a)

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
for i in range(b):
    result = binary_search(data_a, data_b[i], 0, a-1)
    if result == None:
        print("no", end = ' ')
    else:
        print("yes", end = ' ')
