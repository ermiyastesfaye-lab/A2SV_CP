# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        dic = defaultdict(int)
        ans = ""
        for i in s:
            dic[i]+=1
        k = dic["1"]
        while k > 1:
            ans+="1"
            k-=1
        j = dic["0"]
        while j > 0:
            ans += "0"
            j -= 1
        ans += "1"
        return ans

