def countSwaps(arr):
    last = len(arr) - 1
    sorted = False
    count = 0

    while not sorted:
        sorted = True
        for i in range(0, last):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
    
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {arr[0]}")
    print(f"Last Element: {arr[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
