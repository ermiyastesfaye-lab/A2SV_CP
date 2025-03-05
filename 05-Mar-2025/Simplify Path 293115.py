# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for i in path:
            if not i or i == '.':
                continue
            if i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        ans = "/".join(stack)
        ans = '/' + ans
        return ans