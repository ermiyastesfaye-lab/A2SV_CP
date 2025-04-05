# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row  = len(mat)
        col = len(mat[0])
        maxx_val = -1
        ans = None
        cnt = 0
        for i in range(row):
            if maxx_val < sum(mat[i]):
                ans = [i, sum(mat[i])]
                maxx_val = sum(mat[i])
        return ans

        