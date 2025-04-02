# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0 1 2 3 5
        nums.sort()
        left, right = 0,len(nums)-1
        if nums[-1]+1==len(nums):
            return nums[-1]+1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] != mid:
                right = mid - 1
            else:
                left = mid + 1

        return left
                
            


