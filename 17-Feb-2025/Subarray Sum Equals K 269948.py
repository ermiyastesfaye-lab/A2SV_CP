# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        current = 0
        ans = 0
        
        for num in nums:
            current += num
            if current - k in dic:
                ans += dic[current - k]
            dic[current] += 1

        return ans