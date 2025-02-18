# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        curr_sum = 0
        ans = 0

        for num in nums:
            curr_sum += num
            if curr_sum - goal in dic:
                ans += dic[curr_sum - goal]
            dic[curr_sum] += 1

        return ans

        