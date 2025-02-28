# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans1 = 0
        ans2 = float('inf')
        curr_sum1 = 0
        curr_sum2 = 0
        for right in range(len(nums)):
            curr_sum1 += nums[right]
            curr_sum2 += nums[right]
            ans1 = max(ans1, curr_sum1)
            ans2 = min(ans2, curr_sum2)
            if curr_sum1 < 0:
                curr_sum1 = 0
            if curr_sum2 > 0:
                curr_sum2 = 0
        print(ans1)
        print(ans2)
        return max(abs(ans1), abs(ans2))



