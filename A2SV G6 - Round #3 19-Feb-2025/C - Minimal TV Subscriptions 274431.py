# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import defaultdict

def minimalTv(arr, d):
    left = 0
    window = defaultdict(int)
    for i in range(d):
        window[arr[i]]+=1
    min_sub = len(window)
    for right in range(d, len(arr)):
        window[arr[left]]-=1
        if window[arr[left]] == 0:
            del window[arr[left]]
        window[arr[right]]+=1
        left+=1
        min_sub = min(min_sub, len(window))
    return min_sub


t = int(input())
for _ in range(t):
    n , k, d = list(map(int, input().split()))
    arr =  list(map(int, input().split()))
    print(minimalTv(arr, d))