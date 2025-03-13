# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = self.rec(n)[k-1]
        return self.rec(n)[k-1]
    def rec(self, n):
        if n == 1:
            return "0"
        ans = self.rec(n-1)
        return ans + "1" + self.reverseInvert(ans) 
    def reverseInvert(sffelf, x):
        x = list(x)
        for i in range(len(x)):
            if x[i] == "0":
                x[i] = "1"
            else:
                x[i] = "0"
        x = list(reversed(x))
        return "".join(x)
        