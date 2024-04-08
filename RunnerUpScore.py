def runnerUp(n, arr):
    arr.sort()
    n = arr[len(arr)-1]
    for i in range(len(arr)-1, -1, -1):
        if arr[i] != n:
            return arr[i]
        continue


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(runnerUp(n, arr))
