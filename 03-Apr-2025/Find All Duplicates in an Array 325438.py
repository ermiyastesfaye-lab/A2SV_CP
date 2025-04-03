# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        def cycleSort(nums):
            seeker = 0
            while seeker < len(nums):
                holder = nums[seeker]-1
                if nums[holder]!= nums[seeker]:
                    nums[holder], nums[seeker] = nums[seeker], nums[holder]
                else:
                    if holder != seeker:
                        ans.append(nums[holder])
                    seeker += 1
            return sorted(list(set(ans)))
        return cycleSort(nums)
    
        