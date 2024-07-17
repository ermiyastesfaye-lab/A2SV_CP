class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        leng = len(grid)
        res =[[0]*(leng-2) for _ in range(leng-2)]
        for i in range(leng-2):
            for j in range(leng-2):
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        res[i][j] = max(res[i][j], grid[row][col])
        return res
