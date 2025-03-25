# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right =len(nums)-1
        def lower_bound(nums, left, right):
            while left <= right:
                mid = (left + right)//2
                if target > nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            if 0<=left<=len(nums)-1 and nums[left] == target:
                return left
            else:
                return -1
    
        def upper_bound(nums, left, right):
                while left <= right:
                    mid = (left + right)//2
                    if target >= nums[mid]:
                        left = mid+1
                    else:
                        right = mid-1
                    print(right)
                if 0<=right<=len(nums)-1 and nums[right] == target:
                    return right
                else:
                    return -1

        leftL = lower_bound(nums, left, right)
        rightL = upper_bound(nums, left, right)
        return [leftL, rightL]
                