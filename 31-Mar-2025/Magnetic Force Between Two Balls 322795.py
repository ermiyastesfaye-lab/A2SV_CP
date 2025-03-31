# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, nums: List[int], m: int) -> int:
        nums.sort()
        def validate(mid):
            lp = nums[0]
            cnt = 1
            for i in range(1, len(nums)):
                if nums[i] - lp >= mid:
                    lp = nums[i]
                    cnt += 1
            return cnt >= m
        ans = 0
        low, high = 1, nums[-1] - nums[0]
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if validate(mid):
                print('ans')
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        