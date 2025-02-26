# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    maxx = max(arr)
    for i in range(len(arr)):
        if arr.count(maxx) > 1:
            if arr[i] == maxx:
                print(1, end=" ")
                continue
        elif arr.count(maxx) == 1:
            if arr[i] == maxx:
                print(0, end=" ")
                continue
        print(maxx - arr[i] + 1, end=" ")
    print()
    