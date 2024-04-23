def is_possible_to_obtain_single_element(n, arr):
    arr.sort()
    if n ==1:
        return 'YES'
    if max(arr) - min(arr) <= 1:
        return 'YES'
    else:
        v = []
        for i in range(1, n):
            dif = abs(arr[i] - arr[i-1])
            v.append(dif)
        v.sort(reverse=True)
        if v[0] > 1:
            return "NO"
        else:
            return "YES"




    

ans = []
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    ans.append(is_possible_to_obtain_single_element(n, arr))

for result in ans:
    print(result)
