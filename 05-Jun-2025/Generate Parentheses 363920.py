# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = []
        def backtrack(op, cl):
            if op == cl == n:
                ans.append(''.join(temp))
                return
            if op < n:
                temp.append('(')
                backtrack(op+1, cl)
                temp.pop()
            if cl < op:
                temp.append(')')
                backtrack(op, cl+1)
                temp.pop()
        backtrack(0, 0)
        return ans
                


