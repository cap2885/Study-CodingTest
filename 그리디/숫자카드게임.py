n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    minNum = min(data)
    if minNum > result :
        result = minNum

print(result)
