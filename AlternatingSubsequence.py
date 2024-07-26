t = int(input())
 
for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
 
    total_sum = 0
    index = 0
 
    while index < n:
        subsequence = []
 
        if numbers[index] < 0:
            while index < n and numbers[index] < 0:
                subsequence.append(numbers[index])
                index += 1
        else:
            while index < n and numbers[index] > 0:
                subsequence.append(numbers[index])
                index += 1
 
        if subsequence:
            total_sum += max(subsequence)
 
    print(total_sum)
