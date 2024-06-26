class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = n-1
        count = 0
        while left < right:
            if nums[left] + nums[right] < k:
                left+=1
            elif nums[left] + nums[right] > k:
                right-=1
            else:
                left+=1
                right-=1
                count+=1
        return count
