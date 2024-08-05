def LessEqual(arr, n, k):
    arr.sort()
    if k == 0:
        if arr[0] > 1:
            return 1
        else:
            return -1
    if k == n:
        return arr[k-1]
    if arr[k-1] == arr[k]:
        return -1
    return arr[k-1]


inp = input()
arr = inp.split()
n = int(arr[0])
k = int(arr[1])
data = input()
lst = data.split()
lst = [int(ans) for ans in lst]

print(LessEqual(lst, n, k))
