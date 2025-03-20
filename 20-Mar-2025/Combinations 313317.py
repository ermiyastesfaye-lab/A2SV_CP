# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int):
        temp = []
        ans = []
        def backtrack(start):
            if len(temp) == k:
                ans.append(temp[:])
                return
            for candidate in range(start+1, n + 1):
                temp.append(candidate)
                backtrack(candidate)
                temp.pop()
        backtrack(0)
        return ans
