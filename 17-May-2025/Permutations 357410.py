# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def recursive(nums, mask=0, temp=[]):
            nonlocal ans
            if len(temp) == n:
                ans.append(temp)
            for i in range(len(nums)):
                bit = 1 << i
                if mask & bit:
                    continue
                recursive(nums, mask | bit, temp + [nums[i]])
        recursive(nums)
        return ans