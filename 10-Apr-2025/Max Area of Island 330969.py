# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction  = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0
        def inBound(row, col):
            return (0<= row < len(grid)) and (0 <= col < len(grid[0]))
        def dfs(row, col):
            if grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            ans = 1
            for rowC, colC in direction:
                nRow = row + rowC
                nCol = col + colC
                if inBound(nRow, nCol):
                    ans += dfs(nRow, nCol)
            return ans
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = dfs(i, j)
                    maxArea = max(maxArea, ans)
        return maxArea





        