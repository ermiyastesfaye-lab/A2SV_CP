# Problem: F - The Last Problem - https://codeforces.com/gym/591928/problem/F

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

summ = 0
for i in range(n):
    summ += a[i] * b[i]

rev = 0
for center in range(n):
    left, right = center-1, center+1
    temp = 0
    while left >= 0  and right < n:
        temp += a[left]*b[right] + a[right]*b[left] - a[left] * b[left] - a[right] * b[right]
        rev = max(rev, temp)
        left -= 1
        right += 1

for center in range(n-1):
    left, right = center, center+1
    temp = 0
    while left >= 0  and right < n:
        temp += a[left]*b[right] + a[right]*b[left] - a[left] * b[left] - a[right] * b[right]
        rev = max(rev, temp)
        left -= 1
        right += 1
print(summ + rev)

    