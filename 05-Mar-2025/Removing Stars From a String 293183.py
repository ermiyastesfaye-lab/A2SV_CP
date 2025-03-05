# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i != '*':
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)