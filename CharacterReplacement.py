class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = {}
        left = 0
        maxLen = 0
        maxCnt = 0

        for right in range(len(s)):
            ans[s[right]] = ans.get(s[right], 0) + 1
            maxCnt = max(maxCnt, ans[s[right]])

            if (right-left+1)-maxCnt > k:
                ans[s[left]]-=1
                left+=1 
            maxLen = max(maxLen, right-left+1)
        return maxLen
