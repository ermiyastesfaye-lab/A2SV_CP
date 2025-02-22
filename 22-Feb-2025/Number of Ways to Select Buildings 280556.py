# Problem: Number of Ways to Select Buildings - https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix = []
        ans1 = 0
        ans2 = 0
        summ = 0
        for j in s:
            summ += int(j)
            prefix.append(summ)
        for i, val in enumerate(prefix):
            left0 = i - val + 1
            left1 = val
            right1 = prefix[-1] - val
            right0 = len(prefix) - i - right1 - 1
            if int(s[i]) == 1:
                ans1 += left0 * right0
            else:
                ans2 += left1 * right1
        

        return ans1 + ans2
