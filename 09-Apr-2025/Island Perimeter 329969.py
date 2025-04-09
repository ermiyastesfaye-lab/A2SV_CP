# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ans = 0
        def inBound(row, col):
            return (0<=row<len(grid)) and (0<=col<len(grid[0]))
        def dfs(grid, row, col, visited):
            nonlocal ans
            visited[row][col] = True
            for rowC, colC in directions:
                nrow = row + rowC
                ncol = col + colC
                if not inBound(nrow, ncol) or  grid[nrow][ncol] == 0:
                    ans += 1
                elif inBound(nrow, ncol) and grid[nrow][ncol] == 1:
                    if not visited[nrow][ncol]:
                        dfs(grid, nrow, ncol, visited)
                    
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(grid, row, col, visited)
                    return ans

            

