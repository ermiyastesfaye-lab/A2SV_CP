# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n= int(input())
arr =list(map(int, input().split()))
arr.sort()
prefix = [0] * (n + 1)
if len(arr) % 2 != 0:
    mid = arr[len(arr)//2]
else:
    dif = (arr[len(arr)//2] + (arr[(len(arr)//2)-1]))/2
    mid = dif
ans = 0
if len(arr) == 1:
    print(arr[0])
for i in range(len(arr)):
    if mid < arr[i]:
        print(arr[i-1])
        break
