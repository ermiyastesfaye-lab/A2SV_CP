class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}':'{', ']':'['}
        for i in range(len(s)):
            if s[i] in mapping:
                if stack:
                    top = stack.pop()
                    if top != mapping[s[i]]:
                        return False
                else:
                    return False
            else:
                stack.append(s[i])
        return not stack
