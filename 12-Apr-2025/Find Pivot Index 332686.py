# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            prefix_sum[i] = summ
        for i in range(len(prefix_sum)-1):
            sum1 = prefix_sum[i-1]
            sum2 = prefix_sum[-2] - prefix_sum[i]
            if sum1 == sum2:
                return i
        return -1 


        


