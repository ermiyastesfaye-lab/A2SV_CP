# Problem: Grid Game - https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid):
        summ = sum(grid[0])
        summ2 = 0
        ans = float('inf')
        for i in range(len(grid[0])):
            summ -= grid[0][i]
            ans = min(ans, max(summ, summ2))
            summ2 += grid[1][i]
        
        return ans