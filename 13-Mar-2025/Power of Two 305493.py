# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return self.rec(n)
    def rec(self, n):
        if n == 1:
            return True
        if n%2 != 0:
            return False
        return self.rec(n//2)
        
        