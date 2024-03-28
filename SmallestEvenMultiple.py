class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        startNumber = n
        while True:
            if (startNumber % n == 0 and startNumber %  2 == 0):
                break
            else:
                startNumber += 1
                continue
        return startNumber

answer = Solution()
print(answer.smallestEvenMultiple(5))
