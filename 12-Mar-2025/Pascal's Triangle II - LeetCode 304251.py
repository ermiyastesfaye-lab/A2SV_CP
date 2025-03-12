# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex + 1)
        seen = defaultdict(int)

    
        def rec(r, c):
            if (r, c) in seen:
                return seen[(r, c)]
            if not(r * c) or c == r:
                return 1
            seen[(r, c)] = rec(r - 1,  c - 1) + rec(r - 1, c)
            return seen[(r, c)]

        for c in range(1, len(ans) - 1):
            ans[c] = rec(rowIndex - 1, c - 1) + rec(rowIndex - 1, c)

        return ans

