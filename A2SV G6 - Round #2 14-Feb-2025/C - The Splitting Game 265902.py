# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

def splitGame(s, n):
    summ  = 0
    lst1 = [0]*n
    lst2 = [0]*n
    dist_char = set()
    for i in range(len(s)):
        dist_char.add(s[i])
        lst1[i] = len(dist_char)
    dist_char.clear()
    for j in range(len(s)-1, -1, -1):
        dist_char.add(s[j])
        lst2[j] = len(dist_char)
    for k in range(len(s)-1):
        summ = max(summ, lst1[k]+lst2[k+1])
    return summ

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    print(splitGame(s, n))