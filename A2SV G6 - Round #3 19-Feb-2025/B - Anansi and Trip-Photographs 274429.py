# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

def anasi(arr, d):
    arr.sort()
    right = len(arr)//2
    left = 0
    while right < len(arr):
        if arr[right] - arr[left] < d:
            return "NO"
        left+=1
        right+=1
    return "YES"
    
    


t = int(input())
for _ in range(t):
    r, d = list(map(int, input().split()))
    arr =  list(map(int, input().split()))
    print(anasi(arr, d))