class Solution:
    def reverseString(self, s: List[str]) -> None:
        def revFunction(s, left=0, right=len(s)-1):
            if len(s)<=1:
                return s
            if left < right:
                s[left], s[right] = s[right], s[left]
                revFunction(s, left+1, right-1)
        revFunction(s)
