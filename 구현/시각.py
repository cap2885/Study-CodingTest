n = int(input())

cnt = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            timeNow = str(i) + str(j) + str(k)          
            if '3' in timeNow:
                cnt += 1

print(cnt)
