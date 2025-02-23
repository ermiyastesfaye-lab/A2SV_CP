# Problem: Number of Submatrices That Sum to Target - https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix)
        prefix = [[0] * (len(matrix[0])) for _ in range(len(matrix))]
        for i in range(len(prefix)):
            for j in range(len(prefix[i])):
                prefix[i][j] = matrix[i][j]
                if i - 1 >= 0:
                    prefix[i][j] += prefix[i - 1][j]
                if j - 1 >= 0:
                    prefix[i][j] += prefix[i][j - 1]
                if i - 1 >= 0 and j - 1 >= 0:
                    prefix[i][j] -= prefix[i - 1][j - 1]
        ans = 0

        for i in range(len(matrix[0])):
            for j in range(i, len(matrix[0])):
                dic = defaultdict(int)
                dic[0] = 1
                summ = 0
                for k in range(len(matrix)):
                    summ = prefix[k][j]
                    if i > 0:
                        summ -= prefix[k][i - 1]
                    if summ - target in dic:
                        ans += dic[summ - target]
                    dic[summ] += 1
        return ans
