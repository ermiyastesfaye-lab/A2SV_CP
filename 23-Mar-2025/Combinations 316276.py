# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int):
        ans = []
        temp = []
        def backtrack(i):
            if len(temp) == k:
                ans.append(temp[:])
                return
            if i> n:
                return
            temp.append(i)
            backtrack(i+1)
            temp.pop()
            backtrack(i+1)     
        backtrack(1)
        return ans       
