# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
def arrayTransformation(array):
    ans  = float('inf')
    arr_counter = Counter(array)
    lst = []
    for values in arr_counter.values():
        lst.append(values)
    
    lst.sort()
    total = sum(lst)
    left_sum = 0
    right_sum = 0
    for i in range(len(lst)):
        removals = 0
        if i > 0:
            left_sum+=lst[i-1]
        right_sum = total - (left_sum + lst[i])
        right_number = len(lst)-(i+1)
        removals =  left_sum + right_sum - (lst[i]*(right_number))
        ans = min(ans, removals)
    return ans

t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    print(arrayTransformation(array))
