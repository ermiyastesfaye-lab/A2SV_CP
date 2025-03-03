# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        maxx = 0
        if nums[0] == 0 and len(nums) > 1:
            return False
        while i < len(nums)-1:
            maxx = max(maxx, i + nums[i])
            if i + nums[i] >= len(nums) - 1:
                return True
            if nums[i] == 0 and maxx <= i:
                return False
            i+=1
        return True

            