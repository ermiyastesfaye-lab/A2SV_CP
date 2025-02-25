# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(int)
        dic[0] = 1
        prefix = 0
        ans = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix % k in dic:
                ans += dic[prefix % k]
                if ((prefix - nums[i]) % k) == (prefix % k):
                    ans -= 1
                    if ans > 0:
                        return True
                else:
                    return True
            dic[prefix % k] += 1
        return False
        
