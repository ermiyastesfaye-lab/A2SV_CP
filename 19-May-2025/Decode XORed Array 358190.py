# Problem: Decode XORed Array - https://leetcode.com/problems/decode-xored-array/description/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        r = [first]
        for i in encoded:
            r.append(r[-1]^i)
        return r
        