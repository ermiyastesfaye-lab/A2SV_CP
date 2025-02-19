# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        dic = Counter(s)
        ans = 0
        left = 0
        for right in range(len(s)-1):
            count1 = s[:right+1].count('1')
            count0 = s[:right+1].count('0')
            ans = max(ans, count0 + dic['1'] - count1)
        return ans
