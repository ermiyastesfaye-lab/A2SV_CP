# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for i in s:
            if i == '(':
                stack.append(ans)
                ans = 0
            else:
                ans = stack.pop() + max(2*ans, 1)
        return ans