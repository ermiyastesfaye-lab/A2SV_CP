# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

def bomb(ques, row, col):
    for i in range(len(ques)):
        for j in range(len(ques[i])):
            if ques[i][j] != '*':
                if not corner(ques, i, j, row, col):
                    return "NO"
    return "YES"

def corner(ques, n, m, row, col):
    dxn = [(-1, -1), (1, 1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]
    count = 0
    for x, y in dxn:
        x , y = n+x, m+y
        if 0 <= x < row and 0 <= y < col and ques[x][y] == "*":
            count+=1
    if ques[n][m] == '.':
        return count == 0
    elif ques[n][m].isdigit():
        return count == int(ques[n][m])
    return True
array = list(map(int, input().split()))
ques = []
for i in range(array[0]):
    arr = list(map(str, input()))
    ques.append(arr)
print(bomb(ques, array[0], array[1]))


        