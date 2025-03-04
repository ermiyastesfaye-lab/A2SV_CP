# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dic = defaultdict(int)
        ans = 0
        for i in s:
            dic[i]+=1
            if dic["L"] == dic["R"]:
                ans+=1
                dic["R"] = 0
                dic["L"] = 0
        return ans