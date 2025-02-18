# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        ans = float('-inf')
        for num in nums:
            curr_sum += num
            if curr_sum > ans:
                ans = max(ans, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return ans



solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))