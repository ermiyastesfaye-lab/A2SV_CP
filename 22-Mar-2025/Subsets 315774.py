# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        ans = [[]]
        def backtrack(temp, i):
            if i >= len(nums):
                return
            temp.append(nums[i])
            ans.append(temp[:])
            backtrack(temp, i+1)
            temp.pop()
            backtrack(temp, i+1)
        backtrack(temp, 0)
        return ans