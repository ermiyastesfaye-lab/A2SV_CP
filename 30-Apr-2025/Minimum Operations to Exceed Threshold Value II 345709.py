# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        idx = 0
        for i in range(len(nums)):
            if nums[i] > k:
                idx = i
                break
        ans = 0
        while len(nums) >= 2:
            if nums[0] < k:
                ans+=1
                o = heapq.heappop(nums)
                f = heapq.heappop(nums)
                new = min(o, f)*2 + max(o, f)
                heapq.heappush(nums, new)
               
            else:
                
                break
        return ans
            


        