# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict


def longestSegment(arr, uniq):

    left = 0
    window = defaultdict(int)
    max_length = 0
    ans = [0, 0]

    for right in range(len(arr)):

        window[arr[right]]+=1
        count = len(window)

        while count > uniq:

            window[arr[left]]-=1

            if window[arr[left]] == 0:
                del window[arr[left]]

            left+=1
            count = len(window)
        if (right - left + 1) > max_length:
            ans = [left,right]
        max_length = max(max_length, right - left + 1)

    for i in ans:
        print(i+1, end=" ")

n, uniq = list(map(int, input().split()))
arr = list(map(int, input().split()))
longestSegment(arr, uniq)

