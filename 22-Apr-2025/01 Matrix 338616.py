# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def inbound(row, col):
            return (0<=row<len(mat)) and (0<=col<len(mat[0]))
        n, m = len(mat), len(mat[0])
        temp = n * m
        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = temp
        while queue:
            row, col = queue.popleft()
            for i, j in directions:
                nR = row + i
                nC = col + j
                if inbound(nR, nC) and mat[nR][nC] > mat[row][col]+1:
                    queue.append((nR, nC))
                    mat[nR][nC] = mat[row][col]+1
    
        return mat


