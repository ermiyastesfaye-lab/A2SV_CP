# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        def bs(nums, left, right):
            if left > right:
                return -1
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return bs(nums, left, mid-1)
            else:
                return bs(nums, mid+1, right)
        return bs(nums, left, right)