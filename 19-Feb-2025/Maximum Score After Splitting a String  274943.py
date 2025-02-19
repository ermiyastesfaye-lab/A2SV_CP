# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        dic = {'1': s.count('1')}
        ans = 0
        new = ''
        for right in range(len(s)-1):
            new += s[right]
            count1 =new.count('1')
            count0 = new.count('0')
            ans = max(ans, count0 + dic['1'] - count1)
        return ans
