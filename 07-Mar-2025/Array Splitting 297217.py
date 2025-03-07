# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
new = []
if k == 1:
    print(arr[-1] - arr[0])
    exit()
for i in range(1, len(arr)):
    new.append(arr[i] - arr[i - 1])
new.sort()
largest = sum(new[-k+1:])
print(arr[-1] - arr[0] - largest)

    