# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        range_sum = n *(n+1)//2
        arr_sum = sum(nums)
        return range_sum - arr_sum


