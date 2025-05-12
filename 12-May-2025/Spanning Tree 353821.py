# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

import sys
import math
from collections import Counter, defaultdict, deque

inputTaker = sys.stdin.readline

def inp(): return int(inputTaker())
def linp(): return list(map(int, inputTaker().split()))
def sinp(): return inputTaker().strip()
def minp(): return map(int, inputTaker().split())

def solve():
    n, m = linp()
    lst = []
    for i in range(m):
        b, c, w = linp()
        lst.append((b, c, w))
    lst.sort(key=lambda x: x[2])
    root = [i for i in range(n + 1)]
    rank = [0] * (n+1)
    def find(x):
        if root[x] == x:
            return x
        val = find(root[x])
        root[x] = val
        return val
    def union(x, y):
        rootx = find(x)
        rooty = find(y)
        if(rootx != rooty):
            if rank[rootx] < rank[rooty]:
                root[rooty] = rootx
            elif rank[rooty] < rank[rootx]:
                root[rootx] = rooty
            else:
                root[rooty] = rootx
                rank[rootx] +=1
    ans = 0
    for b, c, w in lst:
        if find(b) != find(c):
            ans += w
            union(b, c)
    print(ans)


        
def main():
    t = 1 
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()