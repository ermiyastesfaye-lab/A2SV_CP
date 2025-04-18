# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0,x
        while left <= right:
            mid = (left + right)//2
            if mid * mid <= x:
                left = mid+1
            else:
                right = mid - 1
        return right
        