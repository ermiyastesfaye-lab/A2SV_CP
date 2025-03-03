# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left = 0
        for right in range(2, len(nums)):
            if nums[right] + nums[right-1] > nums[left]:
                return nums[right] + nums[right-1] + nums[left]
            left+=1
        return 0









