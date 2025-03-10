# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict


n = int(input())
tot = []
dic = defaultdict(int)
for _ in range(n):
    arr = list(map(int, input().split()))
    tot.append(arr)
for i in tot:
    dic[i[0]]+=1
    dic[i[1]]-=1
dic = dict(sorted(dic.items()))
lst1 = list(dic.keys())
lst2 = list(dic.values())
for i in range(1, len(lst2)):
    lst2[i] += lst2[i - 1]
idx = lst2.index(max(lst2))
print(lst1[idx], lst2[idx])









