# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        window = 0
        left = 0
        flip = 0
        for right in range(n):
            if nums[right] == 0:
                flip+=1
            if flip > k:
                while nums[left] != 0:
                    left+=1
                flip-=1
                left+=1
            window = max(window, right - left + 1)
        return window

