class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        result = []
        left = 0
        right = 0
        lastIndex = {}
        for i, char in enumerate(s):
            lastIndex[char] = i
        for i, char in enumerate(s):
            right = max(right, lastIndex[char])
            if i == right:
                result.append(right - left+1)
                left = i+1
        
        return result
