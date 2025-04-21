def make_map(i):
    array = i
    X_cnt = array.count('X')
    O_cnt = array.count('O')
    # 리스트 컴프리핸션으로 2차원 리스트 초기화
    gameMap = [[0] * 3 for _ in range(3)] 
    cnt = 0
    for i in range(3):
        for j in range(3): 
            gameMap[i][j] = array[cnt]
            cnt += 1
    
    return gameMap, X_cnt, O_cnt, array

def inspect(i):
    gameMap, X_cnt, O_cnt, array = make_map(i)
    if abs(X_cnt - O_cnt) > 1:
        return print("invalid")
    if array.count('.') == 0:
        return print("valid")
    for i in range(3):
        X_cnt = gameMap[i].count('X')
        O_cnt = gameMap[i].count('O')
        if X_cnt == 3 or O_cnt == 3:
            return print("valid")
    for j in range(3):
        # 각 행(t)에서 j번째 열의 값을 가져오는 리스트 컴프리핸션
        col = [t[j] for t in gameMap]
        X_cnt = col.count('X')
        O_cnt = col.count('O')
        if X_cnt == 3 or O_cnt == 3:
            return print("valid")
        
    return print("valid")

gameMap = []
while True:
    line = input()
    if line == 'end':
        break
    gameMap.append(list(line))

for i in gameMap:
    inspect(i)
