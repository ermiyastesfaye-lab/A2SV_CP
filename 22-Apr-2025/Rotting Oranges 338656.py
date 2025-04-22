# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def inbound(row, col):
            return (0<=row<len(grid)) and (0<=col<len(grid[0]))
        n, m = len(grid), len(grid[0])
        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    grid[i][j] = 0
                elif grid[i][j] == 1:
                    grid[i][j] = -1
        ans = 0
        while queue:
            row, col = queue.popleft()
            if grid[row][col] == -2:
                grid[row][col] = 0
            for i, j in directions:
                nR = row + i
                nC = col + j
                if inbound(nR, nC) and grid[nR][nC] == -1:
                    grid[nR][nC] = grid[row][col]+1
                    ans = max(ans, grid[nR][nC])
                    queue.append((nR, nC))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    return -1

        return ans
                 








