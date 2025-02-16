# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        min_sum = 0
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                diff = abs(summ - target)
                if diff == 0:
                    return target
                if summ > target:
                    right-=1
                elif summ < target:
                    left+=1
                if diff < closest:
                    min_sum = summ
                    closest = min(closest, diff)
        return min_sum
                