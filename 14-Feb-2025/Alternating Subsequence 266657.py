# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

def alternatingSubsequence(arr, n):
    def sign(num):
        return num >= 0
    left = 0
    right = left
    ans = 0
    while right < len(arr):
        maxx = float('-inf')
        while right < len(arr) and sign(arr[right]) == sign(arr[left]):
            maxx = max(arr[right], maxx)
            right+=1
        ans+=maxx
        left = right
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(alternatingSubsequence(arr, n))