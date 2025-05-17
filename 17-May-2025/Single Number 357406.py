# Problem: Single Number - https://leetcode.com/problems/single-number/

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res