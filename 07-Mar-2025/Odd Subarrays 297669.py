# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    if arr == sorted(arr):
        print(0)
        continue
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            cnt += 1
            i+=2
        else:
            i+=1
    print(cnt)