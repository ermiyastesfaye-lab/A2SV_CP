# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        direction_map = {
            1: [((0, -1), 1), ((0, 1), 1)],
            2: [((-1, 0), 2), ((1, 0), 2)],
            3: [((0, -1), 1), ((1, 0), 2)],
            4: [((0, 1), 1), ((1, 0), 2)],
            5: [((0, -1), 1), ((-1, 0), 2)],
            6: [((0, 1), 1), ((-1, 0), 2)],
        }
        

        compatible = {
            (0, -1): {1, 4, 6},
            (0, 1): {1, 3, 5},
            (-1, 0): {2, 3, 4},
            (1, 0): {2, 5, 6}
        }

        visited = [[False]*n for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            x, y = queue.popleft()
            if (x, y) == (m - 1, n - 1):
                return True

            for (dx, dy), _ in direction_map[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if grid[nx][ny] in compatible[(dx, dy)]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

        return False

        