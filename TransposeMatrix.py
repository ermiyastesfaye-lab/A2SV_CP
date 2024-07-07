class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix[0])):
            res = []
            for row in matrix:
                res.append(row[i])
            ans.append(res)
        return ans
