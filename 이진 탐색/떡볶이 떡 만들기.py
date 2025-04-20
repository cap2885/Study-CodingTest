n, m = map(int, input().split())
a = list(map(int, input().split()))

x = list(range(max(a) + 1))

def binary_search(array, start, end):
    if start > end:
        return mid
    mid = (start + end) // 2
    sum_cut = 0
    for i in a:
        if i > array[mid]:
            sum_cut = sum_cut + (i - array[mid])
    if sum_cut == m:
        return mid
    if sum_cut > m:
        return binary_search(array, mid + 1, end)
    elif sum_cut < m:
        return binary_search(array, start, mid - 1)

result = binary_search(x, 0, max(a))
print(result)
