# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        def backtrack(i):
            if len(temp) == len(nums):
                ans.append(temp[:])
                return
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    backtrack(temp)
                    temp.pop()
        backtrack(temp)
        return ans


        