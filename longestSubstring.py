class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = {}
        res = 0 
        for right in range(len(s)):
            while s[right] in count:
                count.pop(s[left]) 
                left += 1
            count[s[right]] = 1
            res = max(res, right - left + 1)
        return res
