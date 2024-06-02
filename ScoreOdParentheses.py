class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = []
        for i in s:
            if i == '(':
                stack.append(score)
                score = 0
            else:
                score= stack.pop() + max(2*score, 1)
        return score
