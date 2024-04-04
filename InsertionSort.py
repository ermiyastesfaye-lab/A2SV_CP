def insertionSort1(n, arr):
    last = arr[-1]
    for i in range(n-2, -1, -1):
        if last < arr[i]:
            arr[i + 1] = arr[i]
            row1 = ' '.join(str(item) for item in arr)
            print(row1)
            if i == 0:
                arr[0] = last
                row1 = ' '.join(str(item) for item in arr)
                print(row1)
        else:
            arr[i + 1] = last
            row1 = ' '.join(str(item) for item in arr)
            print(row1)
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
