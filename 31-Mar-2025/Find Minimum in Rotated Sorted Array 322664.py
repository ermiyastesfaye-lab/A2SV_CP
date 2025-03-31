# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        ans = nums[0]
        while left <= right:
            mid = (left + right)//2
            if nums[mid] >= ans:
                left = mid + 1
            else:
                ans = nums[mid]
                right = mid - 1
        return ans