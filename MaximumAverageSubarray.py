class Solution:
    def findMaxAverage(self, nums, k):
        current_sum = sum(nums[:k])
        max_ave = current_sum/k
        for i in range(len(nums)-k):
            current_sum = current_sum - nums[i] + nums[k+i]
            max_ave = max(max_ave, current_sum/k)
        return max_ave
