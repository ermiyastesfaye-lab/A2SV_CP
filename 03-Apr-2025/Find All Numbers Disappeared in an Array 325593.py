# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seeker = 0
       
        while seeker < len(nums):

            holder = nums[seeker]-1

            if nums[holder] != nums[seeker]:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]

            else:
               
                seeker+=1

        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans
