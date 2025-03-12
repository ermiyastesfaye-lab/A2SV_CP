# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

t = int(input())

for _ in range(t):
  white_space = input()
  n, k = list(map(int, input().split()))
  indices = list(map(int, input().split()))
  temps = list(map(int, input().split()))
  arr1 = [float('inf')] * n
  arr2 = [float('inf')] * n
  
  for i, num in enumerate(indices):
    arr1[num - 1] = temps[i]
    arr2[num - 1] = temps[i]

  for i in range(1, n):
    if arr1[i] > arr1[i - 1] + 1:
      arr1[i] = arr1[i - 1] + 1
      
  for i in range(n - 2, -1, -1):
    if arr2[i] > arr2[i + 1] + 1:
      arr2[i] = arr2[i + 1] + 1
      
  ans = []
  for x, y in zip(arr1, arr2):
    ans.append(min(x, y))
    
  print(*ans)