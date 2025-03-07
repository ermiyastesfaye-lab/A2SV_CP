# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    for i in range(1, len(arr1)):
        arr1[i] += arr1[i-1]
    m = input()
    arr2 = list(map(int, input().split()))
    for j in range(1, len(arr2)):
        arr2[j] += arr2[j-1]
    res1 = max(arr1)
    res2 = max(arr2)
    ans = 0
    if res1 > 0:
        ans+= res1
    if res2 > 0:
        ans += res2
    print(ans)
    

