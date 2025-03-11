# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        return self.recursion(n)

            
    def recursion(self, n):
        if n < 5:
            return 0
        return n//5 + self.recursion(n//5)
        
