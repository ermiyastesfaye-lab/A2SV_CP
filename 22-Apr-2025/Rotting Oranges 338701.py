# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
            
        level = []
        fresh = time = 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    level.append((row, col))
                    
                elif grid[row][col] == 1:
                    fresh += 1
          
        while level:
            next_level = []
            
            for row, col in level:
                for dx, dy in directions:
                    x, y = row + dx, col + dy
                    
                    if inbound(x, y) and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        next_level.append((x, y))     
                        
            if next_level:
                time += 1
                 
            level = next_level
            
        return -1 if fresh else time