# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        total = sum(nums)
        n = len(nums)
        left = 0
        for i in range(len(nums)):
            ans = ((total- left) - (nums[i] * (n - i))) + ((nums[i] * i) -  left)
            left+=nums[i]
            result[i] = ans
        return result