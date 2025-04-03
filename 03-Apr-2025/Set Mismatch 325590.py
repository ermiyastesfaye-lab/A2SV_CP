# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seeker = 0
        ans = []
        dup = [-1, -1]
        while seeker < len(nums):

            holder = nums[seeker]-1

            if nums[holder] != nums[seeker]:
                if nums[holder] == dup[0]:
                    dup[1] = seeker
                nums[holder], nums[seeker] = nums[seeker], nums[holder]

            else:
                if holder!= seeker and not ans:
                    ans.append(nums[holder])
                    dup = [nums[holder], seeker]
               
                seeker+=1

        ans.append(dup[1]+1)
        return ans
        