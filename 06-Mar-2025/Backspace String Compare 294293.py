# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        i = 0
        j = 0
        while i < len(s) or j < len(t):
            if i < len(s):
                if s[i] == '#':
                    if stack1:
                        stack1.pop()
                else:
                    stack1.append(s[i])
                i+=1
            if j < len(t):
                if t[j] == '#':
                    if stack2:
                        stack2.pop()
                else:
                    stack2.append(t[j])
                j+=1
        return stack1 == stack2