# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, nums: List[int]) -> int:
        left = 0
        right = nums[-1]
        while left <= right:
            mid = (left + right)//2
            idx = bisect_left(nums, mid)
            if len(nums)-idx >= mid:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans