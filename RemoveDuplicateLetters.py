class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {ele: idx for idx, ele in enumerate(s)}
        stack = []
        for idx, ele in enumerate(s):
            if ele in stack:
                continue
            while stack and ele < stack[-1] and dic[stack[-1]] > idx:
                stack.pop()
            stack.append(ele)
        return "".join(stack) 
