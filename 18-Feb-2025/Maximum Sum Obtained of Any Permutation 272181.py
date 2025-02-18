# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0] * (len(nums) + 1)
        nums.sort(reverse=True)
        for j in requests:
            prefix[j[0]] += 1
            prefix[j[1] + 1] -= 1

        summ = 0
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        
        prefix.sort(reverse=True)
        k = 0
        ans = 0
        while k < len(nums) and prefix[k] != 0:
            ans += nums[k] * prefix[k]
            k += 1
        return ans %(10**9 + 7)


        