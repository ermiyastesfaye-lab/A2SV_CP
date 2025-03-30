# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1
        while low <= high:
            mid = (low+high)//2
            print(matrix[mid][0])
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        if high < 0:
            return False
        
        left, right = 0, len(matrix[0])-1
        while left <= right:
            mid2 = (left + right)//2
            print(mid, mid2)
            if matrix[high][mid2] == target:
                return True
            elif matrix[high][mid2] < target:
                left = mid2 + 1
            else:
                right = mid2 - 1
        return False
        
