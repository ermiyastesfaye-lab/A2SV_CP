# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def prefix(k):
            new = [0]*(len(nums)+1)
            for i in range(k):
                left, right, val = queries[i][0], queries[i][1], queries[i][2]
                new[left] += val
                new[right+1] -= val
            for i in range(1, len(new)):
                new[i]+=new[i-1]
            for i in range(len(nums)):
                if new[i] < nums[i]:
                    return False
            return True
        if nums.count(0) == len(nums):
            return 0
        left, right = 1, len(queries)
        if not prefix(right):
            return -1
        ans = 0
        while left <= right:
            mid = (left + right)//2
            if not prefix(mid):
                left = mid+1
            else:
                ans = mid
                right = mid-1
        return ans

            





