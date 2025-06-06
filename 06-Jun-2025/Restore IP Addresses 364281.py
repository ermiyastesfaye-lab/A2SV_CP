# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtrack(i, dots, curr):
            if dots == 4 and i == len(s):
                ans.append(curr[:-1])
                return
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i]!= '0'):
                    backtrack(j+1, dots+1, curr+s[i:j+1] + '.')
        
        backtrack(0, 0, "")
        return ans
