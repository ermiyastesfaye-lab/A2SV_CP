# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

def symmetrization(ques):
    n = len(ques)
    operations = 0
    for i in range(n):
        for j in range(n):
            ones, zero = 0, 0
            options = [(i, j), (j, n-1-i), (n-1-i, n-1-j), (n-1-j, i)]
            for nr, nc in options:
                #print(nc, nr, i, j)
              
                if 0<=nr<n and 0<= nc < n and ques[nr][nc] == '1':
                    ones+=1
                elif 0<=nr<n and 0<= nc < n and ques[nr][nc] == '0':
                    zero+=1
            operations += min(ones, zero)
    return operations // 4

t = int(input())

for _ in range(t):
    ques = []
    row = int(input())
    for i in range(row):
        rows = list(input())
        ques.append(rows)
    print(symmetrization(ques))
