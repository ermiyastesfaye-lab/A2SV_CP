# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

import sys
import math
from collections import Counter, defaultdict, deque

inputTaker = sys.stdin.readline

def inp(): return int(inputTaker())
def linp(): return list(map(int, inputTaker().split()))
def sinp(): return inputTaker().strip()
def minp(): return map(int, inputTaker().split())

def solve(lst):
    cnt = defaultdict(int)
    for j in range(1, len(lst)):
        if j != len(lst)-1:
            for k in range(j+1, len(lst)):
                if lst[k][0] == lst[j][1]:
                    if lst[j][0] not in cnt:
                        cnt[lst[j][0]] = 0
                    break
            else:
                cnt[lst[j][0]]+=1
        if j == len(lst)-1:
            cnt[lst[j][0]]+=1
    val = list(cnt.values())
    for m in val:
        if m < 3:
            return "No"
    return "Yes"
def main():
    t = inp()
    lst = [[] for i in range(t)]
    for i in range(t-1):
        tr = inp()
        lst[i+1].append(tr)
        lst[i+1].append(i+2)
    lst[0].append(lst[1][0])
    print(solve(lst))

if __name__ == "__main__":
    main()