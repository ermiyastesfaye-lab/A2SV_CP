# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        black = 0
        ans = 0
        for i in s:
            if i == '1':
                black+=1
            else:
                ans+=black
        return ans
            
        